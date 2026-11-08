# Decisions — the Association's rulings

**Document:** Every ruling that defines the Business Mentors Association
**Version:** 2.33
**Status:** Current
**Owner:** Doug Bower
**Last Updated:** 11-08-26 12:25

---

## How to use this file

Nothing here is a task. **Every ruling below is Doug's.** A ruling changes only when Doug changes it, and then the replaced wording stays visible, marked and dated. Items Claude drafted or assumed are in their own sections at the bottom and are not rulings until Doug confirms them.

The rulings of 09-19-26 came out of one planning conversation. Several of them replace rulings made earlier for the chapter network, whose decision file lives in `dbower44022/cbm-client-intake` at `prds/chapter-network/DECISIONS.md`. **That file is being corrected to match**; until the correction is merged it still states the replaced wording.

---

## Rulings

### Ruled 09-19-26

1. **Chapters hold ultimate authority over all their own technology.** The Association supports each chapter's own technical personnel. Association staff work directly on a chapter's system only when the chapter's support contact is unavailable. *Replaces the chapter network's ruling that the central organization holds the only administrator accounts.*

2. **Releases.** The Association builds and tests each release of the application files. Chapter technical personnel test and certify it. Each chapter's technical personnel then agree a deployment date with their chapter, so chapters may run slightly different versions for a time. *Replaces the chapter network's ruling that all chapters move to each release together.*

3. **One application.** Chapters deploy the application as the Association designs it and do not change it. A chapter that wants something new — a field, for example — submits a feature request; the central technical committee considers it, and if accepted it is built and delivered to every chapter. Chapters may differ through optional settings and different processes; the application itself is the same everywhere. *Amends the chapter network's ruling of strictly identical function, which allowed no per-chapter difference at all.*

4. **A release goes forward on a vote of the chapter representatives**, under a process written into the Association's operating agreement. The vote is counted as a double majority — see rulings 11 and 12.

5. **Legal form: fiscal sponsorship first.** An established nonprofit holds the Association's money and signs for it. Becoming an independent nonprofit is a high priority. **Amended 09-25-26 by ruling 23:** the Association is formed as a separate limited liability company. Whether fiscal sponsorship still has a part to play, and whether the company seeks tax-exempt status, are open.

6. **The chapter applications become open source. Doug Bower continues to own CRM Builder.**

7. **The Association's records live in their own repository.** Ruled as `BusMentAssociation/contact`; **superseded 09-25-26** by this repository, `dbower44022/business-mentors-association`. The records are not kept anywhere else.

8. **Scope: technical services only, for now.** Whether the Association later offers non-technical services is left open, and no process for adding services is defined at this time.

9. **Membership: independent business mentoring nonprofits only.**

10. **The central technical committee has one technical contact from every member chapter while membership is small.** Once membership passes a number set in the governing documents, it becomes a small committee whose seats are elected by the chapter representatives, with the Association's technical lead alongside them.

11. **Dues and voting are set in size bands.** Larger chapters pay more and have more say.

12. **Votes pass by double majority.** A vote needs both a majority of the weighted votes and a majority of the member chapters, so no chapter can carry a vote alone, large or small.

13. **The Association starts with volunteers.** Development and support are done by volunteers at first; the committee decides later whether and when to pay for staff.

14. **Which body governs the Association's money, staffing and membership is left to the committee.** The options in front of it: the chapter representatives as a members' council; a small board elected by the representatives; or the technical committee governing as well.

15. **The shared test system moves to a new server the Association owns.** Today's test system is reproduced on, or moved to, an Association-owned server. It holds test data rather than Cleveland's data, the training is built on that data, and it is restored every night at midnight; all three come with it. The trial chapter system is not used for this, because it has neither training data nor a nightly restore.

16. **One system serves both training and release testing.** A second system costs more than it is worth, and testing against the realistic test data makes usability testing easier. The release waiting for certification is installed on the shared test system, and training runs on whatever version is installed.

17. **No limit on how far behind the current release a chapter may fall.** It is not worth enforcing. The Association neither requires chapters to update by a deadline nor limits support to recent releases.

18. **The Association's accounts are held in its own name, and the domain comes first.** Each account — hosting, code hosting, request system and the rest — is opened under an Association email address, with at least two volunteer owners and the sign-ins kept in an Association-owned password vault, billed to the Association once it can pay its own bills.

19. **The Association's domain is businessmentorsassociation.org.** Availability has not been confirmed at the registrar. **Replaced 11-06-26 by ruling 25.**

