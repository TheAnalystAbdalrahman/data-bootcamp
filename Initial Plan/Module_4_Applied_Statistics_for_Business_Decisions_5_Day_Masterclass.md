# Module 4 — Applied Statistics for Business Decisions
## Extended 5-Day Masterclass

**Audience:** Non-technical adults, including learners with math anxiety  
**Format:** 5 intensive live classes  
**Suggested Structure:** Friday, Saturday, Sunday + following Friday and Saturday  
**Approach:** Intuition first, formulas second  
**Context:** Sudanese business, health, agriculture, digital commerce, NGOs, and research  
**Assessment:** One portfolio-ready applied statistics project  
**Primary Goal:** Help students make better decisions from data without turning the module into a traditional mathematics course

---

# 1. Module Philosophy

This module should not feel like a university statistics lecture.

The core question is not:

> “Can you calculate a formula by hand?”

The core question is:

> **“Can you look at data, judge the strength of the evidence, recognize uncertainty, and make a responsible decision?”**

The module should focus on:

- Intuition
- Interpretation
- Business logic
- Evidence quality
- Uncertainty
- Bias
- Decision-making
- Communication

Mathematical notation should be introduced only when it helps understanding.

---

# 2. Module Learning Outcomes

By the end of the 5-day module, students should be able to:

- Distinguish descriptive statistics from inferential statistics.
- Choose between mean, median, percentages, and rates appropriately.
- Understand spread, variability, and outliers.
- Recognize sampling bias and misleading comparisons.
- Explain probability in everyday terms.
- Understand random variation without heavy formulas.
- Explain the idea of a sampling distribution.
- Understand the Central Limit Theorem intuitively.
- Interpret confidence intervals.
- Explain what statistical significance does and does not mean.
- Compare two groups responsibly.
- Understand the logic of A/B testing.
- Interpret p-values at a practical level.
- Distinguish statistical significance from business significance.
- Explain correlation versus causation.
- Recognize confounding variables.
- Interpret simple regression outputs at a beginner level.
- Communicate uncertainty to a non-technical audience.
- Make recommendations that match the strength of the evidence.

---

# 3. Overall 5-Day Learning Journey

| Day | Theme | Student Mindset |
|---|---|---|
| **Day 1** | Describing Data & Detecting Bias | “I can summarize data without being misled by it.” |
| **Day 2** | Probability & Randomness | “I understand that variation can happen by chance.” |
| **Day 3** | Sampling, CLT & Confidence Intervals | “I understand why a sample can tell us something about a larger population.” |
| **Day 4** | Hypothesis Testing & A/B Testing | “I can compare options without overreacting to random differences.” |
| **Day 5** | Correlation, Causation & Decision-Making | “I can make a recommendation while being honest about what the data proves.” |

The learning progression is:

**Describe → Question → Quantify uncertainty → Test → Interpret → Decide**

---

# 4. Day 1 — Descriptive Statistics, Variability & Bias
## Theme: What Does the Data Actually Say?

### Main Objective

Build confidence with statistics by starting from familiar ideas:

- averages
- percentages
- variation
- outliers
- group comparisons

Students should understand that a single number rarely tells the full story.

## Core Topics

### 1. Descriptive vs Inferential Statistics

**Descriptive statistics** summarize the data we already have.

Examples:

- Average monthly sales
- Median waiting time
- Percentage of customers who completed registration

**Inferential statistics** help us reason beyond the observed sample.

Example:

> “If 120 customers answered our survey, what can we reasonably say about all customers?”

### 2. Mean, Median & Mode

Focus on choosing the right measure.

Use practical examples:

- Salary
- Household expenses
- Patient waiting times
- Product prices
- Daily sales

Key lesson:

> **The mean is not always the best summary.**

Example:

```text
15,000
18,000
19,000
20,000
120,000
```

Ask:

- What is the mean?
- What is the median?
- Which better represents the typical person?

### 3. Percentages, Rates & Denominators

Reinforce:

- Numerator
- Denominator
- Rate
- Percentage
- Comparison base

Example:

> Branch A had 200 sales and Branch B had 150.

Ask:

- Is Branch A necessarily performing better?
- What if Branch A has twice the number of employees?
- What if Branch B has fewer customers but higher conversion?

### 4. Variability

Teach intuitively:

- Range
- Variance concept
- Standard deviation concept
- Consistency vs instability

Key idea:

> Two shops can have the same average sales but completely different stability.

### 5. Outliers

Discuss:

- When an outlier is a real signal
- When an outlier may be an error
- Why deleting outliers automatically is dangerous

### 6. Sampling Bias

Introduce:

- Convenience sampling
- Self-selection bias
- Non-response bias
- Undercoverage
- Survivorship bias

Ask:

> “Who is missing from the data?”

---

# 5. Day 1 Practical Exercise
## Case Study — Sudanese Retail Branch Performance

Students receive synthetic weekly sales data from four branches.

Columns:

```text
branch
week
transactions
customers
revenue_sdg
staff_count
average_basket
```

### Questions

1. Which branch has the highest revenue?
2. Which branch has the highest revenue per employee?
3. Which branch has the highest conversion rate?
4. Which branch is most consistent?
5. Are any weeks obvious outliers?
6. Does the “best branch” change depending on the metric?

### Key Lesson

> **A ranking can change when the denominator changes.**

### Exit Reflection

> “What is one conclusion you would not make from this dataset?”

---

# 6. Day 2 — Probability Without Fear
## Theme: Chance, Randomness & Risk

### Main Objective

Teach probability as a way of thinking about uncertainty, not as a collection of formulas.

Students should leave understanding:

> **Not every difference means something important happened.**

## Core Topics

### 1. What Is Probability?

Use everyday language:

- Impossible
- Unlikely
- Possible
- Likely
- Almost certain

Connect to:

- Loan repayment risk
- Customer conversion
- Product defects
- Rainfall
- Agricultural yield
- Patient outcomes

### 2. Random Events

Use coins, dice, cards, or simulated business events.

Important lesson:

> Randomness can produce patterns that look meaningful.

### 3. Expected Value — Intuition Only

Example:

A delivery business has:

- 70% chance a delivery costs SDG 5,000
- 20% chance it costs SDG 10,000
- 10% chance it costs SDG 30,000

Ask:

> What should management roughly budget per delivery over many deliveries?

### 4. Independent vs Related Events

Examples:

- Two separate customer purchases
- Repeat purchases by the same customer
- Rainfall and crop yield
- Marketing exposure and conversion

### 5. Conditional Probability

Teach through:

> “Given that…”

Examples:

- Given that a customer opened the SMS, what is the chance they purchased?
- Given that a patient is in age group X, what is the chance of outcome Y?
- Given that a farmer used irrigation, what is the chance yield exceeded a threshold?

### 6. Risk vs Certainty

Teach students to communicate:

- likely
- unlikely
- estimated
- uncertain
- risk
- evidence suggests

instead of pretending decisions are certain.

---

# 7. Day 2 Practical Exercise
## Case Study — Mobile Marketing Campaign

A fictional Sudanese telecom company sends two promotional offers.

Students receive:

```text
customer_id
campaign_received
opened_sms
clicked_link
purchased
customer_segment
state
```

### Questions

1. What proportion opened the SMS?
2. What proportion clicked?
3. What proportion purchased?
4. What is the probability of purchase given a click?
5. Is purchase behavior different across customer segments?
6. Could random variation explain small differences?

### In-Class Simulation

Run a simple coin-flip or spreadsheet simulation to show that random groups often produce different results even when there is no true difference.

---

# 8. Day 3 — Sampling, Central Limit Theorem & Confidence Intervals
## Theme: From a Sample to the Bigger Picture

### Main Objective

Help students understand how analysts use samples to estimate population behavior.

This is the day where pacing should be slow.

## Core Topics

### 1. Population vs Sample

Examples:

**Population:** All customers of a bank  
**Sample:** 400 customers surveyed

Discuss:

- Cost
- Time
- Availability
- Practicality

### 2. Sampling Methods

Introduce:

- Random sampling
- Stratified sampling
- Convenience sampling

### 3. Sampling Variability

Core idea:

> If we take different samples from the same population, we will get slightly different answers.

### 4. Sampling Distribution

Explain:

> “Imagine taking hundreds of samples and calculating the average every time.”

Key insight:

> Sample estimates move around, but they tend to cluster.

### 5. Central Limit Theorem — Intuitive Version

Teach:

> “Even if the original data is messy, the distribution of many sample means often becomes more regular as the sample size increases.”

No formal proof.

### 6. Standard Error — Conceptual

Explain:

> Standard deviation describes variability in the data.

> Standard error describes uncertainty in our estimate.

### 7. Confidence Intervals

Teach:

> **Estimate ± uncertainty**

Example:

> Customer satisfaction is estimated at 72%, with a 95% confidence interval from 68% to 76%.

Focus on interpretation.

Use:

> “This method produces intervals that capture the true population value about 95% of the time in repeated sampling.”

Then translate:

> “Our best estimate is around 72%, but there is uncertainty.”

---

# 9. Day 3 Practical Exercise
## Case Study — Agricultural Yield Estimation

