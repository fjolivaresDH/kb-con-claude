# Projects prompt

When you start running projects: documents that come in and documents you deliver, in several versions.

```
I want to keep projects in an area of their own. Create the projects/ folder with its index.md: a table
with each project, who it is for, who pays for it and what state it is in. Each project has its own page,
projects/<project>.md, whose frontmatter says who it is for and who commissions it, because they are not
always the same, and its state (active, on hold or closed); and in the body, the goal, who is involved,
the milestones and two fixed sections: "Status and next step", at the top, in two lines, and
"Decisions", at the bottom, a table with date, what was decided, why and by whom, which only grows (a
decision that changes is not deleted: the one that replaces it is added). When a project has files,
create its folder projects/<project>/
with two subfolders: sources/ for what we receive (proposals, specifications, manuals, minutes) and
deliverables/ for what we produce. Deliverables carry the version in the name (-v1, -v2...),
are never overwritten, and deliverables/index.md is their register: version, date, what changed and who
it was sent to. If I archive originals in another folder, that one stays for what does not belong to a
project (contracts, invoices). A closed project does not move folder (the links would break): the state
field is enough. If a project page goes past about 400 lines, split it into several documents inside
the project folder and move the status and the decisions into files of their own, status.md and
decisions.md, next to the page, with that project's working rules in the same folder; only in that
project, because a status repeated in three places drifts out of sync. Move here whatever we already
have that is a project and update the links; if there are generated views, they must not read sources/
or deliverables/, they must group the projects by state and they must flag the ones without one. And before producing a
final deliverable, show me a sketch first so I can approve it. Add these rules to the Instructions (or to
CLAUDE.md).
```
