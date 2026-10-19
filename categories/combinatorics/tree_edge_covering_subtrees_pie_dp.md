# Principle of Inclusion and Exclusion (PIE)

**Taxonomy Path**: `Combinatorics` > `Inclusion Exclusion` > `Principle of Inclusion and Exclusion (PIE)`

## Description
This topic focuses on principle of inclusion and exclusion (pie) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: By PIE, instead of requiring every edge to be covered, sum over subsets S of edges that are NOT covered. Removing edges in S splits the tree into connected components of sizes s_1, ..., s_k. A pairing traverses no edge in S iff every component has even size and pairs internally, with (2m-1)!! ways to pair 2m vertices. Each cut edge contributes a factor of -1. A tree knapsack DP computes the sum of PIE weights based on the size of the component containing the current root.
- Common Reductions: Given a tree with N vertices (N even), pair vertices into N/2 pairs. Count pairings such that every edge in the tree is traversed by at least one pair's path, modulo 10^9 + 7.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc101_c`](../../analysis/AtCoder-arc101_c.md) | E. Ribbons on Tree | 2913 | Given a tree with N vertices (N even), pair vertices into N/2 pairs. Count pairings such that every edge in the tree is ... |
