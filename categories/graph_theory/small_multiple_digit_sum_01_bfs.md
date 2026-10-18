# 0/1 BFS

**Taxonomy Path**: `Graph Theory` > `Shortest Paths` > `0/1 BFS`

## Description
This topic focuses on 0/1 bfs techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Any positive integer can be constructed starting from 1 by alternating two operations: multiplying by 10 and adding 1 (without carrying beyond 9). The transitions naturally map into modulo $K$ arithmetic where multiplying by 10 does not increase the digit sum, while incrementing adds 1. 0-1 BFS computes shortest paths in linear time without logarithmic overhead.
- Common Reductions: Find the minimum sum of digits of a positive multiple of $K$. Model as shortest path on a directed graph with $K$ vertices $0, 1, \dots, K - 1$ representing remainders modulo $K$. From remainder $u$, multiplying by 10 transitions to $(10u) \bmod K$ with edge weight 0 (digit sum unchanged); adding 1 transitions to $(u + 1) \bmod K$ with edge weight 1 (digit sum +1). The shortest path from state 1 (cost 1) to state 0 computes the answer via 0-1 BFS in $O(K)$ time.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc084_b`](../../analysis/AtCoder-arc084_b.md) | D. Small Multiple | 2457 | Find the minimum sum of digits of a positive multiple of $K$. Model as shortest path on a directed graph with $K$ vertic... |
