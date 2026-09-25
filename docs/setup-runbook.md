# Business Mentors Association — account setup runbook

**Document:** Step-by-step setup of the Association's domain, email, password vault, hosting account and code hosting
**Version:** 1.1
**Status:** Draft for first use
**Owner:** Doug Bower
**Last Updated:** 09-25-26

---

## Before you start

**What this runbook does.** It opens the Association's accounts in the Association's own name, as ruling 18 requires: every account is registered to an Association address, has at least two owners, and has its sign-ins kept in an Association password vault. It ends with the accounts open. Moving the shared test system onto the new hosting account is a separate job with its own runbook, written once these accounts exist.

**You need:**

- About two hours for Parts 1 to 3; Parts 4 and 5 take about thirty minutes each.
- A payment card. Until a fiscal sponsor is in place, bills are paid personally; keep every receipt for reimbursement.
- **The second owner** — a trusted volunteer who will be a co-owner of every account. Parts 1 to 3 can be done without them; they must be added before this runbook is finished.
- An authenticator app on your phone, for two-step verification on every account.

**Terms used below:**

- **Domain name records (DNS)** — the public settings that tell the internet where a domain's website and mail are handled. They are edited in Cloudflare.
- **Group address** — an address such as admin@ that belongs to no single person and delivers every message to all its members.
- **Recovery codes** — one-time codes an account gives you for signing in when your phone is unavailable. Every set goes into the password vault.

**The rule for every account:** the sign-in email is **admin@businessmentorsassociation.org** (a group address, so both owners receive every reset and notice), two-step verification is on, and the sign-in and recovery codes are saved in the password vault.

---

## Part 1 — Register the domain (Cloudflare)

The domain has to exist before any Association address can. So Cloudflare is opened under your own email first and moved to admin@ in step 1.8.

1.1. Go to **dash.cloudflare.com** and create an account with your own email address. Turn on two-step verification (**My Profile → Authentication**).

1.2. In the left menu open **Domain Registration → Register Domains**.

1.3. Search **businessmentorsassociation.org**.
- If it is available, continue.
- **If it is taken, stop here.** Ruling 19 names this domain and a replacement needs a ruling.

1.4. Buy it for one year with auto-renew **on**.

1.5. For the registrant contact, enter yourself as the person and **"Business Mentors Association"** as the organization. The Association has no legal existence yet, so a person must be the registrant; this is changed to the Association after incorporation.

