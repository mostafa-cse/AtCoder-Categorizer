# Segment Tree (Point Update Range Query)

**Taxonomy Path**: `Data Structures (DS)` > `Segment Tree` > `Segment Tree (Point Update Range Query)`

## Description
This topic focuses on segment tree (point update range query) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: The problem guarantees that the larger path count is at least twice the smaller path count. Taking logarithms transforms product queries into range sum queries: sum_{i=l}^{r-1} log binom(dx_i + dy_i, dx_i). Precomputing log-factorials log(m!) allows O(1) evaluation of log binom, and a Fenwick tree supports O(log N) updates and range comparisons with double precision.
- Common Reductions: Given N checkpoints on a grid, moving only North or East, the number of paths between checkpoint i and i+1 is binom(dx + dy, dx). Compare total path products across query subsegments under point checkpoint modifications. Maintain logarithms of binomial coefficients in a Fenwick tree; compare range sums of log-probabilities.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc035_d`](../../analysis/AtCoder-arc035_d.md) | D. 高橋くんとマラソンコース | 2173 | Given N checkpoints on a grid, moving only North or East, the number of paths between checkpoint i and i+1 is binom(dx +... |
