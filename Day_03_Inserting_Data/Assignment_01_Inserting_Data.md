# Day 3 Assignment: Inserting Data

## Overview

- **Topic:** INSERT INTO — Single Rows, Multiple Rows, Conflict Handling, NULLs, and DEFAULTs
- **Type:** Technical / Hands-On
- **Estimated Time:** 30 minutes

## Background

### INSERT Syntax

The basic `INSERT` statement adds one row at a time:

```sql
INSERT INTO table_name (column1, column2, column3)
VALUES ('value1', 'value2', 'value3');
```

You can omit the column list if you provide values for every column in order (except AUTOINCREMENT columns which accept NULL to auto-assign):

```sql
INSERT INTO table_name VALUES (NULL, 'value1', 'value2', 'value3');
```

However, always specifying the column list is considered best practice — it makes your intent clear and protects against schema changes.

### Inserting Multiple Rows

SQLite allows inserting multiple rows in a single statement:

```sql
INSERT INTO pets (name, species) VALUES
    ('Buddy', 'Dog'),
    ('Whiskers', 'Cat'),
    ('Goldie', 'Fish');
```

This is more efficient than three separate INSERT statements.

### Handling Conflicts

When an INSERT would violate a constraint (UNIQUE, PRIMARY KEY, NOT NULL, CHECK), SQLite normally raises an error and the row is rejected. You can change this behavior:

```sql
-- If a conflict occurs, silently skip the row
INSERT OR IGNORE INTO students (first_name, last_name, email, gpa)
VALUES ('Jane', 'Doe', 'jane@example.com', 3.5);

-- If a conflict occurs, replace the existing row with the new one
INSERT OR REPLACE INTO students (first_name, last_name, email, gpa)
VALUES ('Jane', 'Doe', 'jane@example.com', 3.8);
```

| Clause | Behavior on Conflict |
|--------|---------------------|
| (default) | Error — statement fails |
| `INSERT OR IGNORE` | Silently skips the conflicting row |
| `INSERT OR REPLACE` | Deletes the existing row and inserts the new one |
| `INSERT OR ABORT` | Same as default — aborts the statement |

### NULL Values

`NULL` represents the absence of a value. It is not the same as 0 or an empty string:

```sql
-- Explicitly insert NULL
INSERT INTO students (first_name, last_name, email, gpa)
VALUES ('Ghost', 'Student', 'ghost@example.com', NULL);
```

A column with a `NOT NULL` constraint will reject NULL values.

### DEFAULT Values

When a column has a `DEFAULT` defined, you can trigger it by omitting the column from the INSERT:

```sql
-- If 'department' has DEFAULT 'Undeclared', this uses the default:
INSERT INTO courses (course_code, title, credits)
VALUES ('GEN101', 'General Studies', 3);
```

---

## Part 1: Set Up the Database

### Task A: Create the database and tables

Create a new database and build the schema from Day 2. Run the following:

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

Run `.tables` to confirm all three tables exist. Record the output.

---

## Part 2: Insert Students

### Task A: Insert students one at a time

Insert the following 3 students using individual INSERT statements, specifying the column list each time:

| first_name | last_name | email | gpa |
|------------|-----------|-------|-----|
| Alice | Johnson | alice.j@university.edu | 3.8 |
| Bob | Smith | bob.smith@university.edu | 2.9 |
| Carol | Williams | carol.w@university.edu | 3.5 |

Record each INSERT statement and confirm success with:

```sql
SELECT * FROM students;
```

### Task B: Insert students using a multi-row INSERT

Insert the following 5 students in a single INSERT statement:

| first_name | last_name | email | gpa |
|------------|-----------|-------|-----|
| David | Brown | david.b@university.edu | 3.1 |
| Eve | Davis | eve.d@university.edu | 3.9 |
| Frank | Miller | frank.m@university.edu | 2.5 |
| Grace | Wilson | grace.w@university.edu | 3.3 |
| Henry | Moore | henry.m@university.edu | 2.8 |

Record the multi-row INSERT statement and run `SELECT * FROM students;` to show all 8 students.

