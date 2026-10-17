# Module 1 — Data Analysis with Spreadsheets
## Excel / Google Sheets

**Level:** Absolute Beginner  
**Format:** 3 intensive classes — Friday, Saturday, Sunday  
**Application Week:** 1 week after the live classes  
**Module Outcome:** One portfolio-ready spreadsheet analysis project  
**Recommended live class length:** 3–3.5 hours per day  
**Teaching approach:** Approximately **20–30% explanation / 70–80% hands-on practice**

The goal of this first module is **not** to teach students everything in Excel.

By Sunday, a successful beginner should be able to say:

> **“Give me a messy spreadsheet and a business question. I can clean the data, calculate useful metrics, summarize it, visualize it, and explain what I found.”**

This module builds the analytical foundation required before moving to SQL.

---

# 1. Module Learning Outcomes

By the end of the weekend, students should be able to:

- Understand rows, columns, records, variables, and data types.
- Navigate Excel or Google Sheets confidently.
- Identify common data-quality problems.
- Clean a simple real-world dataset.
- Use basic and conditional formulas.
- Calculate common business metrics.
- Use sorting, filtering, and conditional formatting.
- Summarize data using Pivot Tables.
- Create appropriate charts.
- Build a simple one-page dashboard.
- Write short, evidence-based insights from the data.
- Distinguish between **what the data shows** and **what they are guessing**.

A core analytical principle throughout the module is:

> **Guess → Question → Test with Data → Evidence → Conclusion**

---

# 2. Overall Weekend Journey

| Day | Student Mindset |
|---|---|
| **Friday** | “I understand spreadsheets and can work with data.” |
| **Saturday** | “I can clean and analyze data.” |
| **Sunday** | “I can turn analysis into a dashboard and business insights.” |

**Friday → Follow me**  
**Saturday → Try with me**  
**Sunday → Solve it yourself**

---

# 3. Class 1 — Friday
## Spreadsheet Foundations: From Raw Data to Useful Data

### Main Objective

Remove fear of spreadsheets and teach students how to **think about structured data** before introducing more complicated formulas.

Students should leave thinking:

> “Excel/Sheets isn't scary. I understand what I'm looking at.”

## Part 1 — What Is a Spreadsheet Actually Doing?

Start from concepts already introduced in Data Literacy:

- Dataset
- Row
- Column
- Observation / record
- Variable / field
- Header
- Data type
- Missing value
- Unique ID

### Demonstration Dataset

| transaction_id | date | city | product | quantity | unit_price |
|---|---|---|---|---:|---:|
| T001 | 2026-09-01 | Port Sudan | Sugar | 3 | 2500 |
| T002 | 2026-09-01 | Kassala | Oil | 2 | 5000 |
| T003 | 2026-09-02 | Port Sudan | Flour | 5 | 1800 |

Ask:

- What does one row represent?
- Which columns are numerical?
- Which are categorical?
- Which could contain missing values?
- Which column should uniquely identify a transaction?

## Part 2 — Spreadsheet Navigation

### Core Topics

- Workbook vs worksheet
- Rows and columns
- Cells
- Cell references
- Selecting ranges
- Copy / paste
- Fill handle
- Freeze rows
- Resize columns
- Undo / redo
- Find and replace
- Sorting
- Filtering
- Basic formatting

Do not spend too long on formatting. The goal is **data work**, not decorative spreadsheets.

## Part 3 — First Formulas

Introduce formulas as ways to answer questions.

Instead of:

> “Today we're learning the SUM function.”

Say:

> “Management wants to know how much money was collected.”

### Functions

```text
SUM
AVERAGE
MIN
MAX
COUNT
COUNTA
```

Basic arithmetic:

```text
=B2*C2
```

Example:

**Revenue = Quantity × Unit Price**

Introduce:

- Relative cell references
- Absolute references

Example:

```text
=B2*$H$2
```

where H2 contains a fixed tax, exchange rate, or commission.

---

