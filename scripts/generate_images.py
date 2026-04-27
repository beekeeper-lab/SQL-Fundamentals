#!/usr/bin/env python3
"""Generate course illustrations.

Reads IMAGE-PLAN.md and generates each planned image. Skips images that
already exist unless --force is used.

Provider is chosen via the IMAGE-PLAN.md frontmatter:
    **Generator:** gemini-3-pro-image-preview          (default)
    **Generator:** openai-gpt-image-1.5                (OpenAI gpt-image-1.5)
    **Generator:** openai-gpt-image-2                  (OpenAI gpt-image-2; org verification required)
    **Quality:** high|medium|low                       (OpenAI only; default high)
    **Size:** 1536x1024|1024x1024|1024x1536           (OpenAI only; default 1536x1024)

When no `Generator:` line is set, Gemini is used (preserves prior behavior).

Style consistency rule: keep every course on one provider for the life of
the course. The frontmatter records the choice so future regenerations
match the original style.

API key lookup (each provider):
  1. <PROVIDER>_API_KEY environment variable
  2. <course>/.env file
  3. <course>/../.env file (parent Course_Material/.env)

Usage:
    uv run --with google-genai --with openai python scripts/generate_images.py
    ... --dry-run | --force | --filter module-01
    ... --generator openai-gpt-image-1.5  (override frontmatter)
"""

import json
import os
import re
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
IMAGES_DIR = ROOT / "images"
IMAGE_PLAN = ROOT / "IMAGE-PLAN.md"

GEMINI_MODEL = "gemini-3-pro-image-preview"
DEFAULT_OPENAI_MODEL = "gpt-image-1.5"

# API quota is 20 requests/minute/model. Target ~18/min for headroom.
MIN_INTERVAL_SECONDS = 60.0 / 18
MAX_RETRIES_ON_429 = 3


def _read_env_file(path, key):
    """Return the value of `key` from a `.env` file, or None."""
    if not path.exists():
        return None
    for line in path.read_text().splitlines():
        if line.startswith(f"{key}="):
            return line.split("=", 1)[1].strip().strip('"').strip("'")
    return None


def load_api_key(provider):
    """Find <PROVIDER>_API_KEY via env var, course .env, or parent .env."""
    env_key = "OPENAI_API_KEY" if provider == "openai" else "GEMINI_API_KEY"
    key = os.environ.get(env_key)
    if key:
        return key.strip()
    for candidate in (ROOT / ".env", ROOT.parent / ".env"):
        val = _read_env_file(candidate, env_key)
        if val:
            return val
    print(f"ERROR: {env_key} not found in environment or any .env file")
    print(f"  Checked: ${env_key}, {ROOT}/.env, {ROOT.parent}/.env")
    sys.exit(1)


def resolve_provider(defaults, override=None):
    """Return a provider config dict from frontmatter or CLI override.

    {
      'provider': 'gemini' | 'openai',
      'model':    str,                 # e.g. 'gpt-image-1.5'
      'quality':  str (openai only),
      'size':     str (openai only),
    }
    """
    raw = (override or defaults.get("generator") or "").lower().strip()
    if "openai" in raw or "gpt-image" in raw:
        m = re.search(r"gpt-image-[\d.]+", raw)
        model = m.group(0) if m else DEFAULT_OPENAI_MODEL
        return {
            "provider": "openai",
            "model": model,
            "quality": (defaults.get("quality") or "high").lower().strip(),
            "size": (defaults.get("size") or "1536x1024").strip(),
        }
    return {"provider": "gemini", "model": GEMINI_MODEL}


def parse_frontmatter(text):
    """Extract plan-level defaults from top-of-file **Key:** value lines."""
    defaults = {}
    keys = {
        "style": r"^\*\*Style:\*\*\s*(.+)$",
        "branding": r"^\*\*Branding:\*\*\s*(.+)$",
        "aspect_ratio": r"^\*\*Aspect ratio:\*\*\s*(.+)$",
        "background": r"^\*\*Background:\*\*\s*(.+)$",
        "text_in_image": r"^\*\*Text in image:\*\*\s*(.+)$",
        "avoid": r"^\*\*Avoid:\*\*\s*(.+)$",
        "philosophy": r"^\*\*Philosophy:\*\*\s*(.+)$",
        # Provider routing (used by resolve_provider)
        "generator": r"^\*\*Generator:\*\*\s*(.+)$",
        "quality": r"^\*\*Quality:\*\*\s*(.+)$",
        "size": r"^\*\*Size:\*\*\s*(.+)$",
    }

    # Only look at the top of the file, before the first ## heading
    head = text.split("\n## ", 1)[0]
    for key, pattern in keys.items():
        m = re.search(pattern, head, re.MULTILINE)
        if m:
            defaults[key] = m.group(1).strip()

    return defaults


