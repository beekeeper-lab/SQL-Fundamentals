#!/usr/bin/env python3
"""Build the SQL Fundamentals course from markdown source to HTML."""

import argparse
import base64
import json
import re
from pathlib import Path

try:
    import markdown
    from markdown.extensions.codehilite import CodeHiliteExtension
    from markdown.extensions.fenced_code import FencedCodeExtension
    from markdown.extensions.tables import TableExtension
    from markdown.extensions.toc import TocExtension
except ImportError:
    print("ERROR: markdown package not installed. Run: pip install markdown pygments")
    raise SystemExit(1)


PROJECT_ROOT = Path(__file__).parent.parent
SOURCE_DIR = PROJECT_ROOT / "source"
IMAGES_DIR = PROJECT_ROOT / "images"
AUDIO_DIR = PROJECT_ROOT / "audio"
HTML_DIR = PROJECT_ROOT / "html"
QUIZ_DIR = PROJECT_ROOT / "Quiz"

# Module ordering and metadata
MODULES = [
    {"file": "module-00-what-is-sql.md", "short": "Module 0", "title": "What Is SQL?", "hero": "module-00/m00-hero-database-welcome-01.png", "tier": "Start Here", "tier_css": "tier-start-here"},
    {"file": "module-01-creating-tables.md", "short": "Module 1", "title": "Creating Tables", "hero": "module-01/m01-hero-blueprint-01.png", "tier": "Start Here", "tier_css": "tier-start-here"},
    {"file": "module-02-inserting-data.md", "short": "Module 2", "title": "Inserting Data", "hero": "module-02/m02-hero-filling-forms-01.png", "tier": "Start Here", "tier_css": "tier-start-here"},
    {"file": "module-03-select-and-filtering.md", "short": "Module 3", "title": "SELECT and Filtering", "hero": "module-03/m03-hero-detective-01.png", "tier": "Useful Soon", "tier_css": "tier-useful-soon"},
    {"file": "module-04-sorting-and-limiting.md", "short": "Module 4", "title": "Sorting and Limiting", "hero": "module-04/m04-hero-sorting-cards-01.png", "tier": "Useful Soon", "tier_css": "tier-useful-soon"},
    {"file": "module-05-aggregate-functions.md", "short": "Module 5", "title": "Aggregate Functions", "hero": "module-05/m05-hero-zoom-out-01.png", "tier": "Useful Soon", "tier_css": "tier-useful-soon"},
    {"file": "module-06-joins.md", "short": "Module 6", "title": "Joins", "hero": "module-06/m06-hero-puzzle-pieces.png", "tier": "When You're Ready", "tier_css": "tier-when-ready"},
    {"file": "module-07-subqueries-and-views.md", "short": "Module 7", "title": "Subqueries and Views", "hero": "module-07/m07-hero-nesting-dolls-01.png", "tier": "When You're Ready", "tier_css": "tier-when-ready"},
    {"file": "module-08-updating-and-deleting.md", "short": "Module 8", "title": "Updating and Deleting", "hero": "module-08/m08-hero-permanent-marker-01.png", "tier": "When You're Ready", "tier_css": "tier-when-ready"},
    {"file": "module-09-indexes-and-best-practices.md", "short": "Module 9", "title": "Indexes and Best Practices", "hero": "module-09/m09-hero-textbook-index-01.png", "tier": "Advanced", "tier_css": "tier-advanced"},
]

EXTRAS = []

REFERENCES = []


def image_to_base64(image_path: Path) -> str | None:
    """Convert an image file to a base64 data URI."""
    if not image_path.exists():
        return None
    data = base64.b64encode(image_path.read_bytes()).decode()
    return f"data:image/png;base64,{data}"


def resolve_image_path(src: str) -> Path | None:
    """Resolve a markdown image src to an absolute path."""
    # Images in source files use ../images/module-XX/name.png
    clean = src.replace("../images/", "").replace("images/", "")
    candidate = IMAGES_DIR / clean
    if candidate.exists():
        return candidate
    return None


def embed_images(html_content: str) -> str:
    """Replace image src paths with base64-embedded data URIs."""
    def replace_img(match):
        full_tag = match.group(0)
        src = match.group(1)
        img_path = resolve_image_path(src)
        if img_path:
            data_uri = image_to_base64(img_path)
            if data_uri:
                return full_tag.replace(src, data_uri)
        return full_tag

    return re.sub(r'<img[^>]+src="([^"]+)"', replace_img, html_content)


