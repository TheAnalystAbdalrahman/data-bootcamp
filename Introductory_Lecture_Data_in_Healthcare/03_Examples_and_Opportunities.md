# Examples, answer key, and opportunities

## Main exercise — where is medicine availability a problem?

**All values are synthetic.** These are fictional facilities, for the same fictional month and the same medicine. This is a table of facility summaries, not patient-level records.

For this exercise a recorded collection attempt is unsuccessful if the medicine was unavailable at that attempt. A person may make more than one attempt; these counts are not unique people. Attempts not recorded, and people who could not reach a facility, are absent.

### Stage 1: show only this

| Facility | Recorded unsuccessful attempts |
|---|---:|
| A | 40 |
| B | 30 |

Ask: “أي منشأة نحتاج نراجعها أول؟ وشنو المعلومة الناقصة؟” Both a provisional choice and asking for more information are useful responses.

### Stage 2: reveal the full table

| Facility | All recorded attempts | Unsuccessful attempts | Percentage unsuccessful |
|---|---:|---:|---:|
| A | 200 | 40 | 20% |
| B | 60 | 30 | 50% |
| Combined | 260 | 70 | About 26.9% |

**Calculation:** unsuccessful attempts ÷ all recorded attempts × 100.

In Arabic: “في A، من كل 100 محاولة مسجلة، 20 ما نجحت بسبب عدم التوفر. في B، من كل 100 محاولة، 50 ما نجحت.” This restates proportions; it does not assert that exactly 100 people visited either site.

### Answer key and interpretation

- A has the greater count: 40 versus 30. A goal of investigating the largest absolute number of recorded unsuccessful attempts may point there.
- B has the greater proportion: 50% versus 20%. A goal of investigating the higher recorded failure proportion may point there.
- Neither result establishes where additional resources would produce the greatest benefit. That also depends on causes, severity, access, feasibility, and cost.
- Combined: 70/260 ≈ 26.9%. Averaging 20% and 50% gives 35%, which treats facilities as equally weighted rather than attempts. Keep this as an optional answer to a question; do not add a third arithmetic task for beginners.
- We cannot infer poor management, poor clinical quality, community-wide need, treatment outcomes, or causation from these rows.

### Three cards to complete together

| Card | Suitable statement |
|---|---|
| Evidence | In this fictional month, B had a higher percentage of recorded unsuccessful collection attempts. |
| Hypothesis | Delivery delays may contribute; repeat attempts or different recording practices may also affect the comparison. |
| Proposed next step | Validate the records and examine dated stock and delivery logs before choosing an intervention. |

Ask what else would help: dates; stock balances and physical counts; order and delivery records; unrecorded attempts; opening hours; repeat visits; whether definitions were applied consistently. Do not turn the introductory activity into an inventory optimization lesson.

**Review loop:** if an authorized team later changes ordering or distribution, track availability and repeat attempts over a comparable period. Look for other changes before attributing improvement to the intervention.

## Plain-language vocabulary

Use the first seven during the table activity; the rest are available when their scene needs them.

| Term | Simple Arabic explanation | Example |
|---|---|---|
| Data | ملاحظات أو معلومات سجلناها | تاريخ وصول الشحنة أو عدد المحاولات. |
| Dataset | مجموعة بيانات منظمة | جدول المنشآت خلال شهر. |
| Row / record | صف يمثل الوحدة المتفق عليها | منشأة واحدة في شهر واحد؛ وفي جدول مختلف قد يكون محاولة واحدة. |
| Column / variable | صفة أو قياس نسجله بنفس المعنى | اسم المنشأة أو عدد المحاولات. |
| Data quality | هل التسجيل كامل وصحيح ومتسق ومناسب للسؤال؟ | هل الغياب صفر أم تقرير ناقص؟ |
| Analysis | ترتيب ومقارنة وفحص البيانات للإجابة عن سؤال | مقارنة عدد المحاولات غير الناجحة ونسبتها. |
| Insight | معنى مفيد نستخلصه من التحليل داخل حدوده | ترتيب المنشأتين يتغير حسب المقارنة بالعدد أو بالنسبة. |
| Metric / indicator | رقم محدد نستخدمه للمتابعة | نسبة المحاولات غير الناجحة خلال شهر. |
| Denominator | العدد الكلي الذي نقارن الجزء به | كل المحاولات المسجلة في نفس المنشأة والفترة. |
| Dashboard | ملخص بصري لمؤشرات وأسئلة محددة | متابعة التوفر حسب المنشأة والشهر. |
| Database / SQL | تخزين منظم للبيانات، ولغة لطلب أجزاء منها وربطها | ربط جدول الطلبات بجدول التوريد. |
| Bias | طريقة الجمع أو المقارنة تميل إلى صورة غير ممثلة | سجلات المنشأة لا تشمل من تعذر عليهم الوصول إليها. |
| Correlation / causation | حاجتان بتتغيروا مع بعض؛ ده وحده ما يثبت إن واحدة سببت الثانية | تزامن التأخير مع زيادة الطلب يحتاج تحقيقاً إضافياً. |
| Prediction | تقدير للمستقبل تحت افتراضات ومعه احتمال للخطأ | توقع الطلب إذا ظلت ظروف محددة قريبة من السابق. |

