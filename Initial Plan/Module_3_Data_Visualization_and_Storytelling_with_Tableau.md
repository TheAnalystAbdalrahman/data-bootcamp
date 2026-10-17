# Module 3 — Data Visualization and Storytelling with Tableau
## 4-Class Practical Masterclass

**Audience:** Non-technical learners with basic Spreadsheet and SQL skills  
**Format:** 4 intensive live classes  
**Primary Focus:** Visual communication, business intelligence, dashboard design, and executive storytelling  
**Tool:** Tableau Public / Tableau Desktop Public Edition where appropriate  
**Context:** Sudanese business, NGO, agriculture, economic, and service-delivery scenarios  
**Assessment:** One portfolio-ready interactive dashboard + executive presentation  
**Teaching Approach:** Approximately **20–25% explanation / 75–80% hands-on work**

---

# 1. Module Philosophy

This module is not about producing the largest number of charts.

The purpose is to teach students how to answer:

> **“What does the decision-maker need to understand, and what is the clearest visual way to show it?”**

Students should move from:

> “I can make a chart.”

to:

> **“I can design an interactive dashboard that helps someone make a decision.”**

The module should reinforce the analytical habits already built in Spreadsheets and SQL:

**Question → Data → Analysis → Visual → Insight → Decision**

---

# 2. Module Learning Outcomes

By the end of the four classes, students should be able to:

- Connect Tableau to CSV, Excel, and simple tabular datasets.
- Understand Tableau’s interface and workflow.
- Distinguish dimensions from measures.
- Build appropriate basic charts.
- Use filters, sorting, highlighting, and grouping.
- Create calculated fields.
- Create basic table calculations.
- Work with dates and time trends.
- Create geographic maps responsibly.
- Build KPI cards and summary views.
- Combine multiple worksheets into an interactive dashboard.
- Use dashboard actions and filters.
- Apply visual hierarchy and layout principles.
- Avoid clutter, misleading scales, and unnecessary decoration.
- Write meaningful chart titles and annotations.
- Build an executive data story.
- Present dashboard findings to a non-technical audience.
- Distinguish between **description, insight, and recommendation**.
- Publish a portfolio-ready visualization using non-sensitive/public or synthetic data.

---

# 3. Overall 4-Day Learning Journey

| Day | Theme | Student Mindset |
|---|---|---|
| **Day 1** | Tableau Foundations & Basic Visuals | “I can connect data and build the right basic chart.” |
| **Day 2** | Analytical Visuals & Calculated Fields | “I can create deeper analysis, not just pretty charts.” |
| **Day 3** | Dashboard Design & Interactivity | “I can combine views into a useful decision tool.” |
| **Day 4** | Data Storytelling & Executive Presentation | “I can explain what matters, why it matters, and what should happen next.” |

**Build → Analyze → Design → Communicate**

---

# 4. Day 1 — Tableau Foundations & Visual Thinking
## Theme: From Data Table to Useful Visual

### Main Objective

Help students become comfortable with Tableau’s interface while teaching the principle that **chart choice must come from the analytical question**.

Students should leave Day 1 able to connect a dataset, understand the main Tableau workspace, and build several clean basic visualizations.

## Core Topics

### 1. What Is Business Intelligence?

> Business Intelligence is the process of turning operational data into information people can use to monitor performance and make decisions.

Examples:

- A retailer monitoring branch sales
- An NGO monitoring programme coverage
- A telecom company tracking customer activity
- A hospital monitoring service utilization
- An agriculture programme tracking production by state

### 2. Tableau Workflow

**Connect → Explore → Build Worksheets → Combine into Dashboard → Communicate**

Introduce:

- Data Source page
- Worksheet
- Dashboard
- Story
- Shelves
- Marks card
- Show Me
- Filters
- Pages
- Data pane

### 3. Connecting Data

Students connect:

- CSV
- Excel
- Simple flat tables

Explain:

- Field names
- Data types
- Dates
- Geographic roles
- Numbers stored as text
- Why clean data still matters

> Tableau does not magically fix poor data quality.

### 4. Dimensions vs Measures

### Dimension

A field used to **categorize or group**.

Examples:

- State
- Product
- Branch
- Programme
- Customer segment

### Measure

A field we often **calculate or aggregate**.

Examples:

- Revenue
- Quantity
- Beneficiaries
- Cost
- Profit

Ask:

> “Do we want to group BY it, or calculate WITH it?”

