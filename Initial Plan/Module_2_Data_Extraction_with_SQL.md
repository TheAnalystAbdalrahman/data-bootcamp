# Module 2 — Data Extraction with SQL
## 4-Class Practical Module

**Audience:** Absolute beginners who have completed the Spreadsheets module  
**Format:** 4 intensive live classes  
**Primary Focus:** Querying, filtering, aggregating, joining, and reasoning with relational data  
**Practice Platform:** Browser-based SQL environment for daily exercises (e.g., SQLiteOnline)  
**Final Project Platform:** Google BigQuery Sandbox  
**Context:** Sudanese banking, telecom, healthcare, retail, and service-delivery scenarios  
**Assessment:** One portfolio-ready SQL mini-project  
**Teaching Approach:** Approximately **20–25% explanation / 75–80% guided and independent querying**

---

# 1. Module Philosophy

Students have just learned to work with rows, columns, filters, formulas, lookups, Pivot Tables, and summaries in spreadsheets.

The goal of this module is not to make SQL feel like “coding from scratch.”

The goal is to show students:

> **“SQL is another way of asking questions from data — especially when the data is too large, structured, or spread across multiple tables.”**

The teaching bridge should constantly map SQL ideas back to familiar spreadsheet ideas.

For example:

| Spreadsheet Concept | SQL Equivalent |
|---|---|
| Open a worksheet | Query a table |
| Select columns | `SELECT` |
| Filter rows | `WHERE` |
| Sort | `ORDER BY` |
| Count rows | `COUNT()` |
| Sum values | `SUM()` |
| Pivot Table grouping | `GROUP BY` |
| `IF()` | `CASE WHEN` |
| `XLOOKUP()` / `VLOOKUP()` | `JOIN` |
| Filter after summary | `HAVING` |
| Helper table / intermediate result | Subquery / CTE |

The core message should be:

> **SQL is not magic syntax. It is structured questioning.**

---

# 2. Module Learning Outcomes

By the end of the module, students should be able to:

- Understand what a relational database is.
- Distinguish a table, row, column, primary key, and foreign key.
- Write basic `SELECT` statements.
- Filter rows using `WHERE`.
- Use `AND`, `OR`, `IN`, `BETWEEN`, and `LIKE`.
- Sort results with `ORDER BY`.
- Limit results with `LIMIT`.
- Aggregate data using `COUNT`, `SUM`, `AVG`, `MIN`, and `MAX`.
- Group records using `GROUP BY`.
- Filter aggregated results using `HAVING`.
- Build simple categories using `CASE WHEN`.
- Understand relationships between tables.
- Use `INNER JOIN` and `LEFT JOIN`.
- Recognize common JOIN errors.
- Use aliases to make queries readable.
- Write simple subqueries.
- Use beginner-friendly CTEs (`WITH`) to structure longer queries.
- Translate a business question into SQL steps.
- Read and debug basic SQL errors.
- Write a multi-step query that answers a real business question.

---

# 3. Overall 4-Day Learning Journey

| Day | Theme | Student Mindset |
|---|---|---|
| **Day 1** | SQL Foundations: `SELECT`, `WHERE`, `ORDER BY` | “I can ask a database for exactly the rows and columns I need.” |
| **Day 2** | Aggregations, `GROUP BY`, `CASE WHEN` | “I can summarize large datasets and answer business questions.” |
| **Day 3** | Demystifying `JOIN`s | “I can connect related tables instead of using one giant spreadsheet.” |
| **Day 4** | Subqueries, CTEs & Capstone Preparation | “I can break a complex business problem into SQL steps.” |

The progression is:

**Retrieve → Filter → Summarize → Connect → Structure → Explain**

---

# 4. Day 1 — SQL Foundations
## Theme: From Spreadsheet Filters to Database Queries

### Main Objective

Help students understand the structure of a SQL query and build confidence by mapping familiar Excel/Google Sheets actions directly to SQL.

Students should leave Day 1 able to retrieve columns, filter records, sort results, and answer simple questions independently.

---

## Core Topics

### 1. What Is a Database?

Use simple language.

Explain:

> A spreadsheet usually feels like one file with sheets.  
> A database is designed to store larger, structured, related collections of data.

