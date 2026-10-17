# Eulerian Path and Cycle

**Taxonomy Path**: `Graph Theory` > `Eulerian Path` > `Eulerian Path and Cycle`

## Description
This topic focuses on eulerian path and cycle techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Partitioning edges into circuits requires every vertex to have an even degree. If $\max \deg \ge 6$ or the count of degree-4 vertices $c_4 \ge 3$, 3 circuits always exist; if $c_4 \le 1$, impossible; if $c_4 = 2$, 3 circuits exist iff the two degree-4 vertices are connected by 2 paths and have independent simple loops, decidable via path tracing.
- Common Reductions: Given a connected undirected graph where every vertex has even degree, determine if the edges can be partitioned into three or more simple cycles.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc032_c`](../../analysis/AtCoder-agc032_c.md) | C. Three Circuits | 2284 | Given a connected undirected graph where every vertex has even degree, determine if the edges can be partitioned into th... |