# 4. Friday Practical Exercise
## Sudanese Market Price Tracker

Give students a small **synthetic dataset** of commodity prices from several Sudanese markets.

| date | market | state | commodity | unit | price_sdg |
|---|---|---|---|---|---:|
| 2026-08-01 | Market A | Red Sea | Sorghum | kg | 2200 |
| 2026-08-01 | Market B | Kassala | Sorghum | kg | 2050 |
| 2026-08-01 | Market C | Gedaref | Sesame | kg | 4700 |

### Students Must Answer

1. What is the highest commodity price?
2. What is the lowest?
3. What is the average?
4. How many price observations exist?
5. Sort from highest to lowest price.
6. Filter only one commodity.
7. Filter only one location.
8. Create a new column calculating hypothetical purchase cost:

```text
Quantity × Price
```

### End-of-Class Challenge

Ask:

> “Which market looks cheapest?”

Then ask:

> “Cheapest for what commodity?”

This reinforces analytical thinking and context.

## Friday Exit Challenge

Give students five minutes individually.

Ask them to:

- Filter one category.
- Calculate total value.
- Identify the highest value.
- Write one sentence describing what they found.

---

# 5. Class 2 — Saturday
## Cleaning & Analyzing Real-World Data

### Main Objective

Students learn that most data analysis does **not** begin with charts. It begins with making messy data trustworthy enough to analyze.

## Part 1 — What Does Messy Data Look Like?

| city | service | amount | date |
|---|---|---:|---|
| Port Sudan | Mobile Data | 5000 | 01/09/26 |
| port sudan | mobile data | 5,000 | 1 Sept 2026 |
| PORTSUDAN | Mobile_Data |  | 2026-09-01 |
| Kassala | Voice | 0 | Sept 2 |

Ask:

> Can we analyze this immediately?

## Part 2 — Data Cleaning

### Missing Values

Discuss:

- Blank
- Zero
- Not applicable
- Unknown

Reinforce:

> **Missing does not automatically mean zero.**

### Duplicates

Teach:

- Finding duplicate records
- Removing duplicates carefully
- Why duplicates matter

### Inconsistent Categories

Examples:

```text
Port Sudan
port sudan
PORT SUDAN
Port-Sudan
```

Teach:

- Find & Replace
- `TRIM`
- Basic case standardization
- Standard category lists

### Dates

Teach:

- Why dates sometimes behave like text
- Consistent date formats
- Sorting by date
- Basic extraction of month/year

Possible functions:

```text
YEAR()
MONTH()
```

## Part 3 — Conditional Logic

Introduce:

```text
IF
```

Example:

```excel
=IF(F2>=10000,"High Value","Standard")
```

Ask:

> “Management wants transactions above SDG 10,000 labeled High Value. How do we automate that?”

## Part 4 — Conditional Aggregation

Introduce:

```text
COUNTIF
COUNTIFS
SUMIF
SUMIFS
```

Use business questions:

- How many customers are from Port Sudan?
- How much revenue came from Kassala?
- How much revenue came from Port Sudan for Product A?

## Part 5 — Lookup Concept

Teach **one lookup concept**, preferably:

```text
XLOOKUP
```

where available.

Explain `VLOOKUP` briefly only if compatibility requires it.

Example:

| product_id | product | category |
|---|---|---|

and:

| transaction_id | product_id | quantity |
|---|---|---:|

Students retrieve product name or category.

Explain:

> “Today you're connecting tables with XLOOKUP. Later we'll do the same idea using SQL JOIN.”

---

# 6. Saturday Practical Exercise
## Sudanese Telecom Recharge Data

Give students intentionally messy **synthetic mobile recharge/customer transaction data**.

Columns:

```text
transaction_id
date
state
customer_type
service_type
recharge_amount
channel
agent_id
```

Include realistic problems:

- `Port Sudan`
- `port sudan`
- Missing recharge values
- Duplicate transaction
- Different date formats
- Extra spaces
- `Mobile Data`
- `mobile data`
- Blank customer types

