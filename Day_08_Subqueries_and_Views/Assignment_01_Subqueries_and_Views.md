# Day 8 Assignment: Subqueries and Views

## Overview

- **Topic:** Subqueries (WHERE, FROM, correlated), EXISTS, CREATE VIEW, DROP VIEW
- **Type:** Technical / Hands-On
- **Estimated Time:** 30 minutes

## Background

A subquery is a query nested inside another query. Subqueries let you build complex logic step by step. Views are saved queries that act like virtual tables.

### Scalar Subqueries in WHERE

A scalar subquery returns a single value and can be used with comparison operators.

```sql
-- Find students with above-average GPA
SELECT name, gpa
FROM students
WHERE gpa > (SELECT AVG(gpa) FROM students);
```

### List Subqueries with IN

A subquery that returns a list of values can be used with `IN`.

```sql
-- Find students enrolled in course 1
SELECT name
FROM students
WHERE id IN (SELECT student_id FROM enrollments WHERE course_id = 1);
```

### EXISTS

`EXISTS` checks whether a subquery returns any rows at all. It returns true or false.

```sql
-- Find students who have at least one enrollment
SELECT name
FROM students s
WHERE EXISTS (SELECT 1 FROM enrollments e WHERE e.student_id = s.id);
```

### Subqueries in FROM (Derived Tables)

A subquery in the `FROM` clause creates a temporary table you can query against.

```sql
-- Get the major with the highest average GPA
SELECT major, avg_gpa
FROM (
    SELECT major, ROUND(AVG(gpa), 2) AS avg_gpa
    FROM students
    GROUP BY major
) AS major_stats
ORDER BY avg_gpa DESC
LIMIT 1;
```

### Correlated Subqueries

A correlated subquery references a column from the outer query. It runs once for each row of the outer query.

```sql
-- Find students whose GPA is above the average for their major
SELECT name, major, gpa
FROM students s1
WHERE gpa > (
    SELECT AVG(gpa)
    FROM students s2
    WHERE s2.major = s1.major
);
```

### Views

A view is a stored query. It does not store data itself; it runs the query each time you access it.

```sql
-- Create a view
CREATE VIEW enrollment_details AS
SELECT s.name AS student_name, c.name AS course_name, e.grade, e.semester
FROM students s
JOIN enrollments e ON s.id = e.student_id
JOIN courses c ON c.id = e.course_id;

-- Query the view like a table
SELECT * FROM enrollment_details WHERE grade = 'A';

-- Remove a view
DROP VIEW enrollment_details;

-- Use IF EXISTS to avoid errors
DROP VIEW IF EXISTS enrollment_details;
```

---

## Part 1: Scalar Subqueries

### Task A: Above-average GPA

Write a query that finds all students whose GPA is above the overall average GPA. Display the student's name, major, and GPA. Order by GPA descending.

### Task B: Youngest student(s)

Write a query that finds the student(s) with the minimum age. Use a subquery to determine the minimum age. Display name, age, and major.

### Task C: Courses with more credits than average

Write a query that finds all courses whose credit count is above the average number of credits across all courses. Display the course name, department, and credits.

---

## Part 2: List Subqueries and EXISTS

### Task A: Enrolled students (using IN)

Write a query using `IN` with a subquery to find all students who are enrolled in at least one course. Display name and email.

### Task B: Unenrolled students (using NOT IN)

Write a query using `NOT IN` with a subquery to find all students who are not enrolled in any course. Display name and email.

### Task C: Courses with no enrollments (using NOT EXISTS)

Write a query using `NOT EXISTS` to find courses that have no enrollments. Display the course name and department.

### Task D: Students with an A grade (using EXISTS)

Write a query using `EXISTS` to find students who received at least one 'A' grade. Display the student's name and major.

---

## Part 3: Derived Tables and Correlated Subqueries

### Task A: Major statistics

Write a query using a subquery in the `FROM` clause (derived table) that shows each major, the number of students, and the average GPA. Then filter the results in the outer query to show only majors with an average GPA above 3.0.

### Task B: Highest GPA per major

Write a correlated subquery that finds the student with the highest GPA in each major. Display the student's name, major, and GPA. If two students tie, both should appear.

### Task C: Students enrolled in more courses than average

Write a query that finds students whose number of enrollments is greater than the average number of enrollments per student. Use a derived table or subquery to calculate the average enrollment count, then compare each student's count against it. Display the student name and their enrollment count.

---

## Part 4: Views

### Task A: Create enrollment_details view

Create a view called `enrollment_details` that joins all three tables and includes: student name (as `student_name`), student email, course name (as `course_name`), department, grade, and semester. Then write a query that selects all rows from the view where the grade is 'A'.

### Task B: Create student_summary view

Create a view called `student_summary` that shows each student's name, major, GPA, and total number of courses they are enrolled in (aliased as `course_count`). Use a LEFT JOIN so students with no enrollments show a count of 0. Then query the view to find students enrolled in more than 2 courses.

### Task C: Drop and recreate

Write statements to drop both views using `DROP VIEW IF EXISTS`, then recreate them. In your output, confirm that querying each recreated view returns results.

---

## Submission

Save a file named `Day_08_Output.md` in this folder containing the SQL queries and their output.

## Grading Criteria

| Criteria | Points |
|----------|--------|
| Part 1: Scalar subqueries (Tasks A-C) | 20 |
| Part 2: List subqueries and EXISTS (Tasks A-D) | 25 |
| Part 3: Derived tables and correlated subqueries (Tasks A-C) | 25 |
| Part 4: Views (Tasks A-C) | 30 |
| **Total** | **100** |
