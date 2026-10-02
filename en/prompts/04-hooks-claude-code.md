# Hooks prompt · Claude Code

So that Claude Code enforces the rules that get forgotten most: regenerating the views, warning about changes not noted down and not editing generated files by hand. **Paste it after the growth prompt (03)**, which is the one that creates the views.

```
I want Claude Code, not my memory, to enforce the rules that get forgotten most.

Create two Python scripts in _tools/:

1. session_close.py, which runs at the end of each response and:
   - regenerates the views if there are documents newer than _catalog.md;
   - warns if documents have been touched after the last entry in log.md;
   - looks for patterns of passwords, keys or tokens in what was just written;
   - if handoff.md exists, warns when documents have been touched today and it has no entry for today.
   It should only speak when there is something to say, returning a JSON with "systemMessage".

2. protect_views.py, which DENIES editing by hand any of the generated views
   (_catalog.md, _pending.md, _calendar.md, _crosschecks.md, _entities.md) and explains why:
   you correct the source document and regenerate.

Hook them up in .claude/settings.local.json: the first on the Stop event and the second on
PreToolUse with matcher "Write|Edit". Write down in the conventions what each one does and that
the hooks enforce the rules but don't replace them. Then tell me how to check it with /hooks.
```