## Opportunity map: from a problem to evidence of ability

These are illustrative pathways, not verified vacancies or guarantees. Role titles and entry requirements vary by employer and country. The table is a teaching synthesis; the broad healthcare domains are supported by Sources S1–S5. Specialized research, epidemiology, clinical, and regulatory responsibilities require further training and appropriate oversight.

| Direction and possible search terms | Useful question | Beginner portfolio output using synthetic or suitable public data | Further development |
|---|---|---|---|
| Humanitarian information management; monitoring and evaluation (M&E); reporting assistant | Which locations submitted complete, timely reports? | Reporting-completeness table, one chart, and a note on missing reports. | Indicator definitions, field context, data protection, reporting systems. |
| Supply-chain analyst; inventory analyst | Which items repeatedly run out or expire? | Checked stock summary with dates, units, and an explanation of anomalies. | Procurement, lead times, forecasting, and operational constraints. |
| Research data assistant; clinical data management | Which study records have missing or inconsistent fields? | Synthetic data dictionary, cleaning log, and missingness report. | Study design, research ethics, relevant procedures and statistical methods. |
| Quality improvement; operations analyst | At which service step do recorded delays accumulate? | Process map and waiting-time summaries with a clear definition of each timestamp. | Service workflow, fair comparisons, improvement methods. |
| Public-health data support; health information roles | Do recorded service indicators differ across places or groups? | Public-data comparison that states the denominator, period, and coverage limits. | Epidemiology, population estimates, survey methods, contextual interpretation. |
| Digital-health product analyst; business intelligence (BI) analyst | Where do users abandon an appointment-booking process? | Synthetic usage funnel and a brief defining each event. | Product measurement, databases, privacy, evaluating changes. |
| Policy and programme analysis support | Where are services available relative to reported needs? | Sourced public-data brief comparing service coverage with explicit gaps. | Economics, policy evaluation, geography, stakeholder communication. |
| Analysis in other sectors | Which deliveries arrive late, or where do recurring service gaps appear? | Transport, retail, education, or water-service analysis with the same documented workflow. | Sector knowledge and the role's specific tools. |

Talk through only three rows in detail. Ask learners to choose a problem and output before choosing a job title.

## A believable path from interest to opportunity

1. Select a narrow question and appropriate synthetic or public data.
2. Define what a row means, units, dates, and coverage.
3. Keep a record of checks and changes; preserve the input.
4. Produce one useful summary or chart and a short explanation of its limits.
5. Get feedback, revise, and practice explaining the result.
6. Compare the work with actual requirements for a chosen role or further training.

Sample learning deliverable: a medicine-availability brief containing a checked table, one clearly labeled chart, three observations, unresolved questions, and a suggested investigation. This is a starting piece of evidence of skill; employment also depends on the role, experience, communication, and access to opportunities.

## Optional substitutions

If the medicine story does not fit the instructor's experience, keep the learning arc but change the case to waiting times, appointment attendance, or delivery delays. Retain one case across scenes so new terminology does not arrive with a new story every time. Avoid treatment comparisons in this introductory session; they demand additional attention to case mix, research design, and causal inference.