def process_narration_blocks(html_content: str, module_stem: str) -> str:
    """Convert narration blockquotes (🎙️) into audio player widgets."""
    audio_module_dir = AUDIO_DIR / module_stem

    # Load manifest if it exists
    manifest_path = audio_module_dir / "manifest.json"
    audio_files = {}
    if manifest_path.exists():
        manifest = json.loads(manifest_path.read_text())
        for entry in manifest:
            audio_files[entry["index"]] = entry

    narration_counter = 0

    def replace_narration(match):
        nonlocal narration_counter
        narration_counter += 1
        content = match.group(1)

        # Remove the 🎙️ emoji and clean up paragraph tags for display
        display_text = re.sub(r'🎙️\s*', '', content)
        # Ensure content is wrapped in <p> tags for consistent display
        if not display_text.strip().startswith('<p>'):
            display_text = f'<p>{display_text.strip()}</p>'

        # Check for audio file
        audio_entry = audio_files.get(narration_counter)
        audio_html = ""
        if audio_entry:
            audio_path = audio_module_dir / audio_entry["audio_file"]
            if audio_path.exists():
                audio_b64 = base64.b64encode(audio_path.read_bytes()).decode()
                audio_html = f'''
                <button class="narration-play" onclick="playNarration(this)" aria-label="Play narration">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                        <path d="M8 5v14l11-7z"/>
                    </svg>
                </button>
                <audio preload="none">
                    <source src="data:audio/mpeg;base64,{audio_b64}" type="audio/mpeg">
                </audio>'''

        return f'''<div class="narration-block">
            <div class="narration-icon">🎙️</div>
            <div class="narration-content">{display_text}</div>
            {audio_html}
        </div>'''

    # Match blockquotes containing 🎙️ (handles multi-paragraph blockquotes)
    html_content = re.sub(
        r'<blockquote>\s*((?:<p>)*🎙️.*?)\s*</blockquote>',
        replace_narration,
        html_content,
        flags=re.DOTALL,
    )

    # Also match plain <p>🎙️ paragraphs (narrations not in blockquotes)
    html_content = re.sub(
        r'<p>(🎙️.*?)</p>',
        replace_narration,
        html_content,
        flags=re.DOTALL,
    )

    return html_content


_MARKER_EMOJI_RE = re.compile(
    r'[\U0001F3F7]\uFE0F|'   # 🏷️
    r'\U0001F3AF|'            # 🎯
    r'[\U0001F399]\uFE0F|'   # 🎙️
    r'\U0001F504|'            # 🔄
    r'\U0001F4A1'             # 💡
)


def split_merged_blockquotes(html_content: str) -> str:
    """Split <blockquote> blocks that contain multiple <p> marker paragraphs.

    Python-Markdown merges adjacent > lines into one <blockquote> even when
    they are separated by blank lines in the source.  The emoji processors
    expect each marker in its own <blockquote>, so we split them here.
    """
    def _split_one(match: re.Match) -> str:
        inner = match.group(1)
        # Split on paragraph boundaries
        paragraphs = re.split(r'</p>\s*<p>', inner)
        if len(paragraphs) < 2:
            return match.group(0)  # single paragraph, nothing to split

        # Check if any paragraph contains a marker emoji
        has_marker = any(_MARKER_EMOJI_RE.search(p) for p in paragraphs)
        if not has_marker:
            return match.group(0)  # no markers, leave untouched

        # Rewrap each paragraph in its own blockquote
        parts = []
        for p in paragraphs:
            p = p.strip()
            if not p.startswith('<p>'):
                p = '<p>' + p
            if not p.endswith('</p>'):
                p = p + '</p>'
            parts.append(f'<blockquote>\n{p}\n</blockquote>')
        return '\n'.join(parts)

    return re.sub(
        r'<blockquote>\s*(.*?)\s*</blockquote>',
        _split_one,
        html_content,
        flags=re.DOTALL,
    )


def process_tier_badges(html_content: str) -> str:
    """Convert tier markers into styled badge elements."""
    tier_classes = {
        "Start Here": "tier-start-here",
        "Useful Soon": "tier-useful-soon",
        "When You're Ready": "tier-when-ready",
        "Advanced": "tier-advanced",
    }

    def replace_tier(match):
        content = match.group(1)
        text = re.sub(r'🏷️\s*', '', content).strip()
        # Extract tier name (text before any colon or period)
        tier_name = text.split('.')[0].split(':')[0].strip()
        css_class = tier_classes.get(tier_name, "tier-start-here")
        # Check for readiness note after the tier name
        rest = text[len(tier_name):].lstrip('.:').strip()
        readiness = f'<div class="readiness-note">{rest}</div>' if rest else ''
        return f'<div class="tier-badge {css_class}">{tier_name}</div>{readiness}'

    html_content = re.sub(
        r'<blockquote>\s*(?:<p>)*(🏷️.*?)(?:</p>)*\s*</blockquote>',
        replace_tier, html_content, flags=re.DOTALL,
    )
    html_content = re.sub(
        r'<p>(🏷️.*?)</p>',
        replace_tier, html_content, flags=re.DOTALL,
    )
    return html_content


