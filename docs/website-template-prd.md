# Chapter website template — product requirements

**Document:** Requirements for the template website the Association builds and each chapter copies
**Version:** 0.5
**Status:** Draft for Doug's review
**Owner:** Doug Bower
**Last Updated:** 11-07-26 01:46

---

## 1. What this document is for

The Association will build one website that each member chapter copies and makes its own. It will also build an add-on that ties that website to the chapter applications. This document says what both must do, and what the chapter applications must add so the website can do it. It follows rulings 24 to 62 in [`DECISIONS.md`](../DECISIONS.md), made on 11-06-26 and 11-07-26.

This document names no products. The products the rulings chose, and the prices still to be checked, are in [`website-template-implementation-notes.md`](website-template-implementation-notes.md).

Every requirement rests on a ruling. Rulings 42 to 62 are items Claude drafted during the discussion, which Doug confirmed on 11-07-26.

## 2. Terms used in this document

- **Chapter.** An independent business mentoring nonprofit that is a member of the Association.
- **Chapter applications.** The shared set of applications the Association builds and each chapter runs on its own server: the public intake forms, and the staff and mentor tools.
- **Customer relationship management system.** The database in which a chapter keeps its clients, mentors, partners, sponsors, events and contributions. The chapter applications read from it and write to it.
- **System Settings.** The administrator's settings page in the chapter applications. A change there takes effect without reinstalling the applications.
- **Template website.** The website the Association builds once and each chapter copies.
- **Content management system.** Software that lets volunteers change a website's words, pictures and pages through a web browser, without writing code. The template website is built on one particular content management system (ruling 26).
- **Chapter connector.** An add-on to that content management system, which the Association builds and maintains. It applies the settings from System Settings to the website, and places information from the customer relationship management system into the website's pages. "Chapter connector" is a working name.
- **Key pages.** The pages the chapter connector creates and owns: Find a Mentor and each mentor's profile, Workshops and Events, Recorded Webinars, Partners and Sponsors, and Client Stories.
- **Framed embed.** A section of a page whose content comes from the chapter applications and appears inside a frame on that page. The section is placed by pasting **embed code**, a short block of text, into the page.
- **Chapter applications address.** The web address, under the chapter's own domain, at which the chapter's applications run. Cleveland's is apps.clevelandbusinessmentors.org.
- **Hosted payment page.** A payment page run by a payment service inside the chapter's own account with that service. Card details are entered there and never pass through the chapter's website or applications.
- **Mailing service.** The email newsletter service with which the chapter applications exchange contacts.
- **Editor.** A chapter volunteer who changes the website's words and pictures. An editor is not expected to have technical skills.
- **Chapter technical person.** The chapter's own technical volunteer or staff member.
- **Administrator.** The person who uses System Settings, usually the chapter technical person.
- **Campaign.** A piece of outreach a chapter's marketing users create in the chapter applications, such as a postcard mailing or a social media post. Each campaign owns one or more links, and every record created through a campaign link is tagged with that campaign.
- **Placement tag.** A fixed label on a website button saying where on the website the button sits, such as "home page" or "mentor profile".
- **Shared event.** An event a chapter has marked "Shared with Association Members", so other chapters can add it to their own calendars.
- **Hosting chapter** and **adding chapter.** The chapter that runs a shared event, and a chapter that has added it to its own calendar.
- **Guest.** A person registered for a shared event through an adding chapter.
- **Webinar service.** The online meeting service on which a chapter runs its webinars, in the chapter's own account.
- **Member list.** The list, kept by the Association, of every member chapter's applications address. Chapters' applications accept requests from each other only when the requester is on it.
- **Chapter directory.** The list of member chapters, each with the area it serves, on the Association's own website.

## 3. Who the website serves

- **A business owner looking for help.** Learns that mentoring is free and personal, finds a mentor, and asks for one.
- **A prospective mentor.** Learns what mentoring involves and applies.
- **A donor.** Gives money and learns how it is used.
- **A partner or sponsor.** Learns how to work with the chapter and sees others who do.
- **A workshop attendee.** Finds an event, registers, and finds past recordings.
- **An editor.** Keeps the website current without help.
- **The administrator.** Sets the website's look, its key pages and the chapter's details in one place.
- **The chapter technical person.** Sets up the website and keeps it running, with the Association as backup.

