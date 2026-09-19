# Sumo Solutions Website — Project Rules for Claude

This file is read at the start of every Claude Code session in this repository.
Rules here override default behavior. Add new rules below; do not delete existing
rules without discussion.

---

## Repo overview

Source for the public Sumo Solutions company website at
`https://www.sumosols.com/`, deployed via GitHub Pages.

Stack: static site, hand-written CSS in `assets/style.css`. No CSS
framework, no JavaScript on any page, no build step. The only external
request is IBM Plex Sans/Serif/Mono from Google Fonts. Edit HTML/CSS
directly and push; GitHub Pages serves on push.

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

Sumo Solutions is a **mobile-focused** engineering firm. Four service
lines, in this order:

1. Mobile App Development — the core of the business
2. AI-Enabled Mobile Apps — AI features built into those apps
3. Custom Software & Websites — web apps, sites, backends, admin tools
4. Mobile App Security Research — secondary, unchanged

Lines 1 and 2 are the target. Line 3 supports them (the site and admin
panel behind an app) and stands alone when a client needs only that.
Line 4 is secondary: keep it visible but never dominant.

**Cloud/DevOps and digital strategy are no longer service lines.** They
were removed to sharpen the mobile focus. The capability is still real,
so it survives as the "Also part of the work" note at the end of the
services section — hosting, deployment, and advice on what to build
come with an engagement rather than being sold separately. Do not
promote them back to rows without discussion.

### Writing about AI

The same no-buzzwords rule applies, and it is easiest to break here.
Name the actual feature — an assistant over your own content, semantic
search, transcription, summaries, recommendations — never "AI-powered
transformation" or "intelligent solutions". The site states that we
build on existing models rather than training our own; keep that claim
accurate if the capability changes.

### Who the site is written for

The clients are **founders and early-stage teams, creators and
influencers, and local/small businesses**. They are mostly
non-technical. The site is *not* pitched at companies that already have
an in-house engineering team.

This drives the copy: **lead every service with what the client gets in
plain language**, and keep the engineering specifics in the supporting
deliverables list. "We ship your app to the App Store and Play Store"
before "CI/CD pipelines". Do not reintroduce engineer-to-engineer
phrasing like "typed languages" or "tests that run" into body copy.

There is a second, quieter audience: vendor security contacts checking
whether a disclosure email from `research@sumosols.com` is genuine.
That is why the policy pages are written as documents with dates,
metadata, and cross-references. Do not casualise those pages.

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
- SRI integrity attributes on any CDN tag that can carry one. There are
  currently none: the site loads no third-party scripts or stylesheets
  apart from Google Fonts, which cannot be pinned with SRI because the
  stylesheet is generated per user-agent. If you add a CDN dependency,
  it must carry `integrity` — use `_scripts/compute_sri.py`.

## Editing rules

### Adding a CDN dependency

Prefer not to. The site is deliberately framework-free and the privacy
policy states there is no third-party JavaScript on any page. If you do
add one:
1. Put its full URL in `URLS` inside `_scripts/compute_sri.py`.
2. Run `py _scripts/compute_sri.py` to compute the SHA-384 hash.
3. Add `integrity=` and `crossorigin="anonymous"` in every page that
   loads it (all six: `index.html`, `research.html`,
   `responsible-disclosure.html`, `privacy.html`, `terms.html`,
   `404.html`).
4. Update section 5 of `privacy.html`, which enumerates every external
   request the site makes.
5. Test locally (`py -m http.server 8000`) before pushing.

### The design system

Colour and type tokens live at the top of `assets/style.css`; the table
in `README.md` summarises them. Two rules that matter:

- **Brass (`--brass` / `--brass-lt`) is reserved for the security-research
  line.** It marks the research row, the research cell in the hero index,
  disclosure callouts, and focus rings. Using it anywhere else destroys
  the distinction it carries.
- **Mono is for real identifiers only** — email addresses, file paths,
  domains, package names. Not for labels, headings, or captions.

The homepage layout is a "spine": a narrow left column naming the
section, a wide column of content. Keep new sections on that grid
(`.wrap.spine`) rather than centring headings.

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

### Do not describe research methodology publicly

`research.html` deliberately does **not** say how the security research
is carried out. No tooling, no analysis techniques, no categories of
finding. That detail told competitors the playbook and told vendors
what we look for, and it meant nothing to the non-technical readers the
rest of the site is written for.

The page answers only: what this is, what we will and won't do, what to
do if you got an email from us, and how to buy a review. Keep it that
way. The same applies to the homepage research row — its bullets
describe commitments, not techniques.

`responsible-disclosure.html` is the exception and stays detailed: it
is the formal RFC 9116 policy referenced from `security.txt`, and what
it describes is *process and ethics*, not method.

### The social share image

`assets/og.png` (1200x630) is what appears when the site is shared in
WhatsApp, LinkedIn, Slack, or iMessage. It repeats the homepage
headline and the four service lines, so **it goes stale whenever those
change.** Its source is `_scripts/og-card.html`; the re-export steps
are in a comment at the top of that file. Every page declares
`og:image:width`/`height`, so the export must stay exactly 1200x630.

### No generated or stock imagery

Do not add AI-generated illustrations, stock photography, or invented
app mockups. The site's credibility rests on looking verifiable —
generated imagery reads as filler and undercuts it, and a fake app
screenshot is a fabricated portfolio under the "Don't fabricate" rule
below. Real screenshots of shipped apps (with client permission) and
real photos of the team are welcome.

### Updating legal pages

When updating `privacy.html` or `terms.html`, also bump the
"Last updated:" date at the top. Stale dates undermine the legal weight.

### Don't fabricate

Real content only. Do not invent client names, case studies, team
biographies, or specific metrics.
