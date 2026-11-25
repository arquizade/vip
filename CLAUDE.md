# Folder Router

You work inside a knowledge repository. The folder names below are the ones this repository uses. If you rename a folder, update the tables in this file first. Follow these rules in every session.

## Where everything lives

| Area | Home |
| --- | --- |
| Project records | `router/projects/`, one card per project |
| Client records | `router/clients/`, one card per client |
| Reference standards | `router/references/` |
| Card schema and rules | `router/_meta/card-schema.md` |
| Long-term record (sessions, decisions, notes) | `vault/main/` |
| Generated graph | `vault/graphify-out/` (do not edit) |

## Routing

| Task | Go to |
| --- | --- |
| Project status or next step | `router/projects/<project>-card.md`, then the project README |
| Project history or decisions | Newest session log in `vault/main/01-projects/<project>/` |
| Related notes across projects | `vault/graphify-out/GRAPH_REPORT.md`, then `graph.json` through `graph_walker.py` |
| Client status | `router/clients/<client>-card.md` |
| Standards for a topic | The matching file in `router/references/` |
| New project | `scripts/new-project.sh <name>` |

## Rules

1. Never search `vault/main/` broadly. Open only the files these tables name.
2. Read the project README before any other file in its folder. Then read the newest session log.
3. Keep each task to about 5 files. State why if you need more.
4. Before grepping raw notes, read `vault/graphify-out/GRAPH_REPORT.md`. Query `graph.json` only for specific links. Do not rebuild the graph unless the user asks. If the report is missing, say so.
5. Read `router/references/` only for a topic that has a file there.

## Ending a session

1. Write `vault/main/01-projects/<project>/YYYY-MM-DD-session.md` from `vault/main/06-metadata/templates/session-log-template.md`.
2. Update the card's `next` and `updated` fields.
3. Do not write the next step into the project README. The card holds status.

## Naming

Use kebab-case for new files and folders. Session logs start with the date. Cards end with `-card.md`. Keep `README.md` and `CLAUDE.md` as they are. Template folders start with an underscore. Do not use spaces, underscores, or capitals in new names.

## Limits

* Create projects with `scripts/new-project.sh <name>`. Do not copy folders by hand.
* Do not create a card for a project that has no `README.md`.
* Do not edit files in `vault/graphify-out/` by hand.
