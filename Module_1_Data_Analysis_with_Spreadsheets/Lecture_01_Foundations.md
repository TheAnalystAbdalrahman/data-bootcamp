# Lecture 1 — Spreadsheet Foundations

## Outcome for today

By the end of the lecture, students can inspect a structured table, sort and filter it, calculate basic measures, create a row-level formula, and write one defensible observation.

## What to prepare

- Open `Lecture_01_Market_Prices.xlsx` before class.
- Use the `Practice Data` sheet for demonstrations and student work.
- Keep `Instructor Key` for the debrief.
- If students use Google Sheets, upload the workbook and confirm that dates and formulas import correctly.

## 3-hour run-of-show

| Time | Segment | What students do |
|---:|---|---|
| 0:00–0:10 | Welcome and framing | Describe one decision data could improve. |
| 0:10–0:30 | What a dataset is | Identify a row, column, record, field, header, and unique ID. |
| 0:30–0:50 | Spreadsheet navigation | Select ranges, resize columns, freeze the header, use undo, and find a value. |
| 0:50–1:05 | Sort and filter | Sort prices high-to-low and filter one commodity and one state. |
| 1:05–1:15 | Break | — |
| 1:15–1:40 | First formulas | Use `SUM`, `AVERAGE`, `MIN`, `MAX`, `COUNT`, and `COUNTA`. |
| 1:40–2:05 | Row-level calculation | Calculate purchase cost as quantity × unit price and fill the formula down. |
| 2:05–2:20 | Cell references | Compare a relative reference with a fixed tax or commission cell using `$`. |
| 2:20–2:30 | Break | — |
| 2:30–2:50 | Independent challenge | Complete the six questions below without step-by-step instructions. |
| 2:50–3:00 | Debrief and exit ticket | Share one observation and label any explanation as a hypothesis. |

If the class is two hours, omit the fixed-rate extension and complete only questions 1–5.

## Opening explanation

Use this small example:

| transaction_id | date | market | commodity | quantity | unit_price_sdg |
|---|---|---|---|---:|---:|
| T001 | 2026-09-01 | Port Sudan Central | Sorghum | 3 | 2200 |

Ask:

1. What does one row represent?
2. Which field identifies the row?
3. Which columns contain categories?
4. Which columns contain numbers we can calculate with?
5. What could go wrong if a date or price were stored as text?

The key message is: a spreadsheet is a table of observations, and every formula should answer a question.

## Demonstration sequence

### 1. Inspect before calculating

Ask students to state what one row represents. Confirm the unit of price and whether transaction IDs are unique. Point out that `state`, `market`, and `commodity` are categories, while `quantity` and `unit_price_sdg` are numeric measures.

### 2. Sort and filter

Demonstrate:

- sorting `unit_price_sdg` from largest to smallest;
- filtering to one commodity;
- adding a second filter for one state; and
- clearing filters before continuing.

Ask why “Which market is cheapest?” is incomplete. A good answer is that the comparison needs a commodity, unit, and date or period.

### 3. Basic summary formulas

Connect each function to a question:
| Question | Function |
|---|---|
| How much altogether? | `SUM` |
| What is the typical arithmetic average? | `AVERAGE` |
| What is the smallest value? | `MIN` |
| What is the largest value? | `MAX` |
| How many numeric observations? | `COUNT` |
| How many nonblank records or labels? | `COUNTA` |

Have students type formulas themselves. Avoid pasting all formulas at once.

### 4. Calculate purchase cost

In the first data row under `purchase_cost_sdg`, enter:

```excel
=G2*H2
```

Fill the formula down. Explain that the row references change because they are relative.

### 5. Show one absolute reference

Put a commission rate, such as `2%`, in a separate cell. Calculate:

```excel
=I2*$L$2
```

Explain that `$L$2` remains fixed when the formula is copied. Keep this extension short; the goal is recognition, not mastery.

## Independent challenge

Students use the `Practice Data` sheet to answer:

1. How many price observations are recorded?
2. What are the highest and lowest unit prices?
3. What is the average unit price?
4. What is the total purchase cost across all rows?
5. For sorghum only, which listed market has the lowest unit price?
6. Write one observation that includes a number and does not invent a cause.

### Optional challenge for faster students

- Calculate the total purchase cost for only Kassala using `SUMIF` or `SUMIFS`.
- Apply a 2% commission using an absolute reference.

## Debrief prompts

- What formula gave you the greatest difficulty?
- How did you check that the result was reasonable?
- Did sorting change the data, or only its order?
- Is the average always the best description of a price?
- What additional data would you need to explain price differences?

## Exit ticket

Give students five minutes to complete these tasks independently:

1. Filter to one commodity.
2. Calculate its total purchase cost.
3. Identify its highest unit price.
4. Write one evidence-based sentence.

Collect the sentence. It reveals whether students can move from calculation to interpretation.

## Common mistakes to watch for

- Typing a formula without the initial `=`.
- Multiplying the wrong columns.
- Including the header in a numeric range.
- Reading a filtered subtotal as if it represented the full dataset.
- Overwriting the original quantity or price column.
- Claiming a cause that the dataset does not measure.

## End-of-class message

Students do not need to memorize every function. They need to recognize the question, choose a suitable operation, check the answer, and explain it honestly.

