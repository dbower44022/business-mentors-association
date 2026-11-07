# Chapter website template — implementation notes

**Document:** The products chosen for the chapter website template, and what is still to be checked
**Version:** 0.5
**Status:** Draft for Doug's review
**Owner:** Doug Bower
**Last Updated:** 11-07-26 01:46

---

## What this document is for

The requirements in [`website-template-prd.md`](website-template-prd.md) name no products. This document names them, ruling by ruling, so the requirements document stays true if a product changes.

## The products

- **Content management system: WordPress** (ruling 28). The template uses WordPress's built-in block editor and a block theme. It uses no paid page builder, so Elementor, which Cleveland's site uses, is not used.
- **Hosting: Cloudways, on a DigitalOcean server in the chapter's own Cloudways account** (ruling 29). Cloudways keeps the server and PHP, the programming language WordPress runs on, up to date. It also takes backups, installs the security certificate, and provides a staging copy of the website. WordPress core and plugin updates run automatically. The site never runs on the server that holds the chapter's EspoCRM system.
- **Domain name records: Cloudflare, in the chapter's own account**, as the chapter network already rules. The website's address and the chapter applications address are both kept there.
- **Donations: a Stripe Payment Link in the chapter's own Stripe account** (ruling 30). The Donate button runs a short script that opens the Payment Link in a popup window, as Cleveland's Support Us page does today. The Payment Link address is set in the script. The template adds what Cleveland's script lacks: if the browser blocks the popup, the page opens in the same tab.
- **Newsletter: a chapter applications form** (ruling 45). The subscriber lands in EspoCRM first, and the applications' existing Constant Contact synchronisation, described in `cbm-client-intake/MAILING-SETUP.md`, passes them on. Whether the applications already have a newsletter signup form is not checked.
- **The chapter connector: a WordPress plugin** (rulings 34 to 36), published in the WordPress.org plugin directory under the GNU General Public License, version 2 or later. It applies colours and fonts by replacing the theme's `theme.json` values as each page is served; WordPress provides a filter for this, `wp_theme_json_data_theme`, which needs checking against the chosen theme. It registers the key pages as routes it serves itself. It keeps fetched settings and content in WordPress's own short-term store, called transients. Adding and removing menu entries in a block theme's navigation block is not checked; it is the riskiest piece.
- **System Settings: a new Website group** beside the existing Presentation group at `/setup` in the chapter applications (`cbm-client-intake/SYSTEM-SETTINGS-SETUP.md`). The Presentation group already holds the organisation's name, the policy document addresses and a stylesheet that redefines the `--cbm-*` colour values.
- **Framed embeds, for the forms and for chapters not on WordPress: served by the chapter applications** at the chapter applications address, following the embed design in `cbm-client-intake/prds/public-mentor-pages-plan.md`. That design covers the frame, a sizing script that talks to the page holding the frame, and shareable links inside the frame (ruling 27). On WordPress sites, the mentor directory, events, recordings, partners and stories are placed into the page itself instead (ruling 35).

- **Webinars: each chapter's own Zoom account**, through the Zoom connection the chapter applications already have (`cbm-client-intake/event-administration.md`). For shared events (rulings 41 and 42), the hosting chapter's applications add each guest as a Zoom registrant, and read attendance from Zoom's report of who joined. That automatic attendance is built but switched off, and has never run against the real Zoom account.
- **Campaigns: the chapter applications' existing campaign records and links** (marketing rulings 26, 27 and 31 in `cbm-client-intake/prds/prospect-marketing/rulings.md`). Ruling 37 extends campaign links to point at any website page. The website remembers the campaign in the browser's per-tab storage, which is cleared when the tab closes, rather than in a cookie.
- **Visitor statistics: Cloudflare Web Analytics**, free in the chapter's own Cloudflare account, which sets no cookies.
- **Site search: WordPress's own search**, with the chapter connector adding mentor profiles and events to its results.
- **Translation-ready text: WordPress's standard translation functions** in the theme and the chapter connector, and the same discipline in the chapter applications' public pages and forms (ruling 43).

## What the two example websites run on

