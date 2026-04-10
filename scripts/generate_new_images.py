#!/usr/bin/env python3
"""Generate the 12 new images from IMAGE-PLAN.md using NanoBanana Pro (gemini-3-pro-image-preview)."""

import json
import os
import re
import sys
import time
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
IMAGES_DIR = PROJECT_ROOT / "images"

def get_api_key() -> str:
    env_path = PROJECT_ROOT / ".env"
    if env_path.exists():
        for line in env_path.read_text().splitlines():
            if line.startswith("GEMINI_API_KEY="):
                return line.split("=", 1)[1].strip().strip('"').strip("'")
    key = os.environ.get("GEMINI_API_KEY")
    if not key:
        print("ERROR: GEMINI_API_KEY not set")
        sys.exit(1)
    return key


# Parse IMAGE-PLAN.md for "Not generated" entries
def parse_plan():
    plan_path = PROJECT_ROOT / "IMAGE-PLAN.md"
    text = plan_path.read_text()
    blocks = re.split(r'(?=### Image \d+:)', text)
    images = []
    for block in blocks:
        if 'Not generated' not in block:
            continue
        file_m = re.search(r'\*\*File\*\*: `([^`]+)`', block)
        # Get full prompt section
        prompt_m = re.search(r'\*\*Prompt\*\*:\s*\n((?:  .+\n)+)', block)
        scene_m = re.search(r'Scene: (.+?)(?:\n  [A-Z])', block, re.DOTALL)
        if file_m and scene_m:
            scene = scene_m.group(1).strip().replace('\n', ' ')
            images.append({
                'file': file_m.group(1),
                'scene': scene,
            })
    return images


def generate_image(scene: str, output_path: Path, api_key: str, model: str) -> dict:
    """Generate a single image. Returns metadata dict with cost info."""
    from google import genai
    from google.genai import types

    if output_path.exists():
        print(f"  SKIP (exists): {output_path.name}")
        return {"status": "skipped", "cost": 0}

    client = genai.Client(api_key=api_key)

    full_prompt = (
        f"editorial illustration for a programming textbook. "
        f"{scene} "
        f"Head First book illustration style, clean lines, slightly whimsical "
        f"and humorous, warm colors, educational. Simple and clear. "
        f"White background. Minimal or no text in the image."
    )

    start = time.time()
    try:
        response = client.models.generate_content(
            model=model,
            contents=full_prompt,
            config=types.GenerateContentConfig(
                response_modalities=["image", "text"],
            ),
        )

        elapsed = time.time() - start

        for part in response.candidates[0].content.parts:
            if part.inline_data is not None:
                output_path.parent.mkdir(parents=True, exist_ok=True)
                output_path.write_bytes(part.inline_data.data)

                # Save metadata
                meta_path = output_path.with_suffix(".json")
                meta = {
                    "prompt": scene,
                    "full_prompt": full_prompt,
                    "model": model,
                    "file": output_path.name,
                    "generated": time.strftime("%Y-%m-%dT%H:%M:%SZ"),
                    "elapsed_seconds": round(elapsed, 1),
                }
                meta_path.write_text(json.dumps(meta, indent=2))

                size_kb = output_path.stat().st_size / 1024
                print(f"  OK: {output_path.name} ({size_kb:.0f} KB, {elapsed:.1f}s)")
                return {"status": "ok", "size_kb": size_kb, "elapsed": elapsed}

        print(f"  FAIL (no image in response): {output_path.name}")
        return {"status": "fail_no_image", "cost": 0}

    except Exception as e:
        elapsed = time.time() - start
        print(f"  FAIL ({e}): {output_path.name}")
        return {"status": "fail_error", "error": str(e), "cost": 0}


def main():
    api_key = get_api_key()
    images = parse_plan()

    # Try nano-banana-pro-preview first, fall back to imagen-4.0
    model = "nano-banana-pro-preview"

    print(f"Generating {len(images)} new images with {model}...")
    print()

    results = []
    total_size = 0
    success_count = 0

    for img in images:
        rel_path = img['file']
        output_path = IMAGES_DIR / rel_path.replace("images/", "")
        print(f"[{rel_path}]")
        result = generate_image(img['scene'], output_path, api_key, model)

        if result["status"] == "fail_error" and "not found" in result.get("error", "").lower():
            # Fall back to imagen-4.0
            print(f"  Falling back to imagen-4.0-generate-001...")
            from google import genai
            from google.genai import types
            client = genai.Client(api_key=api_key)
            full_prompt = (
                f"editorial illustration for a programming textbook. "
                f"{img['scene']} "
                f"Head First book illustration style, clean lines, slightly whimsical "
                f"and humorous, warm colors, educational. Simple and clear. "
                f"White background. Minimal or no text in the image."
            )
            try:
                r = client.models.generate_images(
                    model='imagen-4.0-generate-001',
                    prompt=full_prompt,
                    config=types.GenerateImagesConfig(number_of_images=1),
                )
                if r.generated_images:
                    img_data = r.generated_images[0].image
                    output_path.parent.mkdir(parents=True, exist_ok=True)
                    output_path.write_bytes(img_data.image_bytes)
                    meta_path = output_path.with_suffix(".json")
                    meta_path.write_text(json.dumps({
                        "prompt": img['scene'],
                        "model": "imagen-4.0-generate-001",
                        "file": output_path.name,
                        "generated": time.strftime("%Y-%m-%dT%H:%M:%SZ"),
                    }, indent=2))
                    size_kb = output_path.stat().st_size / 1024
                    print(f"  OK (fallback): {output_path.name} ({size_kb:.0f} KB)")
                    result = {"status": "ok", "size_kb": size_kb, "model": "imagen-4.0-generate-001"}
            except Exception as e2:
                print(f"  FAIL (fallback): {e2}")
                result = {"status": "fail_error"}

        results.append({**img, **result})
        if result.get("status") == "ok":
            success_count += 1
            total_size += result.get("size_kb", 0)
        time.sleep(2)

    # Cost estimate: NanoBanana Pro ~$0.14/image, Imagen 4.0 ~$0.04/image
    # Use $0.14 as upper bound for all
    cost_per_image = 0.14
    total_cost = success_count * cost_per_image

    print()
    print("=" * 50)
    print(f"Results: {success_count}/{len(images)} generated")
    print(f"Total image size: {total_size:.0f} KB ({total_size/1024:.1f} MB)")
    print(f"Estimated cost: ${total_cost:.2f} ({success_count} images x ${cost_per_image}/image)")
    print("=" * 50)

    # Return cost for logging
    return total_cost, success_count, len(images)


if __name__ == "__main__":
    total_cost, generated, total = main()
