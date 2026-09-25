# The cost workbook

**Document:** What is in this folder, and which of the three artifacts is the source
**Version:** 1.1
**Status:** Current
**Owner:** Doug Bower
**Last Updated:** 09-25-26

---

## Three artifacts, one source

**`build_workbook.py` is the source.** It builds the whole workbook — every sheet, every formula — from the prices written at the top of the file. Run it:

```
python3 build_workbook.py association-costs.xlsx
```

It needs `openpyxl`. Change a price in the lists at the top of the script, rebuild, and everything downstream recalculates.

**The workbook itself is not committed here.** A spreadsheet is a binary file, and Claude's tool writes text files only, so the workbook is delivered in conversation and can be committed by hand. It does not have to be: the script reproduces it exactly.

**The comma-separated files are a readable snapshot** of what the formulas produced on 09-25-26. They exist so the numbers can be read, searched and compared in a pull request, which a spreadsheet cannot be.

| File | The sheet it came from |
|---|---|
| `assumptions.csv` | The inputs: how many people, the percentages, the nonprofit prices |
| `recurring-costs.csv` | Every recurring cost, at standard and nonprofit prices |
| `annual-total.csv` | The annual total, and the one-time costs of forming the company |
| `dues-by-band.csv` | Dues per chapter, by size band, at the example shares |
| `chapter-costs.csv` | What a chapter pays itself, for three example sizes |
| `notes-and-sources.csv` | Where each price came from |

[`../docs/cost-list.md`](../docs/cost-list.md) explains the lines in prose. That document, not this folder, is the one to read first.

## Keeping them in step

Edit the script, rebuild the workbook, re-export the snapshot, commit all of it together. A snapshot that disagrees with the script is worse than no snapshot, because the numbers here look authoritative.

**Nothing here is decided.** The bands, the shares and the dues amounts are the committee's to set (ruling 11), and three prices are still missing: cyber liability insurance, the attorney's fee for the operating agreement, and the Google Integration extension licence.

---

## Change log

| Version | Date | Change |
|---|---|---|
| 1.1 | 09-25-26 | The generator script added and named as the source; the note about the workbook being uncommittable reworded to match. |
| 1.0 | 09-25-26 | First version. Snapshot of the workbook after the company formation costs were added. |
