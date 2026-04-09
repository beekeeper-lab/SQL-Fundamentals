# Module 2: Inserting Data

## Filling Out Forms for Your Database (and What Happens When You Get It Wrong)

> 🏷️ Start Here

---

![Time to fill those empty tables with actual data.](../images/module-02/m02-hero-filling-forms-01.png)
*You've built the filing cabinet. You've labeled the drawers. Now it's time to put something in them.*

> 🎯 **Teach:** INSERT is how data gets into your tables -- and understanding its variations (single row, multi-row, conflict handling) gives you control over exactly how data enters your system.
> **See:** INSERT as filling out a form -- you specify which fields you're filling in and what values go in them.
> **Feel:** Ready to move from empty tables to populated databases, with confidence about handling the edge cases.

> 🎙️ You've got tables. Beautiful, well-designed tables with constraints and foreign keys and everything. But they're empty. A database without data is like a restaurant without food -- technically functional, but kind of missing the point. In this module, we're going to learn INSERT -- all the ways to get data into your tables, what happens when data breaks the rules, and how to handle conflicts gracefully.

---

## INSERT: The Basic Form

> 🎯 **Teach:** The INSERT INTO statement is like filling out a form -- you name the fields you're filling in, then provide the values.
> **See:** The anatomy of an INSERT statement mapped to a physical form: column list = field labels, VALUES = what you write in.
> **Feel:** Comfortable with the basic syntax and confident about writing INSERT statements from scratch.

> 🔄 **Where this fits:** INSERT is the "DML" part of SQL -- Data Manipulation Language. You learned DDL (creating structure) in Modules 0 and 1. Now you're learning to put data INTO that structure.

Think of INSERT as filling out a form. The table is the blank form. The columns are the field labels. The VALUES are what you write in the blanks.

```sql
INSERT INTO students (first_name, last_name, email, gpa)
VALUES ('Alice', 'Johnson', 'alice.j@university.edu', 3.8);
```

Let's break that down:

| Part | What It Does | Form Analogy |
|------|-------------|--------------|
| `INSERT INTO students` | Which table (form) to fill out | Picking up the "Student Registration" form |
| `(first_name, last_name, email, gpa)` | Which columns (fields) you're filling in | Looking at the field labels |
| `VALUES ('Alice', 'Johnson', ...)` | The actual data | Writing in the blanks |

![INSERT is like filling out a form -- column names are the labels, VALUES are what you write.](../images/module-02/m02-insert-as-form-01.png)
*Column list = field labels. VALUES = what you write in the blanks. Same concept, different format.*

A few rules:

1. **Text values go in single quotes.** `'Alice'` not `"Alice"` and definitely not `Alice`.
2. **Numbers don't need quotes.** `3.8` not `'3.8'`.
3. **The order of values must match the order of columns.** If you list `(first_name, last_name)`, the values must be `('Alice', 'Johnson')` -- not `('Johnson', 'Alice')`.
4. **You can skip columns** that have DEFAULT values, allow NULL, or are AUTOINCREMENT.

> 🎙️ Here's the number one best practice for INSERT statements, and I want you to tattoo it on your brain: always specify the column list. Yes, you CAN skip it and just provide values in order. But don't. Specifying columns makes your intent clear, protects you when the table changes, and makes your code readable six months from now. Always. Specify. The columns.

---

## The Shortcut (and Why You Shouldn't Use It)

> 🎯 **Teach:** You can omit the column list, but it's fragile and unclear -- always specifying columns is a best practice worth adopting from day one.
> **See:** The difference between explicit column lists (clear, safe) and implicit ordering (fragile, confusing).
> **Feel:** Convinced that the "shortcut" isn't worth the risk.

You *can* skip the column list if you provide values for every column in order:

```sql
-- This works, but DON'T do this
INSERT INTO students VALUES (NULL, 'Alice', 'Johnson', 'alice.j@university.edu', 3.8, NULL);
```

That `NULL` at the beginning is for the AUTOINCREMENT `id` column (SQLite will assign it). The `NULL` at the end is for `enrollment_date` (the DEFAULT won't trigger -- you're explicitly saying NULL).

**Why this is a bad idea:**

- If someone adds a column to the table later, your INSERT breaks.
- If someone reorders columns, your data goes in the wrong fields.
- Anyone reading the code has to look up the table schema to understand what's happening.

The explicit version is always better:

```sql
-- DO this instead
INSERT INTO students (first_name, last_name, email, gpa)
VALUES ('Alice', 'Johnson', 'alice.j@university.edu', 3.8);
```

No ambiguity. No fragility. No guessing.

