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
with `py --version` on Windows, or with `python3 --version` on macOS and Linux. **On Windows, use `py`**: `python` can
be a shortcut to the Microsoft Store that runs nothing and fails without saying anything.

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

### Five habits that make the difference

- **Tell it what doesn't go through the chat.** The base only knows what reaches it. Five minutes at the end of the week
  with the meetings and the hallway decisions are worth more than anything else.
- **Ask it to file the good answers.** A comparison or a cross-check that took you an afternoon is lost if it stays
  in the chat.
- **Let it disagree with you.** If Claude says a new fact contradicts a stored one, that's not a failure: it's the
  base working. Decide which one is right.
- **Look at the log now and then.** It's the quick way to know what has changed.
- **Keep what is on record apart from what is deduced.** Ask that, when analyzing or giving an opinion, the text
  tells three things apart: what is on record in a document, what Claude deduces and what it could not check. A
  deduction written with the confidence of a fact misleads. If it is an opinion on someone's work or a
  recommendation, have it close with **what the other side would say**, in two or three lines; and before a
  weighty decision, have it give **the opposite case with the same force**: if it convinces just as much, the
  decision is not ripe.

### A model for each task

Not all work needs the most capable model, which is also the slowest and the most expensive. In Claude Code you
switch models with `/model`, and you can delegate the searching to a subagent that uses another one.

| Work | Model |
|---|---|
| **Searching and locating** ("where is…?", gathering fragments) | The cheapest and fastest (Haiku), with a read-only subagent |
| **Drafting, registering and building** | The middle one (Sonnet) |
| **Analyzing, cross-checking, preparing decisions and reviewing what matters** before it goes out | The most capable (Opus) |
| **If in doubt** | The middle one |

The search subagent returns **paths and short quotes, not conclusions**: concluding is the job of the model that
asks it. And the cheap model **does not write to the base**: it keeps read-only tools. A minimal example, in
`.claude/agents/searcher.md`:

```
---
name: searcher
description: Searches and locates information in the base without changing anything. Use it for "where is...?" or to
  gather fragments from several documents before analyzing them. Returns paths, lines and short quotes, not conclusions.
tools: Read, Grep, Glob
model: haiku
---

Search the base for whatever you are asked. Change nothing. Answer with a list of file paths, the line number
and a short quote for each finding. If you find nothing, say so; do not fill in.
```

**Do not fix the model in the project's `.claude/settings.json`**: it is re-applied at every start and overrides
the one you pick by hand with `/model`. If a computer wants another default model, put it in
`.claude/settings.local.json`.

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
| `_calendar-annual.md` | "What is due this month?": what repeats, month by month (closings, renewals, mailings, key rotations) |
| `_queries/index.md` | The frequent questions, with the command that answers them |
| `health-check.md` | What to look at in the periodic check, written once |
| `_findings.md` | The cross-checks that already proved their value, so you don't rediscover them |
| `events.json` · `aliases.json` | The dates that aren't contract expiry dates, and the different names for the same thing |
| `recurring.json` | What repeats, how often, in which months, who does it and the link to its procedure; the annual calendar comes from it |

The views are generated by a Python script that Claude writes and runs. **They are never edited by hand**: you correct the
source document and regenerate them. The prompt is in [`prompts/03-growth.md`](prompts/03-growth.md).

**What repeats is written down at the moment it appears**, even if it is through an email: yearly closings,
renewals, monthly mailings and key rotations usually live in someone's memory. The `recurring.json` register only
says **when it is due**; how it is done stays in its document. If it has a fixed day, it also appears in the
expiry calendar.

### And when you run projects

Projects get **an area of their own**, `projects/`, with a page per project that says **who it is for and who pays
for it**. When a project starts to have files, it gets its own folder with two subfolders: `sources/`, for what comes
in, and `deliverables/`, for what you produce, **with the version in the name** (`-v1`, `-v2`) and a register of what
was sent and to whom. The originals folder stays for what does not belong to a project, such as contracts and invoices.
That way the project document does not end up in whichever area it resembles, and its files do not get mixed with the
invoices. The prompt is in [`prompts/06-projects.md`](prompts/06-projects.md).

Each page declares its **state** in the header —`active`, `on hold` or `closed`— and carries two fixed sections:
**"Status and next step"** at the top, in two lines, and **"Decisions"** at the bottom, a table with date, what was
decided, why and by whom, which **only grows**: a decision that changes is not deleted, the one that replaces it is
added. The catalog groups the projects by state and flags the ones without one. A closed project **does not move
folder**, because the links would break: the field is enough. And when a project outgrows a single page, the status
and the decisions become files of their own, `status.md` and `decisions.md`, next to the page, and the folder carries
its own working rules. **Only in that project**: a status repeated in three places ends up drifting out of sync.