### 5. Aggregation

Introduce:

- SUM
- AVG
- COUNT
- COUNTD
- MIN
- MAX

### 6. Core Charts

#### Bar Chart
Best for comparing categories.

#### Line Chart
Best for trends over time.

#### Highlight Table / Heatmap
Best for patterns across two categories.

#### Scatter Plot
For exploring relationships between two measures.

#### Map
For geographic patterns when geography is relevant.

### 7. Chart Choice

| Question | Good Starting Visual |
|---|---|
| Which category is largest? | Bar chart |
| How did something change over time? | Line chart |
| Where is something happening? | Map |
| Are two numeric measures related? | Scatter plot |
| Where are high/low combinations? | Heatmap / highlight table |

> **Do not start with “Which chart looks nice?” Start with “What question am I answering?”**

---

# 5. Day 1 Practical Exercise
## Sudan Cost-of-Living & Commodity Price Explorer

Use a synthetic or responsibly sourced public dataset representing commodity prices across Sudanese states or markets.

Suggested columns:

```text
date
state
market
commodity
unit
price_sdg
```

Possible commodities:

```text
Sorghum
Millet
Wheat
Sugar
Cooking Oil
Onions
Groundnuts
Sesame
```

### Students Build

1. Bar chart — average price by commodity
2. Line chart — monthly price trend
3. Bar chart — selected commodity by state
4. Simple map — average recorded price by state, if geographic fields resolve correctly
5. Filter — commodity
6. Filter — date

### Questions

- Which commodities have the highest recorded prices?
- Which commodities changed most over time?
- Are some locations consistently more expensive?
- What can the chart show?
- What can it **not** explain?

### Teaching Moment

> “If prices rose sharply in one state, can we conclude why?”

No.

Students should separate **pattern** from **explanation**.

---

# 6. Day 1 Exit Challenge

> “Management wants to compare three product categories across six branches. Which visual would you choose and why?”

Students answer:

1. Chart choice
2. Why
3. What they would avoid

---

# 7. Day 2 — Analytical Visuals, Calculated Fields & Deeper Questions
## Theme: Move Beyond Drag-and-Drop

### Main Objective

Teach students to use Tableau as an analytical tool rather than as chart-making software.

## Core Topics

### 1. Sorting & Filtering

- Sort ascending / descending
- Top N
- Categorical filters
- Date filters
- Measure filters

### 2. Groups

Use groups for combining similar categories.

Example:

Several small product types → **Other**

### 3. Sets — Beginner Introduction

> A way to separate members that meet a condition from those that do not.

Example:

**Top 10 Products vs All Other Products**

### 4. Calculated Fields

#### Profit

```text
SUM([Revenue]) - SUM([Cost])
```

#### Profit Margin

```text
(SUM([Revenue]) - SUM([Cost])) / SUM([Revenue])
```

#### Completion Rate

```text
SUM([Completed]) / COUNT([Participant ID])
```

#### Revenue per Transaction

```text
SUM([Revenue]) / COUNTD([Transaction ID])
```

### 5. IF Logic in Tableau

```text
IF [Profit Margin] >= 0.20 THEN "High Margin"
ELSE "Low Margin"
END
```

### 6. Date Analysis

Teach:

- Year
- Quarter
- Month
- Week
- Continuous vs discrete dates at an intuitive level

### 7. Table Calculations — Beginner Level

Introduce:

- Percent of total
- Running total
- Difference
- Percent difference

### 8. Reference Lines

Use:

- Average
- Target
- Threshold

### 9. Tooltips

Bad:

> SUM(Sales): 5462356

Better:

> Revenue: SDG 5.46M  
> Transactions: 428  
> Profit Margin: 18.2%

---

# 8. Day 2 Practical Exercise
## Sudanese FMCG Sales Performance

Students work with a fictional local FMCG distributor.

Suggested columns:

```text
transaction_id
date
branch
state
sales_rep
product
category
units_sold
revenue_sdg
cost_sdg
channel
```

### Students Create

1. Revenue by branch
2. Profit by category
3. Profit margin calculated field
4. Monthly sales trend
5. Top 10 products set
6. Percent of total revenue by category
7. Reference line for average branch revenue
8. Scatter plot — revenue vs profit
9. Filter by state and product category

### Business Questions

- Which branches generate the most revenue?
- Are the highest-revenue branches also the most profitable?
- Which categories have weak margins?
- Which products contribute disproportionately to revenue?
- Are there branches performing below average?