def parse_image_plan():
    """Parse IMAGE-PLAN.md into a list of image entries.

    Each entry has: short_name, module_title, file, page, description,
    and either prompt_parts (structured) or uses frontmatter defaults.
    """
    text = IMAGE_PLAN.read_text()
    defaults = parse_frontmatter(text)

    images = []
    current_module = ""
    lines = text.split("\n")

    i = 0
    while i < len(lines):
        line = lines[i]

        mod_match = re.match(r"^##\s+(?:Module|Week)\s+.+", line)
        if mod_match:
            current_module = line.lstrip("#").strip()

        img_match = re.match(r"^###\s+Image\s+\d+:\s*(.+)", line)
        if img_match:
            entry = {
                "short_name": img_match.group(1).strip(),
                "module_title": current_module,
                "file": "",
                "page": "",
                "description": "",
                "prompt_parts": {},
                "defaults": defaults,
            }

            j = i + 1
            in_prompt = False
            prompt_lines = []
            while j < len(lines):
                l = lines[j]
                if re.match(r"^###\s+Image\s+\d+:", l) or re.match(r"^##\s+", l):
                    break

                if in_prompt:
                    if re.match(r"^- \*\*", l) or re.match(r"^###\s+", l) or re.match(r"^##\s+", l) or l.strip() == "---":
                        in_prompt = False
                    else:
                        prompt_lines.append(l.strip())
                        j += 1
                        continue

                file_match = re.match(r"- \*\*File\*\*:\s*`?(.+?)`?$", l)
                if file_match:
                    entry["file"] = file_match.group(1).strip("`")

                page_match = re.match(r"- \*\*Page\*\*:\s*(.+)", l)
                if page_match:
                    entry["page"] = page_match.group(1).strip()

                desc_match = re.match(r"- \*\*Description\*\*:\s*(.+)", l)
                if desc_match:
                    entry["description"] = desc_match.group(1).strip()

                if l.strip() == "- **Prompt**:":
                    in_prompt = True

                j += 1

            prompt_text = "\n".join(prompt_lines)
            for key in ["Goal", "Scene", "Style", "Aspect ratio", "Background", "Text in image", "Avoid"]:
                m = re.search(
                    rf"{key}:\s*(.+?)(?:\n\s*(?:Goal|Scene|Style|Aspect ratio|Background|Text in image|Avoid):|$)",
                    prompt_text, re.DOTALL,
                )
                if m:
                    entry["prompt_parts"][key.lower().replace(" ", "_")] = m.group(1).strip()

            if entry["file"]:
                images.append(entry)

        i += 1

    return images


def assemble_prompt(entry):
    """Build a full prompt from structured parts, or Description + defaults."""
    parts = entry["prompt_parts"]
    defaults = entry["defaults"]

    if parts:
        sections = []
        for key in ["goal", "scene", "style", "aspect_ratio", "background", "text_in_image", "avoid"]:
            if key in parts:
                label = key.replace("_", " ").capitalize().replace("Aspect ratio", "Aspect ratio").replace("Text in image", "Text in image")
                sections.append(f"{label}: {parts[key]}")
        return "\n".join(sections)

    if not entry["description"]:
        return ""

    sections = [f"Scene: {entry['description']}"]
    if "style" in defaults:
        sections.append(f"Style: {defaults['style']}")
    if "branding" in defaults:
        sections.append(f"Branding: {defaults['branding']}")
    if "aspect_ratio" in defaults:
        sections.append(f"Aspect ratio: {defaults['aspect_ratio']}")
    if "background" in defaults:
        sections.append(f"Background: {defaults['background']}")
    if "text_in_image" in defaults:
        sections.append(f"Text in image: {defaults['text_in_image']}")
    if "avoid" in defaults:
        sections.append(f"Avoid: {defaults['avoid']}")
    return "\n".join(sections)


def _extract_retry_delay(err_str):
    """Pull retryDelay seconds from a 429 error message, fallback to 30s."""
    m = re.search(r"retryDelay['\"]?:\s*['\"]?(\d+)s", err_str)
    return int(m.group(1)) + 2 if m else 30