## 4. The model

**Two paths serve two kinds of chapter website.**

**The full path is for a chapter on the template's content management system** (rulings 24, 32 and 33).
- The chapter copies the template website and owns its words, its ordinary pages and its layout.
- The administrator sets the website's colours, fonts and logo, the chapter's details, and which key pages are switched on, in one place: a Website group in System Settings.
- The chapter connector applies those settings across the whole website.
- The chapter connector creates and owns the key pages. Their content comes from the customer relationship management system and is placed into the page itself, not inside a frame, so each mentor profile is a page on the chapter's own domain.
- Forms stay in frames for now.

**The basic path is for a chapter whose website runs on another platform** (rulings 25 and 32).
- Boston, on a hosted site builder, is an example.
- The chapter pastes embed code for each part it wants.
- The framed embeds take their colours from the same System Settings.
- There are no page switches, and the website's own look is set in that platform.

The Association builds the template website itself, using Cleveland's and Boston's websites as models of structure and function (ruling 29). Their words, photographs and branding are not copied.

## 5. Requirements

### 5.1 Copying the template website

- **WT-01.** A chapter technical person can install a complete copy of the template website, with every page, setting and sample content, on the chapter's own hosting account, from one package the Association publishes.
- **WT-02.** After installation, the copy belongs to the chapter. Nothing in it depends on any account the Association holds. The chapter connector comes from the content management system's public add-on directory, and its content and settings come from the chapter's own applications.
- **WT-03.** The package comes with a setup guide. The guide is written to the Association's standard for step-by-step instructions, and takes a chapter technical person from an empty hosting account to a published website connected to the chapter applications.
- **WT-04.** The template website uses the content management system's own built-in page editor. It uses no paid add-on for page layout.
- **WT-05.** The template website's theme keeps its colours and fonts in the content management system's central style settings, so the chapter connector can apply them (ruling 32).

### 5.2 The Website group in System Settings

- **WT-10.** System Settings gains a Website group. In it, the administrator sets (ruling 32):
  - the website's colours,
  - its fonts,
  - its logo, and
  - an on/off switch for each key page.
- **WT-11.** The Website group also holds each chapter-wide value, set once and used everywhere it appears.
  - the chapter's name and abbreviation,
  - its contact email, telephone and mailing address,
  - its employer identification number,
  - its social media addresses, and
  - its hosted payment page address.

  On Cleveland's site, three different email domains appear on different pages; one setting prevents that. The existing Presentation group already holds the organisation's name and the policy document addresses; the two groups must not hold the same value twice.
- **WT-12.** A change in the Website group reaches the website within a few minutes, without anyone editing the website.
- **WT-13.** The Website group shows the embed code for each framed embed, ready to copy, for chapters on the basic path.

### 5.3 The chapter connector

- **WT-20.** The chapter connector is set up by entering one value: the chapter applications address.
- **WT-21.** The chapter connector applies the colours, fonts and logo from System Settings to every page of the website, including pages editors build by hand (ruling 32).
- **WT-22.** The chapter connector creates and owns the key pages. A key page switched off in System Settings is not shown, and its menu entry disappears. A key page switched on appears with its menu entry (ruling 32).
- **WT-23.** Key pages do not appear among the pages editors manage. In the content management system, the chapter connector shows a screen saying the key pages are managed in System Settings, with a link to it.
- **WT-24.** The chapter connector supplies the chapter-wide values of WT-11 to the website's footer and Donate button.
- **WT-25.** The chapter connector needs no password. Everything it fetches is public (ruling 32).
- **WT-26.** The chapter connector keeps the last settings and content it fetched. If the chapter applications cannot be reached, the website stays up and shows those (ruling 32).
- **WT-27.** The chapter connector works with older releases of the chapter applications, since chapters may run different releases with no deadline (rulings 2 and 17). Where a feature needs a newer release, the chapter connector says so plainly in its screen in the content management system, rather than failing (ruling 32).
- **WT-28.** The chapter connector is open source under the GNU General Public License, version 2 or later, or a compatible licence (rulings 6 and 34).
- **WT-29.** Each new version of the chapter connector is published in the content management system's public add-on directory, only after the release vote passes (rulings 4 and 34).
- **WT-30.** Each chapter chooses on its own website whether chapter connector updates install automatically or wait for its technical person (rulings 2 and 34).

