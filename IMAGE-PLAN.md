# Image Plan

Total proposed images: 85
Already generated: 43
New images needed: 42 (2026-04-22 audit additions below)

---

## Cost Log

| Date | Model | Images | Total Size | Cost/Image | Total Cost |
|------|-------|--------|------------|------------|------------|
| 2026-04-08 | imagen-4.0-generate-001 | 31 (initial batch) | ~21 MB | ~$0.04 | ~$1.24 |
| 2026-04-09 | nano-banana-pro-preview | 12 (from this plan) | 6.6 MB | ~$0.14 | $1.68 |
| | | **43 total** | **~28 MB** | | **~$2.92** |
| 2026-04-22 | (pending) | 42 (audit additions) | TBD | ~$0.14 est | ~$5.88 est |

---

## Module 00: What Is SQL?

### Image 1: Hero -- Welcome to Databases
- **File**: `images/module-00/m00-hero-database-welcome-01.png`
- **Page**: Title / intro section
- **Placement**: after module title and "Start Here" tag
- **Description**: A welcoming, friendly illustration introducing the world of databases. Sets an approachable tone for absolute beginners.
- **Status**: Generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: A friendly robot librarian welcoming a newcomer into a bright, organized digital library filled with glowing tables and filing cabinets
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

### Image 2: Filing Cabinet Analogy
- **File**: `images/module-00/m00-filing-cabinet-analogy-01.png`
- **Page**: "So what IS a database, anyway?" section
- **Placement**: after the filing cabinet bullet-point analogy
- **Description**: Shows a filing cabinet mapped to database concepts -- the cabinet is the database, drawers are tables, labels are column names, folders are rows. Helps learners connect a familiar physical object to abstract database structure.
- **Status**: Generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: A labeled filing cabinet where each drawer is open showing folders, with callout labels mapping cabinet to database, drawer to table, folder to row
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

### Image 3: Table Visualization
- **File**: `images/module-00/m00-table-visualization-01.png`
- **Page**: "Tables: The Heart of Everything" section
- **Placement**: after the employees table example
- **Description**: A visual representation of a database table that looks like a spreadsheet, showing columns across the top and rows down, reinforcing that tables are just structured grids of data.
- **Status**: Generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: A colorful, friendly-looking spreadsheet-style grid with column headers highlighted at the top and rows of data below, with arrows labeling columns and rows
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

### Image 4: SQL Categories
- **File**: `images/module-00/m00-sql-categories-01.png`
- **Page**: "Enter SQL: Speaking Database" section
- **Placement**: after the DDL/DML/DQL table
- **Description**: Shows the three categories of SQL as three characters or zones -- DDL as an architect building structure, DML as movers carrying data in and out, DQL as a detective asking questions. Helps learners remember the three flavors of SQL.
- **Status**: Generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: Three distinct characters side by side -- an architect with blueprints (DDL), a moving crew carrying boxes (DML), and a detective with a magnifying glass (DQL)
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

---

## Module 01: Creating Tables

### Image 1: Hero -- Blueprint
- **File**: `images/module-01/m01-hero-blueprint-01.png`
- **Page**: Title / intro section
- **Placement**: after module title and "Start Here" tag
- **Description**: A data architect holding blueprints, setting the tone that this module is about designing the structure and rules for tables. Bridges the construction metaphor used throughout the module.
- **Status**: Generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: A cheerful person in a hard hat studying a large blueprint labeled with column names and data types, standing next to a half-built table structure
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

### Image 2: Five Data Types
- **File**: `images/module-01/m01-five-data-types-01.png`
- **Page**: "The Five Types of Data SQLite Understands" section
- **Placement**: after the storage class table
- **Description**: Shows the five SQLite storage classes (INTEGER, REAL, TEXT, BLOB, NULL) as five distinct, friendly icons or containers. Reinforces simplicity -- only five types to remember.
- **Status**: Generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: Five labeled containers or bins in a row, each holding a representative object -- whole numbers, decimal numbers, text strings, binary blobs, and an empty bin with a question mark for NULL
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

### Image 3: Constraint Bouncers
- **File**: `images/module-01/m01-constraint-bouncers-01.png`
- **Page**: "Constraints: Your Data's Bodyguards" section
- **Placement**: after the bouncer analogy introduction
- **Description**: Constraints depicted as nightclub bouncers at a velvet rope, each checking a different rule -- PRIMARY KEY checks ID, NOT NULL checks you exist, UNIQUE checks you are not already inside, CHECK validates your data. Makes abstract constraint rules tangible and memorable.
- **Status**: Generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: A line of bouncers at a nightclub door, each wearing a label (PRIMARY KEY, NOT NULL, UNIQUE, CHECK), inspecting data trying to enter
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

### Image 4: Foreign Key Arrows
- **File**: `images/module-01/m01-foreign-key-arrows-01.png`
- **Page**: "Table-Level Constraints" section, Foreign Keys subsection
- **Placement**: after the FOREIGN KEY SQL example
- **Description**: Shows two or three tables connected by arrows representing foreign key relationships. The enrollments table points to both students and courses tables, illustrating how foreign keys create valid cross-table references.
- **Status**: Generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: Three simplified tables (students, enrollments, courses) with colorful arrows connecting foreign key columns to primary key columns, showing the relational links
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

---

## Module 02: Inserting Data

### Image 1: Hero -- Filling Forms
- **File**: `images/module-02/m02-hero-filling-forms-01.png`
- **Page**: Title / intro section
- **Placement**: after module title and "Start Here" tag
- **Description**: Someone filling out paper forms to represent inserting data into tables. Sets the metaphor that INSERT is like completing a form with field labels and values.
- **Status**: Generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: A person at a desk filling out a stack of paper forms, with each form field mapping to a database column, papers flowing into a filing cabinet
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

### Image 2: INSERT as Form
- **File**: `images/module-02/m02-insert-as-form-01.png`
- **Page**: "INSERT: The Basic Form" section
- **Placement**: after the INSERT anatomy table
- **Description**: A side-by-side visual showing an INSERT statement mapped to a physical form -- column names are field labels, VALUES are what you write in the blanks. Helps learners see the SQL syntax as a familiar paper form.
- **Status**: Generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: A paper form on the left with labeled fields (first_name, last_name, email), and on the right the same information formatted as an INSERT SQL statement, with matching arrows
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

