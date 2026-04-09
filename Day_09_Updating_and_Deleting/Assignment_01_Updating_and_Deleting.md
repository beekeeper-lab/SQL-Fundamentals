# Day 9 Assignment: Updating and Deleting Data

## Overview

- **Topic:** UPDATE, DELETE, CASE expressions, Subqueries in UPDATE/DELETE, Transactions
- **Type:** Technical / Hands-On
- **Estimated Time:** 30 minutes

## Background

`UPDATE` and `DELETE` modify existing data. They are powerful and permanent, so you must use them carefully. The golden rule: **always include a WHERE clause** unless you intentionally want to affect every row.

### UPDATE

```sql
-- Update a single row
UPDATE students
SET gpa = 3.8
WHERE id = 1;

-- Update multiple columns
UPDATE students
SET gpa = 3.9, major = 'Physics'
WHERE name = 'Alice';
```

### DELETE

```sql
-- Delete specific rows
DELETE FROM enrollments
WHERE grade = 'F';

-- Delete all rows (dangerous!)
DELETE FROM students;  -- removes every student
```

### The Safety Rule: Always Test with SELECT First

Before running an UPDATE or DELETE, replace it with a SELECT to preview which rows will be affected.

```sql
-- Step 1: Preview what will be affected
SELECT * FROM students WHERE gpa < 2.0;

-- Step 2: If the results look correct, run the UPDATE/DELETE
DELETE FROM students WHERE gpa < 2.0;
```

### UPDATE with CASE

`CASE` lets you set different values based on conditions, all in one statement.

```sql
UPDATE students
SET gpa = CASE
    WHEN gpa >= 3.5 THEN gpa + 0.1
    WHEN gpa >= 2.5 THEN gpa + 0.2
    ELSE gpa + 0.3
END;
```

### UPDATE and DELETE with Subqueries

You can use subqueries to target rows based on data in other tables.

```sql
-- Delete enrollments for students in a specific major
DELETE FROM enrollments
WHERE student_id IN (SELECT id FROM students WHERE major = 'Art');

-- Update grades for students with high GPA
UPDATE enrollments
SET grade = 'A'
WHERE student_id IN (SELECT id FROM students WHERE gpa > 3.9);
```

### Transactions

A transaction groups multiple statements into a single unit of work. Either all statements succeed (COMMIT) or none of them take effect (ROLLBACK).

```sql
BEGIN TRANSACTION;

UPDATE students SET gpa = 3.5 WHERE id = 1;
UPDATE students SET gpa = 3.6 WHERE id = 2;

-- If everything looks good:
COMMIT;

-- If something went wrong, undo everything:
-- ROLLBACK;
```

Transactions are critical when multiple related changes must succeed or fail together.

---

## Part 1: Basic UPDATE

### Task A: Update a single student's GPA

Write a SELECT query to find the student with id = 1, noting their current GPA. Then write an UPDATE statement to change their GPA to 3.75. Write another SELECT to confirm the change.

### Task B: Update multiple columns

Write an UPDATE statement that changes the major to 'Data Science' and the GPA to 3.6 for any student currently majoring in 'Computer Science' who has a GPA below 3.0. First, write a SELECT to preview which students will be affected.

### Task C: UPDATE with CASE

Write an UPDATE statement using CASE that adjusts student GPAs as follows:
- GPA of 4.0: no change (keep at 4.0, since 4.0 is the max)
- GPA of 3.5 or above: increase by 0.1
- GPA of 3.0 or above: increase by 0.2
- GPA below 3.0: increase by 0.3

Cap the maximum GPA at 4.0 using `MIN(new_value, 4.0)`. Write a SELECT before and after to show the changes.

---

## Part 2: Basic DELETE

### Task A: Preview before deleting

Write a SELECT query that finds all enrollments with a grade of 'F'. Then write the DELETE statement that would remove those enrollments. Run the SELECT again to confirm they are gone.

### Task B: Delete with a condition

Write a DELETE statement that removes all enrollments from a specific semester (choose one from your data). Show a SELECT before and after.

### Task C: What happens without WHERE?

In your output file, write the following statement and explain what it would do. **Do not run it.**

```sql
DELETE FROM students;
```

Explain what would happen to the enrollments table if students were deleted (consider that enrollments references student_id). Would SQLite prevent this? Under what circumstances?

---

## Part 3: UPDATE and DELETE with Subqueries

### Task A: Update grades using a subquery

Write an UPDATE statement that sets the grade to 'A+' for all enrollments belonging to students whose GPA is 3.9 or above. Use a subquery in the WHERE clause. Show a SELECT before and after.

### Task B: Delete enrollments for a department

Write a DELETE statement that removes all enrollments in courses from a specific department (e.g., 'English'). You will need a subquery that selects course IDs from the courses table. Show a SELECT before and after.

### Task C: Update using data from another table

Write an UPDATE statement that changes each student's major to 'Undeclared' if they have no enrollments at all. Use a subquery with `NOT IN` or `NOT EXISTS`. Show a SELECT before and after.

---

## Part 4: Transactions

### Task A: Successful transaction

Write a transaction that performs the following two operations:
1. Insert a new student (choose realistic values).
2. Insert an enrollment for that new student.

Use `BEGIN TRANSACTION;` and `COMMIT;`. After committing, write a SELECT query joining students and enrollments to confirm both records exist.

### Task B: Rolled-back transaction

Write a transaction that:
1. Deletes all enrollments for a specific student.
2. Deletes that student from the students table.

After the DELETE statements but before COMMIT, write a ROLLBACK instead. Then write SELECT queries to confirm both the student and their enrollments still exist.

### Task C: Why transactions matter

In your output file, describe a real-world scenario (2-3 sentences) where a transaction is essential. For example, consider a bank transfer, an online order, or a course registration system. Explain what could go wrong without a transaction.

---

## Submission

Save a file named `Day_09_Output.md` in this folder containing the SQL queries and their output.

## Grading Criteria

| Criteria | Points |
|----------|--------|
| Part 1: Basic UPDATE with CASE (Tasks A-C) | 25 |
| Part 2: Basic DELETE and safety awareness (Tasks A-C) | 25 |
| Part 3: Subqueries in UPDATE/DELETE (Tasks A-C) | 25 |
| Part 4: Transactions (Tasks A-C) | 25 |
| **Total** | **100** |