### Students Must

1. Identify data-quality issues.
2. Remove duplicate records.
3. Standardize categories.
4. Decide what to do with missing values.
5. Create `Recharge_Band` using `IF`.
6. Calculate total recharge amount.
7. Calculate average recharge.
8. Calculate value by state using `SUMIF/S`.
9. Count transactions by service type using `COUNTIF/S`.
10. Write **two observations supported by the data**.

## Important Teaching Moment

Ask:

> “Why is mobile data usage higher in this location?”

If a student gives a reason, ask:

> “Do we actually have data proving that?”

### Observation

> Mobile-data transactions are higher in Location A.

### Possible Hypothesis

> This may be related to customer demographics, network availability, pricing, or another factor.

### Unsupported Conclusion

> People there prefer mobile data because they are younger.

---

# 7. Class 3 — Sunday
## From Data to Decisions: Pivot Tables, Charts & Dashboard

### Main Objective

Students learn to turn cleaned data into something **a manager or decision-maker can understand quickly**.

## Part 1 — Asking Questions Before Making Charts

A Sudanese NGO asks:

- How many beneficiaries did we serve?
- Which locations received the most support?
- Which services were requested most?
- Is participation increasing or decreasing?
- Which locations may need more attention?

Then ask:

> What information do we need to calculate?

## Part 2 — Pivot Tables

### Core Topics

- Rows
- Columns
- Values
- Filters

Explain:

> A Pivot Table is a fast way of grouping and summarizing data.

### Revenue by Branch

```text
Rows: Branch
Values: Sum of Revenue
```

### Transactions by Product

```text
Rows: Product
Values: Count of Transaction ID
```

### Monthly Revenue

```text
Rows: Month
Values: Sum of Revenue
```

### Product × Branch

```text
Rows: Product
Columns: Branch
Values: Sum of Revenue
```

## Part 3 — KPIs

Examples:

- Total Revenue
- Total Transactions
- Average Transaction Value
- Highest Performing Branch
- Best Selling Category

Explain:

> KPI = a number that helps us monitor something important.

## Part 4 — Charts

### Bar Chart

Use for **comparing categories**.

### Line Chart

Use for **change over time**.

### Pie / Donut Chart

Can occasionally show simple composition, but should be used sparingly.

### Avoid for Now

- Complex statistical charts
- 3D charts
- Gauge charts
- Excessive colors
- Decorative charts without a question

## Part 5 — Dashboard Design

```text
-----------------------------------
| KPI | KPI | KPI | KPI           |
-----------------------------------
| Revenue Trend                    |
-----------------------------------
| Sales by Branch | Sales by Type |
-----------------------------------
| Filters                          |
-----------------------------------
```

Teach:

- Clear title
- Consistent formatting
- 3–5 KPIs maximum
- 2–4 useful charts
- Avoid clutter
- Label clearly
- Make important information visually obvious

---

# 8. Sunday Practical Exercise
## Sudanese NGO Programme Dashboard

Give students a synthetic dataset for a fictional NGO delivering community programmes.

Columns:

```text
participant_id
registration_date
state
programme
gender
age_group
attendance_count
completion_status
support_type
```

### Students Build

#### KPIs

- Total participants
- Completion rate
- Average attendance
- Most common programme

#### Pivot Tables

- Participants by state
- Participants by programme
- Completion by programme
- Monthly registrations

#### Charts

- Bar chart: participants by programme
- Line chart: registration trend
- Bar chart: completion by location

### Final Task

Write:

- **3 findings**
- **1 recommendation**

---

# 9. Insight ≠ Description

### Weak

> “Port Sudan has 450 participants.”

That is a number.

### Better

> “Port Sudan represents 38% of all recorded participants, making it the largest programme location.”

That is an observation.

### Stronger

> “Port Sudan represents 38% of participants but has a lower completion rate than the programme average. Programme managers should investigate barriers to completion before expanding enrollment.”