20. **The Association's email runs on Google Workspace** — the same system every chapter uses. Accepted cost: a fee per person per month until the Association qualifies for the free nonprofit edition.

### Ruled 09-20-26

21. **Nonprofit pricing is assumed where it exists.** The Advanced Pack extension costs $395 a year at standard price and $295 a year at EspoCRM's nonprofit price. Anthropic offers nonprofits an 80 percent discount. Google Workspace has a free nonprofit edition. Each requires the Association to qualify, which rulings 23 and 24 may affect.

### Ruled 09-22-26

22. **Chapter cost estimates exclude Association dues.** Dues are not decided and are reported separately from what a chapter pays itself.

### Ruled 09-25-26

23. **The Association is set up as a separate limited liability company, to shield the individual chapters from its liabilities.** A claim against the Association reaches the Association's own assets, not the chapters' buildings, endowments or donor funds; each chapter's exposure is limited to its dues and to its own systems. *Amends ruling 5, whose path — fiscal sponsorship first, then an independent nonprofit — assumed a nonprofit rather than a company.* Left open: whether the company seeks tax-exempt status, whether fiscal sponsorship still has a part to play, and whether nonprofit pricing (ruling 21) survives the change.

24. **The member chapters own the company.** Each member holds a stake, the representatives' votes follow from that ownership, and a chapter's exposure is limited to its dues and its own systems. Neither Doug Bower nor any single chapter owns it. *Settles what ruling 23 left unsaid, and confirms what the proposal summary had assumed.* It also keeps the door open on tax-exempt status, which generally requires every owner of an exempt company to be exempt itself — and every member chapter is.

### Ruled 11-06-26

25. **The Association has two domains, registered the way the Association recommends for every chapter.** businessmentorsassociation.org is the website domain. The shorter mentorsassociation.org is the email domain. *Replaces ruling 19.* *Corrected 11-07-26: first recorded as "The Association's domain is mentorsassociation.org. Both mentorsassociation.org and businessmentorsassociation.org are registered; the shorter name is the one the Association uses."*

26. **The chapter website template is a hybrid.** A chapter copies the template website and then owns it: its pages, layout, design and words. The parts that connect to the chapter's customer relationship management system — the mentor directory, events and registration, and the intake forms — are maintained by the Association and updated as a separate piece. Accepted cost: two things to keep versions of, and the connection between the website and the chapter applications must stay stable across application releases. Chosen over a starter kit copied once and never updated, and over a template the Association maintains in full. *Amended 11-07-26 by ruling 34: for a WordPress chapter, the website's look and its key pages are set in the chapter applications' System Settings and applied by the Association's chapter connector.*

27. **The Association's maintained website piece works on any website.** It is embed code — a frame served by the chapter applications, plus a small script that sizes the frame and keeps links inside it shareable — that any website accepting pasted code can use. A chapter keeps whatever website platform it runs; Boston keeps Squarespace and Cleveland keeps WordPress. The template website is one recommended build, not a required platform. Accepted cost: the embedded parts follow colour settings rather than the website's own styling, search engines credit mentor profiles to the application's web address rather than the chapter's, and some hosted builders allow scripts only on higher-priced plans. Chosen over a plugin for one platform that every chapter would have to run. A plugin for one platform may be added later as an option. *Extends the chapter network's ruling 8, which named WordPress only.* *Amended 11-07-26 by ruling 34: the embed code remains the path for chapters not on WordPress; WordPress chapters get the fuller chapter connector.*

28. **The template website is built on WordPress.** Chosen for an openly shareable template, a full exit for a chapter that leaves, editing a volunteer can manage, and the largest pool of vendors and volunteers who know it. Accepted cost: someone must apply security updates to WordPress, its plugins and its server every month. Chosen over Squarespace (easiest editing and no upkeep, but the template cannot be shared openly and a departing chapter loses its design) and over a static site (cheapest and safest, but the weakest editing for volunteers). Wix, Webflow, Google Sites, Ghost, Drupal, Joomla and serving the whole site from the chapter applications were set aside earlier in the same discussion.

29. **A chapter's WordPress site runs on a lightly managed host on DigitalOcean (Cloudways).** The host keeps the server's operating system and PHP up to date, takes backups, provides the security certificate and a staging copy. The chapter's only upkeep is WordPress's own updates, which can run automatically. The website never shares a server with the chapter's customer relationship management system. Accepted cost: roughly $50 to $100 a year more than a server the chapter runs itself (prices from memory, not yet checked), one more account for the chapter to own, and a one-line change to Rochester's request, which names a basic DigitalOcean server. Chosen over a server the chapter runs itself and over a fully managed WordPress host. Hosting every chapter's site centrally was set aside because it contradicts ruling 1.

