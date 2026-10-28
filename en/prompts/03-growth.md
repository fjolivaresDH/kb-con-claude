# Growth prompt

**Weeks later**, on the base you already have: it adds the generated views, the cross-check rules and the queries. It works in Cowork and in Claude Code. Why you don't paste it on day one: [Cowork guide, part 3](../guide-cowork.md#part-3--the-growth-prompt-once-you-have-content).

```
The knowledge base already has content and it's getting big for me: to answer a
question I have to open several files. I want to add the tools that solve that.

Before you write anything, READ what is already there and tell me what you find. Don't make up generic rules:
I want them to come from MY documents.

1. GENERATED VIEWS. Write a Python script, in _tools/regenerate.py, that regenerates all of them at once,
   and create them:
   - _catalog.md     -> every document with its type, title and description, taken from the
                        frontmatter. It answers "which document talks about this".
   - _pending.md     -> every line marked as pending or warning, WITH FILE AND LINE.
                        It is fed by the markers I write (⚠️, 🚨, "- [ ]",
                        "pending", "to confirm") and an item is closed by marking the line with ✅
                        or "resolved". Start it with "what has a date", sorted by
                        proximity: that includes every future date that appears in the line, and
                        a past date only if the text talks about a deadline (before, expires,
                        lapses). Careful: most dates in the base are stamps of
                        "fact as of such a day" and are NOT deadlines; if you let them in, the view is
                        useless.
   - _calendar.md    -> expiry dates and key dates sorted by proximity.
   - _crosschecks.md -> the mismatches. See point 2.
   - _entities.md    -> identifiers (emails, tax IDs, domains) that appear in 2 or more
                        documents, with where they appear.
   - _calendar-annual.md -> what repeats (yearly closings, renewals, monthly mailings, key
                        rotations), month by month. It comes from _data/recurring.json (see
                        point 7).

2. CROSS-CHECK RULES. This is the important point and I want you to do it by looking at my data:
   go through the base and propose "expected absence" rules —something that is in one document and
   should be in another— based on mismatches you ACTUALLY see. Show me the list with a
   real example of each before you code them, and we'll drop the ones that aren't worth it.

3. NAMED QUERIES. A separate script, in _tools/query.py, for the questions I repeat, and a
   _queries/index.md
   that lists them with their command. Store the RECIPE, not the answer: a written answer goes out of date
   without warning and nobody notices.

4. HEALTH CHECK. A health-check.md with what to look at periodically: dated facts older than
   six months, pending items whose date has already passed, broken links checked by opening them,
   mismatches between each table and its JSON, documents without "type" and pages that don't hang from
   any index.md.

5. _findings.md: one line for each cross-check that has already given us value, with its sources, so we don't
   discover it again. Start it with the ones you find now.

6. In _data/ (create it if it does not exist, with its index.md), add events.json (dates that
   aren't contract expiry dates: domains,
   certificates, end of support, reminders) and aliases.json (different names for the same
   thing, so the index of matches doesn't split it in two).

7. WHAT REPEATS. In _data/ add recurring.json: each thing that repeats, with what it is, the
   frequency (monthly, quarterly, yearly...), the months, who does it and the link to the document
   that explains how it is done. If it has a fixed day and is not already in the expiry calendar,
   have it appear there too. With it, generate _calendar-annual.md, month by month. The register
   only says WHEN it is due; how it is done stays in its document.

RULES THAT MUST BE WRITTEN DOWN in the conventions document:
- Generated views are NOT edited by hand, ever. You correct the source document and
  regenerate. A change written in the view is lost on the next run and, while it lasts,
  it lies.
- They are regenerated at the end of every block of changes.
- A pending item written without a marker is hidden, not noted. And if it has a deadline, the date goes
  on the same line.
- When a mismatch is a conscious decision and not an error, the reason is written in the
  source document so that it stops being flagged.
- What repeats is added to _data/recurring.json at the moment it appears, even if it is through an
  email; otherwise it lives in someone's memory. The register says when it is due; how it is done
  is in its document.
- No script opens a document for writing before it has read it: open(path, "w") empties the file
  the instant it opens it, and if the read fails afterwards, it is left at zero. You read first and
  write in one go.

DON'T touch the content that already exists except to add the missing markers, and tell me beforehand
what you are going to change. When you finish, show me the tree and run the regeneration once so I
can see the views filled in.
```
