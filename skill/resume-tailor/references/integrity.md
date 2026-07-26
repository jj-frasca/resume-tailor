# Integrity — the guarantee, and how to hold it for someone whose facts you can't verify

The promise is NOT "these facts are true" (you can't check a stranger's claims). The
promise you can keep is:

> **The tool adds nothing. Every claim on the resume traces to something the user
> supplied and explicitly attested to. Tailoring rewords and selects for the job but
> introduces no metric, employer, date, title, or skill the user did not give.**

That splits the risk in two:

## 1. Model-fabrication — you prevent this (the grounding gate)
Before finalizing, check every claim on the resume against the confirmed profile:
- Every employer, title, date, number, and named skill must appear in the profile.
- A bullet may reword or combine profile facts for the job, but may not introduce a fact
  that isn't there. If you can't point to the profile source for a claim, cut it.
- Job-driven wording is fine; job-driven *facts* are not. "The posting wants Kafka" is not
  a reason to add Kafka unless the profile already has it.

## 2. User-fabrication — you shift this on-record (attestation)
You cannot verify the user's own claims. So make them own them, explicitly:
- During onboarding, show each extracted fact (especially metrics, dates, employers,
  titles, skills) for confirm / edit / remove.
- Get one clear attestation before anything generates:
  *"Everything I kept is true and I can defend it in an interview."*
- Unconfirmed content cannot enter generation. This is the stranger-equivalent of a
  hand-verified corpus: not proof, but explicit, on-record responsibility.

## Confidence, honestly
Extracted content defaults to `self-reported`. Confirmation does not create a new confidence
tier — it sets a **user-attested flag** on the item (tracked via
`integrity_flags.user_attested` in the schema); the `confidence` value still reflects the
source. No `verified` confidence exists unless the user uploads a backing artifact. Don't
invent one.

## Honest-gap report (every generation)
When the job requires something the profile doesn't have, say so plainly and do not claim
it. Framing it as trust ("I did NOT add this — you don't have it on record") is a feature,
not a failure.

## Privacy
The profile and every generated resume are private personal data (name, contact, career
history). Keep them in this conversation with the user; never post them elsewhere, and let
the user delete them.