### Image 3: NULL vs Zero vs Empty
- **File**: `images/module-02/m02-null-vs-zero-vs-empty-01.png`
- **Page**: "NULL: The Billion-Dollar Misunderstanding" section
- **Placement**: after the three INSERT examples showing NULL, 0.0, and empty string
- **Description**: Three distinct visual representations side by side -- NULL as a shrug or question mark (unknown), zero as a definite "0" answer, and empty string as an empty box. Clarifies a critical distinction that causes real bugs.
- **Status**: Generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: Three side-by-side boxes -- one with a large shrug/question mark labeled NULL, one with a bold zero labeled 0, and one completely empty but with visible borders labeled empty string
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

### Image 4: Conflict Handling
- **File**: `images/module-02/m02-conflict-handling-01.png`
- **Page**: "Conflict Handling: When Data Fights Back" section
- **Placement**: after the three conflict strategy descriptions
- **Description**: Shows three responses to a duplicate form submission -- reject it (error), ignore it (skip), or replace the old one (swap). Makes the three INSERT conflict strategies visually distinct and memorable.
- **Status**: Generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: Three panels showing a form being submitted to a doorway -- panel 1 gets a red X (rejected), panel 2 the form dissolves (ignored), panel 3 the old form is swapped for the new one (replaced)
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

---

## Module 03: SELECT and Filtering

### Image 1: Hero -- Detective
- **File**: `images/module-03/m03-hero-detective-01.png`
- **Page**: Title / intro section
- **Placement**: after module title and "Useful Soon" tag
- **Description**: A detective with a magnifying glass examining a spreadsheet, setting the tone that SELECT is about interrogating your data and finding answers.
- **Status**: Generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: A detective in a trench coat peering through a magnifying glass at a large spreadsheet, with highlighted rows glowing
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

### Image 2: WHERE Funnel
- **File**: `images/module-03/m03-where-funnel-01.png`
- **Page**: "WHERE: Your Search Filter" section
- **Placement**: before the first WHERE code example
- **Description**: A funnel diagram where all rows enter the top and only matching rows come out the bottom. Visually demonstrates that WHERE filters rows based on conditions.
- **Status**: Generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: A large funnel with many colorful data rows pouring in from the top and only a few matching rows emerging from the narrow bottom, with a WHERE label on the funnel
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

### Image 3: Logical Operators Venn Diagram
- **File**: `images/module-03/m03-logical-operators-venn-01.png`
- **Page**: "Logical Operators: Combining Conditions" section
- **Placement**: after the AND/OR/NOT explanations, before the parentheses subsection
- **Description**: A Venn diagram showing AND as the overlap of two circles, OR as the union of both circles, and NOT as everything outside a circle. Provides a visual reference for how logical operators combine conditions, which is a concept students often struggle with.
- **Status**: Generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: Three small Venn diagrams side by side -- first showing the shaded intersection labeled AND, second showing both circles fully shaded labeled OR, third showing the area outside one circle shaded labeled NOT
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

### Image 4: LIKE Wildcards Pattern Matching
- **File**: `images/module-03/m03-like-wildcards-01.png`
- **Page**: "LIKE: Fuzzy Pattern Matching" section
- **Placement**: after the wildcards table showing % and _
- **Description**: A visual showing how the % wildcard matches any number of characters and the _ wildcard matches exactly one character, using letter tiles or blocks to demonstrate patterns like 'J%' and '_ohn'. Makes the abstract wildcard concept concrete and visual.
- **Status**: Generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: A row of letter tiles on a game board, with some tiles replaced by wildcard symbols -- a percent sign stretching across multiple tile spaces and an underscore fitting exactly one tile space, with example matches shown below
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

---

## Module 04: Sorting and Limiting

### Image 1: Hero -- Sorted Cards
- **File**: `images/module-04/m04-hero-sorted-cards-01.png`
- **Page**: Title / intro section
- **Placement**: after module title and "Useful Soon" tag
- **Description**: A messy pile of index cards next to a neatly sorted stack, illustrating the difference between unsorted and sorted query results. Communicates that the same data becomes far more useful when organized.
- **Status**: Generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: On the left, a chaotic scattered pile of index cards; on the right, the same cards neatly sorted in a clean stack, with a satisfied person admiring the sorted version
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

### Image 2: Pagination Pages
- **File**: `images/module-04/m04-pagination-pages-01.png`
- **Page**: "OFFSET: Skipping Ahead" section
- **Placement**: after the three pagination query examples
- **Description**: A visual showing pages of results like a book or catalog, with page numbers at the bottom. Each page represents a different OFFSET with the same LIMIT, making the pagination formula intuitive.
- **Status**: Generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: Three overlapping pages of search results labeled Page 1, Page 2, Page 3, with rows of data visible on each, and navigation buttons at the bottom showing Previous/Next
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

### Image 3: Multi-Column Sort Tiebreaker
- **File**: `images/module-04/m04-multi-column-sort-01.png`
- **Page**: "Multi-Column Sorting: The Tiebreaker" section
- **Placement**: after the card-sorting analogy text block
- **Description**: A visual showing a hand of playing cards being sorted first by suit, then by value within each suit. Demonstrates the tiebreaker concept of multi-column ORDER BY where the second column only matters when the first has a tie.
- **Status**: Generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: A hand of playing cards being sorted in two steps -- first grouped by suit into four piles, then within each pile sorted by number value, with arrows showing the two-level sorting process
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

### Image 4: DISTINCT Deduplication
- **File**: `images/module-04/m04-distinct-dedup-01.png`
- **Page**: "DISTINCT: Removing Duplicates" section
- **Placement**: after the first DISTINCT code example
- **Description**: A visual showing a list of items with many duplicates on the left collapsing into a clean list of unique values on the right. Makes the concept of deduplication immediately clear.
- **Status**: Generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: On the left, a long list with repeated color-coded labels (Biology appears 5 times, CS appears 3 times, etc.); on the right, the same labels appearing exactly once each, with a DISTINCT stamp in between
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

---

## Module 05: Aggregate Functions

### Image 1: Hero -- Zoom Out
- **File**: `images/module-05/m05-hero-zoom-out-01.png`
- **Page**: Title / intro section
- **Placement**: after module title and "Useful Soon" tag
- **Description**: A zoomed-out perspective shifting from individual M&Ms to piles sorted by color, representing the shift from individual rows to aggregate summaries. Sets the tone for thinking about patterns rather than individual data points.
- **Status**: Generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: A zooming-out effect from a single M&M candy to a wide view of M&Ms sorted into colorful piles by color, each pile with a count label
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

