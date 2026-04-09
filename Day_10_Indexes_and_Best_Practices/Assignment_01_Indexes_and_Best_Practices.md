# Day 10 Assignment: Indexes and Best Practices

## Overview

- **Topic:** CREATE INDEX, UNIQUE INDEX, EXPLAIN QUERY PLAN, SQL Injection, Normalization, Naming Conventions
- **Type:** Technical / Hands-On
- **Estimated Time:** 30 minutes

## Background

### Indexes

An index is a data structure that speeds up lookups on a column, similar to the index at the back of a textbook. Without an index, SQLite must scan every row (a "full table scan"). With an index, it can jump directly to the matching rows.

```sql
-- Create an index on the major column
CREATE INDEX idx_students_major ON students(major);

-- Create a unique index (enforces uniqueness)
CREATE UNIQUE INDEX idx_students_email ON students(email);

-- Drop an index
DROP INDEX idx_students_major;
```

### When to Create Indexes

Create indexes on columns that are frequently used in:
- `WHERE` clauses
- `JOIN` conditions
- `ORDER BY` clauses

### When NOT to Create Indexes

Avoid indexes on:
- Tables with very few rows (the overhead is not worth it)
- Columns with very few distinct values (e.g., a boolean column)
- Columns that are updated very frequently (indexes slow down writes)

### Composite Indexes

An index on multiple columns, useful when you frequently filter or sort by a combination.

```sql
CREATE INDEX idx_enrollments_student_course
ON enrollments(student_id, course_id);
```

The order of columns matters: this index helps queries that filter by `student_id` alone or by both `student_id` and `course_id`, but not queries that filter only by `course_id`.

### EXPLAIN QUERY PLAN

SQLite's `EXPLAIN QUERY PLAN` shows how a query will be executed, letting you see whether it uses an index or a full table scan.

```sql
EXPLAIN QUERY PLAN
SELECT * FROM students WHERE major = 'Biology';
```

Output before indexing might show:
```
SCAN students
```

After creating an index on `major`, it might show:
```
SEARCH students USING INDEX idx_students_major (major=?)
```

### SQL Injection

SQL injection is a security vulnerability where an attacker inserts malicious SQL into a query through user input.

**Vulnerable code (never do this):**
```python
# DANGEROUS: user input is inserted directly into the query
query = "SELECT * FROM students WHERE name = '" + user_input + "'"
```

If `user_input` is `'; DROP TABLE students; --`, the query becomes:
```sql
SELECT * FROM students WHERE name = ''; DROP TABLE students; --'
```

**Safe code (always do this):**
```python
# SAFE: parameterized query
cursor.execute("SELECT * FROM students WHERE name = ?", (user_input,))
```

Parameterized queries treat user input as data, never as SQL code.

### Normalization Basics

Normalization organizes tables to reduce data redundancy and improve integrity.

- **First Normal Form (1NF):** Each column contains a single value (no lists or sets). Each row is unique.
- **Second Normal Form (2NF):** Meets 1NF, and every non-key column depends on the entire primary key (not just part of it).
- **Third Normal Form (3NF):** Meets 2NF, and no non-key column depends on another non-key column.

**Example of a violation (not 3NF):**
```
students: id, name, major, department_building
```

Here, `department_building` depends on `major`, not on the student's `id`. To fix this, move `department_building` into a separate `majors` or `departments` table.

### Naming Conventions

Consistent naming makes SQL easier to read and maintain:
- Table names: plural, lowercase, snake_case (`students`, `course_enrollments`)
- Column names: singular, lowercase, snake_case (`first_name`, `student_id`)
- Primary keys: `id` or `table_name_id`
- Foreign keys: `referenced_table_id` (e.g., `student_id` references `students.id`)
- Indexes: `idx_table_column` (e.g., `idx_students_major`)

---

## Part 1: Creating and Using Indexes

### Task A: Analyze before indexing

Run the following queries with `EXPLAIN QUERY PLAN` and record the output:

```sql
EXPLAIN QUERY PLAN SELECT * FROM students WHERE major = 'Biology';
EXPLAIN QUERY PLAN SELECT * FROM enrollments WHERE student_id = 3;
EXPLAIN QUERY PLAN SELECT * FROM courses WHERE department = 'Science';
```

### Task B: Create indexes

Create the following indexes:

1. An index named `idx_students_major` on the `students` table's `major` column.
2. An index named `idx_enrollments_student_id` on the `enrollments` table's `student_id` column.
3. An index named `idx_courses_department` on the `courses` table's `department` column.
4. A unique index named `idx_students_email` on the `students` table's `email` column.

### Task C: Analyze after indexing

Re-run the same three `EXPLAIN QUERY PLAN` queries from Task A. Record the new output and note the differences. In your output file, write 1-2 sentences explaining what changed.

### Task D: Composite index

Create a composite index named `idx_enrollments_student_course` on the `enrollments` table covering both `student_id` and `course_id`. Then run:

```sql
EXPLAIN QUERY PLAN
SELECT * FROM enrollments WHERE student_id = 1 AND course_id = 2;
```

Record whether the composite index is used.

---

## Part 2: SQL Injection

### Task A: Identify the vulnerability

Look at the following Python code and explain in your output file what would happen if `user_input` is set to `' OR '1'='1`:

```python
user_input = "' OR '1'='1"
query = "SELECT * FROM students WHERE name = '" + user_input + "'"
```

Write out the full SQL query that would be executed. Explain why this is dangerous.

### Task B: Write the safe version

Write the parameterized version of the query from Task A using Python's `sqlite3` module syntax (using `?` as the placeholder). Explain in 1-2 sentences why parameterized queries prevent SQL injection.

### Task C: Another injection example

Explain what would happen if `user_input` is `'; DROP TABLE students; --`. Write out the full SQL that would be executed and explain the result.

---

## Part 3: Normalization

### Task A: Identify normal form violations

The following table stores order data. Identify which normal form it violates and explain why:

```
orders table:
| order_id | customer_name | customer_email      | items              | item_prices  |
|----------|---------------|---------------------|--------------------|--------------|
| 1        | Alice         | alice@example.com   | Book, Pen, Notebook| 15.99, 2.50, 5.00 |
| 2        | Bob           | bob@example.com     | Pen                | 2.50         |
```

### Task B: Normalize to 3NF

Redesign the orders table from Task A into a set of normalized tables (at least 3NF). Write the `CREATE TABLE` statements for each table with appropriate primary keys, foreign keys, and data types. Your design should include at least three tables.

### Task C: Design a normalized schema

Design a normalized schema (3NF) for a **library system** with the following requirements:
- Track books (title, ISBN, publication year)
- Track authors (name, birth year) -- a book can have multiple authors
- Track members (name, email, membership date)
- Track checkouts (which member checked out which book, checkout date, return date)

Write the `CREATE TABLE` statements for all necessary tables, including junction tables for many-to-many relationships.

---

## Part 4: Best Practices Review

### Task A: Naming conventions

The following table and column names violate common naming conventions. Rewrite them following the conventions described in the Background section:

1. Table: `StudentData`, Columns: `FirstName`, `LastName`, `E-mail`, `GPA Score`
2. Table: `class`, Columns: `ID`, `Class Name`, `dept.`, `numberOfCredits`
3. Foreign key column in enrollments referencing students: `sid`

### Task B: Index decision-making

For each of the following scenarios, state whether you would create an index and briefly explain why or why not:

1. A `users` table with 10 million rows; queries frequently filter by `email`.
2. A `settings` table with 5 rows.
3. A `logs` table that receives 10,000 inserts per second; queries rarely read from it.
4. A `products` table with 50,000 rows; queries frequently sort by `price`.
5. A `flags` table with a `is_active` column that is either 0 or 1.

### Task C: Query optimization

Write an optimized version of the following query. Explain what you changed and why:

```sql
SELECT *
FROM students, enrollments, courses
WHERE students.id = enrollments.student_id
AND courses.id = enrollments.course_id
AND students.major = 'Biology';
```

Your optimized version should use explicit JOIN syntax, select only necessary columns (student name, course name, grade), and use table aliases.

---

## Submission

Save a file named `Day_10_Output.md` in this folder containing the SQL queries and their output.

## Grading Criteria

| Criteria | Points |
|----------|--------|
| Part 1: Indexes and EXPLAIN QUERY PLAN (Tasks A-D) | 30 |
| Part 2: SQL injection understanding (Tasks A-C) | 20 |
| Part 3: Normalization and schema design (Tasks A-C) | 30 |
| Part 4: Best practices and optimization (Tasks A-C) | 20 |
| **Total** | **100** |
