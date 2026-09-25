# Business Mentors Association — cost list for setting dues

**Document:** Every cost the Association's dues must cover, plus what each chapter pays itself
**Version:** 1.7
**Status:** Draft for review
**Owner:** Doug Bower
**Last Updated:** 09-25-26

---

## What this list is for

Dues must cover the Association's own costs (ruling 11). Sections 1 to 5 name each one, give a current price where one could be found, and say how sure that price is. **Section 6 covers what a chapter pays itself**, in its own accounts. The two are kept apart: dues are not decided, and they are reported separately (ruling 22).

**The working figures are in a spreadsheet**, `association-costs.xlsx`, which calculates the Association's totals, shows how they would split into dues by size band, and estimates a chapter's own costs for three example sizes. This document explains the lines; the spreadsheet does the arithmetic. **The spreadsheet is not yet committed to this repository** — Claude's tool writes text files only, so it must be added by hand.

**Estimated Association total: about $5,120 a year at standard prices, or about $3,620 a year once the Association qualifies for the nonprofit programs.** Both include a 10 percent fee for an outside body holding the money, a 10 percent contingency, and a statutory agent. Both assume the Association buys its own insurance; if a sponsor's policies cover it, take about $1,300 off.

**Three nonprofit programs change the total** (ruling 21), and each needs the Association to qualify:

- **Anthropic** discounts by 80 percent, which is the single largest saving on the list.
- **Google Workspace** has a free edition for nonprofits, which removes the mailbox cost entirely.
- **EspoCRM** prices the Advanced Pack extension at $295 a year instead of $395.

**Rulings 23 and 24 put these in question.** The Association is a limited liability company owned by its member chapters. A company is not a nonprofit, so each program's eligibility has to be confirmed. Ownership by exempt chapters is what keeps the door open, and an attorney should confirm the tax treatment.

**Confidence.** Prices marked "published" were read from the vendor's page or a current pricing summary. "Stated" means Doug supplied it. "Estimate" means a reasoned figure not checked against a bill. The test system's figures have not been checked against Cleveland Business Mentors' actual invoices, which would be the better source.

---

## 1. Recurring — infrastructure the Association owns

| Cost | What it pays for | Standard price | Nonprofit price | Confidence |
|---|---|---|---|---|
| Domain | businessmentorsassociation.org, registered through Cloudflare | about $11 / year | Same | Estimate; not checked at the registrar |
| Shared test system — CRM server | The server holding the shared training and testing CRM (ruling 15). Same size as the trial chapter's, 4 GB memory | $24 / month — $288 / year | Same | Published |
| Shared test system — server backups | Weekly backups of that server, charged at 20 percent of its price | $4.80 / month — $58 / year | Same | Published |
| Shared test system — application | The chapter applications running against the test CRM | $5 to $12 / month — $60 to $144 / year | Same | Estimate from published container prices; depends on the size Cleveland's test application uses today |
| Shared test system — application database | The application's own database | $7 to $15 / month — $84 to $180 / year | Same | $7 development database is published; a managed database costs more |
| Advanced Pack licence for the test CRM | The extension the network standard requires on every CRM | **$395 / year** | **$295 / year** | Both stated by Doug. The vendor says one licence covers a buyer's own test and production systems; whether the Association's test system can share Cleveland's licence is **not settled** |

**Subtotal: about $900 to $1,080 a year, or about $800 to $980 at the nonprofit extension price.**

## 2. Recurring — tools and services

| Cost | What it pays for | Standard price | Nonprofit price | Confidence |
|---|---|---|---|---|
| Google Workspace | Two paid mailboxes (the two account owners, ruling 18). admin@, support@ and releases@ are groups, which cost nothing | $7 / person / month on the annual plan — $168 / year | **Free** once qualified | Published price; free nonprofit edition stated by Doug |
| Password vault (Proton Pass) | The Association Operations vault. Business plans require at least 3 people | $1.99 to $4.49 / person / month × 3 — $72 to $162 / year | Same | Published (third-party summary) |
| Request system (ClickUp) | The one system for feature requests, defects and support | Free, or $7 / person / month × 3 — $252 / year | Same | Published |
| AI development tool (Claude) | The applications are written and maintained with Claude. The volunteer doing development needs a plan with high usage | $100 to $200 / month — $1,200 to $2,400 / year | **80 percent less** — $240 to $480 / year | Published price; nonprofit discount stated by Doug |
| Code hosting (GitHub) | The Association's repositories | Free | Free | Published |

