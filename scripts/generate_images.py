#!/usr/bin/env python3
"""Generate illustrations for the SQL Fundamentals course using Google Gemini."""

import json
import os
import sys
import time
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
IMAGES_DIR = PROJECT_ROOT / "images"


def get_api_key() -> str:
    key = os.environ.get("GEMINI_API_KEY")
    if not key:
        env_path = PROJECT_ROOT / ".env"
        if env_path.exists():
            for line in env_path.read_text().splitlines():
                if line.startswith("GEMINI_API_KEY="):
                    key = line.split("=", 1)[1].strip().strip('"').strip("'")
                    break
    if not key:
        print("ERROR: GEMINI_API_KEY not set")
        sys.exit(1)
    return key


def generate_image(prompt: str, output_path: Path, api_key: str) -> bool:
    """Generate an image using Gemini API."""
    try:
        from google import genai
        from google.genai import types
    except ImportError:
        print("ERROR: google-genai not installed. Run: pip install google-genai")
        sys.exit(1)

    if output_path.exists():
        print(f"  SKIP (exists): {output_path.name}")
        return True

    client = genai.Client(api_key=api_key)

    full_prompt = (
        f"editorial illustration for a programming textbook. "
        f"{prompt} "
        f"Head First book illustration style, clean lines, slightly whimsical "
        f"and humorous, warm colors, educational. Simple and clear. "
        f"White background. Minimal or no text in the image."
    )

    try:
        result = client.models.generate_images(
            model="imagen-4.0-generate-001",
            prompt=full_prompt,
            config=types.GenerateImagesConfig(
                number_of_images=1,
            ),
        )

        if result.generated_images:
            img = result.generated_images[0].image
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_bytes(img.image_bytes)

            # Save metadata
            meta_path = output_path.with_suffix(".json")
            meta_path.write_text(json.dumps({
                "prompt": prompt,
                "full_prompt": full_prompt,
                "model": "imagen-4.0-generate-001",
                "file": output_path.name,
                "generated": time.strftime("%Y-%m-%dT%H:%M:%SZ"),
            }, indent=2))

            size_kb = output_path.stat().st_size / 1024
            print(f"  OK: {output_path.name} ({size_kb:.0f} KB)")
            return True

        print(f"  FAIL (no image in response): {output_path.name}")
        return False

    except Exception as e:
        print(f"  FAIL ({e}): {output_path.name}")
        return False