### 5.4 Information from the customer relationship management system

- **WT-40.** When the customer relationship management system holds what a website list shows, the website shows it from the customer relationship management system, not from a copy kept in the content management system (ruling 30).
- **WT-41.** On the full path, these appear as part of the page itself, not inside a frame (ruling 33):
  - the mentor directory, with search, and each mentor's profile,
  - the upcoming events list,
  - recorded webinars, with search,
  - partners and sponsors, and
  - client success stories.
- **WT-42.** Each mentor profile is a page on the chapter's own domain, with its own title and summary for search engines (ruling 33).
- **WT-43.** The chapter applications produce this content as finished page content. The same content serves the framed embeds of the basic path, so it is produced once (ruling 33).
- **WT-44.** Every style name in content from the chapter applications carries a unique prefix, so the website's styles and the applications' styles cannot collide. An automated test in the chapter applications checks this on every release (ruling 33).
- **WT-45.** A change in the customer relationship management system appears on the website within a few minutes (ruling 33).
- **WT-46.** The mentor search runs inside the website page. The chapter applications permit the website's address to fetch search results (ruling 33).
- **WT-47.** Partners and sponsors carry a logo and a "show on website" switch on their records. A partner or sponsor appears only while the switch is on (ruling 30).
- **WT-48.** A client success story is information on the client record: the story text, a short quotation, a photograph and a "show on website" switch (ruling 30).
- **WT-49.** A success story appears only when the client record holds the client's consent to publication and the date that consent was given. Mentoring is confidential, so a story with no recorded consent never appears.
- **WT-50.** Until the features in section 7 are built, the Partners and Sponsors and Client Stories pages are ordinary pages edited by hand. They become key pages when the features are built.
- **WT-51.** The leadership team is an ordinary page edited in the content management system (ruling 30).
- **WT-52.** Mentor records and client stories carry a "feature on home page" switch. The home page shows the switched-on ones, rotating daily.
- **WT-53.** Recorded webinars can be filtered by subject, using the event topics the customer relationship management system holds.
- **WT-54.** The chapter applications publish the chapter's public events as a calendar feed. A visitor can subscribe to it from Workshops and Events.

### 5.5 Forms

- **WT-55.** These forms appear in frames on both paths, for now (ruling 33):
  - the client intake form, including starting a request for one particular mentor,
  - the mentor application form,
  - the information request form, which is the website's contact form,
  - the partner form,
  - the sponsor form,
  - the newsletter signup form, and
  - event registration.
- **WT-56.** Each framed form sizes itself to its content, so the page shows no inner scroll bar.
- **WT-57.** Each framed form is served from the chapter applications address, never a hosting provider's default address. Cleveland's site links once to such a default address today.
- **WT-58.** Each framed form carries a link that opens the same form full-screen, in case the frame fails to load.
- **WT-59.** Every "Request a Mentor" button on the website leads to the same client intake form. Cleveland's site has three destinations for that action.
- **WT-60.** The newsletter signup is a chapter applications form, not the mailing service's own form. A subscriber lands in the customer relationship management system first, and the applications' existing exchange of contacts with the mailing service passes them on (ruling 43).
- **WT-61.** The embed code stays compatible across releases of the chapter applications. A change that would make a chapter re-paste embed code is announced in the release notes, with the replacement code (ruling 24).
- **WT-62.** A guide offered in exchange for an email address uses the mailing service's own landing page, so the subscriber reaches the customer relationship management system through the applications' existing exchange of contacts with the mailing service. The Resources page has a place to feature one.
- **WT-63.** Review highlights are entered by hand: up to three short excerpts, each with the reviewer's first name or initials, and a link to the chapter's public review page.

### 5.6 Donations

- **WT-65.** The Donate button opens a hosted payment page in the chapter's own payment service account, as Cleveland's website does today (ruling 28).
- **WT-66.** If the visitor's browser blocks the payment page from opening in a new window, the payment page opens in the same tab instead.
- **WT-67.** The Support Us page states the chapter's 501(c)(3) status, its employer identification number, that gifts are tax-deductible, and how gifts are used. The wording is the chapter's.
- **WT-68.** Until the feature in section 7 is built, staff enter each gift in the customer relationship management system by hand, and the chapter sends each donor's tax acknowledgment itself (ruling 28).

