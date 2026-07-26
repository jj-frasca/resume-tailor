# Onboarding — extract the user's fact profile from easy inputs

Goal: fill the schema in `content-schema.md` from what the user gives you, asking as
little as possible. A current resume is the minimum; richer material tailors better.

Point the user to `corpus-guide.md` and invite more than one source: old resume versions,
a LinkedIn "Save to PDF", a brag doc / accomplishments list, performance reviews, project
READMEs. Merge each new source into the profile (adding it to the item's `sources`) and
only re-surface genuinely new conflicts. Never require more than a current resume, but ask
once whether they have any of the extras — more real material means a stronger resume.

## Extraction contract (the rule you follow while reading their documents)
You extract a structured career profile from the user's documents. You never invent,
infer, or inflate any fact, metric, employer, date, title, or skill not present in the
source. Missing means omit, never guess.

Per document, produce JSON matching the schema, and:
- **Identity/contact** — verbatim. If two documents disagree on name or handles, flag it.
  Keep phone/email as private data.
- **Roles** — employer, official title, dates. Set `is_current` instead of "Present". If a
  document shows a preferred title different from an official one, fill `title_override`;
  do not overwrite the official title.
- **Achievements** — split into atomic bullets. Tag `domains` from a small fixed set of
  tags you reuse across the profile. Set `confidence`: `resume-claimed` if on the resume,
  `self-reported` if only pasted or typed. Pull each number into `metrics` verbatim.
- **Skills / education** — extract only what's present.

## What to auto-detect and raise as questions (do not resolve silently)
Emit a `conflict` or `integrity_flag` when:
- Two sources give different values for the same fact (cross-source).
- One document is internally inconsistent — e.g., the same metric with two values.
- A number is large/impressive but unverifiable.
- An employer or date is ambiguous ("Present" with no end).
- A profile handle or name doesn't match across documents.
- A document reads like a **different person's resume** or an unmodified template — do NOT
  ingest its content; raise it as a flag.

Never pick a winner for a conflict yourself; leave `resolution` null until the user decides.

## The confirmation screen (the only place the user makes decisions)
Keep it short and tap-friendly:
1. Show confident items collapsed: "I read 14 details that look clean — want to see them?"
   with a single **Confirm all** affordance.
2. Show a short queue of only the flagged items, most-risky first, each as a small choice:
   - "Your 2023 summer job — which employer? [A] [B]"
   - "Still at this job? [Yes] [No]"
   - "Keep this skill? I found no backing for it. [Keep] [Drop]"
   - "I couldn't read your phone number: [ ____ ]"
   Aim for ~1–3 questions for a clean resume, near-zero typing.
3. Attestation checkbox (see `integrity.md`): "Everything I kept is true and I can defend
   it in an interview."

Only when no blocking conflict or flag remains, set `intake_complete = true`, save
`profile.json`, and offer it to the user to download for reuse.
