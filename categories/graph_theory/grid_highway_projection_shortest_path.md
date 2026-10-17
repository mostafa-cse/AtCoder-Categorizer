# Dijkstra's Algorithm

**Taxonomy Path**: `Graph Theory` > `Shortest Paths` > `Dijkstra's Algorithm`

## Description
This topic focuses on dijkstra's algorithm techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Any optimal trajectory between arbitrary grid points uses at most one entry and exit segment on regular streets to access the highway grid, projecting $S$ and $G$ onto their 4 bounding highway lines.
- Common Reductions: On an integer grid where lines $x = Bn$ and $y = Bn$ are highways (cost 1/unit) and other lines cost $K$/unit, find the minimum time to travel from $(S_x, S_y)$ to $(G_x, G_y)$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc258_f`](../../analysis/AtCoder-abc258_f.md) | F. Main Street | 2306 | On an integer grid where lines $x = Bn$ and $y = Bn$ are highways (cost 1/unit) and other lines cost $K$/unit, find the ... |
