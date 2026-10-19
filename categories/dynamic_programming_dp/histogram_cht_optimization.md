# Convex Hull Trick (CHT) and Dynamic CHT

**Taxonomy Path**: `Dynamic Programming (DP)` > `Convex Hull Trick (CHT)` > `Convex Hull Trick (CHT) and Dynamic CHT`

## Description
This topic focuses on convex hull trick (cht) and dynamic cht techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Sort and group distinct values: a_1 < a_2 < ... < a_M with accumulated weights c_k = sum C_i for A_i = a_k. In any optimal solution, a prefix of values is raised to a_i. The DP transition to cover the first i values with the last group being [j+1, i] raised to a_i is: dp[i] = min_{j < i} (dp[j] + S_{ac}[j] - S_c[j] * a_i) + X + a_i * S_c[i] - S_{ac}[i], where S_c and S_{ac} are prefix sums of c_k and a_k * c_k. This is of the form min(m_j * x + k_j) where query x = a_i is strictly increasing and slope m_j = -S_c[j] is strictly decreasing. Hence, the Convex Hull Trick (CHT) with a deque computes all transitions in O(M) time.
- Common Reductions: Given N pairs (A_i, C_i). Each element A_i can be incremented at cost C_i per unit. If K distinct values remain in A, pay additional K * X. Find the minimum total cost.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc228_h`](../../analysis/AtCoder-abc228_h.md) | H - Histogram | 2729 | Given N pairs (A_i, C_i). Each element A_i can be incremented at cost C_i per unit. If K distinct values remain in A, pa... |
