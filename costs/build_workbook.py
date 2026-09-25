"""Build the Business Mentors Association cost and dues workbook.

Run:  python3 build_workbook.py [output.xlsx]      (default: association-costs.xlsx)

The workbook holds the formulas; the comma-separated files beside this script
are a readable snapshot of what those formulas produced. Change a price here,
rebuild, and re-export the snapshot so the two stay in step.

Every figure is sourced in notes-and-sources.csv and explained in prose in
../docs/cost-list.md. Needs openpyxl.
"""

import sys
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

BLUE = Font(name="Arial", size=10, color="0000FF")    # an input you may change
BLACK = Font(name="Arial", size=10)                   # calculated
GREEN = Font(name="Arial", size=10, color="008000")   # read from another sheet
BOLD = Font(name="Arial", size=10, bold=True)
TITLE = Font(name="Arial", size=12, bold=True)
HDRFILL = PatternFill("solid", fgColor="DDDDDD")
YEL = PatternFill("solid", fgColor="FFFF00")          # the key levers
CUR = "$#,##0;($#,##0);-"
CUR2 = "$#,##0.00;($#,##0.00);-"
PCT = "0.0%"
THIN = Border(bottom=Side(style="thin"))

ASSUMPTIONS = [
    ("Account owners with paid mailboxes", 2, None,
     "Ruling 18: at least two owners"),
    ("People in the password vault", 3, None,
     "Business plans require at least 3"),
    ("People in the request system", 3, None,
     "Support team size"),
    ("Fee for an outside body holding the money", 0.10, PCT,
     "Published range 5%-15%; 3%-8% for the lighter form of sponsorship"),
    ("Contingency", 0.10, PCT, "Rule of thumb"),
    ("Anthropic nonprofit discount", 0.80, PCT, "Stated by Doug 09-19-26"),
    ("Google Workspace nonprofit price", 0, CUR2,
     "Free edition once qualified (stated by Doug)"),
    ("Federal exemption application fee", 600, CUR,
     "$600 full form; $275 short form if receipts stay under $50,000. Only if exempt status is sought"),
    ("Advanced Pack nonprofit price", 295, CUR,
     "EspoCRM nonprofit price for the extension, per year (stated by Doug 09-20-26)"),
    ("Statutory agent (Ohio), per year", 125, CUR,
     "Ohio requires an agent with a physical Ohio address. A volunteer with one may serve for $0; services charge about $99-$300"),
]
OWNERS, VAULT, REQ = "Assumptions!$B$5", "Assumptions!$B$6", "Assumptions!$B$7"
SPON, CONT, DISC = "Assumptions!$B$8", "Assumptions!$B$9", "Assumptions!$B$10"
GWS, EXEMPT = "Assumptions!$B$11", "Assumptions!$B$12"
ADVPACK_NP, AGENT = "Assumptions!$B$13", "Assumptions!$B$14"

# category, item, unit price, quantity (a name = from an assumption), times per
# year, nonprofit factor (a name = from an assumption), note
RECURRING = [
    ("Infrastructure", "Domain name (Cloudflare, at cost)", 11, 1, 1, 1,
     "Estimate; not checked at the registrar"),
    ("Infrastructure", "Shared test system - CRM server (4 GB)", 24, 1, 12, 1,
     "DigitalOcean published price"),
    ("Infrastructure", "Shared test system - server backups", 4.80, 1, 12, 1,
     "20 percent of the server price (published)"),
    ("Infrastructure", "Shared test system - application container", 12, 1, 12, 1,
     "Published range $5-$12; check Cleveland's bill"),
    ("Infrastructure", "Shared test system - application database", 7, 1, 12, 1,
     "$7 development database; a managed database costs more"),
    ("Infrastructure", "EspoCRM Advanced Pack licence (test CRM)", 395, 1, 1, "advpack",
     "Standard $395 a year; $295 on the nonprofit price. Whether the Association's test system can share Cleveland's licence is not settled"),
    ("Tools", "Google Workspace mailboxes", 7, "owners", 12, "gws",
     "$7 per person per month on the annual plan. Free nonprofit edition once qualified"),
    ("Tools", "Password vault (Proton Pass Professional)", 4.49, "vault", 12, 1,
     "Published third-party summary; Essentials is $1.99"),
    ("Tools", "Request system (ClickUp Unlimited)", 7, "req", 12, 1,
     "Published. The free plan may be enough - set the quantity to 0 to test that"),
    ("Tools", "AI development tool (Claude Max)", 100, 1, 12, "claude",
     "Published. $200 for the larger plan. Nonprofit discount stated by Doug"),
    ("Tools", "GitHub organization", 0, 1, 12, 1, "Free plan"),
    ("Organization", "Directors and officers insurance", 800, 1, 1, 1,
     "Published average. May be $0 if another body's policy covers it"),
    ("Organization", "General liability insurance", 500, 1, 1, 1,
     "Published average. Same note as above"),
    ("Organization", "Cyber liability insurance", 0, 1, 1, 1,
     "PRICE NEEDED - volunteers can reach chapters' systems, which hold client and mentor records"),
    ("Organization", "Statutory agent (Ohio)", "agent", 1, 1, 1,
     "Required for an Ohio limited liability company (rulings 23 and 24). $0 if a volunteer with an Ohio address serves"),
]

