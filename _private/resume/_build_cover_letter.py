"""
Builds the cover letter body inside the copied docx (same fonts/margins/theme
as the resume), replacing the entire <w:body> content but keeping headers,
footers, styles, fonts, and section properties intact.
"""
import zipfile, shutil, re

TARGET = "Franklin Fuchs Cover Letter - Pfizer Marketing AI Product.docx"

with zipfile.ZipFile(TARGET) as z:
    doc = z.read("word/document.xml").decode("utf-8")

# Preserve the sectPr (page size/margins/footers) from the original body.
m = re.search(r'<w:sectPr.*?</w:sectPr>', doc, re.S)
sect_pr = m.group(0)

# Common run property fragments (Garamond, matching resume defaults).
def rpr(bold=False, italic=False, size=None, hyperlink=False):
    parts = ['<w:rPr>']
    if hyperlink:
        parts.append('<w:rStyle w:val="Hyperlink"/>')
    parts.append('<w:rFonts w:ascii="Garamond" w:hAnsi="Garamond"/>')
    if bold:
        parts.append('<w:b/><w:bCs/>')
    if italic:
        parts.append('<w:i/><w:iCs/>')
    if not hyperlink:
        parts.append('<w:color w:val="auto"/>')
    if size:
        parts.append(f'<w:sz w:val="{size}"/><w:szCs w:val="{size}"/>')
    parts.append('</w:rPr>')
    return ''.join(parts)

def para(runs, spacing_after=None, spacing_line="253", border_bottom=False, jc=None):
    pPr = ['<w:pPr><w:pStyle w:val="Default"/>']
    if border_bottom:
        pPr.append('<w:pBdr><w:bottom w:val="single" w:sz="6" w:space="1" w:color="auto"/></w:pBdr>')
    spacing_attrs = f'w:line="{spacing_line}" w:lineRule="auto"'
    if spacing_after is not None:
        spacing_attrs = f'w:after="{spacing_after}" ' + spacing_attrs
    pPr.append(f'<w:spacing {spacing_attrs}/>')
    if jc:
        pPr.append(f'<w:jc w:val="{jc}"/>')
    pPr.append('</w:pPr>')
    body = ''.join(runs)
    return f'<w:p>{"".join(pPr)}{body}</w:p>'

def run(text, bold=False, italic=False, size=None, space_preserve=True):
    space = ' xml:space="preserve"' if space_preserve else ''
    return f'<w:r>{rpr(bold=bold, italic=italic, size=size)}<w:t{space}>{text}</w:t></w:r>'

def hyperlink_run(rid, text, size=None):
    r = f'<w:r>{rpr(size=size, hyperlink=True)}<w:t xml:space="preserve">{text}</w:t></w:r>'
    return f'<w:hyperlink r:id="{rid}" w:history="1">{r}</w:hyperlink>'

# ---------------------------------------------------------------------------
# Header block: Name (large, bold) + contact line (same style as resume)
# ---------------------------------------------------------------------------
name_para = para(
    [run("Franklin Fuchs", bold=True, size="44")],
    spacing_line="253",
    border_bottom=True,
)

contact_runs = []
contact_runs.append(hyperlink_run("rId8", "Fuchs.franklin@gmail.com", size="20"))
contact_runs.append(run(" ", size="20"))
contact_runs.append(run("| ", size="20"))
contact_runs.append(hyperlink_run("rId10", "Website &amp; Portfolio", size="20"))
contact_runs.append(run(" ", size="20"))
contact_runs.append(run("| ", size="20"))
contact_runs.append(hyperlink_run("rId9", "GitHub", size="20"))
contact_runs.append(run(" ", size="20"))
contact_runs.append(run("| ", size="20"))
contact_runs.append(run(" 929-346-8485 ", size="20"))
contact_para = para(contact_runs, spacing_line="253", border_bottom=True)

spacer_para = para(
    [f'<w:r><w:rPr><w:rFonts w:ascii="Garamond" w:hAnsi="Garamond"/><w:color w:val="auto"/><w:sz w:val="8"/><w:szCs w:val="8"/></w:rPr></w:r>'],
    spacing_line="253",
)
# Simplify: an empty spacer paragraph with small font size, no run needed
spacer_para = (
    '<w:p><w:pPr><w:pStyle w:val="Default"/><w:spacing w:line="253" w:lineRule="auto"/>'
    '<w:rPr><w:rFonts w:ascii="Garamond" w:hAnsi="Garamond"/><w:color w:val="auto"/>'
    '<w:sz w:val="8"/><w:szCs w:val="8"/></w:rPr></w:pPr></w:p>'
)

date_para = para([run("September 24, 2026", size="22")], spacing_line="253", spacing_after="120")

recipient_lines = [
    para([run("Pfizer", size="22")], spacing_line="253", spacing_after="200"),
]

salutation_para = para([run("Dear Hiring Manager,", size="22")], spacing_line="253", spacing_after="160")

body_paragraphs = [
    (
        "Two years ago, I supported Pfizer\u2019s AI/ML/Analytics Enterprise "
        "Architecture team, prototyping the vector database and RAG "
        "scaffolding that other teams later built on. What stuck with me was "
        "not the architecture itself, but how much of the actual job was "
        "translation: sitting with commercial and clinical stakeholders, "
        "understanding what they actually needed, and making sure the AI and "
        "cloud foundation underneath could support it before anyone got "
        "attached to a demo."
    ),
    (
        "I have spent the two years since doing a version of that same job "
        "from the business side of the table. At Mondelez, I work inside the "
        "commercial organization (Marketing, Insights, and Revenue Growth "
        "Management), helping those teams find and adopt the right AI and "
        "cloud tools, then partnering with MLOps so the resulting "
        "proof-of-concepts sit on infrastructure that actually holds up. The "
        "pattern is the same either way: a business team has an idea, and "
        "someone has to make sure the AI and data foundation gets built "
        "underneath it quickly and correctly, not after the fact. That is "
        "exactly the kind of bridge this role is built around, and it is "
        "the part of the job I find genuinely interesting rather than just "
        "necessary."
    ),
    (
        "I would like to bring that instinct, plus the Pfizer-side view of "
        "how enterprise AI infrastructure actually gets built, back into a "
        "role built around exactly that kind of translation. I would "
        "welcome the chance to talk more about what your team is building."
    ),
]

body_paras_xml = [
    para([run(text, size="22")], spacing_line="253", spacing_after="160")
    for text in body_paragraphs
]

closing_para = para([run("Best,", size="22")], spacing_line="253", spacing_after="240")
signoff_para = para([run("Franklin Fuchs", bold=True, size="22")], spacing_line="253")

body_content = "".join([
    name_para,
    contact_para,
    spacer_para,
    date_para,
    *recipient_lines,
    salutation_para,
    *body_paras_xml,
    closing_para,
    signoff_para,
])

new_body = f'<w:body>{body_content}{sect_pr}</w:body>'

new_doc = re.sub(r'<w:body>.*?</w:body>', new_body, doc, flags=re.S)

tmp = TARGET + ".tmp"
with zipfile.ZipFile(TARGET) as zin, zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zout:
    for item in zin.infolist():
        data = zin.read(item.filename)
        if item.filename == "word/document.xml":
            data = new_doc.encode("utf-8")
        zout.writestr(item, data)
shutil.move(tmp, TARGET)
print("Cover letter body written.")
