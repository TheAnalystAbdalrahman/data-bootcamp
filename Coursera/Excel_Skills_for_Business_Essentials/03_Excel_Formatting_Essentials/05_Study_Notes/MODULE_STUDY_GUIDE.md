# Module 3 study guide: Excel Formatting Essentials

**Original supplementary guide.** It uses general Excel examples and does not reproduce course lessons or assessment questions. Work on copies of official files.

## Important concepts

- Formatting changes how a cell looks; it normally does not change the stored value. A number formatted as currency remains numeric.
- Use font weight, fill, and borders to distinguish headings and totals without making every cell visually loud.
- Alignment and text wrapping help long labels fit; merged cells can make sorting and filtering harder, so use them sparingly in data areas.
- Format Painter copies appearance from one area to another. Check that the destination still contains its intended values and formulas.
- Number formats communicate meaning: decimals, percentage, currency, dates, and thousands separators. Displayed rounding does not round the underlying value.
- Cell styles and themes can standardize a workbook. Use a small consistent palette so readers can recognize headers, inputs, and results.

## Original mini-exercise

Create a four-row fictional expense table with `Date`, `Category`, `Amount`, and `Share of total`. Put `=C2/SUM($C$2:$C$5)` in `D2` and fill down. Format `C2:C5` as currency and `D2:D5` as percentage with one decimal. Add a clear header and a top border on a total row. Then temporarily change `D2` to General format to see that the same underlying ratio is displayed differently. Do not type `%` into the formula result as text.

## Practice order

1. `W03-V01 Font Formatting.xlsx`: set a readable heading hierarchy.
2. `W03-V02 Borders.xlsx`: group a table with restrained borders.
3. `W03-V03-Alignment.xlsx`: align headings and long labels.
4. `W03-V04-Format Painter.xlsx`: replicate a style accurately.
5. `W03-V05-Number Formats.xlsx`: distinguish values from their display.
6. `W03-V06-Styles and Themes.xlsx`: apply a consistent built-in design.

Each has a matching `Soln` file. Check your own attempt first. The [catalog](../../00_Course_Overview/WORKBOOK_CATALOG.md) identifies the worksheets and detectable features.

## Revision checklist

- [ ] I can explain the difference between value and number format.
- [ ] I can format dates, currency, percentages, and decimal places appropriately.
- [ ] I can use alignment, wrapping, fonts, fills, and borders consistently.
- [ ] I can copy only formatting with Format Painter.
- [ ] I can apply a style/theme without obscuring the data.