def process_cycle_anchor_blocks(html_content: str) -> str:
    """Convert cycle anchor blockquotes (🔄) into styled anchor blocks."""

    def replace_anchor(match):
        content = match.group(1)
        display_text = re.sub(r'🔄\s*', '', content)
        if not display_text.strip().startswith('<'):
            display_text = f'<p>{display_text.strip()}</p>'
        return f'''<div class="cycle-anchor">
            <div class="cycle-anchor-icon">🔄</div>
            <div>{display_text}</div>
        </div>'''

    html_content = re.sub(
        r'<blockquote>\s*((?:<p>)*🔄.*?)\s*</blockquote>',
        replace_anchor, html_content, flags=re.DOTALL,
    )
    html_content = re.sub(
        r'<p>(🔄.*?)</p>',
        replace_anchor, html_content, flags=re.DOTALL,
    )
    return html_content


def process_remember_blocks(html_content: str) -> str:
    """Convert remember-one-thing blockquotes (💡) into styled callout blocks."""

    def replace_remember(match):
        content = match.group(1)
        display_text = re.sub(r'💡\s*', '', content)
        if not display_text.strip().startswith('<'):
            display_text = f'<p>{display_text.strip()}</p>'
        return f'''<div class="remember-one-thing">
            <div class="remember-icon">💡</div>
            <div class="remember-content">{display_text}</div>
        </div>'''

    html_content = re.sub(
        r'<blockquote>\s*((?:<p>)*💡.*?)\s*</blockquote>',
        replace_remember, html_content, flags=re.DOTALL,
    )
    html_content = re.sub(
        r'<p>(💡.*?)</p>',
        replace_remember, html_content, flags=re.DOTALL,
    )
    return html_content


def process_teaching_intent_blocks(html_content: str) -> str:
    """Convert teaching intent blockquotes (🎯) into styled intent blocks."""

    def replace_intent(match):
        content = match.group(1)
        # Remove the 🎯 emoji
        display_text = re.sub(r'🎯\s*', '', content)
        # Ensure wrapped in tags
        if not display_text.strip().startswith('<p>') and not display_text.strip().startswith('<strong>'):
            display_text = f'<p>{display_text.strip()}</p>'

        return f'''<div class="teaching-intent">
            <div class="intent-icon">🎯</div>
            <div class="intent-content">{display_text}</div>
        </div>'''

    # Match blockquotes containing 🎯
    html_content = re.sub(
        r'<blockquote>\s*((?:<p>)*🎯.*?)\s*</blockquote>',
        replace_intent,
        html_content,
        flags=re.DOTALL,
    )

    # Also match plain <p>🎯 paragraphs
    html_content = re.sub(
        r'<p>(🎯.*?)</p>',
        replace_intent,
        html_content,
        flags=re.DOTALL,
    )

    return html_content


def generate_toc(html_body: str) -> str:
    """Generate a page-grouped TOC from the HTML body.

    Each H2 starts a new page group (matching split_into_pages logic).
    H3s nest underneath their parent H2.  Output uses toc-page-group
    classes so the template CSS can style them.
    """
    heading_re = re.compile(r'<(h[23])\s[^>]*id="([^"]+)"[^>]*>(.*?)</\1>', re.DOTALL)
    headings = [(m.group(1), m.group(2), re.sub(r'<[^>]+>', '', m.group(3)).strip())
                for m in heading_re.finditer(html_body)]

    if not headings:
        return ''

    # Group: every h2 starts a new page (page 0 is intro content merged with first h2)
    groups: list[dict] = []       # [{h2_id, h2_text, h3s: [(id, text), ...]}]
    for tag, hid, text in headings:
        if tag == 'h2':
            groups.append({'h2_id': hid, 'h2_text': text, 'h3s': []})
        elif tag == 'h3' and groups:
            groups[-1]['h3s'].append((hid, text))

    lines = ['<ul class="toc-list">']
    for page_num, g in enumerate(groups):
        lines.append(f'  <li class="toc-page-group" data-toc-page="{page_num}">')
        lines.append(f'    <a href="#{g["h2_id"]}" class="toc-h2-link">{g["h2_text"]}</a>')
        if g['h3s']:
            lines.append('    <ul class="toc-subsections">')
            for h3_id, h3_text in g['h3s']:
                lines.append(f'      <li><a href="#{h3_id}" class="toc-h3-link">{h3_text}</a></li>')
            lines.append('    </ul>')
        lines.append('  </li>')
    lines.append('</ul>')
    return '\n'.join(lines)


