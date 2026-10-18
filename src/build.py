"""Build the self-contained map page.

Inlines the Leaflet stylesheet and the simplified OpenStreetMap base layer
(base_s.json) into template.html, then writes:

  guwahati_pandal_map.html  page fragment (for the Claude artifact, which adds its own skeleton)
  index.html                full standalone page (for GitHub Pages or any static host)

    python build.py [leaflet.css]

leaflet.css is the Leaflet 1.9.4 stylesheet, e.g. from
https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.min.css
(defaults to ./leaflet.css).
"""
import sys
from pathlib import Path

here = Path(__file__).parent
css = Path(sys.argv[1]) if len(sys.argv) > 1 else here / "leaflet.css"

page = (here / "template.html").read_text(encoding="utf-8")
page = page.replace("/*LEAFLET_CSS*/", css.read_text(encoding="utf-8"))
page = page.replace("/*BASE_JSON*/", (here / "base_s.json").read_text(encoding="utf-8"))
(here / "guwahati_pandal_map.html").write_text(page, encoding="utf-8", newline="\n")

head = (
    '<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
    '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
    '<meta name="description" content="Unofficial Durga Puja 2026 pandal-hopping map of Guwahati, '
    'with three routes from IIT Guwahati.">\n'
    "<style>body{margin:0}[hidden]{display:none!important}</style>\n</head>\n<body>\n"
)
(here / "index.html").write_text(head + page + "\n</body>\n</html>\n", encoding="utf-8", newline="\n")
print(f"wrote guwahati_pandal_map.html and index.html ({len(page):,} chars)")
