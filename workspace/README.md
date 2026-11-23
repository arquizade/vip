# Workspace (Layer 1: Direction and Routing)

This folder is what you open in your AI tool. It holds the instructions and the status cards that route the agent to the right notes.

## Contents

| Path | Purpose |
| :--- | :--- |
| `CLAUDE.md` | Global router. The agent reads this first in every session. |
| `_meta/` | Rules for card format, including the required fields. |
| `_templates/` | Blank cards to copy when you start a new project or client. |
| `projects/` | One card per active project. |
| `clients/` | One card per client, if you do client work. |
| `references/` | Standards the agent follows, such as coding style or writing voice. |

## Rules

* Keep each card under 300 tokens. Cards point to information. They do not hold it.
* Update `next` and `updated` after every session.
* Put long standards in `references/`, not in `CLAUDE.md`.