30. **Online donations use a Stripe Payment Link in the chapter's own Stripe account, as Cleveland's site does now, and a feature request goes to the committee for the chapter applications to record each gift in the customer relationship management system automatically.** The template ships the Donate button and the script that opens the payment page; each chapter supplies its own link. Under the feature request, Stripe notifies the chapter applications when a payment completes and the applications create the donor and the contribution record; card details stay with Stripe. Accepted cost: until the feature is accepted and built, staff enter gifts by hand and the chapter sends donors' tax acknowledgments itself; the Association takes on code that handles payment notices. Chosen over a hosted donation service and over hand entry with no feature request.

31. **The Association builds the template website itself, using Cleveland's site (clevelandbusinessmentors.org) and Boston's site (bbmentors.org) as examples.** The two sites are models of structure and function; their words, photographs and branding are not copied into the template. A chapter such as Rochester adapts the finished template rather than commissioning a site of its own design, if it chooses to — under ruling 1 the choice is the chapter's. Chosen to avoid the cost and complexity of having Rochester's vendor build the template: a fairness question over Rochester paying for every chapter, and a contract clause giving the Association rights to reuse and publish the vendor's work. Accepted cost: the template waits on volunteer time, adding to the risk of depending on one volunteer, and a chapter ready to build now may not wait for it.

32. **When the customer relationship management system holds what a website list shows, the website shows it from there, not from a copy.** Mentors, events and registration, webinar recordings and the intake forms already come from the chapter applications. Two more lists move there by feature requests to the committee: **partners and sponsors**, which gain a logo and a "show on website" switch on their records; and **client success stories**, added as information on the client record in the customer relationship management system and shown on the website through the embed code of ruling 27. Leadership stays a WordPress page. Accepted cost: new work for the applications and the customer relationship management system; until it is built, the partners and client stories pages are edited by hand in WordPress. Chosen over keeping partner and story lists as hand-edited WordPress pages.

33. **The Association supports chapter websites the way it supports the chapter applications.** The chapter's own technical person goes first; the Association helps with the whole website — WordPress itself as well as the embedded parts — when that person is unavailable or asks for help (ruling 1). The Association also fixes anything in the embedded parts it maintains. Accepted cost: the Association supports websites it does not control and that chapters may have changed in any way, and that load falls on the same volunteers already named as the Association's largest risk. Chosen over supporting only the embedded parts, and over that plus published template improvements.

### Ruled 11-07-26

34. **The Association builds a WordPress add-on, the chapter connector (a working name), and a new Website group in the chapter applications' System Settings.** The administrator sets the website's colours, fonts and logo once in System Settings, and the chapter connector applies them to the whole WordPress site. The chapter connector creates and owns the key pages that show information from the customer relationship management system — the mentor directory and profiles, workshops and events, recordings, partners and sponsors, and client stories — and a switch in System Settings turns each one, and its menu entry, on or off. The chapter connector needs no password, keeps the last values it fetched so the website stays up when the applications are down, and is open source. Chapters not on WordPress, such as Boston on Squarespace, keep the framed embed code of ruling 27, with colours from the same System Settings but without page switches. Accepted cost: WordPress, with a theme that keeps its colours and fonts in WordPress's central style settings, becomes a requirement for the integrated website; the Association maintains an add-on through every WordPress release, and a defect in it reaches every chapter at once; the chapter connector must work with older releases of the chapter applications; the Association supports two ways in, and some features may reach WordPress chapters only. Chosen over making WordPress a membership requirement and over keeping the embed-only design. *Amends rulings 26 and 27.* The build goes through the chapter applications' own process in `cbm-client-intake`.

35. **On a WordPress site, information from the customer relationship management system appears as part of the page itself, not inside a frame.** The chapter applications produce the mentor directory and profiles, the events list, recordings, partners and sponsors, and client stories as finished page content; the chapter connector fetches it as a page is served, keeps a copy for a few minutes, and places it in the WordPress page. Mentor profiles become pages on the chapter's own domain. The intake, registration and other forms stay in frames for now. Accepted cost: the applications' content sits inside styling the Association does not fully control, guarded by a unique prefix on every style name the applications use and an automated test of it; a change in the customer relationship management system takes a few minutes to appear; the applications must permit the mentor search to fetch results from the website. Chosen over frames everywhere.

