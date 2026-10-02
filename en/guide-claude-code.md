# Build your knowledge base with Claude Code

*A practical guide, from an empty folder to a base that maintains itself.*

> **Who it is for.** For anyone who wants to keep their working knowledge —suppliers, contracts, access details,
> decisions, procedures, pending items— in a folder of text files that **Claude Code** organizes, cross-checks and
> keeps up to date. You don't need to know how to code: almost everything is done by talking to Claude. You only need
> to install a couple of things at the start.

## Contents

1. [What you will build](#1-what-you-will-build)
2. [Before you start](#2-before-you-start)
3. [Install Claude Code](#3-install-claude-code)
4. [Create the folder and start](#4-create-the-folder-and-start)
5. [The initial prompt](#5-the-initial-prompt)
6. [Day to day](#6-day-to-day)
7. [When it grows: the views and the utilities](#7-when-it-grows-the-views-and-the-utilities)
8. [Make the rules enforce themselves](#8-make-the-rules-enforce-themselves)
9. [If you work from more than one computer](#9-if-you-work-from-more-than-one-computer)
10. [Security and privacy](#10-security-and-privacy)
11. [What we learned by breaking it](#11-what-we-learned-by-breaking-it)

---

## 1. What you will build

A **folder of Markdown documents** —text files with a little formatting— organized by area, where Claude Code stores
what you tell it: a loose fact in the chat, an email you paste, a screenshot, a PDF. Each thing ends up in its place,
with its date and linked to whatever it relates to.

The difference from an ordinary folder of documents is that **Claude doesn't just store things**: when a fact affects
several documents it updates all of them, when something contradicts what was already there it warns you, and over
time the base learns to tell you what you have pending, what expires soon and what doesn't match between two documents.

### Three principles

1. **Capture it when it happens.** Whatever isn't written down at the time gets lost. That's why you tell Claude in the
   chat, with no forms.
2. **Every fact carries its date and its proof.** With a fact without a date, you can't tell whether it is out of date.
   A fact without a source can't be checked.
3. **A single source, with an owner.** Each thing lives in one document; the others link to it instead of copying it.

### What it is not

- It doesn't replace your company's systems: accounting stays in accounting and passwords stay in the password
  manager.
- It is not a place for sensitive personal data or for information that must not leave your computer: whatever you give
  Claude is processed on Anthropic's servers.

## 2. Before you start

| What you need | What for |
|---|---|
| **A Claude account** with access to Claude Code (Pro, Max, Team or Enterprise plan) | It's what you work with |
| **Windows, macOS or Linux** | The examples in this guide are for Windows with PowerShell; on macOS and Linux you use the terminal |
| **A folder on your computer** | Where the base lives. *Optional:* inside a synced cloud (OneDrive, Google Drive, Dropbox…) to get backups and version history — see step 4 |
| **Python 3** | Only from step 7 onwards, for the utilities that regenerate the views |

> **You don't need Git**, or to know how to code. Claude Code writes the scripts itself when the time comes.

> **Do you already have the Claude desktop app installed?** Then **you can skip almost all of step 3 and the
> PowerShell part of step 4**: the app includes Claude Code in its **Code** tab. Open the app, go to **Code**, choose
> your base's folder and start talking to it. **The only thing you still need is Python**, and not until step 7. And
> one more detail: the **scheduled tasks** in step 8 live in the desktop app, so it will come in handy anyway.

## 3. Install Claude Code

> If you already have the Claude desktop app, **skip this step** except for the Python section at the end.

Open **PowerShell as your own user**, without "Run as administrator". If you install it as administrator, it is
installed in the administrator's profile and your user can't find it.

```powershell
irm https://claude.ai/install.ps1 | iex
```

On macOS or Linux, from the terminal:

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

Close PowerShell, open it again and check that it responds:

```powershell
claude --version
```

### If it says it doesn't recognize "claude"

The installer puts it in `%USERPROFILE%\.local\bin`. If that isn't in the PATH, add it for your user and open
PowerShell again:

```powershell
[Environment]::SetEnvironmentVariable("Path", [Environment]::GetEnvironmentVariable("Path","User") + ";$env:USERPROFILE\.local\bin", "User")
```

If it still can't find it, **sign out of Windows and sign back in**: File Explorer keeps the old PATH until then.

### Python, for later

Download it from **python.org** and, on the first screen of the installer, tick **"Add python.exe to PATH"**. Check it
with `python --version`.

## 4. Create the folder and start

1. Create an **empty folder**, for example `Knowledge`.
2. *(Optional)* If you put it inside a synced cloud, set it to be **always downloaded on the
   computer**: in "on demand" mode the files are only placeholders and Claude can't
   read them. In OneDrive, for example, it's right-click → "Always keep on this device".
   If you don't use a cloud, make a copy of the folder from time to time.
3. In PowerShell (or in the terminal), go into the folder and start Claude Code:

```powershell
cd "C:\Users\your.user\Documents\Knowledge"
claude
```

The first time it will ask whether you trust the folder: say yes. You can now talk to it.

**With the desktop app**, steps 1 and 2 are the same; instead of step 3, open the app, go to the
**Code** tab and choose the folder.

## 5. The initial prompt

It is a single message: first it asks what you are going to keep, then creates only that. It is in
[`prompts/02-initial-claude-code.md`](prompts/02-initial-claude-code.md). Before you paste it, replace `[ORGANIZATION]` (and, if you want, `[AREAS]`):

- `[ORGANIZATION]` → the name of your company, team or project.
- `[AREAS]` → the areas you want, separated by commas. For example: `suppliers, systems, budgets, people`.
  **It is optional**: if you leave it as is, Claude proposes them based on what you choose.

The first thing it does is **offer you the [examples already worked through](use-cases.md) and ask which ones fit you and
what other topics you want to keep**: the base is yours and it builds only what you choose. And **adapt it freely**: if you are missing a register of meetings or
of incidents, add it. The right structure is the one that reflects your day to day.

### What it creates

| File or folder | What it is |
|---|---|
| `CLAUDE.md` | **The rules Claude reads when it opens each session.** It is the most important file: whatever isn't here gets forgotten |
| `CONVENTIONS.md` | The formatting rules: file names, document types, dates |
| `index.md` | The map of the base, plus one more in each folder |
| `log.md` | One line per change, grouped by day |
| `_templates/` | One template per document type |
| `_documents/` | The inbox where you drop the PDFs to be processed (and, if you ask for it, the [archive of the originals](guide-cowork.md#optional--keep-the-original-documents)) |
| `_data/` | Only if you choose contracts or invoices: also in JSON, so you can filter and add them up |
| One folder per area | Each with its own `index.md` |

> **Review the `CLAUDE.md` it generates.** It must import the index and the conventions with two lines, `@index.md` and
> `@CONVENTIONS.md`, so that Claude always has them in front of it. And if one day you tell it "from now on, always do
> this", ask it to **write it in `CLAUDE.md`**: its memory lives on your computer, the file travels with the folder.

## 6. Day to day

You work by talking. These are the ways to add things and to ask:

| You want to… | How |
|---|---|
| Add a fact | Tell it in one sentence: "support for X is now handled by So-and-so" |
| Add an email or a text | Paste it as is and say what it's about |
| Add a document | Type `@` and the file path: `@"C:\Downloads\contract.pdf"` |
| Add a screenshot | Paste it into the chat |
| Ask | "What expires in the next six months?", "who handles X?", "what do I have pending on Y?" |
| Keep an answer that took work | "File it" |
| Correct something | "That's not right: it's this". It corrects it wherever it is |

### Four habits that make the difference

- **Tell it what doesn't go through the chat.** The base only knows what reaches it. Five minutes at the end of the week
  with the meetings and the hallway decisions are worth more than anything else.
- **Ask it to file the good answers.** A comparison or a cross-check that took you an afternoon is lost if it stays
  in the chat.
- **Let it disagree with you.** If Claude says a new fact contradicts a stored one, that's not a failure: it's the
  base working. Decide which one is right.
- **Look at the log now and then.** It's the quick way to know what has changed.

## 7. When it grows: the views and the utilities

**Do it weeks later, not on day one.** A utility that summarizes something needs something to summarize, and the
rules that detect mismatches are written against real mismatches: made up, they either never warn or warn about everything.

### Signs that it's time

- To answer an easy question you have to open three files.
- You ask the same question for the third time.
- The first mismatch between two documents appears.
- You've been at it for a month, or you have 25-30 documents.

### What it adds

| Adds | What for |
|---|---|
| `_catalog.md` | "Which document talks about this?" |
| `_pending.md` | "What do I have open?", with file and line, and whatever has a date at the top |
| `_calendar.md` | "What expires soon?" |
| `_crosschecks.md` | "What doesn't match?": what is in one document and missing from another |
| `_entities.md` | "Where else does this email, this tax ID or this domain appear?" |
| `_queries/index.md` | The frequent questions, with the command that answers them |
| `health-check.md` | What to look at in the periodic check, written once |
| `_findings.md` | The cross-checks that already proved their value, so you don't rediscover them |
| `events.json` · `aliases.json` | The dates that aren't contract expiry dates, and the different names for the same thing |

The views are generated by a Python script that Claude writes and runs. **They are never edited by hand**: you correct the
source document and regenerate them. The prompt is in [`prompts/03-growth.md`](prompts/03-growth.md).

## 8. Make the rules enforce themselves

### The hooks

Claude Code lets you hook a script to moments in the session. Two are enough so that what always gets forgotten
doesn't get forgotten:

| When | What it does |
|---|---|
| **When each response ends** | Regenerates the views if needed, warns if there are changes not noted in the log (or, if you keep a handoff log, no entry for today) and looks for passwords that slipped in |
| **Before writing a file** | Prevents editing the generated views by hand |

The prompt for Claude to set them up is in [`prompts/04-hooks-claude-code.md`](prompts/04-hooks-claude-code.md).
They are configured in `.claude\settings.local.json`, inside the folder itself, in this form:

```json
{
  "hooks": {
    "Stop": [
      { "hooks": [ { "type": "command",
                     "command": "cd \"C:/path/to/your/base\" && python _tools/session_close.py",
                     "timeout": 120 } ] }
    ],
    "PreToolUse": [
      { "matcher": "Write|Edit",
        "hooks": [ { "type": "command",
                     "command": "cd \"C:/path/to/your/base\" && python _tools/protect_views.py",
                     "timeout": 20 } ] }
    ]
  }
}
```

You review them by typing `/hooks` in Claude Code.

### The scheduled tasks

In the Claude desktop app you can schedule tasks. The one that pays off most is **regenerating the views
every night and warning only if there is something new**. Always end the instruction with "if there is nothing, do nothing":
otherwise it ends up being noise.

## 9. If you work from more than one computer

If the folder is in a synced cloud, it travels between computers on its own, but **the conversation doesn't**: on the other computer you won't know which step each
topic was left at. Claude's memory and the scheduled tasks don't travel either.

| Doesn't travel | What to do |
|---|---|
| The conversations | A **handoff log**: `handoff.md`, one entry per session with where each topic was left |
| What Claude has learned about you | Move it into `CLAUDE.md`, which does travel |
| The scheduled tasks | Keep them **on a single computer**: if two of them regenerate the same thing, syncing creates conflict copies |

And one rule: **never two sessions open at the same time on two computers.** If both write the same file at almost the
same time, the sync service keeps one and creates another with the computer's name attached. The handoff log prompt is in
[`prompts/05-handoff.md`](prompts/05-handoff.md).

## 10. Security and privacy

- **Passwords, keys and tokens: never in the base.** They go in the password manager. The base can say where they are,
  not what they are.
- **Sensitive personal data: no.** No health data, no people's identity documents, no bank accounts, no
  assessments of people. Professional contact details, yes.
- **Whatever you paste into Claude leaves your computer.** If your company has a policy on AI use, follow it: there is
  information that must not be pasted.
- **Read what Claude asks to run before you accept it.** Claude Code asks for permission to run commands; don't approve
  them blindly.
- **If you use a cloud with version history**, whatever breaks can be recovered. But for that very reason, whatever must not
  remain anywhere must never be written in the folder: even if you delete it, it stays in the history.

> **If you need to keep something confidential**, you can ask Claude for a `_private/` folder with files encrypted with
> 7-Zip and a visible note that only says they exist. You type the password yourself in the terminal: **never give it to
> Claude in the chat**.

## 11. What we learned by breaking it

Real failures in a base like this one. None of them raised an error: they all showed up when someone went to look.

| What happened | How to avoid it |
|---|---|
| A red "expires in 3 days" warning was for something that renewed automatically, and people stopped looking at the warnings | Before marking something as urgent, check whether it renews automatically |
| "What expires in six months?" gave one result; there were ten more in another document that wasn't referenced | Documents that answer the same question reference each other |
| The originals in the Downloads folder disappeared | Whatever matters is filed in `_documents/` |
| A problem that was reviewed and ruled out kept coming back every month | Whatever is ruled out is written down with its date |
| An afternoon's analysis was nowhere to be found three months later | Whatever is answered in the chat and is worth it gets filed |
| The month's summary came out sorted by what was documented, not by what was worked on | Tell Claude what doesn't go through the chat |
| The antivirus took away an archived CSV | Tables are archived as `.xlsx` or in Markdown |
| The "what expires" list was full of dates that weren't deadlines | Tell apart the date of a fact from the date of a deadline |
| A conflict copy of the log appeared | Only one session open at a time |
| The sensitive rules lived in the memory of a single computer | Whatever can't fail goes in `CLAUDE.md` |