Introduce:

- Database
- Table
- Row
- Column
- Record
- Data type

### Spreadsheet Bridge

**Spreadsheet:**

| transaction_id | customer | amount |
|---|---|---:|

**Database Table:**

Same idea — but stored and queried differently.

---

### 2. First SQL Query

```sql
SELECT *
FROM transactions;
```

Explain:

- `SELECT` = what columns do I want?
- `FROM` = which table do I want them from?

Then:

```sql
SELECT transaction_id, customer_name, amount
FROM transactions;
```

### Spreadsheet Bridge

Equivalent to:

> “Show me only these three columns.”

---

### 3. Filtering with `WHERE`

```sql
SELECT *
FROM transactions
WHERE state = 'Khartoum';
```

Map directly to spreadsheet filters.

Teach:

- `=`
- `>`
- `<`
- `>=`
- `<=`
- `<>` or `!=`

---

### 4. Combining Conditions

Teach:

```sql
AND
OR
```

Example:

```sql
SELECT *
FROM transactions
WHERE state = 'Red Sea'
  AND amount_sdg > 50000;
```

---

### 5. `IN`

Instead of:

```sql
state = 'Red Sea'
OR state = 'Kassala'
OR state = 'Gedaref'
```

Teach:

```sql
WHERE state IN ('Red Sea', 'Kassala', 'Gedaref')
```

---

### 6. `BETWEEN`

Example:

```sql
WHERE amount_sdg BETWEEN 10000 AND 50000
```

---

### 7. `LIKE`

Teach text searching.

```sql
WHERE customer_name LIKE 'A%'
```

Examples:

- Names beginning with A
- Products containing “Oil”
- IDs matching a pattern

---

### 8. Sorting

```sql
ORDER BY amount_sdg DESC
```

Map to:

> Sort Largest to Smallest

---

### 9. Limiting Results

```sql
LIMIT 10
```

Use:

> “Show me the top 10 records.”

---

### 10. Aliases

Introduce simple aliases:

```sql
SELECT
  customer_name AS customer,
  amount_sdg AS transaction_value
FROM transactions;
```

Explain aliases as readability, not complexity.

---

# 5. Day 1 Practical Exercise
## Sudanese Mobile Money Transactions

Use a fictional mobile-payment dataset inspired by everyday digital finance usage.

Table:

```text
mobile_transactions
```

Columns:

```text
transaction_id
transaction_date
customer_id
state
transaction_type
amount_sdg
channel
status
```

Possible `transaction_type` values:

```text
Transfer
Bill Payment
Airtime
Cash Out
Cash In
Merchant Payment
```

Possible `channel` values:

```text
Mobile App
USSD
Agent
Merchant
```

### Student Tasks

Write SQL queries to:

1. Show all successful transactions.
2. Show transactions above SDG 100,000.
3. Show only `Transfer` and `Merchant Payment` transactions.
4. Show transactions from `Red Sea` or `Kassala`.
5. Show the 10 largest successful transactions.
6. Find transactions whose channel is `USSD`.
7. Show only:
   - transaction ID
   - state
   - amount
   - transaction type

### Exit Challenge

Ask:

> “Show the 5 largest successful merchant payments from Kassala.”

Students must solve it without step-by-step guidance.

---

# 6. Day 1 Teaching Emphasis

Students should understand the basic SQL sentence:

```text
SELECT
FROM
WHERE
ORDER BY
LIMIT
```

Tell them:

> **Read the query as English before reading it as code.**

Example:

```sql
SELECT transaction_id, amount_sdg
FROM mobile_transactions
WHERE state = 'Kassala'
ORDER BY amount_sdg DESC
LIMIT 5;
```

Read aloud:

> “Select transaction ID and amount from mobile transactions where the state is Kassala, order by amount from highest to lowest, and show only five.”

---

# 7. Day 2 — Aggregation & Business Questions
## Theme: From Individual Rows to Management Summaries

### Main Objective

Teach students to summarize datasets and answer management-level questions using aggregation.

This should feel like moving from:

> Spreadsheet filters

to:

> Pivot Tables in SQL.

---

## Core Topics

