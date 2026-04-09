# Day 5 Assignment: Sorting and Limiting Results

## Overview

- **Topic:** ORDER BY, LIMIT, OFFSET, DISTINCT, Pagination, Top-N Queries
- **Type:** Technical / Hands-On
- **Estimated Time:** 30 minutes

## Background

### ORDER BY

`ORDER BY` sorts the result set by one or more columns. By default, sorting is ascending (`ASC`). Use `DESC` for descending order:

```sql
-- Sort by GPA, highest first
SELECT * FROM students ORDER BY gpa DESC;

-- Sort by last name alphabetically (ascending is the default)
SELECT * FROM students ORDER BY last_name;

-- Sort by department first, then by credits within each department
SELECT * FROM courses ORDER BY department ASC, credits DESC;
```

When sorting by multiple columns, the first column is the primary sort. Ties in the first column are broken by the second column, and so on.

### NULL Sorting Behavior

In SQLite, NULL values sort as if they are **smaller than any other value**:

- `ORDER BY gpa ASC` — NULLs appear first
- `ORDER BY gpa DESC` — NULLs appear last

### LIMIT

`LIMIT` restricts the number of rows returned:

```sql
-- Return only the first 5 rows
SELECT * FROM students LIMIT 5;
```

### OFFSET

`OFFSET` skips a number of rows before starting to return results. It is always used with `LIMIT`:

```sql
-- Skip the first 5 rows, then return the next 5
SELECT * FROM students LIMIT 5 OFFSET 5;
```

This creates a **pagination** pattern:

| Page | SQL |
|------|-----|
| Page 1 (rows 1-5) | `LIMIT 5 OFFSET 0` |
| Page 2 (rows 6-10) | `LIMIT 5 OFFSET 5` |
| Page 3 (rows 11-15) | `LIMIT 5 OFFSET 10` |

The general formula: `OFFSET = (page_number - 1) * page_size`

### DISTINCT

`DISTINCT` removes duplicate rows from the result:

```sql
-- List each unique department (no repeats)
SELECT DISTINCT department FROM courses;
```

### Combining Clauses

These clauses are used together in this order:

```sql
SELECT columns
FROM table
WHERE conditions
ORDER BY columns
LIMIT count
OFFSET skip;
```

Example:

```sql
-- Top 3 students by GPA who have a GPA above 3.0
SELECT first_name, last_name, gpa
FROM students
WHERE gpa > 3.0
ORDER BY gpa DESC
LIMIT 3;
```

---

## Part 1: Set Up the Database

### Task A: Create and populate the database

Create a new database with the same schema and data from Day 4, plus a few additional rows to make sorting and pagination more interesting.

```bash
sqlite3 day05.db
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
    ('Jack', 'Anderson', 'jack.a@university.edu', 3.0),
    ('Karen', 'Thomas', 'karen.t@university.edu', 3.5),
    ('Leo', 'Jackson', 'leo.j@university.edu', 2.7),
    ('Mia', 'White', 'mia.w@university.edu', 3.9),
    ('Noah', 'Harris', 'noah.h@university.edu', 3.2),
    ('Olivia', 'Martin', 'olivia.m@university.edu', NULL);

INSERT INTO courses (course_code, title, credits, department) VALUES
    ('CS101', 'Intro to Computer Science', 4, 'Computer Science'),
    ('CS201', 'Data Structures', 4, 'Computer Science'),
    ('CS301', 'Algorithms', 3, 'Computer Science'),
    ('MATH101', 'Calculus I', 4, 'Mathematics'),
    ('MATH201', 'Linear Algebra', 3, 'Mathematics'),
    ('ENG101', 'English Composition', 3, 'English'),
    ('ENG201', 'American Literature', 3, 'English'),
    ('GEN100', 'Freshman Seminar', 1, 'Undeclared');

INSERT INTO enrollments (student_id, course_id, grade) VALUES
    (1, 1, 'A'),
    (1, 4, 'B'),
    (2, 1, 'C'),
    (2, 6, 'B'),
    (3, 2, 'A'),
    (3, 4, NULL),
    (4, 1, NULL),
    (5, 2, 'A'),
    (5, 8, NULL),
    (6, 6, 'D'),
    (7, 1, 'B'),
    (7, 5, 'A'),
    (8, 4, 'C'),
    (9, 8, NULL),
    (10, 1, 'B'),
    (11, 2, 'A'),
    (11, 3, 'B'),
    (12, 6, 'C'),
    (13, 1, 'A'),
    (13, 3, 'A'),
    (14, 4, 'B'),
    (14, 5, NULL),
    (15, 8, NULL);
```

Verify the data: run `SELECT COUNT(*) FROM students;` (expect 15), `SELECT COUNT(*) FROM courses;` (expect 8), and `SELECT COUNT(*) FROM enrollments;` (expect 23). Record the output.

