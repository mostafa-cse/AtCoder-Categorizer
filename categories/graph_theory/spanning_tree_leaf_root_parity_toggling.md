# DFS Tree

**Taxonomy Path**: `Graph Theory` > `Graph Traversal` > `DFS Tree`

## Description
This topic focuses on dfs tree techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: If K is odd, impossible (output "No"). In a tree, if child v is OFF and we toggle edge (u, v), v becomes ON. Whether u was ON or OFF, the total ON count changes by +2 or 0; it never decreases. Thus, the ON count increases in steps of 2, hitting every even target K up to the maximum achievable capacity.
- Common Reductions: Toggle edge endpoints to turn on exactly K lamps in a graph. Since each operation toggles 2 vertices, the total ON count is always even. On any spanning tree, bottom-up post-order toggling monotonically turns on lamps without ever decreasing the ON count.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| `[problem:AtCoder-abc345_f]` | Many Lamps | 2157 | Toggle edge endpoints to turn on exactly K lamps in a graph. Since each operation toggles 2 vertices, the total ON count... |
