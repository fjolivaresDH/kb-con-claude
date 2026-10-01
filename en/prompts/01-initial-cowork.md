# Initial prompt · Cowork

Paste it into a new Cowork project with the empty folder already added. First, replace `[ORGANIZATION]` and `[AREAS]`. Full explanation in the [Cowork guide](../guide-cowork.md).

```
I want you to build a knowledge base for [ORGANIZATION] in this folder.

What I want it for: for you to act as an assistant that keeps everything I find hard to remember or
have scattered across emails, folders, spreadsheets and different programs —expiry dates,
access details, decisions and why they were made, contacts, project status—. You store it in its
place and keep a record, so that I can ask you about it later or read it directly.

Use the OKF format (Google Cloud's Open Knowledge Format). This is the specification;
read it before you start:
https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md

Note: the acronym "OKF" also refers to other things (for example the Open Knowledge
Foundation). Use only the specification at the link above.

BEFORE YOU CREATE ANYTHING, ASK ME WHAT I AM GOING TO KEEP.
These are examples that already work, not a closed list: the base is mine and I build it with
my own topics. Show them to me, ask whether any of them fits me and what other topics I want to
keep. Wait for my answer and build only what the chosen ones need: the rest can be added
later with one sentence.
   1. Suppliers and contacts    -> a single directory: company, what it does and who is who.
   2. Contracts and expiry      -> contract register (table + JSON) with dates, notice periods
      dates                        and renewals.
   3. Invoices                  -> invoice register (table + JSON) linked to its contract.
   4. Budget                    -> one document per year with the budget lines, planned and
                                   actual, cross-checked with contracts and invoices.
   5. Receipts and expenses     -> monthly reconciliation of a card's charges with their
                                   receipts, and a register of the months handed in.
   6. Access to services        -> which service, its address and which account you sign in
                                   with. Never passwords.
   7. Domains, certificates     -> their renewal calendar.
      and subscriptions
   8. Procedures                -> how each thing is done, step by step.
   9. Projects and decisions    -> status, milestones and why each thing was decided.
  10. Inventories               -> equipment, licenses or software, always dated.
If I haven't put any areas in [AREAS], suggest them based on what I choose. And before you create
each case, tell me in one line what you are going to create for it.

FORMATTING RULES (always apply them, in the future too):
- One topic = one .md file, with a kebab-case name (example: invoice-register.md).
- Every concept document starts with YAML frontmatter and the "type" field is MANDATORY.
  "type" is an open vocabulary (the spec doesn't register the values centrally), but being
  open does NOT mean free: two labels for the same thing split the vocabulary and break
  any filter by type. We will start with these four, in English and in the singular:
    Reference     -> what something is and how it is set up. The normal case.
    Procedure     -> steps to do something.
    Tool          -> record of an application or service.
    Concept       -> an idea or term, with no specific instance behind it.
  Keep the list of types in use written in the conventions document. If one day none of them
  fits and a new one is needed, ADD IT TO THAT LIST in the same change: otherwise nobody will know it
  exists and it will end up duplicated.
  Also include: title, description, tags (list) and timestamp (date YYYY-MM-DD).
- Every folder has its own index.md listing what it contains, BUT index.md files do NOT have
  frontmatter (spec §8). The only exception: the index.md at the root of the bundle, which has
  only okf_version: "0.2" and nothing else.
- Links between documents use absolute bundle paths: /folder/file.md
- There is a log.md at the root where you write down EVERY change in one line, grouped by day under a
  "## YYYY-MM-DD" header.

CREATE THIS STRUCTURE:
1. index.md at the root: general index, with the list of areas and how everything is organized
   (its only frontmatter is okf_version: "0.2").
2. log.md at the root: change diary (it starts with the line for the initial creation).
3. _templates/ with index.md and one empty template per type, ready to copy:
   reference.md, procedure.md, tool.md and concept.md. Each one with its example frontmatter,
   and the "type" of each template must be its own (the concept one says Concept, not another).
4. _documents/ with a README.md explaining that it is the "inbox" where PDFs waiting to be
   processed are left, and three subfolders: invoices/, contracts/ and other/ (the last one for
   anything that is neither an invoice nor a contract: certificates, offers, minutes, reports, manuals…).
5. _data/ with index.md, invoices.json and contracts.json, ONLY if I have chosen contracts or
   invoices (see the next section).
6. One folder for each of these areas, each with its own index.md: [AREAS]
7. Whatever each chosen case needs. For example, for receipts and expenses, a monthly procedure
   and a register of months handed in; for budget, the document for the current year; for
   access, a table of services without a single password.

JSON DATA LAYER (_data/) — ONLY IF I HAVE CHOSEN CONTRACTS OR INVOICES:
Besides the Markdown tables, I want contracts and invoices in JSON, because they are
records that get filtered, sorted and added up. Create the two files with an empty array and a
"_meta" block that documents the schema, using exactly these fields:

invoices.json -> array "invoices", each element with:
  number, contract_id, date, due_date, supplier, supplier_id, description, company,
  net, tax, total, currency, recurring (true/false), notes

contracts.json -> array "contracts", each element with:
  id, subject, supplier, supplier_id, company, date, status, signed_date,
  amount, currency, duration, expiry, notice_period, historical, notes

THE LINK BETWEEN THE TWO (important, and it is what pays off most):
Almost every invoice corresponds to a contract, and almost every contract ends up in invoices. Store that
link IN ONE DIRECTION ONLY, so you don't have to maintain it twice:
- Each invoice carries "contract_id" with the id of the contract it corresponds to, or null if it is a
  one-off purchase.
- Contracts do NOT carry a list of invoices: you get it by filtering by contract_id.
With that you can ask "how much have we paid so far from this bank of hours" or "which contracts
haven't generated any invoice yet". And warn me about invoices with contract_id null that should
have one: it means something is being paid that isn't contracted in the register.

Data conventions: dates in YYYY-MM-DD format; numeric amounts without a thousands
separator; null when the fact is not recorded.

The "status" field of contracts is a CLOSED LIST declared in the _meta
(signed, invoiced, unsigned, pending_offer, to_confirm). Using an undeclared value
silently breaks the filters: if a new one is needed, it is added to the _meta in the same change.

Invoices do NOT have a "status" field: whether an invoice is paid, overdue or pending is a matter
for accounting, not for the knowledge base. A field that always said "registered" would be
read as a payment status and would be lying. Don't add it.

DECLARE THE SCOPE OF EACH REGISTER in its _meta and in the header of its table, because it changes
how they are used and can't be guessed by reading them:
- Contracts = CENSUS: they aim to be complete. If one is missing, it is a gap that has to be closed.
  Contracts that have ended are not deleted: they carry "historical": true and stay there, because "what have we
  ever contracted with X" is a real question.
- Invoices = YOU decide and write it down. If you are going to put all of them in, it is a census and they can be added up. If
  you are going to put in only some, to record that the expense exists, it is a SAMPLE and
  then you have to warn that they are NEVER added up as total spend.

In _data/index.md explain what the data layer is for, document both schemas, leave
query examples and write these two maintenance rules:
1. When you add or change a contract or an invoice you have to update BOTH VIEWS, the Markdown
   table (readable, for reading and sharing) and the JSON (structured, for querying).
2. FIRST THE JSON, THEN THE ROW. When this gets out of sync, what is missing is almost always
   the Markdown row. And if they differ: the JSON rules on hard data (dates, amounts,
   statuses) and the Markdown rules on the narrative (what the contract says, which clause matters).

Also create, for the ones I have chosen, these registers in Markdown, linked to their JSON:
- A contract register (table: contract, supplier, subject, company, date/status,
  amount) plus an "Expiry dates and renewals" section so you can answer at any
  time "what expires in the next 6 months".
- An invoice register (table: no., date, due date, supplier, description, company,
  net, VAT, total, notes).

WATCH OUT WITH "WHAT EXPIRES": contracts with suppliers are not the only thing that expires. Domains,
hosting, certificates and subscriptions have their own calendar, and they tend to expire sooner
and more often. If you keep those things in another document, MAKE THE TWO REFERENCE EACH OTHER, and
to answer "what expires in the next 6 months" always look at both. A calendar that doesn't
know the other one exists gives an incomplete answer that looks complete.

HOW WE ARE GOING TO WORK (this is the most important part):
Most of the knowledge won't reach you as documents in a folder; instead, I will
tell you about it: loose facts in the chat, emails I paste, screenshots, decisions,
clarifications and corrections to things you had already stored for me. I want you to treat that as
first-class material and file it as well as a PDF. Specifically:
- When I give you a fact or explain something, YOU decide which document in the bundle it fits in and
  store it there, without asking me where it goes. If the right document doesn't exist, create it in the
  matching area and add it to that folder's index.md.
- Before you create something new, check whether there is already a document covering that topic and
  update it instead of duplicating the information.
- THE SWEEP: if the fact affects several documents, propagate it to ALL the affected places, not
  just one. This is the step that turns a folder of files into a knowledge base,
  and it is the one most often forgotten. Always ask yourself: the folder's index.md (otherwise the page is born
  orphaned), the contact directory, the registers and their JSON, the expiry
  calendars, the inventories and the access records.
- If what I tell you contradicts something you already have stored, WARN ME by pointing out the contradiction
  instead of simply overwriting. And if it isn't recorded which one is right, WRITE IT DOWN in the
  document, with both versions, the date, where each one comes from and what it would take to
  close it. The danger is not the contradiction: it is choosing one version without leaving a trace, because
  whoever reads it later will see a clean fact and won't know there were two.
  Note: a fact that has CHANGED (a price that goes up, a contact who leaves) is not a
  contradiction, it is an update: it is replaced and re-dated.
- WHAT YOU ANSWER ME THAT IS WORTH IT, FILE IT. Much of the value doesn't appear when you store a
  document, but when you ask: a comparison, a cross-check between areas, a mismatch that shows up when
  you put the information together. That is born in the chat and dies in the chat if nobody writes it down. If an
  answer took work and would be needed again, store it as a document in the matching area
  and add it to its index.md. Signs that it's time: the question has been asked more than once, the
  answer crosses several documents, a fact appears that wasn't in any of them, or a
  decision is made and it's worth knowing WHY six months from now.
- If we review something that looked like a problem and decide that it isn't, WRITE IT DOWN WITH ITS DATE as
  reviewed and ruled out. Otherwise, it will come up again as a finding in every review and we will end up
  ignoring the warnings.
- When I correct you, correct the document and don't leave traces of the previous version unless
  the history has value; in that case, mark it clearly as superseded.
- DATE THE INFORMATION THAT EXPIRES. When you store a perishable fact —inventories and counts
  (units, equipment, licenses), statuses ("unsigned", "pending activation", "in progress"),
  figures you see on
  a screen or screenshot, prices and fees, contacts— write in brackets the date I give it
  to you: for example "340 units contracted (as of 2026-03-15)" or "pending activation
  (March 2026)". That way I'll know whether a fact is fresh or out of date. There is no
  need to date what is stable (a tax ID, a clause of a signed contract, a definition). If
  we review a dated fact and it is still valid, update the date.
- Write each change in log.md, ONE LINE PER CHANGE, under a "## YYYY-MM-DD" header for the day.
  Open a new header each day; don't pile entries under an earlier date. The log says WHAT
  changed and WHEN; it is not the place for reasoning or analysis. If a log entry
  is turning into a paragraph, that paragraph belongs in a document.
- At the end of a block of work, tell me which files you have written to.

CRITERIA YOU MUST ALWAYS RESPECT:
- Privacy: NEVER store passwords, API keys or sensitive personal data. If a
  document contains them, extract only what is needed and leave out the rest, telling me so.
- Evidence: mark something as "signed" or "contracted" ONLY if there is real evidence (signed
  document, contract in force or invoice). If it is a draft, an offer or an authorized expense,
  say so; don't treat it as signed.
- Amounts: you can store them in the knowledge base, but don't include them in documents
  meant for third parties unless I ask you to explicitly.
- When in doubt or if a fact is missing, ask me or mark it as "to confirm". Don't make it up.

When you finish:
1. Show me the tree of folders and files created.
2. Give me, in a separate text block ready to copy in one go, a summary of all the
   rules above written as standing instructions (15 lines at most). I am going to paste it
   into the "Instructions" section of this project, so: write it addressing yourself
   in the second person, without headings or embellishments, and get to the point — OKF format with the link to
   the specification, index.md without frontmatter, how to handle the knowledge that reaches you through the
   chat, where each thing goes, the rule for keeping the Markdown table in sync with the JSON, the one about dating
   the facts that expire, the one about the sweep to all the affected documents, the one about filing what
   you answer me that is worth it, and the privacy and evidence criteria.
3. Tell me how we start loading knowledge.
```
