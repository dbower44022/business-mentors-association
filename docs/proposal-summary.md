# Business Mentors Association — proposal summary

**Document:** Executive summary of the proposal to form a shared technical services association for business mentoring chapters
**Version:** 1.1
**Status:** Draft for review
**Owner:** Doug Bower
**Last Updated:** 09-25-26

---

## The proposal in one paragraph

Independent business mentoring nonprofits would form the Business Mentors Association (a working name) to share one set of client-management and mentoring applications, instead of each chapter building and maintaining its own. The Association builds, tests and supports the applications. Each chapter keeps full ownership of its own systems and data, runs the same application as every other chapter, and has a vote on every release. The applications become open source, so a chapter that leaves keeps everything it runs.

## Why

The applications already exist and have run Cleveland Business Mentors' operations in production. Other chapters want them. Building a separate copy for each chapter would multiply the cost of every fix and every improvement. One application, maintained once and shared, keeps that cost flat as chapters join. The trade is that no chapter customises the application on its own: a chapter that wants a change asks for it, and if accepted, every chapter gets it.

## What a member chapter gets and gives

**It gets:** the applications and their configuration, a new release when one is approved, help for its own technical volunteer, direct help on its system when that volunteer is unavailable, a step-by-step guide for setting up a new chapter's technology, and a shared system for training and testing.

**It keeps:** ultimate authority over all of its own technology. It owns its own hosting, domain, email and password vault, and it decides when to install each release. There is no deadline to update.

**It gives:** dues set by size band, a technical contact and a representative, testing of each release before the vote, and an agreement to run the application as designed rather than altering it. Chapters differ only through optional settings and their own processes.

## How decisions are made

**Releases.** The Association builds and tests each release. Chapters' technical people test it on the shared system. The representatives then vote.

**Votes.** Larger chapters pay more and carry more votes. A vote passes only with both a majority of the weighted votes and a majority of the chapters, so no single chapter, large or small, can decide alone.

**Features.** Requests go to a technical committee with one technical contact from each chapter. When membership grows past a set size, the committee becomes a smaller elected group.

**Money, staffing and membership.** Which body governs these is the committee's first decision. The recommended answer is a small elected board, because the independent nonprofit will need one.

## Structure

- **Members:** independent business mentoring nonprofits only.
- **Scope:** technical services only, for now.
- **Legal form:** it starts under fiscal sponsorship, where an established nonprofit holds its money. Becoming an independent nonprofit is a high priority.
- **Staffing:** volunteers at first. The committee decides later whether to pay for staff.
- **Ownership:** the chapter applications become open source. The tool used to build and configure each chapter's system stays the property of its developer, Doug Bower.
- **Its own accounts:** its own domain (businessmentorsassociation.org), email, password vault and hosting, each with at least two owners, so no one person holds the keys. The shared training and testing system moves from Cleveland's account to the Association's.

## What it costs

**The Association** costs roughly $3,500 to $5,000 a year to run, depending on whether it qualifies for the nonprofit pricing that Anthropic, Google and EspoCRM offer. Dues cover that. See [cost-list.md](cost-list.md).

**Each chapter** pays its own hosting, email, extension licences and password vault: roughly $1,100 to $1,450 a year at nonprofit prices, whatever its size. Dues come on top of that and are not yet decided.

## What could go wrong

**The Association depends on one volunteer.** Today one person can build releases and fix the applications. Until a second person is trained, that is the Association's largest risk.

**Chapters will drift apart.** With no deadline to update, support must handle whatever version a chapter runs, and a security fix reaches a chapter only when it installs the fix.

**The no-changes rule rests on trust.** Chapters hold their own administrator accounts. The rule against altering the application is kept by agreement, not by a technical lock.

**Training and testing share one system.** It is cheaper, but trainees may meet a release that is still being tested.

## Still to decide

The fiscal sponsor. The open-source licence. The size bands, dues and votes per band. The body that governs money and staffing. Admission requirements. The chapter agreement, whose current draft predates these decisions. The second account owner. The full list is in [../OPEN-QUESTIONS.md](../OPEN-QUESTIONS.md).

## Next steps

1. Register the domain and open the Association's accounts, each with two owners — [setup-runbook.md](setup-runbook.md).
2. Choose a fiscal sponsor.
3. Bring the chapter agreement into line with this proposal.
4. Hold the committee's first meeting, to settle the governing body and the dues.

---

## Change log

| Version | Date | Change |
|---|---|---|
| 1.1 | 09-25-26 | Moved into this repository. Cost figures added from the cost list; the open questions now point to the repository's own list. |
| 1.0 | 09-19-26 | First version, summarising the rulings of 09-19-26. |