### 5.7 Pages

- **WT-70. Published at launch.** Key pages are marked "key".
  - Home: the "How can we help you?" chooser, featured mentors and client stories, the chapter's figures, and review highlights.
  - About: mission, history, how mentors are chosen, and the leadership team.
  - How It Works: the steps from request to mentoring, and what a client can expect.
  - Find a Mentor (key), with each mentor's profile (key).
  - Request a Mentor.
  - Become a Mentor.
  - Workshops and Events (key), with Recorded Webinars (key).
  - Support Us: the Donate button, sponsorship and partnership.
  - Contact.
  - Frequently Asked Questions: cost, process and eligibility.
  - Privacy Policy.
  - Terms of Use.
- **WT-71. Shipped switched off, for the chapter to switch on:**
  - Partners and Sponsors (key, once built).
  - Client Stories (key, once built).
  - Blog.
  - Resources and Templates: downloadable documents grouped by subject.
  - In the News: press mentions and podcast episodes, each with its date, outlet and link.
  - Client Code of Conduct.
  - Mentor Code of Conduct.
  - A campaign landing page, such as Cleveland's page for new business owners who received a postcard.
- **WT-72. On every page:**
  - the newsletter signup,
  - a "Request a Mentor" button,
  - a member sign-in link to the chapter applications,
  - social media links,
  - a site search box,
  - a link to the chapter directory for visitors outside the chapter's area (ruling 38), and
  - a footer stating the chapter's 501(c)(3) status, its employer identification number and its contact details.
- **WT-73.** Every ordinary page ships with sample words that explain what belongs there and give an example. A pre-launch checklist in the setup guide lists every sample to replace. The sample words are written for the template, not taken from Cleveland or Boston. Boston's site still shows the placeholder text "Add the description here"; this requirement exists to catch that kind of leftover.
- **WT-74.** The Privacy Policy, Terms of Use and both codes of conduct ship as drafts. Each is marked for review by the chapter's own attorney before it is published. The Privacy Policy is published at launch because the website collects personal details. Boston's site has no privacy policy.

### 5.8 Editing

- **WT-80.** An editor can do each of the following without code and without the chapter technical person:
  - Change words and pictures on any ordinary page.
  - Publish a blog post.
  - Add a downloadable document to Resources.
  - Publish or unpublish an ordinary page.
  - Change the menu's ordinary entries.
  - Add or remove a partner logo while partners are still edited by hand.
- **WT-81.** Mentor profiles, events, webinar recordings, partners, sponsors and client stories are edited in the chapter applications, never in the content management system (ruling 30).
- **WT-82.** The setup guide includes a short guide for editors. It explains which things are changed in the content management system and which in System Settings.

### 5.9 Hosting and upkeep

- **WT-90.** The website runs on a hosting service in the chapter's own account (ruling 27). The hosting service:
  - keeps the server's operating system and programming language up to date,
  - takes daily backups,
  - provides the security certificate that serves the site over an encrypted connection, and
  - provides a staging copy of the website where changes can be tried before they go live.
- **WT-91.** The content management system and its other add-ons update themselves automatically. Updates of the chapter connector follow WT-30.
- **WT-92.** The website never shares a server with the customer relationship management system (ruling 27). Someone who broke into the website could otherwise reach client records.
- **WT-93.** The template website uses as few add-ons as possible. Each add-on is named in the implementation notes with the reason for it.
- **WT-94.** The website's domain name records are kept in the chapter's own domain name account, as the chapter network already rules for every chapter.
- **WT-95.** The shared test system has its own copy of the template website running the chapter connector. Chapters' technical people certify each chapter connector release there before the vote.

### 5.10 Accessibility, search, speed and privacy

