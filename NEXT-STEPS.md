# Next steps — where the work stands

**Document:** The work in progress and the next steps, kept so a new session can continue where the last one stopped
**Version:** 1.22
**Status:** Current
**Owner:** Doug Bower
**Last Updated:** 11-12-26 00:22

---

## How to use this file

A new session reads this file after `README.md` and `DECISIONS.md`. Each item says what is owed, why, and what it waits on. When an item is done, it is moved to "Done recently" with its date. Items here are tasks, not rulings: a ruling exists only in `DECISIONS.md`.

**Before starting work, pull from GitHub. At the end of a session, commit and push.** On 11-07-26 two lines of work had both been kept unpushed, and both had used ruling numbers 23 and 24. Fixing that took a renumbering of 46 rulings.

---

## Next steps, in recommended order

0. **The Association set up as a chapter (rulings 71 and 72), `docs/demo-chapter-plan.md`.** Track 2: the `cbm-client-intake` guide session (11-08-26) finished stages 3 to 5 for the Association, working in Doug's browser, and corrected the guide's stages 3 to 5 from the real screens (its plan: `cbm-client-intake/prds/chapter-network/deployment-guide/association-setup-plan.md`, version 1.5; owed items: that repository's `OPEN-ITEMS.md` item 73). Done: both domains on Cloudflare (still registered at GoDaddy); Google Workspace on mentorsassociation.org, Business Starter, with doug.bower@ and info@ mailboxes and the admin@ and allmembers@ groups, mail tested both ways; DigitalOcean, Zoom Pro, Constant Contact (trial), Stripe (test mode, donation link) and an Association Cloudways account, all signed in with admin@ apart from Stripe. Decision D4 answered: Zoom Pro without the Webinars add-on, Constant Contact Lite monthly. Doug's decisions in that session: every account signs in with admin@; GoDaddy stays on businessmentors@dougbower.com; compulsory two-step sign-in not yet; the Cloudways account is the Association's own. Owed: the second owner (ruling 18), two-step sign-in on six accounts, GoDaddy auto-renew, Constant Contact Lite before the trial ends, Stripe's email to admin@, DMARC to quarantine on or after 12-06-26, the admin@ group's spam setting. Nothing in `cbm-client-intake` is pushed; its `main` also holds another session's code fix, so its push is decided with that. Next: stage 6, the website, after a short plan in a `cbm-client-intake` session. Track 1: Doug reviews piece C at Stop 4 of `cbm-client-intake/prds/chapter-website-plan.md`. *Waits on:* Doug: the owed items above, and the start of the stage 6 session. **Update 11-08-26 14:19:** stage 6's guide rewritten and the website waits on Cloudways' account check; stage 7 guide updated and model policy drafts in `docs/policy-drafts/`; stage 8 done (`cbm-client-intake/prds/chapter-network/chapters/bma-values.yaml`); stage 9 blocked until CRMBuilder can hold a new deployment's own tokens — kickoff `cbm-client-intake/prompts/crmbuilder-deployment-credentials-kickoff.md` (Doug's choice). Rulings 73 and 74 added. The owed items are deferred by Doug while these are test systems.

1. **Correct the stale ruling numbers in `cbm-client-intake`.** `prds/chapter-website-plan.md` in `dbower44022/cbm-client-intake` cites this repository's rulings by their old numbers: "rulings 24 to 68", "Ruling 45", "Ruling 48", "Rulings 64…". Every ruling from 23 to 68 is now two higher (see the 2.29 entry in this repository's `DECISIONS.md` change log). That repository has its own change process. Read its `CLAUDE.md` first, and make the change only through that process. *Waits on:* Doug's go-ahead to start it there.

4. **Decide the test website's address.** Now decision D1a in `docs/demo-chapter-plan.md`: whether the switched-over website moves under businessmentorsassociation.org and becomes the Association's own public website. *Waits on:* Doug, before stage 13.

5. **Open question 30: the legal name.** `OPEN-QUESTIONS.md` asks whether the working name and the domain match the legal name. The domain names are now settled (ruling 25), and the company form is settled (ruling 23). The legal name is the remaining part. *Waits on:* Doug.

6. **Confirm or drop the drafted Cloudflare item.** The "Drafted by Claude" section of `DECISIONS.md` proposes that the Association's domains are registered through Cloudflare and their domain name records kept there. Step 2 answers the registrar part. *Waits on:* Doug. Step 2 answered the registrar part: GoDaddy, not Cloudflare.

7. **Correct `cbm-client-intake`'s chapter network decision file.** Its `prds/chapter-network/DECISIONS.md` still states rulings that this repository's rulings 1 to 3 replaced (noted in `README.md`). Same process rule as step 1. *Waits on:* Doug's go-ahead, best done together with step 1.

8. **Replace the Association's Google service account key.** The key for the service account in the Association's Google Cloud project was left in this folder for a day and was copied into local backups before Doug moved it to his password vault on 11-09-26. Create a new key, store it in the vault, and delete the old key in the Google Cloud console, so the copies stop working. Do it before guide stage 10, where the chapter applications first use the key. Claude writes the steps as a step page when this starts. *Waits on:* Doug, who chose to do it later (11-09-26).

