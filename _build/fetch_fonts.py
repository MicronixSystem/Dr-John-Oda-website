"""Download the latin subsets of Archivo (variable width + weight), Inter and
Source Serif 4 italic from Google Fonts into site/assets/fonts, and print the
@font-face rules to paste into main.css. Run: python -I fetch_fonts.py
"""
import re
import urllib.request
from pathlib import Path

SITE = Path(__file__).resolve().parent.parent
OUT = SITE / "assets" / "fonts"
OUT.mkdir(parents=True, exist_ok=True)
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/130.0 Safari/537.36")
CSS = ("https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,400..900"
       "&family=Inter:wght@400..700"
       "&family=Source+Serif+4:ital,opsz,wght@1,8..60,400..500&display=swap")


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read()


css = get(CSS).decode("utf-8")
blocks = re.findall(r"/\* ([\w-]+) \*/\s*@font-face \{(.*?)\}", css, re.S)
rules = []
for subset, body in blocks:
    if subset != "latin":
        continue
    family = re.search(r"font-family: '([^']+)'", body).group(1)
    style = re.search(r"font-style: (\w+)", body).group(1)
    url = re.search(r"src: url\((.*?)\)", body).group(1)
    name = f"{family.lower().replace(' ', '-')}-{style}-latin.woff2"
    data = get(url)
    (OUT / name).write_bytes(data)
    print(f"/* {name}: {len(data) // 1024} KB */")
    body = re.sub(r"src: url\(.*?\) format\('woff2'\);",
                  f"src: url(\"../fonts/{name}\") format(\"woff2\");", body)
    rules.append("@font-face {" + body.rstrip() + "\n}")
print("\n".join(rules))
