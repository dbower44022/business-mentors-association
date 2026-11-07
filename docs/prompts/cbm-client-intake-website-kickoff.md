# Kickoff prompt — the chapter applications' side of the chapter website

**Document:** Prompt to start a Claude Code session in `cbm-client-intake` on the applications' side of the chapter website
**Version:** 1.0
**Status:** Ready to use
**Owner:** Doug Bower
**Last Updated:** 11-07-26 10:33

---

Paste everything below the line into a new Claude Code session started in `~/Dropbox/Projects/cbm-client-intake`.

---

Operating mode: DETAIL (this repository's default).

## What this session is for

The Business Mentors Association has decided how a chapter's public website connects to the chapter applications in this repository. A prototype of the website side works, built against a stand-in that imitates these applications. This session turns the stand-in's behaviour into tracked requirements here, and then, once Doug approves them, builds the real thing.

**This repository's process comes first.** Read `CLAUDE.md` and `OPEN-ITEMS.md` before anything else. A change here starts as a tracked requirement, on a branch, approved by Doug at the stopping points your plan names. Your first deliverable is the requirement and a plan with named stopping points — not code. Do not write application code until Doug approves the plan.

## Read these, in this order

1. `~/Dropbox/Projects/business-mentors-association/DECISIONS.md`, rulings 24 to 63. These are Doug's rulings. Rulings 32, 33, 35, 42, 43 and 45 bind this work most directly.
2. `~/Dropbox/Projects/business-mentors-association/docs/website-template-prd.md`, sections 5.2 to 5.5, 5.13 and 7. Requirement numbers such as WT-22 refer to it.
3. `~/Dropbox/Projects/chapter-website-prototype/README.md`, for what the prototype proved and found.
4. `~/Dropbox/Projects/chapter-website-prototype/mock-apps/server.py` and `mock-apps/settings.json`. **This is the contract.** The website's chapter connector already calls these addresses and expects these shapes.

## The contract the stand-in imitates

All addresses are on the chapter applications address. All are public and need no sign-in.

- `GET /api/website/settings` — the Website group of System Settings (ruling 32, ruling 45): `colors` (the slugs `base`, `contrast`, `accent-1` to `accent-6`), `fonts` (`heading`, `body`), the logo, `chapter` (name, abbreviation, email, phone, address, employer identification number, payment link) and `pages` (an on/off switch per key page: `mentors`, `events`, `recordings`, `partners`, `stories`). System Settings must refuse to switch on a page the applications cannot serve (WT-10).
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

- **Framing.** Nothing names which websites may show the forms in a frame, and there is no script that sizes a frame to its form. Both are needed (ruling 42).
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
| 1.0 | 11-07-26 10:33 | First version, written after the first prototype. |