9. **Clear the test website's server cache again.** Chapter connector 0.2.6 makes the Member Login link open in a new tab (Doug, 11-10-26). It is installed on chapter-demo.mentorsassociation.org, but the Cloudways server cache saved some pages again after Doug cleared it, with 0.2.5 still running: the home page, Find a Mentor and Contact. Every connector update needs the cache cleared afterwards. *Waits on:* Doug, in the Cloudways console.

10. **Check auto-renew on both domains at GoDaddy.** Both expire 11-07-27 and lapse if auto-renew is off. Doug's answer of 11-11-26 gave the prices but not this setting. Part 1 of `docs/setup-runbook.md` lists it as owed, with GoDaddy two-step sign-in and the second owner. *Waits on:* Doug, signed in to GoDaddy as businessmentors@dougbower.com.

11. **Load crm-test's training data into the Association's system (ruling 77).** Kickoff prompt `docs/prompts/cbm-client-intake-training-data-kickoff.md`, version 1.0, drafted 11-12-26. Doug reviews it, then pastes it into a new session in `~/Dropbox/Projects/cbm-client-intake`. That session's first deliverable is a plan, starting with a read-only count of what crm-test holds that no script made. *Waits on:* Doug's review of the prompt.

12. **Give `chapter-website-prototype` a GitHub copy.** It holds the chapter connector's only source (now 0.2.6), and its commits exist only on this machine under `~/Dropbox/Projects/chapter-website-prototype`. *Waits on:* Doug: which GitHub account or organization holds it.

---

## Done recently