---

## Part 2: ORDER BY

### Task A: Single column sort (ascending)

Write a query that selects `first_name`, `last_name`, and `gpa` from `students`, sorted by `last_name` in ascending order. Record the query and output.

### Task B: Single column sort (descending)

Write a query that selects `first_name`, `last_name`, and `gpa` from `students`, sorted by `gpa` in descending order. Record the query and output.

Note where the NULL GPAs appear in the result.

### Task C: Multi-column sort

Write a query that selects all columns from `courses`, sorted by `department` ascending first, then by `credits` descending within each department. Record the query and output.

### Task D: Sort enrollments by grade

Write a query that selects all columns from `enrollments`, sorted by `grade` ascending. Record the output and note where NULL grades appear.

---

## Part 3: LIMIT and OFFSET

### Task A: Top 5 students by GPA

Write a query that returns the `first_name`, `last_name`, and `gpa` of the 5 students with the highest GPA. Exclude students with NULL GPAs.

Record the query and output.

### Task B: Bottom 3 students by GPA

Write a query that returns the 3 students with the lowest GPA (non-NULL). Record the query and output.

### Task C: Pagination — Page 1

Write a query that returns students sorted by `last_name`, showing page 1 with a page size of 5 (i.e., the first 5 students alphabetically). Record the query and output.

### Task D: Pagination — Page 2

Write a query that returns page 2 (students 6-10 alphabetically by last name). Record the query and output.

### Task E: Pagination — Page 3

Write a query that returns page 3 (students 11-15 alphabetically by last name). Record the query and output.

---

## Part 4: DISTINCT

### Task A: Unique departments

Write a query that returns each unique department from the `courses` table. Record the query and output.

### Task B: Unique grades

Write a query that returns each unique grade from the `enrollments` table. Record the query and output. Note that NULL appears as a distinct value.

### Task C: DISTINCT with multiple columns

Write a query that returns the distinct combinations of `department` and `credits` from the `courses` table, sorted by department. Record the query and output.

---

## Part 5: Combining WHERE, ORDER BY, and LIMIT

### Task A: Top 5 students by GPA with names A through M

Write a query that finds students whose first name starts with a letter from A through M (use `first_name < 'N'`), orders them by GPA descending, and returns only the top 5. Exclude NULL GPAs.

Record the query and output.

### Task B: Highest-credit courses outside Computer Science

Write a query that finds courses not in the `Computer Science` department, ordered by credits descending, and returns only the top 3.

Record the query and output.

### Task C: Students with GPA between 3.0 and 3.5, sorted by last name

Write a query that finds students with GPA between 3.0 and 3.5 (inclusive), sorted alphabetically by last name. Do not use LIMIT.

Record the query and output.

### Task D: The single highest-GPA student

Write a query that returns only the one student with the highest GPA. Record the query and output.

### Task E: Second-highest GPA

Write a query that returns only the student with the second-highest GPA. Use LIMIT and OFFSET together.

Record the query and output.

---

## Part 6: Practical Queries

### Task A: Student directory — paginated

Imagine you are building a student directory that shows 3 students per page, sorted by last name. Write the queries for pages 1 through 5. For each page, select `first_name`, `last_name`, and `email`.

Record all 5 queries and their outputs.

### Task B: Grade distribution

Write a query that shows all distinct non-NULL grades from enrollments, sorted alphabetically. Record the query and output.

### Task C: Courses sorted by department then title

Write a query that returns `department`, `course_code`, and `title` from courses, sorted first by `department` and then by `title` within each department. Record the query and output.

---

## Submission

Save a file named `Day_05_Output.md` in this folder containing the SQL queries and their output.

## Grading Criteria

| Criteria | Points |
|----------|--------|
| Database created and populated with correct data (15 students, 8 courses, 23 enrollments) | 5 |
| ORDER BY ascending query correct | 5 |
| ORDER BY descending query correct with NULL observation noted | 5 |
| Multi-column ORDER BY query correct | 5 |
| Enrollment sort by grade with NULL observation | 5 |
| Top 5 students by GPA query correct | 5 |
| Bottom 3 students by GPA query correct | 5 |
| Pagination pages 1, 2, and 3 all correct | 10 |
| DISTINCT departments query correct | 5 |
| DISTINCT grades query correct | 5 |
| DISTINCT with multiple columns correct | 5 |
| Top 5 A-M students by GPA correct | 5 |
| Highest-credit non-CS courses correct | 5 |
| GPA 3.0-3.5 sorted by last name correct | 5 |
| Single highest GPA query correct | 5 |
| Second-highest GPA using LIMIT/OFFSET correct | 5 |
| Student directory paginated (5 pages) correct | 5 |
| Grade distribution query correct | 5 |
| Courses sorted by department then title correct | 5 |
| **Total** | **100** |