### 1. Aggregation Functions

Teach:

```sql
COUNT()
SUM()
AVG()
MIN()
MAX()
```

Examples:

```sql
SELECT COUNT(*)
FROM transactions;
```

```sql
SELECT SUM(amount_sdg)
FROM transactions;
```

```sql
SELECT AVG(amount_sdg)
FROM transactions;
```

---

### 2. `GROUP BY`

Explain with a direct Pivot Table analogy.

Spreadsheet Pivot:

```text
Rows: State
Values: Sum of Amount
```

SQL:

```sql
SELECT
  state,
  SUM(amount_sdg) AS total_amount
FROM transactions
GROUP BY state;
```

This should be one of the strongest Excel → SQL bridges in the module.

---

### 3. Multiple Aggregations

Example:

```sql
SELECT
  state,
  COUNT(*) AS transaction_count,
  SUM(amount_sdg) AS total_value,
  AVG(amount_sdg) AS avg_value
FROM transactions
GROUP BY state;
```

---

### 4. Grouping by More Than One Field

Example:

```sql
SELECT
  state,
  transaction_type,
  SUM(amount_sdg) AS total_amount
FROM transactions
GROUP BY state, transaction_type;
```

---

### 5. `HAVING`

Teach:

> `WHERE` filters individual rows.  
> `HAVING` filters grouped results.

Example:

```sql
SELECT
  state,
  SUM(amount_sdg) AS total_amount
FROM transactions
GROUP BY state
HAVING SUM(amount_sdg) > 1000000;
```

---

### 6. `CASE WHEN`

Map to spreadsheet `IF()`.

Spreadsheet:

```excel
=IF(F2>=100000,"High Value","Standard")
```

SQL:

```sql
CASE
  WHEN amount_sdg >= 100000 THEN 'High Value'
  ELSE 'Standard'
END
```

---

### 7. Creating Business Categories

Example:

```sql
CASE
  WHEN amount_sdg < 10000 THEN 'Low'
  WHEN amount_sdg < 100000 THEN 'Medium'
  ELSE 'High'
END AS transaction_band
```

---

### 8. Dates — Gentle Introduction

Teach only essential date concepts.

Depending on platform:

- Extract year
- Extract month
- Group by month

Keep syntax examples platform-appropriate during live practice.

The conceptual goal is:

> “How do I summarize behavior over time?”

---

# 8. Day 2 Practical Exercise
## Sudanese Telecom Customer Usage

Use a fictional telecom dataset inspired by mobile service usage.

Table:

```text
telecom_usage
```

Columns:

```text
usage_id
customer_id
usage_date
state
customer_segment
service_type
usage_units
revenue_sdg
```

Possible `service_type` values:

```text
Voice
SMS
Mobile Data
Mobile Money
```

### Student Tasks

Write queries to answer:

1. How many usage records exist?
2. What is total revenue?
3. What is average revenue per usage record?
4. Which service type generates the most revenue?
5. Which state generates the highest total revenue?
6. Which customer segment has the highest average revenue?
7. Which states have total revenue above a specified threshold?
8. Create revenue bands using `CASE WHEN`.
9. Compare service type by state.

### Business Challenge

Ask:

> “Management wants to know where Mobile Data is strongest and where Voice still dominates.”

Students write a grouped query using:

- `state`
- `service_type`
- `SUM(revenue_sdg)`

---

# 9. Day 2 Exit Challenge

Students must answer:

> “Which 3 states generated the highest Mobile Data revenue?”

Expected concepts:

- `WHERE`
- `GROUP BY`
- `SUM`
- `ORDER BY`
- `LIMIT`

This combines Day 1 and Day 2 skills.

---

# 10. Day 3 — Demystifying JOINs
## Theme: Connecting Tables Without Fear

### Main Objective

Give JOINs a full, unhurried class.

Students should understand **why multiple tables exist**, how keys connect them, and what changes when they use different JOIN types.

The target outcome is not memorizing JOIN diagrams.

The target outcome is:

> **“I understand what records I am keeping and what records I might lose.”**

---

# 11. Start Day 3 With a Spreadsheet Problem

Show two sheets.

## Sheet A — Transactions

