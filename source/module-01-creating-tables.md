# Module 1: Creating Tables

## Blueprints, Building Codes, and Why Your Database Needs Both

> 🏷️ Start Here

---

![You're about to become a data architect. Hard hat optional.](../images/module-01/m01-hero-blueprint-01.png)
*You're about to become a data architect. Hard hat optional.*

> 🎯 **Teach:** Creating a table isn't just picking column names -- it's designing a blueprint with built-in rules that protect your data from the start.
> **See:** The analogy between architectural blueprints (structure) and building codes (constraints) applied to database tables.
> **Feel:** Excited to move beyond basic tables and start building ones that actively prevent bad data.

> 🎙️ In Module 0, you built your first tables. They worked, but they were a little... naive. You could shove any data into any column. No rules, no guardrails. That's like building a house without a building code -- sure, it stands up, but the first strong wind is going to cause problems. In this module, we're going to learn how to design tables with data types, constraints, and relationships. These are the blueprints and building codes for your data.

---

## The Five Types of Data SQLite Understands

> 🎯 **Teach:** SQLite has five storage classes, and understanding them helps you choose the right type for each column.
> **See:** The five types mapped to real-world examples -- whole numbers, decimals, text, binary blobs, and the concept of "nothing."
> **Feel:** Confident about picking the right data type without overthinking it.

> 🔄 **Where this fits:** Data types are the foundation of table design. Every column you create needs a type, and the type you choose determines what kind of data can go in that column.

Before you build a table, you need to know what kinds of data you can store. SQLite keeps it simple -- there are only five:

| Storage Class | What It Stores | Real-World Example |
|---------------|---------------|-------------------|
| `INTEGER` | Whole numbers | Age, ID number, quantity |
| `REAL` | Decimal numbers | GPA, salary, price |
| `TEXT` | Strings of characters | Name, email, department |
| `BLOB` | Binary data (raw bytes) | Images, files, audio |
| `NULL` | The absence of a value | "We don't know yet" |

![Five types. That's it. SQLite keeps things simple.](../images/module-01/m01-five-data-types-01.png)
*Five types. Compare this to PostgreSQL's 40+ types. SQLite keeps things simple.*

A few important notes:

**INTEGER vs. REAL:** Use INTEGER for things you count (people, items, IDs). Use REAL for things you measure (money, GPA, temperature).

**TEXT:** This is your workhorse. Names, emails, dates (yes, SQLite stores dates as text), descriptions -- all TEXT.

**NULL:** This is NOT zero. It's NOT an empty string. It means "this value is unknown or doesn't exist." Think of it as a blank space on a form that hasn't been filled in yet. We'll see NULL cause some interesting surprises later.

> 🎙️ Here's a quirk about SQLite that confuses people coming from other databases. SQLite uses something called "type affinity" -- it's flexible about types. If you declare a column as INTEGER but insert the text "hello," SQLite won't stop you. Other databases would throw an error. This is why constraints -- which we'll cover next -- are extra important in SQLite. They're your real enforcement mechanism.

> 💡 **Remember this one thing:** When in doubt: use INTEGER for whole numbers, REAL for decimals, TEXT for everything else. You'll be right 95% of the time.

---

## Constraints: Your Data's Bodyguards

> 🎯 **Teach:** Constraints are rules attached to columns that automatically reject bad data before it gets into your table.
> **See:** Each constraint as a specific type of bouncer at the door -- one checks for empty values, one checks for duplicates, one checks if the data is reasonable.
> **Feel:** Relief that you don't have to manually check every piece of data -- the database does it for you.

OK, here's where tables get smart.

A **constraint** is a rule you attach to a column. When someone tries to insert data, the database checks the rules FIRST. If the data breaks a rule, the insert is rejected. No bad data gets in.

Think of constraints as bouncers at a nightclub. Each bouncer checks one thing:

![Constraints are bouncers. Each one checks a different rule at the door.](../images/module-01/m01-constraint-bouncers-01.png)
*PRIMARY KEY checks your ID. NOT NULL checks you exist. UNIQUE checks you're not already inside. CHECK... checks whatever you tell it to check.*

Let's meet the crew.

### PRIMARY KEY -- "You need a unique ID"

Every table should have a primary key -- a column (or combination of columns) that uniquely identifies each row.

```sql
id INTEGER PRIMARY KEY
```

Think of it like a student ID number. No two students share the same ID, and every student has one.

### AUTOINCREMENT -- "I'll assign your number"

Pair this with PRIMARY KEY and SQLite will automatically assign the next number:

```sql
id INTEGER PRIMARY KEY AUTOINCREMENT
```

You insert a row without specifying an ID, and SQLite says "You're number 1. Next person is number 2." And so on.

### NOT NULL -- "You MUST fill this in"

```sql
first_name TEXT NOT NULL
```

This column cannot be empty. It's like a required field on a web form -- that red asterisk that won't let you submit until you fill it in.

### UNIQUE -- "No duplicates allowed"

```sql
email TEXT UNIQUE
```

No two rows can have the same value in this column. Perfect for emails, usernames, social security numbers -- anything that should be one-of-a-kind.

### DEFAULT -- "If you don't tell me, I'll assume THIS"

```sql
status TEXT DEFAULT 'active'
enrollment_date TEXT DEFAULT (date('now'))
```

If you insert a row without specifying this column, the default value kicks in. It's like a form that pre-fills "Country: United States" -- you can change it, but if you don't, there's a sensible default.

### CHECK -- "Prove it's reasonable"

```sql
gpa REAL CHECK(gpa >= 0.0 AND gpa <= 4.0)
age INTEGER CHECK(age >= 0)
```

CHECK lets you write a custom rule. "GPA must be between 0 and 4." "Age can't be negative." If the data doesn't pass the test, it's rejected.

> 🎙️ Here's the mindset shift. Without constraints, YOU are responsible for making sure every piece of data is valid -- every time, forever. With constraints, the DATABASE is responsible. It never gets tired, it never forgets to check, and it never lets bad data slip through because it's Friday afternoon and everyone wants to go home. Constraints are your safety net. Use them generously.

---

## Putting It All Together: A Real Table

> 🎯 **Teach:** A well-designed table combines data types and constraints into a blueprint that documents itself.
> **See:** A complete CREATE TABLE statement where every line serves a purpose, with comments explaining the reasoning.
> **Feel:** Appreciation for how a few lines of SQL encode a surprising amount of business logic.

Here's what a properly designed table looks like:

```sql
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,       -- Unique ID, auto-assigned
    first_name TEXT NOT NULL,                    -- Required
    last_name TEXT NOT NULL,                     -- Required
    email TEXT UNIQUE NOT NULL,                  -- Required, no duplicates
    gpa REAL CHECK(gpa >= 0.0 AND gpa <= 4.0),  -- Must be valid GPA
    enrollment_date TEXT DEFAULT (date('now'))   -- Auto-fills with today's date
);
```

Read that out loud: "Each student has an auto-assigned ID, a required first name, a required last name, a required unique email, an optional GPA that must be between 0 and 4, and an enrollment date that defaults to today."

That's not just a table definition -- it's a **contract**. It documents the rules of your data in the same place where the data lives.

> 💡 **Remember this one thing:** A well-designed CREATE TABLE statement is both structure AND documentation. Anyone reading it can understand exactly what data is expected and what rules apply.

> 🎙️ Look at that students table for a second. Six lines of SQL, and each line is doing real work. One line guarantees uniqueness. One line guarantees a valid GPA range. One line fills in today's date automatically. When you see a well-designed CREATE TABLE statement, it reads like a specification document -- except the database actually enforces every rule. That's the goal. Make your tables self-documenting and self-defending.

---

## Table-Level Constraints: The Big Picture Rules

> 🎯 **Teach:** Some rules apply across multiple columns or reference other tables -- these are table-level constraints like composite keys and foreign keys.
> **See:** How composite primary keys work (two columns together form the key) and how foreign keys create relationships between tables.
> **Feel:** The "aha" of understanding how tables connect to each other -- this is the "relational" in relational database.

Some constraints don't belong to a single column -- they span multiple columns or reference other tables entirely. These go at the bottom of the CREATE TABLE statement, after all the columns.

### Composite Primary Keys -- "Two Columns, One Identity"

Sometimes one column isn't enough to uniquely identify a row. For example: a student can enroll in many courses, and a course can have many students. But a student should only be enrolled in each course *once*.

The combination of `student_id` + `course_id` is the unique identifier:

```sql
CREATE TABLE enrollments (
    student_id INTEGER NOT NULL,
    course_id INTEGER NOT NULL,
    grade TEXT CHECK(grade IN ('A', 'B', 'C', 'D', 'F') OR grade IS NULL),
    enrolled_date TEXT DEFAULT (date('now')),
    PRIMARY KEY (student_id, course_id)
);
```

That `PRIMARY KEY (student_id, course_id)` at the bottom says: "The combination of these two columns must be unique. Student 1 in Course 3 can only appear once."

### Foreign Keys -- "This Value Must Exist Over THERE"

A **foreign key** says: "This column references a row in another table." It's how tables relate to each other.

```sql
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

Those FOREIGN KEY lines say: "The `student_id` must match an existing `id` in the `students` table, and the `course_id` must match an existing `id` in the `courses` table."

If someone tries to enroll student 999 (who doesn't exist), the database says NO.

![Foreign keys are like arrows connecting tables -- they enforce that references are valid.](../images/module-01/m01-foreign-key-arrows-01.png)
*Foreign keys are the "relational" in relational database. They connect your tables with guaranteed-valid references.*

> **Watch it!** SQLite has foreign keys OFF by default. You must turn them on each time you open the database:

```sql
PRAGMA foreign_keys = ON;
```

This is a SQLite quirk. MySQL and PostgreSQL enforce foreign keys automatically.

> 🎙️ Foreign keys are where the magic of relational databases really shows up. Without them, you could enroll a student who doesn't exist in a course that doesn't exist. With them, the database guarantees that every reference points to something real. It's like a hyperlink that's guaranteed to never be a 404 error.

---

## Modifying Tables: ALTER and DROP

> 🎯 **Teach:** Tables aren't permanent sculptures -- you can add columns with ALTER TABLE or remove entire tables with DROP TABLE.
> **See:** The limited but useful ALTER TABLE operations in SQLite, and the "nuclear option" of DROP TABLE.
> **Feel:** Comfortable knowing you can evolve your table designs, but cautious about destructive operations.

Tables aren't set in stone. You can change them after creation.

### Adding a Column

```sql
ALTER TABLE students ADD COLUMN phone TEXT;
```

This adds a new `phone` column to every existing row (filled with NULL for existing rows).

### Renaming a Table

```sql
ALTER TABLE old_name RENAME TO new_name;
```

### The Nuclear Option: DROP TABLE

```sql
DROP TABLE IF EXISTS table_name;
```

This **deletes the entire table and all its data**. Gone. Forever. The `IF EXISTS` part prevents an error if the table doesn't exist.

> **Watch it!** SQLite's ALTER TABLE is limited. You can add columns and rename tables, but you can't drop columns, rename columns, or change constraints in older versions (column dropping was added in SQLite 3.35.0). If you need to change a column's type or constraints, the typical approach is: create a new table, copy the data, drop the old table, rename the new one.

> 🎙️ DROP TABLE is the delete key for tables. Use it freely during learning -- you can always recreate the table. But in a production database with real data? Treat it like a loaded weapon. The IF EXISTS clause is your safety catch -- always include it.

---

## 🗨️ There Are No Dumb Questions

> 🎯 **Teach:** Clear up the most common confusions about data types, constraints, and table design.
> **See:** Practical answers that connect abstract concepts to real decision-making.
> **Feel:** Confident enough to start designing tables without second-guessing every choice.

**Q: If SQLite is flexible about types, why bother declaring them at all?**

A: Two reasons. First, it documents your intent -- anyone reading your schema knows that `salary` is supposed to be a number. Second, SQLite does use type affinity to make smart storage decisions even if it doesn't strictly enforce types. And when you move to MySQL or PostgreSQL someday, strict types will be enforced.

**Q: What's the difference between PRIMARY KEY and UNIQUE?**

A: A table can only have ONE primary key (which can span multiple columns). It can have MANY unique constraints. The primary key is the "official" way to identify a row. UNIQUE just means "no duplicates in this column." Also, PRIMARY KEY implies NOT NULL in most databases.

**Q: Should every table have an AUTOINCREMENT id?**

A: It's a solid default pattern. Some tables (like our `enrollments` table) use composite primary keys instead, where the combination of two foreign keys is the natural identifier. But when in doubt, `id INTEGER PRIMARY KEY AUTOINCREMENT` is a safe bet.

**Q: What happens to existing data when I ADD COLUMN?**

A: All existing rows get NULL in the new column. If you add a column with a DEFAULT, existing rows still get NULL (the default only applies to future inserts). If you add a column with NOT NULL and no default, the ALTER TABLE will fail -- SQLite can't fill in a value for existing rows.

**Q: Can I have a FOREIGN KEY that references a column other than the primary key?**

A: Technically yes -- it can reference any UNIQUE column. But 99% of the time, foreign keys reference primary keys. Keep it simple.

> 🎙️ The primary-key-versus-unique question comes up in every cohort. Here's the shorthand. Primary key is the row's official name -- the one the database uses to find it quickly. Unique is just a promise that no two rows share a value. One table, one primary key. But you can have many unique columns. Use primary key for identity, unique for anything else that shouldn't repeat.

---

## ✏️ Sharpen Your Pencil

> 🎯 **Teach:** Building three interconnected tables from specs teaches the full design cycle -- types, constraints, and relationships.
> **See:** Six exercises progressing from simple table creation to constraint testing to schema modification.
> **Feel:** Accomplishment at building a real (small) university database schema from scratch.

Time to build a proper database. You're going to create three interconnected tables for a university system.

### Exercise 1: Set Up

Create a new database and enable foreign keys:

```bash
sqlite3 day02.db
```

```sql
PRAGMA foreign_keys = ON;
```

### Exercise 2: Create the Students Table

Build the `students` table using this specification:

| Column | Type | Constraints |
|--------|------|-------------|
| id | INTEGER | PRIMARY KEY AUTOINCREMENT |
| first_name | TEXT | NOT NULL |
| last_name | TEXT | NOT NULL |
| email | TEXT | UNIQUE, NOT NULL |
| gpa | REAL | CHECK(gpa >= 0.0 AND gpa <= 4.0) |
| enrollment_date | TEXT | DEFAULT (date('now')) |

Write the CREATE TABLE statement yourself. Then run `.schema students` to verify.

### Exercise 3: Create the Courses Table

Build the `courses` table:

| Column | Type | Constraints |
|--------|------|-------------|
| id | INTEGER | PRIMARY KEY AUTOINCREMENT |
| course_code | TEXT | UNIQUE, NOT NULL |
| title | TEXT | NOT NULL |
| credits | INTEGER | NOT NULL, CHECK(credits > 0 AND credits <= 6) |
| department | TEXT | DEFAULT 'Undeclared' |

Write and execute it. Verify with `.schema courses`.

### Exercise 4: Create the Enrollments Table

This is the big one. Build the `enrollments` table with:

| Column | Type | Constraints |
|--------|------|-------------|
| student_id | INTEGER | NOT NULL, FOREIGN KEY references students(id) |
| course_id | INTEGER | NOT NULL, FOREIGN KEY references courses(id) |
| grade | TEXT | CHECK(grade IN ('A', 'B', 'C', 'D', 'F') OR grade IS NULL) |
| enrolled_date | TEXT | DEFAULT (date('now')) |

The primary key is the combination of `(student_id, course_id)`.

Run `.tables` to confirm all three tables exist.

### Exercise 5: Test Your Constraints

Try each of these and record what happens:

**Test NOT NULL:**
```sql
INSERT INTO students (last_name, email) VALUES ('Doe', 'doe@example.com');
```

**Test UNIQUE:**
```sql
INSERT INTO students (first_name, last_name, email, gpa)
VALUES ('Jane', 'Doe', 'jane@example.com', 3.5);

INSERT INTO students (first_name, last_name, email, gpa)
VALUES ('John', 'Smith', 'jane@example.com', 3.0);
```

**Test CHECK:**
```sql
INSERT INTO students (first_name, last_name, email, gpa)
VALUES ('Bad', 'Data', 'bad@example.com', 5.0);
```

**Test DEFAULT:**
```sql
INSERT INTO students (first_name, last_name, email, gpa)
VALUES ('Test', 'User', 'test@example.com', 3.2);

.headers on
.mode column
SELECT * FROM students WHERE email = 'test@example.com';
```

Did the `enrollment_date` fill in automatically?

### Exercise 6: ALTER TABLE and DROP TABLE

**Add a column:**
```sql
ALTER TABLE students ADD COLUMN phone TEXT;
```

Run `.schema students` -- can you see the new column?

**Create and drop a throwaway table:**
```sql
CREATE TABLE temp_test (id INTEGER PRIMARY KEY, note TEXT);
.tables
DROP TABLE temp_test;
.tables
```

Record the `.tables` output before and after the DROP.

> 🎙️ Exercise 4 is the most important one here. The enrollments table has a composite primary key AND foreign keys -- that's real-world table design. If you can build that table and understand why each constraint is there, you've leveled up significantly from Module 0. Take your time and make sure you understand every line.

---

## Bullet Points

- **SQLite has five data types:** INTEGER, REAL, TEXT, BLOB, and NULL. When in doubt, INTEGER for counts, REAL for measurements, TEXT for everything else.
- **Constraints are your safety net.** They enforce rules at the database level so you don't have to check every insert manually.
- **PRIMARY KEY** uniquely identifies each row. **AUTOINCREMENT** assigns IDs automatically.
- **NOT NULL** = required field. **UNIQUE** = no duplicates. **DEFAULT** = fallback value. **CHECK** = custom validation rule.
- **Composite primary keys** use two or more columns together as the unique identifier.
- **Foreign keys** connect tables by requiring that a value exists in another table. Turn them on with `PRAGMA foreign_keys = ON;`.
- **ALTER TABLE** can add columns and rename tables. **DROP TABLE** deletes a table entirely.
- **A good CREATE TABLE statement is both structure AND documentation.** Anyone should be able to read it and understand the rules.

> 🎙️ Let's recap. You started this module knowing how to create basic tables. Now you know how to create tables with real rules -- types that describe the data, constraints that enforce quality, and foreign keys that connect tables together. Your tables went from empty spreadsheets to self-defending data structures. In the next module, you'll learn how to fill these tables with data -- and what happens when data breaks the rules.

---

## Up Next

> 🎯 **Teach:** The next module covers INSERT -- all the ways to get data into your carefully designed tables.
> **See:** The link to Module 2 and the preview that inserting data is more nuanced than it first appears.
> **Feel:** Curious about what happens when you try to insert data that violates the constraints you just built.

[Module 2: Inserting Data](./module-02-inserting-data.md) -- You've built tables with rules. Now let's see what happens when you start filling them with data -- including what happens when the data fights back against your constraints.

> 🎙️ That's Module 1 in the books. You know data types, constraints, composite keys, foreign keys, ALTER TABLE, and DROP TABLE. That's a serious toolkit. Next up, we're going to fill these tables with data using INSERT -- single rows, multiple rows, and what to do when things go wrong. See you in Module 2.