def convert_markdown_to_html(source_path: Path) -> tuple[str, str]:
    """Convert a markdown file to HTML content. Returns (title, html_body, toc)."""
    text = source_path.read_text()

    # Extract title from first H1
    title_match = re.match(r'^#\s+(.+)', text, re.MULTILINE)
    title = title_match.group(1) if title_match else source_path.stem

    md = markdown.Markdown(
        extensions=[
            FencedCodeExtension(),
            CodeHiliteExtension(css_class="highlight", guess_lang=False),
            TableExtension(),
            TocExtension(permalink=False, toc_depth="2-3"),
            "md_in_html",
        ]
    )

    html_body = md.convert(text)
    toc = generate_toc(html_body)

    return title, html_body, toc


def split_into_pages(html_body: str) -> list[str]:
    """Split HTML body into pages at each <h2> boundary."""
    # Split on h2 tags, keeping the h2 with its section
    parts = re.split(r'(?=<h2[ >])', html_body)
    pages = []
    for i, part in enumerate(parts):
        part = part.strip()
        if not part:
            continue
        if i == 0 and not part.startswith('<h2'):
            # Intro content (before first h2) -- merge with the next section
            # so the title page includes the first section's content
            if len(parts) > 1:
                parts[1] = part + "\n" + parts[1]
                continue
        pages.append(f'<div class="page" data-page="{len(pages)}">{part}</div>')
    return pages if pages else [f'<div class="page" data-page="0">{html_body}</div>']


def generate_quiz_html(module_num: int, module_slug: str) -> str:
    """Generate quiz HTML from the Day_XX quiz JSON file."""
    quiz_dir = QUIZ_DIR / f"Day_{module_num + 1:02d}_Quiz_File"
    quiz_file = quiz_dir / f"day_{module_num + 1:02d}_quiz.json"
    if not quiz_file.exists():
        return ""

    data = json.loads(quiz_file.read_text())
    title = data.get("quiz_title", f"Module {module_num} Quiz")
    passing = data.get("passing_score", 0)
    total = data.get("total_questions", len(data.get("questions", [])))
    questions = data.get("questions", [])

    if not questions:
        return ""

    # Build question HTML
    q_html = []
    for q in questions:
        qid = q["id"]
        opts = ""
        for opt in q["options"]:
            safe_opt = opt.replace('"', '&quot;').replace("'", "&#39;")
            opts += (
                f'<label><input type="radio" name="q{qid}" value="{safe_opt}">'
                f' <span>{opt}</span></label>\n'
            )
        safe_answer = q["answer"].replace('"', '&quot;')
        q_html.append(
            f'<div class="quiz-question" data-answer="{safe_answer}" style="display:none;">\n'
            f'  <div class="quiz-question-number">Question {qid}</div>\n'
            f'  <div class="quiz-question-text">{q["question"]}</div>\n'
            f'  <div class="quiz-options">\n{opts}  </div>\n'
            f'  <div class="quiz-feedback-text"></div>\n'
            f'</div>'
        )

    quiz_data_json = json.dumps({
        "moduleSlug": module_slug,
        "passingScore": passing,
        "totalQuestions": total,
    })

    return (
        f'\n<h2 id="quiz">Knowledge Check: {title}</h2>\n'
        f'<p class="quiz-meta">{total} questions &middot; {passing} to pass &middot; 45 seconds per question</p>\n'
        f'<div class="quiz-status-bar">\n'
        f'  <span id="quizStatusScore">Score: 0 / 0</span>\n'
        f'  <span id="quizStatusProgress">0 of {total} answered</span>\n'
        f'  <span class="quiz-timer" id="quizTimer">45s</span>\n'
        f'</div>\n'
        f'<div class="quiz-progress-track"><div class="quiz-progress-fill" id="quizProgressFill" style="width:0%"></div></div>\n'
        f'<script type="application/json" id="quizData">{quiz_data_json}</script>\n'
        f'<div class="quiz-container" id="quizForm">\n'
        + "\n".join(q_html) +
        f'\n</div>\n'
        f'<button class="quiz-action-btn" id="quizActionBtn" disabled>Submit Answer</button>\n'
        f'<div class="quiz-results" id="quizResults">\n'
        f'  <div class="quiz-score" id="quizScore"></div>\n'
        f'  <div class="quiz-pct" id="quizScorePct"></div>\n'
        f'  <div class="quiz-label" id="quizLabel"></div>\n'
        f'  <div class="quiz-detail" id="quizDetail"></div>\n'
        f'  <button class="quiz-retry-btn" id="quizRetryBtn">Retake Quiz</button>\n'
        f'</div>\n'
    )


