#!/usr/bin/env python3
"""Keyword walk over a Graphify graph.json.

Usage:
    python3 graph_walker.py "your task description" [--hops 2]

Expected JSON layout (adjust KEYS below if your export differs):
    {"nodes": [{"id": "...", "label": "..."}],
     "links": [{"source": "...", "target": "...", "relation": "..."}]}
"""
import argparse
import json
import re
from collections import deque
from pathlib import Path

# Path: vault/main/.scripts/graph_walker.py -> vault/graphify-out/graph.json
GRAPH_PATH = Path(__file__).resolve().parents[2] / "graphify-out" / "graph.json"

NODES_KEY = "nodes"
EDGES_KEY = "links"  # Some exports use "edges"
STOPWORDS = {
    "the", "and", "for", "with", "that", "this", "from", "into", "about",
    "make", "need", "help", "work", "file", "files", "task",
}
MAX_OUTPUT_NODES = 40


def terms_from(prompt):
    words = re.findall(r"[a-zA-Z][a-zA-Z0-9_-]{2,}", prompt.lower())
    return {w for w in words if w not in STOPWORDS}


def build_adjacency(data):
    edges = data.get(EDGES_KEY, data.get("edges", []))
    adj = {}
    relations = {}
    for e in edges:
        s, t = e.get("source"), e.get("target")
        if s is None or t is None:
            continue
        adj.setdefault(s, set()).add(t)
        adj.setdefault(t, set()).add(s)
        relations[(s, t)] = relations[(t, s)] = e.get("relation", "related")
    return adj, relations


def find_seeds(nodes, terms):
    seeds = set()
    for n in nodes:
        label = str(n.get("label", n.get("id", ""))).lower()
        if any(term in label for term in terms):
            seeds.add(n["id"])
    return seeds


def walk(adj, seeds, hops):
    depth = {s: 0 for s in seeds}
    queue = deque(seeds)
    while queue:
        node = queue.popleft()
        if depth[node] >= hops:
            continue
        for nxt in adj.get(node, ()):
            if nxt not in depth:
                depth[nxt] = depth[node] + 1
                queue.append(nxt)
    return depth


def main():
    parser = argparse.ArgumentParser(description="Print a keyword sub-graph.")
    parser.add_argument("prompt")
    parser.add_argument("--hops", type=int, default=2)
    args = parser.parse_args()

    if not GRAPH_PATH.exists():
        raise SystemExit(f"Graph not found: {GRAPH_PATH}. Run Graphify first.")

    data = json.loads(GRAPH_PATH.read_text(encoding="utf-8"))
    nodes = data.get(NODES_KEY, [])
    labels = {n["id"]: n.get("label", n["id"]) for n in nodes}
    adj, relations = build_adjacency(data)

    seeds = find_seeds(nodes, terms_from(args.prompt))
    if not seeds:
        raise SystemExit("No matching nodes. Try different keywords.")

    depth = walk(adj, seeds, args.hops)
    ordered = sorted(depth.items(), key=lambda kv: (kv[1], labels.get(kv[0], "")))

    print(f"Seeds: {len(seeds)}  Nodes in sub-graph: {len(depth)}\n")
    for node_id, d in ordered[:MAX_OUTPUT_NODES]:
        print(f"[hop {d}] {labels.get(node_id, node_id)}")

    print("\nEdges:")
    shown = set(depth)
    printed = 0
    for s in shown:
        for t in adj.get(s, ()):
            if t in shown and s < t and printed < MAX_OUTPUT_NODES:
                rel = relations.get((s, t), "related")
                print(f"  {labels.get(s, s)} --{rel}--> {labels.get(t, t)}")
                printed += 1


if __name__ == "__main__":
    main()
