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
| `assets/og.png` | 1200x630 social share image (`og:image`) |
| `favicon.svg` | Inline-SVG favicon |
| `.well-known/security.txt` | RFC 9116 contact file for security reporters |
| `robots.txt` | Crawler instructions |
| `sitemap.xml` | Sitemap |
| `CNAME` | GitHub Pages custom-domain config |
| `CLAUDE.md` | Project rules for Claude Code sessions |
| `.nojekyll` | Disables Jekyll on GitHub Pages so files are served as-is (required for `.well-known/security.txt`) |
| `_scripts/compute_sri.py` | Helper to compute SRI hashes for CDN tags (currently unused — no CDN assets) |
| `_scripts/og-card.html` | Source for `assets/og.png`; re-export at 1200x630 after headline changes |

## Stack

- Hand-written CSS in `assets/style.css` — no CSS framework
- IBM Plex Sans / Serif / Mono (Google Fonts CDN — the only external request)
- No JavaScript at all, on any page
- No build step

Bootstrap and FontAwesome were removed in favour of hand-written CSS.
The nav is four links that wrap on small screens, so it needs no
JavaScript toggle.

### Design system

Defined as custom properties at the top of `assets/style.css`.

| Token | Value | Use |
|---|---|---|
| `--ink` | `#12211C` | Body text, footer background |
| `--pine` | `#1C3A30` | Masthead, hero, contact panel |
| `--moss` | `#2F6350` | Links on paper |
| `--paper` | `#F3F2ED` | Page background |
| `--brass` / `--brass-lt` | `#8A6524` / `#D9B24C` | **Security-research line only** |

Brass is the single accent and is reserved for the security-research
line — the research row on the homepage, the research cell in the hero
index, disclosure callouts, and focus rings. Adding it elsewhere breaks
the signal it carries.

Type: IBM Plex Sans for headings and UI, IBM Plex Serif for prose, IBM
Plex Mono for real identifiers only (email addresses, file paths,
domains) — not for decorative labels.

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
