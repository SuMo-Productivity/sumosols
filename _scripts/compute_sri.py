"""One-shot helper: fetch CDN assets and emit SHA-384 SRI hashes.

Used to populate `integrity=` attributes in HTML when the site loads a
script or stylesheet from a CDN. Run locally with:
    py _scripts/compute_sri.py

URLS is currently empty. The site dropped Bootstrap and FontAwesome in
favour of hand-written CSS, so no page loads an SRI-able third-party
asset any more. The only remaining external request is Google Fonts,
which cannot be pinned with SRI: the stylesheet at fonts.googleapis.com
is generated per user-agent and changes without notice, so any hash you
computed would break for some visitors.

If a CDN dependency is added back, put its full URL in URLS, run the
script, and paste the printed integrity string into every page that
loads it.

GitHub Pages is in `.nojekyll` mode, so this file IS served at
https://www.sumosols.com/_scripts/compute_sri.py. That is intentional —
the script contains no secrets, and serving it costs nothing. It never
executes on the server; only its printed output (the hash strings) is
copied into HTML.
"""

import base64
import hashlib
import sys
import urllib.request

URLS: list[str] = []

UA = "Mozilla/5.0 (sumosols-build/1.0)"


def main() -> int:
    if not URLS:
        print(
            "URLS is empty — the site loads no SRI-able CDN assets.\n"
            "Add a URL to URLS in this file if that changes.",
            file=sys.stderr,
        )
        return 0
    for url in URLS:
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            data = urllib.request.urlopen(req, timeout=20).read()
        except Exception as e:
            print(f"FAIL {url} -> {e}", file=sys.stderr)
            continue
        digest = hashlib.sha384(data).digest()
        sri = "sha384-" + base64.b64encode(digest).decode()
        print(f"{url}\n  integrity=\"{sri}\"\n  bytes={len(data)}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
