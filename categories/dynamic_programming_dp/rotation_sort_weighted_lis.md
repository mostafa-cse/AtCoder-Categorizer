# Longest Increasing Subsequence (LIS)

**Taxonomy Path**: `Dynamic Programming (DP)` > `Classic DP` > `Longest Increasing Subsequence (LIS)`

## Description
This topic focuses on longest increasing subsequence (lis) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: The elements that never move must form an increasing subsequence. For any element between two preserved elements P_j < P_i: if P_k < P_j, it must move left (cost B); if P_k > P_i, it must move right (cost A); otherwise, it moves at cost min(A, B). This cost decomposes into (i - 1 - j) * min(A, B) plus |A - B| times the count of elements on the heavier side.
- Common Reductions: Given a permutation P of 1 to N, pay A to cyclic shift any subarray [l, r] left (moving p_l to the right), or pay B to shift [l, r] right (moving p_r to the left). Find the minimum cost to sort P.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc032_d`](../../analysis/AtCoder-agc032_d.md) | D. Rotation Sort | 2602 | Given a permutation P of 1 to N, pay A to cyclic shift any subarray [l, r] left (moving p_l to the right), or pay B to s... |
