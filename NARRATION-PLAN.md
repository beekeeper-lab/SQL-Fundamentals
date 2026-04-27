# SQL Fundamentals — Narration Plan

This plan enumerates every `> 🎙️` narration block in `source/`,
organized by source module → block index (1-based, in source order)→
full text → character count → ElevenLabs credit estimate
(`eleven_multilingual_v2`: 1 character = 1 credit).

Already-generated blocks are marked **DONE** based on the presence of the
matching `audio/<source-stem>/NN_<source-stem>.mp3` file. Missing blocks
are marked **MISSING** — they are the focus of any next narration run.

> Voice: ElevenLabs Rachel (course default). Run `uv run --with elevenlabs python scripts/generate_narration.py` to fill in the MISSING blocks below — the script numbers blocks by position and skips ones whose MP3 already exists.

## Totals

- **Modules with narration:** 10
- **Total narration blocks:** 126
- **Total characters:** 44,008
- **Generated (DONE):** 107 blocks, 37,374 chars
- **Outstanding (MISSING):** 19 blocks, 6,634 chars
- **Estimated ElevenLabs credits to finish:** ~6,634 (multilingual_v2, 1 char = 1 credit)

---

## `module-00-what-is-sql.md`

- Blocks: **12** | Chars: **4,252** | DONE: **9** | MISSING: **3** (955 chars)

### Block 1 — DONE

_408 chars · ~408 credits_

> Welcome to Module 0 -- the very beginning. If you've never touched a database before, perfect. If you've used spreadsheets, even better -- because you already understand more than you think. We're about to learn how to talk to databases using a language called SQL, and by the end of this module, you'll have created your first database, built a table, stuffed data into it, and asked it questions. Let's go.

### Block 2 — DONE

_323 chars · ~323 credits_

> Think of it this way. You wouldn't just dump a thousand paper records into a cardboard box and call it "organized." You'd file them into labeled folders, in labeled drawers, in a cabinet. A relational database does the same thing -- but digitally, and with the ability to search through millions of records in milliseconds.

### Block 3 — DONE

_432 chars · ~432 credits_

> Here's the mental model I want you to hold onto. A table is a grid. Columns describe the shape of your data -- what goes where and what type it is. Rows are the actual records -- one person, one order, one transaction per row. That's it. Everything fancy we'll do in SQL -- constraints, joins, aggregates -- all of it still comes back to this one idea. Rows and columns. You already read spreadsheets every day. You can read tables.

### Block 4 — DONE

_285 chars · ~285 credits_

> Here's a way to remember the three categories. DDL is the architect -- it designs the building. DML is the moving crew -- it puts stuff in, rearranges it, and takes stuff out. DQL is the detective -- it asks questions and finds answers. Architect, movers, detective. That's all of SQL.

### Block 5 — DONE

_338 chars · ~338 credits_

> Real talk -- the SQL you learn with SQLite works in MySQL, PostgreSQL, and everywhere else. The language is the same. So we're using the simplest tool to learn the universal skill. Once you know SQL, switching databases later is like switching from driving an automatic to a manual -- same road, same rules, just a few different controls.

### Block 6 — DONE

_308 chars · ~308 credits_

> Here's a common gotcha. You type a query, hit Enter, and... nothing happens. Just a weird `...>` prompt staring at you. Don't panic. You just forgot the semicolon at the end. Type a semicolon, hit Enter, and your query will run. Every single person learning SQL hits this at least once. Now you know the fix.

### Block 7 — DONE

_431 chars · ~431 credits_

> These are the questions every beginner has, and none of them are dumb. The math question is the big one -- people assume databases are a numerical thing, but they're really a logic and organization thing. The SQL-versus-SQLite question is another one that trips everyone up at first. SQL is the language. SQLite is one tool that speaks it. Keep that distinction straight and you'll never be confused by job postings that list both.

### Block 8 — DONE

_327 chars · ~327 credits_

> Take a moment here. You just went from an empty terminal to a fully functioning database with five employee records. That first SELECT query -- where data you typed actually comes back in a nice organized table -- that's the moment it clicks for most people. You told the database what you wanted, and it delivered. That's SQL.

### Block 9 — DONE

_445 chars · ~445 credits_

> SELECT star is the firehose -- it dumps every column at you. Most of the time, you don't want the firehose. You want a sip. Naming specific columns is a tiny habit that pays off constantly. And COUNT is your first taste of what SQL is really for -- turning a pile of records into an answer. We'll do a lot more of that in later modules. For now, just get comfortable asking the database small, specific questions instead of "show me everything."

### Block 10 — **MISSING**

_262 chars · ~262 credits_

> Exercise 6 is the important one. Anyone can copy and paste a CREATE TABLE statement. Writing one from scratch -- adapting a pattern you've seen to a new situation -- that's where learning happens. Take your time with it. Get it wrong. Fix it. That's the process.

### Block 11 — **MISSING**

_425 chars · ~425 credits_

> Here's your recap. You learned what databases are -- organized collections of tables. You learned what SQL is -- the language databases speak. You installed SQLite, created a database file, built a table, loaded data into it, and asked questions about that data. And you built a second table on your own. That's a real foundation. In the next module, we'll learn how to design better tables with rules that keep bad data out.

### Block 12 — **MISSING**

_268 chars · ~268 credits_

> That wraps up Module 0. You've got a database, you've got data in it, and you've got the basics down. Next up, we're going to learn how to build tables that are much smarter -- tables with rules, constraints, and guardrails that keep bad data out. See you in Module 1.

---

## `module-01-creating-tables.md`

- Blocks: **10** | Chars: **3,647** | DONE: **8** | MISSING: **2** (730 chars)

### Block 1 — DONE

_450 chars · ~450 credits_