Students receive synthetic crop-yield data from a sample of farms.

Columns:

```text
farm_id
state
crop
farm_size_hectares
irrigation_type
yield_kg_per_hectare
```

### Questions

1. What is the average yield in the sample?
2. What is the median?
3. How much does yield vary?
4. Which crop or region is most variable?
5. What does a confidence interval add beyond reporting the average?
6. Why might the sample not represent all Sudanese farms?

### Key Lesson

> **A sample gives an estimate, not certainty.**

---

# 10. Day 4 — Hypothesis Testing & A/B Testing
## Theme: Is the Difference Real or Just Noise?

### Main Objective

Teach students how to compare two options without overreacting to random differences.

This day should focus on decision logic, not formulas.

## Core Topics

### 1. The Logic of a Hypothesis Test

Explain:

> We start by assuming there is no meaningful difference.

This is the **null hypothesis**.

Then ask:

> “Would the observed difference be surprising if there really were no difference?”

### 2. Null & Alternative Hypotheses

Example:

**H0:** Campaign A and Campaign B have the same conversion rate.

**H1:** The conversion rates differ.

Use plain language before notation.

### 3. p-value — Intuitive Explanation

Teach:

> A p-value asks how surprising our result would be if the null hypothesis were true.

Explicitly teach that this is incorrect:

> “The p-value is the probability that the null hypothesis is true.”

### 4. Statistical Significance

Explain common threshold:

```text
p < 0.05
```

but emphasize:

> **0.05 is not magic.**

### 5. Statistical vs Practical Significance

Example:

Campaign B improves conversion:

```text
10.00% → 10.15%
```

With a huge dataset, this might be statistically significant.

Ask:

> “Is the improvement worth the campaign cost?”

### 6. A/B Testing

Workflow:

**Question  
→ Hypothesis  
→ Random assignment  
→ Measure outcome  
→ Compare groups  
→ Quantify uncertainty  
→ Decide**

### 7. Common A/B Testing Mistakes

- Stopping early
- Testing too many metrics
- Unequal groups
- Changing the experiment halfway
- Looking only at percentage change
- Ignoring sample size
- Ignoring practical cost

---

# 11. Day 4 Practical Exercise
## Case Study — Sudanese Marketplace A/B Test

Use a fictional Sudanese digital marketplace inspired by local e-commerce behavior.

Scenario:

The platform tests two versions of a product-listing page.

### Version A

Current page

### Version B

Simplified page with a clearer “Contact Seller” button

Dataset:

```text
visitor_id
version
device_type
state
contacted_seller
completed_purchase
session_duration
```

### Questions

1. What is the conversion rate for A?
2. What is the conversion rate for B?
3. What is the absolute difference?
4. What is the relative percentage difference?
5. Is the difference statistically significant?
6. Is it practically meaningful?
7. Does the result vary by mobile vs desktop?
8. Should the company launch Version B?

### Required Decision Format

Students must choose:

- **Launch**
- **Do not launch**
- **Run a larger test**

and justify the decision with evidence.

---

# 12. Day 5 — Correlation, Causation & Responsible Decisions
## Theme: What Can We Actually Claim?

### Main Objective

Teach students to distinguish association from causation and communicate conclusions responsibly.

This day brings together the entire module.

## Core Topics

### 1. Correlation

Examples:

- Advertising spend and sales
- Rainfall and crop yield
- Income and spending
- Study hours and exam score

### 2. Correlation Does Not Prove Causation

Ask:

> “If two things move together, does one necessarily cause the other?”

### 3. Confounding

Sudanese-context example:

Mobile-money usage and sales both increase in some areas.

Possible confounders:

- Urbanization
- Income
- Smartphone penetration
- Network availability

### 4. Reverse Causality

Example:

> Does advertising cause sales, or do businesses advertise more when they expect strong sales?

### 5. Simple Regression — Beginner Interpretation

Introduce:

- Outcome variable
- Predictor variable
- Direction
- Strength
- Coefficient
- R² at a conceptual level

No matrix algebra.

Example interpretation:

> “For each additional SDG 10,000 in marketing spend, sales increased by an estimated X units, on average, in this dataset.”

Then ask:

> “Can we call this causal?”

Usually no, unless the design supports it.

### 6. Decision-Making Under Uncertainty

Teach students to separate:

- What we know
- What we estimate
- What we suspect
- What we recommend

### 7. Communicating Results

Recommended structure:

**Finding  
→ Evidence  
→ Uncertainty / limitation  
→ Recommendation**

---

# 13. Day 5 Practical Exercise
## Case Study — Marketing Spend vs Sales

