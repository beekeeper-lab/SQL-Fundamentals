# Day 2 Assignment: Creating Tables

## Overview

- **Topic:** CREATE TABLE, Data Types, Constraints, ALTER TABLE, DROP TABLE
- **Type:** Technical / Hands-On
- **Estimated Time:** 30 minutes

## Background

### SQLite Data Types

SQLite uses a flexible type system called **type affinity**. There are five storage classes:

| Storage Class | Description | Examples |
|---------------|-------------|---------|
| `INTEGER` | Whole numbers | 1, 42, -7 |
| `REAL` | Floating-point numbers | 3.14, 99.99 |
| `TEXT` | Strings | 'Alice', 'Hello World' |
| `BLOB` | Binary data (stored as-is) | Images, files |
| `NULL` | Absence of a value | NULL |

### Column Constraints

Constraints enforce rules on the data in a column:

```sql
CREATE TABLE example (
    id INTEGER PRIMARY KEY AUTOINCREMENT,  -- Unique row identifier, auto-assigned
    name TEXT NOT NULL,                     -- Cannot be NULL
    email TEXT UNIQUE,                      -- No two rows can have the same value
    age INTEGER CHECK(age >= 0),           -- Must satisfy the condition
    status TEXT DEFAULT 'active'           -- Used when no value is provided
);
```

| Constraint | Purpose |
|------------|---------|
| `PRIMARY KEY` | Uniquely identifies each row. Only one per table. |
| `AUTOINCREMENT` | Automatically assigns the next integer. Used with INTEGER PRIMARY KEY. |
| `NOT NULL` | The column must have a value — NULL is rejected. |
| `UNIQUE` | No duplicate values allowed in this column. |
| `DEFAULT` | Provides a fallback value when none is specified during INSERT. |
| `CHECK` | Validates that a condition is true before accepting the data. |

### Table-Level Constraints

Constraints can also be defined at the table level (after all columns), which is required for composite keys or multi-column constraints:

```sql
CREATE TABLE enrollment (
    student_id INTEGER,
    course_id INTEGER,
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (course_id) REFERENCES courses(id)
);
```

### Modifying and Dropping Tables

```sql
-- Add a new column to an existing table
ALTER TABLE students ADD COLUMN phone TEXT;

-- Rename a table
ALTER TABLE old_name RENAME TO new_name;

-- Delete a table entirely
DROP TABLE IF EXISTS table_name;
```

Note: SQLite has limited `ALTER TABLE` support. You cannot drop or rename columns in older versions (support was added in SQLite 3.35.0). You cannot modify a column's type or constraints after creation.

### Inspecting Tables

```sql
.schema              -- Show CREATE statements for all tables
.schema table_name   -- Show CREATE statement for one table
```

---

## Part 1: Create the Students Table

### Task A: Create a new database

Open a terminal and create a new database:

```bash
sqlite3 day02.db
```

Enable foreign key enforcement (SQLite has it off by default):

```sql
PRAGMA foreign_keys = ON;
```

### Task B: Create the `students` table

Create a table called `students` with the following specification:

| Column | Type | Constraints |
|--------|------|-------------|
| id | INTEGER | PRIMARY KEY AUTOINCREMENT |
| first_name | TEXT | NOT NULL |
| last_name | TEXT | NOT NULL |
| email | TEXT | UNIQUE, NOT NULL |
| gpa | REAL | CHECK(gpa >= 0.0 AND gpa <= 4.0) |
| enrollment_date | TEXT | DEFAULT (date('now')) |

Write and execute the `CREATE TABLE` statement. Then run `.schema students` and record the output.

---

## Part 2: Create the Courses Table

### Task A: Create the `courses` table

Create a table called `courses` with the following specification:

| Column | Type | Constraints |
|--------|------|-------------|
| id | INTEGER | PRIMARY KEY AUTOINCREMENT |
| course_code | TEXT | UNIQUE, NOT NULL |
| title | TEXT | NOT NULL |
| credits | INTEGER | NOT NULL, CHECK(credits > 0 AND credits <= 6) |
| department | TEXT | DEFAULT 'Undeclared' |

