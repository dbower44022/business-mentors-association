# Business Mentors Association — proposal summary

**Document:** Executive summary of the proposal to form a shared technical services association for business mentoring chapters
**Version:** 1.2
**Status:** Draft for review
**Owner:** Doug Bower
**Last Updated:** 09-25-26

---

## The proposal in one paragraph

Independent business mentoring nonprofits would form the Business Mentors Association (a working name) to share one set of client-management and mentoring applications, instead of each chapter building and maintaining its own. The Association is **a separate limited liability company (LLC)**, so its liabilities stay with it and do not reach the chapters. It builds, tests and supports the applications. Each chapter keeps full ownership of its own systems and data, runs the same application as every other chapter, and has a vote on every release. The applications become open source, so a chapter that leaves keeps everything it runs.

## Why a separate company

This is the point most easily missed, and it is why the Association is not run as a joint project between chapters.

The Association will hold administrative access to chapters' systems, run shared infrastructure, sign contracts with vendors, and take responsibility for software that handles client and mentor records. Work of that kind carries risk: a data breach, a vendor bill that goes unpaid, a dispute over a release that lost someone's data.

A separate limited liability company is the thing those claims land on. Set up properly, a claim against the Association is a claim against the Association's own assets, not against each chapter's building, endowment or donor funds. **Each chapter's exposure is limited to what it puts in** — its dues, and its own systems, which it owns and controls anyway.

Run instead as an informal joint effort, or as a program inside one chapter, the same claim would reach the chapters themselves, or reach that one chapter. No small nonprofit should take that on for its peers, and no board should be asked to approve it.

The company is expected to be owned by its member chapters. **Two questions go with that and need an attorney:** whether the company also seeks tax-exempt status, which a limited liability company does not get automatically and which the tax authorities allow only under set conditions when every owner is itself exempt; and how this fits the earlier plan to start under fiscal sponsorship, which suits a project rather than a company. Both are recorded in the open questions.

## Why share at all

The applications already exist and have run Cleveland Business Mentors' operations in production. Other chapters want them. Building a separate copy for each chapter would multiply the cost of every fix and every improvement. One application, maintained once and shared, keeps that cost flat as chapters join. The trade is that no chapter customises the application on its own: a chapter that wants a change asks for it, and if accepted, every chapter gets it.

## What a member chapter gets and gives

**It gets:** the applications and their configuration, a new release when one is approved, help for its own technical volunteer, direct help on its system when that volunteer is unavailable, a step-by-step guide for setting up a new chapter's technology, a shared system for training and testing, and the liability shield described above.

**It keeps:** ultimate authority over all of its own technology. It owns its own hosting, domain, email and password vault, and it decides when to install each release. There is no deadline to update.

**It gives:** dues set by size band, a technical contact and a representative, testing of each release before the vote, and an agreement to run the application as designed rather than altering it. Chapters differ only through optional settings and their own processes.

## How decisions are made

**Releases.** The Association builds and tests each release. Chapters' technical people test it on the shared system. The representatives then vote.

**Votes.** Larger chapters pay more and carry more votes. A vote passes only with both a majority of the weighted votes and a majority of the chapters, so no single chapter, large or small, can decide alone.

**Features.** Requests go to a technical committee with one technical contact from each chapter. When membership grows past a set size, the committee becomes a smaller elected group.

**Money, staffing and membership.** Which body governs these is the committee's first decision. The recommended answer is a small elected board.

## Structure

- **Legal form:** a separate limited liability company, owned by its member chapters, formed to keep its liabilities away from them.
- **Members:** independent business mentoring nonprofits only.
- **Scope:** technical services only, for now.
- **Staffing:** volunteers at first. The committee decides later whether to pay for staff.
- **Ownership of the software:** the chapter applications become open source. The tool used to build and configure each chapter's system stays the property of its developer, Doug Bower.
- **Its own accounts:** its own domain (businessmentorsassociation.org), email, password vault and hosting, each with at least two owners, so no one person holds the keys. The shared training and testing system moves from Cleveland's account to the Association's.

## What it costs

**The Association** costs roughly $3,500 to $5,000 a year to run, depending on whether it qualifies for the nonprofit pricing that Anthropic, Google and EspoCRM offer. Dues cover that. See [cost-list.md](cost-list.md). Whether a limited liability company qualifies for that nonprofit pricing is now one of the open questions, and it is worth roughly $1,500 a year to the Association.

**Each chapter** pays its own hosting, email, extension licences and password vault: roughly $1,100 to $1,450 a year at nonprofit prices, whatever its size. Dues come on top of that and are not yet decided.

## What could go wrong

**The Association depends on one volunteer.** Today one person can build releases and fix the applications. Until a second person is trained, that is the Association's largest risk.

**A liability shield has to be maintained, not just formed.** It protects the chapters only while the company keeps its own accounts, its own records and its own decisions separate from theirs. Sloppy bookkeeping, or a chapter paying the company's bills directly, is how a shield is argued away.

**Chapters will drift apart.** With no deadline to update, support must handle whatever version a chapter runs, and a security fix reaches a chapter only when it installs the fix.

**The no-changes rule rests on trust.** Chapters hold their own administrator accounts. The rule against altering the application is kept by agreement, not by a technical lock.

**Training and testing share one system.** It is cheaper, but trainees may meet a release that is still being tested.

## Still to decide

Whether the company seeks tax-exempt status, and how fiscal sponsorship fits. The open-source licence. The size bands, dues and votes per band. The body that governs money and staffing. Admission requirements. The chapter agreement, whose current draft predates these decisions. The second account owner. The full list is in [../OPEN-QUESTIONS.md](../OPEN-QUESTIONS.md).

## Next steps

1. Have a nonprofit attorney confirm the company structure, its ownership by the chapters, and its tax treatment.
2. Register the domain and open the Association's accounts, each with two owners — [setup-runbook.md](setup-runbook.md).
3. Bring the chapter agreement into line with this proposal.
4. Hold the committee's first meeting, to settle the governing body and the dues.

---

## Change log

| Version | Date | Change |
|---|---|---|
| 1.2 | 09-25-26 | The Association is a separate limited liability company, formed to shield the chapters (ruling 23). New section on why a separate company; the structure, costs, risks and next steps updated to match. |
| 1.1 | 09-25-26 | Moved into this repository. Cost figures added from the cost list; the open questions now point to the repository's own list. |
| 1.0 | 09-19-26 | First version, summarising the rulings of 09-19-26. |