> **High sales do not automatically mean high profit.**

---

# 9. Day 2 Exit Challenge

### Branch A

Revenue: SDG 20M  
Profit: SDG 1.5M

### Branch B

Revenue: SDG 14M  
Profit: SDG 2.8M

Ask:

> “Which branch is performing better?”

Correct answer:

> **It depends on the decision question and metric.**

---

# 10. Day 3 — Dashboard Design & Interactivity
## Theme: Build a Decision Tool, Not a Poster

### Main Objective

Teach students how to combine multiple visualizations into one coherent, interactive dashboard.

## Core Topics

### 1. What Is a Dashboard?

> A dashboard is a collection of coordinated views designed to help a specific audience monitor, understand, or decide something.

It is **not** every chart placed on one page.

### 2. Define the Audience First

Possible audiences:

- CEO
- Programme manager
- Sales manager
- NGO coordinator
- Research lead
- Operations manager

Ask:

> What decisions do they need to make?

### 3. Dashboard Hierarchy

```text
---------------------------------------
| TITLE / CONTEXT                     |
---------------------------------------
| KPI | KPI | KPI | KPI               |
---------------------------------------
| PRIMARY TREND / MAIN QUESTION       |
---------------------------------------
| COMPARISON       | BREAKDOWN        |
---------------------------------------
| FILTERS / SUPPORTING DETAIL         |
---------------------------------------
```

### 4. KPI Cards

Examples:

- Total Revenue
- Profit
- Transactions
- Beneficiaries
- Completion Rate
- Average Price

Recommended:

**3–5 KPIs**

### 5. Visual Hierarchy

Teach:

- Most important information first
- Use whitespace
- Align related elements
- Minimize visual noise
- Use consistent labels
- Avoid unnecessary borders

### 6. Color

> Color should communicate meaning, not decorate.

Avoid:

- Rainbow palettes
- One unique color for every bar
- Decorative backgrounds

### 7. Dashboard Filters

Teach:

- Global filter
- Single-select filter
- Multi-select filter
- Date filter

### 8. Dashboard Actions

Introduce:

- Filter actions
- Highlight actions

### 9. Containers & Layout

Teach:

- Horizontal container
- Vertical container
- Tiled layout
- Floating objects only when needed

### 10. Device / Screen Awareness

Discuss:

- Desktop viewing
- Mobile limitations
- Large-screen presentation

---

# 11. Day 3 Practical Exercise
## NGO Aid Distribution Dashboard

Use a fictional Sudanese NGO programme dataset.

Suggested fields:

```text
distribution_id
date
state
locality
programme
beneficiary_households
beneficiary_individuals
aid_type
planned_quantity
distributed_quantity
delivery_status
partner
```

### Students Build

#### KPIs

- Total households reached
- Total individuals reached
- Planned vs distributed quantity
- Completion rate

#### Views

1. Map — beneficiaries by state
2. Bar chart — beneficiaries by programme
3. Trend — monthly distributions
4. Planned vs delivered comparison
5. Highlight table — programme × state

#### Interactivity

- State filter
- Programme filter
- Date filter
- Click-map-to-filter action

### Management Questions

- Which states received the most support?
- Where are delivery gaps largest?
- Which programmes are furthest behind plan?
- Is delivery improving over time?
- Where should management investigate first?

> **A dashboard should make the next question easier to ask.**

---

# 12. Day 3 Dashboard Critique Exercise

Show an intentionally bad dashboard containing:

- 9 charts
- 12 colors
- Tiny labels
- 8 filters
- 3 pie charts
- No clear title
- Repeated information

Ask groups:

1. What should be removed?
2. What should be combined?
3. What is the primary question?
4. What should be the first thing the user sees?

Then redesign it together.

---

# 13. Day 4 — Data Storytelling & Executive Communication
## Theme: From Dashboard to Decision

### Main Objective

Teach students how to present analytical findings to a non-technical decision-maker.

## Core Topics

### 1. Description vs Insight vs Recommendation

#### Description

> “Branch A generated SDG 20M.”

#### Insight

> “Branch A generated the highest revenue but had a lower-than-average profit margin.”

#### Recommendation

> “Management should review Branch A’s product mix and discounting before investing further in sales expansion.”

Teach:

**Number → Context → Meaning → Action**

### 2. Start With the Decision

Ask:

> “What does the audience need to decide?”

### 3. Executive Story Structure

1. **Situation**
2. **Finding**
3. **Evidence**
4. **Meaning**
5. **Recommendation**

### 4. Better Titles

Avoid:

> “Sales by Category”

Prefer:

> “Medical Supplies Generate the Highest Revenue, but Personal Care Has the Strongest Margin”

### 5. Annotation

Use annotations only for important events or exceptions.

### 6. Story Points — Optional

Briefly introduce Tableau Story if useful.

A strong dashboard plus verbal presentation may be more useful than forcing Story Points.

### 7. Presenting to Executives

Teach:

- Do not explain every chart.
- Lead with the finding.
- Use simple language.
- Give evidence.
- State uncertainty.
- End with a recommendation.

### 8. Three-Minute Presentation Structure

**0:00–0:30** — Business question  
**0:30–1:30** — 2–3 major findings  
**1:30–2:15** — Risk / limitation / context  
**2:15–3:00** — Recommendation and next action

### 9. Handling Questions

Teach students to say:

> “The data does not allow us to answer that confidently.”

That is better than guessing.

---

# 14. Day 4 Practical Exercise
## Executive Briefing — Sudan FMCG Regional Performance

Students use the dashboard developed from the previous sales exercise.

Scenario:

> The CEO has only three minutes before another meeting.

Each student must present:

1. One major performance issue
2. One major opportunity
3. One supporting chart for each
4. One limitation
5. One recommendation

### Peer Feedback

Other students score:

- Was the message clear?
- Was the chart necessary?
- Was the claim supported?
- Was the recommendation connected to evidence?
- Could anything be removed?

---

# 15. Mini-Portfolio Project
# Project 03 — Sudan FMCG Executive Performance Dashboard

## Business Scenario

Students act as junior Business Intelligence Analysts for:

> **NileGoods Distribution Co.**

A fictional Sudanese FMCG distributor supplying food, household, and personal-care products across multiple locations.

The CEO asks:

> **“Where are we performing well, where are we losing opportunity, and what should management focus on next month?”**

Students must build an executive Tableau dashboard and present their findings.

---

# 16. Raw Data Provided

Recommended dataset size:

**2,000–5,000 transaction-level records**

Main table:

```text
transaction_id
transaction_date
branch
state
sales_rep
customer_type
channel
product_id
product_name
category
units_sold
unit_price_sdg
revenue_sdg
cost_sdg
discount_pct
```

Optional product table:

```text
product_id
product_name
category
supplier
standard_cost_sdg
```

Optional branch table:

```text
branch
state
branch_type
opening_date
monthly_target_sdg
```

---

# 17. Required Calculated Fields

## Profit

```text
SUM([Revenue SDG]) - SUM([Cost SDG])
```

## Profit Margin

```text
(SUM([Revenue SDG]) - SUM([Cost SDG])) / SUM([Revenue SDG])
```

## Average Transaction Value

```text
SUM([Revenue SDG]) / COUNTD([Transaction ID])
```

## Target Achievement

If target data is included:

```text
SUM([Revenue SDG]) / SUM([Monthly Target SDG])
```

Exact formulas may be adjusted to match the final dataset structure.

---

# 18. Business Questions the Dashboard Must Answer

1. What is total revenue?
2. What is total profit?
3. What is the overall profit margin?
4. How is performance changing over time?
5. Which branches generate the most revenue?
6. Which branches generate the strongest margin?
7. Which states or locations are underperforming?
8. Which categories drive revenue?
9. Which categories drive profit?
10. Which products are top performers?
11. Are discounts associated with lower margins?
12. Which channels perform best?
13. Are any branches missing targets?
14. Where should management investigate?
15. What should management prioritize next month?

---

# 19. Exact Portfolio Deliverables

## Deliverable 1 — Interactive Tableau Dashboard

The dashboard should include:

### 4–5 KPIs

Examples:

- Revenue
- Profit
- Profit Margin
- Transactions
- Target Achievement

### At Least 4 Analytical Views

Required categories:

1. **Time trend**
2. **Branch or state comparison**
3. **Category/product performance**
4. **Profitability or target analysis**

### At Least 3 Interactive Features

Examples:

- Date filter
- State filter
- Category filter
- Dashboard filter action
- Highlight action

### At Least 1 Calculated Field

Preferably more than one.

### At Least 1 Reference / Benchmark Element

Example:

- Average line
- Sales target
- Margin threshold

---

## Deliverable 2 — Published Tableau Public Link

Students publish the final dashboard to **Tableau Public**.

Important rule:

> **Only synthetic, anonymized, or genuinely public data may be published to Tableau Public.**

Students must not upload:

- Patient data
- Personal contact data
- Confidential employer data
- Sensitive NGO beneficiary-level data
- Internal company records
- Any dataset they do not have permission to make public

The portfolio project dataset should therefore be synthetic or explicitly approved for public use.

---

## Deliverable 3 — Dashboard Screenshot / PDF Export

Students submit a static backup of the dashboard for:

- Easy grading
- Backup if the public link has technical problems
- Portfolio documentation

---

## Deliverable 4 — Three-Minute Executive Presentation

Students record a **maximum 3-minute video**.

Audience:

> Mock CEO / Senior Manager

The presentation must include:

1. Business question
2. Top 3 findings
3. One limitation
4. Recommendation

Students should not explain every Tableau feature.

The purpose is **decision communication**, not software demonstration.

---

## Deliverable 5 — Executive Insight Summary

Maximum:

**1 page**

Include:

### 3 Key Insights

Each must contain:

**Evidence + Meaning**

### 2 Recommendations

Each must be linked to evidence.

### 1 Limitation

Something the dashboard cannot answer confidently.

---

# 20. Dashboard Design Requirements

Students should follow these rules:

- One clear dashboard title
- Maximum approximately 5 KPIs
- Maximum approximately 5–6 major visual elements
- Consistent terminology
- Meaningful chart titles
- Minimal decorative elements
- No unnecessary 3D effects
- No rainbow color scheme
- No chart included without a clear question
- Filters should have a reason to exist
- Important information should appear first
- Tooltips should add useful context
- Units must be clear
- Currency must be labeled
- Time period must be visible

---

# 21. Suggested Portfolio Rubric

| Competency | Weight |
|---|---:|
| Data connection & accuracy | 10% |
| Chart selection | 15% |
| Calculated fields / analytical depth | 15% |
| Dashboard structure & usability | 20% |
| Interactivity | 10% |
| Insight quality | 15% |
| Executive presentation | 10% |
| Documentation / professionalism | 5% |
| **Total** | **100%** |

### Suggested Pass Threshold

**70%**

---

# 22. Must-Pass Competencies

A student should not pass merely because the dashboard looks attractive.

They must demonstrate that they can:

- Choose an appropriate chart for a question.
- Build at least one correct calculated field.
- Create a usable interactive dashboard.
- Interpret at least one pattern correctly.
- Avoid making unsupported causal claims.
- Communicate at least one actionable insight.
- Give a recommendation connected to evidence.
- Explain one limitation.

---

# 23. Assessment Status

## PASS

Student demonstrates the required visualization and communication competencies.

→ Progress to the next module.

## REVISE

Student has built the dashboard but important competencies are missing.

Examples:

- Dashboard is too cluttered.
- Chart type does not fit the question.
- Metric is calculated incorrectly.
- Recommendation is unsupported.
- Student describes charts without interpreting them.
- Filters do not work logically.
- Dashboard has no clear audience.

→ Student receives targeted feedback and resubmits.

## INCOMPLETE

Required work is missing.

→ Student does not progress until requirements are resolved.

---

# 24. Teaching Tips

## Tip 1 — Make Students State the Question Before Touching Tableau

Create a rule:

> **No chart without a question.**

Before each worksheet, students write:

```text
Question:
Audience:
Metric:
Comparison:
```

Example:

```text
Question: Which branch has the strongest profit margin?
Audience: Sales Director
Metric: Profit Margin
Comparison: Branch
```

Only then build the chart.

---

## Tip 2 — Use a “Remove Before Add” Dashboard Rule

When a student finishes a dashboard, ask:

> **“What can you remove without losing the message?”**

Teach:

> **Clarity often comes from subtraction.**

Run a cleanup exercise where students remove:

- One chart
- Two colors
- One filter
- One unnecessary label
- One decorative element

---

## Tip 3 — Grade the Spoken Story Separately From the Dashboard

Treat them as separate competencies:

### Dashboard Skill

Can you build the analytical tool?

### Storytelling Skill

Can you explain what it means?

The 3-minute presentation should therefore be assessed independently.

---

# 25. Additional Pedagogical Technique
## The 5-Second Test

Display a dashboard for only five seconds.