def build_module_html(
    source_path: Path,
    prev_module: dict | None,
    next_module: dict | None,
    module_index: int,
    total_modules: int,
    embed_media: bool = True,
) -> str:
    """Build a complete HTML page for a module."""
    title, body, toc = convert_markdown_to_html(source_path)
    module_stem = source_path.stem

    # Split merged blockquotes so each emoji marker gets its own <blockquote>
    body = split_merged_blockquotes(body)

    # Process special blocks
    body = process_tier_badges(body)
    body = process_cycle_anchor_blocks(body)
    body = process_remember_blocks(body)
    body = process_teaching_intent_blocks(body)

    # Process narration blocks
    body = process_narration_blocks(body, module_stem)

    # Embed images
    if embed_media:
        body = embed_images(body)

    # Append quiz page if quiz exists for this module
    module_num_match = re.search(r'module-(\d+)', module_stem)
    if module_num_match:
        module_num = int(module_num_match.group(1))
        quiz_html = generate_quiz_html(module_num, module_stem)
        if quiz_html:
            body += quiz_html

    # Split into pages
    pages = split_into_pages(body)
    paginated_body = "\n".join(pages)

    # Navigation
    prev_link = ""
    if prev_module:
        prev_file = prev_module["file"].replace(".md", ".html")
        prev_link = f'<a href="{prev_file}" class="nav-prev">← {prev_module["short"]}: {prev_module["title"]}</a>'

    next_link = ""
    if next_module:
        next_file = next_module["file"].replace(".md", ".html")
        next_link = f'<a href="{next_file}" class="nav-next">{next_module["short"]}: {next_module["title"]} →</a>'

    progress_pct = ((module_index + 1) / total_modules) * 100

    template_path = Path(__file__).parent / "module_template.html"
    template = template_path.read_text()

    return (template
        .replace("{{TITLE}}", title)
        .replace("{{TOC}}", toc)
        .replace("{{BODY}}", paginated_body)
        .replace("{{PREV_LINK}}", prev_link)
        .replace("{{NEXT_LINK}}", next_link)
    )


def _build_card(mod: dict, prefix: str = "html/") -> str:
    """Build a single module card with embedded hero thumbnail."""
    html_file = prefix + mod["file"].replace(".md", ".html")
    slug = mod["file"].replace(".md", "")
    hero_path = IMAGES_DIR / mod.get("hero", "")
    thumb = image_to_base64(hero_path) if hero_path.exists() else ""
    thumb_html = f'<img class="card-thumb" src="{thumb}" alt="">' if thumb else ""
    tier = mod.get("tier", "")
    tier_css = mod.get("tier_css", "")
    tier_html = f'<span class="card-tier {tier_css}">{tier}</span>' if tier else ""
    return f'''
            <a href="{html_file}" class="module-card" data-module-slug="{slug}">
                {thumb_html}
                <div class="card-text">
                    <div class="module-number">{mod["short"]} {tier_html}</div>
                    <div class="module-title">{mod["title"]}</div>
                    <div class="quiz-score-line" data-quiz-score></div>
                </div>
                <div class="card-right">
                    <span class="quiz-badge not-taken" data-quiz-badge>Quiz</span>
                    <div class="module-progress"></div>
                </div>
            </a>'''


def build_index_html() -> str:
    """Build the course landing/index page."""
    # Build card HTML organized by section
    sections = {
        "foundations": [0, 1, 2],
        "intermediate": [3, 4, 5],
        "advanced": [6, 7, 8],
        "expert": [9],
    }
    section_cards = {}
    for section_name, indices in sections.items():
        cards = [_build_card(MODULES[i]) for i in indices]
        section_cards[section_name] = "\n".join(cards)

    # Embed hero image
    hero_img = image_to_base64(IMAGES_DIR / "module-00" / "m00-hero-database-welcome-01.png") or ""

    return INDEX_TEMPLATE.format(
        cards_foundations=section_cards["foundations"],
        cards_intermediate=section_cards["intermediate"],
        cards_advanced=section_cards["advanced"],
        cards_expert=section_cards["expert"],
        hero_image=hero_img,
    )


# ─── HTML Templates ───────────────────────────────────────────────
# Module template is loaded from module_template.html at build time.