**Subtotal: about $1,440 to $2,980 a year at standard prices, or about $310 to $890 once the nonprofit programs apply.**

## 3. Recurring — the company itself

| Cost | What it pays for | Price | Confidence |
|---|---|---|---|
| Statutory agent | Ohio requires every company to keep an agent with a physical Ohio address, available in business hours, to receive legal notices. A member or volunteer with an Ohio address may serve for nothing; a service charges yearly | $0, or about $125 / year (services range from about $99 to $300) | Published range |
| Annual report to the state | Ohio does not require one from a company, and charges no yearly fee | $0 | Published |
| Money held by an outside body | If an established nonprofit holds the Association's money under a sponsorship arrangement (ruling 5, now in question), it charges a percentage | 5 to 15 percent of funds received; 3 to 8 percent for the lighter form | Published range |
| Directors and officers insurance | Protects the volunteers who make decisions for the Association | about $800 / year, or $0 if another body's policy covers it | Published average for a nonprofit; a company's cover may differ |
| General liability insurance | Claims arising from the Association's activities | about $500 / year, same note | Published average |
| Cyber liability insurance | The Association's volunteers can reach chapters' systems, which hold client and mentor records (ruling 1) | **Price needed** | Not priced |
| Contingency | Price rises and surprises | 10 percent | Rule of thumb |

## 4. One-time — forming the company

These are a company's costs, not a nonprofit's (rulings 23 and 24).

| Cost | Price | Confidence |
|---|---|---|
| Ohio articles of organization | $99 | Published |
| Trade name registration | $39, only if the Association operates publicly under a name different from its registered one | Published |
| Operating agreement, drafted or reviewed by an attorney | **Price needed** — ask for a quote | Not priced. **This is the document that does the work of the liability shield** and that carries the release vote, the double majority and the chapters' ownership |
| Attorney review of the chapter agreement and the open-source licence | **Price needed** — ask for the same quote | Not priced |
| Federal tax-exemption application | $275 (short form) or $600 (full form), **only if the company seeks exempt status** | Published (IRS). Not required to operate |
| Federal employer identification number | $0 | Published |
| Moving the shared test system to the new server | Volunteer time, no cash cost | Estimate |

**Subtotal: about $99 to $738 in fees**, plus the attorney, whose quote is likely to be the largest single item.

## 5. Future — only if the committee decides

| Cost | Note |
|---|---|
| Paid staff | Ruling 13 starts with volunteers; the committee decides later whether to pay anyone. A part-time role would outweigh every other line on this list combined, so it would change dues entirely |
| Volunteer expense reimbursement | Only if the governing body adopts a policy |
| Tax filings | A company that does not hold exempt status has its own filing obligations, and the members are nonprofits receiving a share of it. An accountant should say what this costs |

---

## 6. Estimated chapter costs — what a chapter pays itself

Each chapter pays these directly, in its own accounts, as the chapter network rulings require. **Association dues are not included here** (ruling 22). The figures assume the chapter qualifies as a nonprofit, which every member chapter does (ruling 9). The spreadsheet's **Chapter costs** sheet holds the same lines, with every quantity editable.

**Three example sizes.** Small is 4 staff and 10 mentors; medium is 10 staff and 40 mentors; large is 20 staff and 100 mentors.

| Cost | Price | Small | Medium | Large |
|---|---|---|---|---|
| CRM server (4 GB) | $24 / month | $288 | $288 | $288 |
| CRM server backups | 20 percent of the server | $58 | $58 | $58 |
| Application container | $12 / month | $144 | $144 | $144 |
| Application database | $15 / month, managed | $180 | $180 | $180 |
| Domain name | about $11 / year | $11 | $11 | $11 |
| Domain name records (Cloudflare) | Free | $0 | $0 | $0 |
| Google Workspace — staff and mentor mailboxes | Free nonprofit edition | $0 | $0 | $0 |
| Advanced Pack extension licence | $295 / year (nonprofit price) | $295 | $295 | $295 |
| Google Integration extension licence | **Price needed** | — | — | — |
| Password vault | $4.49 / person / month, at least 3 people | $162 | $162 | $269 |
| Video meeting account | about $16 / month, only for public webinars | $0 | $192 | $192 |
| **Chapter's own costs** | | **$1,137** | **$1,329** | **$1,437** |

