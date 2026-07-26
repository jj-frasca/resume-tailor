# Content schema — the user's confirmed fact profile

The profile is the ONLY source of resume facts. Store it as `profile.json`. Every claim
carries a confidence level and the source it came from, so the generator never has to
guess and can prefer better-backed facts.

## Confidence levels
- `verified` — backed by an artifact the user uploaded (offer letter, transcript, work
  record). Only reachable if the user chooses to upload such an artifact.
- `resume-claimed` — stated on the user's own resume; self-asserted.
- `self-reported` — the user only typed or pasted it; least verified.

In self-serve use most facts are `resume-claimed` or `self-reported`. There is no
automatic `verified`. Do not fake a higher level than the source supports.

## Sources
`resume_pdf`, `linkedin_export`, `pasted_text`, `typed_answer`, `uploaded_artifact`.

## Shape (JSON)
```json
{
  "identity": {
    "full_name": "", "location": "", "email": "", "phone": "",
    "links": { "linkedin": "", "github": "", "portfolio": "" }
  },
  "roles": [
    { "id": "", "employer": "", "title": "", "title_override": "",
      "start": "YYYY-MM", "end": "YYYY-MM", "is_current": false,
      "location": "", "confidence": "resume-claimed", "sources": ["resume_pdf"] }
  ],
  "achievements": [
    { "id": "", "role_id": "", "text": "",
      "domains": ["#data-eng", "#ai", "#backend"],
      "metrics": ["62%", "3000+ users"],
      "confidence": "resume-claimed", "sources": ["resume_pdf"],
      "defense_notes": "what this actually means, so it is never overclaimed",
      "scope_guard": "e.g. owned N, not the larger M — do not conflate" }
  ],
  "projects": [
    { "id": "", "name": "", "summary": "", "link": "", "date": "",
      "tech": ["Python", "DuckDB"],
      "domains": [], "confidence": "self-reported", "sources": ["typed_answer"],
      "safe_framing": "the approved one-line claim",
      "banned_framings": ["claims the user cannot defend"] }
  ],
  "education": [
    { "school": "", "degree": "", "start": "", "end": "",
      "honors": "", "confidence": "resume-claimed", "sources": ["resume_pdf"] }
  ],
  "skills": { "Languages": [], "Frameworks": [], "Data": [], "Cloud": [] },
  "conflicts": [
    { "id": "", "item": "", "version_a": "", "version_b": "",
      "kind": "cross-source|internal|high-risk-unverifiable",
      "resolution": null, "resolved": false }
  ],
  "integrity_flags": [
    { "claim_ref": "", "reason": "", "action": "surface_once|drop|keep_with_attestation",
      "user_attested": false }
  ],
  "banned_claims": [
    { "pattern": "an employer never worked at / a skill with no backing", "reason": "" }
  ],
  "intake_complete": false
}
```

Notes:
- `title` vs `title_override`: keep BOTH. If the user prefers a variant title, store it in
  `title_override`; never silently overwrite the official one.
- `is_current` replaces an ambiguous "Present".
- `intake_complete` is true only once every blocking conflict and integrity flag is resolved.
- Re-runs: a later upload merges as a new `source` on existing items and only re-surfaces
  genuinely new conflicts.