CHAPTER = [
    ("CRM server (4 GB)", 24, 12, 1, 1, 1,
     "Same size as the trial chapter's. A large chapter may need more memory"),
    ("CRM server backups", 4.80, 12, 1, 1, 1, "20 percent of the server price"),
    ("Application container", 12, 12, 1, 1, 1, "Published range $5-$12 per month"),
    ("Application database", 15, 12, 1, 1, 1,
     "Managed database for live data; the $7 development database is not suitable for production"),
    ("Domain name", 11, 1, 1, 1, 1, "Most chapters already own one, so this may be $0"),
    ("Domain name records (Cloudflare)", 0, 1, 1, 1, 1, "Free plan"),
    ("Google Workspace - staff mailboxes", 0, 12, 4, 10, 20,
     "Free nonprofit edition. At standard prices this is $7 per person per month"),
    ("Google Workspace - mentor mailboxes", 0, 12, 10, 40, 100,
     "Free nonprofit edition. Set the quantity to 0 if mentors use their own email"),
    ("Advanced Pack extension licence", 295, 1, 1, 1, 1,
     "Nonprofit price stated by Doug; $395 standard"),
    ("Google Integration extension licence", 0, 1, 1, 1, 1,
     "PRICE NEEDED - required by the network standard"),
    ("Password vault (Proton Pass)", 4.49, 12, 3, 3, 5,
     "Business plans require at least 3 people"),
    ("Video meeting account (public webinars only)", 16, 12, 0, 1, 1,
     "Estimate. Only a chapter that runs public webinars needs one"),
]

NOTES = [
    ("Prices stated by Doug",
     "EspoCRM Advanced Pack $395 a year standard and $295 for nonprofits. Anthropic discounts 80 percent for nonprofits. Google Workspace has a free nonprofit edition."),
    ("Nonprofit programs",
     "All three need the Association to qualify. It is a limited liability company owned by its member chapters (rulings 23 and 24), so eligibility must be confirmed with each provider."),
    ("Google Workspace", "emailtooltester.com/en/blog/google-workspace-pricing/"),
    ("DigitalOcean", "digitalocean.com/pricing/droplets and digitalocean.com/pricing/app-platform"),
    ("Proton Pass", "ifeeltech.com/blog/proton-pass-business-review"),
    ("ClickUp", "clickup.com/pricing"),
    ("Claude", "claude.com/pricing"),
    ("Ohio company fees",
     "Articles of organization $99; no annual report and no yearly state fee; statutory agent about $125 a year: llcforge.com/llc-costs/ohio/ and llcuniversity.com/ohio-llc/registered-agent/"),
    ("Fee for an outside body holding the money",
     "5%-15% of funds received; 3%-8% for the lighter form: holisticunderground.org/fiscal-sponsorship/fees"),
    ("Insurance",
     "Directors and officers about $800 a year, general liability about $500 a year: insureon.com/nonprofit-business-insurance/cost"),
    ("Federal exemption application", "irs.gov Form 1023 user fee"),
    ("Not checked",
     "The test system's application and database prices are estimates. Cleveland's current bill is the better source."),
]


