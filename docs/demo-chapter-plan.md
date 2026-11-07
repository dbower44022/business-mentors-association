# Demo chapter — plan

**Document:** Plan for building the demo chapter as a full new chapter, and for finishing the test chapter website, under ruling 71
**Version:** 0.1
**Status:** Draft — drafted by Claude, waiting on Doug's decisions in section 4
**Owner:** Doug Bower
**Last Updated:** 11-07-26 14:38

---

## 1. What this plan delivers

A demo chapter that is exactly what a new chapter would run: its own domains, Google Workspace, customer relationship management (CRM) system, chapter applications, Constant Contact account, video meeting account, Stripe account in test mode, and a WordPress website with the chapter connector. It is built by following the New Chapter Deployment Guide, and the guide is corrected wherever it proves wrong or incomplete. The demo chapter then serves as the Association's shared test system (ruling 15).

Two tracks run side by side (ruling 71).

- **Track 1 — the test website on crm-test.** Finishes the integration between the website and the chapter applications now, on Cleveland's test system.
- **Track 2 — the demo chapter.** Builds the demo chapter's own accounts and systems, stage by stage. When its applications run, the test website is switched over to them.

## 2. Where the work happens

- **This repository** holds the rulings, this plan, the Association-side runbooks and the record of progress.
- **`cbm-client-intake`** holds the chapter applications, the website plan (`prds/chapter-website-plan.md`) and the New Chapter Deployment Guide (`prds/chapter-network/deployment-guide/steps/`, one data file per stage, rendered into `guide/`). That repository runs in DETAIL mode with its own change process. Every change there, including every correction to the guide, is made in a session started in that repository. Nothing in it is edited from here.
- **`chapter-website-prototype`** holds the chapter connector.
- **CRM Builder** builds the CRM system (guide stage 9). It is Doug's property and read-only from here; Doug runs it.

## 3. What the review of the guide found (11-07-26)

The guide's data files were last changed 09-25-26, before rulings 25 to 71.

1. **Stages 6 and 13, the website, predate the website rulings.** They describe a colour stylesheet, a logo held only in the CRM system and embedded pages. They need rewriting for WordPress on Cloudways, the chapter connector, the Website group of System Settings and framed forms (rulings 26 to 70).
2. **Stages 2 and 14 contradict ruling 1.** Step 2.3 requires identical software and step 14.3 confirms no one at the chapter holds an administrator account. Ruling 1 gives the chapter ultimate authority over its own technology.
3. **Stage 3 still treats the number of domains as open.** Ruling 25 registered two, the way the Association recommends for every chapter.
4. **Services with no steps:** Constant Contact; Stripe and its Payment Link (ruling 30); the website host account (ruling 29); Cloudflare Web Analytics (ruling 63). The video meeting account has one step.
5. **The guide speaks of "the central support organization".** That is the Association; the wording should follow.

These are findings, not changes. Each is corrected in `cbm-client-intake` when its stage is done in track 2.

## 4. Decisions owed by Doug

Taken one at a time. Each recommendation is Claude's, not a ruling.

- **D1. The demo chapter's domains and Google Workspace.** Whether the demo chapter has its own domains and its own Google Workspace, or uses the Association's. Decides guide stages 3, 4 and 10, and the test website's final address (next-steps item 4).
- **D2. The extension licences** (open questions 24 and 25). Whether the demo CRM shares Cleveland's Advanced Pack licence, and what the Google Integration licence costs. Needed before stage 9.
- **D3. The demo chapter's data.** Ruling 15 gives the shared test system invented training data restored every night. Whether that data is a copy of crm-test's training data or built fresh. Needed before stage 15.
- **D4. The video meeting service and the Constant Contact plan.** Which service and which plan, at what price. Needed before stage 5.

## 5. Order and stopping points

Work pauses for Doug's go-ahead at each stop. Between two stops it proceeds without asking.

**Track 1 — test website on crm-test.** Its stops are owned by `cbm-client-intake/prds/chapter-website-plan.md`, section 6:

1. Stop 4 there — Doug reviews piece C, forms in frames (v0.316.0), on crm-test.
2. Pieces D (campaigns through the website) and E (newsletter signup form) built; Stop 5 there.
3. Doug sets up the test website from `docs/runbooks/test-website-runbook.html` (piece F). Its Cloudways and Cloudflare screens have not been walked through; the runbook is corrected as Doug follows it.
4. Stop 6 there — the end-to-end test on the test website.

**Track 2 — the demo chapter.**

1. **Stop A — decision D1.**
2. Claude writes a kickoff prompt for a `cbm-client-intake` session that corrects the guide stage by stage, starting with the findings in section 3. **Stop B — Doug approves the prompt.**
3. Stages 1 and 2 (legal organization, agreement) are recorded as not applicable to a demo chapter, with invented placeholder values where later stages need them, such as an employer identification number.
4. Accounts: stages 3 to 5, plus the missing services — Constant Contact, Stripe in test mode, Cloudflare Web Analytics. Each set of steps a person follows is written as a runbook. **Stop C — every account open and recorded.** Decision D4 is taken before this stage starts.
5. Stages 7 and 8: policy documents from the template's drafts, and the chapter information form. **Stop D — Doug reviews the completed form.**
6. Stage 9, the CRM build, run by Doug with CRM Builder. Decision D2 is taken first. **Stop E — the CRM system passes the checking tool.**
7. Stages 10 to 12: Google permissions, the applications deployed, backups, monitoring and the nightly restore. **Stop F — the applications healthy and the restore proven once.**
8. Stage 13, the switch-over: the test website's chapter connector pointed at the demo chapter's applications, and the Website group filled in there. **Stop G — the website runs on the demo chapter.**
9. Stages 14 to 16: staff and training accounts, the training data (decision D3), training notes. Stage 17, the checks before going live. **Stop H — the end-to-end test on the demo chapter.** Stage 18, handover, is recorded as not applicable except the check that the accounts can be reached without help.

## 6. Out of scope

- Production for any chapter.
- Shared events between chapters (rulings 41 and 42).
- The seven feature requests in section 7 of the website template requirements.
- Moving the demo chapter's accounts from Doug's name into the Association's name. That waits on the Association's own accounts (ruling 18).

---

## Change log

| Version | Date (MM-DD-YY HH:MM) | Author | Change |
|---|---|---|---|
| 0.1 | 11-07-26 14:38 | Claude (Claude Code) | First draft, after ruling 71 and a review of the New Chapter Deployment Guide's data files as of 09-25-26. |
