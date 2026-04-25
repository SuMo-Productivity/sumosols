# sumosols

Source for the public Sumo Solutions website at <https://www.sumosols.com/>.

Static site, deployed via GitHub Pages. No build step — edit HTML/CSS
directly and push. The `CNAME` file resolves the apex domain to the
GitHub Pages host.

## Files

| Path | Purpose |
|---|---|
| `index.html` | Homepage |
| `research.html` | Security research service line |
| `responsible-disclosure.html` | Disclosure policy (linked from `/.well-known/security.txt`) |
| `privacy.html` | Privacy Policy |
| `terms.html` | Terms of Use |
| `404.html` | Error page (GitHub Pages serves this on any 404) |
| `assets/style.css` | Shared stylesheet |
| `favicon.svg` | Inline-SVG favicon |
| `.well-known/security.txt` | RFC 9116 contact file for security reporters |
| `robots.txt` | Crawler instructions |
| `sitemap.xml` | Sitemap |
| `CNAME` | GitHub Pages custom-domain config |
| `CLAUDE.md` | Project rules for Claude Code sessions |
| `_scripts/compute_sri.py` | One-shot helper to compute SRI hashes for CDN tags. Lives under `_scripts/` so Jekyll excludes it from the deployed site. |

## Stack

- Bootstrap 5.3.3 (CDN, with SRI integrity)
- FontAwesome 6.5.2 (CDN, with SRI integrity)
- Poppins (Google Fonts CDN)
- Vanilla HTML/CSS — no JS framework, no build step

## Local preview

Open any `.html` file directly in a browser, or run a quick static server:

```sh
py -m http.server 8000
# then http://localhost:8000/
```

## Deploying

```sh
git add -A && git commit -m "<message>" && git push
```

GitHub Pages picks up the push automatically; the live site updates
within a minute.
