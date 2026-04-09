# Day 1 Assignment: What Is SQL

## Overview

- **Topic:** Introduction to SQL and Relational Databases
- **Type:** Technical / Hands-On
- **Estimated Time:** 30 minutes

## Background

### Relational Database Management Systems (RDBMS)

A **relational database** stores data in **tables** (also called relations). Each table is made up of:

- **Columns** (fields) — define the type of data stored (e.g., name, age, email)
- **Rows** (records) — each row is one entry in the table

Think of a table like a spreadsheet: columns are the headers, rows are the data underneath.

An **RDBMS** is the software that manages these tables and the relationships between them. Examples include SQLite, MySQL, PostgreSQL, Microsoft SQL Server, and Oracle.

### SQL as a Language

**SQL** (Structured Query Language) is the standard language for interacting with relational databases. SQL commands fall into three main categories:

| Category | Full Name | Purpose | Example Commands |
|----------|-----------|---------|-----------------|
| **DDL** | Data Definition Language | Define and modify database structure | `CREATE TABLE`, `ALTER TABLE`, `DROP TABLE` |
| **DML** | Data Manipulation Language | Insert, update, and delete data | `INSERT`, `UPDATE`, `DELETE` |
| **DQL** | Data Query Language | Retrieve data | `SELECT` |

### SQLite vs MySQL vs PostgreSQL

| Feature | SQLite | MySQL | PostgreSQL |
|---------|--------|-------|------------|
| Setup | No server needed — single file | Requires server installation | Requires server installation |
| Use case | Embedded apps, learning, prototyping | Web applications | Complex enterprise applications |
| Concurrency | Limited (file-level locking) | Good | Excellent |
| Data types | Flexible (type affinity) | Strict | Strict |

We use **SQLite** because it requires zero configuration. The entire database lives in a single file, and you interact with it through the `sqlite3` command-line tool.

### Basic SQLite Shell Commands

These are **dot-commands** (they start with `.`) and are specific to the SQLite shell — they are not SQL:

```
.help        -- Show all available dot-commands
.tables      -- List all tables in the database
.schema      -- Show the CREATE TABLE statements for all tables
.headers on  -- Display column headers in query output
.mode column -- Format output in aligned columns
.quit        -- Exit the SQLite shell
```

### Basic SQL Examples

Creating a table:

```sql
CREATE TABLE pets (
    id INTEGER PRIMARY KEY,
    name TEXT,
    species TEXT
);
```

Inserting data:

```sql
INSERT INTO pets (name, species) VALUES ('Buddy', 'Dog');
```

Querying data:

```sql
SELECT * FROM pets;
```

---

## Part 1: Install SQLite and Create a Database

### Task A: Verify SQLite is installed

Open a terminal and run:

```bash
sqlite3 --version
```

Record the version number in your output file. If `sqlite3` is not installed, install it:

- **Ubuntu/Debian:** `sudo apt install sqlite3`
- **macOS:** Already installed (or `brew install sqlite3`)
- **Arch Linux:** `sudo pacman -S sqlite`

### Task B: Create a new database

Create a new SQLite database called `day01.db`:

```bash
sqlite3 day01.db
```

This opens the SQLite shell and creates the file if it does not exist. You should see a prompt like `sqlite>`.

### Task C: Explore dot-commands

Run each of the following dot-commands inside the SQLite shell and record the output:

1. `.help` — Skim through the list. You do not need to record all of it, just note 3 commands you find interesting.
2. `.tables` — This should show nothing yet (no tables exist).
3. `.quit` — Exit the shell, then reopen it with `sqlite3 day01.db` to confirm the file persists.

---

## Part 2: Create Your First Table

### Task A: Create a table called `employees`

Enter the following SQL in the SQLite shell:

```sql
CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    department TEXT,
    salary REAL
);
```

### Task B: Verify the table exists

Run the following commands and record the output:

```
.tables
.schema employees
```

---

## Part 3: Insert and Query Data

### Task A: Insert rows into `employees`

Run each INSERT statement one at a time:

```sql
INSERT INTO employees (first_name, last_name, department, salary) VALUES ('Alice', 'Johnson', 'Engineering', 85000.00);
INSERT INTO employees (first_name, last_name, department, salary) VALUES ('Bob', 'Smith', 'Marketing', 62000.00);
INSERT INTO employees (first_name, last_name, department, salary) VALUES ('Carol', 'Williams', 'Engineering', 91000.00);
INSERT INTO employees (first_name, last_name, department, salary) VALUES ('David', 'Brown', 'Sales', 57000.00);
INSERT INTO employees (first_name, last_name, department, salary) VALUES ('Eve', 'Davis', 'Marketing', 68000.00);
```

### Task B: Query all rows

First, turn on readable output formatting:

```sql
.headers on
.mode column
```

Then run:

```sql
SELECT * FROM employees;
```

Record the full output.

### Task C: Query specific columns

Run the following query and record the output:

```sql
SELECT first_name, department FROM employees;
```

### Task D: Count the rows

Run the following query and record the output:

```sql
SELECT COUNT(*) FROM employees;
```

---

## Part 4: Experiment

### Task A: Create a second table

Create a table called `departments` with the following columns:

| Column | Type | Notes |
|--------|------|-------|
| id | INTEGER | Primary key |
| name | TEXT | Department name |
| building | TEXT | Building location |

Write the `CREATE TABLE` statement yourself (do not copy one from above — adapt the pattern).

### Task B: Insert 3 rows into `departments`

Write three `INSERT` statements to add rows for Engineering, Marketing, and Sales. Choose any building names you like.

### Task C: Verify both tables

Run `.tables` to confirm both `employees` and `departments` appear. Run `SELECT * FROM departments;` and record the output.

---

## Submission

Save a file named `Day_01_Output.md` in this folder containing the SQL queries and their output.

## Grading Criteria

| Criteria | Points |
|----------|--------|
| SQLite version recorded | 5 |
| Dot-commands explored and output recorded (.help, .tables, .quit) | 10 |
| `employees` table created with correct schema | 15 |
| `.tables` and `.schema` output recorded | 10 |
| All 5 employee rows inserted successfully | 15 |
| `SELECT *` output recorded with headers and column formatting | 10 |
| `SELECT first_name, department` output recorded | 5 |
| `COUNT(*)` output recorded | 5 |
| `departments` table created with correct schema | 10 |
| 3 rows inserted into `departments` and output recorded | 10 |
| Output file is clearly organized with queries and results | 5 |
| **Total** | **100** |
