# VIP: Vault-Index-Priority

A three-layer repository for AI agents and humans to manage project knowledge without wasting context.

VIP separates three jobs:

1. **Direction (router/):** Small routing cards tell the AI agent where to look and what to do next.
2. **Memory (vault/main/):** An Obsidian vault holds project entry points, session logs, and atomic notes.
3. **Connections (vault/graphify-out/):** A knowledge graph shows how notes relate, so the agent loads only the relevant neighbors.

Result: an agent reads about 5 targeted pages per task instead of scanning thousands of files.

The framework combines three methods:

* **ICM (Interpretable Context Methodology):** The folder structure is the instruction set.
* **PARA (Projects, Areas, Resources, Archive):** Organizes the vault by how active each item is.
* **Graphify:** Builds a graph from your notes to surface links you did not write by hand.

---

## Why this structure

Large knowledge bases hurt AI performance in three ways:

* Scanning a full vault for each question dilutes reasoning.
* Long contexts slow responses.
* Token usage climbs fast, which limits how many sessions you can run.

VIP fixes this with routing. The agent reads one global file, one status card, and one project README. Then it stops.

---

## Quick start

### Requirements

* [Claude Code](https://docs.claude.com/en/docs/claude-code) or another AI coding CLI that reads `CLAUDE.md`
* [Obsidian](https://obsidian.md) (optional, but recommended for the vault)
* Python 3.9+ (only for the graph walker script)
* Graphify or another graph builder (optional; see `vault/graphify-out/README.md`)

### Setup

```bash
git clone https://github.com/arquizade/vip.git
cd vip
scripts/new-project.sh my-first-project
```

The script copies `vault/main/01-projects/_template/` into `vault/main/01-projects/my-first-project/` and creates `router/projects/my-first-project-card.md`.

Then:

1. Open the `vip/` folder in your AI tool. Claude Code reads the root `CLAUDE.md` automatically. `AGENTS.md` links to the same file.
2. Open `vault/main/` as a vault in Obsidian.
3. Fill in the project README and the card. Replace every remaining `{{PLACEHOLDER}}`.
4. Start a session. Ask the agent for the project status. It should open only the card, then the project README.
5. At the end of the session, ask the agent to write a session log using the template.

---

## Folder map

```text
vip/
├── README.md                     This file
├── LICENSE                       MIT license
├── .gitignore                    Files excluded from git
├── scripts/
│   └── new-project.sh            Creates a project from the template and its card
│
├── router/                    Layer 1: Direction and routing
│   ├── CLAUDE.md                 Global router instructions (keep under 500 tokens)
│   ├── README.md                 Guide to the router layer
│   ├── _meta/                    Card schema and formatting rules
│   ├── _templates/               Blank cards for new projects and clients
│   ├── projects/                 One status card per project (under 300 tokens each)
│   ├── clients/                  One status card per client
│   └── references/               Shared standards the agent should follow
│
└── vault/                        Layers 2 and 3: Memory and connections
    ├── README.md                 Guide to the vault and graph layers
    ├── main/                     Layer 2: Obsidian vault (PARA structure)
    │   ├── 00-inbox/             Raw captures waiting for processing
    │   ├── 01-projects/          Active projects, one folder each
    │   │   └── _template/        Starting point. Copy it, do not edit it.
    │   ├── 02-areas/             Ongoing responsibilities
    │   ├── 03-resources/         Atomic notes, one idea per note
    │   ├── 04-archive/           Finished or inactive work
    │   ├── 05-attachments/       Images, PDFs, and media
    │   ├── 06-metadata/          Templates and vault standards
    │   └── .scripts/             Helper scripts such as graph_walker.py
    └── graphify-out/             Layer 3: Generated graph files (do not edit by hand)
```

Each top-level folder has its own README with more detail.

---

## The "One Home Per Fact" rule

Every fact lives in exactly one place. Duplicates drift apart, and the agent then reads conflicting information.

| Data type | Single home | Never store here |
| :--- | :--- | :--- |
| Status and next step | `router/projects/` cards | Vault notes, graph files |
| Purpose, architecture, and session logs | `vault/main/01-projects/<project>/` | Cards, router files |
| Relationships between notes | `vault/graphify-out/graph.json` | Hand-written index notes |

If a fact needs a second home, link to the first home instead of copying it.

---

## Typical session flow

1. The agent reads the root `CLAUDE.md`.
2. It opens `router/projects/<project>-card.md` and reads the `next` field.
3. It follows the card's `Vault folder` path and reads that folder's `README.md`.
4. It reads the newest session log in that folder.
5. If it needs related notes, it runs the graph walker against `graph.json`.
6. It works on the task.
7. It writes a session log and updates the card's `next` and `updated` fields.

---

## Graph walker

`vault/main/.scripts/graph_walker.py` takes a prompt, matches keywords to graph nodes, and walks one or two hops outward. It prints only the matching sub-graph.

```bash
python3 vault/main/.scripts/graph_walker.py "webhook retry logic" --hops 2
```

The script assumes a simple JSON layout (`nodes` with `id` and `label`, and `links` or `edges` with `source` and `target`). Check the script header and adjust the keys if your Graphify export differs.

---

## Adapting VIP to your work

* Rename the numbered folders if your vault uses a different structure. Update the paths in the root `CLAUDE.md` to match.
* Edit `vault/main/01-projects/_template/README.md` to change the sections every project gets.
* Add a card for each project or client. Keep cards short.
* Add standards to `router/references/` for anything the agent should follow every time.

---

## Credits

VIP builds on these projects and ideas:

* PARA setup: [heyitsnoah/claudesidian](https://github.com/heyitsnoah/claudesidian)
* ICM structure: [RinDig/Interpretable-Context-Methodology](https://github.com/RinDig/Interpretable-Context-Methodology/tree/main)
* One Home Per Fact concept: Kenneth, [BrewedOps](https://brewedops.com/about/)

---

## License

MIT. See `LICENSE`.
