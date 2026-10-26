---
name: graphify
description: Map a codebase or GitHub repo into a knowledge graph with the graphify CLI, then query it (explain, path, query) instead of reading files one by one. Use for questions about a project's architecture or how files connect.
---

# Graphify

Graphify (github.com/Graphify-Labs/graphify, MIT) parses code with tree-sitter into a knowledge graph. Code extraction is local and needs no LLM.

## Setup (once per machine or virtual environment)

```bash
pip install graphifyy   # the official package is graphifyy (double y)
```

On Windows with uv: `uv pip install graphifyy` inside the project's venv.

## Build the graph (code only, no LLM)

```bash
cd <project> && graphify update .
```

Outputs in `graphify-out/`: `graph.json` (full graph), `graph.html` (interactive viewer), `GRAPH_REPORT.md` (key concepts, communities, suggested questions). Read GRAPH_REPORT.md first. Add `graphify-out/` to `.gitignore` unless the team wants it committed.

## Query instead of grepping

```bash
graphify explain "NodeName"        # a node and its neighbors (add --all for every edge)
graphify path "A" "B"              # shortest path between two concepts
graphify query "plain question"    # scoped subgraph for a question
```

Edges are tagged EXTRACTED (read from the source) or INFERRED (resolved by graphify). Say which when it matters.

## Notes

- Docs, PDFs and images need a semantic pass with an LLM API key; skip them unless the user provides one. Never ask the user to paste API keys into chat.
- Re-run `graphify update .` after code changes; it only re-extracts changed files.
- Explain results in Spanish, step by step, in plain language.
