---
name: resume-tailor
description: Build a tailored, one-page, ATS-safe resume from a job posting, using only facts the user confirms; never invents experience. Use to build, tailor, or set up a resume for a specific job.
---

# resume-tailor

Build ONE tailored, one-page resume for a specific job, using only facts the user
has supplied and confirmed. Be methodical; follow every step. The user runs this in
a chat with file upload and code execution — there is no terminal and no local repo.

There are two phases. **Onboarding** happens once (build the user's fact profile).
**Tailoring** happens every job. Detect which is needed: if no confirmed profile
exists in this conversation (or the user hasn't uploaded one), run Onboarding first.
If the user uploaded a saved `profile.json` from a previous setup, parse it into the
schema (`references/content-schema.md`) and use it directly — don't make them re-onboard.

## Golden rule (read `references/integrity.md` and never break it)
The resume may contain ONLY facts the user supplied and attested to. You reword and
select for the job; you never add a metric, employer, date, title, or skill the user
did not give you. When the job needs something the user lacks, report the gap — never
fill it. This is the whole point of the tool.

---

## PHASE 1 — Onboarding (first time only)

Goal: turn what the user can easily give you into a structured, confirmed fact profile.

1. **Collect inputs.** Ask the user to upload their current resume (PDF or Word). Then
   invite richer material per `references/corpus-guide.md` — old resume versions, a
   LinkedIn "Save to PDF", a brag doc, performance reviews, project READMEs. More real
   material tailors better, but never require more than a current resume. Don't ask them
   to fill a form.
2. **Extract.** Follow `references/onboarding.md` to extract identity/contact, roles
   (employer, title, dates), achievement bullets, skills, education — each tagged with a
   confidence level and its source. Extract every number verbatim; never round or invent.
3. **Surface conflicts, don't resolve them.** When two sources disagree, a metric looks
   unverifiable, an end date is missing ("Present"), or a document looks like a different
   person's, raise it as a short question with 2–3 choices. Ask only about material items.
4. **Confirm + attest.** Show what you read (confident items collapsed as "does this look
   right?"), ask the user to fix flagged items, then get one explicit attestation:
   *"Everything here is true and I can defend it in an interview."* Nothing generates
   until this is done. See `references/integrity.md`.
5. **Save the profile.** Write the confirmed profile to a file (`profile.json` per the
   schema in `references/content-schema.md`) and offer it back to the user to download,
   so they can re-upload it next time instead of re-onboarding. Treat it as private data.

---

## PHASE 2 — Tailor a resume (every job)

### Step 1 — Ingest the job
- If given a URL, try to fetch it. If that isn't available or it needs a login, ask the
  user to paste the job text.
- Write down: exact **job title**, **company**, **seniority/level**, **years required**,
  **must-have** skills/tech (verbatim), **nice-to-haves**, **domain**, and the **role
  archetype** (see `references/role-playbooks.md`: FDE / AI Engineer / Data Engineer /
  Trading-firm DE / SWE / Quant / Aerospace / or closest fit).

### Step 2 — Level & fit check (before writing)
- If the job is Senior/Staff/Principal or wants more years than the user has, warn them
  plainly (under-leveled candidates are often auto-filtered) and ask whether to proceed
  or find a better-leveled posting.
- Note any hard requirement the user genuinely lacks. Plan to report it; never fabricate.

### Step 3 — Select content
- Load the matching archetype block from `references/role-playbooks.md` and apply its
  weighting. These are strategy patterns, not facts — the facts come only from the profile.
- From the profile, choose: an optional positioning line, the strongest 3–5 bullets on the
  most relevant role, other relevant roles, job-relevant projects (with links where the
  user provided them), and a job-relevant skills subset. Prefer higher-confidence bullets.
- Rank candidate bullets by overlap with the job's must-haves; keep the highest-signal
  ones that fit one page.

### Step 4 — Write the bullets (alignment + anti-AI)
- Mirror the job's exact terminology naturally where the user has real backing for it;
  aim for ~70–80% of hard requirements mapped to a real bullet or skill. Do not stuff.
- Use the X-Y-Z shape (outcome as measured by Y by doing Z), strong past-tense verbs,
  lead with the real outcome/metric. Keep the user's real, asymmetric numbers.
- Run the full gate in `references/anti-ai-rules.md`: zero banned words; varied bullet
  structure and verbs; at most one em dash per page; no all-round numbers; no keyword
  echo; reads like a specific person.

### Step 5 — Assemble and enforce ONE PAGE
- Order per `references/style.md`: Name + contact line → (optional summary) → Experience
  → Projects → Technical Skills → Education.
- Fill `templates/resume-template.html` with the selected content (single column; the only
  tables are the borderless entry-header rows, per the template comments). Build the contact
  line and links from only the fields the profile has — never emit an empty `href`.
- Render to a **one-page, text-based PDF** and verify it is exactly one page BEFORE
  finishing (see `references/style.md` "One-page enforcement" and the render step below).
  If it overflows, cut the weakest job-irrelevant bullets/skills — never shrink font
  below 10pt or margins below 0.5in, and never go to two pages.

#### Rendering the PDF in this environment
Use the helper, resolving its path from THIS skill's own directory (the folder containing
`SKILL.md`), not the current working directory:
`python <skill-dir>/scripts/render_pdf.py <filled.html> <out.pdf>`.
It must print `PAGES: 1` (exit 0) before you treat the PDF as done. Any other result means
NOT done: more than one page or an unverified page count (exit 2) → cut the weakest content
and re-render; no PDF library available (exit 3) → run `pip install xhtml2pdf pypdf` (this
sandbox can reach PyPI by default) and re-run the script; if that install is blocked (no
network), either produce the one-page PDF with your own built-in file-creation from the
filled HTML, or fall back to delivering the polished one-page HTML for the user to open and
Print → Save as PDF (Letter); input-not-found (exit 1) → check the path. Whichever path you
use, still confirm the result is exactly one page. Never claim a one-page PDF you did not verify.

### Step 6 — Report honestly
Give the user a short summary:
- Which archetype you used and how you weighted the resume.
- Job must-haves covered vs. genuine gaps, stated plainly ("the role asks for Kubernetes;
  you don't have it on record, so I did NOT add it").
- Any flags (level mismatch, a claimed skill worth double-checking).
- The downloadable PDF (and the editable source).

### Step 7 — Optional: save to Google Drive as a Doc
If, and only if, the user has connected Google Drive to their Claude account, offer to
save an editable copy as a Google Doc. Follow `references/google-docs.md`, and tell the
user the honest limitation: the Doc won't keep the flush-right dates/locations (Google
drops that on import), so the PDF stays the polished, submit-ready artifact and the Doc is
an editable draft. If Drive isn't connected, or Doc creation isn't supported by their
connector or fails, skip it and just deliver the PDF/HTML — never block on this step.

## Never
- Never add a fact not in the confirmed profile. Never produce a two-page resume.
- Never keyword-stuff to raise a match score; treat any ATS/keyword score as a hint only.
- Treat the profile and every generated resume as private data — they contain contact
  info. Don't paste them anywhere beyond this conversation with the user.