- **11-12-26** — Ruling 77: the Association's training data comes from rerunning crm-test's training data scripts, with addresses on a domain that has no mailboxes. Answers decision D3 (demo chapter plan 0.6). Kickoff prompt drafted. Step 6, the drafted Cloudflare item, was put to Doug with a recommendation (record GoDaddy as registrar and Cloudflare for the domain name records as a ruling) and is still open.
- **11-11-26** — Step 3 done: ruling 76, two domains recommended to every chapter and counted in the chapter cost estimate, at about $21 a year each. Cost list 1.10, proposal summary 1.6, workbook generator, workbook and snapshot updated. The deployment guide in `cbm-client-intake` follows it (guide stage 3 version 0.8, planning document 1.5), committed there 11-11-26.
- **11-11-26** — Step 2 done: the domains' prices paid at GoDaddy, $20.88 (businessmentorsassociation.org) and $20.68 (mentorsassociation.org) a year, renewal the same, stated by Doug. Setup runbook Part 1 marked done (version 1.5); cost list 1.9, proposal summary 1.5, workbook generator, workbook and snapshot updated. Association total now about $5,154 a year, or $3,653 at nonprofit prices. Auto-renew on both domains is still to be checked; it was not in Doug's answer.
- **11-10-26** — The Association's Zoom credentials checked, read-only: Zoom issues a token and finds admin@mentorsassociation.org, licensed; webinars are refused without the Webinars add-on, as expected. Nothing was put into the Association's applications; the values go in through the chapter information form when the add-on is bought (Doug's choice). Recorded in `cbm-client-intake` commit 534efaa2, pushed: guide step 5.5, the setup plan and open item 73.
- **11-10-26** — Member Login opens in a new tab: chapter connector 0.2.6, installed on the test website. It goes to apps.businessmentorsassociation.org, the Association's own applications, whose first page is the sign-in screen.
- **11-10-26** — Member Login link moved to the footer's bottom line at Doug's request: chapter connector 0.2.5, installed on the test website.
- **11-10-26** — Chapter connector 0.2.4 installed on chapter-demo.mentorsassociation.org. The Member Login link shows on every page, lined up above "Request a Mentor", and opens the chapter applications' sign-in page. 0.2.4 fixes 0.2.3, which put the link at the window's far edge on a wide screen.
- **11-10-26** — A "Member Login" link added to the chapter website template: chapter connector 0.2.3, in `chapter-website-prototype` commit a1d6ed9. It sits in a slim bar above the header, because as a menu entry it pushed "Request a Mentor" onto a second line. It links to the chapter applications' address, whose root page is their sign-in page. Tested on desktop and phone width in the local prototype.
- **11-09-26** — The New Chapter Deployment Guide follows ruling 75: step 5.10 lists the five things any host must do, and stage 6 builds on the chosen host with Cloudways as the tested path (`cbm-client-intake` commits a20d43c3 and 2a084142; checked, no further change needed). `docs/website-hosting-comparison.md` corrected to version 1.2: Cloudways' 1 GB Standard server is $11 a month in the sign-up form, and the 2 GB server advised for a live site is $28 a month on the pricing page. Still to confirm in the Cloudways account: staging on the smallest plan, the default backup schedule, and the 2 GB Standard price.
- **11-09-26** — Ruling 29 reopened and replaced by ruling 75. Prices checked for Cloudways and Hostinger; a chapter now chooses its own host.
- **11-07-26** — Kickoff prompt reviewed and revised to version 1.2: commit and push rules for `cbm-client-intake`, where a push to `main` deploys production; the stale ruling numbers flagged; open decisions listed. Zoom confirmed as the video meeting service, so decision D4 is now the Zoom and Constant Contact plans.
- **11-07-26** — Ruling 72: the demo chapter is the Association itself. Kickoff prompt for correcting the guide drafted and approved; the two consequences of ruling 72 confirmed.
- **11-07-26** — Ruling 71: the demo system is built as a full new chapter by the deployment guide. The guide reviewed; findings and the two-track plan in `docs/demo-chapter-plan.md`.
- **11-07-26** — Ruling 25: two domains, businessmentorsassociation.org for the website and mentorsassociation.org for email. The setup runbook, cost list, proposal summary, workbook generator, workbook and number snapshot all updated.
- **11-07-26** — The rulings of 09-25-26 (ruling 23, a separate limited liability company; ruling 24, owned by the member chapters) merged with the website and domain work. Rulings of 11-06-26 and 11-07-26 renumbered from 23–68 to 25–70 across this repository.

---

## Prompt to start the next session

> Operating mode: ARCHITECTURE. Repository: `~/Dropbox/Projects/business-mentors-association`. Pull from GitHub first. Read `README.md`, `DECISIONS.md` and `NEXT-STEPS.md`. If I bring the closing report of the `cbm-client-intake` guide session, record it under step 0; otherwise take up the step I name, or step 6 if I name none. If I bring the closing report of the training data session, record it under step 11. Before changing anything in `cbm-client-intake`, read that repository's `CLAUDE.md` and follow its process. Before pushing `cbm-client-intake`, check `git log origin/main..HEAD`: other sessions commit to the same local `main`, and a push sends their commits too. At the end, update `NEXT-STEPS.md`, commit and push.

---

## Change log

| Version | Date | Change |
|---|---|---|
| 1.22 | 11-12-26 00:22 | Ruling 77 recorded; step 11 added for the training data kickoff; the prototype's GitHub copy renumbered to 12. |
| 1.21 | 11-11-26 23:15 | Steps 10 (GoDaddy auto-renew) and 11 (a GitHub copy of the prototype) added; the next-session prompt warns about other sessions' commits in `cbm-client-intake`. |
| 1.20 | 11-11-26 23:07 | Ruling 76 carried into the deployment guide. |
| 1.19 | 11-11-26 22:36 | Step 3 done: ruling 76. |
| 1.18 | 11-11-26 22:13 | Step 2 done and removed; step 3 notes the domain price; step 6 no longer waits on step 2. |
| 1.17 | 11-10-26 10:41 | Zoom credentials checked. |
| 1.16 | 11-10-26 09:03 | Connector 0.2.6 (new tab) installed; step 9 is now a second cache clear. |
| 1.15 | 11-10-26 01:45 | Member Login link moved to the footer (0.2.5); step 9 added to clear the test website's server cache. |
| 1.14 | 11-10-26 01:39 | Step 9 done: connector 0.2.4 installed on the test website. |
| 1.13 | 11-10-26 01:35 | Member Login link done in the prototype; step 9 added to install it on the test website. |
| 1.12 | 11-09-26 17:02 | Step 8 done and moved to Done recently; the service account key step renumbered to 8. |
| 1.11 | 11-09-26 14:51 | Step 8: step 5.10 done; stage 6 handed to the guide session; the comparison's Cloudways price to correct. |
| 1.10 | 11-09-26 14:21 | Step 8 corrected: the work is in the deployment guide, not the setup runbook. |
| 1.9 | 11-09-26 14:18 | Step 9 added: replace the Google service account key. |
| 1.8 | 11-09-26 14:10 | Ruling 75 recorded; step 8 added for the runbook. |
| 1.7 | 11-08-26 14:19 | Step 0: stages 6 to 8 progress, stage 9 blocked on CRMBuilder, rulings 73 and 74. |
| 1.6 | 11-08-26 09:54 | Step 0: the closing report of the `cbm-client-intake` guide session (stages 3 to 5 done, D4 answered, what is owed). Step 2: the registrar is GoDaddy. |
| 1.5 | 11-07-26 15:04 | The `cbm-client-intake` guide session started; step 0 now waits on its plan and report; the next-session prompt updated. |
| 1.4 | 11-07-26 15:00 | Kickoff prompt at version 1.2; Zoom confirmed, D4 narrowed. |
| 1.3 | 11-07-26 14:52 | Stop B passed; step 0 now points at the approved kickoff prompt. |
| 1.2 | 11-07-26 14:47 | Step 0 updated for ruling 72 and the guide kickoff prompt; step 4 now decision D1a. |
| 1.1 | 11-07-26 14:38 | Step 0 added for the demo chapter (ruling 71); step 4 folded into its decision D1. |
| 1.0 | 11-07-26 14:29 | First version, written at the end of the session that corrected ruling 25 and merged the two lines of work. |
