# Optional: save the finished resume to the user's Google Drive as a Doc

Offer this only AFTER a resume is generated, and only as a convenience. The one-page PDF
is always the primary, highest-fidelity artifact. A Google Doc is an editable copy. If Doc
creation isn't supported by the user's connector or it fails, don't block — just hand them
the HTML copy and move on.

## When it's possible
Only if the user has connected **Google Drive** to their Claude account (claude.ai
Settings → Connectors). If Drive isn't connected, don't attempt it — just say the PDF/HTML
is the deliverable, and point them to connect Drive if they want the Doc option next time.

## How to offer it
After delivering the PDF, ask: "Want an editable copy saved to your Google Drive as a
Doc?" If yes and Drive is connected, create a Google Doc in their Drive from the resume
content.

## Honest formatting limitation (state this to the user)
A Doc created this way will be clean and ATS-safe, but it **will not keep the flush-right
dates/locations** — when content is imported into Google Docs this way, Google ignores the
CSS that right-aligns them, and the API path that would force it (computed spacing / tab
handling) isn't available through the Drive connector. So:
- **The PDF is the polished, submit-ready artifact** (right-aligned headers, exact one page).
- **The Doc is an editable draft** — dates/locations sit inline rather than flush right,
  and the user may need to nudge margins/spacing. Tell them this up front so they aren't
  surprised.

## What to put in the Doc
Use simple, import-friendly HTML: centered bold name; a plain contact line; bold section
headers with a bottom border; **real `<b>`/`<i>` tags** (not CSS classes, which Google
drops on import); plain `<ul><li>` bullets (never style the `<ul>` — it breaks the Doc's
bullet indent); inline `<a>` links. Keep it one screen of content so it stays one page.