Then hide it.

Ask:

> “What do you remember?”

If students cannot identify:

- The main question
- The biggest finding
- The most important metric

the dashboard probably lacks hierarchy.

---

# 26. One Chart = One Main Message

Before accepting a chart, ask:

> “What sentence should the viewer understand from this chart?”

If the student needs a paragraph to explain the chart, it may be too complicated.

---

# 27. Recommended Live-Class Rhythm

Use:

**Question → Demonstrate → Rebuild → Modify → Explain**

Example:

- 15 min — Explain why a bar chart fits a category comparison
- 10 min — Instructor builds it
- 15 min — Students rebuild it
- 15 min — Students modify it for a new question
- 10 min — Students explain what the visual shows

---

# 28. Common Beginner Mistakes to Explicitly Teach

## Mistake 1 — Too Many Colors

Fix: use color for meaning.

## Mistake 2 — Too Many Charts

Fix: include only visuals connected to decision questions.

## Mistake 3 — Pie Charts Everywhere

Fix: use bars when accurate comparison matters.

## Mistake 4 — Showing Raw Numbers Without Context

Bad:

> Revenue = SDG 8.4M

Better:

> Revenue = SDG 8.4M  
> +12% vs previous month

## Mistake 5 — Titles That Only Name the Chart

Weak:

> Revenue by Branch

Better:

> Port Sudan Leads Revenue, but Kassala Has the Strongest Margin

## Mistake 6 — Confusing Correlation With Causation

A scatter plot can show association.

It does not automatically prove cause.

## Mistake 7 — Every Filter Everywhere

Only include filters that support real questions.

## Mistake 8 — Designing for the Instructor

Students should not ask:

> “What chart will get marks?”

They should ask:

> “What would the manager need to see?”

---

# 29. Optional Context Tracks

## Track A — Health / Research

Examples:

- Clinic utilization dashboard
- Patient-flow summary using synthetic data
- Research survey dashboard
- Public-health indicators

## Track B — Business / Finance

Examples:

- FMCG sales dashboard
- Customer segmentation
- Branch profitability
- Product performance

## Track C — Development / Humanitarian / Agriculture

Examples:

- Aid distribution
- Agriculture production
- Education access
- Programme monitoring
- Service-delivery coverage

The technical rubric remains the same regardless of track.

---

# 30. What We Deliberately Do Not Teach in Module 3

Avoid overloading beginners with:

- Advanced Level of Detail expressions
- Complex parameter actions
- Advanced spatial analysis
- Advanced forecasting
- Advanced clustering
- Complex dashboard extensions
- Tableau Server administration
- Complex data modeling
- Advanced performance optimization
- Highly customized design tricks

The objective is not:

> **Become a Tableau specialist in four days.**

The objective is:

> **Build a clear, interactive decision dashboard and communicate its insights professionally.**

---

# 31. End-to-End Tableau Workflow

**Business Question**  
↓  
**Audience**  
↓  
**Connect Data**  
↓  
**Check Fields & Types**  
↓  
**Choose Metric**  
↓  
**Choose Visual**  
↓  
**Analyze**  
↓  
**Combine into Dashboard**  
↓  
**Add Interactivity**  
↓  
**Remove Clutter**  
↓  
**Identify Insight**  
↓  
**State Limitation**  
↓  
**Recommend Action**  
↓  
**Present**

---

# 32. Final Module Mindset

By the end of the module, students should stop asking:

> “Which chart should I create?”

and start asking:

> **What question are we trying to answer?**

> **Who needs this information?**

> **What is the clearest visual evidence?**

> **What should the viewer notice first?**

> **What does this pattern mean?**

> **What does it not prove?**

> **What should happen next?**

---

# 33. Module Summary

**Module:** Data Visualization and Storytelling with Tableau  
**Duration:** 4 intensive classes  
**Teaching Style:** Practical, question-first, decision-oriented  
**Main Themes:** Tableau foundations, chart selection, calculated fields, maps, dashboards, interactivity, visual hierarchy, storytelling, executive presentation  
**Portfolio Output:** Interactive Tableau dashboard + Tableau Public link + static backup + 3-minute executive presentation + 1-page insight summary  
**Progression Standard:** Mastery before progression  
**Primary Goal:** Transform analysis into clear visual communication and decision support

> **The student should leave this module able to say: “I can turn data into a dashboard that helps someone understand what matters and decide what to do next.”**
