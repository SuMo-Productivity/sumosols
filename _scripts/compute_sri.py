"""One-shot helper: fetch CDN assets and emit SHA-384 SRI hashes.

Used during site build to populate `integrity=` attributes in HTML.
Run locally with:
    py _scripts/compute_sri.py

Lives under `_scripts/` so Jekyll (the default GitHub Pages build) excludes
it from the deployed site — directories starting with `_` are skipped.
The script itself never runs on GitHub Pages; only its printed output is
copied into HTML.
"""

import base64
import hashlib
import sys
import urllib.request

URLS = [
    "https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css",
    "https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css",
]

UA = "Mozilla/5.0 (sumosols-build/1.0)"


def main() -> int:
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