| transaction_id | customer_id | amount |
|---|---|---:|
| T001 | C01 | 50000 |
| T002 | C02 | 80000 |
| T003 | C03 | 30000 |

## Sheet B — Customers

| customer_id | customer_name | state |
|---|---|---|
| C01 | Ahmed | Red Sea |
| C02 | Sara | Kassala |
| C03 | Mona | Gedaref |

Ask:

> “If I want customer name and state beside every transaction, what would we do in Excel?”

Students will likely say:

> XLOOKUP / VLOOKUP.

Then say:

> **JOIN is the database version of the same idea.**

This should be the anchor concept.

---

# 12. Core Topics — Day 3

### 1. Why Databases Use Multiple Tables

Explain:

Instead of repeating customer information in every transaction:

```text
customer_name
phone
state
segment
```

we store the customer once and connect using:

```text
customer_id
```

Benefits:

- Less duplication
- Easier updates
- Cleaner structure
- Better consistency

---

### 2. Primary Key

Explain:

> A field that uniquely identifies a row.

Example:

```text
customer_id
```

---

### 3. Foreign Key

Explain:

> A field in another table that points back to the primary key.

Example:

```text
transactions.customer_id
```

---

### 4. `INNER JOIN`

Teach visually first.

Meaning:

> Keep only records where a match exists in both tables.

Example:

```sql
SELECT
  t.transaction_id,
  t.amount_sdg,
  c.customer_name,
  c.state
FROM transactions AS t
INNER JOIN customers AS c
  ON t.customer_id = c.customer_id;
```

---

### 5. `LEFT JOIN`

Meaning:

> Keep every record from the left table, even when no matching record exists on the right.

Example:

```sql
SELECT
  c.customer_id,
  c.customer_name,
  t.transaction_id
FROM customers AS c
LEFT JOIN transactions AS t
  ON c.customer_id = t.customer_id;
```

Use case:

> “Show me all customers — including customers who never made a transaction.”

---

### 6. What Can Go Wrong?

Teach common JOIN mistakes:

- Joining on the wrong field
- Duplicate keys
- Many-to-many duplication
- Missing matches
- Losing records unintentionally
- Not checking row counts

---

### 7. Table Aliases

Teach:

```sql
customers AS c
transactions AS t
```

to make longer queries readable.

---

### 8. JOIN + Aggregation

Example:

```sql
SELECT
  c.state,
  SUM(t.amount_sdg) AS total_amount
FROM customers AS c
JOIN transactions AS t
  ON c.customer_id = t.customer_id
GROUP BY c.state;
```

This is where students start to feel the power of relational analysis.

---

# 13. Day 3 Practical Exercise
## Sudanese Hospital Service Database

Use **synthetic, non-identifiable** data.

Three tables:

### `patients`

```text
patient_id
age_group
gender
state
```

### `visits`

```text
visit_id
patient_id
facility_id
visit_date
service_type
visit_status
```

### `facilities`

```text
facility_id
facility_name
state
facility_type
```

No names, phone numbers, or sensitive diagnosis details are required for the exercise.

### Student Tasks

1. Join `visits` to `patients`.
2. Show:
   - visit ID
   - patient age group
   - patient state
   - service type
3. Join `visits` to `facilities`.
4. Show facility name beside each visit.
5. Join all three tables.
6. Count visits by facility.
7. Count visits by age group.
8. Compare service type by facility.
9. Use a `LEFT JOIN` to identify facilities with zero visits, if present.

### Key Discussion

Ask:

> “What happens if one facility exists in the facilities table but has no visits?”

Then compare:

- `INNER JOIN`
- `LEFT JOIN`

Students should **see the missing row**, not just hear the definition.

---

# 14. JOIN Visual Teaching Model

Use three physical or visual cards:

### Card A — Customer

```text
C01 | Sara | Kassala
```

### Card B — Transaction

```text
T100 | C01 | 75,000
```

### Match Key

```text
C01
```

Then physically connect them.

Repeat with:

- a matched customer
- a customer with no transaction
- a transaction with an invalid customer ID

This makes JOIN behavior concrete.

---

# 15. Day 3 Exit Challenge

