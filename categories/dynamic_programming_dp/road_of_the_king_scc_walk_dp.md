# DP on Trees and DAGs

**Taxonomy Path**: `Dynamic Programming (DP)` > `Dp on Different Structures` > `DP on Trees and DAGs`

## Description
This topic focuses on dp on trees and dags techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Maintain the state of the walk $(c, p)$ where $c$ is the number of vertices in the strongly connected component containing vertex 1, and $p$ is the length of the simple path extending outward from $C$ currently being traversed. When an edge returns to $C$, all $p$ path vertices merge into $C$, increasing $c$ to $c + p$. When an edge visits an unvisited vertex, $p$ increments to $p + 1$. When an edge visits an already traversed path vertex, a sub-cycle merges into the path.
- Common Reductions: Count directed walks of length $M$ starting and ending at vertex 1 that visit all $N$ vertices and form a strongly connected graph.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-codefestival_2016_final_f`](../../analysis/AtCoder-codefestival_2016_final_f.md) | F - Road of the King | 2539 | Count directed walks of length $M$ starting and ending at vertex 1 that visit all $N$ vertices and form a strongly conne... |