> 💡 **Remember this one thing:** Always specify the column list in INSERT statements. It's a few extra characters that save you from a world of confusion.

---

## Multi-Row INSERT: The Bulk Load

> 🎯 **Teach:** You can insert multiple rows in a single statement, which is cleaner and more efficient than repeating INSERT for each row.
> **See:** Side-by-side comparison of five individual INSERTs vs. one multi-row INSERT doing the same work.
> **Feel:** Satisfaction at writing less code that does more work.

Why write five INSERT statements when you can write one?

```sql
-- Instead of this...
INSERT INTO students (first_name, last_name, email, gpa) VALUES ('David', 'Brown', 'david.b@university.edu', 3.1);
INSERT INTO students (first_name, last_name, email, gpa) VALUES ('Eve', 'Davis', 'eve.d@university.edu', 3.9);
INSERT INTO students (first_name, last_name, email, gpa) VALUES ('Frank', 'Miller', 'frank.m@university.edu', 2.5);
INSERT INTO students (first_name, last_name, email, gpa) VALUES ('Grace', 'Wilson', 'grace.w@university.edu', 3.3);
INSERT INTO students (first_name, last_name, email, gpa) VALUES ('Henry', 'Moore', 'henry.m@university.edu', 2.8);

-- ...do THIS:
INSERT INTO students (first_name, last_name, email, gpa) VALUES
    ('David', 'Brown', 'david.b@university.edu', 3.1),
    ('Eve', 'Davis', 'eve.d@university.edu', 3.9),
    ('Frank', 'Miller', 'frank.m@university.edu', 2.5),
    ('Grace', 'Wilson', 'grace.w@university.edu', 3.3),
    ('Henry', 'Moore', 'henry.m@university.edu', 2.8);
```

Same result. Less typing. And it's actually faster for the database -- one transaction instead of five.

Notice the pattern: the column list appears once, and then each row is a parenthesized group of values, separated by commas. The last row gets a semicolon instead of a comma.

> 🎙️ Multi-row INSERT is one of those things that seems like a small convenience but matters a lot in practice. When you're populating a table with test data or loading initial records, one multi-row INSERT is cleaner to read, easier to edit, and faster for the database to process. Get comfortable with this syntax -- you'll use it constantly.

---

## NULL: The Billion-Dollar Misunderstanding

> 🎯 **Teach:** NULL means "unknown" -- it's not zero, not empty string, not false. Understanding this distinction prevents a whole category of bugs.
> **See:** The three-way comparison between NULL, empty string, and zero -- with concrete examples showing they behave completely differently.
> **Feel:** A healthy respect for NULL and its quirks.

This section might be the most important one in the module. **NULL is not what you think it is.**

NULL means "this value is unknown or does not exist." It is NOT:

- **Zero** (0 is a known value -- zero)
- **An empty string** ('' is a known value -- an empty string)
- **False** (FALSE is a known value -- false)

Here's what this looks like in practice:

```sql
-- These three rows are DIFFERENT
INSERT INTO students (first_name, last_name, email, gpa)
VALUES ('Ghost', 'Student', 'ghost@university.edu', NULL);     -- GPA is unknown

INSERT INTO students (first_name, last_name, email, gpa)
VALUES ('Zero', 'Student', 'zero@university.edu', 0.0);        -- GPA is known: it's 0.0

-- And for text columns:
-- NULL means "we don't have a phone number"
-- ''    means "we asked, and their phone number is literally blank"
```

![NULL, zero, and empty string are three completely different things.](../images/module-02/m02-null-vs-zero-vs-empty-01.png)
*Think of NULL as a shrug. Zero is an answer. Empty string is an answer. NULL is "I don't know."*

Why does this matter? Because NULL behaves weirdly in comparisons:

```sql
-- This will NOT find rows where gpa is NULL:
SELECT * FROM students WHERE gpa = NULL;    -- WRONG! Returns nothing.

-- You have to use IS NULL:
SELECT * FROM students WHERE gpa IS NULL;   -- Correct!
```

NULL isn't equal to anything -- not even itself. `NULL = NULL` is not true. It's NULL. This trips up everyone, including experienced developers.

> 🎙️ Here's the way to think about NULL. If I ask you "Is an unknown number equal to another unknown number?" -- you can't say yes. They MIGHT be equal, but you don't KNOW. That's why NULL equals NULL isn't true -- it's unknown. This seems philosophical, but it causes real bugs in real applications. When you see NULL, think "unknown," and remember to use IS NULL, never equals NULL.

> 💡 **Remember this one thing:** NULL means "unknown." Use `IS NULL` to check for it, never `= NULL`. This single rule will save you hours of debugging.