> In Module 0, you built your first tables. They worked, but they were a little... naive. You could shove any data into any column. No rules, no guardrails. That's like building a house without a building code -- sure, it stands up, but the first strong wind is going to cause problems. In this module, we're going to learn how to design tables with data types, constraints, and relationships. These are the blueprints and building codes for your data.

### Block 2 — DONE

_402 chars · ~402 credits_

> Here's a quirk about SQLite that confuses people coming from other databases. SQLite uses something called "type affinity" -- it's flexible about types. If you declare a column as INTEGER but insert the text "hello," SQLite won't stop you. Other databases would throw an error. This is why constraints -- which we'll cover next -- are extra important in SQLite. They're your real enforcement mechanism.

### Block 3 — DONE

_385 chars · ~385 credits_

> Here's the mindset shift. Without constraints, YOU are responsible for making sure every piece of data is valid -- every time, forever. With constraints, the DATABASE is responsible. It never gets tired, it never forgets to check, and it never lets bad data slip through because it's Friday afternoon and everyone wants to go home. Constraints are your safety net. Use them generously.

### Block 4 — DONE

_426 chars · ~426 credits_

> Look at that students table for a second. Six lines of SQL, and each line is doing real work. One line guarantees uniqueness. One line guarantees a valid GPA range. One line fills in today's date automatically. When you see a well-designed CREATE TABLE statement, it reads like a specification document -- except the database actually enforces every rule. That's the goal. Make your tables self-documenting and self-defending.

### Block 5 — DONE

_311 chars · ~311 credits_

> Foreign keys are where the magic of relational databases really shows up. Without them, you could enroll a student who doesn't exist in a course that doesn't exist. With them, the database guarantees that every reference points to something real. It's like a hyperlink that's guaranteed to never be a 404 error.

### Block 6 — DONE

_248 chars · ~248 credits_

> DROP TABLE is the delete key for tables. Use it freely during learning -- you can always recreate the table. But in a production database with real data? Treat it like a loaded weapon. The IF EXISTS clause is your safety catch -- always include it.

### Block 7 — DONE

_375 chars · ~375 credits_

> The primary-key-versus-unique question comes up in every cohort. Here's the shorthand. Primary key is the row's official name -- the one the database uses to find it quickly. Unique is just a promise that no two rows share a value. One table, one primary key. But you can have many unique columns. Use primary key for identity, unique for anything else that shouldn't repeat.

### Block 8 — DONE

_320 chars · ~320 credits_

> Exercise 4 is the most important one here. The enrollments table has a composite primary key AND foreign keys -- that's real-world table design. If you can build that table and understand why each constraint is there, you've leveled up significantly from Module 0. Take your time and make sure you understand every line.

### Block 9 — **MISSING**

_428 chars · ~428 credits_

> Let's recap. You started this module knowing how to create basic tables. Now you know how to create tables with real rules -- types that describe the data, constraints that enforce quality, and foreign keys that connect tables together. Your tables went from empty spreadsheets to self-defending data structures. In the next module, you'll learn how to fill these tables with data -- and what happens when data breaks the rules.

### Block 10 — **MISSING**

_302 chars · ~302 credits_

> That's Module 1 in the books. You know data types, constraints, composite keys, foreign keys, ALTER TABLE, and DROP TABLE. That's a serious toolkit. Next up, we're going to fill these tables with data using INSERT -- single rows, multiple rows, and what to do when things go wrong. See you in Module 2.

---

## `module-02-inserting-data.md`

- Blocks: **11** | Chars: **4,255** | DONE: **9** | MISSING: **2** (731 chars)

### Block 1 — DONE

_406 chars · ~406 credits_

> You've got tables. Beautiful, well-designed tables with constraints and foreign keys and everything. But they're empty. A database without data is like a restaurant without food -- technically functional, but kind of missing the point. In this module, we're going to learn INSERT -- all the ways to get data into your tables, what happens when data breaks the rules, and how to handle conflicts gracefully.

### Block 2 — DONE

_360 chars · ~360 credits_

> Here's the number one best practice for INSERT statements, and I want you to tattoo it on your brain: always specify the column list. Yes, you CAN skip it and just provide values in order. But don't. Specifying columns makes your intent clear, protects you when the table changes, and makes your code readable six months from now. Always. Specify. The columns.

### Block 3 — DONE

_422 chars · ~422 credits_

> I keep coming back to this one because it matters. The shortcut saves you maybe a dozen keystrokes. But the day someone adds a new column to the table and pushes it to production, every short-form INSERT in your codebase starts failing -- or worse, silently puts data in the wrong column. That's the kind of bug that makes you look bad on a Monday morning. Write the column list. Always. Future you will thank present you.

### Block 4 — DONE

_339 chars · ~339 credits_

> Multi-row INSERT is one of those things that seems like a small convenience but matters a lot in practice. When you're populating a table with test data or loading initial records, one multi-row INSERT is cleaner to read, easier to edit, and faster for the database to process. Get comfortable with this syntax -- you'll use it constantly.

### Block 5 — DONE

_379 chars · ~379 credits_

> Here's the way to think about NULL. If I ask you "Is an unknown number equal to another unknown number?" -- you can't say yes. They MIGHT be equal, but you don't KNOW. That's why NULL equals NULL isn't true -- it's unknown. This seems philosophical, but it causes real bugs in real applications. When you see NULL, think "unknown," and remember to use IS NULL, never equals NULL.

### Block 6 — DONE

_443 chars · ~443 credits_

> This is a subtle but important distinction. If you want the default value, leave the column OUT of your column list entirely. If you include it and pass NULL, you're telling the database "I specifically want nothing here." The database respects your explicit instruction over the default. It's like a form that pre-fills your country -- if you erase it and submit blank, the system doesn't put the default back. You said blank, so blank it is.

### Block 7 — DONE

