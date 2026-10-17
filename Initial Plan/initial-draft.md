This is a strong foundation for the bootcamp. The main design challenge is not fitting the content into three months—it is preventing **cognitive overload** while still getting beginners to a level where they can independently complete a credible portfolio project.

Your bi-weekly structure can work particularly well if the “off” weeks are treated as **structured application weeks**, rather than simply homework weeks.

Sudan-specific contextualization is also worth making a core design principle rather than a cosmetic one. Agriculture remains a major part of Sudan's economy and livelihoods, while trade, telecommunications, education, healthcare, logistics, and other services have been significantly affected by recent economic conditions. That gives us many authentic analytical problems to build around. ([World Bank][1])

## 1. My assessment of the proposed structure

### What I would keep

**The Friday–Sunday intensive format is good.** It creates momentum and gives each module a clear beginning and end.

**The one-weekend gap is especially important.** Beginners need time to forget, struggle, revisit, and finally understand. Three consecutive weekends of SQL → Tableau → Python would probably produce superficial learning.

**A mini-project after every course is one of the strongest parts of the design.** Students should graduate with more than a certificate. Ideally, they finish with:

* 1 spreadsheet project
* 1 SQL project
* 1 Tableau dashboard
* 1 applied statistics case study
* 1 Python analysis
* 1 substantial personalized capstone

That means a successful student leaves with **six demonstrable pieces of work**.

### The personalized capstone is excellent—with one modification

I would personalize the **problem**, but standardize the **assessment**.

If every student receives a completely different project with completely different expectations, grading becomes inconsistent and mentoring becomes extremely difficult.

Instead, every capstone should follow the same analytical framework:

**Business/Research Problem → Data → Cleaning → Exploration → Analysis → Visualization → Insights → Recommendations → Presentation**

Students can choose very different subjects within that framework.

For example:

> A pharmacist could analyze medicine inventory or demand.

> An engineer could analyze energy consumption or infrastructure data.

> A finance graduate could analyze business transactions.

> Someone interested in agriculture could investigate crop production or agricultural prices.

> A student pursuing a master's degree could analyze data related to their research area.

The **subject changes, but the required analytical skills remain standardized**.

I would therefore create one universal capstone rubric covering areas such as problem formulation, data preparation, analysis, visualization, interpretation, communication, reproducibility, and presentation.

---

# 2. The most important pedagogical enhancement

I would change the mental model from:

**Teaching Weekend → Assignment → Pass → Next Course**

to:

**Learn → Practice → Build → Receive Feedback → Improve → Demonstrate Mastery → Progress**

That difference matters enormously.

A beginner failing SQL joins should not simply receive "Fail: 58%." They need to know *which competency they haven't mastered* and have a short remediation pathway.

I recommend five design principles:

### 1. 30/70 theory-practice balance

Approximately **30% explanation and 70% doing** during live classes.

A three-hour session should not become three hours of slides.

Concept → instructor demonstration → guided exercise → independent challenge.

### 2. Friday should feel easier than Sunday

Friday creates confidence.

Saturday builds competence.

Sunday introduces ambiguity and independence.

For example, in SQL:

**Friday:** `SELECT`, `WHERE`, `ORDER BY`

**Saturday:** `GROUP BY`, aggregations, joins

**Sunday:** "Here is a business question and database. Figure out how to answer it."

That transition is essential.

### 3. Use one continuing Sudanese fictional company

Alongside independent datasets, I strongly recommend creating a fictional company that appears throughout the bootcamp.

For example:

**NileMart Sudan**

A fictional retailer/distributor operating across several Sudanese cities or states.

Students might first analyze its sales in Excel, later query its database with SQL, create its management dashboard in Tableau, statistically investigate customer behavior, and eventually automate analysis with Python.

This creates continuity:

> "I know this business already. I'm learning a new tool—not a completely new world."

For beginners, that reduces cognitive load substantially.

### 4. Use real Sudanese data where appropriate—but responsibly

Sudan currently faces extraordinary economic and humanitarian circumstances. Some datasets can therefore be meaningful but also sensitive. I would combine **publicly available data, carefully constructed synthetic datasets, and anonymized realistic business datasets** rather than forcing every exercise to use real-world personal information.

For example, FAO publishes useful Sudanese agricultural information covering sorghum, millet, wheat, sesame, groundnuts and other crops, and has also published recent remote-sensing work on cultivated areas. ([FAOHome][2])

Students could therefore work with highly relevant Sudanese scenarios without using personally identifiable or sensitive data.