36. **New versions of the chapter connector are published in WordPress's public add-on directory, and only after the release vote passes** (ruling 4). Each chapter chooses on its own website whether updates install automatically or wait for its technical person, which keeps ruling 2. Accepted cost: the chapter connector carries the GNU General Public License, version 2 or later, or a compatible licence; the directory reviews the first submission, which can take days to weeks; every published version is public at once. Chosen over an update channel the Association runs itself and over manual download.

37. **A campaign follows a visitor through the website for the length of the visit.** A campaign link in the chapter applications may point at any website page, not only a form. The website remembers the campaign until the visitor closes the browser tab and adds it to every "Request a Mentor" button and every form on that visit, so the records created carry the campaign as the applications' campaign tagging already does (marketing rulings 26 and 27 in `cbm-client-intake/prds/prospect-marketing/rulings.md`). Each website button also carries a fixed placement tag, such as home page or mentor profile, so a chapter can see which buttons bring clients. On the full path the chapter connector does this; on the basic path it works only when a visitor goes straight from the landing page to a form. Accepted cost: new work in the chapter connector and the campaign links; the website stores a small marker, holding nothing personal, in the visitor's browser for the length of the tab, and the Privacy Policy must say so. Chosen over campaign links that open forms only, and over per-campaign landing pages with no memory.

38. **The figures the website states about a chapter are counted from the customer relationship management system.** The chapter applications count them daily — for example active mentors, clients mentored in the past twelve months, sessions held and workshop attendees — and the chapter connector shows them. The administrator switches each figure on or off in the System Settings Website group, so no chapter has to show a figure it does not want. A feature request goes to the committee under ruling 3. Accepted cost: every figure needs a written definition all chapters share; counted figures may be lower than numbers a chapter already publishes. Chosen over figures typed by hand into pages, and over figures entered once in System Settings.

39. **A "Request a Success Story" action sends a client a form for their own story.** Staff or the mentor choose the action on the client's record; the client receives a personal link that belongs to their record, of the kind the chapter applications already send to known contacts. The form asks for exactly what the website's client story shows, in separate text boxes, and accepts several photographs. The client gives consent in the form, and the submission lands on the client record awaiting review; staff edit and approve it, then switch it on. A feature request goes to the committee under ruling 3. Accepted cost: a new form, a review step each chapter must keep up with, and stories still depend on someone choosing the action. Chosen over stories written by staff, and over an open nomination form on the website.

40. **The Association's website lists every member chapter, and each chapter's website links to it for visitors outside its area.** The directory on mentorsassociation.org gives each chapter's name, the area it serves and a link; every chapter website carries a line such as "Outside our area? Find a mentoring chapter near you". A chapter's stated area is information for visitors, not a boundary. Passing a client's submission from one chapter's customer relationship management system to another's is sent to the committee as a governance question. Accepted cost: the Association needs a website of its own and someone to keep the directory current, and each chapter states its area. Chosen over doing nothing, and over building referrals between chapters' records now.

41. **Chapters share events through an "Add Association Events" function in event management.** A chapter marks an event "Shared with Association Members". Another chapter browses every shared event from the other chapters and adds the ones it wants to its own calendar. An added event is managed exactly like a local event: the adding chapter shows it on its own website, takes its own registrations and runs its own marketing campaigns and registration links, so a registrant becomes the adding chapter's contact. The event stays linked to the hosting chapter's webinar for viewing. Two problems are open and being decided: how a registrant from the adding chapter gets access to the host's webinar when it requires registration, and how the adding chapter learns which of its contacts attended. Chosen in place of a network calendar where registration happens at the hosting chapter.

42. **Chapters' applications register guests with each other for shared events.** When a contact registers on the adding chapter's website, the adding chapter's applications ask the hosting chapter's applications to add a guest; the host's applications add the person to the host's webinar and return the person's own join link, which the adding chapter's confirmation email delivers. After the webinar, the host's applications read the webinar service's report of who joined and return attendance and minutes for the adding chapter's guests only, which the adding chapter records on its own contacts. Guests are never added to the host's customer relationship management system; the host sees how many guests each chapter sent, not who they are. The same connection lets Add Association Events browse other chapters' shared events. Chapters trust each other through a list of member chapters' applications addresses kept by the Association beside the directory of ruling 40. Accepted cost: a new connection between chapters' applications; each guest's name and email reach the host's webinar account, which the chapter agreement must allow and the registration form must state; automatic attendance from the webinar service must be switched on and proven first; guests count against the host's capacity, so the host sets a limit on guest seats. Chosen over shared events without registration, and over hosting shared events on an Association webinar account. *Answers the two problems left open by ruling 41.*