_443 chars · ~443 credits_

> Here's my rule of thumb for conflict handling. If you're loading data and want to keep what you already have, use INSERT OR IGNORE. If you're loading data and want the newest version to win, use INSERT OR REPLACE -- but be careful, because it's a delete-then-insert, not an update. For most day-to-day work, the default error behavior is what you want -- it forces you to deal with the problem explicitly rather than sweeping it under the rug.

### Block 8 — DONE

_377 chars · ~377 credits_

> That O'Brien question is a classic, and the double-quote trick surprises people every time. Two single quotes in a row -- that's how SQL escapes a quote inside a string. It looks weird, but it's the standard. The other two gotchas in this section are order-of-insertion for foreign keys, and letting AUTOINCREMENT do its job. Keep those in mind and your inserts will just work.

### Block 9 — DONE

_355 chars · ~355 credits_

> Pay special attention to Exercise 6. The INSERT OR REPLACE test is the one that surprises people -- when you replace Alice, her ID changes. That's because REPLACE deletes the old row and inserts a brand new one. If other tables had foreign keys pointing to Alice's old ID, those references would break. That's a real-world consequence worth understanding.

### Block 10 — **MISSING**

_504 chars · ~504 credits_

> Here's your Module 2 recap. You learned INSERT in all its forms -- single row, multi-row, with and without explicit columns. You learned that NULL is its own special kind of nothing. You learned how DEFAULT values work, and you learned three strategies for handling conflicts. Most importantly, you populated a complete university database with real data across three interconnected tables. In the next module, we'll finally learn SELECT in depth -- the most powerful and most-used command in all of SQL.

### Block 11 — **MISSING**

_227 chars · ~227 credits_

> That wraps up Module 2. You know how to get data in. Next up, you learn how to get data out -- selectively, precisely, and powerfully. SELECT is the star of the SQL show, and Module 3 is where it takes the stage. See you there.

---

## `module-03-select-and-filtering.md`

- Blocks: **14** | Chars: **4,274** | DONE: **14** | MISSING: **0** (0 chars)

### Block 1 — DONE

_382 chars · ~382 credits_

> Welcome to Module 3. This is where SQL stops being a toy and starts being a tool. Up until now, you've been looking at tables and understanding structure. Now? Now you're going to learn how to ask your database questions -- specific questions, filtered questions, fuzzy questions. By the end of this module, you'll be able to pull exactly the data you need from any table. Let's go.

### Block 2 — DONE

_330 chars · ~330 credits_

> Here's a habit to build early: stop using SELECT star in production code. It's fine for quick exploration -- like when you're poking around a table to see what's in there. But when you're writing a real query, name your columns. It's clearer, it's faster, and it won't break when someone adds a new column to the table next month.

### Block 3 — DONE

_284 chars · ~284 credits_

> Aliases might seem like a small thing, but they make your query results dramatically more readable. When you're presenting data to someone who doesn't know what "stu_fn" means, aliases are your best friend. Get in the habit of using them whenever column names aren't self-explanatory.

### Block 4 — DONE

_275 chars · ~275 credits_

> The WHERE clause is where SQL goes from "show me a table" to "answer my question." Every comparison operator gives you a different way to slice the data. Equal, not equal, greater than, less than -- these are the fundamental building blocks of every filter you'll ever write.

### Block 5 — DONE

_343 chars · ~343 credits_

> AND and OR are straightforward on their own. The trouble starts when you combine them. AND binds tighter than OR -- just like multiplication before addition. The solution is simple: use parentheses every single time you mix AND and OR in the same WHERE clause. It makes your intent crystal clear and prevents bugs that are really hard to spot.

### Block 6 — DONE

_296 chars · ~296 credits_

> BETWEEN is syntactic sugar -- it doesn't do anything you can't do with greater-than-or-equal and less-than-or-equal. But it reads better, and readable SQL is maintainable SQL. One thing to remember: BETWEEN is inclusive on both ends. If you say BETWEEN 3.0 AND 3.5, both 3.0 and 3.5 are included.

### Block 7 — DONE

_249 chars · ~249 credits_

> IN is one of those features that, once you learn it, you'll use constantly. Any time you find yourself writing three or more OR conditions on the same column, switch to IN. It's cleaner, it's shorter, and it's less likely to have a bug hiding in it.

### Block 8 — DONE

_313 chars · ~313 credits_

> LIKE is your fuzzy search. The percent sign matches any number of characters, the underscore matches exactly one. Between these two wildcards, you can express just about any text pattern you need. It's especially useful for searching names, emails, and any free-text field where exact matching would be too rigid.

### Block 9 — DONE

_367 chars · ~367 credits_

> NULL will bite you if you're not careful. It's not zero, it's not an empty string, it's not false -- it's the complete absence of data. And because of that, normal comparison operators don't work with it. You must use IS NULL and IS NOT NULL. Burn this into your brain. You will forget it at least once, spend twenty minutes debugging, and then remember this warning.

### Block 10 — DONE

_308 chars · ~308 credits_

> These complex queries are where everything comes together. Notice how each one reads almost like English: "Show me students where GPA is above 3.7 and major is in this list and they have an advisor." That's the beauty of SQL -- when you write it well, it tells you exactly what it does. No decoding required.

### Block 11 — DONE

_297 chars · ~297 credits_

> That NULL question comes up every single time, and it trips up people who've been writing SQL for years. There's no shame in finding it confusing. Three-valued logic is genuinely weird. The practical takeaway is simple: for NULL, always use IS NULL or IS NOT NULL. For everything else, use equals.

### Block 12 — DONE

_237 chars · ~237 credits_

> Exercises 3 and 4 are the real test here. They force you to combine multiple techniques in a single query. Don't skip exercise 5 either -- understanding operator precedence with AND and OR will save you hours of debugging in your career.