- **WT-100.** The template website meets the Web Content Accessibility Guidelines (WCAG) version 2.2 at level AA, on every page, in every key page and in every framed form. Every image has a text description.
- **WT-101.** Every page has its own title and summary for search engines. The website publishes a site map for search engines that includes every key page and every mentor profile. Each page's web address is short and readable.
- **WT-102.** Pages load quickly on a mobile telephone. The layout works at every screen width from telephone to desktop.
- **WT-103.** Visitor statistics are gathered by a service that sets no cookies, so no consent banner is needed, and only as the Privacy Policy describes.
- **WT-105.** Site search finds ordinary pages, mentor profiles and events.
- **WT-106.** All text a visitor reads, on the website and in the chapter applications' public pages and forms, is kept in a form that can be translated. English is the only language at launch (ruling 41).
- **WT-104.** The website collects no personal details itself. Every form that collects personal details is a framed form from the chapter applications, apart from the guide offered for an email address (WT-62), so personal details are stored in the customer relationship management system or the mailing service, never in the content management system.

### 5.11 Support

- **WT-110.** The chapter technical person is the first source of help for the website. The Association helps with the whole website when that person is unavailable or asks for help (ruling 31).
- **WT-111.** Website support requests use the same request system as the chapter applications.
- **WT-112.** The Association fixes defects in the chapter connector, the key pages and the framed forms through the normal release process (rulings 2, 4 and 34).

### 5.12 Ownership and openness

- **WT-120.** The template website is published openly, as the chapter applications will be (ruling 6). Its licence is not yet chosen; see section 8.
- **WT-121.** A chapter can export its whole website, with its words, pictures and design, and move it to another host without the Association.

### 5.13 Campaigns through the website (ruling 35)

- **WT-130.** A campaign link in the chapter applications may point at any website page, not only a form.
- **WT-131.** A visitor who arrives through a campaign link keeps that campaign until they close the browser tab. Every "Request a Mentor" button and every form on that visit carries it, so the records created are tagged with the campaign exactly as a direct campaign link tags them today.
- **WT-132.** Every website button that leads to a form carries a placement tag. The records created show which button brought the person.
- **WT-133.** The campaign is remembered by a small marker in the visitor's browser that holds nothing personal and is gone when the tab closes. The Privacy Policy says so.
- **WT-134.** If a visitor arrives through a second campaign in the same visit, the later campaign replaces the earlier.
- **WT-135.** On the basic path, a campaign carries through only when the visitor goes straight from the landing page to a form.

### 5.14 The chapter's figures (ruling 36)

- **WT-140.** The figures the website states about the chapter are counted daily from the customer relationship management system. Examples: active mentors, clients mentored in the past twelve months, sessions held in the past twelve months, and workshop attendees in the past twelve months.
- **WT-141.** The administrator switches each figure on or off in the Website group of System Settings.
- **WT-142.** Every figure has a written definition that all chapters share. The definitions are agreed before the feature is built.

### 5.15 Client success stories (ruling 37)

- **WT-150.** A "Request a Success Story" action on the client's record sends the client a personal link to a story form. Staff or the mentor choose the action.
- **WT-151.** The form asks for exactly what the website's client story shows.
  - The business name, and how the client wants to be named: full name, first name only, or business name only.
  - The kind of business and its town.
  - A one-line headline.
  - Three text boxes: the challenge before mentoring; what the client and mentor worked on; the results, with optional figures such as funding raised or jobs created.
  - A short quotation, up to about 200 characters, for the home page and story cards.
  - Whether to name the mentor, who is filled in from the engagement.
  - Up to five photographs. The client chooses the main one, and confirms that they own the photographs and that everyone pictured agrees.
  - The business's website and social media addresses.
- **WT-152.** The client gives consent separately for the website, the chapter's social media and its newsletter. The client's typed name and the date are recorded. The form says consent can be withdrawn at any time.
- **WT-153.** A submission lands on the client record awaiting review. Staff edit and approve it, then switch it on.
- **WT-154.** If staff change the client's words beyond spelling and length, the edited story goes back to the client through the same link for one-click approval before it is published.
- **WT-155.** A story switched off, or whose consent is withdrawn, leaves the website within minutes.

### 5.16 The chapter directory (ruling 38)

- **WT-160.** The Association's website lists every member chapter, with its name, the area it serves and a link to its website.
- **WT-161.** Every chapter website links to the chapter directory for visitors outside its area. A chapter's stated area is information for visitors, not a boundary.

### 5.17 Shared events (rulings 39 and 40)

