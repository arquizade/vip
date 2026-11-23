# Graphify Output (Layer 3: Connections)

Graphify builds these files from the notes in `vault/main/`. Regenerate them after large changes. Do not edit them by hand.

| File | Contents |
| :--- | :--- |
| `graph.json` | Nodes and edges in machine-readable form. Used by `graph_walker.py`. |
| `graph.html` | Interactive graph for browsing in a browser. |
| `GRAPH_REPORT.md` | Community clusters and the most connected nodes. |

Keep this folder outside `vault/main/`. If Graphify writes inside the vault, the graph can index its own output.

Generated files are listed in `.gitignore` by default. Remove the entries if you want to share the graph with your team.