Both checked on 11-06-26.

- **Cleveland** (clevelandbusinessmentors.org) runs on WordPress with the Elementor, Elementor Pro, Header Footer Elementor and Google Site Kit plugins. Its Donate button opens a Stripe Payment Link. Its newsletter signup is believed to be Constant Contact's, judged from the form's wording; this has not been confirmed.
- **Boston** (bbmentors.org) runs on Squarespace. Its client, mentor and contact forms are HubSpot hosted forms. Its newsletter is a Constant Contact signup page. Donations go through a PayPal donate button, Venmo, and checks by mail. Its mentor portal is a Google Site.

## Prices to check before anyone relies on them

Every figure below is from memory. None has been checked.

- **Cloudways** on a small DigitalOcean server: about $14 a month.
- **A server the chapter runs itself**, for comparison: about $6 to $12 a month, plus about $2 for backups.
- **Stripe's card fee:** about 2.9 percent plus 30 cents per gift. Stripe offers a lower rate to nonprofits that apply.
- **Squarespace plans that allow scripts**, relevant only to a chapter that keeps Squarespace: about $23 to $39 a month.

## What the chapter applications already have

Read from `cbm-client-intake` on 11-07-26, without changing anything.

- **Recorded webinars and upcoming events: built.** The applications serve them publicly at `/api/events/recordings` and the events listing in `events/public.py`. The recordings library has search and a subject filter, and lists only subjects that have recordings. Cleveland's website shows both through a browser script, `wp-plugin/cbm-events/assets/cbm-events.js`. That script builds the content inside the page, not in a frame, using class names copied from Cleveland's Elementor page. Ruling 35 asks for content placed into the page as it is served, by the chapter connector, and for prefixed style names. The existing script is the starting point, not the finished piece.
- **Event topics: built.** The recordings library's subject filter uses them (ruling 55).
- **Newsletter signup form: not built.** The public forms are client intake, volunteer, information request, partner, sponsor, event registration, the prospect response form and the information mailbox. The client intake and event registration forms set the marketing opt-in on the contact, and the mailing synchronisation sends opted-in contacts to Constant Contact. A newsletter form would create a contact with that opt-in set (ruling 45).
- **Frames: not built.** The applications set no rule saying which websites may show them in a frame, and have no sizing script. Browsers allow framing by default when no rule is set, but whether the hosting platform adds one has not been checked. The public mentor pages plan, which carries the frame design, is marked "not built".
- **Permission for other websites to fetch data: built.** The applications already have a setting listing the websites allowed to fetch from them (`allowed_origins` in `core/app.py`). The mentor search of ruling 35 can use it.

## Things to check before the build

1. Whether the hosting platform adds a rule that stops the chapter applications being shown in a frame.
2. Whether Squarespace runs the sizing script on Boston's current plan.
3. Whether a Stripe Payment Link offers monthly giving.
4. Which WordPress block theme the template starts from. It must keep its colours and fonts in `theme.json`.
5. Whether a block theme's navigation block lets a plugin add and remove menu entries cleanly.
6. How long the chapter connector should keep a fetched copy.
7. Which plugins are needed at all. The aim is as few as possible, with the reason for each written here.

---

## Change log

| Version | Date | Change |
|---|---|---|
| 0.5 | 11-07-26 01:46 | Added what the chapter applications already have, read from the code: recordings, events and topics built; newsletter form and frame support not built; cross-site fetch setting built. |
| 0.4 | 11-07-26 01:40 | The newsletter signup is a chapter applications form, not Constant Contact's own (ruling 45). Drafted marks removed after Doug's confirmation. |
| 0.3 | 11-07-26 01:31 | Added webinars, campaigns, visitor statistics, site search and translation-ready text (rulings 37 to 43). |
| 0.2 | 11-07-26 00:51 | Added the chapter connector plugin and the System Settings Website group (rulings 34 to 36); framed embeds now serve forms and chapters not on WordPress. Two checks added. |
| 0.1 | 11-07-26 00:42 | First draft, from rulings 26 to 33 and the survey of Cleveland's and Boston's websites. |
