# Module 1 study guide: Critical Core of Excel

**AI-created supplementary material. Not an official Coursera resource.** Based on general Excel knowledge and the public module objectives, not on proprietary lesson content.

## What to be able to do

Open and save a workbook; identify the ribbon, name box, formula bar, sheet tabs, rows, columns, cells, and ranges; move and select efficiently; enter and correct text, numbers, dates, and formulas; use the fill handle, copy/paste, and an appropriate worksheet view.

## The mental model

A **workbook** is the file. It contains **worksheets**. A **cell** is one intersection of a column and row, such as `B3`; a **range** is a group such as `B3:D12`. Excel stores a value or formula in a cell and displays the calculated result. The formula bar shows what is actually stored in the selected cell.

For office reporting, give each column one meaning: `Date`, `Department`, `Item`, `Quantity`, `Unit price`. Give each row one record. Keep headers in one row and avoid decorative blank rows inside a data table. That structure makes later filtering and analysis far easier.

## Essential actions

| Goal | Typical action |
| --- | --- |
| Save a new working copy | File → Save As; give it a descriptive name |
| Jump to a cell | Type a reference, such as `F120`, in the Name Box |
| Edit a cell | Double-click it, or press `F2` on Windows |
| Finish entry | Press `Enter`; `Tab` moves right |
| Undo a mistake | `Ctrl+Z` |
| Copy / paste | `Ctrl+C` / `Ctrl+V` |
| Select a contiguous data region | `Ctrl+A` while inside it; check the selection before acting |
| Move to an edge of a data block | `Ctrl` plus an arrow key |

Shortcuts can vary by operating system and Excel version. Use the menu command when a shortcut differs on your machine.

## Data types and first formulas

`North Office` is text. `125` is a number and can be summed. `2026-10-17` may be a date **if Excel recognizes it** under your regional settings; otherwise it is text. A formula starts with `=`. For an order row with quantity in `D2` and price in `E2`, enter `=D2*E2` in `F2`. A total of `F2:F11` can use `=SUM(F2:F11)`. Save the workbook, reopen it, and check that the values and formulas still behave as expected.

The fill handle is the small square at a selected cell's lower-right corner. Dragging it can copy a formula or extend a pattern. Verify the first, middle, and final filled rows: the pattern Excel inferred may not be the one you intended.

## Try this on your own

Create a small **office supply log** with columns `Date`, `Department`, `Item`, `Quantity`, `Unit price`, and `Cost`. Add six fictional purchases. Calculate each cost and a grand total. Then copy a row, correct one entry, use undo once, test the fill handle, and save a separate practice copy. This exercise is original; it does not replace the course's Week 1 challenge.

## Common beginner mistakes

- Typing `10 units` into a quantity cell makes it text rather than a clean number; keep units in the header.
- Treating a displayed date as proof Excel stored a date; try changing its number format to confirm.
- Dragging a fill handle without checking the generated pattern.
- Pasting over a formula or source data; undo immediately if the result is wrong.
- Editing the original downloaded workbook instead of saving a practice copy. Keep any future Coursera original untouched.

## Revision check

- [ ] I can explain workbook, worksheet, cell, and range.
- [ ] I can jump to a cell and select a rectangular range.
- [ ] I can tell text, number, date, and formula apart.
- [ ] I can correct an entry, copy/paste, and undo.
- [ ] I can fill a pattern or formula and inspect the result.
- [ ] I can save and reopen my own practice workbook.

## Official workbook practice order

Use a copy of each official file, in this order: `W01-V01 Take charge.xlsx` (open/close and identify interface areas), `W01-V02-Select and Navigate.xlsx` (move and select), `W01-V03 Change View Options.xlsx` (view controls), `W01-V04-Enter Data.xlsx` (entry and correction), then `W01-V05-Fill Handle.xlsx` (patterns). Compare the last exercise with `W01-V05-Fill Handle Soln.xlsx` only after trying it. Find the files and their worksheet names in the [workbook catalog](../../00_Course_Overview/WORKBOOK_CATALOG.md). None of these originals should be edited in place.