### Image 2: GROUP BY M&Ms
- **File**: `images/module-05/m05-group-by-mms-01.png`
- **Page**: "GROUP BY: The Game Changer" section
- **Placement**: before the first GROUP BY code example
- **Description**: M&Ms sorted into piles by color, with each pile counted -- a direct visual metaphor for GROUP BY. Shows how the same bag of candy reveals distribution when grouped.
- **Status**: Generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: A bag of M&Ms spilled onto a table, sorted into distinct piles by color, each pile labeled with its count, showing the grouping process
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

### Image 3: WHERE vs HAVING Pipeline
- **File**: `images/module-05/m05-where-vs-having-01.png`
- **Page**: "HAVING: Filtering Groups" section
- **Placement**: after the HAVING explanation, before the execution order list
- **Description**: A pipeline diagram showing the query execution order -- WHERE filters individual rows before grouping, GROUP BY forms groups, then HAVING filters groups after aggregation. Clarifies one of the most commonly confused distinctions in SQL.
- **Status**: Generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: A horizontal pipeline with three stages -- a WHERE gate filtering individual rows, a GROUP BY station forming rows into colored groups, and a HAVING gate filtering out small groups
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

### Image 4: The Big Five Aggregate Functions
- **File**: `images/module-05/m05-big-five-functions-01.png`
- **Page**: "The Big Five: COUNT, SUM, AVG, MIN, MAX" section
- **Placement**: after the "Combining Them" code example
- **Description**: Five calculator-like icons, each representing one aggregate function -- COUNT shows a tally counter, SUM shows an adding machine, AVG shows a balance scale, MIN shows a downward arrow, MAX shows an upward arrow. Provides a visual cheat sheet for the five core functions.
- **Status**: Generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: Five friendly calculator characters in a row, each with a distinct personality -- COUNT holds a clicker tally, SUM has a plus sign, AVG balances on a scale, MIN points down to the floor, MAX reaches up to the ceiling
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

---

## Module 06: Joins

### Image 1: Hero -- Puzzle Pieces
- **File**: `images/module-06/m06-hero-puzzle-pieces.png`
- **Page**: Title / intro section
- **Placement**: after module title and "When You're Ready" tag
- **Description**: Two puzzle pieces clicking together, representing how joins connect data from separate tables into a unified result. Sets the tone for the defining feature of relational databases.
- **Status**: Generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: Two large, colorful puzzle pieces about to snap together, each piece showing partial table data that becomes complete when connected
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

### Image 2: INNER JOIN Venn Diagram
- **File**: `images/module-06/m06-inner-join-venn.png`
- **Page**: "INNER JOIN: Only the Matched Pairs Dance" section
- **Placement**: before the first INNER JOIN code example
- **Description**: A Venn diagram showing two overlapping circles (tables), with only the intersection shaded -- representing that INNER JOIN returns only rows that match in both tables. The dance metaphor reinforces: no partner, you sit out.
- **Status**: Generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: Two overlapping circles labeled Table A and Table B as a Venn diagram, with only the center overlap region highlighted and filled with matched row pairs
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

### Image 3: LEFT JOIN Venn Diagram
- **File**: `images/module-06/m06-left-join-venn.png`
- **Page**: "LEFT JOIN: Everyone From the Left Gets In" section
- **Placement**: before the first LEFT JOIN code example
- **Description**: A Venn diagram with the entire left circle shaded plus the intersection -- the left table keeps all its rows, with NULLs filling in where no match exists on the right. The inclusive dance metaphor: everyone from the left side gets on the floor.
- **Status**: Generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: Two overlapping circles where the entire left circle and the overlap are highlighted, with the non-overlapping right section faded, and NULL labels where right-side data is missing
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

### Image 4: CROSS JOIN Grid
- **File**: `images/module-06/m06-cross-join-grid.png`
- **Page**: "CROSS JOIN: Speed Dating for Tables" section
- **Placement**: before the first CROSS JOIN code example
- **Description**: A speed-dating grid showing every row from one table paired with every row from another. Five students across the top, four courses down the side, all 20 combinations filled in. Makes the Cartesian product concept visual and the explosive row count obvious.
- **Status**: Generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: A speed-dating event grid with student names across the top and course names down the side, every cell filled in showing all possible pairings, with a large 20 count displayed
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

### Image 5: Self-Join Mirror
- **File**: `images/module-06/m06-self-join-mirror-01.png`
- **Page**: "Self-Joins: Comparing Yourself to Your Classmates" section
- **Placement**: after the self-join introduction, before the first self-join code example
- **Description**: A table looking at itself in a mirror, with the reflection showing the same table under a different alias. Illustrates that a self-join is the same table playing two roles in one query, which is a concept that bends beginners' brains.
- **Status**: Generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: A database table standing in front of a mirror, where its reflection wears a different name tag (alias), and lines connect matching rows between the original and the reflection
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

---

## Module 07: Subqueries and Views

### Image 1: Hero -- Nesting Dolls
- **File**: `images/module-07/m07-hero-nesting-dolls.png`
- **Page**: Title / intro section
- **Placement**: after module title and "When You're Ready" tag
- **Description**: Russian nesting dolls (matryoshka), each containing a smaller SQL query. Sets the tone for the concept of queries nested inside other queries that execute from the inside out.
- **Status**: Generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: A set of Russian nesting dolls being opened, each one revealing a smaller doll inside with a SQL SELECT statement visible, illustrating inside-out query execution
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

### Image 2: Scalar vs List Subquery
- **File**: `images/module-07/m07-scalar-vs-list-01.png`
- **Page**: "List Subqueries: IN and NOT IN" section
- **Placement**: after the guest list analogy introduction
- **Description**: A side-by-side comparison showing a scalar subquery returning a single value (one box, one number) versus a list subquery returning multiple values (a column of values, like a guest list). Helps learners distinguish the two types and know when to use = versus IN.
- **Status**: Generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: On the left, a subquery bubble producing a single number (3.25) being compared with an equals sign; on the right, a subquery bubble producing a list of IDs being checked against with an IN operator and a guest-list clipboard
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

### Image 3: EXISTS -- Knocking on a Door
- **File**: `images/module-07/m07-exists-door-knock-01.png`
- **Page**: "EXISTS and NOT EXISTS" section
- **Placement**: after the knocking-on-a-door analogy
- **Description**: A person knocking on a door -- they do not care who answers, only whether anyone is home. Illustrates that EXISTS is a true/false existence check, not a value lookup. This is a subtle but important distinction from IN.
- **Status**: Generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: A person knocking on a door with a speech bubble saying "Anyone home?" -- behind the door, shadowy figures are visible but their identities are obscured, emphasizing that EXISTS only cares about presence, not specific values
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

