# Module 4 study guide: Excel Data Management

**Original supplementary guide.** The examples are independent of Coursera lessons and assessments. Practice on copies of official files.

## Important concepts

- A tidy data range has one header row, one variable per column, and one record per row. Avoid blank rows and merged cells inside the range.
- Insert, delete, hide, and resize rows or columns intentionally. Hiding is not deleting; formulas may still include hidden rows.
- Find locates values or text. Replace changes matching content, potentially across many cells; review the scope and a sample result before replacing all.
- Filtering temporarily displays matching rows. Sorting changes their order. Keep every field of a record together and include the full data range.
- Conditional formatting applies a rule to highlight values, dates, duplicates, or other conditions. The rule should make a specific question easier to answer, not merely add color.
- Before destructive data changes, save a working copy. After filtering or sorting, check the row count and a few complete records.

## Original mini-exercise

Create a fictional customer list with `Customer ID`, `City`, `Orders`, and `Revenue`. Filter to one city and sort revenue largest to smallest. Remove the filter and confirm all rows return. Highlight revenue above a chosen threshold with conditional formatting. In a separate copy, use Find and Replace to standardize one deliberately inconsistent city spelling. If you add a `Revenue per order` column, `=IF(C2=0,"n.a.",D2/C2)` avoids dividing by zero; this formula is an original example, not a required course technique.

## Practice order

1. `W04-V01-Work with Data.xlsx`: manage rows and columns.
2. `W04-V02-Work with Data.xlsx`: find and replace, checking scope.
3. `W04-V03-Work with Data.xlsx`: filter without losing records.
4. `W04-V04-Work with Data.xlsx`: sort complete records.
5. `W04-V05 Conditional Formatting.xlsx`: create and inspect highlighting rules.

The ZIP contains no separately named `Soln` workbooks for Module 4. Use the [catalog](../../00_Course_Overview/WORKBOOK_CATALOG.md) to distinguish these similarly named files by their `V01`–`V05` identifiers.

## Revision checklist

- [ ] I can preserve a tidy header-and-record structure.
- [ ] I can distinguish hide from delete and verify the effect of row/column changes.
- [ ] I can limit Find and Replace to the intended scope.
- [ ] I can filter and sort while keeping rows intact.
- [ ] I can explain and inspect a conditional-formatting rule.
