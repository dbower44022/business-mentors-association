# The cost workbook

**Document:** What is in this folder, and how the snapshot stays in step with the workbook
**Version:** 1.0
**Status:** Current
**Owner:** Doug Bower
**Last Updated:** 09-25-26

---

## What is here

`association-costs.xlsx` is the working copy: it holds the formulas, so changing an input recalculates every total and every dues figure. **The workbook is a binary file and cannot be written to this repository by Claude**, whose tool writes text files only. It is delivered in the conversation and has to be committed here by hand.

What is committed here instead is a **readable snapshot of every sheet**, one comma-separated file each, holding the calculated values as they stood on 09-25-26. A snapshot is readable in a pull request, searchable, and diffable; the workbook is none of those.

| File | The sheet it came from |
|---|---|
| `assumptions.csv` | The inputs: how many people, the percentages, the nonprofit prices |
| `recurring-costs.csv` | Every recurring cost, at standard and nonprofit prices |
| `annual-total.csv` | The annual total, and the one-time costs of forming the company |
| `dues-by-band.csv` | Dues per chapter, by size band, at the example shares |
| `chapter-costs.csv` | What a chapter pays itself, for three example sizes |
| `notes-and-sources.csv` | Where each price came from |

[`../docs/cost-list.md`](../docs/cost-list.md) explains the lines in prose. That document, not this folder, is the one to read first.

## Keeping the two in step

The workbook is the source: edit it, then re-export these files and commit both together. A snapshot that disagrees with the workbook is worse than no snapshot, because the numbers here look authoritative.

**Nothing here is decided.** The bands, the shares and the dues amounts are the committee's to set (ruling 11), and three prices are still missing: cyber liability insurance, the attorney's fee for the operating agreement, and the Google Integration extension licence.

---

## Change log

| Version | Date | Change |
|---|---|---|
| 1.0 | 09-25-26 | First version. Snapshot of the workbook as it stood after the company formation costs were added. |