### Block 13 — DONE

_363 chars · ~363 credits_

> Let's wrap up Module 3. You now have the tools to ask your database precise questions. SELECT picks the columns, WHERE filters the rows, and everything in between -- the comparisons, the logical operators, BETWEEN, IN, LIKE, IS NULL -- gives you the precision to find exactly what you need. In the next module, you'll learn how to sort and organize those results.

### Block 14 — DONE

_230 chars · ~230 credits_

> Now that you can filter your data, the next question is: how do you organize it? Module 4 covers sorting, limiting, and pagination -- the tools that turn a pile of matching rows into a clean, presentable result set. See you there.

---

## `module-04-sorting-and-limiting.md`

- Blocks: **12** | Chars: **3,388** | DONE: **12** | MISSING: **0** (0 chars)

### Block 1 — DONE

_418 chars · ~418 credits_

> Welcome to Module 4. In the last module, you learned how to filter data -- how to ask the right questions. But getting the right rows is only half the battle. If your results come back in random order, or you get 10,000 rows when you only need the top 5, you've got a presentation problem. This module solves that. We're going to sort, limit, paginate, and deduplicate your results until they're exactly what you need.

### Block 2 — DONE

_242 chars · ~242 credits_

> The key mental model is this: without ORDER BY, you have a pile of cards tossed on a table. With ORDER BY, you have a neatly arranged stack. The database will not sort for you automatically -- ever. If order matters to you, say so explicitly.

### Block 3 — DONE

_248 chars · ~248 credits_

> Multi-column sorting is one of those features that feels obvious once you see it, but it's surprisingly powerful. Any time you need a "sort by this, then by that" structure -- which is most of the time in real applications -- this is how you do it.

### Block 4 — DONE

_235 chars · ~235 credits_

> NULL sorting is one of those details that bites you exactly once, and then you remember it forever. In SQLite, NULLs come first when sorting ascending. If that's not what you want, filter them out with WHERE IS NOT NULL before sorting.

### Block 5 — DONE

_295 chars · ~295 credits_

> LIMIT plus ORDER BY is one of the most common query patterns in all of SQL. "Show me the top 10 by sales." "Show me the 5 most recent orders." "What's the single most expensive product?" You'll write this pattern hundreds of times in your career. It's simple, it's powerful, and it's everywhere.

### Block 6 — DONE

_277 chars · ~277 credits_

> The pagination formula is worth memorizing: offset equals page number minus one, times page size. It's one of those formulas that comes up in almost every web application. Any time you see a "page 2 of 47" interface, there's probably a LIMIT and OFFSET query running behind it.

### Block 7 — DONE

_276 chars · ~276 credits_

> DISTINCT is your deduplication tool. Need a list of all majors? All states? All departments? DISTINCT gives you the unique values. Just remember: when you SELECT DISTINCT with multiple columns, it's looking for unique combinations, not unique values in each individual column.

### Block 8 — DONE

_279 chars · ~279 credits_

> Notice the pattern in all of these: filter with WHERE, sort with ORDER BY, restrict with LIMIT. That three-step combo is the bread and butter of SQL. You'll write it so often it'll become muscle memory. And remember -- the clause order matters. SQL is very particular about that.

### Block 9 — DONE

_217 chars · ~217 credits_

> The most common mistake I see is LIMIT without ORDER BY. Without ORDER BY, LIMIT just gives you arbitrary rows. It's like asking for "the top 5" without saying what they're the top 5 of. Always sort first, then limit.

### Block 10 — DONE

_249 chars · ~249 credits_

> Exercise 6 is the real test. It combines everything from both this module and the last one -- filtering, sorting, limiting, and NULL handling -- into a single query. If you can write that one from scratch without looking back, you're in great shape.

### Block 11 — DONE

_350 chars · ~350 credits_

> Here's the summary for Module 4. ORDER BY sorts, LIMIT restricts, OFFSET paginates, and DISTINCT deduplicates. Combined with the filtering you learned in Module 3, you now have all the tools to write clean, organized, presentation-ready queries. Next up: we stop looking at individual rows and start looking at patterns. Aggregate functions are next.

### Block 12 — DONE

_302 chars · ~302 credits_

> You've learned to filter and sort individual rows. But what if you want to zoom out? What's the average GPA? How many students per major? What's the highest enrollment year? Module 5 introduces aggregate functions -- the tools that let you see patterns instead of individual data points. See you there.

---

## `module-05-aggregate-functions.md`

- Blocks: **11** | Chars: **3,837** | DONE: **11** | MISSING: **0** (0 chars)

### Block 1 — DONE

_440 chars · ~440 credits_

> Welcome to Module 5, and welcome to a fundamental shift in how you think about data. Up until now, every query you've written has returned individual rows -- individual students, individual records. That's useful, but it's like reading a city one house at a time. Aggregate functions let you zoom out and see the neighborhoods, the districts, the whole skyline. This is where SQL stops being a lookup tool and starts being an analysis tool.

### Block 2 — DONE

_302 chars · ~302 credits_

> Five functions, five superpowers. COUNT tells you "how many." SUM tells you "how much total." AVG tells you "what's typical." MIN and MAX tell you "what are the extremes." Individually, they're useful. Combined -- and especially combined with GROUP BY, which we'll cover next -- they're transformative.

### Block 3 — DONE

_260 chars · ~260 credits_

> Think of it as a two-step process. Step one: WHERE removes the rows you don't care about. Step two: the aggregate function summarizes what's left. The WHERE always happens first. This will become very important when we compare WHERE to HAVING in a few minutes.

### Block 4 — DONE

_368 chars · ~368 credits_

> GROUP BY is the single most important concept in this module. Without it, aggregate functions give you one summary for the whole table. With it, you get a summary for each group. It's the difference between "the average temperature this year was 65 degrees" and "here's the average temperature for each month." Both are useful, but the monthly breakdown tells a story.