### 5. Off-weeks need structure

Each application week should contain roughly:

**Day 1–2:** revision exercises
**Day 3–5:** mini-project
**Day 6:** peer review or mentor feedback
**Day 7:** revision/submission

I would also run an optional **60–90 minute online clinic** during these weeks.

That could dramatically reduce dropout among beginners.

---

# 3. Proposed 12-week architecture

I would avoid adding too many technologies.

Five major tools/skills plus the capstone is enough.

| Week        | Stage                                           |
| ----------- | ----------------------------------------------- |
| **Week 1**  | Spreadsheets Intensive                          |
| **Week 2**  | Spreadsheet project + feedback                  |
| **Week 3**  | SQL Intensive                                   |
| **Week 4**  | SQL project + feedback                          |
| **Week 5**  | Tableau / Data Visualization                    |
| **Week 6**  | Tableau project + feedback                      |
| **Week 7**  | Applied Statistics                              |
| **Week 8**  | Statistics project + feedback                   |
| **Week 9**  | Python for Data Analysis                        |
| **Week 10** | Python project + Capstone Proposal              |
| **Week 11** | Personalized Capstone Development               |
| **Week 12** | Capstone Completion + Presentation + Graduation |

I deliberately put **Tableau before Statistics and Python**.

Beginners benefit from an early visual achievement. Building a professional-looking dashboard around week 5 can be a major confidence boost before statistics and programming become more demanding.

---

# 4. Module 1 — Spreadsheets for Data Analysis

### Core goal

Move students from "I can use Excel/Google Sheets" to:

> **"I can take messy business data and turn it into useful information."**

### Friday — Data Thinking + Spreadsheet Foundations

Introduce the data analysis workflow.

Topics:

* Rows, columns, records and variables
* Data types
* Good vs bad datasets
* Sorting and filtering
* Basic formulas
* `SUM`, `AVERAGE`, `MIN`, `MAX`
* Relative vs absolute references
* Basic business metrics
* Data-quality thinking

Use examples such as shop sales, household expenditure, student enrollment, agricultural transactions and inventory.

### Saturday — Cleaning and Analysis

Topics:

* Missing values
* Duplicate records
* Text cleaning
* Dates
* `IF`
* `COUNTIF/S`
* `SUMIF/S`
* Lookup functions
* Conditional formatting
* PivotTables
* Basic KPI creation

### Sunday — From Analysis to Decision

Topics:

* Pivot charts
* Dashboard principles
* Selecting useful KPIs
* Trend analysis
* Comparing categories
* Communicating insights
* Turning numbers into recommendations

### Portfolio Project

**Sudan Market Basket & Small Business Performance Dashboard**

Students receive transaction and commodity-price data from a fictional Sudanese retail business.

They answer questions such as:

Which products generate the most revenue?

Which locations perform best?

How have prices changed?

Which categories have the highest margins?

Which products should management monitor?

**Portfolio output:** cleaned workbook + interactive spreadsheet dashboard + one-page business summary.

---

# 5. Module 2 — SQL for Data Analysis

### Core goal

Teach students to communicate with databases and retrieve information independently.

### Friday — Thinking in Tables

Topics:

* What databases are
* Tables, rows and columns
* Primary/foreign keys
* `SELECT`
* `DISTINCT`
* `WHERE`
* `AND`, `OR`
* `IN`
* `BETWEEN`
* `LIKE`
* `ORDER BY`
* `LIMIT`

### Saturday — Business Analysis with SQL

Topics:

* `COUNT`
* `SUM`
* `AVG`
* `MIN/MAX`
* `GROUP BY`
* `HAVING`
* `CASE WHEN`
* Date functions
* Handling NULLs

### Sunday — Connecting Business Data

Topics:

* Database relationships
* `INNER JOIN`
* `LEFT JOIN`
* Multiple-table joins
* Subqueries or CTE introduction
* Translating a business question into a query
* Debugging SQL

### Portfolio Project

**Sudanese Retail & Distribution SQL Investigation**

Students work with a fictional database containing:

`customers`

`orders`

`products`

`branches`

`suppliers`

`payments`

Students receive a management brief with 10–15 questions.

Examples:

> Which branch generated the highest monthly revenue?

> Which products have declining demand?

> Which customer segments purchase most frequently?

> Which suppliers account for most inventory?

> Which regions show potential expansion opportunities?

**Portfolio output:** SQL script + analytical findings + short executive summary.

---

# 6. Module 3 — Tableau & Data Storytelling