That is an **actionable insight**.

---

# 10. Mini-Portfolio Project
# Project 01 — Sudan Community Pharmacy Performance Analysis

The first portfolio project combines **business, inventory, operational, and financial analysis** while remaining relevant to much of the cohort.

The business is fictional to avoid privacy and confidentiality concerns.

## Business Scenario

Students become junior analysts for:

> **NileCare Community Pharmacies**

A fictional Sudanese pharmacy and health-supplies business with several branches.

Management asks:

> “What is happening in our business, which products and branches are performing well, and what should we pay attention to?”

Students have one week to answer.

---

# 11. Raw Data Provided

Give students approximately **500–1,000 rows**.

### Dataset Columns

```text
transaction_id
transaction_date
branch
state
product_id
product_name
category
quantity
unit_price_sdg
unit_cost_sdg
payment_method
customer_type
stock_remaining
```

Possible categories:

```text
OTC Medicines
Personal Care
First Aid
Baby Care
Vitamins
Medical Supplies
```

Avoid real prescription or patient information.

---

# 12. Controlled Data Problems to Include

### Inconsistent Branch Names

```text
Port Sudan
port sudan
Port-Sudan
```

### Category Inconsistency

```text
First Aid
first aid
FirstAid
```

### Missing Values

Examples:

```text
customer_type
stock_remaining
```

### Duplicate Rows

Add approximately 5–10 duplicates.

### Dates

Use a few inconsistent date formats.

### Extra Spaces

```text
" Vitamins "
```

Do **not** make the dataset excessively dirty. The challenge should come from applying the workflow, not surviving chaos.

---

# 13. Calculated Columns Students Must Create

### Revenue

```text
Revenue = Quantity × Unit Price
```

### Cost

```text
Cost = Quantity × Unit Cost
```

### Gross Profit

```text
Gross Profit = Revenue - Cost
```

### Profit Margin

```text
Profit Margin = Gross Profit / Revenue
```

### Optional — Transaction Value Category

Using `IF`:

```text
Low
Medium
High
```

---

# 14. Questions Management Wants Answered

Students should answer at least:

1. What is total revenue?
2. What is total gross profit?
3. Which branch generates the highest revenue?
4. Which branch generates the highest profit?
5. Which product category generates the most revenue?
6. Which products sell the highest quantity?
7. Which products appear to have low stock?
8. What is the average transaction value?
9. Which payment methods are most commonly used?
10. How do sales change over time?

Then ask:

> **What else did you discover that management did not explicitly ask?**

---

# 15. Exact Student Deliverables

Students submit **one spreadsheet workbook**.

## Sheet 1 — `README`

Students write:

- Student name / ID
- Project title
- Short description
- What one row represents
- Known assumptions
- Important cleaning decisions

## Sheet 2 — `RAW_DATA`

Original data.

> **Do not modify this sheet.**

## Sheet 3 — `CLEAN_DATA`

Students must demonstrate:

- Consistent categories
- Correct dates
- Duplicate handling
- Missing-value handling
- Calculated fields

## Sheet 4 — `ANALYSIS`

Contains:

- Formulas
- Summary tables
- Pivot Tables
- KPI calculations

## Sheet 5 — `DASHBOARD`

Must contain:

### At Least 4 KPIs

For example:

- Total Revenue
- Gross Profit
- Number of Transactions
- Average Transaction Value

### At Least 3 Charts

For example:

- Revenue by branch
- Revenue by category
- Sales trend over time

### At Least One Filter / Slicer

If supported.

## Sheet 6 — `INSIGHTS`

Students write:

### 3 Data Insights

Every insight must contain:

**Evidence + Interpretation**

Example:

> Branch A generated 31% of total revenue but only 22% of total profit, suggesting its product mix may contain lower-margin items.

Avoid unsupported conclusions such as:

> Branch A needs better management.

### 1 Business Recommendation

Example:

