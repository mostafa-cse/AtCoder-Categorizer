# Coordinate Compression

**Taxonomy Path**: `Miscellaneous` > `Techniques` > `Coordinate Compression`

## Description
This topic focuses on coordinate compression techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: A ratio gap S_{k+1} / S_k >= 1.01 indicates that no subset sum falls into (S_k, 1.01 S_k). Any two achievable sums s_1 <= s_2 with 100 s_2 < 101 s_1 cannot create a ratio gap between them because their reachable neighborhoods overlap geometrically. Thus, we prune achievable sums by merging any sums within a 1.01 factor! The number of geometrically pruned sums is bounded by O(log_{1.01}(sum A_i)) <= 3600.
- Common Reductions: Given N <= 2 * 10^5 positive integers A_i, consider all non-empty subset sums sorted in increasing order: S_1 < S_2 < ... < S_M. Count the number of indices k such that 101 S_k <= 100 S_{k+1}.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc210_e`](../../analysis/AtCoder-arc210_e.md) | E - Subset Sum Gaps | 2970 | Given N <= 2 * 10^5 positive integers A_i, consider all non-empty subset sums sorted in increasing order: S_1 < S_2 < ..... |
