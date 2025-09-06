import json, pathlib, sys
from lxml import etree

ROOT = pathlib.Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "texts.xml"
DTD  = ROOT / "data" / "texts.dtd"
SITE = ROOT / "site"
INDEX = SITE / "index.html"

PLACEHOLDER = "/* DATA_PLACEHOLDER */"
SITE_URL = "https://vickymx.github.io/Multilingua/"

def parse_and_validate():
    xml = etree.parse(str(DATA))
    dtd = etree.DTD(str(DTD))
    if not dtd.validate(xml):
        print("DTD validation failed:\n", dtd.error_log)
        sys.exit(1)
    return xml

def to_js_data(xml):
    out = []
    for entry in xml.xpath("//entry"):
        eid = entry.get("id")
        cat = (entry.findtext("category") or "").strip()
        langs = {}
        for lang in entry.findall("lang"):
            code = lang.get("code")
            title = (lang.findtext("title") or "").strip()
            content = (lang.findtext("content") or "").strip()
            langs[code] = {"title": title, "content": content}
        out.append({"id": eid, "category": cat, "langs": langs})
    return out

def inject_into_index(data):
    html = INDEX.read_text(encoding="utf-8")
    if PLACEHOLDER not in html:
        print(f"ERROR: placeholder {PLACEHOLDER!r} not found in {INDEX}")
        sys.exit(1)
    payload = "window.DATA = " + json.dumps(data, ensure_ascii=False) + ";"
    html = html.replace(PLACEHOLDER, payload)
    INDEX.write_text(html, encoding="utf-8")
    print(f"Injected {len(data)} entries into {INDEX}")

if __name__ == "__main__":
    xml = parse_and_validate()
    data = to_js_data(xml)
    inject_into_index(data)
    print("Done.")
    print(f"Deploy the contents of {SITE} to GitHub Pages, then open: {SITE_URL}")