### Image 4: Views as Bookmarks
- **File**: `images/module-07/m07-view-bookmark-01.png`
- **Page**: "Views: Save Your Favorite Query as a Virtual Table" section
- **Placement**: after the view introduction, before the CREATE VIEW code
- **Description**: A complex SQL query being bookmarked and saved with a simple name, like placing a bookmark in a thick book. Illustrates that a view is a saved query you can reuse by name, not a copy of data. Helps learners grasp the virtual-table concept.
- **Status**: Generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: A long, complex SQL scroll being bookmarked with a colorful tab labeled with a short view name, and a person later pulling out just the bookmark to instantly access the full query result
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

---

## Module 08: Updating and Deleting Data

### Image 1: Hero -- Red Button
- **File**: `images/module-08/m08-hero-red-button-01.png`
- **Page**: Title / intro section
- **Placement**: after module title and "When You're Ready" tag
- **Description**: A finger hovering over a big red button labeled DELETE, conveying the gravity and permanence of data modification operations. Sets the cautious-but-confident tone for the module.
- **Status**: Generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: A dramatic close-up of a finger hovering over a large, shiny red button on a console, with warning labels around it
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

### Image 2: Parachute Check
- **File**: `images/module-08/m08-parachute-check-01.png`
- **Page**: "The Golden Rule: Test with SELECT First" section
- **Placement**: before the SELECT-first pattern code examples
- **Description**: A skydiver checking their parachute before jumping, representing the safety practice of always running SELECT with the same WHERE clause before UPDATE or DELETE. Reinforces that this precaution is non-negotiable.
- **Status**: Generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: A skydiver carefully inspecting and checking their parachute pack before jumping from a plane, with a checklist in hand
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

### Image 3: Empty Table Tumbleweed
- **File**: `images/module-08/m08-empty-table-tumbleweed-01.png`
- **Page**: "DELETE in Detail" section, nuclear option subsection
- **Placement**: after the "DELETE FROM students" (without WHERE) warning
- **Description**: An empty table with a tumbleweed rolling through, illustrating the aftermath of DELETE without a WHERE clause. Provides a humorous but sobering visual of what happens when you accidentally delete all rows.
- **Status**: Generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: An empty, desolate spreadsheet-style table with a cartoon tumbleweed rolling across the empty rows, and a shocked person in the background
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

### Image 4: Bank Transfer Transaction
- **File**: `images/module-08/m08-bank-transfer-01.png`
- **Page**: "Transactions: Your Undo Button" section
- **Placement**: after the transaction code example, before the bank transfer explanation
- **Description**: A bank transfer diagram showing withdrawal and deposit as one atomic operation -- either both happen or neither does. Makes the concept of transaction atomicity immediately intuitive through the most classic example in database education.
- **Status**: Generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: Two bank account boxes connected by an arrow showing money moving from Account A to Account B, wrapped in a glowing transaction boundary that ensures both sides happen together
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

### Image 5: Pencil vs Permanent Marker
- **File**: `images/module-08/m08-pencil-vs-marker-01.png`
- **Page**: "SELECT is a pencil. UPDATE and DELETE are permanent markers." section
- **Placement**: after the section heading, before the first UPDATE code example
- **Description**: A pencil and a permanent marker side by side, with the pencil labeled SELECT (safe, erasable) and the marker labeled UPDATE/DELETE (permanent, irreversible). Drives home the fundamental safety distinction introduced at the start of the module.
- **Status**: Generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: A pencil with a clean eraser on the left labeled SELECT (with light, erasable marks on paper) and a bold permanent marker on the right labeled UPDATE/DELETE (with thick, permanent marks on a shared whiteboard)
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

---

## Module 09: Indexes and Best Practices

### Image 1: Hero -- Magnifying Glass
- **File**: `images/module-09/m09-hero-magnifying-glass-01.png`
- **Page**: Title / intro section
- **Placement**: after module title and "Advanced" tag
- **Description**: A magnifying glass over a database with speed lines, representing fast, focused searching. Sets the tone for the performance, security, and design topics in this final module.
- **Status**: Generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: A large magnifying glass hovering over a database table, with speed lines radiating outward suggesting fast lookup, and a needle found instantly in a haystack
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

### Image 2: Textbook Index Analogy
- **File**: `images/module-09/m09-textbook-index-01.png`
- **Page**: "Indexes: The Back of the Textbook" section
- **Placement**: after the textbook index analogy explanation
- **Description**: A textbook open to the index page in the back, with a finger pointing to an entry and an arrow jumping straight to the correct page. Contrasts with flipping through every page one by one. Makes the database index concept immediately intuitive.
- **Status**: Generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: An open textbook showing the index page in the back, with a finger pointing to "Photosynthesis -- page 247" and a dotted arrow jumping directly to page 247, contrasted with a faded image of someone flipping through every page
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

### Image 3: SQL Injection Letter
- **File**: `images/module-09/m09-sql-injection-letter-01.png`
- **Page**: "SQL Injection: The Security Hole You Must Close" section
- **Placement**: after the attack example showing the DROP TABLE injection
- **Description**: A forged letter being slipped under a door, representing SQL injection as someone sneaking malicious instructions into your system through an input field. Makes the security vulnerability tangible and memorable.
- **Status**: Generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: A suspicious letter being slipped under a door, with visible malicious SQL code written on it (like DROP TABLE), while an unsuspecting person on the other side picks it up thinking it is a normal form submission
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

### Image 4: Normalization Messy Closet to Organized Shelves
- **File**: `images/module-09/m09-normalization-closet-01.png`
- **Page**: "Normalization: Organizing the Closet" section
- **Placement**: after the section heading, before the messy table example
- **Description**: A before-and-after split image showing a messy closet with everything jumbled together on the left and the same items neatly organized on labeled shelves on the right. Visually introduces normalization as organizing data so each fact has its own place.
- **Status**: Generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: A split image -- on the left, a chaotic closet with shirts, shoes, and coats tangled together in one heap; on the right, the same items neatly sorted onto labeled shelves and hangers, each category in its own section
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

### Image 5: Index Trade-Off Balance
- **File**: `images/module-09/m09-index-tradeoff-balance-01.png`
- **Page**: "When to Index (and When NOT To)" section
- **Placement**: after the "When NOT to create indexes" subsection, before the scenario table
- **Description**: A balance scale with "Fast Reads" on one side and "Slow Writes" on the other, showing the core trade-off of database indexes. Helps learners internalize that indexes are not free and require judgment about when the read benefit outweighs the write cost.
- **Status**: Generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: A balance scale where one side holds a fast rocket labeled "Reads" and the other holds a heavy anchor labeled "Writes," with index cards piled on both sides, showing the trade-off decision
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

