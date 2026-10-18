# Contribution Technique

**Taxonomy Path**: `Combinatorics` > `Techniques` > `Contribution Technique`

## Description
This topic focuses on contribution technique techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: In Kruskal's algorithm on the line with edges between |i - j| <= K, sorting A allows computing the MST weight as sum_{v=1}^{N-1} (A_{v+1} - A_v) (c(v) - 1) + A_1 (N - 1), where c(v) is the number of connected components formed by vertices with values <= A_v. The number of gaps between consecutive placed vertices exceeding K follows hypergeometric/stars-and-bars counting, with probability C(N-K, v)/C(N, v) per gap.
- Common Reductions: Represent MST weight as sum of (A_{v+1} - A_v) (c(v) - 1). For vertices placed on a line, components using edges of span <= K correspond to clusters separated by index gaps > K. Linearity of expectation and stars-and-bars evaluate the total weight in O(N log N) time.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc167_c`](../../analysis/AtCoder-arc167_c.md) | C. MST on Line++ | 2388 | Represent MST weight as sum of (A_{v+1} - A_v) (c(v) - 1). For vertices placed on a line, components using edges of span... |
