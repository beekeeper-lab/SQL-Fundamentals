# SQL Fundamentals

A 10-day SQL course covering relational database fundamentals from table creation through indexing and best practices.

## Course Details

- **10 days** of content with source markdown, assignments, and quizzes
- Source files: `source/module-01-what-is-sql.md` through `source/module-10-indexes-and-best-practices.md`
- Day folders: `Day_01_What_Is_SQL/` through `Day_10_Indexes_and_Best_Practices/`

## Build Pipeline

See `COURSE-BUILDER-GUIDE.md` for the full build pipeline documentation.

```bash
uv run --with markdown --with pygments python scripts/build_course.py
uv run --with elevenlabs python scripts/generate_narration.py
uv run --with markdown --with pygments python scripts/deploy.py --version 1.0
```

## Quizzes

10 quizzes in `Quiz/Day_01_Quiz_File/` through `Quiz/Day_10_Quiz_File/`. Run from the parent directory:

```bash
python ../quiz_app.py SQL_Fundamentals <day>
```

Results tracked in `Gradebook.md`.

## Content Scope

Days 1-10 cover: what is SQL, creating tables, inserting data, SELECT/filtering, sorting/limiting, aggregate functions, joins, subqueries/views, updating/deleting, and indexes/best practices.
