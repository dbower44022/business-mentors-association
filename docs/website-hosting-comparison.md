# Website hosting — Cloudways and Hostinger compared

**Document:** Checked prices and features for reopening ruling 29, where a chapter's WordPress site is hosted
**Version:** 1.1
**Status:** Decided — ruling 75 (option 3)
**Owner:** Doug Bower
**Last Updated:** 11-09-26 14:10

---

## Why this exists

Ruling 29 put every chapter's WordPress site on Cloudways, a lightly managed host running on a DigitalOcean server. The ruling's cost figure was marked "prices from memory, not yet checked", and it recorded no reason for choosing Cloudways over a fully managed WordPress host. Cleveland's website maintainer has since recommended Hostinger instead. Doug reopened the ruling on 11-09-26 and asked for checked prices. Nothing here is a ruling. **Doug ruled on 11-09-26 (ruling 75):** option 3. A chapter chooses its own host; the Association runs its own websites on Cloudways and tests only there.

## The finding

**Hostinger costs about $550 less per chapter over the first four years. After that, it costs slightly more per year than Cloudways.** Both meet the hosting requirements WT-90 to WT-92, as long as the chapter buys Hostinger's second plan, Unlimited. The plan the maintainer quoted, about $100 for four years, is Hostinger's first plan, Premium. It takes backups weekly, not daily, so it does not meet WT-90.

**Being on DigitalOcean gives Cloudways no technical advantage.** Cloudways bills separately from DigitalOcean. The website reaches the chapter applications over the public internet with either host. The chapter connector needs nothing that Hostinger does not allow.

## The two hosts against the requirements

| Requirement | Cloudways, smallest plan ("Micro") | Hostinger Unlimited |
|---|---|---|
| Operating system and PHP kept up to date by the host (WT-90) | Yes, as a managed host. Not stated plan by plan on the pages read | Yes, managed WordPress hosting |
| Daily backups (WT-90) | Automated backups, required and cannot be turned off. Schedule is set by the chapter. Off-site storage charged at $0.033 per gigabyte per month | Daily backups, with easy restore |
| Security certificate (WT-90) | Free, built in | Free |
| Staging copy (WT-90) | One-click staging. Whether the smallest plan includes it was not confirmed | One-click staging, stated for every plan |
| Never on the same server as the customer relationship management system (WT-92) | Met. The site has its own small server | Met. The site shares a server with other customers' websites, but never with the chapter's own system |
| Automatic WordPress updates (WT-91) | Set inside WordPress | Built in |
| Malware scanning | Not on the pages read | Included |
| Email mailboxes | Paid add-on. Not needed, because chapters use Google Workspace | Free for the first year. Not needed |
| Server access for a technical person | Full: secure shell access, PHP settings, scheduled tasks | Limited, through Hostinger's control panel |

## Cost per chapter

Prices read from the hosts' own pricing pages on 11-09-26. Both pages carried Black Friday offers, so the introductory price may change.

- **Cloudways Micro:** $14 a month, billed monthly, no contract. Four years: $672, plus backup storage, about $16 for a small site. **About $690.** After that, $168 a year plus storage.
- **Hostinger Unlimited:** $133.92 paid at the start for 48 months. It renews at $16.99 a month, which is $203.88 a year. **Four years: about $134.** After that, about $204 a year.
- **Hostinger Premium (the maintainer's figure):** $95.52 for 48 months, renewing at $10.99 a month. Weekly backups only, so it does not meet WT-90.

Over eight years: Cloudways about $1,380, Hostinger Unlimited about $950.

For comparison, the server a chapter runs itself, which ruling 29 rejected, is about $6 a month on DigitalOcean. Ruling 29's figure of "$50 to $100 a year more" for Cloudways holds up.

## What differs besides price

- **Who can look after it.** Hostinger's control panel is aimed at site owners. Cloudways shows server choices at sign-up and suits someone comfortable with servers. Cleveland's maintainer has said he will support Hostinger and not Cloudways. This is the strongest practical point for Hostinger.
- **Prepayment.** Hostinger's price depends on paying four years at the start, which sits awkwardly with a chapter's yearly budget and with a host change later. Cloudways bills monthly and can be cancelled at any time.
- **Price after year four.** Hostinger's renewal price is higher than Cloudways' monthly price. A chapter that stays is then paying more each year.
- **Room to grow.** Cloudways can be resized in minutes. Hostinger's plan limits are fixed: 2 processor cores, 3 gigabytes of memory, 50 gigabytes of disk. That is ample for a chapter website.
- **One standard either way.** The real benefit of a single host is one runbook and one tested platform for the chapter connector. That holds for whichever host the Association names. The test website on Cloudways (ruling 70) has not been fully set up yet, so a change now costs a runbook rewrite and little else.

## The options for the ruling

1. **Keep Cloudways.** No work to change anything. Costs about $550 more per chapter over four years, and a host Cleveland's maintainer will not support.
2. **Change the standard to Hostinger Unlimited.** Cheaper for four years, and supported by Cleveland's maintainer. Costs four years paid at the start, a higher price after year four, less server access, and a rewrite of the test website runbook and the website template's implementation notes.
3. **Name no single host. State only the requirements WT-90 to WT-92, and give Cloudways and Hostinger Unlimited as tested examples.** Fits ruling 1 (chapters control their own technology). Costs two platforms to test the chapter connector on, and two sets of setup steps.

## What was not confirmed

- Whether Cloudways' smallest plan includes staging, and its default backup schedule. Check in the Cloudways account during the test website's setup.
- Hostinger's prices for 12-month and 24-month terms. They were not shown on the pages read.
- Whether either host offers a nonprofit discount. Neither pricing page mentions one.

## Sources

- Cloudways pricing: https://www.cloudways.com/en/pricing.php
- Cloudways on DigitalOcean: https://www.cloudways.com/en/digital-ocean-cloud-hosting.php
- Hostinger WordPress hosting: https://www.hostinger.com/wordpress-hosting
- Hostinger pricing: https://www.hostinger.com/pricing
- Hostinger plan limits: https://www.hostinger.com/support/6976044-parameters-and-limits-for-hosting-plans

---

## Change log

| Version | Date | Change |
|---|---|---|
| 1.1 | 11-09-26 14:10 | Ruling 75 recorded: option 3. |
| 1.0 | 11-09-26 13:50 | First version, written by Claude after Doug reopened ruling 29. |