---

## Audit Additions -- 2026-04-22

These 42 images fill coverage gaps identified in the 2026-04-22 narration/image audit. All are pending approval and generation.

### Module 00 additions

#### Image 5: Why SQLite (vs. the big dogs)
<!-- orphan: queued for source-side wiring -->
- **File**: `images/module-00/m00-sqlite-vs-big-dogs-01.png`
- **Page**: "Why SQLite? (And What Are the Alternatives?)"
- **Placement**: after the SQLite/MySQL/PostgreSQL comparison table
- **Description**: SQLite as a friendly pocket-sized creature next to hulking server cabinets labeled MySQL and PostgreSQL, emphasizing simplicity vs. setup overhead.
- **Status**: Pending
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: A tiny, friendly SQLite character holding a single file labeled .db, standing next to two big intimidating server cabinets labeled MySQL and PostgreSQL, with the small character smiling confidently
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

#### Image 6: SQLite Shell Command Center
<!-- orphan: queued for source-side wiring -->
- **File**: `images/module-00/m00-shell-command-center-01.png`
- **Page**: "The SQLite Shell: Your Command Center"
- **Placement**: after the two-command-types explanation
- **Description**: The SQLite shell as a control panel with two switches -- one for SQL statements (ending with semicolon), one for dot-commands. Reinforces that the shell has two languages.
- **Status**: Pending
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: A friendly retro control panel with two large labeled switches -- one labeled with a semicolon, the other labeled with a dot -- above them a screen showing a sqlite> prompt
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

#### Image 7: First Database Journey
<!-- orphan: queued for source-side wiring -->
- **File**: `images/module-00/m00-first-database-journey-01.png`
- **Page**: "Let's Do This: Your First Database"
- **Placement**: after the step-by-step CREATE/INSERT/SELECT walkthrough
- **Description**: A four-step journey showing the complete lifecycle -- empty terminal, CREATE TABLE, INSERT, SELECT -- as a celebratory path with a trophy at the end.
- **Status**: Pending
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: Four connected stepping stones across a path, each with a small icon -- empty terminal, table blueprint, folders being loaded, magnifying glass -- leading to a trophy at the end
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

### Module 01 additions

#### Image 5: Self-Documenting Table Blueprint
<!-- orphan: queued for source-side wiring -->
- **File**: `images/module-01/m01-self-documenting-table-01.png`
- **Page**: "Putting It All Together: A Real Table"
- **Placement**: after the students CREATE TABLE example
- **Description**: A CREATE TABLE statement rendered as an architectural blueprint, with each line annotated as a rule or contract. Shows that a well-designed schema is self-documenting.
- **Status**: Pending
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: An architectural blueprint scroll showing a table schema, with callout labels pointing to each constraint line -- "required," "unique," "valid range," "auto-filled date"
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

#### Image 6: ALTER vs. DROP
<!-- orphan: queued for source-side wiring -->
- **File**: `images/module-01/m01-alter-vs-drop-01.png`
- **Page**: "Modifying Tables: ALTER and DROP"
- **Placement**: after the DROP TABLE section, before the Watch It callout
- **Description**: ALTER as a contractor adding a room to a house, DROP as a wrecking ball demolishing the whole house. Emphasizes the difference between modification and destruction.
- **Status**: Pending
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: Split image -- on the left, a contractor happily adding a new wing to a small house (ALTER); on the right, a wrecking ball reducing a similar house to rubble (DROP)
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

### Module 02 additions

#### Image 5: The Shortcut Pitfall
<!-- orphan: queued for source-side wiring -->
- **File**: `images/module-02/m02-shortcut-pitfall-01.png`
- **Page**: "The Shortcut (and Why You Shouldn't Use It)"
- **Placement**: after the explicit-columns recommendation
- **Description**: Two paths diverging -- the "shortcut" path leads to a cliff labeled "Schema Changed," the longer path with explicit column labels leads safely to the data. Reinforces why naming columns matters.
- **Status**: Pending
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: A fork in the road with two paths -- the shorter path has a warning sign and leads to a cliff, the longer path is lined with labeled signposts and leads safely to a database file
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

#### Image 6: Multi-Row Bulk Load
<!-- orphan: queued for source-side wiring -->
- **File**: `images/module-02/m02-multi-row-bulk-load-01.png`
- **Page**: "Multi-Row INSERT: The Bulk Load"
- **Placement**: after the side-by-side single-row vs. multi-row examples
- **Description**: A single pallet truck carrying five boxes at once vs. a person carrying one box at a time. Visualizes why multi-row INSERT is more efficient.
- **Status**: Pending
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: Split image -- on the left, a small character carrying a single box with many trips shown as dotted lines; on the right, a forklift carrying a pallet stacked with five boxes in a single trip
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

#### Image 7: DEFAULT Auto-Fill
<!-- orphan: queued for source-side wiring -->
- **File**: `images/module-02/m02-default-autofill-01.png`
- **Page**: "DEFAULT Values: Let the Database Fill It In"
- **Placement**: after the enrollment_date default example
- **Description**: A form being auto-filled by a helpful robot hand stamping today's date in the empty field. Shows the database filling in defaults for you.
- **Status**: Pending
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: A paper form with most fields handwritten, and one remaining empty field being stamped by a cheerful robot arm holding a rubber stamp that reads "TODAY"
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

### Module 03 additions

#### Image 5: SELECT Picking Columns
<!-- orphan: queued for source-side wiring -->
- **File**: `images/module-03/m03-select-picking-columns-01.png`
- **Page**: "SELECT: The Foundation of Every Question"
- **Placement**: after the SELECT * vs. named-columns comparison
- **Description**: A hand picking specific columns off a buffet tray of data while ignoring others. Shows that SELECT is selective, not a firehose.
- **Status**: Pending
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: A long buffet counter full of labeled columns like dishes, with a hand using tongs to pick only two or three specific items onto a plate, while other columns stay on the counter
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

#### Image 6: Column Aliases Nametags
<!-- orphan: queued for source-side wiring -->
- **File**: `images/module-03/m03-aliases-nametags-01.png`
- **Page**: "Column Aliases: Giving Your Results Better Names"
- **Placement**: after the alias example with AS
- **Description**: Stiff database column headers getting friendly nametags stuck over them -- turning stu_fn into "First Name." Visualizes aliases as renaming.
- **Status**: Pending
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: Three formal table column headers with cryptic short names, each having a colorful "Hello my name is..." nametag being pressed over it by a friendly hand, revealing readable names
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