**Nonprofit status is what makes this affordable.** At standard prices the same chapters would pay about $2,410, $5,630 and $11,620 a year. Almost all of that difference is mailboxes: a large chapter's 120 mailboxes cost about $10,000 a year at $7 each per month, and nothing on the free nonprofit edition.

**A larger chapter costs the Association no more to serve.** Its own costs barely rise with size, because the application and CRM are the same. If larger chapters contribute more, that follows from the shares in ruling 11, not from a larger cost to serve.

**Not included:** Association dues, the chapter's own website, its staff time, and anything it already pays for.

---

## How these become dues

Take the Association's annual total and split it across the size bands (ruling 11), in proportion to the share each band carries. The spreadsheet does this: enter the number of chapters in each band and the share per band, and it gives the dues per chapter under both standard and nonprofit prices.

As an example, with one chapter in each of three bands carrying shares of one, two and three, yearly dues come to roughly $850, $1,700 and $2,560 at standard prices, or about $600, $1,200 and $1,810 at the nonprofit prices.

The bands, their shares and the amounts are the committee's to set. Nothing here is decided.

## Sources

- Prices stated by Doug (09-19-26 and 09-20-26): the Advanced Pack licence at $395, its nonprofit price of $295, the Anthropic nonprofit discount, and the free Google Workspace nonprofit edition.
- Ohio company filing fee, the absence of an annual report, and statutory agent costs: [LLCForge — Ohio LLC cost](https://llcforge.com/llc-costs/ohio/); [LLC University — Ohio registered agent](https://www.llcuniversity.com/ohio-llc/registered-agent/)
- Google Workspace prices: [emailtooltester.com — Google Workspace pricing 2026](https://www.emailtooltester.com/en/blog/google-workspace-pricing/); nonprofit offer: [Google for Nonprofits — Workspace](https://www.google.com/nonprofits/offerings/workspace/)
- Claude prices: [claude.com/pricing](https://claude.com/pricing); nonprofit discounts reported at [NonProfit PRO — Claude for Nonprofits](https://www.nonprofitpro.com/article/claude-for-nonprofits-launches-with-sector-discounts-data-connectors-and-training/)
- DigitalOcean server and backup prices: [digitalocean.com/pricing/droplets](https://www.digitalocean.com/pricing/droplets); application and database prices: [digitalocean.com/pricing/app-platform](https://www.digitalocean.com/pricing/app-platform)
- Proton Pass business prices: [ifeeltech.com — Proton Pass Business review](https://ifeeltech.com/blog/proton-pass-business-review)
- ClickUp prices: [clickup.com/pricing](https://clickup.com/pricing)
- Sponsorship fees: [Holistic Underground — fiscal sponsorship fees](https://www.holisticunderground.org/fiscal-sponsorship/fees)
- Insurance averages: [Insureon — cost of nonprofit insurance](https://www.insureon.com/nonprofit-business-insurance/cost)
- Extension licensing for test systems: [EspoCRM forum — one licence for development and production](https://forum.espocrm.com/forum/extensions/125844-advanced-pack-and-extensions-one-instance-for-development-and-production)
- Federal exemption application fee: [IRS — Form 1023 user fee](https://www.irs.gov/charities-non-profits/form-1023-and-1023-ez-amount-of-user-fee)

---

## Change log

| Version | Date | Change |
|---|---|---|
| 1.7 | 09-25-26 | Formation costs rewritten for a limited liability company (rulings 23 and 24): Ohio articles of organization, trade name registration, the operating agreement, and the federal exemption application only if exempt status is sought. A statutory agent added as a recurring cost. Totals restated at about $5,120 and $3,620. Nonprofit pricing flagged as needing confirmation for a company. |
| 1.6 | 09-25-26 | Moved into this repository; ruling numbers now point to this repository's decision file. |
| 1.5 | 09-22-26 | Association dues removed from the chapter cost section and from the Chapter costs sheet. |
| 1.4 | 09-20-26 | Estimated chapter costs added for three sizes. |
| 1.3 | 09-20-26 | EspoCRM's nonprofit price of $295 a year for the Advanced Pack added. |
| 1.2 | 09-20-26 | Advanced Pack priced at $395 a year; the Google and Anthropic nonprofit programs added as a second price column. |
| 1.1 | 09-19-26 | Corrected the arithmetic on the low end of the total, the sponsor's fee and the contingency. |
| 1.0 | 09-19-26 | First version. |