43. **The template website and the chapter applications are built ready for other languages, with English at launch.** All text a visitor reads is kept in a form that can be translated, so adding Spanish later is a translation job rather than a rebuild. Mentor profiles gain a "languages spoken" field, so a visitor can find a mentor who speaks their language; a feature request goes to the committee under ruling 3. Accepted cost: more care in the build, and visitors who do not read English are not served at launch beyond finding a mentor who speaks their language. Chosen over English only, Spanish forms and key pages now, and automatic machine translation.

### Ruled 11-07-26 — website items Claude drafted, confirmed by Doug

Doug confirmed items 3 to 21 of Claude's drafted list as written, and changed items 1 and 2.

44. **Forms appear in frames, served from the chapter's own applications address.** The intake, mentor application, information request, partner, sponsor and newsletter signup forms and event registration appear in frames on both paths; on Boston's basic path the mentor directory, events and recordings do too (ruling 35 puts them into the page itself on WordPress sites). A frame is never served from a hosting provider's default address, and each carries a link that opens the same form full-screen if the frame fails. Every "Request a Mentor" button on the website leads to the same client intake form; Cleveland's site has three destinations.

45. **The newsletter signup is a chapter applications form, not the mailing service's own form.** A subscriber lands in the customer relationship management system first, and the applications' existing synchronisation passes them to Constant Contact. The applications have no such form today (checked 11-07-26), so it is built.

46. **The general contact form is the chapter applications' information request form**, so every enquiry lands in the customer relationship management system.

47. **Chapter-wide values live in the System Settings Website group, and the chapter connector supplies them to the website** — the chapter's name, abbreviation, contact email, telephone, mailing address, employer identification number, social media addresses, and Stripe Payment Link address. The footer and Donate button read them from there, so each is set once (follows ruling 34).

48. **If a visitor arrives through a second campaign in the same visit, the later campaign replaces the earlier** (follows ruling 37).

49. **The template's pages.** Drawn from Cleveland's and Boston's sites (ruling 31). Published at launch: Home; About, including mission, history, how mentors are chosen and the leadership team; How It Works, including what a client can expect; Find a Mentor, with the embedded directory and profiles; Request a Mentor; Become a Mentor; Workshops and Events, with embedded listings, registration and recordings; Support Us, with the Donate button, sponsorship and partnership; Contact; Frequently Asked Questions; Privacy Policy; Terms of Use. Shipped as unpublished drafts a chapter may switch on: Blog; Resources and Templates; Partners and Sponsors; Client Stories; In the News; Client Code of Conduct; Mentor Code of Conduct *(the two codes amended 11-08-26 by ruling 73: published, marked as drafts)*; a campaign landing page like Cleveland's postcard page. On every page: newsletter signup, member sign-in link to the chapter applications, social links, and a footer stating 501(c)(3) status and the employer identification number. Legal pages ship as drafts marked for review by the chapter's own attorney; Boston's site has no privacy policy although its forms collect personal details. *The single Partners and Sponsors page was replaced 11-07-26 by ruling 66.*

50. **A "How can we help you?" chooser on the home page.** Three tiles: ask a question (the information request form), request a mentor (the client intake form) and meet our mentors (Find a Mentor), as on Cleveland's site.

51. **Featured mentors and client stories on the home page.** Mentor and story records carry a "feature on home page" switch; the chapter connector shows the switched-on ones on the home page, rotating daily (follows ruling 32).

52. **Public review highlights are entered by hand.** An editor enters up to three short excerpts, with the reviewer's first name or initials, and a link to the chapter's public review page. No automatic feed: it needs a paid key from the review site, and review sites restrict how their reviews are shown.

53. **Press mentions and podcasts share one page, "In the News"**, shipped switched off: an editor adds each mention or episode with its date, outlet and link. It replaces the separate Podcasts page.

54. **A guide offered for an email address uses the mailing service's own landing page**, as Boston does, so a subscriber reaches the customer relationship management system through the existing synchronisation. The template's Resources page has a place to feature one.

55. **Recorded webinars can be filtered by subject**, using the event topics the customer relationship management system holds, as on Boston's video library. Shared events a chapter has added link to the host's recording.

56. **An events calendar feed.** The chapter applications publish the chapter's public events as a calendar feed a visitor can subscribe to, linked from Workshops and Events. A feature request goes to the committee under ruling 3.

