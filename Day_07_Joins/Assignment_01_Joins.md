# Day 7 Assignment: Joins

## Overview

- **Topic:** INNER JOIN, LEFT JOIN, RIGHT JOIN, CROSS JOIN, Self-Joins, Multi-Table Joins, Table Aliases
- **Type:** Technical / Hands-On
- **Estimated Time:** 30 minutes

## Background

Joins combine rows from two or more tables based on a related column. They are the primary mechanism for querying data spread across multiple tables in a relational database.

### Table Aliases

Aliases give tables short names to make queries more readable, especially with joins.

```sql
SELECT s.name, c.name
FROM students AS s
JOIN courses AS c ON ...;
```

You can also omit the `AS` keyword:

```sql
SELECT s.name, c.name
FROM students s
JOIN courses c ON ...;
```

### INNER JOIN

Returns only rows where there is a match in both tables.

```sql
SELECT s.name, e.grade
FROM students s
INNER JOIN enrollments e ON s.id = e.student_id;
```

Only students who have at least one enrollment will appear in the results.

### LEFT JOIN

Returns all rows from the left table, and matching rows from the right table. If there is no match, the right side columns are `NULL`.

```sql
SELECT s.name, e.grade
FROM students s
LEFT JOIN enrollments e ON s.id = e.student_id;
```

All students appear, even those with no enrollments (their grade will be `NULL`).

### RIGHT JOIN and FULL OUTER JOIN

**Important:** SQLite does not support `RIGHT JOIN` or `FULL OUTER JOIN`. However, you should understand them conceptually:

- **RIGHT JOIN:** Returns all rows from the right table, and matching rows from the left. The reverse of LEFT JOIN. In SQLite, you can achieve the same result by swapping the table order and using LEFT JOIN.
- **FULL OUTER JOIN:** Returns all rows from both tables, with NULLs where there is no match on either side.

```sql
-- RIGHT JOIN equivalent in SQLite: swap the tables and use LEFT JOIN
-- Instead of: students RIGHT JOIN enrollments
-- Use:        enrollments LEFT JOIN students
SELECT s.name, e.grade
FROM enrollments e
LEFT JOIN students s ON s.id = e.student_id;
```

### CROSS JOIN

Returns the Cartesian product: every row from the first table paired with every row from the second table. Rarely used, but good to understand.

```sql
SELECT s.name, c.name
FROM students s
CROSS JOIN courses c;
```

If students has 10 rows and courses has 5 rows, this returns 50 rows.

### Self-Join

A table joined to itself. Useful for comparing rows within the same table.

```sql
-- Find pairs of students in the same major
SELECT a.name, b.name, a.major
FROM students a
JOIN students b ON a.major = b.major AND a.id < b.id;
```

### Joining Multiple Tables

You can chain joins to connect three or more tables.

```sql
SELECT s.name, c.name, e.grade
FROM students s
JOIN enrollments e ON s.id = e.student_id
JOIN courses c ON c.id = e.course_id;
```

---

## Part 1: INNER JOIN Basics

### Task A: Student enrollments

Write a query using INNER JOIN to display each student's name alongside their grade and semester from the enrollments table. Use table aliases.

### Task B: Course enrollments

Write a query using INNER JOIN to display each course name alongside the student_id and grade for that course.

### Task C: Full enrollment details

Write a query that joins all three tables (students, enrollments, courses) to display: student name, course name, grade, and semester. Order the results by student name, then by course name.

---

## Part 2: LEFT JOIN

### Task A: All students with enrollments

Write a query using LEFT JOIN to show all students and their enrollment information. Students with no enrollments should still appear with NULL values for the enrollment columns.

### Task B: Students not enrolled in any course

Write a query using LEFT JOIN and `IS NULL` to find students who are not enrolled in any course. Display only the student's name and email.

### Task C: All courses with enrollment counts

Write a query using LEFT JOIN to show every course name and the number of students enrolled in it. Courses with zero enrollments should show a count of 0. Alias the count as `enrollment_count`. Order by `enrollment_count` descending.

---

## Part 3: CROSS JOIN and Self-Join

### Task A: Cartesian product

Write a CROSS JOIN between students and courses. Limit the output to the first 10 rows. Display student name and course name.

### Task B: Same-major pairs

Write a self-join query that finds all pairs of students who share the same major. Ensure each pair appears only once (use `a.id < b.id` to avoid duplicates and self-pairs). Display both student names and the shared major.

---

## Part 4: Complex Join Queries

### Task A: A students

Write a query that finds all students who received a grade of 'A' in any course. Display the student name, course name, and grade. Use joins across all three tables.

### Task B: Students with multiple enrollments

Write a query that finds students who are enrolled in more than one course. Display the student name and the number of courses they are enrolled in, aliased as `course_count`. Use a JOIN with GROUP BY and HAVING.

### Task C: Department enrollment summary

Write a query that shows each department and the total number of student enrollments in courses from that department. Join courses to enrollments and group by department. Display department and `total_enrollments`. Order by `total_enrollments` descending.

### Task D: RIGHT JOIN simulation

Write a query that achieves the effect of a RIGHT JOIN between students and enrollments. Do this by swapping the table order and using a LEFT JOIN. The result should show all enrollments, including any that might not match a student. Add a comment in your SQL explaining why you swapped the tables.

### Task E: Average grade by course

Write a query that joins enrollments and courses, and for each course name, shows the number of enrollments and lists all distinct grades received. Use `GROUP_CONCAT(DISTINCT e.grade)` to list the grades. Order by course name.

---

## Submission

Save a file named `Day_07_Output.md` in this folder containing the SQL queries and their output.

## Grading Criteria

| Criteria | Points |
|----------|--------|
| Part 1: INNER JOIN basics (Tasks A-C) | 25 |
| Part 2: LEFT JOIN queries (Tasks A-C) | 25 |
| Part 3: CROSS JOIN and Self-Join (Tasks A-B) | 20 |
| Part 4: Complex join queries (Tasks A-E) | 30 |
| **Total** | **100** |
