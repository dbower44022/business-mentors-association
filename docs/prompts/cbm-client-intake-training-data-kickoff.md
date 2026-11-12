# Kickoff prompt — loading crm-test's training data into the Association's system

**Document:** Prompt to start a Claude Code session in `cbm-client-intake` that loads the Association's customer relationship management system with the training data crm-test holds, under Association ruling 77
**Version:** 1.1
**Status:** Approved by Doug 11-12-26
**Owner:** Doug Bower
**Last Updated:** 11-12-26 00:24

---

Paste everything below the line into a new Claude Code session started in `~/Dropbox/Projects/cbm-client-intake`.

---

Operating mode: DETAIL (this repository's default).

## What this session is for

The Business Mentors Association is set up as a chapter. Its customer relationship management (CRM) system is at crm.businessmentorsassociation.org, and its chapter applications are at apps.businessmentorsassociation.org (guide stages 9 and 11, done 11-09-26). Neither holds training data yet. Doug wants the Association's system to hold the same invented training data that crm-test holds.

Association ruling 77 (11-12-26) settles how. The scripts that built crm-test's training data, in `scripts/sandbox/`, are rerun against the Association's CRM system. Every invented address goes on a domain of the Association's that has no mailboxes. The invented contacts are kept out of the Association's Constant Contact account. Records typed into crm-test by hand are not copied; that is the ruling's accepted cost.

This is the Association's guide stage 15, the training data, together with the invented mentors' sign-ins that stage 14 creates. Correct the guide's stages 14 and 15 wherever doing the work shows them wrong.

**This repository's process comes first.** Read `CLAUDE.md`, `OPEN-ITEMS.md` (item 73 and item 76 especially), `SANDBOX-RESET.md`, `prds/chapter-network/deployment-guide/association-setup-plan.md` and the guide's data files for stages 14 and 15 before anything else. Your first deliverable is a written plan with named stopping points, not code and not writes to any CRM system. Do not change code or write a record until Doug approves the plan.

## What the plan must cover

1. **A read-only count first.** Count what crm-test holds, record type by record type, against what the `scripts/sandbox/` scripts produce. Report what crm-test holds that no script made, so Doug can see what ruling 77's accepted cost actually loses before anything is loaded.
2. **The scripts' order and their Cleveland assumptions.** Which scripts built crm-test's data and in what order: `seed_training_data.py`, `enrich_training_data.py`, `deepen_showcase_records.py`, `seed_outreach_data.py`, `seed_import_templates.py`, and any others. List every place a script assumes Cleveland: names, the sandbox.cbmentors.org address domain, settings, or the CRM system it connects to.
3. **The address domain.** Propose a domain of the Association's with no mailboxes, such as sandbox.mentorsassociation.org. Verify, without changing anything, that no Google Workspace user or group and no mail exchange record exists for it. The scripts' own note explains why the domain must never become real.
4. **Pointing the scripts at the Association's system.** Whether this needs a code change, such as an option naming the target CRM system, or only different settings at run time. A code change follows this repository's process.
5. **The invented mentors' sign-ins.** The seed script attaches profiles to sign-ins that already exist, such as joe.mentor@. Say which sign-ins the Association's system needs and how they are created: guide stage 14, by an administrator.
6. **Keeping the invented contacts out of Constant Contact,** and from receiving any mail or calendar invitation.
7. **The nightly restore.** Ruling 15 says the shared test system's data is restored every night. Say whether the baseline is captured in this session or later, and what `SANDBOX-RESET.md` needs for a second system.
8. **The checks after loading.** The counts match step 1 apart from the hand-made records, and the training mentor's screens show data.

## Committing and pushing — read before any commit

**A push to `main` in this repository deploys crm-test and production.** Other sessions commit to the same local `main`, and parallel sessions share one git index.

- Pull first. Run `git status` and `git log origin/main..HEAD`, and report what is uncommitted or unpushed before you change anything.
- Commit only the files you changed. Stage them by path. Never stage, stash, reset or discard another line of work's changes.
- **Never push without Doug's explicit go-ahead,** given at a stopping point. When you ask, say what else the push would carry, and whether a deploy follows.
- **No write to crm-test, to Cleveland's production system, or to the Association's system without Doug's go-ahead at a stopping point.** Every script runs with `--check` or without `--apply` first.

## Read these, in the Association's repository

1. `~/Dropbox/Projects/business-mentors-association/DECISIONS.md` — rulings 15, 71, 72 and 77. Ruling 72's accepted cost is why containment matters: the applications' permission grant reaches every Association mailbox.
2. `~/Dropbox/Projects/business-mentors-association/docs/demo-chapter-plan.md` — decision D3, now answered, and Stop H.

The Association's repository is read-only from this session. Do not edit it.

## How the session ends

The closing reply reports: the counts from step 1, what was loaded, what was not, what changed in the code and the guide, and what is owed. Owed work is recorded in `OPEN-ITEMS.md`. Doug carries the closing report back to the Association's repository, where `NEXT-STEPS.md` records it.

---

## Change log

| Version | Date | Change |
|---|---|---|
| 1.1 | 11-12-26 00:24 | Approved by Doug. |
| 1.0 | 11-12-26 00:22 | First version, written after ruling 77. |