Students receive data from a fictional Sudanese retail chain.

Columns:

```text
branch
month
marketing_spend_sdg
sales_sdg
foot_traffic
discount_rate
location_type
```

### Questions

1. Is marketing spend correlated with sales?
2. How strong is the relationship?
3. What other variables could explain the relationship?
4. Can we say marketing caused the increase?
5. Does the relationship differ by branch type?
6. What should management do next?

### Final Class Discussion

> “What would we need to know before making a causal claim?”

---

# 14. Mini-Portfolio Project
# Project 04 — Should We Scale the Campaign?

## Business Scenario

Students act as junior analysts for a fictional Sudanese digital commerce company:

> **SouqSudan Online**

The company has run a promotional campaign in several regions and wants to know whether to expand it nationally.

Management asks:

> **“Did the campaign work, and should we invest more money in it?”**

The dataset intentionally contains enough complexity to require descriptive analysis, bias awareness, statistical testing, and business judgment.

---

# 15. Project Dataset

Suggested size:

**1,000–3,000 customer records**

Columns:

```text
customer_id
state
age_group
customer_segment
campaign_group
channel
opened_message
clicked_offer
purchased
purchase_value_sdg
prior_customer
device_type
registration_month
```

Optional supplemental table:

```text
state
population_estimate
internet_access_rate
urban_rural
```

---

# 16. Project Questions

Students must answer:

1. What does the dataset contain?
2. Who is represented?
3. Who may be missing or underrepresented?
4. What are the major descriptive statistics?
5. What are the conversion rates for treatment and control?
6. What is the absolute difference?
7. What is the relative difference?
8. Is the difference statistically significant?
9. What does the confidence interval suggest?
10. Is the difference practically meaningful?
11. Does the result differ by customer segment or device type?
12. Are there possible sources of bias?
13. What confounders or alternative explanations should management consider?
14. What can we claim?
15. What can we **not** claim?
16. Should management scale the campaign?

---

# 17. Exact Deliverables

## Deliverable 1 — Analysis Workbook / Notebook

Can be completed using:

- Excel
- Google Sheets
- Python, if Python has already been introduced
- Instructor-provided statistical calculator/template if needed

Must include:

- Cleaned data
- Descriptive statistics
- Group comparisons
- Confidence interval
- Hypothesis test
- Segmentation analysis
- Supporting charts

## Deliverable 2 — Two-Page Executive Memo

Maximum:

**2 pages**

Audience:

**Business management**

The memo must contain:

### Section 1 — Business Question

What decision needs to be made?

### Section 2 — What the Data Shows

3–5 key findings.

### Section 3 — Statistical Evidence

Explain:

- Difference between groups
- Confidence interval
- Statistical significance
- Practical significance

Use plain language.

### Section 4 — Biases & Limitations

Identify at least:

**3 limitations or risks**

### Section 5 — Recommendation

Choose one:

- **Scale the campaign**
- **Do not scale**
- **Run another test before deciding**

The recommendation must be supported by evidence.

## Deliverable 3 — One-Page Decision Dashboard

Include approximately:

- Overall conversion rate
- Treatment conversion rate
- Control conversion rate
- Absolute lift
- Confidence interval
- Revenue impact
- Key segment comparison
- Final recommendation

## Deliverable 4 — “What We Can and Cannot Claim”

Students submit a short table:

| Supported by Evidence | Not Supported by Evidence |
|---|---|
| Example claim | Example unsupported claim |

At least:

**3 statements on each side**

---

# 18. Suggested Project Rubric

| Competency | Weight |
|---|---:|
| Descriptive analysis | 15% |
| Identification of bias / data limitations | 15% |
| Statistical reasoning | 20% |
| A/B test interpretation | 20% |
| Practical/business interpretation | 15% |
| Recommendation quality | 10% |
| Communication clarity | 5% |
| **Total** | **100%** |

### Suggested Pass Threshold

**70%**

---

# 19. Must-Pass Competencies

A student should not pass solely because calculations are correct.

They must demonstrate that they can:

- Distinguish correlation from causation.
- Recognize at least one important source of bias.
- Correctly interpret statistical significance.
- Distinguish statistical significance from practical significance.
- Avoid claiming that a p-value proves a hypothesis.
- Explain uncertainty.
- Make a recommendation aligned with the evidence.

---

# 20. Assessment Status

## PASS

The student demonstrates the core statistical reasoning skills.

→ Progress to the next module.

## REVISE

The student shows partial understanding but has a major interpretation problem.

Examples:

- Correct calculation but incorrect interpretation
- Confuses correlation with causation
- Claims p-value proves the null or alternative hypothesis
- Ignores sample bias
- Makes a recommendation stronger than the evidence