> 💡 **Before a deliverable, ask for a sketch** and approve it: fixing an outline takes a minute; redoing a
> presentation, an afternoon.

### One folder per application

Whatever explains **how a business application is configured and how it is used** —rules, procedures,
configurations— goes in **a folder for that application**. The systems area keeps the infrastructure, the access,
the security and the integrations between systems. Why: systems ends up as the drawer for "everything that touches
a system" and nobody looks there for how a tool is used. The folders are opened when there are documents that call
for them, not in advance.

### And the regulation that is coming

If your work touches subjects that change —data protection, artificial intelligence— keep a document of
**regulation to watch**: the changes in the pipeline that could change what is allowed (for example, a European
proposal under negotiation), with what they say, what state they are in, what they affect and what is still
unknown. And a rule in `CLAUDE.md`: every time that subject comes up, Claude consults it and says what would change
the answer, **making clear that it is not law yet**. It is not legal advice: it is a reminder of what to look at
before deciding.

## 8. Make the rules enforce themselves

### The hooks

Claude Code lets you hook a script to moments in the session. Three are enough so that what always gets forgotten
doesn't get forgotten:

| When | What it does |
|---|---|
| **When each response ends** | Regenerates the views if needed, warns if there are changes not noted in the log (or, if you keep a handoff log, no entry for today), looks for passwords that slipped in and checks that no `.md` file is left empty |
| **Before writing a file** | Prevents editing the generated views by hand |
| **After each action that writes** | Compares the size of the `.md` and JSON files with the previous snapshot and warns at that moment if any has been emptied, has shrunk to less than half or has disappeared |

The prompt for Claude to set them up is in [`prompts/04-hooks-claude-code.md`](prompts/04-hooks-claude-code.md).
They are configured in `.claude\settings.local.json`, inside the folder itself, in this form:

```json
{
  "hooks": {
    "Stop": [
      { "hooks": [ { "type": "command",
                     "command": "cd \"C:/path/to/your/base\" && py _tools/session_close.py",
                     "timeout": 120 } ] }
    ],
    "PreToolUse": [
      { "matcher": "Write|Edit",
        "hooks": [ { "type": "command",
                     "command": "cd \"C:/path/to/your/base\" && py _tools/protect_views.py",
                     "timeout": 20 } ] }
    ],
    "PostToolUse": [
      { "matcher": "Bash|PowerShell|Write|Edit",
        "hooks": [ { "type": "command",
                     "command": "cd \"C:/path/to/your/base\" && py _tools/watch_sizes.py",
                     "timeout": 30 } ] }
    ]
  }
}
```

**On Windows, call the scripts with `py` and not with `python`** (on macOS and Linux, `python3`): `python` can be
the Microsoft Store shortcut, which runs nothing and fails without saying anything, and the hooks would go for
weeks without running without anyone noticing. You review them by typing `/hooks` in Claude Code, and **it is worth
running a real test**: empty a test `.md` file on purpose and check that the warning shows up.

### Writing without losing data

One rule for the base's scripts: **none of them opens a document for writing before it has read it**. In Python,
`open(path, "w")` empties the file the very instant it opens it; if the read fails afterwards, the file is left at
zero and nobody finds out. Changes in bulk go through a small utility, `_tools/safe.py`, that **reads first, writes in
one go to a temporary file and swaps it for the original**, and that **refuses to empty a file or to leave it at less
than half its size**. One-off changes, with the editing tool. And the third hook warns at that moment if something has
been emptied. The cloud's version history is still the safety net, but this way you do not have to use it.

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

The entry starts with the **next step**, written so that it can be done without asking; it goes on with what is in
progress (results, not activity), what is being waited on, the **assumptions and how they get confirmed**, the
documents touched and the warnings. **Each pending item carries its owner and its date**, if there is one.

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
| Projects ended up in whichever area they resembled, and their files mixed with the invoices | An area of their own for projects, and a folder per project with what comes in and what is delivered, with versions |
| An analysis took for granted what was only a deduction, and whoever read it took it as a fact | The text keeps apart what is on record, what is deduced and what could not be checked |
| A script opened an index for writing before reading it, emptied it and nobody noticed for a week; the cloud's version history saved it | Changes in bulk go through a utility that reads first and refuses to empty, and a hook warns at that moment |
| The hooks had not been running for weeks: they called `python`, which on that Windows was the store shortcut and failed without saying anything | Call them with `py` and check with `/hooks` that they really run |
| What repeats was in no calendar: the yearly closings and the monthly mailings lived in someone's memory | A register of what recurs and an annual calendar, month by month |