def generate_image(prompt, output_path, api_key, config):
    """Dispatch to provider-specific generator based on `config['provider']`."""
    if config["provider"] == "openai":
        return _generate_openai(prompt, output_path, api_key, config)
    return _generate_gemini(prompt, output_path, api_key, config)


def _generate_openai(prompt, output_path, api_key, config):
    """Generate an image via OpenAI Images API. Returns metadata dict."""
    import base64
    from openai import OpenAI

    client = OpenAI(api_key=api_key)
    start_time = time.time()
    last_err = None
    for attempt in range(MAX_RETRIES_ON_429 + 1):
        try:
            resp = client.images.generate(
                model=config["model"],
                prompt=prompt,
                size=config["size"],
                quality=config["quality"],
                n=1,
            )
            break
        except Exception as e:
            err = str(e)
            last_err = e
            if ("429" in err or "rate limit" in err.lower()) and attempt < MAX_RETRIES_ON_429:
                wait_s = _extract_retry_delay(err)
                print(f" (429, retry in {wait_s}s)", end="", flush=True)
                time.sleep(wait_s)
                continue
            raise

    elapsed_ms = int((time.time() - start_time) * 1000)
    img_bytes = base64.b64decode(resp.data[0].b64_json)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_bytes(img_bytes)

    return {
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "provider": "openai",
        "model": config["model"],
        "quality": config["quality"],
        "size": config["size"],
        "prompt": prompt,
        "output_file": output_path.name,
        "generation_time_ms": elapsed_ms,
        "usage": {},  # OpenAI image API doesn't return token usage in the same way
    }


def _generate_gemini(prompt, output_path, api_key, config):
    """Generate an image via Gemini with retry-on-429. Returns metadata dict."""
    from google import genai
    from google.genai import types

    client = genai.Client(api_key=api_key)

    start_time = time.time()

    for attempt in range(MAX_RETRIES_ON_429 + 1):
        try:
            response = client.models.generate_content(
                model=config["model"],
                contents=prompt,
                config=types.GenerateContentConfig(
                    response_modalities=["IMAGE", "TEXT"],
                ),
            )
            break
        except Exception as e:
            err = str(e)
            if "429" in err and "RESOURCE_EXHAUSTED" in err and attempt < MAX_RETRIES_ON_429:
                wait_s = _extract_retry_delay(err)
                print(f" (429, retry in {wait_s}s)", end="", flush=True)
                time.sleep(wait_s)
                continue
            raise

    elapsed_ms = int((time.time() - start_time) * 1000)

    if not response.candidates or not response.candidates[0].content.parts:
        raise ValueError("No image in response")

    image_data = None
    for part in response.candidates[0].content.parts:
        if part.inline_data and part.inline_data.mime_type.startswith("image/"):
            image_data = part.inline_data.data
            break

    if not image_data:
        raise ValueError("No image data found in response parts")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_bytes(image_data)

    usage = {}
    if hasattr(response, "usage_metadata") and response.usage_metadata:
        um = response.usage_metadata
        usage = {
            "prompt_tokens": getattr(um, "prompt_token_count", 0),
            "candidates_tokens": getattr(um, "candidates_token_count", 0),
            "total_tokens": getattr(um, "total_token_count", 0),
        }

    return {
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "provider": "gemini",
        "model": config["model"],
        "prompt": prompt,
        "output_file": output_path.name,
        "generation_time_ms": elapsed_ms,
        "usage": usage,
    }


