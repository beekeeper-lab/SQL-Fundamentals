# Day 4 Assignment: SELECT and Filtering

## Overview

- **Topic:** SELECT, WHERE Clause, Comparison Operators, Logical Operators, Pattern Matching, Aliases
- **Type:** Technical / Hands-On
- **Estimated Time:** 30 minutes

## Background

### SELECT Basics

The `SELECT` statement retrieves data from tables:

```sql
-- Select specific columns
SELECT first_name, last_name FROM students;

-- Select all columns
SELECT * FROM students;
```

### WHERE Clause

`WHERE` filters rows based on conditions:

```sql
SELECT * FROM students WHERE gpa > 3.0;
```

### Comparison Operators

| Operator | Meaning |
|----------|---------|
| `=` | Equal to |
| `!=` or `<>` | Not equal to |
| `<` | Less than |
| `>` | Greater than |
| `<=` | Less than or equal to |
| `>=` | Greater than or equal to |

### Logical Operators

Combine multiple conditions with `AND`, `OR`, and `NOT`:

```sql
-- Both conditions must be true
SELECT * FROM students WHERE gpa > 3.0 AND department = 'CS';

-- Either condition can be true
SELECT * FROM students WHERE gpa > 3.5 OR department = 'Math';

-- Negate a condition
SELECT * FROM students WHERE NOT department = 'English';
```

Use parentheses to control evaluation order:

```sql
SELECT * FROM students
WHERE (gpa > 3.0 AND department = 'CS') OR gpa > 3.8;
```

### BETWEEN

Tests if a value falls within a range (inclusive on both ends):

```sql
SELECT * FROM students WHERE gpa BETWEEN 3.0 AND 3.5;
-- Equivalent to: WHERE gpa >= 3.0 AND gpa <= 3.5
```

### IN

Tests if a value matches any value in a list:

```sql
SELECT * FROM courses WHERE department IN ('Computer Science', 'Mathematics');
-- Equivalent to: WHERE department = 'Computer Science' OR department = 'Mathematics'
```

### LIKE (Pattern Matching)

| Pattern | Meaning |
|---------|---------|
| `%` | Matches zero or more characters |
| `_` | Matches exactly one character |

```sql
-- Names starting with 'A'
SELECT * FROM students WHERE first_name LIKE 'A%';

-- Names with exactly 3 characters
SELECT * FROM students WHERE first_name LIKE '___';

-- Email containing 'university'
SELECT * FROM students WHERE email LIKE '%university%';
```

### IS NULL / IS NOT NULL

NULL requires special operators — you cannot use `=` or `!=` with NULL:

```sql
-- Find rows where gpa is missing
SELECT * FROM students WHERE gpa IS NULL;

-- Find rows where gpa has a value
SELECT * FROM students WHERE gpa IS NOT NULL;
```

### Column Aliases with AS

Rename columns in the output:

```sql
SELECT first_name AS "First Name", gpa AS "Grade Point Average"
FROM students;
```

---

## Part 1: Set Up the Database

### Task A: Create and populate the database

Create a new database and set up the tables with data. Run the following:

```bash
sqlite3 day04.db
```

```sql
PRAGMA foreign_keys = ON;
.headers on
.mode column

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

INSERT INTO students (first_name, last_name, email, gpa) VALUES
    ('Alice', 'Johnson', 'alice.j@university.edu', 3.8),
    ('Bob', 'Smith', 'bob.smith@university.edu', 2.9),
    ('Carol', 'Williams', 'carol.w@university.edu', 3.5),
    ('David', 'Brown', 'david.b@university.edu', 3.1),
    ('Eve', 'Davis', 'eve.d@university.edu', 3.9),
    ('Frank', 'Miller', 'frank.m@university.edu', 2.5),
    ('Grace', 'Wilson', 'grace.w@university.edu', 3.3),
    ('Henry', 'Moore', 'henry.m@university.edu', 2.8),
    ('Iris', 'Taylor', 'iris.t@university.edu', NULL),
    ('Jack', 'Anderson', 'jack.a@university.edu', 3.0);

INSERT INTO courses (course_code, title, credits, department) VALUES
    ('CS101', 'Intro to Computer Science', 4, 'Computer Science'),
    ('CS201', 'Data Structures', 4, 'Computer Science'),
    ('MATH101', 'Calculus I', 4, 'Mathematics'),
    ('ENG101', 'English Composition', 3, 'English'),
    ('GEN100', 'Freshman Seminar', 1, 'Undeclared'),
    ('MATH201', 'Linear Algebra', 3, 'Mathematics');

INSERT INTO enrollments (student_id, course_id, grade) VALUES
    (1, 1, 'A'),
    (1, 3, 'B'),
    (2, 1, 'C'),
    (2, 4, 'B'),
    (3, 2, 'A'),
    (3, 3, NULL),
    (4, 1, NULL),
    (5, 2, 'A'),
    (5, 5, NULL),
    (6, 4, 'D'),
    (7, 1, 'B'),
    (7, 6, 'A'),
    (8, 3, 'C'),
    (9, 5, NULL),
    (10, 1, 'B');
```

