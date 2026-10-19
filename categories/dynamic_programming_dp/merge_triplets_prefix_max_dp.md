# Knapsack and Basic Dynamic Programming

**Taxonomy Path**: `Dynamic Programming (DP)` > `Intro to DP` > `Knapsack and Basic Dynamic Programming`

## Description
This topic focuses on knapsack and basic dynamic programming techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: When adding a block of size a in {1, 2, 3} to a prefix of length s, the maximum among the s + a elements must be the first element of the new block, and there are (s + a - 1)! / s! = prod_{j=1}^{a-1} (s + j) ways to choose and arrange the remaining elements. Thus transition weights are 1 (for a=1), s+1 (for a=2), and (s+1)(s+2) (for a=3).
- Common Reductions: A permutation P of length 3N can be formed by merging N sorted triplets iff its prefix-maximum blocks have sizes in {1, 2, 3} and the count of size-1 blocks c_1 >= count of size-2 blocks c_2. Counting such permutations is solved via DP on prefix length s and difference d = c_1 - c_2 with transitions for adding blocks of size 1, 2, 3.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc043_d`](../../analysis/AtCoder-agc043_d.md) | Merge Triplets | 2708 | A permutation P of length 3N can be formed by merging N sorted triplets iff its prefix-maximum blocks have sizes in {1, ... |