Write and execute the `CREATE TABLE` statement. Then run `.schema courses` and record the output.

---

## Part 3: Create the Enrollments Table

### Task A: Create the `enrollments` table

This table links students to courses. It uses a **composite primary key** (two columns together form the primary key) and **foreign keys** that reference the other tables.

Create a table called `enrollments` with the following specification:

| Column | Type | Constraints |
|--------|------|-------------|
| student_id | INTEGER | NOT NULL, FOREIGN KEY references students(id) |
| course_id | INTEGER | NOT NULL, FOREIGN KEY references courses(id) |
| grade | TEXT | CHECK(grade IN ('A', 'B', 'C', 'D', 'F', NULL)) |
| enrolled_date | TEXT | DEFAULT (date('now')) |

The primary key should be the combination of `(student_id, course_id)` — a student can only enroll in each course once.

Write and execute the `CREATE TABLE` statement. Then run `.schema enrollments` and record the output.

### Task B: Verify all tables

Run `.tables` and confirm all three tables appear. Record the output.

---

## Part 4: Test Your Constraints

### Task A: Test NOT NULL

Try to insert a student without a `first_name`:

```sql
INSERT INTO students (last_name, email) VALUES ('Doe', 'doe@example.com');
```

Record the error message.

### Task B: Test UNIQUE

Insert a student, then try to insert another with the same email:

```sql
INSERT INTO students (first_name, last_name, email, gpa) VALUES ('Jane', 'Doe', 'jane@example.com', 3.5);
INSERT INTO students (first_name, last_name, email, gpa) VALUES ('John', 'Smith', 'jane@example.com', 3.0);
```

Record the error message from the second INSERT.

### Task C: Test CHECK

Try to insert a student with a GPA of 5.0:

```sql
INSERT INTO students (first_name, last_name, email, gpa) VALUES ('Bad', 'Data', 'bad@example.com', 5.0);
```

Record the error message.

### Task D: Test DEFAULT

Insert a student without specifying `enrollment_date`:

```sql
INSERT INTO students (first_name, last_name, email, gpa) VALUES ('Test', 'User', 'test@example.com', 3.2);
```

Then query the row:

```sql
.headers on
.mode column
SELECT * FROM students WHERE email = 'test@example.com';
```

Record the output. Notice the `enrollment_date` column was filled in automatically.

---

## Part 5: ALTER TABLE and DROP TABLE

### Task A: Add a column

Add a `phone` column to the `students` table:

```sql
ALTER TABLE students ADD COLUMN phone TEXT;
```

Run `.schema students` and record the output showing the new column.

### Task B: Create and drop a temporary table

Create a throwaway table, verify it exists, then drop it:

```sql
CREATE TABLE temp_test (id INTEGER PRIMARY KEY, note TEXT);
.tables
DROP TABLE temp_test;
.tables
```

Record the `.tables` output before and after the DROP to confirm the table was removed.

---

## Submission

Save a file named `Day_02_Output.md` in this folder containing the SQL queries and their output.

## Grading Criteria

| Criteria | Points |
|----------|--------|
| `students` table created with all correct columns and constraints | 15 |
| `.schema students` output recorded | 5 |
| `courses` table created with all correct columns and constraints | 15 |
| `.schema courses` output recorded | 5 |
| `enrollments` table created with composite PK and foreign keys | 15 |
| `.tables` output showing all three tables | 5 |
| NOT NULL constraint violation tested and error recorded | 5 |
| UNIQUE constraint violation tested and error recorded | 5 |
| CHECK constraint violation tested and error recorded | 5 |
| DEFAULT value demonstrated and output recorded | 5 |
| ALTER TABLE ADD COLUMN executed and `.schema` recorded | 10 |
| DROP TABLE demonstrated with before/after `.tables` output | 5 |
| Output file is clearly organized with queries and results | 5 |
| **Total** | **100** |
