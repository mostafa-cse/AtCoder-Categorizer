# Invariants and Monovariants

**Taxonomy Path**: `Miscellaneous` > `Techniques` > `Invariants and Monovariants`

## Description
This topic focuses on invariants and monovariants techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: By antidiagonal reflection symmetry across i + j = N + 1, the second half of the path is the reversed and character-inverted (D <-> R) first half. For any cell (i, j) in the upper triangle, the departure direction is strictly periodic with cycle i + j consisting of i Down moves followed by j Right moves. The visit counts after K-1 exercises can be computed by grid flow DP.
- Common Reductions: On an N x N grid, a runner starts at (1, 1) and moves 2N-2 steps to (N, N), always choosing the adjacent cell visited fewer times in past exercises (ties broken by Down). Determine the path of the K-th exercise for N <= 100 and K <= 10^18.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc072_c`](../../analysis/AtCoder-agc072_c.md) | C - Human Exercise | 2984 | On an N x N grid, a runner starts at (1, 1) and moves 2N-2 steps to (N, N), always choosing the adjacent cell visited fe... |