#### Image 7: BETWEEN Range Slider
<!-- orphan: queued for source-side wiring -->
- **File**: `images/module-03/m03-between-range-01.png`
- **Page**: "BETWEEN: Range Queries Made Easy"
- **Placement**: after the inclusive-range example
- **Description**: A number line with a bracket-shaped range selector highlighting a span inclusive of both endpoints. Clarifies the "inclusive on both ends" rule.
- **Status**: Pending
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: A horizontal number line with a colorful bracket-shaped highlighter covering a span, and two arrows pointing to the endpoints labeled "included"
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

#### Image 8: IN Guest List
<!-- orphan: queued for source-side wiring -->
- **File**: `images/module-03/m03-in-guest-list-01.png`
- **Page**: "IN: Matching Against a List"
- **Placement**: after the IN vs. OR comparison
- **Description**: A bouncer with a clipboard checking names against a guest list. Shows IN as "are you on the list?"
- **Status**: Pending
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: A friendly bouncer character holding a clipboard with a bulleted list, checking names as people walk by a velvet rope, with some people being waved through and others politely turned away
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

#### Image 9: IS NULL Mystery Box
<!-- orphan: queued for source-side wiring -->
- **File**: `images/module-03/m03-is-null-mystery-01.png`
- **Page**: "IS NULL / IS NOT NULL: The Special Case"
- **Placement**: after the three-valued-logic explanation
- **Description**: A mystery box with a question mark, next to a zero and an empty string, showing that NULL is different from all of them. Reinforces that NULL means "unknown."
- **Status**: Pending
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: Three cartoon boxes labeled "0", "empty string", and "NULL" -- the first two have visible contents, the NULL box is wrapped in question marks and shrugging shoulders
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

#### Image 10: Complex Query Recipe
<!-- orphan: queued for source-side wiring -->
- **File**: `images/module-03/m03-complex-query-recipe-01.png`
- **Page**: "Putting It All Together: Complex Queries"
- **Placement**: after the combined WHERE examples
- **Description**: A recipe card layering SELECT, WHERE, AND, IN, and LIKE as stacked ingredients. Shows that complex queries are just combinations of building blocks.
- **Status**: Pending
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: A chef's recipe card with labeled layered ingredients stacked like a sandwich -- each layer is a SQL clause (SELECT, WHERE, AND, IN, LIKE) -- with a finished dish at the bottom
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

### Module 04 additions

#### Image 5: ORDER BY Stacking Cards
<!-- orphan: queued for source-side wiring -->
- **File**: `images/module-04/m04-order-by-stacking-01.png`
- **Page**: "ORDER BY: Sorting Your Results"
- **Placement**: after the ASC/DESC discussion
- **Description**: A random pile of playing cards collapsing into a neat ascending stack via ORDER BY. Reinforces "without ORDER BY, rows come in any order."
- **Status**: Pending
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: Two scenes side by side -- on the left, a chaotic pile of index cards; on the right, the same cards neatly stacked in order, with an arrow showing a magical transformation via ORDER BY
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

#### Image 6: NULL Sorts First
<!-- orphan: queued for source-side wiring -->
- **File**: `images/module-04/m04-null-sorts-first-01.png`
- **Page**: "NULL Sorting: The Odd One Out"
- **Placement**: after the ASC NULL-first example
- **Description**: A lineup of numbers in ascending order, with a mysterious NULL figure standing at the very front. Shows the SQLite NULLs-first default.
- **Status**: Pending
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: A queue of cheerful number characters from 1 to 10 lined up in order, with a ghostly figure labeled NULL standing at the very front of the line, looking a little confused
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

#### Image 7: LIMIT Top N
<!-- orphan: queued for source-side wiring -->
- **File**: `images/module-04/m04-limit-top-n-01.png`
- **Page**: "LIMIT: Just the Top N, Please"
- **Placement**: after the Top 5 by sales example
- **Description**: A podium with just the top three labeled 1, 2, 3 -- rest of the competitors cut off. Emphasizes "just the top N."
- **Status**: Pending
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: A three-level winners podium with cheerful characters on places 1, 2, and 3, while a long line of other competitors stretches off into the distance blurred or faded
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

#### Image 8: WHERE + ORDER BY + LIMIT Combo
<!-- orphan: queued for source-side wiring -->
- **File**: `images/module-04/m04-power-combo-01.png`
- **Page**: "The Power Combo: WHERE + ORDER BY + LIMIT"
- **Placement**: after the combo overview
- **Description**: Three gears labeled FILTER, SORT, LIMIT meshing together in a pipeline. Shows the canonical SQL query structure.
- **Status**: Pending
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: Three interlocking gears or conveyor belts labeled FILTER, SORT, and LIMIT in that order, with a pile of raw rows entering the left and a clean ordered result leaving the right
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

### Module 05 additions

#### Image 5: Aggregates With WHERE
<!-- orphan: queued for source-side wiring -->
- **File**: `images/module-05/m05-aggregates-with-where-01.png`
- **Page**: "Aggregates with WHERE: Filtered Summaries"
- **Placement**: after the two-step filter-then-summarize explanation
- **Description**: A sieve (WHERE) filtering rows, with a summary badge (AVG/COUNT/SUM) appearing below. Reinforces "WHERE first, then aggregate."
- **Status**: Pending
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: A kitchen sieve strainer filtering rows labeled with values, only some fall through, and beneath it a label that reads "AVG" with a summary number emerging
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

#### Image 6: Multi-Column GROUP BY Drill-Down
<!-- orphan: queued for source-side wiring -->
- **File**: `images/module-05/m05-multi-column-drilldown-01.png`
- **Page**: "GROUP BY with Multiple Columns"
- **Placement**: after the department+year example
- **Description**: Nested buckets showing department containing year buckets, illustrating multi-level grouping. Shows drill-down via additional GROUP BY columns.
- **Status**: Pending
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: A large labeled bucket "Department" containing smaller bins labeled "Year," each of which contains piles of records, showing a drill-down hierarchy
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

#### Image 7: Real-World Analysis
<!-- orphan: queued for source-side wiring -->
- **File**: `images/module-05/m05-real-world-analysis-01.png`
- **Page**: "Practical Queries: Real-World Analysis"
- **Placement**: after the example analytical queries
- **Description**: A database query transforming into a business insight chart or headline. Shows that aggregate queries produce decisions, not just numbers.
- **Status**: Pending
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: A SQL query on the left morphing via an arrow into a business insight on the right -- a clean bar chart with a big "Insight!" lightbulb above it
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