### Core goal

Teach students that visualization isn't decoration—it is communication.

### Friday — Visualization Fundamentals

Topics:

* Connecting data
* Dimensions vs measures
* Bar charts
* Line charts
* Maps
* Tables
* Filters
* Sorting
* Choosing the right chart
* Avoiding misleading visualization

### Saturday — Tableau Analysis

Topics:

* Calculated fields
* Groups
* Sets
* Parameters
* Date analysis
* KPIs
* Filters
* Dashboard actions
* Interactive visualization

### Sunday — Dashboard + Storytelling

Topics:

* Dashboard layout
* Visual hierarchy
* Audience-first design
* Data storytelling
* Insight annotation
* Executive dashboards
* Presenting findings

### Portfolio Project

**Sudan Agriculture & Food Production Dashboard**

Students investigate crops such as sorghum, millet, wheat, sesame or groundnuts across seasons/regions using public or responsibly synthesized data.

Agriculture is particularly appropriate for the cohort because it remains central to Sudanese livelihoods and the national economy. FAO identifies major production systems and crops across the country, while recent agricultural assessments provide realistic contemporary analytical questions. ([FAOHome][2])

Possible questions:

Where is production concentrated?

How does production change over time?

Which crops demonstrate greater variability?

Where might supply pressures exist?

**Portfolio output:** interactive Tableau dashboard + 3–5 written insights.

---

# 7. Module 4 — Applied Statistics for Decision-Making

This should **not** resemble a university statistics class.

Students don't need pages of formulas.

They need to understand:

> "When can I trust what my data appears to be telling me?"

### Friday — Understanding Data

Topics:

* Population vs sample
* Categorical vs numerical variables
* Mean, median and mode
* Variance
* Standard deviation
* Percentiles
* Outliers
* Distribution
* Histograms
* Sampling

### Saturday — Relationships and Uncertainty

Topics:

* Probability intuition
* Normal distribution
* Sampling variation
* Confidence intervals
* Correlation
* Correlation ≠ causation
* Introduction to hypothesis testing
* Statistical vs practical significance

### Sunday — Applied Business Statistics

Topics:

* Comparing groups
* Basic hypothesis tests
* A/B-testing concepts
* Linear relationships
* Simple regression intuition
* Interpreting results
* Common statistical mistakes

### Portfolio Project

**Sudanese Telecom Customer Experience Study**

Create a realistic survey dataset containing variables such as:

network usage

monthly recharge amount

service satisfaction

location

age bracket

data usage

complaints

customer tenure

Students investigate:

> Are heavier users more satisfied?

> Is spending associated with satisfaction?

> Are differences between customer groups meaningful?

> Which factors appear associated with customer experience?

Importantly, students must distinguish between **evidence, association and causality**.

**Portfolio output:** statistical analysis report + management recommendations.

---

# 8. Module 5 — Python for Data Analysis

This will probably be the most intimidating course for true beginners, so it should be taught differently from a traditional Python course.

They do **not** need to become software developers.

The learning objective is:

> **"I can use Python to load, clean, analyze and visualize data."**

### Friday — Python Without Fear

Topics:

* Jupyter/Colab
* Code cells
* Variables
* Strings and numbers
* Lists
* Dictionaries
* Simple conditions
* Loops
* Functions at a basic level
* Reading error messages

Keep general programming theory short.

### Saturday — Pandas

Topics:

* DataFrames
* `read_csv`
* `.head()`
* `.info()`
* Selecting columns
* Filtering
* Missing values
* Duplicates
* Creating columns
* Sorting
* `groupby`
* Aggregation
* Merging datasets

### Sunday — End-to-End Analysis

Topics:

* Exploratory Data Analysis
* Visualization
* Group comparisons
* Basic statistical analysis
* Reusable analysis workflow
* Documenting notebooks
* Translating results into insights

### Portfolio Project

**Sudanese SME Business Intelligence Analysis**

Students act as junior data analysts for a fictional Sudanese SME.

They receive messy:

sales data

customer data

product data

expense data

Students use Python to:

**Import → Inspect → Clean → Merge → Analyze → Visualize → Recommend**

**Portfolio output:** polished Jupyter/Colab notebook + README/project summary.

---

# 9. Final Graduation Capstone

This is where I would make your bootcamp distinctive.

The project should begin **before Week 11**.

During Week 8, students start identifying interests.

During Week 9, they discuss potential problems.

During Week 10, they submit a one-page:

### Capstone Proposal

