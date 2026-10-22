> **Design update:** The current board is English-only and freeform, using circles, curved arrows, and sketches. The frame layout and Arabic visual labels below are historical; use the Board Guide and root AGENTS.md for current design preferences. The content and timing still inform delivery.

# Excalidraw storyboard — content before visual production

This specification is implemented in `Data_in_Healthcare.excalidraw`: nine numbered frames arranged in three rows of three, plus a separate answer frame 4B to the right of the second row. Each frame fits one shared-screen view. See `05_Board_Guide.md` for navigation and preview details.

## Visual grammar

- Arabic main labels; the English term below where needed. Test mixed Arabic/English text in separate text boxes if direction becomes confusing.
- Dark text on a light background. Blue: recorded evidence. Amber: questions or uncertainty. Green: proposed action. Include words or symbols so meaning never depends on color alone.
- Start with a readable title, one question, and a simple diagram. Speaker explanations stay in the lecture plan.
- At the opening show the journey briefly, then return to frame 1. Move through numbered frames; return to the original person at the end.
- Use large labels. Check readability through an actual screen-share view; avoid squeezing more text into a frame by shrinking it.
- Prebuild the main shapes. Draw only simple arrows, annotations, and comparisons live. Excalidraw objects are visible when panning; put answers in a separate area outside the current view and deliberately move to them. Do not rely on unsupported slide-style animations.

## Frame 1 — Why should I care? / ليه الموضوع يهمني؟

**Time:** 00–05.  
**Draw:** A person, a facility, and a medicine box with an “غير متوفر” label.  
**Question:** قبل ما نختار الحل، محتاجين نعرف شنو؟  
**Live action:** Collect two possible explanations on amber notes. Leave them as questions.  
**Anchor phrase:** تقليل عدم اليقين — Reduce uncertainty. Explain that uncertainty means there are important things we do not yet know; keep this phrase visible as a recurring label.  
**Transition:** Zoom out from this event to the system around it.

## Frame 2 — From one person to a system / من الفرد للمنظومة

**Time:** 05–12.  
**Draw:** Four connected areas: فرد → منشأة → مجتمع → أنظمة مترابطة. Connect the last area to transport, purchasing, budgets, and policy. Add “من لم يصل للخدمة؟” beside the community.  
**Question:** منو كمان بيأثر على وصول الخدمة؟  
**Live action:** Add one participant suggestion; mark a shared transport or stock problem outside healthcare.  
**Transition:** To understand this network, begin with something observable and recordable.

## Frame 3 — A question becomes a table / من السؤال للجدول

**Time:** 12–20.  
**Draw:** “أين يتكرر عدم توفر الدواء؟” above the first-stage table from the exercise. Bracket one row as “منشأة واحدة، شهر واحد” and one column as “صفة أو قياس”. Below, show Question → Collect → Check → Compare → Explain → Act → Review, with a loop back to the question.  
**Question:** الصف ده بيحكي عن شنو؟  
**Live action:** Read one row, underline the time period, and circle “recorded attempts”.  
**Transition:** We can already make a comparison, but what information might change it?

## Frame 4 — You are the analyst / دوركم تحللوا

**Time:** 20–32.  
**Draw:** Initial counts: A = 40, B = 30 unsuccessful attempts. Keep the denominator reveal in an adjacent subarea.  
**Reveal:** A: 40/200 = 20%; B: 30/60 = 50%. Show counts and percentages side by side with labels, rather than a chart with two incompatible units on one axis.  
**Question:** أكبر عدد؟ ولا أعلى نسبة؟  
**Live action:** Ask for a vote, move to the reveal, then add Evidence / Hypothesis / Proposed action cards.  
**Footer:** مثال تعليمي بأرقام افتراضية — لا يمثل منشآت حقيقية.  
**Transition:** The kind of question determines the kind of analysis.

## Frame 5 — Four types of analytics, one purpose / أربعة أنواع لتقليل عدم اليقين

**Time:** 32–40.  
**Draw:** A central heading “تقليل عدم اليقين / Reduce uncertainty” linked to four equal cards. Each has the Arabic question, full English type name, and one short medicine-availability example:

| Card | Question | Example |
|---|---|---|
| وصفي / Descriptive Analytics | حصل شنو؟ | أين وكم مرة سُجل عدم التوفر؟ |
| تشخيصي / Diagnostic Analytics | ممكن يكون حصل ليه؟ | هل تدعم سجلات التوريد فرضية تأخر التسليم؟ |
| تنبؤي / Predictive Analytics | متوقع يحصل شنو؟ | ما الطلب المتوقع الشهر الجاي تحت افتراضات محددة؟ |
| توجيهي / Prescriptive Analytics | نعمل شنو حسب هدفنا وظروفنا؟ | أي خيار طلب أو توزيع يناسب الميزانية والقيود؟ |

Use Arabic as the larger text. Four links from a shared purpose are preferable to a staircase suggesting automatic progress toward certainty.  
**Question:** السؤال ده محتاج وصف، تفسير، توقع، ولا مقارنة خيارات؟  
**Live action:** Point to the uncertainty each card addresses: size of the problem, possible explanation, future demand, or choice of action. Add “سبب محتمل ≠ سبب مثبت” and “توقع ≠ ضمان”. Keep a small amber note “ما زال غير معروف” visible beside the central heading; analysis can expose missing information as well as answer questions.  
**Source footer:** KMS Technology, “Different Types of Data Analytics in Healthcare”; full link in Source S4.  
**Takeaway:** نقلل عدم اليقين ونوضح حدوده؛ لا نضمن إزالته بالكامل.  
**Transition:** The same thinking is useful beyond one facility.

## Frame 6 — Sudan and the wider world / أثر محلي وعالمي

**Time:** 40–49.  
**Draw:** Left: reporting site → report → review → investigation → response. Label “Sudan: WHO report, March–April 2025”. Right: an overall result splitting into different population groups, without invented factual statistics.  
**Questions:** غياب التقرير يعني صفر؟ / مين اختفى وراء المتوسط؟  
**Live action:** Put a question mark, not a zero, beside an unreported site. Add one missing group from audience responses.  
**Source footer:** WHO Sudan report; WHO EWARS; WHO Health Inequality Monitor. Full links are in `04_Sources.md`.  
**Transition:** Each useful question creates a task somebody must do.

## Frame 7 — Where could I contribute? / ممكن أساهم وين؟

**Time:** 49–58.  
**Draw:** Three large branches from “معرفة المجال + مهارات التحليل”: humanitarian reporting, supply and operations, research. Each ends in a concrete sample output. Put digital health, quality, policy, and other sectors in a smaller surrounding ring.  
**Question:** أي مشكلة عايز تكون قادر تشتغل عليها؟  
**Live action:** Trace problem → analysis task → output for one participant interest.  
**Footer:** مسارات ممكنة؛ المتطلبات تختلف حسب الدور والجهة.  
**Transition:** Show the skills behind the outputs and how a beginner starts.

## Frame 8 — A reachable route / بداية تقدر تعملها

**Time:** 58–65.  
**Draw:** Question → clean table → checked summary → clear chart → documented recommendation. Place Excel, SQL, Tableau, statistics, and optional Python beside the tasks they support, using the course map in the plan.  
**Question:** سؤالك؟ محتاج أي بيانات؟ أول نتيجة شكلها شنو؟  
**Live action:** Complete one three-part learner response.  
**Transition:** Return to the person and ask what is needed before a useful action follows.

## Frame 9 — My next step / خطوتي الجاية

**Time:** 65–75.  
**Draw:** Original person + Question → Evidence → Action → Review. Leave three large blanks for problem, needed data, first output.  
**Question:** شنو السؤال العايز تبدأ بيه؟  
**Live action:** Discussion, exit ticket, closing.  
**Final takeaway:** سؤال واضح + دليل قابل للمراجعة → عدم يقين أقل أو أوضح → خطوة قابلة للتنفيذ، ثم مراجعة النتيجة.

## Board acceptance check

Before teaching: nine scenes in the agreed order; answers kept out of the initial activity view; English terms readable; Arabic direction checked; no real personal data; synthetic examples visibly labeled; dated factual examples attributed; all figures consistent with the answer key; complete timed rehearsal including audience pauses; offline fallback available.