---

## DEFAULT Values: Let the Database Fill It In

> 🎯 **Teach:** DEFAULT values kick in when you omit a column from your INSERT -- the database fills in a sensible value automatically.
> **See:** How omitting a column with a DEFAULT triggers the automatic fill, vs. explicitly providing NULL (which overrides the default).
> **Feel:** Appreciation for how defaults reduce repetitive work and ensure consistency.

Remember those DEFAULT constraints from Module 1? Here's where they shine.

If a column has a DEFAULT and you *omit it from your INSERT*, the default value is used:

```sql
-- The courses table has: department TEXT DEFAULT 'Undeclared'

-- Omit department entirely -- DEFAULT kicks in:
INSERT INTO courses (course_code, title, credits)
VALUES ('GEN100', 'Freshman Seminar', 1);

-- Check the result:
SELECT * FROM courses WHERE course_code = 'GEN100';
-- department will be 'Undeclared'
```

But here's the catch: if you explicitly pass NULL, you get NULL -- not the default:

```sql
-- Explicitly passing NULL overrides the default:
INSERT INTO courses (course_code, title, credits, department)
VALUES ('GEN200', 'Study Skills', 1, NULL);

-- department will be NULL, not 'Undeclared'
```

The difference: **omitting the column** triggers the default. **Explicitly providing NULL** gives you NULL.

> 🎙️ This is a subtle but important distinction. If you want the default value, leave the column OUT of your column list entirely. If you include it and pass NULL, you're telling the database "I specifically want nothing here." The database respects your explicit instruction over the default. It's like a form that pre-fills your country -- if you erase it and submit blank, the system doesn't put the default back. You said blank, so blank it is.

---

## Conflict Handling: When Data Fights Back

> 🎯 **Teach:** When an INSERT would violate a constraint, SQLite normally errors out -- but INSERT OR IGNORE and INSERT OR REPLACE give you alternatives.
> **See:** The three conflict strategies as different responses to a duplicate form submission: reject it, ignore it, or replace the old one.
> **Feel:** Empowered to handle real-world data scenarios where duplicates and conflicts are inevitable.

You've got constraints. They protect your data. But what happens when an INSERT violates one?

By default: **the database throws an error and the row is rejected.** Full stop.

```sql
-- Alice already has email 'alice.j@university.edu' (UNIQUE constraint)
INSERT INTO students (first_name, last_name, email, gpa)
VALUES ('Alicia', 'Jones', 'alice.j@university.edu', 3.0);

-- ERROR: UNIQUE constraint failed: students.email
```

That's usually what you want. But sometimes you need a different strategy.

### INSERT OR IGNORE -- "If there's a conflict, just skip it"

```sql
INSERT OR IGNORE INTO students (first_name, last_name, email, gpa)
VALUES ('Alicia', 'Jones', 'alice.j@university.edu', 3.0);
```

No error. The row is silently skipped. The original Alice row is untouched.

**Use this when:** You're loading data that might have duplicates and you want to keep the original.

### INSERT OR REPLACE -- "If there's a conflict, replace the old row"

```sql
INSERT OR REPLACE INTO students (first_name, last_name, email, gpa)
VALUES ('Alicia', 'Jones', 'alice.j@university.edu', 3.0);
```

The original Alice row is **deleted**, and the new Alicia row takes its place.

**Use this when:** You want the latest data to win.

![Three strategies for handling conflicts: Error (default), Ignore, or Replace.](../images/module-02/m02-conflict-handling-01.png)
*Someone submits a duplicate form. Do you reject it, ignore it, or replace the old one?*

> **Watch it!** INSERT OR REPLACE doesn't just update the conflicting columns -- it **deletes the old row entirely** and inserts a new one. This means the `id` changes (AUTOINCREMENT assigns a new one), and any other columns not specified in the new INSERT get their defaults, not the old values. This catches people off guard.

Here's the full picture:

| Strategy | On Conflict... | Original Row | New Row |
|----------|---------------|-------------|---------|
| (default) | Error thrown | Untouched | Not inserted |
| `INSERT OR IGNORE` | Silently skips | Untouched | Not inserted |
| `INSERT OR REPLACE` | Deletes old, inserts new | Deleted | Inserted (new id!) |
| `INSERT OR ABORT` | Same as default | Untouched | Not inserted |

> 🎙️ Here's my rule of thumb for conflict handling. If you're loading data and want to keep what you already have, use INSERT OR IGNORE. If you're loading data and want the newest version to win, use INSERT OR REPLACE -- but be careful, because it's a delete-then-insert, not an update. For most day-to-day work, the default error behavior is what you want -- it forces you to deal with the problem explicitly rather than sweeping it under the rug.