→ Receive targeted feedback and resubmit.

## INCOMPLETE

Required work is missing.

→ Cannot progress until requirements are met.

---

# 21. Teaching Tips for Math Anxiety

## Tip 1 — Intuition Before Notation

Never open a new topic with a formula.

Bad approach:

```text
SE = σ / √n
```

Better approach:

> “If we survey 20 people, how stable do you think our estimate will be?”

Then:

> “What if we survey 2,000?”

Once the intuition is clear, show the formula only as a compact representation of the idea.

## Tip 2 — Use Visual Simulation Repeatedly

Probability and sampling are easier to understand when students can **see randomness**.

Use:

- Coin-flip simulations
- Random sampling in spreadsheets
- Histograms
- Repeated sample means
- Simple A/B simulations

Students should visually observe:

> random variation → repeated samples → clustering → uncertainty

before learning terminology.

## Tip 3 — Reward Interpretation More Than Arithmetic

Ask:

> “What does this result mean?”

> “What would you tell the manager?”

> “What can we not conclude?”

A student who can interpret a confidence interval correctly demonstrates more useful analytical skill than a student who reproduces a formula without understanding it.

---

# 22. Additional Engagement Techniques

Use a repeating class rhythm:

**Question → Prediction → Small Exercise → Concept → Practice → Discussion**

Before revealing answers, ask students to predict.

Example:

> “Campaign B converted 12.1% and Campaign A converted 11.8%. Which is better?”

Then ask:

> “But is that difference meaningful?”

This creates curiosity before introducing statistical testing.

---

# 23. Recommended Use of Calculators and Software

Do not make students manually calculate complex test statistics.

Use:

- Excel
- Google Sheets
- Simple instructor templates
- Statistical calculators
- Python later, if appropriate

The learner's responsibility is:

1. Choose the correct analytical question.
2. Understand the output.
3. Interpret it.
4. Communicate it.
5. Make a responsible decision.

Not:

> Memorize statistical tables.

---

# 24. What We Deliberately Do Not Teach

Avoid:

- Formal probability proofs
- Deriving the normal distribution
- Manual z-tables
- Manual t-tables
- Calculus
- Matrix algebra
- Advanced ANOVA
- Advanced Bayesian statistics
- Advanced regression diagnostics
- Multiple regression in depth
- Machine-learning statistics
- Heavy mathematical notation

---

# 25. Recommended Daily Rhythm

Each day can follow:

### 20–25 min
Concept explanation

### 15 min
Visual demonstration

### 20–30 min
Guided exercise

### 10 min
Break

### 30–45 min
Case study

### 15–20 min
Group discussion

### 10 min
Exit challenge

Avoid long uninterrupted lectures.

---

# 26. Exit Questions by Day

## Day 1

> “Which number could be technically correct but misleading?”

## Day 2

> “Could this difference have happened by chance?”

## Day 3

> “How certain are we about our estimate?”

## Day 4

> “Is the difference statistically significant — and does it actually matter?”

## Day 5

> “What can we claim, and what can we not claim?”

---

# 27. Final Module Mindset

By the end of the module, students should stop asking:

> “Which formula do I use?”

and begin asking:

> **What decision are we trying to make?**

> **What does the data actually show?**

> **How uncertain is the result?**

> **Could bias explain it?**

> **Could chance explain it?**

> **What can we responsibly claim?**

> **What should we do next?**

---

# 28. End-to-End Statistical Decision Workflow

**Business Question**  
↓  
**Define the Metric**  
↓  
**Inspect the Data**  
↓  
**Check Bias & Quality**  
↓  
**Describe the Data**  
↓  
**Quantify Uncertainty**  
↓  
**Compare Groups / Test Hypothesis**  
↓  
**Evaluate Practical Significance**  
↓  
**Consider Confounders**  
↓  
**State What the Evidence Supports**  
↓  
**Make a Decision**  
↓  
**Communicate Limitations**

---

# 29. Module Summary

**Module:** Applied Statistics for Business Decisions  
**Duration:** 5 live teaching days  
**Teaching Style:** Intuition-first, low-math, highly practical  
**Main Themes:** Descriptive statistics, probability, sampling, confidence intervals, hypothesis testing, A/B testing, correlation, causation, bias, business decisions  
**Portfolio Output:** Analysis + 2-page executive memo + dashboard + supported/unsupported claims table  
**Progression Standard:** Mastery before progression  
**Primary Goal:** Build statistical judgment, not mathematical memorization

> **The student should leave this module able to say: “I can use data to make a decision without pretending the evidence is stronger than it really is.”**
