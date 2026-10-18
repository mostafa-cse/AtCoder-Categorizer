# Breadth First Search (BFS)

**Taxonomy Path**: `Graph Theory` > `Graph Traversal` > `Breadth First Search (BFS)`

## Description
This topic focuses on breadth first search (bfs) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Operations $(x, y)$ with $x \ne y$ are reversible CNOT gates that can turn 0 into 1 without destroying existing 1s. Self-resets $(i, i)$ irreversibly turn 1 into 0. By running forward BFS on $A$ along non-loop edges, all reachable positions become 1. For any position $i$ where $B_i=0$ but $A_i=1$, if self-reset $(i, i)$ exists, we can treat $B_i$ as 1 and append $(i, i)$ at the end. Then run reverse BFS from $B$ along non-loop edges. If the forward and backward expanded states coincide, the concatenated sequence of operations achieves the transformation in $\le 2N$ operations.
- Common Reductions: Transform binary string $A$ into $B$ using at most $2N$ operations where $(x, y)$ flips $y$ when $x=1$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc215_e`](../../analysis/AtCoder-arc215_e.md) | E - CNOT Party | 2418 | Transform binary string $A$ into $B$ using at most $2N$ operations where $(x, y)$ flips $y$ when $x=1$.... |
