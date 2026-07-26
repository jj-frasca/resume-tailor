# Anti-AI rules (enforced as a QA gate before finalizing)

AI-flagged resumes are a real rejection driver — many hiring managers screen for and
reject resumes that read as generated. Treat these as hard rules, not style suggestions.

## BANNED words/phrases (strike on sight — never output)
spearheaded, leveraged (as a verb), orchestrated (unless literally an orchestrator
system), passionate, dynamic, seamlessly, robust, comprehensive, cutting-edge,
state-of-the-art, results-driven, results-oriented, detail-oriented, proven track record,
synergy, holistic, myriad, plethora, realm, intricate, showcasing, pivotal, delve,
tapestry, testament, underscore, foster, embark, navigate (figurative), elevate, empower,
unlock, harness (figurative), revolutionize, transformative, meticulous, "in today's
fast-paced world," "not only ... but also," "a strong foundation in," "demonstrated
ability to."

## CAUTION (use at most once on the whole resume, and only carrying a real metric)
utilized→use, facilitated, streamlined, optimized, enhanced, implemented, developed,
designed, built — vary these rather than repeating them.

## Structural anti-patterns (the real giveaways)
- **Uniform bullets.** If every bullet is "[Verb] [thing] by [method], achieving [round %]"
  it reads as generated. Vary sentence shape, length, and where the metric lands — some
  bullets lead with the number, some end with it, some have none.
- **Round/symmetrical numbers.** "50%", "doubled", "10x" everywhere signals fabrication.
  Real metrics are asymmetric (62%, 8.75 TB→50 MB, 158 columns, ~30%). Keep the user's
  real, lumpy numbers exactly — never smooth or invent precision.
- **Em dash.** Not banned, but overuse is a tell (generated text uses it far above the
  human rate). Limit to about one per page; prefer commas and periods.
- **Tricolons everywhere** ("fast, scalable, and reliable"). One is fine; a pattern is not.
- **Verb monotony.** Don't open five bullets with "Built." Rotate concrete verbs (Built,
  Cut, Migrated, Shipped, Designed, Owned, Diagnosed, Automated, Reduced).
- **Adjective stacking / vague nouns** ("robust scalable solutions"). Replace vague verb +
  abstract noun with plain verb + real asymmetric number + named tool/system.

## The one principle
Replace "vague verb + abstract noun" with "plain verb + real asymmetric number + named
system/tool." A person's actual lumpy metrics and specific system names are the strongest
anti-AI signal — keep them concrete and specific.

## Keyword alignment (do this; don't stuff)
- Mirror the job's exact terminology where the user has real backing (if it says "Python,"
  write "Python," not "scripting"); spell out an acronym once ("Retrieval-Augmented
  Generation (RAG)").
- Target ~70–80% of the job's hard requirements represented by a real bullet or skill.
  Place keywords where they're earned, not in a keyword dump.
- **Alignment-vs-stuffing test:** if a human reader would find the sentence natural and
  true, it's alignment; if a keyword appears with no backing accomplishment, it's stuffing
  — cut it. Never claim a skill the user doesn't have to match a keyword; report the gap.

## Keyword ECHO vs alignment (a tell even with no banned word)
Mirroring the posting's phrasing back at them is a tell.
- **BAD (echo):** posting says "trace issues back to their source" → resume says "tracing
  data anomalies back to their upstream source." The posting, reworded and pointed back.
- **GOOD (alignment):** state the user's real, specific incident in their own concrete
  terms and let the keyword match be incidental.
- **Rule:** a specific true story beats a generic posting-shaped claim. If a bullet could
  be written by anyone who just read the posting, it's echo — make it specific or cut it.

## Survival-badge rule
"Primary on-call, resolved 500+ incidents" is a worthless survival badge — everyone goes
on-call. The value is the capability (anomaly → trace → root cause), shown via one specific
incident, not the rotation or the count. Write the reasoning, not the rotation.

## QA checklist (run before output)
1. Zero banned terms present.
2. At most one em dash per page; bullet structures vary; no verb repeated more than twice.
3. Numbers are the user's real asymmetric figures — no invented precision, no all-round numbers.
4. ~70–80% of hard requirements covered by real content; no unsupported keyword.
5. Reads like a specific person wrote it, not a template.
