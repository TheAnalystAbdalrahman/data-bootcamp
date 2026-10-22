"""Render the manually verified course-outline CSV as a readable index."""

import csv
from collections import Counter
from pathlib import Path

BASE = Path(__file__).resolve().parent
rows = list(csv.DictReader((BASE / "LESSON_INDEX.csv").open(encoding="utf-8-sig", newline="")))
assert len(rows) == 127

MODULES = {
    1: ("Critical Core of Excel", "5 hours", "46 min video; 2h 5m readings", ["Recognize the main parts of the Excel interface.", "Navigate and select data.", "Create and edit a spreadsheet; work with rows and columns."]),
    2: ("Excel Calculations", "4 hours", "43 min video; 2h 5m readings", ["Explain basic formula and function syntax.", "Use formulas and functions for simple calculations.", "Distinguish relative from absolute cell references."]),
    3: ("Excel Formatting Essentials", "3 hours", "40 min video; 1h readings", ["Choose and apply key formatting tools.", "Use styles and themes.", "Use number formats and format raw data for readability."]),
    4: ("Excel Data Management", "3 hours", "35 min video; 1h readings", ["Manage rows, columns, and worksheets.", "Find, change, filter, and sort data.", "Use conditional formatting to highlight selected data."]),
    5: ("Printing Excel Spreadsheets", "4 hours", "35 min video; 1h 30m readings", ["Recognize Excel print tools and options.", "Prepare a sheet for printing.", "Use repeating elements such as print titles, headers, and footers."]),
    6: ("Excel Data Charts", "5 hours", "35 min video; 1h 30m readings", ["Describe chart types and terminology.", "Create basic charts.", "Modify chart type, style, position, and elements."]),
    7: ("Final Assessment", "1 hour", "1 graded assessment", ["Demonstrate the essential skills from Modules 1–6."]),
}

counts = Counter(int(row["module"]) for row in rows)
lines = [
    "# Complete lesson index",
    "",
    "Authenticated Coursera classroom outline inspected 17 October 2026. This index records visible titles and lesson URLs through ordinary navigation; it does not reproduce lesson text or assessment questions. Module time estimates are from the published course listing. A blank item duration means **not verified**, not zero. Practice activity labels are inferred from their position in the classroom's practice section; only items in its Assessment section are labelled graded.",
    "",
    "| Module | Published title | Indexed items | Video + reading time shown in classroom |",
    "| ---: | --- | ---: | --- |",
]
for number, (name, total, class_time, objectives) in MODULES.items():
    lines.append(f"| [{number}](#module-{number}-{name.lower().replace(' ', '-').replace(':', '')}) | {name} | {counts[number]} | {class_time} |")
lines += ["", f"**Total: {len(rows)} indexed items.** See [LESSON_INDEX.csv](LESSON_INDEX.csv) for a filterable version. For the 45 locally saved workbooks, see [WORKBOOK_CATALOG.md](WORKBOOK_CATALOG.md).", ""]

for number, (name, total, class_time, objectives) in MODULES.items():
    selected = [row for row in rows if int(row["module"]) == number]
    lines += [f"## Module {number}: {name}", "", f"[Open classroom module](https://www.coursera.org/learn/excel-essentials/home/module/{number}) · Published estimate: {total} · {len(selected)} indexed items.", "", "**Learning objectives:** " + " ".join(objectives), ""]
    lines += ["| Section | Type | Lesson | Duration (min) |", "| --- | --- | --- | ---: |"]
    for row in selected:
        title = row["title"].replace("|", "\\|")
        duration = row["duration_min"] or "—"
        lines.append(f"| {row['section']} | {row['type']} | [{title}]({row['official_url']}) | {duration} |")
    if number < 7:
        workbook = next(row for row in selected if row["type"] == "Workbook download")
        lines += ["", f"Workbook source: [{workbook['title']}]({workbook['official_url']}). Official ZIP and extracted workbooks are in the corresponding module's `02_Official_Downloads` folder; the [catalog](WORKBOOK_CATALOG.md) maps each file to its likely skill.", ""]
    else:
        lines += ["", "No separate Week 7 workbook download is listed in the classroom outline. The assessment itself was not opened or attempted.", ""]

(BASE / "COMPLETE_LESSON_INDEX.md").write_text("\n".join(lines), encoding="utf-8")
print("Indexed items by module:", dict(sorted(counts.items())))