> Management should review stock levels for the five highest-selling products because three are currently among the lowest-stock items.

The recommendation must connect directly to evidence.

---

# 16. Pass Criteria

## Suggested Rubric

| Competency | Weight |
|---|---:|
| Data cleaning | 20% |
| Formula accuracy | 20% |
| Pivot Tables / analysis | 20% |
| Dashboard & charts | 15% |
| Insights & interpretation | 15% |
| Documentation & organization | 10% |
| **Total** | **100%** |

### Suggested Pass Threshold

**70%+**

Students must also demonstrate key must-pass skills:

- Preserve raw data.
- Clean obvious problems.
- Calculate revenue correctly.
- Build at least one correct Pivot Table.
- Produce at least one meaningful chart.
- Write at least one evidence-supported insight.

---

# 17. Assessment Status

## PASS

Student demonstrates the required competencies.

→ Progress to SQL.

## REVISE

The foundation is there, but some competencies are missing.

→ Student receives specific feedback and resubmits.

## INCOMPLETE

Required work was not submitted.

→ Student cannot progress until the requirement is resolved according to bootcamp rules.

The objective is to identify **which competency is missing**, not simply assign a failing percentage.

---

# 18. Suggested Live-Class Rhythm

For adult absolute beginners, avoid speaking for more than approximately 20–25 minutes continuously.

Use:

**Explain → Demonstrate → Students Copy → Students Modify → Students Solve Alone**

Example:

- 15 min — Explain `SUMIF`
- 10 min — Instructor demonstration
- 15 min — Students reproduce it
- 15 min — Students solve a slightly different problem
- 10 min — Discuss mistakes

---

# 19. Teaching Tips

## Tip 1 — Teach Questions, Not Functions

Do not say:

> “Today we'll study SUMIFS syntax.”

Start with:

> “The manager wants to know how much revenue came from Port Sudan from Medical Supplies only.”

Then ask:

> “How can we ask the spreadsheet this question?”

This changes the student's mental model from memorizing formulas to using formulas as tools.

## Tip 2 — Normalize Errors Immediately

Absolute beginners often see:

```text
#VALUE!
#N/A
#DIV/0!
```

and think:

> “I'm bad at this.”

Teach:

> **Errors are information.**

Ask:

1. What is Excel telling us?
2. Which part of the formula might be wrong?
3. What should we inspect?

## Tip 3 — Do Not Let the Fastest Students Set the Pace

Use optional challenges.

### Core Task

Calculate revenue by branch.

### Challenge

Find the highest-margin product within each branch.

---

# 20. Teaching Progression Rule

Use this progression:

### First Demonstration

Tiny clean dataset.

### Guided Practice

Slightly messy dataset.

### Independent Exercise

Realistic messy dataset.

### Portfolio Project

Student decides what steps are necessary.

By project week, stop giving procedural instructions such as:

1. Remove duplicates.
2. Fix categories.
3. Create a Pivot Table.

Instead tell them:

> **Management gave you this dataset and these questions. Prepare the data and answer them.**

That is the difference between following an Excel tutorial and becoming an analyst.

---

# 21. What We Deliberately Do Not Teach in Module 1

Leave these out:

- VBA / macros
- Power Query
- Power Pivot
- Complex nested formulas
- Advanced financial formulas
- Advanced array formulas
- Solver
- Complex statistical analysis
- Advanced dashboard techniques
- Dozens of chart types

The objective is not:

> **Become an Excel expert in three days.**

It is:

> **Build the analytical foundation required for the rest of the bootcamp.**

---

# 22. End-to-End Workflow

By Sunday, students should understand this workflow:

**Question**  
↓  
**Raw Data**  
↓  
**Inspect**  
↓  
**Clean**  
↓  
**Calculate**  
↓  
**Summarize**  
↓  
**Visualize**  
↓  
**Interpret**  
↓  
**Recommend**

This same workflow will reappear in:

- SQL
- Tableau
- Applied Statistics
- Python
- Final Capstone
