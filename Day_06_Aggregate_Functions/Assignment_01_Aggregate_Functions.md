# Day 6 Assignment: Aggregate Functions

## Overview

- **Topic:** COUNT, SUM, AVG, MIN, MAX, GROUP BY, HAVING
- **Type:** Technical / Hands-On
- **Estimated Time:** 30 minutes

## Background

Aggregate functions perform calculations across multiple rows and return a single result. They are essential for summarizing and analyzing data.

### Core Aggregate Functions

```sql
-- COUNT: number of rows
SELECT COUNT(*) FROM students;

-- SUM: total of a numeric column
SELECT SUM(credits) FROM courses;

-- AVG: average of a numeric column
SELECT AVG(gpa) FROM students;

-- MIN / MAX: smallest / largest value
SELECT MIN(age), MAX(age) FROM students;
```

### GROUP BY

`GROUP BY` splits rows into groups and applies the aggregate function to each group separately.

```sql
SELECT major, COUNT(*) AS student_count
FROM students
GROUP BY major;
```

### HAVING

`HAVING` filters groups after aggregation. This is different from `WHERE`, which filters individual rows before aggregation.

```sql
-- WHERE filters rows BEFORE grouping
SELECT major, AVG(gpa) AS avg_gpa
FROM students
WHERE age > 20
GROUP BY major;

-- HAVING filters groups AFTER grouping
SELECT major, AVG(gpa) AS avg_gpa
FROM students
GROUP BY major
HAVING AVG(gpa) > 3.0;
```

### GROUP BY with Multiple Columns

You can group by more than one column to create finer-grained groups.

```sql
SELECT department, credits, COUNT(*) AS course_count
FROM courses
GROUP BY department, credits;
```

### Key Distinction: WHERE vs HAVING

| Feature | WHERE | HAVING |
|---------|-------|--------|
| Filters | Individual rows | Groups |
| Runs | Before GROUP BY | After GROUP BY |
| Can use aggregates? | No | Yes |

```sql
-- This FAILS: cannot use aggregate in WHERE
SELECT major, AVG(gpa)
FROM students
WHERE AVG(gpa) > 3.0   -- ERROR
GROUP BY major;

-- This WORKS: use HAVING for aggregate conditions
SELECT major, AVG(gpa)
FROM students
GROUP BY major
HAVING AVG(gpa) > 3.0;
```

---

## Part 1: Basic Aggregate Functions

### Task A: Count all students

Write a query that returns the total number of students in the `students` table. Alias the result as `total_students`.

### Task B: GPA statistics

Write a single query that returns the minimum GPA, maximum GPA, and average GPA across all students. Alias the columns as `min_gpa`, `max_gpa`, and `avg_gpa`. Round the average to two decimal places using `ROUND()`.

### Task C: Total credits

Write a query that returns the total number of credits across all courses. Alias the result as `total_credits`.

---

## Part 2: GROUP BY

### Task A: Students per major

Write a query that counts the number of students in each major. Display the major and the count, aliased as `student_count`. Order the results by `student_count` in descending order.

### Task B: Average GPA by major

Write a query that calculates the average GPA for each major. Display the major and the average GPA rounded to two decimal places, aliased as `avg_gpa`. Order by `avg_gpa` descending.

### Task C: Department with most courses

Write a query that counts the number of courses in each department. Display the department and the count, aliased as `course_count`. Order by `course_count` descending and use `LIMIT 1` to show only the department with the most courses.

### Task D: Enrollment count by semester

Write a query that counts the number of enrollments in each semester. Display the semester and the count, aliased as `enrollment_count`. Order by semester.

---

## Part 3: HAVING

### Task A: Popular majors

Write a query that shows only majors that have more than 2 students. Display the major and the student count.

### Task B: High-performing majors

Write a query that shows majors where the average GPA is above 3.0. Display the major and the average GPA rounded to two decimal places.

### Task C: Busy semesters

Write a query that shows only semesters that have more than 5 enrollments. Display the semester and the enrollment count.

---

## Part 4: GROUP BY with Multiple Columns

### Task A: Grade distribution by semester

Write a query that counts the number of each grade (A, B, C, etc.) per semester. Display the semester, grade, and count. Order by semester and then by grade.

### Task B: Combining WHERE, GROUP BY, and HAVING

Write a query that finds majors where the average GPA of students aged 21 or older is above 3.2. Use `WHERE` to filter by age, `GROUP BY` to group by major, and `HAVING` to filter by average GPA. Display the major, average GPA (rounded to two decimal places), and the count of qualifying students.

### Task C: Explain the difference

In your output file, write a brief explanation (2-3 sentences) of why the following query is invalid, and then write the corrected version:

```sql
SELECT major, COUNT(*)
FROM students
WHERE COUNT(*) > 2
GROUP BY major;
```

---

## Submission

Save a file named `Day_06_Output.md` in this folder containing the SQL queries and their output.

## Grading Criteria

| Criteria | Points |
|----------|--------|
| Part 1: Basic aggregate functions (Tasks A-C) | 20 |
| Part 2: GROUP BY queries (Tasks A-D) | 30 |
| Part 3: HAVING queries (Tasks A-C) | 25 |
| Part 4: Multiple columns and combined clauses (Tasks A-C) | 25 |
| **Total** | **100** |