### Module 06 additions

#### Image 6: Why We Need Joins (Normalization)
<!-- orphan: queued for source-side wiring -->
- **File**: `images/module-06/m06-why-joins-01.png`
- **Page**: "Why Do We Even Need Joins?"
- **Placement**: after the normalization reasoning
- **Description**: One fat repetitive table split into two clean related tables with a connecting line. Shows why joins exist -- data lives in separate tables on purpose.
- **Status**: Pending
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: Split image -- on the left, one messy wide table with repeated data highlighted in red; on the right, two tidy separate tables connected by an arrow, with the repeated data removed
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

#### Image 7: Table Aliases Nicknames
<!-- orphan: queued for source-side wiring -->
- **File**: `images/module-06/m06-aliases-nicknames-01.png`
- **Page**: "Table Aliases: Your Sanity Savers"
- **Placement**: after the with/without aliases comparison
- **Description**: Three long table names being given short nickname nametags. Reinforces aliases as sanity-saving shorthand.
- **Status**: Pending
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: Three large cartoon table characters each with a long formal name on their chest getting a small "call me..." sticker pressed on with a single letter alias
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

#### Image 8: RIGHT JOIN Mirror
<!-- orphan: queued for source-side wiring -->
- **File**: `images/module-06/m06-right-join-mirror-01.png`
- **Page**: "RIGHT JOIN and FULL OUTER JOIN: The Ones SQLite Skipped"
- **Placement**: after the RIGHT JOIN workaround
- **Description**: A LEFT JOIN reflected in a mirror, showing that RIGHT JOIN is just LEFT JOIN flipped. Demystifies the unsupported join types.
- **Status**: Pending
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: A diagram of a LEFT JOIN on one side of a mirror, and its mirror image labeled RIGHT JOIN on the other side, with a FULL OUTER JOIN Venn diagram floating above both
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

#### Image 9: Three-Table Join Chain
<!-- orphan: queued for source-side wiring -->
- **File**: `images/module-06/m06-three-table-chain-01.png`
- **Page**: "Joining 3+ Tables: The Full Picture"
- **Placement**: after the students-enrollments-courses example
- **Description**: Three tables connected by chain links following foreign keys, forming a continuous path. Shows multi-table joins as links in a chain.
- **Status**: Pending
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: Three labeled tables connected by visible chain links, with arrows showing foreign keys, forming one continuous chain from students through enrollments to courses
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

#### Image 10: Complex Join Orchestra
<!-- orphan: queued for source-side wiring -->
- **File**: `images/module-06/m06-complex-join-orchestra-01.png`
- **Page**: "Complex Join Queries: Joins + GROUP BY + HAVING"
- **Placement**: after the combined query example
- **Description**: A conductor coordinating sections labeled JOIN, WHERE, GROUP BY, HAVING, AGGREGATE, ORDER BY -- each contributing to a unified result. Shows complex queries as orchestrated combinations.
- **Status**: Pending
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: A cheerful orchestra conductor coordinating sections of players, each section labeled with a SQL clause -- JOIN, WHERE, GROUP BY, HAVING -- with harmonious music notes rising
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

### Module 07 additions

#### Image 5: Subquery Inside-Out
<!-- orphan: queued for source-side wiring -->
- **File**: `images/module-07/m07-subquery-inside-out-01.png`
- **Page**: "What Is a Subquery, Really?"
- **Placement**: after the inside-out execution explanation
- **Description**: An outer query peeling back to reveal an inner query being evaluated first, then feeding its result outward. Reinforces the "inside out" execution order.
- **Status**: Pending
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: A larger SQL scroll with a smaller SQL scroll tucked inside it -- an arrow shows the smaller scroll being read first, then its answer passed up into the larger scroll
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

#### Image 6: Scalar Subquery One Value
<!-- orphan: queued for source-side wiring -->
- **File**: `images/module-07/m07-scalar-one-value-01.png`
- **Page**: "Scalar Subqueries: One Value to Rule Them All"
- **Placement**: after the AVG-comparison example
- **Description**: A subquery distilling a whole column of values into a single gem labeled with one number. Shows "scalar" means one value.
- **Status**: Pending
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: A column of many cartoon rows being funneled through a laboratory distillation apparatus, emerging as one labeled droplet with a single number inside
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

#### Image 7: Derived Table Workbench
<!-- orphan: queued for source-side wiring -->
- **File**: `images/module-07/m07-derived-table-workbench-01.png`
- **Page**: "Derived Tables: Subqueries in the FROM Clause"
- **Placement**: after the aliased-subquery example
- **Description**: A workbench where a temporary "virtual" table is assembled from other pieces, labeled with an alias, then queried. Shows derived tables as intermediate workbenches.
- **Status**: Pending
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: A carpenter's workbench where a small wooden table is being assembled from pieces of other tables, with a name tag hanging from it, and a query magnifying glass examining it
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

#### Image 8: Correlated Subquery Phone Home
<!-- orphan: queued for source-side wiring -->
- **File**: `images/module-07/m07-correlated-phone-home-01.png`
- **Page**: "Correlated Subqueries: The Ones That Phone Home"
- **Placement**: after the correlated example
- **Description**: An inner query on a phone calling the outer query, row by row. Shows correlation as "phoning home" for each outer row.
- **Status**: Pending
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: A small inner-query character on a telephone, connected by a stretched cord to an outer-query character who is walking row by row across a table, each step prompting a new call
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

#### Image 9: DROP VIEW Clean Up
<!-- orphan: queued for source-side wiring -->
- **File**: `images/module-07/m07-drop-view-cleanup-01.png`
- **Page**: "DROP VIEW: Cleaning Up"
- **Placement**: after the DROP-then-CREATE pattern
- **Description**: An old view being tossed in a recycling bin while a fresh new view is being unveiled. Reinforces the drop-and-recreate workflow.
- **Status**: Pending
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: A hand tossing an old rolled-up view document into a recycling bin, while on the other side a shiny new view document is being unrolled on a pedestal
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

#### Image 10: Putting It All Together (Subq + Joins + Views)
<!-- orphan: queued for source-side wiring -->
- **File**: `images/module-07/m07-all-together-01.png`
- **Page**: "Putting It All Together: Subqueries + Joins + Views"
- **Placement**: after the combined-pieces walkthrough
- **Description**: Three puzzle pieces -- subquery, join, view -- clicking together into one unified image of a completed dashboard. Shows that these three tools combine into real analytical power.
- **Status**: Pending
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: Three labeled puzzle pieces -- SUBQUERY, JOIN, VIEW -- snapping together to complete a picture of a dashboard with charts and insights
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

