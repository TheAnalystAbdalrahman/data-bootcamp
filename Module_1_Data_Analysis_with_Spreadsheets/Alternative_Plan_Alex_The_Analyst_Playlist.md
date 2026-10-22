# Alternative Module 1 Plan — Alex The Analyst Excel Playlist

**Source playlist:** [Excel Tutorials for Data Analysts](https://www.youtube.com/playlist?list=PLUaB-1hjhk8Hyd5NiPQ9CND82vNodlFF5)  
**Format:** Three live sessions of approximately 3 hours, followed by one application week  
**Level:** Absolute beginners  
**Primary tool:** Microsoft Excel. Google Sheets can be used where the demonstrated feature is available, but menu steps may differ.

## Why this version is different

This plan uses the playlist's seven practical skills as the module spine. It places spreadsheet orientation before the playlist's first lesson on PivotTables because students need to understand a structured table before grouping its records. Each video becomes a short preparation or review resource; live time is used for demonstration, guided practice, and independent work. The portfolio project remains an original Sudanese business case rather than a copy of the video's guided project.

## Playlist map

The playlist presents these seven lessons in the order shown below. Durations are approximate.

| Playlist order | Video | Length | Use in this module |
|---:|---|---:|---|
| 1 | [Pivot Tables in Excel](https://www.youtube.com/watch?v=lH7HfwUFnYA) | 18 min | Session 3: group and summarize records. |
| 2 | [Formulas in Excel](https://www.youtube.com/watch?v=XRPyj7cKVsQ) | 34 min | Sessions 1–2: arithmetic, basic functions, `IF`, and conditional totals. |
| 3 | [XLOOKUP in Excel](https://www.youtube.com/watch?v=Z7hPEwCzk2s) | 19 min | Session 2: bring a product attribute into a transaction table. |
| 4 | [Conditional Formatting in Excel](https://www.youtube.com/watch?v=_eZRkmRfVTM) | 21 min | Session 2: highlight missing values and low stock. |
| 5 | [Charts in Excel](https://www.youtube.com/watch?v=gMAHXrty6wI) | 15 min | Session 3: compare categories and show change over time. |
| 6 | [Cleaning Data in Excel](https://www.youtube.com/watch?v=_jmiEGZ6PIY) | 21 min | Session 2: inspect, standardize, and document cleaning. |
| 7 | [Full Project in Excel](https://www.youtube.com/watch?v=opJgMj1IUrc) | 41 min | Session 3 preview and optional project-week model. |

The full set is about 2 hours 48 minutes of video. Watching it all during class would consume most of a live day, so assign the relevant videos as optional preparation and focused review.

## Session 1 — Understand the data and calculate

**Learning target:** Students can read a rectangular dataset, sort and filter it, calculate a new column, and check basic summary figures.

**Use today:** The existing `Lecture_01_Market_Prices.xlsx` and `Lecture_01_Foundations.md` work as the Session 1 practice pack. Prepare a student copy of the workbook without the `Instructor Key` sheet before distributing it.

| Time | Activity | Student output |
|---:|---|---|
| 0:00–0:20 | Business question and table anatomy: one row, one record, headers, IDs, dates, categories, numeric fields. | Students explain what one row represents. |
| 0:20–0:45 | Excel navigation, cell references, sorting, filtering, and checking the number of visible records. | Correctly filtered commodity and state. |
| 0:45–1:15 | Arithmetic and the first functions: `SUM`, `AVERAGE`, `MIN`, `MAX`, `COUNT`, `COUNTA`. | Six answers with formulas. |
| 1:15–1:25 | Break. | — |
| 1:25–1:55 | Create `purchase_cost_sdg = quantity × unit_price_sdg`; fill down; test one result by hand. | Complete calculated column. |
| 1:55–2:15 | Relative versus fixed cell references using one commission rate. | One copied formula with `$` references. |
| 2:15–2:25 | Break. | — |
| 2:25–2:50 | Independent market-price challenge. | One formula-backed observation. |
| 2:50–3:00 | Debrief: observation versus explanation. | Exit ticket and one question for the next class. |

**Video assignment:** Use the [Formulas](https://www.youtube.com/watch?v=XRPyj7cKVsQ) lesson for review. Ask students to identify three functions they used and one function they have not yet practiced. The video covers more functions than Session 1; students are not expected to master them all immediately.

**Mastery check:** Each student can identify the grain of the data, calculate purchase cost correctly, explain a summary result, and distinguish a direct observation from a guess about its cause.

## Session 2 — Clean and enrich data

**Learning target:** Students can make a working copy of raw data, find quality problems, use simple conditional calculations, and connect a lookup table.

Use a small synthetic NileCare pharmacy sales extract with 30–50 rows and a separate product reference table. Include a few duplicates, inconsistent branch/category labels, blanks, extra spaces, and one product ID absent from the reference table. Avoid patient data.

| Time | Activity | Student output |
|---:|---|---|
| 0:00–0:25 | Compare `RAW_DATA` with `CLEAN_DATA`; inspect before making changes. | A short issue log. |
| 0:25–0:55 | Clean branch/category text, inspect duplicates, and decide how to handle blanks. | Clean working table with original preserved. |
| 0:55–1:20 | `IF`, `COUNTIF/S`, and `SUMIF/S` to answer business questions. | Value bands and two grouped totals. |
| 1:20–1:30 | Break. | — |
| 1:30–2:05 | `XLOOKUP` product ID to product name/category; inspect the unmatched ID. | Joined product attributes and an explicit unmatched case. |
| 2:05–2:25 | Conditional formatting for low stock, duplicates, and blanks. | Two useful, bounded rules. |
| 2:25–2:35 | Break. | — |
| 2:35–3:00 | Independent repair challenge and discussion. | Cleaning decisions and two evidence-based observations. |

**Video assignments:** [Cleaning Data](https://www.youtube.com/watch?v=_jmiEGZ6PIY) and [XLOOKUP](https://www.youtube.com/watch?v=Z7hPEwCzk2s) before or after class; [Conditional Formatting](https://www.youtube.com/watch?v=_eZRkmRfVTM) as optional review. Use only the relevant parts of the [Formulas](https://www.youtube.com/watch?v=XRPyj7cKVsQ) lesson for `IF` and conditional totals.

**Mastery check:** Students preserve raw data, document cleaning decisions, calculate one conditional metric correctly, and notice an unmatched lookup instead of treating it as a valid category.

## Session 3 — Summarize, visualize, and explain

**Learning target:** Students can build and check a PivotTable, make two appropriate charts, and state what a manager should investigate or do next.

| Time | Activity | Student output |
|---:|---|---|
| 0:00–0:25 | Start with management questions and choose measures before making a chart. | Three analysis questions. |
| 0:25–1:05 | PivotTables: rows, columns, values, filters; check `Sum` versus `Count`. | Revenue by branch and category. |
| 1:05–1:15 | Break. | — |
| 1:15–1:50 | Bar chart for category comparison; line chart for a date trend. | Two labeled charts. |
| 1:50–2:15 | Build a compact one-page dashboard: 3–4 KPIs, 2–3 charts, one filter if supported. | Draft dashboard. |
| 2:15–2:25 | Break. | — |
| 2:25–2:50 | Mini case: interpret a branch with strong sales but weaker gross profit. | Two insights and one evidence-linked recommendation. |
| 2:50–3:00 | Project briefing and exit ticket. | Individual project plan. |

**Video assignments:** [Pivot Tables](https://www.youtube.com/watch?v=lH7HfwUFnYA) and [Charts](https://www.youtube.com/watch?v=gMAHXrty6wI) as targeted review. The [Full Project](https://www.youtube.com/watch?v=opJgMj1IUrc) video is an optional model after students attempt their own mini case. Students may watch its workflow, but their portfolio submission must use the module's different dataset and questions.

**Mastery check:** Students can trace a dashboard number back to clean rows, explain the aggregation used in a PivotTable, and give one recommendation grounded in the displayed evidence.

## Application week — Independent portfolio project

**Project:** NileCare Community Pharmacies Performance Analysis, using the synthetic business case in the original Module 1 outline.

**Management questions:** Which branches and product categories generate the most revenue and gross profit? What is changing over time? Which fast-selling products have low remaining stock? What should management review first?

**Suggested work sequence:**

| Stage | Student task | Checkpoint |
|---|---|---|
| Days 1–2 | Inspect raw transactions, define one row, log quality issues, and create clean data. | Raw data preserved; cleaning log completed. |
| Days 3–4 | Calculate revenue, cost, gross profit, and margin; use a lookup where appropriate. | Spot-check sample rows by hand. |
| Day 5 | Create PivotTables, KPIs, and charts. | Totals reconcile with clean data. |
| Day 6 | Peer or mentor review. | Correct errors and sharpen insight wording. |
| Day 7 | Submit workbook and short findings. | Final independent submission. |

**Submission:** One workbook containing `README`, `RAW_DATA`, `CLEAN_DATA`, `ANALYSIS`, `DASHBOARD`, and `INSIGHTS`; three evidence-based findings; and one recommendation. A short spoken presentation can serve as the final check.

**Assessment:** Cleaning 20%, formula accuracy 20%, analysis and PivotTables 20%, charts/dashboard 15%, interpretation 15%, documentation 10%. Use a 70% pass threshold and allow a targeted revision when a core skill is missing. Required evidence includes preserved raw data, a correct revenue calculation, one valid PivotTable, one meaningful chart, and one supported insight.

## Scope controls

- Teach only the functions needed to answer the module's business questions. The formula video demonstrates more than beginners need in one weekend.
- Keep `XLOOKUP` to exact-match product IDs; show the unmatched case explicitly. If the cohort's Excel version lacks it, use an instructor-prepared lookup alternative for that exercise.
- Use conditional formatting to reveal a defined issue, not as decoration.
- Require every chart to answer a stated question and display units clearly.
- Leave Power Query, VBA, macros, advanced formulas, and elaborate dashboards for later study.

## Source and adaptation note

The seven titles, sequence, and approximate durations were cross-checked against [a seven-lesson course listing](https://www.mindluster.com/lesson/247567-video) and the linked creator videos. The session sequence, Sudanese practice cases, timing, mastery checks, and assessment are this bootcamp's adaptation; they are not presented as the creator's syllabus.
