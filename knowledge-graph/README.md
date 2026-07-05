# Knowledge Graph

A machine-readable map of the relationships across this research program: Go-Shape Theory, the Sovereign Constitution / Sovereign Agent Architecture (SAA), Constitutional Hiring, and *The Art of Clarity*. It documents how the repo's concepts connect to each other — it does not introduce new claims beyond what's argued in the source papers.

## Files

- `research_program_knowledge_graph_v4.json` — the graph data (91 nodes, 138 edges)
- `graph_overview.mermaid` — a full Mermaid rendering of the graph, generated directly from the JSON (not hand-drawn), grouped by category

## Structure

Nodes are typed into 7 categories:

| Category | Count | Examples |
|---|---|---|
| Core Concept | 29 | Go-Shape Theory, Deep/Surface Structure, Enduring Intent, Alignment |
| Property | 28 | Persistence, Stability, Brittleness, Resilience, Flexibility, Transparency |
| Framework | 8 | The Sovereign Constitution, Propositions 1–6 |
| Diagnostic Tool | 8 | Method Marks, The Intent Audit Protocol, M.I.R.R.O.R. |
| Sovereign Principle | 7 | S1–S7 |
| Domain Application | 6 | Constitutional Hiring, Project Collapse |
| Technical Application | 5 | The Sovereign Shell, Constitutional Reasoning Engine |

Edges are typed relations (`contains`, `governs`, `includes`, `has`, `proposes`, `tests`, `positive inheritance`, `negative inheritance`, etc.) — not a generic "related to" link. The two largest hubs are **Go-Shape Theory** and **The Sovereign Constitution**, reflecting a top-down architecture: Go-Shape Theory supplies the theoretical grammar, the Sovereign Constitution supplies the normative grammar, and downstream applications (Sovereign Shell, Constitutional Hiring, Project Collapse) inherit from both.

## Known open items (intentional, as of v4)

- **Project Collapse** and **Guru vs. Architect Diagnostic** are currently orphan nodes (no edges). This is intentional, not an error: Project Collapse is still in early conceptual stages, and Guru vs. Architect is a human-specific diagnostic rather than a general systems property, so it doesn't yet map cleanly onto the structural backbone. Both will be wired in once they mature.

## Version history

- **v3 → v4**: Merged two pairs of duplicate nodes that had emerged from earlier revisions without full reconciliation — `strategic_structure` / `strategic_structure_definition`, and `enduring_intent` / `enduring_intent_construct`. Also fixed the `structural_properties` node, which previously listed the six structural properties only as description text with no actual edges to those property nodes (a dead end); it now connects to them directly.

## Regenerating the diagram

The Mermaid file is generated programmatically from the JSON, not maintained by hand, so it never drifts out of sync:

```python
import json, re

d = json.load(open('research_program_knowledge_graph_v4.json'))

def safe_id(i):
    return re.sub(r'[^a-zA-Z0-9_]', '_', i)

cats = {}
for n in d['nodes']:
    cats.setdefault(n['category'], []).append(n)

lines = ["flowchart TD"]
for cat, ns in cats.items():
    lines.append(f'  subgraph {safe_id(cat)} ["{cat}"]')
    for n in ns:
        lines.append(f'    {safe_id(n["id"])}["{n["label"]}"]')
    lines.append('  end')

for e in d['edges']:
    lines.append(f'  {safe_id(e["source"])} -->|{e["label"]}| {safe_id(e["target"])}')

open('graph_overview.mermaid', 'w').write("\n".join(lines))
```
