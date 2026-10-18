# Breadth First Search (BFS)

**Taxonomy Path**: `Graph Theory` > `Graph Traversal` > `Breadth First Search (BFS)`

## Description
This topic focuses on breadth first search (bfs) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Since coordinates are bounded by M = 200000, we can represent free cells on each row x in [0, M] as maximal disjoint open intervals between obstacles. Two intervals on adjacent rows x and x+1 are connected iff they overlap. The total number of intervals is at most N + M. Running a BFS from the boundary / infinity marks all unclosed cells. Any cell belonging to an unmarked interval is completely enclosed by obstacles.
- Common Reductions: On an unbounded 2D grid with N obstacle points with coordinates up to 200000, find the number of non-negative integer grid points that cannot reach infinity without crossing obstacles.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc361_g`](../../analysis/AtCoder-abc361_g.md) | G - Go Terrirory | 2613 | On an unbounded 2D grid with N obstacle points with coordinates up to 200000, find the number of non-negative integer gr... |