Run `SELECT COUNT(*) FROM students;` and `SELECT COUNT(*) FROM enrollments;` to verify you have 10 students and 15 enrollments.

---

## Part 2: Basic SELECT Queries

### Task A: Select all students

```sql
SELECT * FROM students;
```

Record the output.

### Task B: Select specific columns

Write a query that returns only `first_name`, `last_name`, and `gpa` from the `students` table. Record the query and output.

### Task C: Use column aliases

Write a query that selects `course_code` as `"Code"`, `title` as `"Course Title"`, and `credits` as `"Credit Hours"` from the `courses` table. Record the query and output.

---

## Part 3: WHERE with Comparison Operators

Write and run each of the following queries. Record the SQL and the output for each.

### Task A: Equality

Find all students with a GPA of exactly 3.5.

### Task B: Not equal

Find all courses that are not in the `Computer Science` department.

### Task C: Greater than

Find all students with a GPA greater than 3.0.

### Task D: Less than or equal

Find all students with a GPA of 2.9 or below.

### Task E: Comparison on text

Find all students whose last name comes after 'M' alphabetically (i.e., `last_name > 'M'`).

---

## Part 4: Logical Operators (AND, OR, NOT)

Write and run each of the following queries. Record the SQL and the output for each.

### Task A: AND

Find students with a GPA above 3.0 AND whose first name starts with a letter between A and D (use `first_name < 'E'`).

### Task B: OR

Find courses that are in the `Mathematics` department OR have more than 3 credits.

### Task C: NOT

Find all students whose last name is NOT `Smith`.

### Task D: Combined logic with parentheses

Find students who either (have a GPA above 3.5) OR (have a GPA between 2.5 and 3.0 AND a last name starting with a letter after 'K'). Use parentheses to group the logic correctly.

---

## Part 5: BETWEEN, IN, and LIKE

Write and run each of the following queries. Record the SQL and the output for each.

### Task A: BETWEEN

Find all students with a GPA between 3.0 and 3.5 (inclusive).

### Task B: IN

Find all courses in the `Computer Science` or `Mathematics` departments using the `IN` operator.

### Task C: LIKE with %

Find all students whose email contains the word `university`.

### Task D: LIKE with _

Find all course codes that match the pattern: two letters followed by `101` (e.g., CS101, ENG101 would not match because ENG is three letters). Use `_` wildcards.

Hint: `__101` matches codes that are exactly 5 characters with `101` at the end.

### Task E: LIKE for names starting with a range

Find all students whose first name starts with a letter from A through D. Use four separate LIKE conditions combined with OR.

---

## Part 6: IS NULL and IS NOT NULL

### Task A: Find NULL values

Find all students where the GPA is NULL. Record the query and output.

### Task B: Find non-NULL values

Find all enrollments where the grade IS NOT NULL. Record the query and output.

### Task C: Count NULLs vs non-NULLs

Write two queries:
1. Count the number of enrollments that have a grade assigned.
2. Count the number of enrollments that do not have a grade assigned (grade IS NULL).

Record both queries and outputs.

---

## Part 7: Putting It All Together

### Task A: Complex query

Write a single query that finds all students who meet ALL of these criteria:
- GPA is not NULL
- GPA is between 2.5 and 3.5
- Last name does not start with 'W'

Record the query and output.

### Task B: Another complex query

Write a query against the `courses` table that finds courses where:
- The department is either `Computer Science` or `Mathematics`
- AND the number of credits is greater than or equal to 4

Record the query and output.

---

## Submission

Save a file named `Day_04_Output.md` in this folder containing the SQL queries and their output.

## Grading Criteria

| Criteria | Points |
|----------|--------|
| Database created and populated with correct data | 5 |
| SELECT * and SELECT with specific columns recorded | 5 |
| Column aliases used correctly | 5 |
| Equality comparison query correct | 5 |
| Not-equal comparison query correct | 5 |
| Greater-than comparison query correct | 5 |
| Less-than-or-equal comparison query correct | 5 |
| Text comparison query correct | 5 |
| AND query correct | 5 |
| OR query correct | 5 |
| NOT query correct | 5 |
| Combined logic with parentheses query correct | 5 |
| BETWEEN query correct | 5 |
| IN query correct | 5 |
| LIKE with % correct | 5 |
| LIKE with _ correct | 5 |
| IS NULL and IS NOT NULL queries correct | 5 |
| NULL vs non-NULL counts correct | 5 |
| Complex combined query (Part 7A) correct | 5 |
| Complex combined query (Part 7B) correct | 5 |
| **Total** | **100** |
