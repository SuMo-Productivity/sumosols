# Sumo Solutions Website — Project Rules for Claude

This file is read at the start of every Claude Code session in this repository.
Rules here override default behavior. Add new rules below; do not delete existing
rules without discussion.

---

## Repo overview

Source for the public Sumo Solutions company website at
`https://www.sumosols.com/`, deployed via GitHub Pages.

Stack: static site, Bootstrap 5.3.3 + FontAwesome 6.5.2 + Poppins (Google
Fonts) — all from CDN with SRI integrity attributes. No build step. Edit
HTML/CSS directly and push; GitHub Pages serves on push.

## Content rules

### Do not mention ShieldX

ShieldX is an internal project. **Do not** add it to any HTML page,
metadata, sitemap, README, or commit message in this repo.

### Tone

Concrete, professional, brief. No buzzwords. Replace phrases like
"transformative solutions", "dynamic team", "powerful synergies" with
specific descriptions of what the firm actually does. If a section needs
filler, leave a placeholder or omit the section — never fabricate clients,
metrics, case studies, or team biographies.

### Multi-service framing

Sumo Solutions is a generalist technology firm with four service lines:

1. Custom Software Development
2. Cloud & DevOps
3. Digital Strategy & Consulting
4. Mobile App Security Research

Security research is one line, not the whole pitch. Keep it visible but
not dominant on the homepage.

### Two contact addresses (and only these on the public site)

- `contact@sumosols.com` — general inquiries
- `research@sumosols.com` — security research and responsible disclosure

Other aliases may exist for internal use; do not add them to the public
site without confirming with the user.

### Security-firm posture

Because the firm offers security research, the site is held to a higher
bar than a generic small-business landing page. Maintain:

- `/.well-known/security.txt` (RFC 9116) — current `Expires:` date.
- `responsible-disclosure.html` — linked from `security.txt` and footer.
- Privacy policy that accurately describes what the site collects (default:
  hosting-provider server logs only; no analytics, no third-party trackers).
- SRI integrity attributes on all CDN tags. Use
  `tools_compute_sri.py` to recompute when bumping CDN versions.

## Editing rules

### Bumping CDN versions

When upgrading Bootstrap or FontAwesome:
1. Update the version number in the URL inside `_scripts/compute_sri.py`
   and in every HTML file that loads it.
2. Run `py _scripts/compute_sri.py` to compute new SHA-384 hashes.
3. Update the `integrity=` attribute in every page that loads it
   (currently: `index.html`, `research.html`, `responsible-disclosure.html`,
   `privacy.html`, `terms.html`, `404.html`).
4. Test locally (`py -m http.server 8000`) before pushing.

### `.nojekyll` and what gets served

The repo contains a `.nojekyll` file at the root. This disables GitHub
Pages' default Jekyll build and tells Pages to serve every file in the
repo as-is. **This is required** — without it, Jekyll's default rules
exclude dot-prefixed paths and `/.well-known/security.txt` returns 404.

A consequence: nothing in this repo is hidden from the public site.
`_scripts/compute_sri.py` is publicly accessible at
`https://www.sumosols.com/_scripts/compute_sri.py`. That file contains
no secrets — only a one-shot helper that fetches public CDN files and
prints their SHA-384 hashes — but be aware that anything committed to
this repo will be served. **Do not commit secrets, drafts, internal
notes, or anything you would not want indexed by search engines.**

### Updating legal pages

When updating `privacy.html` or `terms.html`, also bump the
"Last updated:" date at the top. Stale dates undermine the legal weight.

### Don't fabricate

Real content only. Do not invent client names, case studies, team
biographies, or specific metrics.
