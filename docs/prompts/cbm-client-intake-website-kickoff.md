# Kickoff prompt — the chapter applications' side of the chapter website

**Document:** Prompt to start a Claude Code session in `cbm-client-intake` on the applications' side of the chapter website
**Version:** 1.2
**Status:** Ready to use
**Owner:** Doug Bower
**Last Updated:** 11-07-26 11:08

---

Paste everything below the line into a new Claude Code session started in `~/Dropbox/Projects/cbm-client-intake`.

---

Operating mode: DETAIL (this repository's default).

## What this session is for

The Business Mentors Association has decided how a chapter's public website connects to the chapter applications in this repository. A prototype of the website side works, built against a stand-in that imitates these applications. This session turns the stand-in's behaviour into tracked requirements here, and then, once Doug approves them, builds the real thing.

**This repository's process comes first.** Read `CLAUDE.md`, `OPEN-ITEMS.md` and `DEPLOYMENT.md` before anything else. There is no branch-level review gate here: every push to `main` builds dev, crm-test and Cleveland's production, and pushing the `release` branch deploys every chapter. The gate is the feature flag. Build each piece dark (default off), switch it on in crm-test's overlay, review it live, and only then consider production — `DEPLOYMENT.md` § *Reviewing a change before it reaches production*. Your first deliverable is a written plan with named stopping points, not code. Do not write application code until Doug approves the plan.

**The goal of this round** is to deploy a test chapter website, built from the template, that is connected to crm-test, so the integration can be tested end to end. Production is not part of this round.

**Runbooks are part of the work.** Every setup and configuration step a chapter's technical person would take — switching the features on, filling in the Website group of System Settings, allowing the website's address to frame the forms and fetch data — is written as a runbook others can follow, to Doug's step-by-step instructions standard (in `~/.claude/CLAUDE.md`).

## Read these, in this order

1. `~/Dropbox/Projects/business-mentors-association/DECISIONS.md`, rulings 24 to 63. These are Doug's rulings. Rulings 32, 33, 35, 42, 43 and 45 bind this work most directly.
2. `~/Dropbox/Projects/business-mentors-association/docs/website-template-prd.md`, sections 5.2 to 5.5, 5.13 and 7. Requirement numbers such as WT-22 refer to it.
3. `~/Dropbox/Projects/chapter-website-prototype/README.md`, for what the prototype proved and found.
4. `~/Dropbox/Projects/chapter-website-prototype/mock-apps/server.py` and `mock-apps/settings.json`. **This is the contract.** The website's chapter connector already calls these addresses and expects these shapes.

## The contract the stand-in imitates

All addresses are on the chapter applications address. All are public and need no sign-in.

- `GET /api/website/settings` — the Website group of System Settings (ruling 32, ruling 45): `colors` (the slugs `base`, `contrast`, `accent-1` to `accent-6`), `fonts` (`heading`, `body`), the logo, `chapter` (name, abbreviation, email, phone, address, employer identification number, payment link) and `headerImage`, and `pages` (an on/off switch per key page: `mentors`, `events`, `recordings`, `partners`, `sponsors`, `stories`). System Settings must refuse to switch on a page the applications cannot serve (WT-10).
- `GET /api/website/pages/{key}` and `GET /api/website/pages/mentors/{slug}` — finished page content as `{title, description, html}`; `404` for an unknown mentor. Every class name in the HTML starts with `cmw-`, checked by an automated test (ruling 33, WT-44).
- `GET /api/website/sitemap` — `{paths: [...]}`, every mentor profile's path.
- `GET /api/website/mentors.json?q=` — `{slugs: [...]}` matching the search; the chapter website's address must be allowed to fetch it (WT-46).
- `GET /assets/website.css` and `GET /assets/search.js` — the styles and the search script for that content. The styles use the website's colour variables, such as `var(--wp--preset--color--accent-1)`.
- Campaign links may point at a website page: following one sends the visitor to that page with `?cmp=CAMPAIGN` (ruling 35). The stand-in imitates this at `/c/{link}`.
- The framed forms receive `campaign` and `placement` in their address. They must write both to the records they create, alongside the existing campaign tagging (marketing rulings 26 and 27).

## What already exists here, to build on rather than duplicate

These were read on 11-07-26; check each one before relying on it.

- `events/public.py` — the public upcoming events and recordings, with search and a subject filter.
- The `allowed_origins` setting in `core/app.py` — which other websites may fetch from the applications.
- The Presentation group in System Settings (`SYSTEM-SETTINGS-SETUP.md`). The new Website group sits beside it. The two must not hold the same value twice.
- The campaign records and campaign links (`prds/prospect-marketing/rulings.md`, rulings 26, 27 and 31).
- `prds/public-mentor-pages-plan.md` and the `mentorprofile/` page template — the earlier plan for public mentor pages, marked not built.
- `wp-plugin/cbm-events/` — Cleveland's browser script for events. It uses Cleveland's own class names, so it is not the finished piece.

## Also owed by the rulings, outside the stand-in

- **Framing.** Nothing names which websites may show the forms in a frame, and there is no script that sizes a frame to its form. Both are needed (ruling 42). The prototype shows exactly what works: `mock-apps/frame-size.js`, served inside each form, and the embed styles built by `embed_css()` in `mock-apps/server.py`, which map the form's `--cbm-*` colour and font tokens to the Website settings and hide the form's own heading, footer and background (WT-56, WT-56b). The forms already read `campaign` from their address; they do not yet read `placement`.
- **A newsletter signup form.** None exists. It creates a contact with marketing consent set (ruling 43).

## Out of scope for this session

- Shared events between chapters (rulings 39 and 40). That needs automatic attendance from Zoom proven first, and a clause in the chapter agreement.
- The seven feature requests listed in section 7 of the requirements document. Those go to the committee under ruling 3.

## Questions to put to Doug, not to decide alone

- How the logo is stored and served.
- Where `campaign` and `placement` are written on the records a form creates.
- Whether mentor page content is built from the existing `mentorprofile/` template or written fresh.
- The order of the work, and where your plan's stopping points fall.

---

## Change log

| Version | Date | Change |
|---|---|---|
| 1.2 | 11-07-26 11:08 | Corrected the process paragraph: this repository has no branch gate; every push to main deploys crm-test and production, and feature flags are the gate. Added the round's goal (a test chapter website connected to crm-test) and the runbook requirement. |
| 1.1 | 11-07-26 11:01 | Added the sponsors page key, the header graphic, the proven frame sizing script and embed styles, and the placement gap. |
| 1.0 | 11-07-26 10:33 | First version, written after the first prototype. |
