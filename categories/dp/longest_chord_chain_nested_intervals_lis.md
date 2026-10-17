# Longest Increasing Subsequence (LIS)

**Taxonomy Path**: `Dynamic Programming (DP)` > `Classic DP` > `Longest Increasing Subsequence (LIS)`

## Description
This topic focuses on longest increasing subsequence (lis) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: A single chord cuts the circle into two arcs and intersects a set of pairwise non-intersecting chords iff their intervals are mutually strictly nested: I_1 subset I_2 subset ... subset I_k. Each given chord (a, b) with a < b corresponds to two circular intervals: [a, b] and [b, a + 2N]. A set of chords can be intersected simultaneously iff their chosen intervals form a nested chain. Sorting all 2N intervals by right endpoint R in descending order (with ties broken by L ascending) reduces finding the maximum nested chain to finding the Longest Increasing Subsequence (LIS) on the left endpoints L.
- Common Reductions: Select a subset of pairwise non-intersecting circle chords such that a single newly added chord can intersect as many of them as possible.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc410_g`](../../analysis/AtCoder-abc410_g.md) | Longest Chord Chain | 2242 | Select a subset of pairwise non-intersecting circle chords such that a single newly added chord can intersect as many of... |