57. **A client success story is published only with the client's recorded permission.** The client record carries the client's consent to publication and its date, alongside the story text, a short quotation, a photograph and the "show on website" switch. Mentoring is confidential, so a story with no recorded consent never appears (follows ruling 32).

58. **What the success story form asks** (follows ruling 39). The business name, and how the client wants to be named (full name, first name only, or business name only); the kind of business and its town; a one-line headline; three text boxes — the challenge before mentoring, what the client and mentor worked on, and the results, with optional figures such as funding raised or jobs created; a short quotation of up to about 200 characters for the home page and story cards; whether to name the mentor, who is filled in from the engagement; up to five photographs, with the client choosing the main one and confirming they own the photographs and that everyone pictured agrees; and the business's website and social media addresses. Consent is given separately for the website, the chapter's social media and its newsletter, with the client's typed name and the date recorded. The form says the client can withdraw consent at any time; switching the story off removes it from the website within minutes.

59. **The client approves the final wording.** If staff change the client's words beyond spelling and length, the edited story goes back to the client through the same personal link for a one-click approval before it is published (follows ruling 39).

60. **The template website uses WordPress's built-in block editor, not a paid page builder** such as Elementor, which Cleveland's site uses. This avoids a licence fee and keeps the template simple to copy (follows ruling 28).

61. **The shared test system gains a WordPress test website running the chapter connector**, so chapters' technical people can certify a chapter connector release before the vote; the version awaiting certification is installed there by hand (follows rulings 16 and 36).

62. **Site search.** The website uses WordPress's own search, and the chapter connector makes mentor profiles and events findable through it.

63. **Visitor statistics without cookies, so no consent banner is needed.** The template uses a statistics service that sets no cookies, such as Cloudflare Web Analytics, which is free and available in the Cloudflare account each chapter already owns. Cleveland's site uses Google Site Kit today and would change only if Cleveland adopts the template.

64. **The template website meets the Web Content Accessibility Guidelines (WCAG) version 2.2 at level AA** on every page, in every key page and in every framed form. Every image has a text description.

65. **The first prototype is the website side only, with the chapter applications imitated.** It runs locally: WordPress, a starter theme, a first chapter connector, and a stand-in for the chapter applications that serves the Website settings and mentor content. It shows crm-test's real intake form in a frame. It lives in a new local repository, `~/Dropbox/Projects/chapter-website-prototype`, not pushed until the Association's code hosting account exists. Nothing changes in `cbm-client-intake`. It tests the riskiest assumption first — that the chapter connector can own the key pages and their menu entries — and its data shapes become the written requirement for the applications' side. Accepted cost: the applications' side stays imitated until a second prototype builds it. Chosen over an end-to-end prototype and over prototyping shared events first. Work proceeds in PROTOTYPE mode from 11-07-26 01:59.

### Ruled 11-07-26 — after the first prototype

66. **Partners and sponsors have separate pages: Our Partners and Our Sponsors.** Each is a key page served from the customer relationship management system and switched on or off on its own. *Replaces the single Partners and Sponsors page in ruling 49.*

67. **The template supports a header graphic.** Accepted cost: one more image each chapter supplies.

68. **The template replaces the starter theme's header and footer with its own.** The starter theme's footer menus held placeholder links (Blog, Authors, Shop and others) that looked wrong. The template's footer has a Mentoring column listing the key pages, filled by the chapter connector, and an About us column of ordinary pages.

69. **The header graphic is set in the System Settings Website group, like the colours, and shown under the header: tall on the home page, a narrow strip on every other page.** Confirmed by Doug after seeing it in the prototype. The chapter's logo returns the visitor to the home page.

70. **The test chapter website runs on Cloudways, in Doug's own account for now, at chapter-demo.mentorsassociation.org,** and connects to crm-test to test the integration end to end. It moves to an Association account once those exist. Its domain name records are in the Association's Cloudflare account. Every step is written as a runbook others can follow. Accepted cost: the account is in Doug's name until the move, which departs from ruling 18 for that time, and the move is one more step. Chosen over waiting for an Association account and over a plain DigitalOcean server. The applications' side is built in a separate session in `cbm-client-intake`, in that repository's DETAIL mode. *Amended 11-07-26 by ruling 71: the test website connects to crm-test only until the demo chapter's own applications are running.*