### Module 08 additions

#### Image 6: UPDATE Targeted Fix
<!-- orphan: queued for source-side wiring -->
- **File**: `images/module-08/m08-update-targeted-fix-01.png`
- **Page**: "UPDATE in Detail"
- **Placement**: after the SET clause and CASE expression examples
- **Description**: A precision tool editing exactly one row in a table while other rows sit untouched. Shows UPDATE with a WHERE as targeted surgery rather than blunt force.
- **Status**: Pending
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: A table of rows with a precision tweezers or laser pointer selecting one specific row and changing a single field, while neighboring rows glow to show they are unaffected
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

#### Image 7: Subquery-Driven UPDATE/DELETE
<!-- orphan: queued for source-side wiring -->
- **File**: `images/module-08/m08-subquery-driven-01.png`
- **Page**: "UPDATE and DELETE with Subqueries"
- **Placement**: after the cross-table DELETE example
- **Description**: A subquery acting as a targeting scope, feeding coordinates to an UPDATE or DELETE action. Shows subqueries as aim, modification as fire.
- **Status**: Pending
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: A friendly scope or telescope labeled SUBQUERY identifying specific rows on a table, with dotted lines feeding those coordinates to an UPDATE action button below
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

#### Image 8: Why Transactions Matter -- Bank Transfer
<!-- orphan: queued for source-side wiring -->
- **File**: `images/module-08/m08-why-transactions-01.png`
- **Page**: "Why Transactions Matter: The Bank Transfer Problem"
- **Placement**: after the split-transfer scenario (complements existing bank-transfer image higher up)
- **Description**: A transfer caught mid-operation with half the money in transit -- one scenario shows it aborting cleanly, another shows the broken half-state without transactions. Illustrates atomicity.
- **Status**: Pending
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: Two parallel strips -- the top labeled "No Transaction" showing a coin stuck in mid-air between two piggy banks, one missing the coin; the bottom labeled "Transaction" showing either both piggy banks intact or the coin safely arrived
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

#### Image 9: Putting Transactions to Work
<!-- orphan: queued for source-side wiring -->
- **File**: `images/module-08/m08-transactions-to-work-01.png`
- **Page**: "Putting Transactions to Work"
- **Placement**: after the BEGIN/COMMIT/ROLLBACK examples
- **Description**: An envelope labeled BEGIN being sealed (COMMIT) or shredded (ROLLBACK). Reinforces the transaction-as-envelope mental model.
- **Status**: Pending
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: Three panels -- an envelope labeled BEGIN being opened, statements going inside, and finally either sealed with a green COMMIT stamp or fed into a shredder labeled ROLLBACK
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

#### Image 10: The Danger Zone
<!-- orphan: queued for source-side wiring -->
- **File**: `images/module-08/m08-danger-zone-01.png`
- **Page**: "The Danger Zone: Common Mistakes"
- **Placement**: after the list of common mistakes
- **Description**: A warning-sign style collage of the four most common UPDATE/DELETE mistakes -- missing WHERE, wrong operator, forgotten cascade, and skipped SELECT preview. Reinforces awareness of pitfalls.
- **Status**: Pending
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: A yellow caution-tape border around four small illustrated pitfalls -- a missing WHERE clause, a reversed greater-than symbol, a cracked cascade chain, and a skipped preview step, each with a tiny warning icon
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

### Module 09 additions

#### Image 6: Composite Index Phone Book
<!-- orphan: queued for source-side wiring -->
- **File**: `images/module-09/m09-composite-phonebook-01.png`
- **Page**: "Composite Indexes and Column Order"
- **Placement**: after the phone-book analogy
- **Description**: A phone book opened to show the last-name-then-first-name ordering, with a highlighted Smith section and a crossed-out "all Johns" search. Reinforces column-order matters.
- **Status**: Pending
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: An open phone book sorted by last name then first name, with the Smith pages highlighted and a red X over a frustrated character trying to find "all Johns" by flipping through randomly
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

#### Image 7: EXPLAIN QUERY PLAN X-Ray
<!-- orphan: queued for source-side wiring -->
- **File**: `images/module-09/m09-explain-xray-01.png`
- **Page**: "EXPLAIN QUERY PLAN: Seeing What the Database Sees"
- **Placement**: after the SCAN-vs-SEARCH comparison
- **Description**: An X-ray machine showing the internal execution of a query -- SCAN labeled slow, SEARCH labeled fast. Makes the diagnostic tool feel tangible.
- **Status**: Pending
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: An X-ray style illustration of a query running through a database, with a highlighted bone labeled SCAN shown as cracked and slow on one side, and a healthy bone labeled SEARCH USING INDEX glowing fast on the other side
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

#### Image 8: Naming Conventions Good vs. Bad
<!-- orphan: queued for source-side wiring -->
- **File**: `images/module-09/m09-naming-conventions-01.png`
- **Page**: "Naming Conventions: The Stuff Nobody Teaches But Everyone Judges"
- **Placement**: after the bad-vs-good examples
- **Description**: Side-by-side comparison -- cluttered labels like "StudentData", "FirstName", "E-mail" on the left; clean snake_case labels on the right. Shows conventions at a glance.
- **Status**: Pending
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: Split image -- on the left, a messy jumble of label stickers with mixed capitalization and punctuation; on the right, a neatly aligned column of clean snake_case labels, each hanging straight
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

#### Image 9: Query Cleanup Before/After
<!-- orphan: queued for source-side wiring -->
- **File**: `images/module-09/m09-query-cleanup-01.png`
- **Page**: "Query Optimization: Writing Better SQL"
- **Placement**: after the refactored query
- **Description**: A tangled spaghetti query being combed into a clean orderly one. Reinforces that clean SQL is a craft, not an afterthought.
- **Status**: Pending
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: A tangled mess of query lines on the left being combed out by a comb or brush into straight clean lines on the right, with labels BEFORE and AFTER
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

#### Image 10: Schema Design Capstone
<!-- orphan: queued for source-side wiring -->
- **File**: `images/module-09/m09-schema-capstone-01.png`
- **Page**: "Schema Design: Putting It All Together"
- **Placement**: after the full-schema example
- **Description**: A finished database schema diagram like an architectural drawing -- normalized tables, foreign keys, indexes, all labeled. Signals the capstone feel of the entire course.
- **Status**: Pending
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: A framed architectural blueprint of a small relational schema -- tables with column lists, foreign key arrows, index tags, all neatly labeled, hanging on a wall like a diploma
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots
