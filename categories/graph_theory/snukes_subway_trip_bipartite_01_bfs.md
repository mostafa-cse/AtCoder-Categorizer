# Breadth First Search (BFS)

**Taxonomy Path**: `Graph Theory` > `Graph Traversal` > `Breadth First Search (BFS)`

## Description
This topic focuses on breadth first search (bfs) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Because edge weights are strictly 0 and 1, Dijkstra is unnecessary; 0-1 BFS using a double-ended queue computes the shortest path in linear time $O(N + M)$.
- Common Reductions: Find minimum subway fare to travel from station 1 to station $N$. Each company charges 1 fare when boarded, and transfers between lines of the same company are free. Construct a state graph: for each station $u$ and company $c$ operating at $u$, create an auxiliary vertex $(u, c)$. Add directed edge $u \to (u, c)$ with weight 1 (boarding), and $(u, c) \to u$ with weight 0 (alighting). Track edges connecting station $p$ and $q$ under company $c$ become 0-weight bidirectional edges $(p, c) \leftrightarrow (q, c)$. Run 0-1 BFS from station 1 to station $N$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc061_c`](../../analysis/AtCoder-arc061_c.md) | E. Snuke's Subway Trip | 2502 | Find minimum subway fare to travel from station 1 to station $N$. Each company charges 1 fare when boarded, and transfer... |
