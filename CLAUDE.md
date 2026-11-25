# VIP Router

You work inside a VIP (Vault-Index-Priority) repository. Follow these rules in every session.

## Execution rules

1. Never run broad searches across `vault/main/`. Open only the files named by these rules.
2. To learn project status, open `router/projects/<project>-card.md`. Read its `next` field and its Home table.
3. Follow the card's `Vault folder` path. Read that folder's `README.md` first. Then read the newest session log (highest date in the filename).
4. For questions about related notes or cross-project topics, read the Graphify report first (see the Graphify section below). Query `graph.json` only for specific links.
5. Keep each task to about 5 files. If you need more, state why before you read further.
6. Read `router/references/` only when the task touches a topic that has a reference file.

## Graphify knowledge graph

Before searching or grepping raw notes, read `vault/graphify-out/GRAPH_REPORT.md` when the question relates to the vault. It lists the note clusters and the most connected notes.

* Summary: `vault/graphify-out/GRAPH_REPORT.md`
* Links: `vault/graphify-out/graph.json`, queried with `vault/main/.scripts/graph_walker.py <keywords> --hops 2`
* Do not rebuild the graph. Graphify runs only when the user asks.
* If the report is missing, say so, then use the card and project README instead.

## One Home Per Fact

* Status and next step: `router/projects/` or `router/clients/`
* Purpose, architecture, and decisions: the project `README.md` in `vault/main/01-projects/`
* Session history: dated logs in the same project folder
* Relationships: `vault/graphify-out/graph.json` (generated, never edited by hand)

If you find the same fact in two places, update the authoritative home and link to it from the other place. Do not copy the fact.

## Ending a session

1. Write a session log at `vault/main/01-projects/<project>/YYYY-MM-DD-session.md` using `vault/main/06-metadata/templates/session-log-template.md`.
2. Update the card's `next` and `updated` fields.
3. Do not write the next step into the project README. The card holds status.

## Naming

* Name every new file and folder in kebab-case: lowercase letters, digits, and single hyphens. Example: `webhook-retry-logic.md`.
* Session logs start with the date: `YYYY-MM-DD-session.md`.
* Project cards end with `-card.md`: `webhook-service-card.md`.
* Keep these exceptions: `README.md` and `CLAUDE.md` keep their names. Template folders start with an underscore, such as `_template`.
* Do not use spaces, underscores, or capital letters in new names.

## Limits

* Create new projects with `scripts/new-project.sh <name>`. Do not copy folders by hand.
* Do not create a card for a project that has no `README.md` in its vault folder.
* Do not edit files in `vault/graphify-out/`. Regenerate them with Graphify.
* Keep this file under 500 tokens. Move long guidance to `router/references/`.