### Block 5 — DONE

_263 chars · ~263 credits_

> Multi-column GROUP BY gives you drill-down capability. Need stats by department? Group by one column. Need stats by department and year? Group by two. Department, year, and advisor status? Three. Each additional column creates finer and finer slices of your data.

### Block 6 — DONE

_375 chars · ~375 credits_

> WHERE versus HAVING is probably the single most asked-about distinction in SQL. Here's the easy way to remember it: if you can point to the value in a single row of the original table, use WHERE. If you need to calculate the value across multiple rows first -- like a count or an average -- use HAVING. WHERE for rows, HAVING for groups. Tattoo it on your arm if you have to.

### Block 7 — DONE

_296 chars · ~296 credits_

> These are the kinds of queries that get you noticed at work. Not because they're complicated -- they're not -- but because they answer real questions. "How many students need advisors?" "Which departments are struggling?" "What's our enrollment trend?" Aggregate queries turn data into decisions.

### Block 8 — DONE

_366 chars · ~366 credits_

> That last question about NULLs is a great one. NULL means "I don't know this value." It doesn't mean zero. If you have three students with GPAs of 4.0, 3.0, and NULL, the average should be 3.5 (average of the two known values), not 2.33 (which is what you'd get if NULL were treated as zero). SQL's default behavior is correct here, even if it's surprising at first.

### Block 9 — DONE

_308 chars · ~308 credits_

> Exercise 5 is the critical one. It forces you to think about when WHERE runs versus when HAVING runs. If you can get that one right without help, you've got the WHERE-versus-HAVING distinction nailed. Exercise 7 is a thinking exercise -- the answer reveals how WHERE interacts with COUNT star in subtle ways.

### Block 10 — DONE

_492 chars · ~492 credits_

> That's Module 5. You've made the leap from looking at individual rows to seeing patterns across your entire dataset. COUNT, SUM, AVG, MIN, MAX -- these are your summary tools. GROUP BY splits data into meaningful categories. HAVING lets you filter those categories. Combined with WHERE, ORDER BY, and LIMIT from the previous modules, you now have a seriously powerful SQL toolkit. In the next module, we'll connect tables together with JOINs -- and that's where things get really interesting.

### Block 11 — DONE

_367 chars · ~367 credits_

> So far, every query we've written has pulled from a single table. But real databases have many tables, and the interesting questions usually span more than one. How many courses is each student taking? Which professor teaches the most popular class? Module 6 introduces JOINs -- the tool that connects tables together. That's where SQL really opens up. See you there.

---

## `module-06-joins.md`

- Blocks: **14** | Chars: **5,126** | DONE: **11** | MISSING: **3** (1,027 chars)

### Block 1 — DONE

_379 chars · ~379 credits_

> Welcome to Module 6, and honestly? This is the one. If there's a single concept that separates someone who "knows a little SQL" from someone who actually gets relational databases, it's joins. Everything you've done so far has been querying one table at a time. That's like reading one chapter of a book and saying you've read the whole thing. Joins let you read the whole story.

### Block 2 — DONE

_356 chars · ~356 credits_

> The reason data lives in separate tables has a fancy name -- normalization -- but the idea is simple. Don't repeat yourself. Keep each fact in one place. When you need to see the full picture, joins reassemble the pieces. It's elegant, it's efficient, and once you get it, you'll never want to go back to spreadsheet-style everything-in-one-table thinking.

### Block 3 — DONE

_444 chars · ~444 credits_

> Aliases look trivial, but they're one of those habits that separates cramped SQL from readable SQL. Pick the first letter of the table, or an abbreviation if that clashes. Stay consistent across your queries -- if s means students on Monday, it should still mean students on Friday. And once you start writing self-joins and derived tables in the next modules, aliases stop being optional. They become the only way the query makes sense at all.

### Block 4 — DONE

_324 chars · ~324 credits_

> INNER JOIN is the most common join you'll write. If someone just says "join" without specifying a type, they almost always mean INNER JOIN. In fact, you can even drop the word INNER -- just writing JOIN by itself defaults to an inner join. But I'd recommend being explicit, at least while you're learning. Say what you mean.

### Block 5 — DONE

_399 chars · ~399 credits_

> Here's a pro tip that will save you from a common mistake. The table order matters in a LEFT JOIN. The left table -- the one listed first, after FROM -- is the one that keeps all its rows. If you write FROM students LEFT JOIN enrollments, all students are preserved. Flip the order and you preserve all enrollments instead. The word "left" refers to position in the query, not some abstract concept.

### Block 6 — DONE

_291 chars · ~291 credits_

> Don't stress about RIGHT JOIN or FULL OUTER JOIN too much. RIGHT JOIN is just a LEFT JOIN with the tables swapped, and FULL OUTER JOIN is rare in the wild. If you master INNER JOIN and LEFT JOIN, you'll handle 95% of the joins you'll ever write. The other 5%? You'll Google them and be fine.

### Block 7 — DONE

_415 chars · ~415 credits_

> CROSS JOIN is the one you'll use the least, but when you need it, nothing else will do. The classic legitimate use is generating all valid combinations -- every day paired with every time slot to build a schedule, every product paired with every region for a sales matrix. Just remember it multiplies. Two tables of a hundred rows each becomes ten thousand rows. Check the size first or you'll lock up your session.

### Block 8 — DONE

_374 chars · ~374 credits_

> Self-joins are one of those things that seem weird until they click, and then you see uses for them everywhere. The key insight is that aliases let the same table pretend to be two different tables. Table "a" is one copy of students, table "b" is another copy. SQL doesn't care that they're actually the same table -- it treats them as two separate participants in the join.

### Block 9 — DONE

