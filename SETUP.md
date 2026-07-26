# Setup guide (no technical skills needed)

This takes about 3 minutes. You'll do it once. If you get stuck, the official Claude help
article on custom Skills is here:
https://support.claude.com/en/articles/12512198-creating-custom-skills

## Before you start
- You need a **Claude account** with **file creation** turned on (Settings → Features →
  enable code execution / file creation). This works on Free, Pro, and Max.
- You'll do everything at **https://claude.ai** in a web browser. No app to install.
- If your account doesn't offer the "Upload skill" option, you may need **Pro or Max** —
  everything else is identical.

## Step 1 — Download the skill file
1. Click this link: **[⬇ resume-tailor.zip](https://github.com/jj-frasca/resume-tailor/raw/master/dist/resume-tailor.zip)**.
   It downloads a file called `resume-tailor.zip` (usually to your Downloads folder).
   Don't unzip it — you upload the .zip as-is.

## Step 2 — Upload the skill to Claude
1. Go to **https://claude.ai** and sign in.
2. Click your **name/profile** (bottom-left) → **Settings**.
3. Open **Features** (on some accounts this is called **Capabilities**).
4. Find **Skills** and click **Upload skill** (or **Add skill**).
5. Choose the `resume-tailor.zip` file you downloaded. Claude will add it.
   - If it asks you to enable **file creation** / **code execution** first, turn that on
     and try again.

## Step 3 — Set up your resume profile (once)
1. Start a **new chat**.
2. Type: **"Help me set up my resume profile."**
3. When asked, **upload your current resume** (PDF or Word). If you don't have one, you can
   paste your details instead.
4. Claude will show what it read and ask you to confirm a few things (like which job title
   is right, or to fix anything it misread). Answer those.
5. It will ask you to confirm everything is true and something you could explain in an
   interview. Say yes. Your profile is now saved for reuse.

## Step 4 — Make a tailored resume (each job)
1. In a chat, paste the **job posting link** (or paste the job description text).
2. Say: **"Tailor my resume for this job."**
3. Claude will build a one-page resume, check it doesn't read like AI, and tell you which
   requirements you match and which you don't.
4. **Download the PDF** it gives you. Done.

## Optional: get a Google Doc copy too
If you connect **Google Drive** to Claude (Settings → Connectors), you can ask Claude to
save an editable copy of your resume to your Drive as a Google Doc. The **PDF is still the
polished, submit-ready version** — the Doc is just an editable draft, and its dates and
locations won't sit flush-right (Google drops that when importing). If you don't connect
Drive, you simply get the PDF (and an HTML copy), which is all most people need.

## Tips
- **Feed it more than your current resume for a better result.** Old resumes, your
  LinkedIn, a list of your wins, past performance reviews — the more real material, the
  better it can tailor. Just say "help me set up my resume profile" and add what you have.
- Be honest in Step 3. The tool deliberately won't add skills or numbers you don't have —
  if a job needs something you're missing, it tells you instead of faking it.
- To reuse your profile in a fresh chat, upload the `profile.json` file Claude gave you
  during setup, or just re-run "Help me set up my resume profile."
- If the upload button isn't there, make sure **file creation** is enabled in Settings →
  Features. If it still isn't offered on your plan, upgrading to **Pro or Max** unlocks it.

## If PDF download doesn't work
Rarely, Claude's environment can't build the PDF directly. If that happens, it will give
you the resume as a web page (HTML) file instead — open it in your browser and choose
**Print → Save as PDF** (paper size: Letter). Same result.
