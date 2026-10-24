"""
Downloads the K-12 mandatory-disclosure documents from snsacademy.org into
Complaince/K12/ using the file names the website expects.

Run from the SNS-Groups folder:   python fetch_k12_docs.py
(needs internet access; uses only the Python standard library)
"""
import os, re, sys, urllib.request, urllib.parse
from html.parser import HTMLParser

SRC = "https://snsacademy.org/mandatoryDisclosure/"
OUT = os.path.join("Complaince", "K12")

# keyword found in the row label on snsacademy.org  ->  file name used by mandatory-disclosure/index.html
WANTED = [
    (("affiliation", "upgradation"),            "01-affiliation-letter"),
    (("societ", "trust", "registration"),       "02-trust-registration"),
    (("no objection", "noc"),                   "03-noc"),
    (("rte",),                                  "04-rte-recognition"),
    (("building",),                             "05-building-safety"),
    (("fire",),                                 "06-fire-safety"),
    (("deo",),                                  "07-deo-certificate"),
    (("water", "sanitation", "health"),         "08-water-health-sanitation"),
    (("fee structure",),                        "c1-fee-structure"),
    (("calender", "calendar"),                  "c2-academic-calendar"),
    (("management committee", "smc"),           "c3-smc-list"),
    (("parents teacher", "pta"),                "c4-pta-members"),
    (("three-year", "three year", "result"),    "c5-board-results"),
]

class Rows(HTMLParser):
    """Collects (row text, first link in the row) for every <tr>."""
    def __init__(self):
        super().__init__(); self.rows = []; self.cur = None
    def handle_starttag(self, t, a):
        if t == "tr": self.cur = {"text": "", "href": None}
        elif t == "a" and self.cur is not None and self.cur["href"] is None:
            self.cur["href"] = dict(a).get("href")
    def handle_endtag(self, t):
        if t == "tr" and self.cur is not None:
            self.rows.append(self.cur); self.cur = None
    def handle_data(self, d):
        if self.cur is not None: self.cur["text"] += " " + d

def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    return urllib.request.urlopen(req, timeout=60).read()

def main():
    os.makedirs(OUT, exist_ok=True)
    p = Rows(); p.feed(get(SRC).decode("utf-8", "replace"))
    done = set()
    for r in p.rows:
        text = re.sub(r"\s+", " ", r["text"]).lower()
        if not r["href"] or r["href"].startswith("#"): continue
        for keys, name in WANTED:
            if name in done or not any(k in text for k in keys): continue
            url = urllib.parse.urljoin(SRC, r["href"])
            ext = os.path.splitext(urllib.parse.urlparse(url).path)[1].lower() or ".pdf"
            dest = os.path.join(OUT, name + ext)
            try:
                open(dest, "wb").write(get(url)); done.add(name)
                print("OK  ", dest, "<-", url)
            except Exception as e:
                print("FAIL", name, url, e)
            break
    missing = [n for _, n in WANTED if n not in done]
    if missing:
        print("\nNot downloaded (save these manually into", OUT + "):", *missing, sep="\n  ")
    print("\nNote: the site links expect .pdf. If any file came down as .doc/.docx/.jpg,",
          "convert it to PDF or update its href in mandatory-disclosure/index.html.")

if __name__ == "__main__":
    sys.exit(main())