_398 chars · ~398 credits_

> Three-table joins feel like a big leap until you realize they're just two joins stacked together. Students connect to enrollments. Enrollments connect to courses. Each join statement handles one connection, and the database walks the chain for you. Your foreign keys are the map -- they literally tell you which columns belong in each ON clause. Follow the foreign keys and the query writes itself.

### Block 10 — DONE

_407 chars · ~407 credits_

> These complex queries are the payoff for everything you've learned so far. Joins bring the tables together. WHERE filters individual rows. GROUP BY collapses rows into groups. HAVING filters those groups. Aggregate functions crunch the numbers. And ORDER BY presents the results the way you want. Each piece you've learned is a tool, and now you're combining all of them in a single query. This is real SQL.

### Block 11 — DONE

_312 chars · ~312 credits_

> The most common confusion I see is people using INNER JOIN when they should be using LEFT JOIN, and then wondering why some rows disappeared from their results. If rows are vanishing, check your join type. INNER JOIN drops unmatched rows. LEFT JOIN keeps everything from the left side. That's usually the answer.

### Block 12 — **MISSING**

_346 chars · ~346 credits_

> Exercise 6 is the tricky one. When you use LEFT JOIN with COUNT, you need to count a column from the right table, not use COUNT star. COUNT star counts all rows including the NULL ones from the left join, which would give you 1 instead of 0 for unenrolled students. COUNT of a specific column skips NULLs. Try it both ways and see the difference.

### Block 13 — **MISSING**

_377 chars · ~377 credits_

> Here's your cheat sheet. INNER JOIN for matched rows only. LEFT JOIN for everything from the left plus matches from the right. CROSS JOIN for every possible combination. Self-join when you need to compare rows within the same table. And when in doubt, start with LEFT JOIN -- you can always see what's missing and then switch to INNER JOIN if you don't need the unmatched rows.

### Block 14 — **MISSING**

_304 chars · ~304 credits_

> You just learned how to connect tables together with joins. In the next module, you'll learn how to nest queries inside other queries -- like Russian dolls made of SQL. Combined with joins, subqueries let you answer questions that would be nearly impossible with a single flat query. See you in Module 7.

---

## `module-07-subqueries-and-views.md`

- Blocks: **14** | Chars: **5,012** | DONE: **13** | MISSING: **1** (333 chars)

### Block 1 — DONE

_432 chars · ~432 credits_

> Welcome to Module 7. You've already learned how to pull data from one table, filter it, aggregate it, and join multiple tables together. Now we're going to take it up a notch. What if the answer to your question depends on the answer to another question first? That's what subqueries are for -- a query inside a query. And once you've built a complex query you love, views let you save it and reuse it like a bookmark. Let's dig in.

### Block 2 — DONE

_340 chars · ~340 credits_

> If you can write a SELECT statement -- and you can, because you've been doing it for six modules -- then you can write a subquery. It's just a SELECT inside parentheses, tucked into another query. The database runs the inner query first, gets the result, and then plugs that result into the outer query. Inside out. That's the whole secret.

### Block 3 — DONE

_323 chars · ~323 credits_

> Scalar subqueries are the simplest type and the easiest to reason about. The inner query returns one number. The outer query uses that number in a comparison. If you can write "find the average" or "find the minimum," you can turn it into a scalar subquery by wrapping it in parentheses and dropping it into a WHERE clause.

### Block 4 — DONE

_329 chars · ~329 credits_

> IN with a subquery is one of those patterns you'll reach for all the time. "Find me everyone who has done X" -- subquery finds who did X, IN matches them. "Find me everyone who hasn't done X" -- same thing with NOT IN. Just watch out for NULLs with NOT IN. That gotcha has tripped up more experienced developers than I can count.

### Block 5 — DONE

_311 chars · ~311 credits_

> Here's my rule of thumb. If you're thinking "is this value in a list?" use IN. If you're thinking "does a related row exist?" use EXISTS. And if you're using NOT IN and getting weird empty results, switch to NOT EXISTS -- NULLs are probably the culprit. EXISTS is the more robust choice when NULLs are possible.

### Block 6 — DONE

_369 chars · ~369 credits_

> Derived tables are one of those features that makes you feel like a SQL wizard. You're basically saying to the database, "First, build me this little summary table. OK, now query THAT." It's a two-step thought process packed into one statement. The key thing to remember is that the derived table needs an alias -- give it a name, or SQL won't know how to reference it.

### Block 7 — DONE

_438 chars · ~438 credits_

> Correlated subqueries are the most powerful and the most misunderstood type of subquery. The key distinction is that reference to the outer query -- that's the "phone home" part. Every time the outer query moves to a new row, the inner query calls back and says "hey, what's the value for this row?" and recalculates. It's powerful for row-by-row comparisons, but it can be slow. When performance matters, try rewriting with a join first.

### Block 8 — DONE

_308 chars · ~308 credits_

> Views are one of those features that seem simple but change how you work with SQL day to day. Instead of copy-pasting that complex join query into every new report, you save it as a view once and then treat it like any other table. It keeps your queries short, your logic centralized, and your sanity intact.

### Block 9 — DONE

_487 chars · ~487 credits_

> Views don't have an ALTER VIEW statement in most databases -- at least not one you should rely on. The accepted pattern is drop and recreate. The IF EXISTS clause keeps things safe the first time you run the script when no view exists yet. You'll find yourself keeping a little block at the top of your SQL scripts that drops every view in reverse dependency order, then recreates them all. It's a tiny bit of ceremony that makes your schema reproducible, which is exactly what you want.

### Block 10 — DONE

_268 chars · ~268 credits_

> When you face a complex question, break it into pieces. What do I need to know first? Write that as a subquery. What do I need to know next? Wrap it in another layer. Build from the inside out, test each piece, and then combine. That's the method. It works every time.