def build(path):
    wb = Workbook()

    a = wb.active
    a.title = "Assumptions"
    a["A1"] = "Business Mentors Association - cost assumptions"
    a["A1"].font = TITLE
    a["A2"] = "Blue cells are inputs. Yellow cells are the key levers. Black cells are calculated."
    a["A2"].font = BLACK
    for col, head in ((1, "Input"), (2, "Value"), (3, "Note")):
        c = a.cell(4, col, head)
        c.font, c.fill = BOLD, HDRFILL
    for i, (label, value, fmt, note) in enumerate(ASSUMPTIONS):
        r = 5 + i
        a.cell(r, 1, label).font = BLACK
        c = a.cell(r, 2, value)
        c.font, c.fill = BLUE, YEL
        if fmt:
            c.number_format = fmt
        a.cell(r, 3, note).font = BLACK
    for col, w in {1: 38, 2: 14, 3: 78}.items():
        a.column_dimensions[get_column_letter(col)].width = w

    s = wb.create_sheet("Recurring costs")
    s["A1"] = "Recurring annual costs - the Association's own"
    s["A1"].font = TITLE
    s["A2"] = ("Column F is today's price. Column H applies the nonprofit programs once the "
               "Association qualifies. Blue = input, black = calculated, green = read from Assumptions.")
    s["A2"].font = BLACK
    heads = ["Category", "Item", "Unit price", "Quantity", "Times per year",
             "Annual - standard", "Nonprofit factor", "Annual - nonprofit", "Note and source"]
    for i, h in enumerate(heads, 1):
        c = s.cell(4, i, h)
        c.font, c.fill, c.border = BOLD, HDRFILL, THIN
        c.alignment = Alignment(wrap_text=True, vertical="top")
    first = 5
    for i, (cat, item, price, qty, times, factor, note) in enumerate(RECURRING):
        r = first + i
        s.cell(r, 1, cat).font = BLACK
        s.cell(r, 2, item).font = BLACK
        if price == "agent":
            c = s.cell(r, 3, f"={AGENT}")
            c.font = GREEN
        else:
            c = s.cell(r, 3, price)
            c.font = BLUE
        c.number_format = CUR2
        if qty in ("owners", "vault", "req"):
            ref = {"owners": OWNERS, "vault": VAULT, "req": REQ}[qty]
            c = s.cell(r, 4, f"={ref}")
            c.font = GREEN
        else:
            c = s.cell(r, 4, qty)
            c.font = BLUE
        s.cell(r, 5, times).font = BLUE
        c = s.cell(r, 6, f"=C{r}*D{r}*E{r}")
        c.font, c.number_format = BLACK, CUR
        if factor == "claude":
            c = s.cell(r, 7, f"=1-{DISC}")
            c.font = GREEN
        elif factor == "gws":
            c = s.cell(r, 7, f"={GWS}/C{r}")
            c.font = GREEN
        elif factor == "advpack":
            c = s.cell(r, 7, f"={ADVPACK_NP}/C{r}")
            c.font = GREEN
        else:
            c = s.cell(r, 7, factor)
            c.font = BLUE
        c.number_format = PCT
        c = s.cell(r, 8, f"=F{r}*G{r}")
        c.font, c.number_format = BLACK, CUR
        c = s.cell(r, 9, note)
        c.font = BLACK
        c.alignment = Alignment(wrap_text=True, vertical="top")
    last = first + len(RECURRING) - 1
    sub = last + 1
    s.cell(sub, 2, "Subtotal - recurring costs").font = BOLD
    for col, letter in ((6, "F"), (8, "H")):
        c = s.cell(sub, col, f"=SUM({letter}{first}:{letter}{last})")
        c.font, c.number_format = BOLD, CUR
    for col, w in {1: 16, 2: 42, 3: 12, 4: 10, 5: 14, 6: 18, 7: 16, 8: 18, 9: 60}.items():
        s.column_dimensions[get_column_letter(col)].width = w

    t = wb.create_sheet("Annual total")
    t["A1"] = "Annual total and dues"
    t["A1"].font = TITLE
    for col, head in ((1, "Line"), (2, "Standard prices"), (3, "With nonprofit programs")):
        c = t.cell(3, col, head)
        c.font, c.fill = BOLD, HDRFILL
    t["A4"] = "Recurring costs (from the previous sheet)"
    t["B4"] = f"='Recurring costs'!F{sub}"
    t["C4"] = f"='Recurring costs'!H{sub}"
    t["A5"] = "Fee for an outside body holding the money"
    t["B5"] = f"=B4/(1-{SPON})-B4"
    t["C5"] = f"=C4/(1-{SPON})-C4"
    t["A6"] = "Contingency"
    t["B6"] = f"=(B4+B5)*{CONT}"
    t["C6"] = f"=(C4+C5)*{CONT}"
    t["A7"] = "Annual total to be covered by dues"
    t["B7"] = "=SUM(B4:B6)"
    t["C7"] = "=SUM(C4:C6)"
    for row in range(4, 8):
        t.cell(row, 1).font = BOLD if row == 7 else BLACK
        for col in (2, 3):
            c = t.cell(row, col)
            c.number_format = CUR
            c.font = BOLD if row == 7 else BLACK
    t["A9"] = "One-time costs of forming the company"
    t["A9"].font = BOLD
    for col, head in ((1, "Item"), (2, "Amount"), (3, "Note")):
        c = t.cell(10, col, head)
        c.font, c.fill = BOLD, HDRFILL
    onetime = [
        ("Ohio articles of organization", 99, "Published"),
        ("Trade name registration (only if the public name differs)", 39, "Published"),
        ("Operating agreement and attorney review", 0,
         "PRICE NEEDED - the document that carries the liability shield, the release vote and the chapters' ownership"),
        ("Federal tax-exemption application (only if exempt status is sought)", f"={EXEMPT}",
         "$275 short form, $600 full form. Not required to operate"),
    ]
    for i, (item, amount, note) in enumerate(onetime):
        r = 11 + i
        t.cell(r, 1, item).font = BLACK
        c = t.cell(r, 2, amount)
        c.number_format = CUR
        c.font = GREEN if isinstance(amount, str) else BLUE
        t.cell(r, 3, note).font = BLACK
    r = 11 + len(onetime)
    t.cell(r, 1, "Total one-time").font = BOLD
    c = t.cell(r, 2, f"=SUM(B11:B{r-1})")
    c.font, c.number_format = BOLD, CUR
    for col, w in {1: 46, 2: 20, 3: 60}.items():
        t.column_dimensions[get_column_letter(col)].width = w

    d = wb.create_sheet("Dues by band")
    d["A1"] = "Dues by size band"
    d["A1"].font = TITLE
    d["A2"] = ("Ruling 11: larger chapters pay more and carry more votes. Enter the number of chapters "
               "in each band and the share each band carries. Nothing here is decided.")
    d["A2"].font = BLACK
    d["A2"].alignment = Alignment(wrap_text=True, vertical="top")
    heads = ["Band", "Chapters", "Share per chapter", "Dues per chapter - standard",
             "Dues per chapter - with nonprofit programs", "Band total - standard",
             "Band total - with nonprofit programs"]
    for i, h in enumerate(heads, 1):
        c = d.cell(4, i, h)
        c.font, c.fill = BOLD, HDRFILL
        c.alignment = Alignment(wrap_text=True, vertical="top")
    for i, (name, count, share) in enumerate((("Small", 1, 1), ("Medium", 1, 2), ("Large", 1, 3))):
        r = 5 + i
        d.cell(r, 1, name).font = BLACK
        for col, value in ((2, count), (3, share)):
            c = d.cell(r, col, value)
            c.font, c.fill = BLUE, YEL
        c = d.cell(r, 4, f"=IF($B$9=0,0,'Annual total'!$B$7*C{r}/$B$9)")
        c.font, c.number_format = BLACK, CUR
        c = d.cell(r, 5, f"=IF($B$9=0,0,'Annual total'!$C$7*C{r}/$B$9)")
        c.font, c.number_format = BLACK, CUR
        c = d.cell(r, 6, f"=D{r}*B{r}")
        c.font, c.number_format = BLACK, CUR
        c = d.cell(r, 7, f"=E{r}*B{r}")
        c.font, c.number_format = BLACK, CUR
    d.cell(8, 1, "Total chapters").font = BOLD
    d.cell(8, 2, "=SUM(B5:B7)").font = BOLD
    d.cell(9, 1, "Total shares").font = BOLD
    d.cell(9, 2, "=SUMPRODUCT(B5:B7,C5:C7)").font = BOLD
    d.cell(10, 1, "Total dues collected").font = BOLD
    for col in (6, 7):
        letter = get_column_letter(col)
        c = d.cell(10, col, f"=SUM({letter}5:{letter}7)")
        c.font, c.number_format = BOLD, CUR
    for col, w in {1: 24, 2: 14, 3: 18, 4: 24, 5: 30, 6: 22, 7: 30}.items():
        d.column_dimensions[get_column_letter(col)].width = w

    c_ = wb.create_sheet("Chapter costs")
    c_["A1"] = "What a chapter pays itself, per year"
    c_["A1"].font = TITLE
    c_["A2"] = ("These are the chapter's own costs, paid directly in its own accounts. Association dues "
                "are NOT included: they are not decided and are reported separately (ruling 22). Prices "
                "assume the chapter qualifies as a nonprofit.")
    c_["A2"].font = BLACK
    c_["A2"].alignment = Alignment(wrap_text=True, vertical="top")
    c_.merge_cells("A2:J2")
    c_.row_dimensions[2].height = 32
    heads = ["Item", "Unit price", "Times per year", "Small - quantity", "Medium - quantity",
             "Large - quantity", "Small - annual", "Medium - annual", "Large - annual", "Note"]
    for i, h in enumerate(heads, 1):
        cell = c_.cell(4, i, h)
        cell.font, cell.fill, cell.border = BOLD, HDRFILL, THIN
        cell.alignment = Alignment(wrap_text=True, vertical="top")
    first = 5
    for i, (item, price, times, qs, qm, ql, note) in enumerate(CHAPTER):
        r = first + i
        c_.cell(r, 1, item).font = BLACK
        cell = c_.cell(r, 2, price)
        cell.font, cell.number_format = BLUE, CUR2
        c_.cell(r, 3, times).font = BLUE
        for col, q in ((4, qs), (5, qm), (6, ql)):
            c_.cell(r, col, q).font = BLUE
        for col, qcol in ((7, "D"), (8, "E"), (9, "F")):
            cell = c_.cell(r, col, f"=$B{r}*{qcol}{r}*$C{r}")
            cell.font, cell.number_format = BLACK, CUR
        cell = c_.cell(r, 10, note)
        cell.font = BLACK
        cell.alignment = Alignment(wrap_text=True, vertical="top")
    last = first + len(CHAPTER) - 1
    own = last + 1
    c_.cell(own, 1, "Chapter's own costs - nonprofit prices").font = BOLD
    for col in (7, 8, 9):
        letter = get_column_letter(col)
        cell = c_.cell(own, col, f"=SUM({letter}{first}:{letter}{last})")
        cell.font, cell.number_format = BOLD, CUR
    staff_row, mentor_row = first + 6, first + 7
    r = own + 2
    c_.cell(r, 1, "Same chapter at standard prices (no nonprofit status)").font = BOLD
    mail = r + 1
    c_.cell(mail, 1, "Mailboxes at $7 per person per month").font = BLACK
    for col, qcol in ((7, "D"), (8, "E"), (9, "F")):
        cell = c_.cell(mail, col, f"=7*12*({qcol}{staff_row}+{qcol}{mentor_row})")
        cell.font, cell.number_format = BLACK, CUR
    ap = mail + 1
    c_.cell(ap, 1, "Advanced Pack at $395 instead of $295").font = BLACK
    for col in (7, 8, 9):
        cell = c_.cell(ap, col, "=395-295")
        cell.font, cell.number_format = BLACK, CUR
    total = ap + 1
    c_.cell(total, 1, "Chapter's own costs - standard prices").font = BOLD
    for col in (7, 8, 9):
        letter = get_column_letter(col)
        cell = c_.cell(total, col, f"={letter}{own}+{letter}{mail}+{letter}{ap}")
        cell.font, cell.number_format = BOLD, CUR
    c_.cell(total + 2, 1,
            "Example sizes: small = 4 staff and 10 mentors; medium = 10 staff and 40 mentors; "
            "large = 20 staff and 100 mentors. Change any quantity to match a real chapter.").font = BLACK
    c_.cell(total + 3, 1,
            "Association dues are on the 'Dues by band' sheet and are not added here.").font = BLACK
    for col, w in {1: 46, 2: 12, 3: 14, 4: 16, 5: 18, 6: 16, 7: 18, 8: 18, 9: 18, 10: 60}.items():
        c_.column_dimensions[get_column_letter(col)].width = w

    n = wb.create_sheet("Notes and sources")
    n["A1"] = "Where each price came from"
    n["A1"].font = TITLE
    for col, head in ((1, "Topic"), (2, "Detail")):
        cell = n.cell(3, col, head)
        cell.font, cell.fill = BOLD, HDRFILL
    for i, (topic, detail) in enumerate(NOTES):
        r = 4 + i
        n.cell(r, 1, topic).font = BLACK
        cell = n.cell(r, 2, detail)
        cell.font = BLACK
        cell.alignment = Alignment(wrap_text=True, vertical="top")
    n.column_dimensions["A"].width = 34
    n.column_dimensions["B"].width = 110

    wb.save(path)
    return path


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "association-costs.xlsx"
    print("written:", build(out))
