# Guwahati Pandal Map

An unofficial Durga Puja 2026 pandal-hopping guide for Guwahati. It has three routes that start from IIT Guwahati, each pandal is pinned on a map of the city, and every stop links to Google Maps directions.

**Unofficial guide, locations approximate.** It is not affiliated with any puja committee, the city or IIT Guwahati. Solid pins sit on a landmark mapped in OpenStreetMap. Dashed pins mark the centre of a neighbourhood. Check each committee's page for this year's themes and timings.

## Files

- `index.html` is the whole site, a single self-contained page. It loads Leaflet from cdnjs and fonts from Google Fonts.
- `src/template.html` is the page source.
- `src/base_s.json` holds the simplified river, road and rail layers taken from OpenStreetMap.
- `src/leaflet.css` is the Leaflet 1.9.4 stylesheet, which gets inlined into the page.
- `src/build.py` inlines all of these into the page. Run `python src/build.py`, then copy `src/index.html` to the repo root.

## Hosting

To serve it with GitHub Pages, go to Settings → Pages, choose **Deploy from a branch**, then pick `main` and `/ (root)`.

## Credits and licences

- Map data © [OpenStreetMap](https://www.openstreetmap.org/copyright) contributors, available under the ODbL. Place coordinates come from OSM via Nominatim and Overpass.
- [Leaflet](https://leafletjs.com) 1.9.4, under the BSD-2-Clause licence.
- Fonts: Tiro Bangla and Hind Siliguri, under the SIL Open Font License.
- Pandal names and themes come from 2024–26 reports in The Sentinel, NE Now, Outlook Traveller and Curlytales, plus some general local knowledge.