### Block 11 — DONE

_368 chars · ~368 credits_

> The question I get most is "subquery or join?" and the honest answer is: it depends on readability. Both can solve the same problem. Subqueries read more like English -- "find students where the GPA is above the average." Joins are often more efficient for combining data. Learn both, and use whichever makes your intent clearer to the next person who reads your code.

### Block 12 — DONE

_335 chars · ~335 credits_

> Exercise 5 is the one that will really test your understanding of correlated subqueries. The subquery needs to find the MAX GPA for the current student's major, and then the outer query checks if the student's GPA matches that max. Think about what the correlation point is -- what value from the outer query does the inner query need?

### Block 13 — DONE

_371 chars · ~371 credits_

> Quick recap. Scalar subqueries for single values. IN and NOT IN for lists. EXISTS for checking if rows exist. Derived tables for intermediate result sets. Correlated subqueries when the inner query needs to reference the outer query. And views for saving your favorite complex queries so you never have to retype them. That's your subquery and views toolkit. Use it well.

### Block 14 — **MISSING**

_333 chars · ~333 credits_

> You now know how to query data in incredibly sophisticated ways -- joins, subqueries, views. But so far, you've only been reading. In the next module, we'll learn how to change what's already there. UPDATE and DELETE are powerful, and just a little bit dangerous. We'll make sure you know how to use them safely. See you in Module 8.

---

## `module-08-updating-and-deleting.md`

- Blocks: **14** | Chars: **5,091** | DONE: **10** | MISSING: **4** (1,379 chars)

### Block 1 — DONE

_471 chars · ~471 credits_

> Welcome to Module 8. Up until now, everything you've done in SQL has been safe. SELECT queries are like window shopping -- you look, but you don't touch. That changes today. UPDATE and DELETE actually change your data, and in most cases, there's no undo button. So before we write a single UPDATE statement, we're going to talk about safety. Because the difference between a good database administrator and someone updating their resume is often one missing WHERE clause.

### Block 2 — DONE

_267 chars · ~267 credits_

> Notice that both UPDATE and DELETE have the same basic shape -- a table name and a WHERE clause. That WHERE clause is doing all the heavy lifting. It's the difference between "fix Alice's GPA" and "fix everyone's GPA." We'll come back to why that matters in a moment.

### Block 3 — DONE

_311 chars · ~311 credits_

> I cannot stress this enough. Professional database administrators who have been doing this for twenty years still test with SELECT first. It's not a beginner thing -- it's a smart thing. The five seconds it takes to preview your results can save you from explaining to your boss why the customer table is empty.

### Block 4 — DONE

_282 chars · ~282 credits_

> CASE expressions in UPDATE are incredibly powerful. Instead of writing three separate UPDATE statements and scanning the table three times, you write one statement that handles all the logic. It's more efficient, and more importantly, it's atomic -- all the changes happen together.

### Block 5 — DONE

_485 chars · ~485 credits_

> DELETE is blunt. It's not a soft delete, it's not a hide, it's not a move-to-archive. It's gone. That's why the WHERE clause is the most important part of any DELETE statement. Read your DELETE statement out loud before running it -- "delete from enrollments where grade equals F" sounds right. But "delete from enrollments" with no WHERE -- that's the one that shows up in post-mortems. Every professional DBA has a war story about a missing WHERE clause. Don't add yours to the pile.

### Block 6 — DONE

_358 chars · ~358 credits_

> Subqueries in UPDATE and DELETE are where the golden rule matters most. You're now modifying data based on a chain of logic -- "delete enrollments for students whose major is this, in courses from that department." The more complex the logic, the more critical it is to preview with SELECT first. Test every layer of the subquery before you pull the trigger.

### Block 7 — DONE

_500 chars · ~500 credits_

> The cascade question is the most important one here. When you delete a student, what happens to their enrollments? If you set up the foreign key with ON DELETE CASCADE, the enrollments vanish too -- automatic cleanup. Without cascade, you either get blocked by the foreign key or you leave orphan records behind. Neither is a disaster, but both need to be a conscious choice when you design the schema. Don't just copy-paste foreign keys. Think about what should happen when the parent row goes away.

### Block 8 — DONE

_319 chars · ~319 credits_

> Think of a transaction like an envelope. You put all your SQL statements inside the envelope, and you don't mail it until you're ready. BEGIN opens the envelope. Each statement goes inside. COMMIT seals it and sends it. ROLLBACK shreds the whole thing. Nothing inside the envelope affects the database until you COMMIT.

### Block 9 — DONE

_302 chars · ~302 credits_

> The pattern is always the same: multiple related changes that must succeed or fail together. Anytime you find yourself writing two or more statements that are logically connected -- where one without the other would leave your data in a broken state -- wrap them in a transaction. It's cheap insurance.

### Block 10 — DONE

_417 chars · ~417 credits_

> Here's the workflow I want you to internalize. Type BEGIN TRANSACTION. Run your changes. Run a SELECT to verify the result looks right. If it does, COMMIT. If it doesn't, ROLLBACK. That sequence -- begin, change, verify, commit or rollback -- is the safest way to do surgery on a database. Do that every single time until it becomes muscle memory. It turns every risky operation into a preview you can walk away from.

### Block 11 — **MISSING**

_307 chars · ~307 credits_

> None of these mistakes require advanced SQL knowledge to make. They're typos, mental slips, and moments of inattention. That's exactly what makes them so dangerous -- and exactly why the safety habits we've been drilling matter so much. The SELECT-first rule and transactions are your two best friends here.

### Block 12 — **MISSING**

_398 chars · ~398 credits_

