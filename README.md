# Business Mentors Association — organizational records

**Document:** What this repository holds and how to read it
**Version:** 1.2
**Status:** Draft
**Owner:** Doug Bower
**Last Updated:** 11-07-26 14:29

---

## What this repository is

The Business Mentors Association (a working name until the legal name is chosen) is a central organization that provides technical services to independent business mentoring chapters. Each chapter is its own nonprofit and keeps ultimate authority over its own technology. The Association builds, tests and supports one shared set of chapter applications, and supports each chapter's own technical personnel.

This repository holds the Association's organizational records. It holds no application code.

## How to read it

1. **[DECISIONS.md](DECISIONS.md)** — every ruling, dated, in plain words. The rulings are the source; everything else follows from them.
2. **[NEXT-STEPS.md](NEXT-STEPS.md)** — the work in progress and the next steps, so a new session can continue where the last one stopped.
3. **[OPEN-QUESTIONS.md](OPEN-QUESTIONS.md)** — what is not yet decided, and what each question waits on.
4. **[docs/proposal-summary.md](docs/proposal-summary.md)** — the executive summary of the proposal, written for chapter leaders.
5. **[docs/cost-list.md](docs/cost-list.md)** — every cost dues must cover, plus what a chapter pays itself. The figures come from the workbook built by [costs/build_workbook.py](costs/build_workbook.py); see [costs/README.md](costs/README.md).
6. **[docs/setup-runbook.md](docs/setup-runbook.md)** — step-by-step setup of the Association's domain, email, password vault, hosting account and code hosting.
7. **[docs/website-template-prd.md](docs/website-template-prd.md)** — requirements for the template website each chapter copies, with the products chosen in [docs/website-template-implementation-notes.md](docs/website-template-implementation-notes.md).

## Where things stand

The Association does not exist legally yet. It is to be formed as a separate limited liability company owned by its member chapters, to shield the chapters from its liabilities (rulings 23 and 24). It has two domains: businessmentorsassociation.org for its website and mentorsassociation.org for email (ruling 25).

**This repository sits in a personal account** (`dbower44022`). Under the ruling that every Association account is held in the Association's own name, it should move to an account the Association controls once that account exists. Until then this is the only live copy of these records: no copy is kept in a chat, a Claude project or a downloads folder.

**The cost and dues workbook** is `docs/association-costs.xlsx`. Its source is `costs/build_workbook.py`, which builds it; `costs/README.md` explains how the script, the workbook and the number snapshot are kept in step.

## Related repositories

- **`dbower44022/cbm-client-intake`** — the chapter applications, and the technical design of the chapter network in `prds/chapter-network/`, including the New Chapter Deployment Guide. Its decision file still states three rulings this repository has replaced; correcting it is owed.
- **`dbower44022/crmbuilder`** — CRM Builder, the tool that builds and configures each chapter's customer relationship management (CRM) system. It stays the property of Doug Bower, not the Association.

---

## Change log

| Version | Date | Change |
|---|---|---|
| 1.2 | 11-07-26 14:29 | Next steps file added to the reading list. Where things stand updated: the company form (rulings 23 and 24), the two domains (ruling 25), and the workbook, which is now committed with its generator. |
| 1.1 | 11-07-26 00:30 | Added the website template requirements and implementation notes to the reading list. |
| 1.0 | 09-25-26 | First version. Records moved in from the interim Claude project documents. |