---

## Part 3: Insert Courses

### Task A: Insert courses with explicit department values

Insert the following courses using a multi-row INSERT:

| course_code | title | credits | department |
|-------------|-------|---------|------------|
| CS101 | Intro to Computer Science | 4 | Computer Science |
| CS201 | Data Structures | 4 | Computer Science |
| MATH101 | Calculus I | 4 | Mathematics |
| ENG101 | English Composition | 3 | English |

### Task B: Insert a course that uses the DEFAULT value

Insert the following course without specifying a department:

| course_code | title | credits |
|-------------|-------|---------|
| GEN100 | Freshman Seminar | 1 |

Run the following and record the output:

```sql
.headers on
.mode column
SELECT * FROM courses;
```

Confirm that GEN100 has the department value `Undeclared`.

---

## Part 4: Insert Enrollments

### Task A: Enroll students in courses

Insert the following enrollment records. Some students have grades, some do not (NULL — they are currently enrolled):

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

Write the INSERT statements (you may use one multi-row INSERT or individual statements). Record the SQL used.

### Task B: Verify the data

Run the following and record the output:

```sql
SELECT * FROM enrollments;
```

Confirm there are 10 rows. Note which rows have NULL grades.

---

## Part 5: Handle Conflicts and Edge Cases

### Task A: Demonstrate INSERT OR IGNORE

Try to insert a duplicate student (same email as Alice):

```sql
INSERT OR IGNORE INTO students (first_name, last_name, email, gpa)
VALUES ('Alicia', 'Jones', 'alice.j@university.edu', 3.0);
```

Run `SELECT * FROM students WHERE email = 'alice.j@university.edu';` and record the output. The original Alice row should be unchanged.

### Task B: Demonstrate INSERT OR REPLACE

Now use INSERT OR REPLACE with the same email:

```sql
INSERT OR REPLACE INTO students (first_name, last_name, email, gpa)
VALUES ('Alicia', 'Jones', 'alice.j@university.edu', 3.0);
```

Run `SELECT * FROM students WHERE email = 'alice.j@university.edu';` and record the output. Note what changed (including the `id` value).

### Task C: Demonstrate a constraint violation

Try inserting a student with a GPA of -1.0:

```sql
INSERT INTO students (first_name, last_name, email, gpa)
VALUES ('Bad', 'Student', 'bad@university.edu', -1.0);
```

Record the error message.

### Task D: Insert a row with an explicit NULL

Insert a student with no GPA:

```sql
INSERT INTO students (first_name, last_name, email, gpa)
VALUES ('Iris', 'Taylor', 'iris.t@university.edu', NULL);
```

Run `SELECT * FROM students WHERE first_name = 'Iris';` and record the output. Note that `gpa` is NULL (not 0, not empty — NULL).

---

## Part 6: Verify Final State

### Task A: Record final row counts

Run the following queries and record each result:

```sql
SELECT COUNT(*) AS student_count FROM students;
SELECT COUNT(*) AS course_count FROM courses;
SELECT COUNT(*) AS enrollment_count FROM enrollments;
```

---

## Submission

Save a file named `Day_03_Output.md` in this folder containing the SQL queries and their output.

## Grading Criteria

| Criteria | Points |
|----------|--------|
| Database created with all three tables | 5 |
| 3 students inserted individually with correct syntax | 10 |
| 5 students inserted using multi-row INSERT | 10 |
| `SELECT * FROM students` output recorded after all inserts | 5 |
| 4 courses inserted with explicit department values | 10 |
| 1 course inserted using DEFAULT department value, verified | 5 |
| 10 enrollment rows inserted with correct foreign key values | 15 |
| NULL grades correctly represented in enrollments | 5 |
| INSERT OR IGNORE demonstrated with output recorded | 10 |
| INSERT OR REPLACE demonstrated with output and observations recorded | 10 |
| CHECK constraint violation demonstrated with error recorded | 5 |
| Explicit NULL insert demonstrated and output recorded | 5 |
| Final row counts recorded for all three tables | 5 |
| **Total** | **100** |