71. **The demo system is built as a full new chapter, by following the New Chapter Deployment Guide, in two tracks.** First track: the test chapter website goes live connected to crm-test, as ruling 70 says, so the integration between the website and the chapter applications is tested now. Second track, in parallel: a demo chapter is built stage by stage from the guide, with its own Google Workspace, customer relationship management system, chapter applications, Constant Contact account, video meeting account, Stripe account in test mode, and website. Each gap the guide shows is corrected in the guide as that stage is done, through `cbm-client-intake`'s own process. When the demo chapter's applications are running, the test website is switched from crm-test to them. The demo chapter then serves as the shared test system of ruling 15. Accepted cost: monthly accounts in Doug's name beyond the test system the cost list already budgets, estimated at $40 to $70 a month (from memory, not checked); one switch-over step; the finished demo takes several sessions; open question 24, on the Advanced Pack licence, must be answered before the customer relationship management system is built. Chosen over the website alone on crm-test, which shows Cleveland's name and accounts and never tests the guide, and over building the whole demo chapter before any website test. *Amends ruling 70.*

72. **The demo chapter is the Association itself, set up as a chapter.** The Association gets its own chapter environment on its own two domains (ruling 25): a new Google Workspace on mentorsassociation.org (ruling 20), a Constant Contact account, a Zoom account and the rest, exactly as a new chapter would. No separate demo domains or demo Workspace are registered. *Answers the question ruling 71 left open, which domains and Google Workspace the demo chapter uses.* Accepted cost, confirmed by Doug 11-07-26 (first noted by Claude): the chapter applications' Google machine account holds a permission grant over every mailbox in that Workspace (deployment guide stage 10), so it reaches the Association's real mailboxes; and the demo's invented contacts must not be sent mail from the Association's real domain, which would harm its standing with mail providers.

### Ruled 11-08-26

73. **The template publishes all four policy documents — Privacy Policy, Terms of Use, Client Code of Conduct and Mentor Code of Conduct — each marked as a draft for review by the chapter's own attorney.** Every public form's consent box links to the two codes, so unpublished codes would leave those links dead on every form. Accepted cost: the codes are live, marked as drafts, before a chapter's attorney has read them. Chosen over keeping the codes unpublished until each chapter publishes them. *Amends ruling 49, which shipped both codes as unpublished drafts.* Doug chose Claude's recommendation 11-08-26.

---

## Decisions the committee will make