> The transaction exercise is the one I really want you to do. Seeing ROLLBACK actually undo a DELETE you just ran is a genuinely reassuring experience -- it turns transactions from an abstract concept into a tool you trust. Run the DELETE statements, check that the rows are gone with a SELECT, then ROLLBACK, then SELECT again and watch the rows come back. That moment is why we teach transactions.

### Block 13 — **MISSING**

_380 chars · ~380 credits_

> Let's recap. UPDATE and DELETE are powerful and permanent. Your safety net is a three-part system: test with SELECT first, use transactions for multi-step operations, and always double-check your WHERE clause. Master those three habits and you can confidently modify data without losing sleep. Next up, we'll look at how to make your queries faster and your databases more secure.

### Block 14 — **MISSING**

_294 chars · ~294 credits_

> You now know how to do everything with data -- create it, read it, update it, delete it. The full CRUD cycle. In Module 9, we zoom out and ask the bigger questions: how do we make this fast? How do we make this secure? How do we design databases that don't become a tangled mess? See you there.

---

## `module-09-indexes-and-best-practices.md`

- Blocks: **14** | Chars: **5,126** | DONE: **10** | MISSING: **4** (1,479 chars)

### Block 1 — DONE

_428 chars · ~428 credits_

> Welcome to Module 9, the final module. Up until now, you've been learning how to talk to databases -- how to create tables, insert data, query it, join it, and modify it. All essential skills. But there's a difference between a query that works and a query that works well. Between a database that functions and one that's fast, secure, and well-organized. That's what this module is about. We're zooming out to the big picture.

### Block 2 — DONE

_321 chars · ~321 credits_

> Here's the key insight: you don't change your queries at all. You write the same SELECT statements you've always written. The index works behind the scenes, silently making things faster. The database optimizer sees the index, recognizes it can skip the full table scan, and uses the shortcut. You just have to create it.

### Block 3 — DONE

_269 chars · ~269 credits_

> Indexing is about trade-offs. Every index you create makes reads faster and writes slower. The art is finding the columns where the read benefit far outweighs the write cost. In most applications, that's your WHERE columns, your JOIN columns, and your ORDER BY columns.

### Block 4 — DONE

_488 chars · ~488 credits_

> The phone book analogy is the one that sticks for most people. A phone book is sorted by last name, then first name. You can find all the Smiths instantly because last name is the primary sort. You can find John Smith quickly because within the Smiths, it's sorted by first name. But finding every John in the book? You'd have to read every page. That's exactly how composite indexes work. Put the column you filter on most often first, and the index earns its keep on almost every query.

### Block 5 — DONE

_269 chars · ~269 credits_

> EXPLAIN QUERY PLAN is like asking the database to show its work. Instead of guessing whether your index is helping, you can see exactly what strategy the database is using. SCAN means slow. SEARCH USING INDEX means fast. That's all you need to know to start optimizing.

### Block 6 — DONE

_347 chars · ~347 credits_

> SQL injection has been around for decades and it's still one of the top security vulnerabilities. Not because it's hard to prevent -- the fix is literally one line of code -- but because developers forget. Or they think "nobody would try that on my little app." They would. They do. Use parameterized queries everywhere, every time, no exceptions.

### Block 7 — DONE

_466 chars · ~466 credits_

> The question about why databases don't just auto-index everything is a really common one. The answer is always a trade-off. Every index makes reads faster and writes slower and takes up disk space. On a tiny table, none of that matters. On a table with millions of rows and lots of inserts, it matters a lot. Your job as the developer is to decide which columns get indexes based on how that table is actually used. There's no automatic answer -- it's a design call.

### Block 8 — DONE

_295 chars · ~295 credits_

> The progression is logical. 1NF says no lists in cells. 2NF says every column depends on the whole key. 3NF says no column depends on another non-key column. Each step reduces redundancy and makes your data harder to accidentally mess up. For most applications, getting to 3NF is the sweet spot.

### Block 9 — DONE

_519 chars · ~519 credits_

> Nobody teaches naming conventions in a beginner course, but every senior developer has strong opinions about them. Pick a convention and stick to it. Tables plural, columns singular, everything lowercase with underscores. Foreign keys name the table they point to. Indexes name the table and the columns. It looks like fussiness, but it pays off the first time you're reading someone else's schema and can figure out what every column does without having to ask. Consistency is a form of kindness to the next developer.

### Block 10 — DONE

_245 chars · ~245 credits_

> The difference between a beginner and a professional often isn't what queries they write -- it's how they write them. Clean SQL is easier to read, easier to debug, and often faster. The habits you build now will serve you for your entire career.

### Block 11 — **MISSING**

_317 chars · ~317 credits_

> This is what it all looks like when you put it together. Every naming convention, every normalization rule, every indexing decision -- they all stack on top of each other to create a database that's fast, consistent, and a pleasure to work with. This is the difference between a hobby database and a professional one.

### Block 12 — **MISSING**

_515 chars · ~515 credits_

> The e-commerce schema exercise is the capstone. It pulls together everything -- normalization, foreign keys, constraints, and indexing -- on a problem you've seen a hundred times as a customer. Pay special attention to the order-items table. That's where most beginners stumble, because it stores the price at the time of purchase separately from the current product price. That's deliberate. Prices change. Orders don't. Getting that detail right is the difference between a student schema and a production schema.

### Block 13 — **MISSING**

_407 chars · ~407 credits_

> That wraps up not just this module, but the entire SQL Fundamentals course. You started by learning what a database even is, and now you're designing normalized schemas, optimizing queries with indexes, and defending against SQL injection. That's a real skill set. Whether you're building your own applications or working with a team, you now have the foundation to work with data professionally. Nice work.

### Block 14 — **MISSING**

_240 chars · ~240 credits_

> You've gone from zero to a solid foundation in SQL. That's not a small thing. Databases are everywhere -- behind every website, every app, every system that stores and retrieves information. You now speak their language. Go build something.

---