INDEX_TEMPLATE = """<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>SQL Fundamentals</title>
<link rel="icon" type="image/png" href="favicon.png">
<style>
*, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}

:root {{
    --bg: #ffffff;
    --bg-secondary: #f8f9fa;
    --bg-code: #f4f4f4;
    --text: #1a1a2e;
    --text-secondary: #555;
    --border: #e0e0e0;
    --accent: #2563eb;
    --accent-light: #dbeafe;
    --narration-bg: #fef3c7;
    --narration-border: #f59e0b;
    --shadow: 0 1px 3px rgba(0,0,0,0.1);
    --font-body: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    --font-mono: 'SF Mono', 'Fira Code', 'Cascadia Code', monospace;
}}

[data-theme="dark"] {{
    --bg: #0f172a;
    --bg-secondary: #1e293b;
    --bg-code: #1e293b;
    --text: #e2e8f0;
    --text-secondary: #94a3b8;
    --border: #334155;
    --accent: #60a5fa;
    --accent-light: #1e3a5f;
    --narration-bg: #422006;
    --narration-border: #d97706;
    --shadow: 0 1px 3px rgba(0,0,0,0.3);
}}

body {{
    font-family: var(--font-body);
    background: var(--bg);
    color: var(--text);
    line-height: 1.7;
    font-size: 17px;
    transition: background 0.3s, color 0.3s;
}}

/* ── Layout ── */
.page-wrapper {{
    display: flex;
    min-height: 100vh;
}}

.theme-toggle {{
    position: fixed;
    top: 1rem;
    right: 1rem;
    background: var(--bg-secondary);
    border: 1px solid var(--border);
    border-radius: 6px;
    padding: 0.3rem 0.5rem;
    cursor: pointer;
    font-size: 16px;
    color: var(--text);
    z-index: 100;
}}

.main-content {{
    max-width: 820px;
    margin: 0 auto;
    padding: 2rem 2rem 4rem;
}}

/* ── Typography ── */
h1 {{ font-size: 2rem; margin: 0 0 0.25rem; line-height: 1.3; }}
h2 {{ font-size: 1.5rem; margin: 2.5rem 0 1rem; padding-top: 1.5rem; border-top: 1px solid var(--border); }}
h3 {{ font-size: 1.2rem; margin: 2rem 0 0.75rem; }}

h2:first-of-type {{ border-top: none; padding-top: 0; }}

p {{ margin: 0.75rem 0; }}
a {{ color: var(--accent); text-decoration: none; }}
a:hover {{ text-decoration: underline; }}
strong {{ font-weight: 600; }}

.subtitle {{
    color: var(--text-secondary);
    font-size: 1.1rem;
    margin-bottom: 1.5rem;
}}

/* ── Images ── */
img {{
    max-width: 100%;
    height: auto;
    border-radius: 8px;
    margin: 1rem 0;
    box-shadow: var(--shadow);
}}

.hero-image {{
    display: block;
    max-width: 520px;
    margin: 1.5rem 0;
}}


/* ── Module Grid ── */
.section-label {{
    font-size: 0.8rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    color: var(--text-secondary);
    margin: 2rem 0 0.75rem;
}}

.module-grid {{
    display: grid;
    gap: 0.6rem;
}}

.module-card {{
    display: flex;
    align-items: center;
    gap: 1rem;
    padding: 0.75rem 1rem;
    background: var(--bg-secondary);
    border: 1px solid var(--border);
    border-radius: 10px;
    text-decoration: none;
    color: var(--text);
    transition: border-color 0.2s, box-shadow 0.2s, transform 0.15s;
    overflow: hidden;
}}

.module-card:hover {{
    border-color: var(--accent);
    box-shadow: var(--shadow);
    transform: translateY(-2px);
    text-decoration: none;
}}

.card-thumb {{
    width: 80px;
    height: 56px;
    object-fit: cover;
    border-radius: 6px;
    flex-shrink: 0;
    box-shadow: none;
    margin: 0;
}}

.card-text {{
    flex: 1;
    min-width: 0;
}}

.module-number {{
    font-weight: 700;
    font-size: 0.8rem;
    color: var(--accent);
    white-space: nowrap;
}}

.module-title {{
    font-size: 0.95rem;
    line-height: 1.3;
}}

.card-tier {{
    font-size: 0.6rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    padding: 0.15rem 0.45rem;
    border-radius: 100px;
    margin-left: 0.4rem;
    vertical-align: middle;
}}

.tier-start-here {{ background: #dcfce7; color: #166534; border: 1px solid #86efac; }}
.tier-useful-soon {{ background: #dbeafe; color: #1e40af; border: 1px solid #93c5fd; }}
.tier-when-ready {{ background: #fef3c7; color: #92400e; border: 1px solid #fcd34d; }}
.tier-advanced {{ background: #f3e8ff; color: #6b21a8; border: 1px solid #c4b5fd; }}

[data-theme="dark"] .tier-start-here {{ background: #052e16; color: #86efac; border-color: #166534; }}
[data-theme="dark"] .tier-useful-soon {{ background: #172554; color: #93c5fd; border-color: #1e40af; }}
[data-theme="dark"] .tier-when-ready {{ background: #451a03; color: #fcd34d; border-color: #92400e; }}
[data-theme="dark"] .tier-advanced {{ background: #3b0764; color: #c4b5fd; border-color: #6b21a8; }}

.card-right {{
    margin-left: auto;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    gap: 0.25rem;
    flex-shrink: 0;
}}

.module-progress {{
    font-size: 0.85rem;
    color: var(--text-secondary);
}}

.quiz-badge {{
    font-size: 0.6rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    padding: 0.15rem 0.5rem;
    border-radius: 100px;
}}

.quiz-badge.not-taken {{ background: var(--bg-code); color: var(--text-secondary); border: 1px solid var(--border); }}
.quiz-badge.passed {{ background: #dcfce7; color: #166534; border: 1px solid #86efac; }}
.quiz-badge.failed {{ background: #fee2e2; color: #991b1b; border: 1px solid #fca5a5; }}
[data-theme="dark"] .quiz-badge.passed {{ background: #052e16; color: #86efac; border-color: #166534; }}
[data-theme="dark"] .quiz-badge.failed {{ background: #450a0a; color: #fca5a5; border-color: #991b1b; }}

.quiz-score-line {{
    font-size: 0.75rem;
    color: var(--text-secondary);
    margin-top: 0.1rem;
}}

/* ── Quick Reference ── */
.quick-ref {{
    background: var(--bg-secondary);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 1.5rem;
    margin: 1.5rem 0;
}}

.quick-ref h3 {{ margin: 0 0 0.75rem; }}

.quick-ref pre {{
    background: var(--bg);
    border: 1px solid var(--border);
    border-radius: 6px;
    padding: 1rem;
    font-family: var(--font-mono);
    font-size: 0.85rem;
    overflow-x: auto;
    line-height: 1.8;
    margin: 0;
}}

/* ── Learning Outcomes ── */
.outcomes {{
    padding-left: 1.75rem;
}}
.outcomes li {{
    margin: 0.4rem 0;
}}

/* ── Footer ── */
.footer {{
    text-align: center;
    padding: 2rem 0 1rem;
    color: var(--text-secondary);
    font-size: 0.85rem;
    border-top: 1px solid var(--border);
    margin-top: 2.5rem;
}}

/* ── Mobile ── */
@media (max-width: 600px) {{
    .main-content {{ padding: 1.5rem 1.25rem 3rem; }}
    .hero-image {{ max-width: 100%; }}
}}

@media print {{
    .main-content {{ padding: 0; }}
    .theme-toggle {{ display: none !important; }}
}}
</style>
</head>
<body>

<button class="theme-toggle" onclick="toggleTheme()" aria-label="Toggle theme">🌓</button>

<main class="main-content">
        <h1>SQL Fundamentals</h1>
        <p class="subtitle">A structured course in SQL and relational databases</p>

        <img src="{hero_image}" alt="Welcome to SQL Fundamentals" class="hero-image">

        <h2>What you'll learn</h2>

        <p>This course teaches you the foundations of <strong>SQL and relational databases</strong> — from creating your first table to writing complex queries, joining data across tables, and following best practices for performance and security.</p>

        <ul class="outcomes">
            <li>Understand relational databases and how data is organized in tables</li>
            <li>Write DDL (<strong>CREATE, ALTER, DROP</strong>), DML (<strong>INSERT, UPDATE, DELETE</strong>), and DQL (<strong>SELECT</strong>) statements</li>
            <li>Use constraints to enforce data integrity</li>
            <li>Query with filtering, sorting, pagination, and deduplication</li>
            <li>Summarize data with aggregate functions and <strong>GROUP BY</strong></li>
            <li>Connect tables using joins</li>
            <li>Build complex logic with subqueries and views</li>
            <li>Safely modify data with transactions</li>
            <li>Optimize with indexes and prevent SQL injection</li>
            <li>Design normalized schemas following best practices</li>
        </ul>

        <h2>Self-Study Modules</h2>

        <div class="section-label">Foundations</div>
        <div class="module-grid">
            {cards_foundations}
        </div>

        <div class="section-label">Intermediate</div>
        <div class="module-grid">
            {cards_intermediate}
        </div>

        <div class="section-label">Advanced</div>
        <div class="module-grid">
            {cards_advanced}
        </div>

        <div class="section-label">Expert</div>
        <div class="module-grid">
            {cards_expert}
        </div>

        <h2>Your Practice Path</h2>

        <div class="quick-ref">
            <pre>After Modules 0-2:  Create your first database with tables and data
After Modules 3-5:  Write queries that filter, sort, and summarize real data
After Modules 6-7:  Join tables and build subqueries for complex questions
After Modules 8-9:  Modify data safely and design optimized schemas</pre>
        </div>

    </main>

<script>
function toggleTheme() {{
    const html = document.documentElement;
    const next = html.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
    html.setAttribute('data-theme', next);
    localStorage.setItem('theme', next);
}}

(function() {{
    const saved = localStorage.getItem('theme');
    if (saved) document.documentElement.setAttribute('data-theme', saved);
    else if (window.matchMedia('(prefers-color-scheme: dark)').matches)
        document.documentElement.setAttribute('data-theme', 'dark');

    // Mark visited modules with checkmarks
    const visited = JSON.parse(localStorage.getItem('sql_fund_visited') || '[]');
    visited.forEach(v => {{
        const card = document.querySelector(`a[href="html/${{v}}.html"]`);
        if (card) {{
            const prog = card.querySelector('.module-progress');
            if (prog) prog.textContent = '✓';
        }}
    }});

    // Update quiz badges from saved results
    const quizResults = JSON.parse(localStorage.getItem('sql-fundamentals-quiz-results') || '{{}}');
    document.querySelectorAll('.module-card[data-module-slug]').forEach(card => {{
        const slug = card.getAttribute('data-module-slug');
        const badge = card.querySelector('[data-quiz-badge]');
        const scoreLine = card.querySelector('[data-quiz-score]');
        const result = quizResults[slug];
        if (result && badge) {{
            if (result.passed) {{
                badge.className = 'quiz-badge passed';
                badge.textContent = 'Passed';
            }} else {{
                badge.className = 'quiz-badge failed';
                badge.textContent = 'Retry';
            }}
            if (scoreLine) {{
                scoreLine.textContent = result.score + '/' + result.total;
            }}
        }}
    }});
}})();
</script>

</body>
</html>"""


