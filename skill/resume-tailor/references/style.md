# Resume style spec — exactly one page, ATS-safe, human-looking

The non-negotiable formatting contract for every generated resume. Derived from
established resume best practices (Harvard/Yale career guides, Jobscan ATS testing).

## Layout
- **Single column. No multi-column layouts, text boxes, sidebars, images, or icons.** This
  is the #1 ATS rule — multi-column/full-page-table layouts get parsed as word-salad and
  silently drop sections.
- **The one allowed table exception:** each entry's header row (company left / location
  right, title left / dates right) is a single-row, two-cell borderless table. This is
  linear text an ATS reads as "Company … Location," and it's the only reliable way to keep
  the dates/locations flush-right across every PDF renderer. Never use tables anywhere else
  (bullets, skills, body) — those stay plain `<ul>` / `<p>`.
- Contact info goes in the document **body**, never in the page header/footer (parsers
  often skip headers/footers).
- Black text on white. No color blocks. Hyperlink LinkedIn/GitHub inline.

## Typography
- Body font: Calibri or Arial (sans) or Garamond/Cambria (serif) — pick one, use throughout.
- Body size 10.5–11 pt (never below 10 pt). Name ~14–16 pt bold. Section headers ~11–12 pt bold.
- Line spacing 1.0–1.15; a little more space before section headers than between bullets.
- Margins 0.5"–0.75" all sides. If it won't fit one page, **cut content — never shrink font
  below 10 pt or margins below 0.5"**.

## Structure / order
1. Name (centered, bold) + one contact line: `City, ST | email | phone | linkedin | github`
2. **Summary line — default omit for early-career.** A summary that just restates the
   posting is wallpaper and costs a line a bullet would use better; let the lead bullet do
   the framing. Add one only if it conveys something no bullet can.
3. **Experience** (reverse-chronological) — most bullets on the most recent/relevant role.
4. **Projects** — the bridge to the target role; include only job-relevant ones.
5. **Technical Skills** — grouped, job-relevant subset (not a dump).
6. **Education** — below experience once there's industry experience; above it for new grads.
- Each entry: company bold left + location right; title italic left + dates right.

## Bullets
- **X-Y-Z formula:** "Accomplished [X] as measured by [Y] by doing [Z]." Lead with the
  outcome/metric, name the method.
- Start with a strong past-tense verb. No first-person pronouns. Never "responsible for" /
  "assisted with" / "helped."
- 3–4 bullets per role, fewer on older roles. Each ideally ≤2 lines.
- Quantify wherever real. Don't invent precision; "~30%" beats a fake "31.4%".

## File output
- Submit a text-based PDF (not scanned, not an image). Use .docx only if the posting
  explicitly requires Word. The real parse-killers are images/tables/columns, not the container.

## One-page enforcement (the skill must verify)
This layout holds roughly 38–45 body lines at 11 pt / 0.6" margins. After drafting, render
to PDF and confirm exactly one page before finishing. If over, cut the weakest job-
irrelevant bullets/skills rather than compressing formatting below the limits above.

## Fill the page — no big bottom gap, no orphan lines
One page means one *full* page. Under-filling looks as unfinished as overflowing.
- **Pack toward the bottom.** Aim to end near the bottom margin, not two-thirds down. If
  there's a gap, add another real, verified bullet or restore a relevant role/skill before
  reaching for spacing tweaks. Fill with substance first; use small line-spacing/margin
  nudges (within the 10 pt / 0.5" floors) only for the final sliver.
- **Kill orphan trailing lines.** A bullet whose last wrapped line holds only 1–4 words
  ("… latency.", "… the pipeline.") wastes a whole line's width. Densify that bullet with
  real scope/metric/mechanism from the profile so its last line runs closer to full width —
  never with filler, and never so much that it spills to a new near-empty line. Target each
  bullet's last line at roughly ≥70% of the text width.
- **Trade-off, honestly:** all packing uses only real, confirmed content. Do not stretch to
  fill a page by inventing or padding. A slightly shorter honest resume beats a full fake one.