# All images to generate: (output_path_relative_to_images_dir, prompt)
IMAGES = [
    # Module 0: What Is SQL?
    ("module-00/m00-hero-database-welcome-01.png",
     "A friendly robot librarian standing at a big ornate filing cabinet, holding a magnifying glass in one hand and a folder in the other, with a 'Welcome' banner above. The cabinet drawers are labeled with table names. Warm, inviting scene."),

    ("module-00/m00-filing-cabinet-analogy-01.png",
     "A split view: on the left, a traditional metal filing cabinet with labeled drawers (Employees, Departments, Orders). On the right, the same structure shown as a simple database diagram with boxes and arrows. An equals sign connects them."),

    ("module-00/m00-table-visualization-01.png",
     "A database table shown as a colorful spreadsheet-like grid with column headers (id, name, email, department) and 5 rows of sample data. Arrows label 'columns' pointing to the headers and 'rows' pointing to the data entries."),

    ("module-00/m00-sql-categories-01.png",
     "Three workers at a construction site, each wearing a hard hat with a different label: DDL (holding blueprints), DML (carrying bricks and mortar), and DQL (holding binoculars/magnifying glass). They represent Define, Manipulate, and Query."),

    # Module 1: Creating Tables
    ("module-01/m01-hero-blueprint-01.png",
     "An architect at a drafting table rolling out a blueprint, but the blueprint shows a database table schema instead of a building -- column names, data types, and constraint annotations are visible on the paper."),

    ("module-01/m01-five-data-types-01.png",
     "Five labeled containers/jars on a shelf, each holding a different type of content: INTEGER (jar of numbered balls), REAL (jar with a measuring beaker showing 3.14), TEXT (jar of alphabet letters), BLOB (jar of mixed colorful objects), NULL (an empty transparent jar)."),

    ("module-01/m01-constraint-bouncers-01.png",
     "A nightclub entrance with several bouncers at the door, each wearing a name tag: NOT NULL (turning away an empty ghost), UNIQUE (checking IDs against a list), CHECK (holding a measuring tape), PRIMARY KEY (wearing a VIP badge), DEFAULT (handing a visitor a default name tag)."),

    ("module-01/m01-foreign-key-arrows-01.png",
     "Three tables shown as connected bulletin boards: Students, Courses, and Enrollments in the middle. Red string/yarn connects pins on the Enrollments board to matching pins on Students and Courses, like a detective's evidence board."),

    # Module 2: Inserting Data
    ("module-02/m02-hero-filling-forms-01.png",
     "A person at a desk enthusiastically filling out forms and dropping them into a colorful inbox/database slot. Completed forms float down into neatly organized table rows below."),

    ("module-02/m02-insert-as-form-01.png",
     "A paper form with fields (first_name, last_name, email, gpa) being filled out with a pen. An arrow shows the completed form sliding into a filing drawer labeled 'students table'."),

    ("module-02/m02-null-vs-zero-vs-empty-01.png",
     "Three boxes side by side: one labeled 'NULL' is completely transparent/see-through (nothing inside), one labeled '0' has a big zero in it, one labeled 'empty string' has an empty speech bubble. Below reads 'These are NOT the same thing'."),

    ("module-02/m02-conflict-handling-01.png",
     "A mail sorting scenario with three paths: a letter arrives at a mailbox. Path 1 labeled 'ERROR' shows the letter bouncing back. Path 2 labeled 'IGNORE' shows the letter being quietly shredded. Path 3 labeled 'REPLACE' shows the old letter being removed and the new one taking its place."),

    # Module 3: SELECT and Filtering
    ("module-03/m03-hero-detective-01.png",
     "A detective with a magnifying glass examining rows of data on a large table/whiteboard. Some rows are highlighted in yellow (matching the search criteria) while others are grayed out."),

    ("module-03/m03-where-funnel-01.png",
     "A large funnel: many colored data rows enter from the top, and the funnel is labeled 'WHERE clause'. Only a few matching rows come out the bottom, while rejected rows bounce off the sides."),

    # Module 4: Sorting and Limiting
    ("module-04/m04-hero-sorted-cards-01.png",
     "Hands sorting playing cards that have database records on them instead of suits. Cards are being arranged from highest GPA to lowest, with some cards being placed in a 'Top 5' section."),

    ("module-04/m04-pagination-pages-01.png",
     "A book lying open, but each page shows a 'page' of database results (5 rows each). Page tabs at the bottom are labeled Page 1, Page 2, Page 3. An arrow labeled 'OFFSET' points to where the next page starts."),

    # Module 5: Aggregate Functions
    ("module-05/m05-hero-zoom-out-01.png",
     "A person looking through binoculars turned backwards -- zooming out from individual trees to see the whole forest. The trees have numbers on them, and floating above the forest are summary statistics: COUNT, AVG, SUM."),

    ("module-05/m05-group-by-mms-01.png",
     "A pile of M&M candies being sorted into separate bowls by color. Each bowl has a label showing the count. One hand is sorting them, another is writing counts on a notepad. Label: GROUP BY color."),

    ("module-05/m05-where-vs-having-01.png",
     "A two-stage assembly line: Stage 1 (labeled WHERE) shows individual items being filtered on a conveyor belt. Stage 2 (labeled HAVING) shows grouped boxes being checked. An arrow shows the flow: filter rows first, then filter groups."),

    # Module 6: Joins
    ("module-06/m06-hero-puzzle-pieces.png",
     "Two large puzzle pieces clicking together, each piece showing part of a database table. The left piece shows student names, the right shows course names, and where they connect shows the enrollment data linking them."),

    ("module-06/m06-inner-join-venn.png",
     "A Venn diagram with two overlapping circles. Left circle labeled 'Students', right circle labeled 'Courses'. The overlap is brightly colored and labeled 'INNER JOIN -- matched rows only'. People icons in the overlap are connected to course books."),

    ("module-06/m06-left-join-venn.png",
     "A Venn diagram where the entire left circle (Students) is brightly colored, including the non-overlapping part. The overlap with Courses is also colored. Students in the non-overlapping left area look lonely, holding NULL signs."),

    ("module-06/m06-cross-join-grid.png",
     "A grid/matrix showing every student paired with every course -- like a speed dating chart. Arrows connect every person on the left to every item on the right, creating a dense web. Label: 'CROSS JOIN: everyone meets everyone'."),

    # Module 7: Subqueries and Views
    ("module-07/m07-hero-nesting-dolls.png",
     "Russian nesting dolls (matryoshka), but each doll has a SQL query written on it. The outermost doll shows SELECT, the middle shows a subquery, and the innermost shows another nested query. They're partially opened to show the nesting."),

    # Module 8: Updating and Deleting
    ("module-08/m08-hero-red-button-01.png",
     "A big red button labeled 'DELETE' under a glass case with a warning sign. A developer's hand hovers nearby hesitantly. A smaller green button labeled 'SELECT first!' is next to it with a checkmark."),

    ("module-08/m08-parachute-check-01.png",
     "A skydiver carefully checking their parachute before jumping. The parachute pack is labeled 'SELECT * WHERE...' and the airplane door has a sign saying 'Always test before you leap (DELETE)'."),

    ("module-08/m08-empty-table-tumbleweed-01.png",
     "A desolate desert scene with a tumbleweed rolling through. In the background, an empty database table stands like an abandoned building with a sign: 'DELETE FROM students; -- oops, forgot WHERE'. Dark humor."),

    ("module-08/m08-bank-transfer-01.png",
     "Two bank vaults with money being transferred between them. One side shows -$500 (withdrawal) and the other shows +$500 (deposit). A safety rope labeled 'TRANSACTION' connects both operations. Below: 'Both succeed or both fail.'"),

    # Module 9: Indexes and Best Practices
    ("module-09/m09-hero-magnifying-glass-01.png",
     "A person holding a magnifying glass over a database, examining its internal structure. Visible through the magnifying glass: an organized B-tree index structure, while the rest of the database looks like unsorted rows."),

    ("module-09/m09-textbook-index-01.png",
     "An open textbook with the index page visible in the back. The index entries have database column names instead of topics (email: page 42, major: page 87). An arrow connects an index entry to the right page. Label: 'Same idea, different scale'."),

    ("module-09/m09-sql-injection-letter-01.png",
     "A hand slipping a forged letter into a mail slot. The letter reads 'Dear Database, DROP TABLE students; --'. A security guard labeled 'Parameterized Query' is blocking a second attempt, holding a shield."),
]


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Generate illustrations for SQL Fundamentals course")
    parser.add_argument("--force", action="store_true", help="Regenerate existing images")
    parser.add_argument("--module", help="Only generate for a specific module (e.g., module-00)")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be generated")
    args = parser.parse_args()

    api_key = get_api_key()

    images = IMAGES
    if args.module:
        images = [(p, prompt) for p, prompt in IMAGES if p.startswith(args.module)]

    print(f"Generating {len(images)} images...")
    success = 0
    skipped = 0
    failed = 0

    for rel_path, prompt in images:
        output_path = IMAGES_DIR / rel_path

        if output_path.exists() and not args.force:
            print(f"  SKIP (exists): {rel_path}")
            skipped += 1
            continue

        if args.dry_run:
            print(f"  WOULD GENERATE: {rel_path}")
            print(f"    Prompt: {prompt[:80]}...")
            continue

        if generate_image(prompt, output_path, api_key):
            success += 1
        else:
            failed += 1

        # Rate limiting
        time.sleep(2)

    print(f"\nDone: {success} generated, {skipped} skipped, {failed} failed")


if __name__ == "__main__":
    main()
