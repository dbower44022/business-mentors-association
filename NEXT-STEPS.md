# Next steps — where the work stands

**Document:** The work in progress and the next steps, kept so a new session can continue where the last one stopped
**Version:** 1.0
**Status:** Current
**Owner:** Doug Bower
**Last Updated:** 11-07-26 14:31

---

## How to use this file

A new session reads this file after `README.md` and `DECISIONS.md`. Each item says what is owed, why, and what it waits on. When an item is done, it is moved to "Done recently" with its date. Items here are tasks, not rulings: a ruling exists only in `DECISIONS.md`.

**Before starting work, pull from GitHub. At the end of a session, commit and push.** On 11-07-26 two lines of work had both been kept unpushed, and both had used ruling numbers 23 and 24. Fixing that took a renumbering of 46 rulings.

---

## Next steps, in recommended order

1. **Correct the stale ruling numbers in `cbm-client-intake`.** `prds/chapter-website-plan.md` in `dbower44022/cbm-client-intake` cites this repository's rulings by their old numbers: "rulings 24 to 68", "Ruling 45", "Ruling 48", "Rulings 64…". Every ruling from 23 to 68 is now two higher (see the 2.29 entry in this repository's `DECISIONS.md` change log). That repository has its own change process. Read its `CLAUDE.md` first, and make the change only through that process. *Waits on:* Doug's go-ahead to start it there.

2. **Bring the setup runbook in line with what is already done.** Both domains are registered (ruling 25), but Part 1 of `docs/setup-runbook.md` still tells the reader to search for them and buy them. Mark Part 1 as done, and record the registrar and the price actually paid. Then replace the estimate in the "Domains" line of `docs/cost-list.md` and in `costs/build_workbook.py`, which still say "about $11 / year each" and "not checked at the registrar". *Waits on:* Doug: which registrar holds the two domains, the price paid, and whether auto-renew is on.

3. **Decide whether the chapter cost estimate counts two domains.** Ruling 25 says the Association registered two domains "the way the Association recommends for every chapter". The chapter cost section of `docs/cost-list.md`, and the Chapter costs sheet that `costs/build_workbook.py` builds, still count one domain per chapter at about $11 a year. The chapter network's deployment guide in `cbm-client-intake` still calls one domain or two an open question. *Waits on:* Doug: is two domains the recommendation, or one of two options?

4. **Decide the test website's address.** Ruling 70 places the test chapter website at chapter-demo.mentorsassociation.org. Under ruling 25 that is the email domain, not the website domain (businessmentorsassociation.org). The chapter deployment guide allows a website address under either domain, so this may be intended. *Waits on:* Doug: keep the address, or move it to the website domain.

5. **Open question 30: the legal name.** `OPEN-QUESTIONS.md` asks whether the working name and the domain match the legal name. The domain names are now settled (ruling 25), and the company form is settled (ruling 23). The legal name is the remaining part. *Waits on:* Doug.

6. **Confirm or drop the drafted Cloudflare item.** The "Drafted by Claude" section of `DECISIONS.md` proposes that the Association's domains are registered through Cloudflare and their domain name records kept there. Step 2 answers the registrar part. *Waits on:* step 2.

7. **Correct `cbm-client-intake`'s chapter network decision file.** Its `prds/chapter-network/DECISIONS.md` still states rulings that this repository's rulings 1 to 3 replaced (noted in `README.md`). Same process rule as step 1. *Waits on:* Doug's go-ahead, best done together with step 1.

---

## Done recently

- **11-07-26** — Ruling 25: two domains, businessmentorsassociation.org for the website and mentorsassociation.org for email. The setup runbook, cost list, proposal summary, workbook generator, workbook and number snapshot all updated.
- **11-07-26** — The rulings of 09-25-26 (ruling 23, a separate limited liability company; ruling 24, owned by the member chapters) merged with the website and domain work. Rulings of 11-06-26 and 11-07-26 renumbered from 23–68 to 25–70 across this repository.

---

## Prompt to start the next session

> Operating mode: ARCHITECTURE. Repository: `~/Dropbox/Projects/business-mentors-association`. Pull from GitHub first. Read `README.md`, `DECISIONS.md` and `NEXT-STEPS.md`. Then take up step 1 of `NEXT-STEPS.md` unless I name another step. Before changing anything in `cbm-client-intake`, read that repository's `CLAUDE.md` and follow its process. At the end, update `NEXT-STEPS.md`, commit and push.

---

## Change log

| Version | Date | Change |
|---|---|---|
| 1.0 | 11-07-26 14:31 | First version, written at the end of the session that corrected ruling 25 and merged the two lines of work. |