Ask:

> “Find all customers, including those who have never completed a transaction.”

Students must choose:

> `LEFT JOIN`

Then explain **why** before writing the query.

---

# 16. Day 4 — Subqueries, CTEs & Capstone Preparation
## Theme: Break Complex Questions Into Smaller Steps

### Main Objective

Teach students how to handle business questions that require more than one logical step.

The emphasis should be:

> **Think first, query second.**

---

# 17. Core Topics — Day 4

### 1. SQL Order of Thought

Teach students to translate:

> “Which customers spent more than the average customer?”

into steps:

1. Calculate spend per customer.
2. Calculate average customer spend.
3. Compare each customer with that average.

Only then write SQL.

---

### 2. Subqueries

Begin with a simple example:

```sql
SELECT *
FROM transactions
WHERE amount_sdg > (
  SELECT AVG(amount_sdg)
  FROM transactions
);
```

Explain:

> The inner query answers one question first.  
> The outer query uses that answer.

---

### 3. CTEs — `WITH`

Use CTEs for readability.

Example:

```sql
WITH customer_spend AS (
  SELECT
    customer_id,
    SUM(amount_sdg) AS total_spend
  FROM transactions
  GROUP BY customer_id
)

SELECT *
FROM customer_spend
ORDER BY total_spend DESC;
```

Explain:

> A CTE is like creating a temporary named result that we can query next.

### Spreadsheet Bridge

Think of:

> A helper sheet / intermediate table.

---

### 4. CTE + JOIN

Example structure:

```sql
WITH branch_sales AS (
  SELECT
    branch_id,
    SUM(amount_sdg) AS total_sales
  FROM transactions
  GROUP BY branch_id
)

SELECT
  b.branch_name,
  bs.total_sales
FROM branch_sales AS bs
JOIN branches AS b
  ON bs.branch_id = b.branch_id;
```

---

### 5. Ranking Logic Without Overloading

If appropriate, introduce only one window function as an optional challenge:

```sql
ROW_NUMBER()
```

or:

```sql
RANK()
```

Do not make window functions a core pass requirement.

---

### 6. Query Formatting

Teach students to format:

```sql
SELECT
  ...
FROM
  ...
JOIN
  ...
WHERE
  ...
GROUP BY
  ...
HAVING
  ...
ORDER BY
  ...
```

Readable SQL is easier to debug.

---

### 7. Debugging SQL

Teach students to check:

- commas
- quotes
- column names
- table names
- aliases
- parentheses
- `GROUP BY`
- JOIN condition

Use a debugging checklist instead of letting syntax errors feel mysterious.

---

### 8. Business Question → Query Plan

Before writing SQL, students fill in:

```text
Business question:
Tables needed:
Key to connect them:
Metric:
Filter:
Grouping:
Output needed:
```

This becomes the planning template for the final project.

---

# 18. Day 4 Practical Exercise
## Sudanese Banking Customer Activity

Use a fictional banking dataset inspired by everyday digital banking patterns.

Tables:

### `customers`

```text
customer_id
state
customer_segment
registration_date
```

### `accounts`

```text
account_id
customer_id
account_type
open_date
status
```

### `transactions`

```text
transaction_id
account_id
transaction_date
transaction_type
amount_sdg
channel
status
```

### Student Tasks

Write queries to answer:

1. Which customers have the highest total transaction value?
2. Which states have the highest average transaction amount?
3. Which customers have more than one active account?
4. Which customers have total transaction value above the average customer?
5. Which account types generate the highest total transaction volume?

Students should use combinations of:

- JOINs
- GROUP BY
- HAVING
- subquery or CTE
- ORDER BY

---

# 19. Day 4 Capstone Preparation Exercise

Give students a business question such as:

> “Which customer segments are most valuable, and which channels do they use most?”

Before writing SQL, they must write the logical plan:

```text
1. Join customers → accounts
2. Join accounts → transactions
3. Filter successful transactions
4. Group by customer segment and channel
5. Calculate total value and transaction count
6. Rank or sort results
```

Only then write the query.

---

# 20. Mini-Portfolio Project
# Project 02 — Sudan Digital Banking Customer Intelligence

## Business Scenario