---

## 🗨️ There Are No Dumb Questions

> 🎯 **Teach:** Address the practical confusions that come up when people start inserting real data into real tables.
> **See:** Clear answers to the questions that trip up beginners most -- NULL handling, quoting rules, AUTOINCREMENT behavior.
> **Feel:** Ready to insert data with confidence, knowing the common pitfalls.

**Q: What happens if I INSERT into a table with AUTOINCREMENT and specify the id anyway?**

A: SQLite will use the ID you specify, as long as it doesn't conflict with an existing row. If you leave it out (or pass NULL for it), SQLite assigns the next number. Best practice: let AUTOINCREMENT do its job and don't specify the ID.

**Q: What's the difference between INSERT OR REPLACE and UPDATE?**

A: INSERT OR REPLACE deletes the old row and inserts a new one. UPDATE modifies the existing row in place. UPDATE preserves the row's id and any columns you don't mention. INSERT OR REPLACE creates a brand new row. We'll cover UPDATE in a later module.

**Q: Can I insert into a table that has foreign keys referencing another table that's empty?**

A: No -- and that's the point. If the `enrollments` table has a foreign key to `students`, you must insert students first. The order matters: parent tables (the ones being referenced) need data before child tables (the ones doing the referencing).

**Q: I put single quotes around a number. Is that a problem?**

A: In SQLite, it usually works because of type affinity -- SQLite will convert `'3.8'` to `3.8` when storing it in a REAL column. But it's sloppy and won't work in stricter databases. Use quotes for text, no quotes for numbers.

**Q: How do I insert a text value that contains a single quote, like "O'Brien"?**

A: Double the quote: `'O''Brien'`. Two single quotes inside a string represent a literal single quote. This is standard SQL.

---

## ✏️ Sharpen Your Pencil

> 🎯 **Teach:** Populate a complete university database and test every edge case you've learned about.
> **See:** A structured sequence of exercises that builds from simple inserts to conflict handling and NULL testing.
> **Feel:** Satisfied at having a fully populated, realistic database that you built from scratch.

Time to fill those tables. You'll use the three-table university schema from Module 1.

### Exercise 1: Set Up the Database

Create a fresh database with all three tables:

```bash
sqlite3 day03.db
```

```sql
PRAGMA foreign_keys = ON;

CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    gpa REAL CHECK(gpa >= 0.0 AND gpa <= 4.0),
    enrollment_date TEXT DEFAULT (date('now'))
);

CREATE TABLE courses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_code TEXT UNIQUE NOT NULL,
    title TEXT NOT NULL,
    credits INTEGER NOT NULL CHECK(credits > 0 AND credits <= 6),
    department TEXT DEFAULT 'Undeclared'
);

CREATE TABLE enrollments (
    student_id INTEGER NOT NULL,
    course_id INTEGER NOT NULL,
    grade TEXT CHECK(grade IN ('A', 'B', 'C', 'D', 'F') OR grade IS NULL),
    enrolled_date TEXT DEFAULT (date('now')),
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (course_id) REFERENCES courses(id)
);
```

Run `.tables` to confirm all three exist.

### Exercise 2: Insert Students (Individual)

Insert these 3 students one at a time, specifying the column list:

| first_name | last_name | email | gpa |
|------------|-----------|-------|-----|
| Alice | Johnson | alice.j@university.edu | 3.8 |
| Bob | Smith | bob.smith@university.edu | 2.9 |
| Carol | Williams | carol.w@university.edu | 3.5 |

Verify with `SELECT * FROM students;`.

### Exercise 3: Insert Students (Multi-Row)

Insert these 5 students in a single multi-row INSERT:

| first_name | last_name | email | gpa |
|------------|-----------|-------|-----|
| David | Brown | david.b@university.edu | 3.1 |
| Eve | Davis | eve.d@university.edu | 3.9 |
| Frank | Miller | frank.m@university.edu | 2.5 |
| Grace | Wilson | grace.w@university.edu | 3.3 |
| Henry | Moore | henry.m@university.edu | 2.8 |

Run `SELECT * FROM students;` to show all 8 students.

### Exercise 4: Insert Courses

Insert these 4 courses with explicit departments in one multi-row INSERT:

| course_code | title | credits | department |
|-------------|-------|---------|------------|
| CS101 | Intro to Computer Science | 4 | Computer Science |
| CS201 | Data Structures | 4 | Computer Science |
| MATH101 | Calculus I | 4 | Mathematics |
| ENG101 | English Composition | 3 | English |

