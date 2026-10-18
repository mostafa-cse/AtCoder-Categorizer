# Segment Tree (Point Update Range Query)

**Taxonomy Path**: `Data Structures (DS)` > `Segment Tree` > `Segment Tree (Point Update Range Query)`

## Description
This topic focuses on segment tree (point update range query) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Between two consecutive fixed constraints $i_{j-1} \to i_j$, the transition of valid fillings depending on whether the endpoints contain coffee is expressed as a $2 \times 2$ transfer matrix $\bm{f}(\Delta i, \Delta a)$ using non-adjacent combinations $\text{noadj}(n, r) = \binom{n - r + 1}{r}$. Placing these matrices at indices $i_j$ in a Segment Tree allows dynamic point updates and range product queries in $O(\log N)$ per query, with the remaining suffix multiplied by Fibonacci numbers.
- Common Reductions: Maintain the number of ways to fill $N$ teapots with tea or coffee (no two adjacent coffee) under dynamic prefix coffee constraints $a_p = x$ updated online across $Q$ queries.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc418_f`](../../analysis/AtCoder-abc418_f.md) | F - We're teapots | 2496 | Maintain the number of ways to fill $N$ teapots with tea or coffee (no two adjacent coffee) under dynamic prefix coffee ... |