def main():
    parser = argparse.ArgumentParser(description="Build SQL Fundamentals course HTML")
    parser.add_argument("--no-embed", action="store_true", help="Link images instead of embedding")
    parser.add_argument("--module", help="Build only a specific module (e.g., module-00-what-is-sql)")
    args = parser.parse_args()

    HTML_DIR.mkdir(parents=True, exist_ok=True)
    embed = not args.no_embed

    if args.module:
        # Build single module
        source_path = SOURCE_DIR / f"{args.module}.md"
        if not source_path.exists():
            print(f"ERROR: {source_path} not found")
            return

        idx = next((i for i, m in enumerate(MODULES) if m["file"].startswith(args.module)), -1)
        prev_mod = MODULES[idx - 1] if idx > 0 else None
        next_mod = MODULES[idx + 1] if idx < len(MODULES) - 1 else None

        html = build_module_html(source_path, prev_mod, next_mod, idx, len(MODULES), embed)
        out_path = HTML_DIR / f"{args.module}.html"
        out_path.write_text(html)
        print(f"Built: {out_path}")
        return

    # Build all modules
    print(f"Building {len(MODULES)} modules...")
    for i, mod in enumerate(MODULES):
        source_path = SOURCE_DIR / mod["file"]
        if not source_path.exists():
            print(f"  SKIP: {mod['file']} not found")
            continue

        prev_mod = MODULES[i - 1] if i > 0 else None
        next_mod = MODULES[i + 1] if i < len(MODULES) - 1 else None

        html = build_module_html(source_path, prev_mod, next_mod, i, len(MODULES), embed)
        out_path = HTML_DIR / mod["file"].replace(".md", ".html")
        out_path.write_text(html)
        print(f"  Built: {out_path.name}")

    # Build extras (if any)
    if EXTRAS:
        print(f"Building {len(EXTRAS)} extras...")
        for ex in EXTRAS:
            source_path = SOURCE_DIR / ex["file"]
            if not source_path.exists():
                print(f"  SKIP: {ex['file']} not found")
                continue

            html = build_module_html(source_path, None, None, -1, len(MODULES), embed)
            out_path = HTML_DIR / ex["file"].replace(".md", ".html")
            out_path.write_text(html)
            print(f"  Built: {out_path.name}")

    # Build references (if any)
    if REFERENCES:
        print(f"Building {len(REFERENCES)} references...")
        for ref in REFERENCES:
            source_path = SOURCE_DIR / ref["file"]
            if not source_path.exists():
                print(f"  SKIP: {ref['file']} not found")
                continue

            html = build_module_html(source_path, None, None, -1, len(MODULES), embed)
            out_path = HTML_DIR / ref["file"].replace(".md", ".html")
            out_path.write_text(html)
            print(f"  Built: {out_path.name}")

    # Build index at project root
    index_html = build_index_html()
    index_path = PROJECT_ROOT / "index.html"
    index_path.write_text(index_html)
    print(f"  Built: index.html (project root)")

    print(f"\nDone. Open index.html to view the course.")


if __name__ == "__main__":
    main()