Then insert this course WITHOUT specifying a department:

| course_code | title | credits |
|-------------|-------|---------|
| GEN100 | Freshman Seminar | 1 |

Run `SELECT * FROM courses;` -- confirm GEN100 has department `Undeclared`.

### Exercise 5: Insert Enrollments

Insert these enrollment records (use one multi-row INSERT or individual statements):

| student_id | course_id | grade |
|------------|-----------|-------|
| 1 | 1 | A |
| 1 | 3 | B |
| 2 | 1 | C |
| 2 | 4 | B |
| 3 | 2 | A |
| 3 | 3 | NULL |
| 4 | 1 | NULL |
| 5 | 2 | A |
| 5 | 5 | NULL |
| 6 | 4 | D |

Run `SELECT * FROM enrollments;` and confirm 10 rows. Note which rows have NULL grades (those students are still taking the course).

### Exercise 6: Test Edge Cases

**Test INSERT OR IGNORE:**
```sql
INSERT OR IGNORE INTO students (first_name, last_name, email, gpa)
VALUES ('Alicia', 'Jones', 'alice.j@university.edu', 3.0);
```
Query Alice's row -- is it unchanged?

**Test INSERT OR REPLACE:**
```sql
INSERT OR REPLACE INTO students (first_name, last_name, email, gpa)
VALUES ('Alicia', 'Jones', 'alice.j@university.edu', 3.0);
```
Query the row again -- what changed? (Pay attention to the `id` value!)

**Test a constraint violation:**
```sql
INSERT INTO students (first_name, last_name, email, gpa)
VALUES ('Bad', 'Student', 'bad@university.edu', -1.0);
```
Record the error message.

**Test explicit NULL:**
```sql
INSERT INTO students (first_name, last_name, email, gpa)
VALUES ('Iris', 'Taylor', 'iris.t@university.edu', NULL);
```
Query Iris's row. Her `gpa` should be NULL (not 0, not empty -- NULL).

### Exercise 7: Verify Final State

Run these counts and record the results:

```sql
SELECT COUNT(*) AS student_count FROM students;
SELECT COUNT(*) AS course_count FROM courses;
SELECT COUNT(*) AS enrollment_count FROM enrollments;
```

> 🎙️ Pay special attention to Exercise 6. The INSERT OR REPLACE test is the one that surprises people -- when you replace Alice, her ID changes. That's because REPLACE deletes the old row and inserts a brand new one. If other tables had foreign keys pointing to Alice's old ID, those references would break. That's a real-world consequence worth understanding.

---

## Bullet Points

- **INSERT INTO** is like filling out a form -- column list is the fields, VALUES is what you write in.
- **Always specify the column list.** Skipping it is fragile and unclear.
- **Multi-row INSERT** lets you add many rows in one statement -- cleaner and faster.
- **NULL means "unknown."** It's not zero, not empty string, not false. Use `IS NULL` to check for it, never `= NULL`.
- **DEFAULT values** trigger when you *omit* the column. Explicitly passing NULL overrides the default.
- **INSERT OR IGNORE** silently skips conflicting rows. **INSERT OR REPLACE** deletes the old row and inserts a new one.
- **Order matters with foreign keys.** Parent tables (referenced) must be populated before child tables (referencing).
- **Single quotes for text values.** No quotes for numbers. Escape quotes by doubling them: `'O''Brien'`.

> 🎙️ Here's your Module 2 recap. You learned INSERT in all its forms -- single row, multi-row, with and without explicit columns. You learned that NULL is its own special kind of nothing. You learned how DEFAULT values work, and you learned three strategies for handling conflicts. Most importantly, you populated a complete university database with real data across three interconnected tables. In the next module, we'll finally learn SELECT in depth -- the most powerful and most-used command in all of SQL.

---

## Up Next

> 🎯 **Teach:** The next module dives deep into SELECT -- filtering, searching, and retrieving exactly the data you need.
> **See:** The link to Module 3 and the promise that SELECT is where SQL gets really powerful and really fun.
> **Feel:** Eager to start asking interesting questions of the data you just inserted.

[Module 3: SELECT and Filtering](./module-03-select-and-filtering.md) -- You've got a database full of data. Now let's learn how to ask it interesting questions. SELECT is the command you'll use 80% of the time in SQL, and it can do way more than just "show me everything."

> 🎙️ That wraps up Module 2. You know how to get data in. Next up, you learn how to get data out -- selectively, precisely, and powerfully. SELECT is the star of the SQL show, and Module 3 is where it takes the stage. See you there.