- **WT-170.** A chapter can mark any public event "Shared with Association Members".
- **WT-171.** An "Add Association Events" function in event management lets a chapter browse every shared event from the other chapters and add one to its own calendar.
- **WT-172.** An added event is managed exactly like a local event. The adding chapter shows it on its own website, takes its own registrations, and runs its own campaigns and registration links. Each registrant becomes the adding chapter's contact.
- **WT-173.** When someone registers for an added event, the adding chapter's applications ask the hosting chapter's applications to add a guest. The hosting chapter's applications add the guest to the host's webinar and return the guest's own join link, which the adding chapter's confirmation email delivers.
- **WT-174.** After the event, the hosting chapter's applications return attendance and minutes attended for the adding chapter's guests only. The adding chapter records them on its own contacts, as for a local event.
- **WT-175.** Guests are never added to the hosting chapter's customer relationship management system. The hosting chapter sees how many guests each chapter sent, not who they are.
- **WT-176.** The registration form for an added event names the hosting chapter, and says the registrant's name and email are passed to the hosting chapter's webinar service.
- **WT-177.** The hosting chapter sets a limit on guest seats for each shared event.
- **WT-178.** Chapters' applications accept guest and browsing requests only from chapters on the member list.

### 5.18 Languages (ruling 41)

- **WT-180.** Mentor profiles carry a "languages spoken" field, and the mentor directory can be filtered by it.
- **WT-181.** Adding a language later is a translation job, not a rebuild (WT-106).

## 6. Not in scope

- **The customer relationship management system's internal screens.** These belong to the chapter applications.
- **The members-only mentor portal.** The website only links to it.
- **Writing each chapter's words.** The chapter writes its own, guided by the samples in WT-73.
- **Moving Cleveland's or Boston's existing website onto the template.** Each chapter decides that for itself.
- **Page switches and whole-site styling on the basic path.** Those depend on the chapter connector (ruling 32).
- **Hosting any chapter's website centrally.** Doing so would contradict ruling 1.
- **Passing a client's submission from one chapter's customer relationship management system to another's.** Sent to the committee as a governance question (ruling 38).
- **Spanish or any other language at launch** (ruling 41).

## 7. Work owed

**The work the rulings require.** This is built through the chapter applications' own process in `cbm-client-intake`: a tracked requirement first, on a branch.

1. The Website group in System Settings (section 5.2).
2. Finished page content for the key pages, with prefixed style names and the test that guards them (WT-43, WT-44).
3. Permission for the website to fetch mentor search results (WT-46).
4. The chapter connector itself, and its first submission to the public add-on directory (section 5.3).
5. The test website on the shared test system (WT-95).
6. Campaigns through the website: campaign links that point at any page, the remembered campaign, and placement tags (section 5.13).
7. Shared events: the Shared marking, Add Association Events, and the guest and attendance connection between chapters' applications (section 5.17).
8. The newsletter signup form, which the chapter applications do not have today (WT-60).
9. Translatable text throughout the website and the chapter applications' public pages and forms (WT-106).

**Prerequisites, before shared events can work.**

1. Automatic attendance from the webinar service, built but switched off, is switched on and proven (WT-174).
2. The chapter agreement allows a guest's name and email to pass to the hosting chapter's webinar service (WT-176).
3. The Association keeps the member list (WT-178), and has its own website for the chapter directory (WT-160).

**Feature requests owed to the committee under ruling 3.** None has been filed.

1. **Record gifts automatically.** The payment service notifies the chapter applications when a payment completes. The applications then create the donor and the contribution record in the customer relationship management system (ruling 28).
2. **Partners and sponsors on the website.** Add a logo and a "show on website" switch to partner and sponsor records, and make Partners and Sponsors a key page (ruling 30).
3. **Client success stories.** Add story fields and recorded consent to the client record, and make Client Stories a key page (ruling 30, WT-48, WT-49).
4. **The chapter's figures.** Count the figures daily, with shared definitions (ruling 36, section 5.14).
5. **Request a Success Story.** The action, the client's form, the review step and the client's approval of edited wording (ruling 37, section 5.15).
6. **An events calendar feed** (WT-54).
7. **Languages spoken on mentor profiles** (ruling 41, WT-180).

## 8. Open questions