Students act as junior data analysts for a fictional Sudanese digital bank:

> **NileBank Digital**

The bank wants to understand customer activity, account usage, and transaction behavior.

Management asks:

> **“Who are our most active customers, which account types and channels matter most, and where should we focus our digital banking strategy?”**

Students will use **Google BigQuery Sandbox** to query a relational database.

The project is intentionally designed to require:

- filtering
- aggregation
- JOINs
- business logic
- subqueries or CTEs

---

# 21. Final Project Database Schema

The project uses **three related tables**.

---

## Table 1 — `customers`

One row = one customer.

```text
customer_id           STRING
state                 STRING
customer_segment      STRING
registration_date     DATE
age_group             STRING
preferred_language    STRING
```

Example `customer_segment` values:

```text
Individual
Student
Small Business
Professional
```

---

## Table 2 — `accounts`

One row = one bank account.

```text
account_id            STRING
customer_id           STRING
account_type          STRING
open_date             DATE
account_status        STRING
```

Example `account_type` values:

```text
Current
Savings
Mobile Wallet
Business
```

Relationship:

```text
customers.customer_id
        ↓
accounts.customer_id
```

One customer may have multiple accounts.

---

## Table 3 — `transactions`

One row = one transaction.

```text
transaction_id        STRING
account_id            STRING
transaction_date      DATE
transaction_type      STRING
channel               STRING
amount_sdg            NUMERIC
transaction_status    STRING
```

Example `transaction_type` values:

```text
Transfer
Bill Payment
Merchant Payment
Cash In
Cash Out
Airtime
```

Example `channel` values:

```text
Mobile App
USSD
Agent
ATM
Merchant
```

Relationship:

```text
accounts.account_id
        ↓
transactions.account_id
```

---

# 22. Relationship Diagram

```text
CUSTOMERS
---------
customer_id  PK
state
segment
...
     |
     | 1-to-many
     v

ACCOUNTS
--------
account_id   PK
customer_id  FK
account_type
...
     |
     | 1-to-many
     v

TRANSACTIONS
------------
transaction_id PK
account_id     FK
amount_sdg
channel
...
```

Students should understand this diagram before writing the final queries.

---

# 23. Final Project Business Questions

Students must answer **five required business questions**.

---

## Question 1 — Customer Value

> **Which 10 customers generated the highest total value of successful transactions?**

Required concepts:

- JOIN all three tables
- Filter successful transactions
- `SUM`
- `GROUP BY`
- `ORDER BY`
- `LIMIT`

Expected output may include:

```text
customer_id
state
customer_segment
total_transaction_value
transaction_count
```

---

## Question 2 — Digital Channel Performance

> **Which digital channel generates the highest successful transaction value, and how does this differ by customer segment?**

Required concepts:

- JOINs
- `WHERE`
- `GROUP BY`
- `SUM`
- segment + channel comparison

Students should distinguish:

- transaction count
- total transaction value

---

## Question 3 — High-Value Customers vs the Average

> **Which customers have total successful transaction value above the average total value per customer?**

Required concepts:

- CTE or subquery
- customer-level aggregation
- average of aggregated customer values
- comparison

This is the main multi-step logic question.

---

## Question 4 — Account Type Performance

> **Which account type produces the highest average transaction value and the highest total transaction value?**

Required concepts:

- JOIN `accounts` to `transactions`
- `AVG`
- `SUM`
- `GROUP BY`

Students must explain why:

> “highest average”

and:

> “highest total”

are different business questions.

---

## Question 5 — Market Opportunity by State

> **Which states have many registered customers but relatively low successful digital transaction activity?**

Required concepts:

- JOINs
- customer count
- transaction count or transaction value
- `LEFT JOIN`
- aggregation
- business interpretation

This should be treated as an **opportunity analysis**, not merely a ranking.

Students may calculate:

```text
registered_customers
active_transacting_customers
successful_transaction_count
successful_transaction_value
```

Then identify states where:

> customer base is large, but digital activity is relatively low.

---

# 24. Project Deliverables

Students submit:

## Deliverable 1 — SQL Script

One `.sql` file containing:

- Clear comments
- Five required queries
- Meaningful aliases
- Consistent formatting

Example:

```sql
-- Question 1: Top 10 customers by successful transaction value

SELECT
  ...
```

---

## Deliverable 2 — BigQuery Evidence

Students provide one of:

- Saved query links where practical
- Screenshots of query results
- Exported results
- PDF / document showing outputs

The instructor should specify the exact submission method before project week.

---

## Deliverable 3 — Business Answer Sheet

For each business question, students write:

### Query Result

What did the query return?

### Insight

What does it mean?

### Business Interpretation

Why should management care?

Maximum:

**2–4 sentences per question**

---

## Deliverable 4 — Query Explanation

Students choose **two of their five queries** and explain them in plain language.

Example:

> “First I joined customers to accounts using customer_id. Then I joined accounts to transactions using account_id. I filtered only successful transactions, grouped the results by customer, calculated total value, and sorted from highest to lowest.”

This proves they understand the logic rather than copying syntax.

---

# 25. Suggested Portfolio Rubric

| Competency | Weight |
|---|---:|
| Correct use of `SELECT` / filters | 10% |
| Aggregations & `GROUP BY` | 15% |
| JOIN logic | 25% |
| Subquery / CTE logic | 15% |
| Query accuracy | 15% |
| Business interpretation | 10% |
| Readability / formatting | 5% |
| Explanation of logic | 5% |
| **Total** | **100%** |

### Suggested Pass Threshold

**70%**

---

# 26. Must-Pass Competencies

A student should not progress simply because some queries run.

They must demonstrate that they can:

- Write a correct basic `SELECT`.
- Filter data correctly.
- Aggregate and group correctly.
- Use at least one correct `INNER JOIN`.
- Use at least one correct `LEFT JOIN`.
- Explain the JOIN key.
- Use either a subquery or CTE correctly.
- Interpret a query result in business language.
- Avoid duplicated or misleading results caused by incorrect JOIN logic.

JOIN competence should be a required skill before progression.

---

# 27. Assessment Status

## PASS

Student demonstrates the required SQL competencies.

→ Progress to the Tableau module.

## REVISE

Student demonstrates partial mastery but has one or more important logic issues.

Examples:

- Query runs but JOIN duplicates rows incorrectly.
- `GROUP BY` is incorrect.
- Uses `WHERE` when `HAVING` is required.
- Correct output but cannot explain the query logic.
- Business interpretation does not match the result.

→ Student receives targeted feedback and resubmits.

## INCOMPLETE

Required work was not submitted.

→ Student cannot progress until module requirements are resolved.

---

# 28. Teaching Tip 1 — Separate Logic Errors From Syntax Errors

Beginners often think every red error message means:

> “I don't understand SQL.”

Teach two categories:

## Syntax Problem

SQL cannot understand what you wrote.

Examples:

- Missing comma
- Misspelled keyword
- Unclosed quote

## Logic Problem

The query runs, but answers the wrong question.

Examples:

- Wrong filter
- Wrong JOIN key
- Wrong aggregation

Tell students:

> **A query that runs is not automatically a correct query.**

This prevents students from treating “no error message” as the definition of success.

---

# 29. Teaching Tip 2 — Use a Query Translation Habit

Before students type SQL, make them say the question in ordinary language.

Example:

> “Show total successful transfer value by state, highest first.”

Then translate:

```text
Show → SELECT
from transactions → FROM
successful transfers → WHERE
by state → GROUP BY
total value → SUM
highest first → ORDER BY DESC
```

Then write SQL.

This reduces syntax frustration because they are not inventing logic and syntax simultaneously.

---

# 30. Teaching Tip 3 — Teach JOINs Physically Before Coding Them

Do not begin JOIN class with:

```sql
SELECT ...
FROM ...
INNER JOIN ...
```

Begin with two printed tables, cards, sticky notes, or objects.

Example:

## Customers

```text
C01 Ahmed
C02 Sara
C03 Mona
```

## Transactions

```text
T01 C01 50000
T02 C01 30000
T03 C03 70000
```

Ask students to physically match IDs.

Then ask:

> “What happens to C02?”

Now explain:

### INNER JOIN

C02 disappears because there is no match.

