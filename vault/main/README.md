# Obsidian Vault (PARA Structure)

PARA sorts notes by how actionable they are. Folder names use kebab-case with a number prefix so they sort in order.

| Folder | What goes here | Example |
| :--- | :--- | :--- |
| `00-inbox/` | Unsorted captures. Empty this folder regularly. | Voice memo transcript, web clip |
| `01-projects/` | Work with an end point | `webhook-service/` |
| `02-areas/` | Ongoing responsibilities with no end point | Client accounts, infrastructure |
| `03-resources/` | Atomic notes. One idea per note. | `zettel-one-home-per-fact.md` |
| `04-archive/` | Finished projects and inactive material | Completed `01-projects/` folders |
| `05-attachments/` | Images, PDFs, and other binary files | Diagrams, screenshots |
| `06-metadata/` | Templates and vault rules | `templates/` |
| `.scripts/` | Helper scripts for the vault | `graph_walker.py` |

## Project folders

The `01-projects/_template/` folder is the starting point for every project. Do not work inside it. Copy it with `scripts/new-project.sh <name>` from the repository root.

Each project folder contains:

* `README.md`: the entry point. The AI agent reads it first. It holds purpose, architecture, decisions, and links.
* `YYYY-MM-DD-session.md`: one log per working session.

## Rules

* Use the templates in `06-metadata/templates/` for session logs and atomic notes.
* Keep one idea per note in `03-resources/`.
* Link related notes with wikilinks, such as `[[zettel-one-home-per-fact]]`.
* When a project ends, move its folder to `04-archive/` and set the card's `status` to `done`.
