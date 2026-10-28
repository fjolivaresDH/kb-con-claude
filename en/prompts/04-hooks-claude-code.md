# Hooks prompt · Claude Code

So that Claude Code enforces the rules that get forgotten most: regenerating the views, warning about changes not noted down, not editing generated files by hand and not losing data when writing. **Paste it after the growth prompt (03)**, which is the one that creates the views.

```
I want Claude Code, not my memory, to enforce the rules that get forgotten most.

Create in _tools/ three Python scripts for the hooks and one utility:

1. session_close.py, which runs at the end of each response and:
   - regenerates the views if there are documents newer than _catalog.md;
   - warns if documents have been touched after the last entry in log.md;
   - looks for patterns of passwords, keys or tokens in what was just written;
   - checks that no .md file is left empty;
   - if handoff.md exists, warns when documents have been touched today and it has no entry for today.
   It should only speak when there is something to say, returning a JSON with "systemMessage".

2. protect_views.py, which DENIES editing by hand any of the generated views
   (_catalog.md, _pending.md, _calendar.md, _calendar-annual.md, _crosschecks.md, _entities.md)
   and explains why: you correct the source document and regenerate.

3. watch_sizes.py, which runs after each action that writes and compares the size of
   all the .md files and of the JSON files in _data/ with the previous snapshot (keep it in a separate
   file, inside the folder). If any of them has been emptied, has shrunk to less than half or has
   disappeared, it warns at that very moment, with the file name, returning a "systemMessage". If it
   warns, stop and restore before going on.

4. safe.py, a utility that is NOT a hook. No script writes a document with open(path, "w"):
   that empties the file the instant it is opened, and if the read fails afterwards, it is left at
   zero. safe.py offers three functions: replace a text, insert after a line and write a whole file.
   All three READ first, write in one go to a temporary file and swap it for the original, and they
   REFUSE to empty a file or to leave it at less than half its size. Changes in bulk are made with it;
   one-off changes, with the editing tool.

Hook the three hooks up in .claude/settings.local.json: the first on the Stop event, the second on
PreToolUse with matcher "Write|Edit" and the third on PostToolUse with matcher
"Bash|PowerShell|Write|Edit". Call the scripts with "py" and not with "python": on Windows, "python"
can be the Microsoft Store shortcut, which runs nothing and fails without saying anything (on
macOS and Linux, "python3"). Write down in the conventions what each one does and that the hooks
enforce the rules but don't replace them. Then check with /hooks that they are registered and
run a real test: with a test .md file, empty it on purpose and confirm that the warning shows up;
then delete it.
```