### LEFT JOIN from Customers

C02 remains, but transaction fields are empty.

Only after this should students write the SQL.

---

# 31. Additional Pedagogical Rule
## One New Concept Per Query

For beginners, do not introduce:

```text
JOIN + CASE + GROUP BY + HAVING + subquery
```

all at once.

Build progressively.

Example:

### Step 1

JOIN two tables.

### Step 2

Add a filter.

### Step 3

Add aggregation.

### Step 4

Add grouping.

### Step 5

Add business logic.

This allows students to identify exactly where a query breaks.

---

# 32. Debugging Checklist

Before asking the instructor for help, students check:

### Structure

- Did I write `SELECT`?
- Did I write `FROM`?
- Is the table name correct?

### Columns

- Is the column name correct?
- Does the column belong to this table?
- Do I need the table alias?

### Text

- Did I use quotes around text values?

### Commas

- Are columns separated correctly?

### Aggregation

- Am I using `GROUP BY` correctly?
- Should this condition be in `WHERE` or `HAVING`?

### JOIN

- Which two fields am I connecting?
- Are they actually the same key?
- Am I using `INNER JOIN` or `LEFT JOIN` intentionally?

### Result

- Does the row count make sense?
- Did the query answer the business question?

---

# 33. Recommended Live-Class Rhythm

Use:

**Question → Predict → Write Together → Run → Read Result → Modify → Solve Alone**

Example:

### 10 min
Introduce the business question

### 10 min
Translate the question into SQL logic

### 15 min
Build the query together

### 10 min
Run and inspect the result

### 15 min
Students modify the query

### 20 min
Students solve a new version alone

### 10 min
Discuss common errors

This keeps syntax connected to meaning.

---

# 34. What We Deliberately Do Not Teach in Module 2

Avoid overloading beginners with:

- Database administration
- Creating production databases
- Indexing
- Query optimization
- Stored procedures
- Triggers
- Transactions / ACID theory in depth
- Complex recursive CTEs
- Advanced window functions
- Advanced date manipulation
- Complex data warehousing
- Database normalization theory in depth

Optional stretch topics may include:

- `RANK()`
- `ROW_NUMBER()`

but these should not be required for passing.

The goal is not:

> **Become a database engineer in four classes.**

The goal is:

> **Become confident enough to extract, combine, summarize, and explain the data needed for analysis.**

---

# 35. End-to-End SQL Workflow

Students should internalize:

**Business Question**  
↓  
**Which Tables?**  
↓  
**Which Columns?**  
↓  
**How Are the Tables Connected?**  
↓  
**Which Rows Do I Need?**  
↓  
**Do I Need Aggregation?**  
↓  
**Do I Need Grouping?**  
↓  
**Do I Need Multiple Steps?**  
↓  
**Write Query**  
↓  
**Run**  
↓  
**Check Row Count / Logic**  
↓  
**Interpret Result**  
↓  
**Answer the Business Question**

---

# 36. Final Module Mindset

By the end of the module, students should stop asking:

> “What SQL command do I use?”

and begin asking:

> **What question am I answering?**

> **Where does the data live?**

> **Which rows and columns do I need?**

> **How are the tables related?**

> **Am I summarizing or looking at individual records?**

> **Could this JOIN be duplicating data?**

> **Does the result actually make sense?**

---

# 37. Module Summary

**Module:** Data Extraction with SQL  
**Duration:** 4 intensive classes  
**Teaching Style:** Beginner-friendly, Excel-to-SQL mapping, highly practical  
**Practice Environment:** Browser-based SQL editor  
**Final Project:** Google BigQuery Sandbox  
**Main Themes:** `SELECT`, filtering, aggregation, `GROUP BY`, `CASE WHEN`, JOINs, subqueries, CTEs, business interpretation  
**Portfolio Output:** SQL script + BigQuery query evidence + business answer sheet + plain-language query explanation  
**Progression Standard:** Mastery before progression  
**Primary Goal:** Teach students to retrieve, connect, summarize, and interpret relational data confidently.

> **The student should leave this module able to say: “I can take a business question, identify the tables I need, write the SQL to answer it, and explain what the result means.”**
