# SQL Fundamentals

A free, self-paced course that teaches SQL from scratch — from the relational model through joins, transactions, indexing, and schema design — using SQLite, with zero server setup.

**Live URL:** **<https://beekeeper-lab.github.io/SQL-Fundamentals/>**

![A developer at a laptop, surrounded by friendly tables of data.](images/module-00/m00-hero-relational-tables-01.png)

---

This repository serves two audiences. Pick whichever describes you, or skim both — they're written to work together.

- **If you want to take the course**, start at the live URL above. Everything below is optional.
- **If you want to build a course like this**, most of this README is for you. The pipeline that produced the course — illustrations, narration, HTML, quizzes — is entirely here in the repo, documented and reproducible. SQL Fundamentals is the most-polished course in the [Stonewaters Consulting intern portfolio](https://github.com/beekeeper-lab) and is a good reference for builders.

---

## Table of contents

- [Take the course](#take-the-course)
- [What's in this repo](#whats-in-this-repo)
- [How this course was built (the pipeline)](#how-this-course-was-built-the-pipeline)
  - [1. Content authored in markdown](#1-content-authored-in-markdown)
  - [2. Illustration generation via Gemini](#2-illustration-generation-via-gemini)
  - [3. Narration generation via ElevenLabs](#3-narration-generation-via-elevenlabs)
  - [4. HTML build and deploy](#4-html-build-and-deploy)
  - [5. Quizzes](#5-quizzes)
- [Running the pipeline locally](#running-the-pipeline-locally)
- [Repository map](#repository-map)
- [Design philosophy worth stealing](#design-philosophy-worth-stealing)
- [Status and maintenance](#status-and-maintenance)
- [Credits and source material](#credits-and-source-material)

---

## Take the course

**Live URL:** **<https://beekeeper-lab.github.io/SQL-Fundamentals/>**

Ten day-modules (Day 1 through Day 10), each narrated, illustrated, and quizzed end-to-end. No login, no sign-up, no tracking — your progress checkmarks and quiz scores live privately in your browser's `localStorage`.

**Who this is for.** Developers who can already write a little code (Python, JavaScript, Java — anything) and want a structured, principled introduction to SQL and relational databases. No prior database experience required. If you've used spreadsheets and want to graduate to real query languages, you're in the right place.

**What you'll learn.** The relational model; DDL (`CREATE`, `ALTER`, `DROP`); DML (`INSERT`, `UPDATE`, `DELETE`); DQL (`SELECT`) with `WHERE`, `LIKE`, `BETWEEN`, `IN`; sorting and pagination (`ORDER BY`, `LIMIT`, `OFFSET`, `DISTINCT`); aggregation (`COUNT`, `SUM`, `AVG`, `GROUP BY`, `HAVING`); joins (`INNER`, `LEFT`, `CROSS`, self-joins); subqueries and views; transactions; indexes and `EXPLAIN QUERY PLAN`; SQL injection defense; and normalized schema design.

**How long it takes.** Roughly 10-15 hours of self-paced reading + listening, plus 1-3 hours per day if you work the assignments and quizzes. The course is structured for one day per module, but nothing forces that pace.

**Prefer offline?** Each release also ships as a self-contained zip in [`dist/`](dist/). Unzip and open `index.html` in any browser.

**Tooling needed.** Just the `sqlite3` CLI:

- Ubuntu/Debian: `sudo apt install sqlite3`
- macOS: already included (or `brew install sqlite3`)
- Arch Linux: `sudo pacman -S sqlite`

---

## What's in this repo

Source of truth for the course plus every tool that produces it:

```
SQL_Fundamentals/
├── source/                 # Markdown source for all 10 modules
├── images/                 # 43 illustrations, organized by module
├── audio/                  # 107 narration MP3s + per-module manifest.json
├── Quiz/                   # 10 quiz JSON banks (250 questions total, 25 per day)
├── Day_XX_*/               # Per-day assignment + desktop quiz launcher folders
├── scripts/                # Build and generation scripts (see pipeline below)
├── html/                   # Generated per-module HTML (gitignored, rebuilt on deploy)
├── dist/                   # Distribution zips for offline students
├── .github/workflows/      # GitHub Pages deploy workflow
├── IMAGE-PLAN.md           # Gemini prompts for every illustration
├── COURSE-BUILDER-GUIDE.md # Authoritative documentation for the build pipeline
├── CLAUDE.md               # Project instructions for Claude Code sessions in this repo
├── Gradebook.md            # Desktop quiz runner writes scores here
└── README.md               # You are here
```

---

## How this course was built (the pipeline)

This is the section for builders. It walks through the actual sequence that produced every page you see live. The pattern is shared across the [Stonewaters Consulting intern portfolio](https://github.com/beekeeper-lab) but SQL Fundamentals is the most-complete reference implementation: 100% narration coverage, fully embedded media, ae101-aligned chrome.

### 1. Content authored in markdown

Everything starts in `source/*.md`. Each day-module is one file named `module-XX-topic.md` (zero-padded, `module-00` through `module-09`). Pages are separated by `## ` headings; the HTML builder paginates automatically.

A typical module file contains:

- **Tier badge** — `> 🏷️ Start Here` (or `Useful Soon`, `When You're Ready`, `Advanced`) to signal difficulty.
- **Teaching intents** per section — `> 🎯 **Teach:**`, `> **See:**`, `> **Feel:**` lines that state the objective before the prose.
- **Where-this-fits callouts** — `> 🔄 **Where this fits:**` to anchor the module to the relational/SQL big picture.
- **Inline illustrations** — `![alt](../images/module-XX/name-01.png)` + a caption on the next line.
- **Narration blocks** — `> 🎙️ Welcome to Module 0...` blockquotes are picked up by the narration pipeline and spoken aloud on the page.
- **Remember-this callouts** — `> 💡 **Remember this one thing:** ...` for the load-bearing takeaway from each section.
- **Runnable SQL** — fenced ` ```sql` blocks with input data and expected output, designed to be pasted into `sqlite3`.

### 2. Illustration generation via Gemini

All 43 illustrations are generated by **Google Gemini** (`gemini-3-pro-image-preview`, nicknamed "Nano Banana") from prompts catalogued in [`IMAGE-PLAN.md`](IMAGE-PLAN.md).

**Process:**

1. Write the image into the content file as `![alt](../images/module-XX/name-01.png)` — the file doesn't exist yet.
2. Add a corresponding entry in `IMAGE-PLAN.md` with the Gemini prompt (Head First illustration style, 16:9, white background, minimal text).
3. Run `uv run --with google-genai python scripts/generate_images.py` — the script parses the plan, finds entries whose PNG doesn't yet exist, and generates each via Gemini. Includes 429-retry, rate-limit handling, `--dry-run`, `--filter`, and `--force`.
4. Rebuild the course; `build_course.py` inlines every PNG as a base64 data URI so the distribution zip is fully offline-capable.

The IMAGE-PLAN doubles as documentation: every image has a canonical prompt that can be re-generated, tweaked, or restyled.

### 3. Narration generation via ElevenLabs

Every `> 🎙️ ...` block in source markdown becomes an MP3 file, spoken by the **ElevenLabs Rachel voice**. SQL Fundamentals ships with **100% narration coverage** — every page in every module has at least one narration block, and 19 new narration scripts were added during the final polish pass to close the last remaining gaps.

**Process:**

1. Author narration inline in the markdown, one `> 🎙️` block per teaching beat (typically 2-4 sentences).
2. Run `uv run --with elevenlabs python scripts/generate_narration.py` — the script parses every source file's narration blocks, numbers them by position, and generates MP3s into `audio/<module-slug>/NN_<module-slug>.mp3`.
3. Each module has an `audio/<module-slug>/manifest.json` recording which text each MP3 corresponds to. The script also supports `--regenerate-changed` to detect drift between text and audio.

**Important behavior:** because narrations are numbered by position, **inserting a narration mid-file shifts every subsequent narration's index**, which triggers cascade re-records. Plan inserts at the end of a module when possible.

In the live build, audio plays inline in the browser via `<audio>` players embedded next to the prose, with a hush toggle and autoplay-on-page-advance (with click-to-start fallback when the browser blocks autoplay).

### 4. HTML build and deploy

`scripts/build_course.py` renders every source markdown file into an HTML page using `scripts/module_template.html`. Outputs go to `html/` (gitignored) plus `index.html` at the repo root.

What the build does:

- Markdown → HTML via Python-Markdown + Pygments for SQL syntax highlighting.
- Paginates each module at every `## ` heading.
- Embeds every image as a base64 data URI.
- Processes custom blocks: narration players, teaching-intent accordion cards, tier badges, remember banners.
- Injects a Day Quiz page per module (second-to-last, before the wrap-up) with the matching quiz JSON embedded inline.

The chrome (sidebar, theme toggle, narration runtime, quiz embed) is aligned with the agentic-engineering-101 reference course, with a course-specific `isNewPage` scroll optimization and `sql_fund_*` `localStorage` keys (kept stable across releases for backward compatibility with returning students).

**Deployment** is via [`.github/workflows/pages.yml`](.github/workflows/pages.yml). Every push to `main` triggers a GitHub Actions run that rebuilds the course and publishes to GitHub Pages. Cost: $0 on public repos.

For offline distribution, `scripts/deploy.py` produces a self-contained zip that includes `index.html`, all `html/`, and all referenced media inlined as base64.

### 5. Quizzes

Two runners, one set of questions. Both read the same JSON banks at `Quiz/Day_XX_Quiz_File/day_XX_quiz.json` (10 files, **25 questions each, 250 total**, 80% passing).

**Note on numbering.** Source modules use the zero-indexed `module-00` … `module-09` convention from the build pipeline; quiz folders and Day folders use the one-indexed `Day_01` … `Day_10` convention used elsewhere in the portfolio. The mapping is `module-NN` ↔ `Day_{NN+1}` (so `module-00-what-is-sql.md` pairs with `Quiz/Day_01_Quiz_File/day_01_quiz.json` and `Day_01_What_Is_SQL/`).

- **In-browser quiz.** Each module's built HTML has an embedded `<script type="application/json" id="quiz-data">` block with the full quiz, plus a JS runner (`sql_quiz_*` namespace) that paints into the Day Quiz page. Timer, shuffle, submit/timeout, review-answers summary, retake. Scores persisted in `localStorage` per day.
- **Desktop tkinter quiz.** The shared `quiz_app.py` at the portfolio root (sibling to this repo) provides a full-screen quiz window. Results write to [`Gradebook.md`](Gradebook.md). Launcher scripts at `Day_XX_*/run_quiz.{py,sh,bat}` invoke it with the right arguments.

```bash
# From the portfolio root:
python quiz_app.py SQL_Fundamentals 1     # Day 1 quiz
# Or from any Day folder:
python Day_01_What_Is_SQL/run_quiz.py
```

---

## Running the pipeline locally

All scripts use [`uv`](https://github.com/astral-sh/uv) for dependency management — no virtualenv setup required. Commands run from the repo root.

```bash
# 1. Build the course HTML (rebuild any time source changes)
uv run --with markdown --with pygments python scripts/build_course.py

# 2. Generate any missing illustrations (skips images that already exist)
uv run --with google-genai python scripts/generate_images.py

# 3. Generate narration audio (only generates missing or changed files)
uv run --with elevenlabs python scripts/generate_narration.py

# 4. Regenerate audio for narrations whose text changed since last run
uv run --with elevenlabs python scripts/generate_narration.py --regenerate-changed

# 5. Build the distribution zip (self-contained, browser-offline)
uv run --with markdown --with pygments python scripts/deploy.py --version 1.0

# 6. Run any day's quiz in the desktop tkinter app
python ../quiz_app.py SQL_Fundamentals 1
# ...or via launcher...
python Day_01_What_Is_SQL/run_quiz.py
```

**API keys needed** (only for generation scripts, not for building or reading):

- `GEMINI_API_KEY` for image generation (read from the repo's `.env` or the parent directory's `.env` — never committed)
- `ELEVENLABS_API_KEY` for narration

Reading the course and rebuilding the HTML requires **no API keys**. All generated assets are committed, so anyone who clones the repo can build and browse immediately.

---

## Repository map

A one-screen view of what lives where:

```
.github/workflows/pages.yml    # CI: build + deploy to GitHub Pages on push
CLAUDE.md                       # Instructions for Claude Code in this repo
COURSE-BUILDER-GUIDE.md         # Full build pipeline documentation
Gradebook.md                    # Desktop quiz runner writes scores here
IMAGE-PLAN.md                   # All Gemini prompts for the 43 illustrations
README.md                       # You are here
favicon.png                     # Course favicon

source/                         # Course content (markdown → HTML)
└── module-00..module-09        # 10 day-modules

images/                         # 43 PNGs + sibling JSON metadata
│                               # subdirs: module-00..module-09
│
audio/                          # 107 MP3s + manifest.json per module
│                               # subdirs match source file slugs
│
Quiz/                           # 10 quiz JSON banks (25 Q each, 250 total)
└── Day_XX_Quiz_File/day_XX_quiz.json

Day_XX_Topic/                   # Per-day assignment + desktop quiz launchers
├── Assignment_XX_*.md
└── run_quiz.{py,sh,bat}

scripts/                        # Build + generation pipeline
├── build_course.py             # Markdown → HTML + index
├── deploy.py                   # Build + bundle into dist/ zip
├── generate_images.py          # IMAGE-PLAN.md + Gemini → PNGs
├── generate_narration.py       # 🎙️ blocks + ElevenLabs → MP3s
└── module_template.html        # HTML shell with runtime JS/CSS
```

---

## Design philosophy worth stealing

If you're building your own narrated, illustrated, self-paced technical course, these are the choices in this repo that paid off:

1. **Everything is markdown.** One source of truth. Narrators, illustrators, the HTML builder, and the quiz embed all read the same files. Editing is `vim source/module-06-joins.md`, not round-tripping through a CMS.
2. **Every asset has a plan.** Illustrations are catalogued in `IMAGE-PLAN.md` with the exact Gemini prompt. Narrations live in `🎙️` blocks inside the prose. Re-generating any asset is deterministic and cheap.
3. **One runner, many courses.** The desktop quiz runner (`quiz_app.py`) is shared across the whole portfolio. One bug fix, eight courses benefit.
4. **Embedded over linked.** Images and audio are base64-inlined in the HTML so the offline zip works without any external dependencies. `localStorage` persistence keeps progress private and backendless.
5. **Graceful degradation.** Narration auto-plays by default but shows a click-to-start banner when browsers block autoplay. Quizzes fall back to the desktop runner if a student prefers full-screen. No feature assumes the runtime environment is ideal.
6. **Backward-compat keys.** `localStorage` keys are namespaced (`sql_fund_*`) and stable across releases so returning students don't lose progress when the course rebuilds.

---

## Status and maintenance

**Shipped — April 2026.** SQL Fundamentals is feature-complete and is currently the most-polished course in the Stonewaters Consulting intern portfolio:

- 100% narration coverage across all 10 modules (107 MP3s).
- 43 hand-prompted Gemini illustrations.
- 250 quiz questions (10 days × 25), embedded in-browser and runnable on desktop.
- Free public hosting on GitHub Pages; the deployed URL is the one at the top of this README.
- Used as the reference implementation when polishing the other intern courses.

The course content tracks ANSI/portable SQL with SQLite-specific notes where they matter; updates are expected to be small and infrequent.

---

## Credits and source material

The course's substantive content is the author's original work, drawing on standard SQL references (the SQL:2016 standard for portability notes, the SQLite documentation for engine-specific behavior) and a decade of teaching SQL to Purdue CIT undergraduates and Stonewaters Consulting interns.

Illustrations generated via **Google Gemini** (`gemini-3-pro-image-preview`). Narrations generated via **ElevenLabs** (Rachel voice). Built and maintained as part of the **Stonewaters Consulting** internship curriculum portfolio.

**Questions, issues, pull requests** → use the GitHub Issues and Pull Requests tabs of this repo. The repo is public; contributions are welcome.
