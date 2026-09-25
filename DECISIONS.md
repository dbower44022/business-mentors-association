# Decisions — the Association's rulings

**Document:** Every ruling that defines the Business Mentors Association
**Version:** 2.0
**Status:** Current
**Owner:** Doug Bower
**Last Updated:** 09-25-26

---

## How to use this file

Nothing here is a task. **Every ruling below is Doug's.** A ruling changes only when Doug changes it, and then the replaced wording stays visible, marked and dated. Items Claude drafted or assumed are in their own sections at the bottom and are not rulings until Doug confirms them.

The rulings of 09-19-26 came out of one planning conversation. Several of them replace rulings made earlier for the chapter network, whose decision file lives in `dbower44022/cbm-client-intake` at `prds/chapter-network/DECISIONS.md`. **That file still states the replaced wording**; correcting it is owed.

---

## Rulings

### Ruled 09-19-26

1. **Chapters hold ultimate authority over all their own technology.** The Association supports each chapter's own technical personnel. Association staff work directly on a chapter's system only when the chapter's support contact is unavailable. *Replaces the chapter network's ruling that the central organization holds the only administrator accounts.*

2. **Releases.** The Association builds and tests each release of the application files. Chapter technical personnel test and certify it. Each chapter's technical personnel then agree a deployment date with their chapter, so chapters may run slightly different versions for a time. *Replaces the chapter network's ruling that all chapters move to each release together.*

3. **One application.** Chapters deploy the application as the Association designs it and do not change it. A chapter that wants something new — a field, for example — submits a feature request; the central technical committee considers it, and if accepted it is built and delivered to every chapter. Chapters may differ through optional settings and different processes; the application itself is the same everywhere. *Amends the chapter network's ruling of strictly identical function, which allowed no per-chapter difference at all.*

4. **A release goes forward on a vote of the chapter representatives**, under a process written into the Association's bylaws or operating procedures. The vote is counted as a double majority — see rulings 11 and 12.

5. **Legal form: fiscal sponsorship first.** An established nonprofit holds the Association's money and signs for it. Becoming an independent nonprofit is a high priority.

6. **The chapter applications become open source. Doug Bower continues to own CRM Builder.**

7. **The Association's records live in their own repository.** Ruled as `BusMentAssociation/contact`; **superseded 09-25-26** by this repository, `dbower44022/business-mentors-association`. The records are not kept anywhere else.

8. **Scope: technical services only, for now.** Whether the Association later offers non-technical services is left open, and no process for adding services is defined at this time.

9. **Membership: independent business mentoring nonprofits only.**

10. **The central technical committee has one technical contact from every member chapter while membership is small.** Once membership passes a number set in the bylaws, it becomes a small committee whose seats are elected by the chapter representatives, with the Association's technical lead alongside them.

11. **Dues and voting are set in size bands.** Larger chapters pay more and have more say.

12. **Votes pass by double majority.** A vote needs both a majority of the weighted votes and a majority of the member chapters, so no chapter can carry a vote alone, large or small.

13. **The Association starts with volunteers.** Development and support are done by volunteers at first; the committee decides later whether and when to pay for staff.

14. **Which body governs the Association's money, staffing and membership is left to the committee.** The options in front of it: the chapter representatives as a members' council; a small board elected by the representatives; or the technical committee governing as well.

15. **The shared test system moves to a new server the Association owns.** Today's test system is reproduced on, or moved to, an Association-owned server. It holds test data rather than Cleveland's data, the training is built on that data, and it is restored every night at midnight; all three come with it. The trial chapter system is not used for this, because it has neither training data nor a nightly restore.

16. **One system serves both training and release testing.** A second system costs more than it is worth, and testing against the realistic test data makes usability testing easier. The release waiting for certification is installed on the shared test system, and training runs on whatever version is installed.

17. **No limit on how far behind the current release a chapter may fall.** It is not worth enforcing. The Association neither requires chapters to update by a deadline nor limits support to recent releases.

18. **The Association's accounts are held in its own name, and the domain comes first.** Each account — hosting, code hosting, request system and the rest — is opened under an Association email address, with at least two volunteer owners and the sign-ins kept in an Association-owned password vault, billed to the fiscal sponsor once one exists.

19. **The Association's domain is businessmentorsassociation.org.** Availability has not been confirmed at the registrar.

20. **The Association's email runs on Google Workspace** — the same system every chapter uses. Accepted cost: a fee per person per month until the Association qualifies for the free nonprofit edition.

### Ruled 09-20-26

21. **Nonprofit pricing is assumed where it exists.** The Advanced Pack extension costs $395 a year at standard price and $295 a year at EspoCRM's nonprofit price. Anthropic offers nonprofits an 80 percent discount. Google Workspace has a free nonprofit edition. Each requires the Association to qualify as a nonprofit.

### Ruled 09-22-26

22. **Chapter cost estimates exclude Association dues.** Dues are not decided and are reported separately from what a chapter pays itself.

---

## Decisions the committee will make

- Whether and when to pay for staff (ruling 13).
- Which body governs money, staffing and membership (ruling 14).
- The size bands, their shares and the dues amounts (ruling 11).

---

## Drafted by Claude — not yet confirmed by Doug

These are not rulings. Each one either follows from a ruling or fills a gap, and each waits on Doug.

- **"The committee" in rulings 13 and 14** is read as the central technical committee of ruling 10 — one technical contact from each member chapter — because it is the only committee defined.
- **Everyday requests** (adding a person, resetting a password) are done by each chapter's own technical personnel, with the Association as backup. This follows from ruling 1 and would replace the chapter network's 09-18-26 ruling that the Association's support team handles them as they arrive.
- **A second trained volunteer.** Recommended practice: train a second volunteer to build releases and back up support, so the Association does not depend on one person.
- **Release notice and test data.** Chapters are told in advance when a release waiting for certification is installed on the shared test system, so a trainer knows which version the trainees will meet. Testers are told that the midnight restore returns the data to its starting point, so records they create while testing are gone the next morning; the restore resets the data, not the installed version.
- **A record of versions.** The Association keeps a record of which release each chapter runs, so a support request starts from the right version.
- **Cloudflare for the domain.** The Association's domain is registered through Cloudflare and its domain name records kept there, the same arrangement already ruled for every chapter.
- **Membership requirements.** Proposed: own your infrastructure, name a technical contact and a representative, sign the chapter agreement, adopt the application as designed. Also proposed: admission confirmed by a member vote.

---

## Change log

| Version | Date | Change |
|---|---|---|
| 2.0 | 09-25-26 | Moved into this repository from the interim Claude project document. Ruling 7 superseded: the records live here. Rulings 21 and 22 added from the cost work of 09-20-26 and 09-22-26. |
| 1.x | 09-19-26 to 09-22-26 | Kept as an interim document in the Claude project while this repository could not be written to. Twenty rulings from the planning conversation of 09-19-26, then the cost rulings. |