# Per-image cost estimates for cost reporting (USD)
OPENAI_COST_TABLE = {
    ("gpt-image-1.5", "low",    "1024x1024"):  0.011,
    ("gpt-image-1.5", "medium", "1024x1024"):  0.042,
    ("gpt-image-1.5", "high",   "1024x1024"):  0.167,
    ("gpt-image-1.5", "low",    "1536x1024"):  0.011,
    ("gpt-image-1.5", "medium", "1536x1024"):  0.042,
    ("gpt-image-1.5", "high",   "1536x1024"):  0.133,
    ("gpt-image-1.5", "low",    "1024x1536"):  0.011,
    ("gpt-image-1.5", "medium", "1024x1536"):  0.042,
    ("gpt-image-1.5", "high",   "1024x1536"):  0.133,
    ("gpt-image-2",   "low",    "1024x1024"):  0.006,
    ("gpt-image-2",   "medium", "1024x1024"):  0.053,
    ("gpt-image-2",   "high",   "1024x1024"):  0.211,
    ("gpt-image-2",   "low",    "1536x1024"):  0.005,
    ("gpt-image-2",   "medium", "1536x1024"):  0.041,
    ("gpt-image-2",   "high",   "1536x1024"):  0.165,
    ("gpt-image-2",   "low",    "1024x1536"):  0.005,
    ("gpt-image-2",   "medium", "1024x1536"):  0.041,
    ("gpt-image-2",   "high",   "1024x1536"):  0.165,
}


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Generate course illustrations")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be generated")
    parser.add_argument("--force", action="store_true", help="Regenerate existing images")
    parser.add_argument("--filter", help="Only generate images whose file path contains this string")
    parser.add_argument("--generator", help="Override IMAGE-PLAN.md frontmatter Generator: line")
    args = parser.parse_args()

    images = parse_image_plan()
    if args.filter:
        images = [img for img in images if args.filter in img["file"]]

    # Provider config from frontmatter (or CLI override). All entries share
    # the same provider for a course — the frontmatter is the contract.
    plan_text = IMAGE_PLAN.read_text() if IMAGE_PLAN.exists() else ""
    defaults = parse_frontmatter(plan_text)
    config = resolve_provider(defaults, override=args.generator)
    api_key = load_api_key(config["provider"])

    print(f"Image Generator — {len(images)} images planned")
    if config["provider"] == "openai":
        print(f"Provider: openai · model: {config['model']} · quality: {config['quality']} · size: {config['size']}")
    else:
        print(f"Provider: gemini · model: {config['model']}")
    print("=" * 60)

    total_tokens = 0
    total_time_ms = 0
    generated = 0
    skipped = 0
    errors = 0
    last_call_time = 0.0

    for idx, img in enumerate(images):
        rel = img["file"]
        if rel.startswith("images/"):
            rel = rel[len("images/"):]
        file_path = IMAGES_DIR / rel
        short = f"[{idx+1}/{len(images)}] {img['short_name']}"

        if file_path.exists() and not args.force:
            print(f"  {short} — exists, skipping")
            skipped += 1
            continue

        prompt = assemble_prompt(img)
        if not prompt:
            print(f"  {short} — no prompt (no Description and no structured Prompt block), skipping")
            skipped += 1
            continue

        if args.dry_run:
            print(f"  {short} — WOULD GENERATE → {img['file']}")
            continue

        elapsed = time.time() - last_call_time
        if elapsed < MIN_INTERVAL_SECONDS:
            time.sleep(MIN_INTERVAL_SECONDS - elapsed)

        print(f"  {short} — generating...", end="", flush=True)
        last_call_time = time.time()

        try:
            meta = generate_image(prompt, file_path, api_key, config)

            json_path = file_path.with_suffix(".json")
            json_path.write_text(json.dumps(meta, indent=2))

            tokens = meta.get("usage", {}).get("total_tokens", 0)
            elapsed = meta.get("generation_time_ms", 0)
            total_tokens += tokens
            total_time_ms += elapsed
            generated += 1

            size_kb = file_path.stat().st_size / 1024
            print(f" OK {size_kb:.0f} KB, {tokens} tokens, {elapsed/1000:.1f}s")

        except Exception as e:
            errors += 1
            print(f" ERROR: {e}")

    print("=" * 60)
    print(f"Generated: {generated}, Skipped: {skipped}, Errors: {errors}")
    if generated > 0:
        if config["provider"] == "openai":
            per_img = OPENAI_COST_TABLE.get(
                (config["model"], config["quality"], config["size"]), 0.13
            )
            est_cost = generated * per_img
            print(f"Total time: {total_time_ms/1000:.1f}s ({total_time_ms/1000/generated:.1f}s avg)")
            print(f"Estimated cost: ${est_cost:.2f}  (~${per_img:.3f}/image at {config['quality']} {config['size']})")
        else:
            est_cost = total_tokens * 0.00007
            print(f"Total tokens: {total_tokens:,}")
            print(f"Total time: {total_time_ms/1000:.1f}s ({total_time_ms/1000/generated:.1f}s avg)")
            print(f"Estimated cost: ${est_cost:.2f}")

    return {
        "generated": generated,
        "skipped": skipped,
        "errors": errors,
        "total_tokens": total_tokens,
        "total_time_ms": total_time_ms,
    }


if __name__ == "__main__":
    main()