1. **The template website's licence** (ruling 6, and open question 15). The chapter connector's licence is settled by ruling 34. If the template's theme is also published in the public directory, the same licence applies to it.
2. **Menu control.** Whether the chapter connector can add and remove menu entries cleanly in the content management system's newer kind of theme. This has not been checked, and it is the riskiest part of WT-22.
3. **Recorded webinars.** Answered 11-07-26: the chapter applications already serve the public recordings library, with search and a subject filter. See the implementation notes.
4. **The forms in frames.** Answered 11-07-26: nothing for frames is built yet — no sizing script and no rule naming which websites may frame the forms — and the public mentor pages plan is not built. Both are build work. See the implementation notes.
5. **How long the chapter connector keeps a copy.** "A few minutes" is a placeholder.
6. **The automatic-update recommendation.** Whether the setup guide recommends chapter connector updates on or off (WT-30).
7. **Tax acknowledgments.** Whether the customer relationship management system sends donors' tax acknowledgments once gifts are recorded automatically.
8. **Monthly giving.** Whether the hosted payment page offers monthly giving.
9. **Partner logos.** Size and format rules.
10. **Cleveland.** Whether Cleveland's existing website moves to the template and to the hosting arrangement of ruling 27.
11. **Rochester.** Whether Rochester adapts the template instead of issuing its request for proposals, and if so, when it needs the template (ruling 29).
12. **Who builds the template, and by when.** Ruling 29 places the work on Association volunteers.
13. **The chapter connector's name.**
14. **The figures' definitions** (WT-142).
15. **The consent wording** on the story form, for the attorney review already listed as open question 29 in `OPEN-QUESTIONS.md`.
16. **Guest seats.** What happens when an added event's guest seats run out (WT-177).
17. **Recordings of shared events.** How the hosting chapter's recording link reaches the adding chapter's "recording available" email.
18. **Changes to shared events.** What happens to adding chapters when the hosting chapter moves or cancels a shared event.
19. **Who builds the Association's own website** (WT-160). It could be built from the template.

## 9. Problems on the example websites this template prevents

| Problem seen | Website | Requirement that prevents it |
|---|---|---|
| 0.5 | 11-07-26 01:46 | Open questions 3 and 4 answered from a reading of the chapter applications' code; see the implementation notes. WT-53 no longer marked as inferred; the newsletter form is confirmed as new work. |
| Three different email domains on different pages | Cleveland | WT-11 |
| "Request a Mentor" goes to three different places | Cleveland | WT-59 |
| A link to a page that returns "page not found" | Cleveland | WT-22, key pages and their menu entries switch together |
| The intake form at a hosting provider's default address | Cleveland | WT-57 |
| No privacy policy although forms collect personal details | Boston | WT-74 |
| Placeholder text left in published image descriptions | Boston | WT-73, WT-100 |
| Mentor profiles and partner logos kept by hand beside the customer relationship management system | Boston | WT-40, WT-47 |
| A stylesheet copied from the website drifted, unnoticed for three weeks | Cleveland | WT-44 |
| Figures such as "16+ certified mentors" typed by hand and never updated | Cleveland | WT-140 |
| A story nomination form open to anyone, about anyone | Boston | WT-150 |

---

## Change log

| Version | Date | Change |
|---|---|---|
| 0.4 | 11-07-26 01:40 | Every drafted requirement confirmed by Doug as rulings 42 to 62, and the drafted marks removed. The newsletter signup is now a chapter applications form, listed with the framed forms and in the work owed. |
| 0.3 | 11-07-26 01:31 | Added rulings 35 to 41 and the drafted capabilities: campaigns through the website (5.13), the chapter's figures (5.14), client success stories (5.15), the chapter directory (5.16), shared events (5.17), languages (5.18), and home page features, review highlights, recording filters, a calendar feed, a guide for an email address, an In the News page, site search and statistics without cookies. Work owed, open questions and the problems table extended. |
| 0.2 | 11-07-26 00:58 | Revised for rulings 32 to 34. Added the full and basic paths (section 4), the Website group in System Settings (5.2) and the chapter connector (5.3). Information from the customer relationship management system now appears as part of the page (5.4). The forms (5.5) and donations (5.6) are now separate sections. Work owed (7) gains the build items. Requirements renumbered. |
| 0.1 | 11-07-26 00:40 | First draft, from the planning discussion of 11-06-26 and 11-07-26 and rulings 24 to 31. |