- Whether and when to pay for staff (ruling 13).
- Which body governs money, staffing and membership (ruling 14).
- The size bands, their shares and the dues amounts (ruling 11).
- Whether chapters have territories, and whether a client's submission may be passed from one chapter's customer relationship management system to another's, with the client's consent (ruling 40). Both need a data-sharing agreement between chapters before anything is built.

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
| 2.33 | 11-08-26 12:25 | Ruling 73 added: the template publishes all four policy documents, marked as drafts. Ruling 49 marked as amended. |
| 2.32 | 11-07-26 14:52 | Ruling 72: Doug confirmed the two consequences Claude had noted as accepted costs. |
| 2.31 | 11-07-26 14:46 | Ruling 72 added: the demo chapter is the Association itself, set up as a chapter on its own domains and accounts. |
| 2.30 | 11-07-26 14:38 | Ruling 71 added: the demo system is built as a full new chapter by the deployment guide, with the test website on crm-test first and switched over later. Ruling 70 marked as amended. |
| 2.29 | 11-07-26 14:25 | Merged with the line of work published on 09-25-26, which had added rulings 23 and 24 (the separate limited liability company, and the member chapters owning it). Those keep their numbers. The rulings of 11-06-26 and 11-07-26 were renumbered from 23 to 68 to 25 to 70, here and in every document in this repository that cites them. The two lines numbered their versions separately, so versions 2.1 and 2.2 appear twice below, each with its own date. |
| 2.28 | 11-07-26 14:18 | Ruling 25 corrected: businessmentorsassociation.org is the website domain and mentorsassociation.org the email domain, registered the way the Association recommends for every chapter. The drafted item that had the website domain forward to the email domain is removed. |
| 2.27 | 11-07-26 11:11 | Ruling 70: the test chapter website on Cloudways in Doug's account, at chapter-demo.mentorsassociation.org. |
| 2.26 | 11-07-26 11:08 | Ruling 69: the drafted header graphic placement confirmed by Doug, and the logo links home. |
| 2.25 | 11-07-26 11:01 | Rulings 66 to 68 added after the first prototype: separate partners and sponsors pages, a header graphic, the template's own header and footer. Ruling 49 marked as partly replaced. Drafted item added: where the header graphic is set and shown. |
| 2.24 | 11-07-26 01:59 | Ruling 65 added: the first prototype is the website side only, with the applications imitated. |
| 2.23 | 11-07-26 01:46 | Rulings 45 and 55 updated from a reading of the chapter applications' code: no newsletter form exists yet; event topics exist and the recordings library already filters by them. |
| 2.22 | 11-07-26 01:39 | Rulings 44 to 64 added: the website items Claude drafted, confirmed by Doug and moved out of the drafted section. Item 1 reworded to cover forms and the basic path; item 2 changed so the newsletter signup is a chapter applications form. |
| 2.21 | 11-07-26 01:30 | Ruling 43 added: built ready for other languages, English at launch, with a languages spoken field on mentor profiles. |
| 2.20 | 11-07-26 01:29 | Ruling 42 added: guest registration and attendance between chapters' applications. Four drafted items added: review highlights, recording filters, a guide for an email address, the In the News page. |
| 2.19 | 11-07-26 01:28 | Ruling 41 added: chapters share events through Add Association Events; access and attendance for remote webinars still open. |
| 2.18 | 11-07-26 01:21 | Ruling 40 added: a chapter directory on the Association's website. Territories and referrals between chapters added to the committee's decisions. |
| 2.17 | 11-07-26 01:19 | Five drafted items added: featured mentors and stories, the home page chooser, an events calendar feed, site search, and visitor statistics without cookies. |
| 2.16 | 11-07-26 01:14 | Ruling 39 added: the Request a Success Story action. Two drafted items added: what the story form asks, and the client's approval of the final wording. |
| 2.15 | 11-07-26 01:08 | Ruling 38 added: website figures are counted from the customer relationship management system. |
| 2.14 | 11-07-26 01:01 | Ruling 37 added: a campaign follows a visitor through the website for the visit, with placement tags on website buttons. |
| 2.13 | 11-07-26 00:50 | Ruling 36 added: chapter connector versions are published in the public add-on directory after the release vote. Two drafted items added: a test website on the shared test system; chapter-wide values in System Settings. |
| 2.12 | 11-07-26 00:48 | Ruling 35 added: on WordPress sites, customer relationship management content is part of the page, not framed. |
| 2.11 | 11-07-26 00:48 | Ruling 34 added: the chapter connector and a Website group in System Settings. Rulings 26 and 27 marked as amended. |
| 2.10 | 11-07-26 00:29 | Ruling 33 added: the Association supports chapter websites as backup to the chapter's technical person. |
| 2.9 | 11-07-26 00:28 | Ruling 32 added: website lists come from the customer relationship management system where it holds them, including partners, sponsors and client success stories. Drafted item added: a story needs the client's recorded consent. |
| 2.8 | 11-06-26 23:57 | Drafted item added: the template's page set. |
| 2.7 | 11-06-26 23:57 | Ruling 31 added: the Association builds the template itself, using Cleveland's and Boston's sites as examples. |
| 2.6 | 11-06-26 23:49 | Ruling 30 added: donations through a Stripe Payment Link, with a feature request for automatic recording in the customer relationship management system. |
| 2.5 | 11-06-26 23:45 | Ruling 29 added: chapter websites run on a lightly managed host on DigitalOcean. Three drafted items added: embedded connected parts, the newsletter signup, the contact form. |
| 2.4 | 11-06-26 23:43 | Ruling 28 added: the template website is built on WordPress. Drafted item added: the built-in block editor rather than a paid page builder. |
| 2.3 | 11-06-26 23:41 | Ruling 27 added: the maintained website piece is embed code that works on any website platform. |
| 2.2 | 11-06-26 23:40 | Ruling 26 added: the chapter website template is a hybrid of a copied website and a maintained connected piece. |
| 2.1 | 11-06-26 22:47 | Ruling 25 added: both mentorsassociation.org and businessmentorsassociation.org are registered, and mentorsassociation.org is the Association's domain. Ruling 19 marked as replaced. Drafted item added: the second domain forwards to the first. |
| 2.2 | 09-25-26 | Ruling 24 added: the member chapters own the company. Removed from the drafted section, where it had been Claude's assumption. Ruling 4 now names the operating agreement. |
| 2.1 | 09-25-26 | Ruling 23 added: the Association is a separate limited liability company, shielding the chapters. Ruling 5 marked as amended by it. |
| 2.0 | 09-25-26 | Moved into this repository from the interim Claude project document. Ruling 7 superseded: the records live here. Rulings 21 and 22 added. |
| 1.x | 09-19-26 to 09-22-26 | Kept as an interim document in the Claude project while this repository could not be written to. |
