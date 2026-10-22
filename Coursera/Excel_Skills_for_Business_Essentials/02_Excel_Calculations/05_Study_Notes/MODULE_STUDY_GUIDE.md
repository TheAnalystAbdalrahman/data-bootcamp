# Module 2 study guide: Excel Calculations

**Original supplementary guide.** General Excel examples, not copied course lessons or assessment answers. Work on copies of official files.

## Important concepts

- A formula begins with `=`. A cell reference points to a value; an operator such as `+`, `-`, `*`, or `/` combines values.
- Excel follows normal order of operations. Parentheses make the intended calculation explicit.
- Functions accept arguments inside parentheses: `SUM`, `AVERAGE`, `MIN`, and `MAX` are the core set here. AutoSum is a shortcut for inserting a likely `SUM` range; always inspect the suggested range.
- A relative reference such as `B2` changes when copied. An absolute reference such as `$B$2` stays fixed. Mixed forms `$B2` and `B$2` fix one dimension.
- A cross-sheet reference names both sheet and cell, for example `='Rates'!B2`. Quoted sheet names work safely when they contain spaces.
- A displayed result is not the formula itself. Select the cell and inspect the formula bar when checking work.

## Original examples to try

In a fictional order table, put quantity in `B2`, unit price in `C2`, and tax rate in `H1`. Enter `=B2*C2` for subtotal and `=B2*C2*(1+$H$1)` for total including tax. Copy both down and confirm that row references move while the tax-rate reference stays fixed. For rows 2–11, use `=SUM(D2:D11)`, `=AVERAGE(D2:D11)`, `=MIN(D2:D11)`, and `=MAX(D2:D11)` in separate summary cells. If another sheet is named `Rates`, `=B2*'Rates'!$B$2` multiplies by a fixed rate on that sheet.

Check the first, middle, and last copied formulas. A correct-looking total can still use the wrong range. If division is involved, check whether a zero denominator needs a clear not-applicable result rather than silently returning zero.

## Practice order

1. `W02-V01-Simple Formulas.xlsx`: write and copy basic formulas.
2. `W02-V02-Formulas in Business.xlsx`: translate a business calculation into cell references.
3. `W02-V03-Basic Functions.xlsx` and `W02-V04-Average Max Min.xlsx`: practice function ranges.
4. `W02-V05-Absolute Cell Refs.xlsx`: copy formulas with a fixed shared input.
5. `W02-V06-Calculate Across Sheets.xlsx`: link a calculation to another worksheet.

Matching `Soln` workbooks are available for all six steps. Compare them after independent practice. The [catalog](../../00_Course_Overview/WORKBOOK_CATALOG.md) lists the exact files, sheets, and formulas found in each.

## Revision checklist

- [ ] I can explain why a formula starts with `=` and use parentheses deliberately.
- [ ] I can choose the correct range for `SUM`, `AVERAGE`, `MIN`, and `MAX`.
- [ ] I can explain what happens to `B2`, `$B$2`, `$B2`, and `B$2` when copied.
- [ ] I can write a quoted cross-sheet reference.
- [ ] I can inspect copied formulas and catch an incorrect reference or range.