1.6. Leave **WHOIS privacy** on (Cloudflare's default).

1.7. Confirm that the domain appears under **Websites** with Cloudflare as its DNS. Registration through Cloudflare sets this automatically.

1.8. **Do this after Part 2 is complete:** in **Manage Account → Configurations** (or **My Profile**), change the account's email to admin@businessmentorsassociation.org, then in **Manage Account → Members** invite the second owner as a **Super Administrator**. Save the Cloudflare sign-in and recovery codes in the vault (Part 3).

---

## Part 2 — Set up email (Google Workspace)

Google Workspace needs one person account to be its first administrator. That is you; the admin@ group comes after.

2.1. Go to **workspace.google.com** and choose **Get started**. Business name: **Business Mentors Association**. Number of employees: **Just you**.

2.2. When asked for a domain, choose **Yes, I have one I can use** and enter **businessmentorsassociation.org**.

2.3. Create your administrator account, for example **doug@businessmentorsassociation.org**. Choose the smallest plan offered (Business Starter). Enter the payment card. Apply for the free nonprofit edition once the Association qualifies (ruling 21).

2.4. **Verify the domain.** Google offers to sign in to Cloudflare and add the records itself. Accept it. If that option does not appear, Google shows a verification record (a line beginning `google-site-verification=`); add it in Cloudflare under **Websites → businessmentorsassociation.org → DNS → Records → Add record**, type **TXT**, name **@**, and return to Google to click **Verify**.

2.5. **Mail routing.** Google's automatic setup adds this. If it did not, add in Cloudflare DNS: type **MX**, name **@**, mail server **smtp.google.com**, priority **1**. Remove any other MX records.

2.6. **Sender proof records** — these stop the Association's mail being marked as spam. In Cloudflare DNS add:
- type **TXT**, name **@**, content `v=spf1 include:_spf.google.com ~all`
- type **TXT**, name **_dmarc**, content `v=DMARC1; p=none; rua=mailto:admin@businessmentorsassociation.org`

2.7. **Signing key.** In the Google Admin console (**admin.google.com**) go to **Apps → Google Workspace → Gmail → Authenticate email**, click **Generate new record**, and copy the value. In Cloudflare DNS add type **TXT**, name **google._domainkey**, and paste the value. Wait an hour, return to the same page and click **Start authentication**.

2.8. **Create the group addresses.** In the Admin console go to **Directory → Groups → Create group**, three times:
- **admin@** — members: you and the second owner. Purpose: the sign-in address for every Association account.
- **support@** — members: the volunteers who answer chapters.
- **releases@** — members: the volunteers who build and announce releases.

For each group, under **Access settings**, set **Who can post** to **Anyone on the web**. Without this, messages from the hosting company, the code host and the others are silently rejected.

2.9. **Second administrator.** Create a person account for the second owner (**Directory → Users → Add new user**), then under **Account → Admin roles → Super Admin → Assign users**, assign them. Two administrators means neither of you can be locked out of the Association's email.

2.10. **Test it.** From a personal email account, send a message to admin@. Both owners must receive it. Do not continue until they do.

2.11. Turn on two-step verification for both administrator accounts, and save their recovery codes in the vault (Part 3).

---

## Part 3 — Create the password vault (Proton Pass)

The Association uses the same password manager already ruled for chapters, so volunteers learn one tool.

3.1. Go to **proton.me/pass** and choose a **business** plan. Sign up with **admin@businessmentorsassociation.org** as the account email.

3.2. Turn on two-step verification and save the recovery phrase. **The recovery phrase is the one thing not stored in the vault itself.** Print it and give one copy to each owner to keep somewhere safe.

3.3. Invite the second owner into the organization as an **administrator**.

3.4. Create one shared vault named **Association Operations**, shared with both owners.

3.5. Save these into it, one entry each: the Cloudflare sign-in and recovery codes; both Google administrator sign-ins and recovery codes; the Google Workspace billing details (plan and renewal date, not the card number).

3.6. Now go back and finish **step 1.8** (move Cloudflare to admin@ and add the second owner).

---

## Part 4 — Open the hosting account (DigitalOcean)

4.1. Go to **cloud.digitalocean.com** and sign up with **admin@businessmentorsassociation.org**.

4.2. Turn on two-step verification and save the sign-in and recovery codes in the vault.

4.3. Name the team **Business Mentors Association**.

4.4. Enter the payment card. Under **Billing**, set a **billing alert** at a monthly amount you choose, so an unexpected bill is noticed in days, not at month end.

4.5. Under **Team → Members**, invite the second owner with the **Owner** role.

4.6. Stop here. Moving the shared test system into this account is the next runbook.

---

## Part 5 — Put the code hosting under two owners

The Association's records and, later, the open-source applications live on GitHub. Organizations there are owned by people's own accounts, not by an email address, so this part adds the second owner and points the billing contact at admin@.

5.1. Decide where the Association's repositories live. They are in a personal account today (`dbower44022/business-mentors-association`); under ruling 18 they belong in an account the Association controls. Creating an organization and transferring the repository into it is the cleanest move, and GitHub keeps redirects for transferred repositories.

5.2. In that account's or organization's settings, set the **billing email** to **admin@businessmentorsassociation.org**.

5.3. Invite the second owner's GitHub account with the **Owner** role.

5.4. Turn on **Require two-factor authentication** for everyone.

5.5. Install the Claude GitHub App on it, so Claude can keep the records updated: **github.com/apps/claude → Configure**, choose the account, give it access to the repository, and click **Install**.

5.6. Save both owners' GitHub recovery codes in the vault.

---

## Done when

- businessmentorsassociation.org is registered, with auto-renew on.
- A message sent to admin@ reaches both owners.
- Cloudflare, Google Workspace, Proton Pass, DigitalOcean and the code hosting each have **two owners**, two-step verification, and their sign-ins and recovery codes in the Association Operations vault.
- Every receipt is kept for reimbursement.

---

## Change log

| Version | Date | Change |
|---|---|---|
| 1.1 | 09-25-26 | Moved into this repository. Part 5 rewritten: the records now live in a personal GitHub account and should be transferred to an Association-controlled one. Nonprofit edition noted in step 2.3. |
| 1.0 | 09-19-26 | First version, from rulings 15 and 18 to 20. |