**My area of interest:**
**Problem I want to investigate:**
**Who would care about this problem:**
**Dataset:**
**Questions I want to answer:**
**Tools I expect to use:**
**Expected output:**

Then the instructors approve, reduce or modify the scope.

---

## Example personalized capstones

A student working in banking might create:

**Customer Transaction & Branch Performance Analysis**

An agriculture graduate:

**Sesame Production and Market Trends in Sudan**

A healthcare worker:

**Healthcare Facility Utilization Analysis**

A master's student:

**Data Analysis Supporting Their Research Topic**

An entrepreneur:

**Sales Forecasting and Customer Segmentation for a Sudanese SME**

An engineer:

**Solar Energy Performance Analysis for Sudanese Communities**

An education professional:

**Student Performance and Retention Analysis**

Someone interested in logistics:

**Supply-Chain and Delivery Performance to Port Sudan**

The World Bank specifically identifies disrupted services including healthcare, education, telecommunications and trade, while FAO documents the importance and diversity of Sudan's agricultural sector. Those areas therefore provide a broad pool of meaningful project contexts rather than forcing every student into a single industry. ([World Bank][1])

---

# 10. Capstone graduation requirement

I would make graduation genuinely competency-based.

For example:

| Area                             |   Weight |
| -------------------------------- | -------: |
| Problem definition               |      10% |
| Data cleaning & preparation      |      15% |
| Analytical methodology           |      20% |
| Technical execution              |      20% |
| Visualization                    |      15% |
| Interpretation & recommendations |      10% |
| Final presentation               |      10% |
| **Total**                        | **100%** |

A student might need **70% overall**, plus no serious deficiency in the core technical areas.

Most importantly, students who do not initially pass should get **one structured revision opportunity** rather than simply being removed.

---

# 11. The alumni community should become part of the learning model

I would position the private alumni community as more than a reward at the end.

The message becomes:

**Learn → Build → Graduate → Belong → Continue Growing**

Graduates could use the community for:

* job and internship opportunities
* Sudanese data-science networking
* project collaboration
* peer troubleshooting
* monthly data challenges
* portfolio feedback
* guest sessions from professionals
* postgraduate/research collaboration
* mentorship of future cohorts

Eventually, strong graduates from Cohort 1 could become **peer mentors for Cohort 2**.

That creates a self-strengthening Sudanese data community rather than another bootcamp whose relationship with the student ends after the certificate.

---

# 12. One addition I strongly recommend: career skills should be embedded, not made into another course

We have limited time, so I would **not** create a sixth "Career Development" module.

Instead, every project teaches one professional skill.

**Excel:** writing business insights
**SQL:** answering stakeholder questions
**Tableau:** presenting to management
**Statistics:** defending a conclusion with evidence
**Python:** documenting technical work
**Capstone:** presenting yourself as an analyst

By graduation, each student should ideally have a **GitHub/portfolio page, CV-ready project descriptions, Tableau portfolio where appropriate, and a concise professional Data Analyst/Data Scientist profile**.

---

## The resulting learning journey

The progression becomes very deliberate:

**Spreadsheets**
*"I can analyze data."*

↓

**SQL**
*"I can retrieve the data I need."*

↓

**Tableau**
*"I can communicate what the data says."*

↓

**Statistics**
*"I understand whether the evidence is meaningful."*

↓

**Python**
*"I can perform analysis programmatically."*

↓

**Personalized Capstone**
*"I can solve a real problem independently."*

↓

**Graduation + Private Alumni Community**
*"I now belong to a professional network that helps me keep developing."*

That is a much stronger outcome than trying to produce "data scientists" after 12 weeks. The realistic first objective is to create **confident, employable beginner data practitioners with strong analytical foundations and a portfolio**, after which some will naturally progress deeper into data science, machine learning, engineering, or research.

### Next step

**Yes—send me the student pre-course survey.** That should be the next input before we lock this curriculum.

Once I see it, I would use the responses to refine **the technical difficulty, assumed starting level, industries and career tracks, preferred project areas, software requirements, support/remediation strategy, capstone categories, and potentially the exact exercises used in each Friday/Saturday/Sunday class**.

The survey may also reveal that we should modify the order or depth of these five modules rather than assuming the same pathway is appropriate for this particular cohort.

[1]: https://www.worldbank.org/ext/en/country/sudan?utm_source=chatgpt.com "Sudan | World Bank Group"
[2]: https://www.fao.org/sudan/fao-sudan/sudan-at-a-glance/en?utm_source=chatgpt.com "Sudan at a glance"
