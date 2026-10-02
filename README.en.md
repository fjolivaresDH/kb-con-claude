# Knowledge base with Claude

[Español](README.md) · **English**

How to build, in a folder of text files, a **working knowledge base** that Claude organizes, cross-checks and
keeps up to date: suppliers, contracts, access details, decisions, procedures and pending items, each fact with its date
and its source.

It comes from a real base, used every day for months. What is published here is **the method**:
the guides, the prompts and what we learned by breaking it. The content of that base is not here, and you don't need it
to build yours.

## Some examples of what you can keep

Suppliers and contacts · contracts and expiry dates · invoices · budget · receipts and expenses · access to services ·
domains, certificates and subscriptions · procedures · projects and decisions · inventories · articles and communication.

**These are examples we have already worked through, not a limit: everyone builds their own base with their own
topics.** When you paste the initial prompt, Claude offers them, asks whether any of them fits you and what other
topics you want to keep, and builds only that. What each one builds and which questions it answers: [`use-cases.md`](en/use-cases.md).

## Where to start

| If you use… | Start with |
|---|---|
| **Claude Cowork** *(nothing to install)* | [`guide-cowork.md`](en/guide-cowork.md) |
| **Claude Code** *(terminal or the Code tab of the desktop app)* | [`guide-claude-code.md`](en/guide-claude-code.md) |

Both build the same structure on the same folder, so **you can use them at the same time**.

**In Word?** Both guides are available for download in the [latest published release](https://github.com/fjolivaresDH/kb-con-claude/releases/latest).
They are generated automatically from these same files every time a release is published, so the web and the Word
files always say the same thing.

## The prompts, ready to copy

| Prompt | When |
|---|---|
| [`prompts/01-initial-cowork.md`](en/prompts/01-initial-cowork.md) | On day one, in Cowork |
| [`prompts/02-initial-claude-code.md`](en/prompts/02-initial-claude-code.md) | On day one, in Claude Code |
| [`prompts/03-growth.md`](en/prompts/03-growth.md) | **Weeks later**: generated views, cross-checks and queries |
| [`prompts/04-hooks-claude-code.md`](en/prompts/04-hooks-claude-code.md) | In Claude Code, after the growth prompt: so the rules enforce themselves |
| [`prompts/05-handoff.md`](en/prompts/05-handoff.md) | If you work from more than one computer |

## The idea in three principles

1. **Capture it when it happens**: you tell Claude in the chat, no forms.
2. **Every fact carries its date and its proof**: otherwise you can't tell whether it is out of date, or check it.
3. **A single source, with an owner**: each thing lives in one document, and the others link to it.

## Why this format

The documents follow the **[Open Knowledge Format (OKF) v0.2](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)**,
an open specification from Google Cloud designed so that people and AI agents understand the same knowledge in the
same way. It is minimal on purpose: a folder of Markdown files with a YAML header, no central registry and no
mandatory tool. That gives the base four properties:

| | What it means in practice |
|---|---|
| **You can read it without tools** | They are text files: they open in any editor, today and ten years from now. |
| **An agent understands it as is** | Claude reads and writes it directly, with no adapters and no database. |
| **Every change is visible** | A change is a text diff, in git or in your cloud's version history. |
| **It is yours and it moves with you** | It doesn't depend on any app: you change tool or computer and take all of it with you. |

And it is tolerant: the only mandatory thing is that each document says **what kind of thing it is**. Everything else
is optional, so you can start small and grow.

### Every fact, with its source, its date and its reliability

The specification starts from the same idea as this method. A base that **an agent maintains** has to be able to say,
besides what it knows, where it knows it from and how much it is worth. OKF v0.2 solves it with fields in the header of
each document; here, with working rules that Claude applies to each fact:

| The question | In OKF v0.2 | In this method |
|---|---|---|
| **Where does it come from?** | `sources`: the sources of each document | Every fact carries its proof: the original is linked (and, if you enable the archive, kept in `_documents/`) |
| **How much do I trust it?** | `verified`: unverified, confirmed by a process or reviewed by a person | "Signed" only with real evidence; whatever is missing is marked "to confirm", never made up |
| **Is it still true?** | `stale_after`: an expiry date per document | **Every** perishable **fact** carries the date it was provided, and the health check looks for the old ones |
| **Is it the current one?** | `status`: draft, stable or obsolete | One source per topic; whatever is superseded is marked, and `log.md` says what changed and when |
| **Does anything contradict it?** | — | If a new fact clashes with a stored one, both are written down with their source instead of choosing silently |

## Suggest improvements

This comes from a real base and gets better with what each person brings: a rule that is not needed, an example
that is missing, a simpler way to explain something or a technology that helps. Leave it in
[the repository's issues](https://github.com/fjolivaresDH/kb-con-claude/issues) *(a free GitHub account is
needed)*. Each published version says what changed.

## Author and license

Francisco Javier Rivas Olivares. Published under [CC BY 4.0](LICENSE): you can use and adapt it, crediting the author.
