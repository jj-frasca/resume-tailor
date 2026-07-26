# resume-tailor

A free, private helper that turns your resume + a job posting into a tailored, one-page,
ATS-safe PDF that reads like a real person wrote it — not AI. It uses **only the facts you
give it and confirm**; it never invents experience.

It runs inside [claude.ai](https://claude.ai) as a **custom Skill**, using **your own
Claude subscription**. There's nothing to install, no terminal, no account to create
beyond the Claude subscription you already have. You set it up once from this page.

## What you need
- A **Claude account** with **file creation / code execution** enabled (Settings →
  Features). This is available on Free, Pro, and Max plans.
- The ability to add a custom **Skill** in Settings. If your account doesn't show the
  Skills upload option, you may need to be on **Pro or Max** — the rest of the steps are
  the same.

## Set it up (about 3 minutes, no technical skills needed)
See **[SETUP.md](SETUP.md)** for step-by-step instructions with the exact clicks.
Short version:
1. Download the skill file: **[⬇ resume-tailor.zip](https://github.com/jj-frasca/resume-tailor/raw/master/dist/resume-tailor.zip)**
   (clicking it downloads the file directly).
2. In claude.ai, go to **Settings → Features** (or "Capabilities") → **Skills** →
   **Upload skill**, and pick the file you downloaded.
3. Start a new chat and say: *"Help me set up my resume profile."* Upload your current
   resume when asked, and confirm the details.
4. From then on, paste a job link (or the job text) and say *"tailor my resume for this,"*
   then download your one-page PDF.

## What it does
- **Onboards you once:** reads your uploaded resume, asks you to confirm a few things, and
  saves a private profile of your real facts.
- **Tailors per job:** picks and rewords your real experience to match the posting, keeps
  it to one page, runs an anti-AI-writing check, and reports honestly which requirements
  you cover and which you don't.
- **Stays honest:** it will tell you when a job wants something you don't have rather than
  making it up. That's the point.

## Privacy
Your resume and career details stay in your own Claude account and the chat. This project
ships no personal data. Nothing is sent to the author of this tool.

## For power users
The same logic can run in Claude Code as a plugin with a heavier ATS-scoring suite. That
path needs a terminal and isn't covered here. This repo targets the zero-setup claude.ai path.
