# Knapsack and Basic Dynamic Programming

**Taxonomy Path**: `Dynamic Programming (DP)` > `Intro to DP` > `Knapsack and Basic Dynamic Programming`

## Description
This topic focuses on knapsack and basic dynamic programming techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: When prepending P_i to suffix i+1..N, P_i can be: (1) largest (previous max was at i + D_i); (2) 2nd largest (max was at i + D_i); or (3) smaller than both. The 3rd case preserves the relative max and 2nd-max positions, valid iff D_i == D_{i+1}, which multiplies all existing states by N - i - 2. If D_i != D_{i+1}, all other states become 0.
- Common Reductions: Count permutations P of 1..N such that in every suffix P[i..N], the distance between the largest and 2nd largest element is D_i. Process elements from right to left (suffix i from N-2 down to 0) tracking only the index a of the maximum element. Multiplications by N - i - 2 and point updates are efficiently handled via a Lazy Segment Tree.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc457_f`](../../analysis/AtCoder-abc457_f.md) | F. Second Gap | 2167 | Count permutations P of 1..N such that in every suffix P[i..N], the distance between the largest and 2nd largest element... |
