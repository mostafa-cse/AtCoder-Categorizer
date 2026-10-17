# Knapsack and Basic Dynamic Programming

**Taxonomy Path**: `Dynamic Programming (DP)` > `Intro to DP` > `Knapsack and Basic Dynamic Programming`

## Description
This topic focuses on knapsack and basic dynamic programming techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Since total wins K <= 10^9 is large while days N <= 2000 is small, invert the DP state: dp[j] is the minimum cumulative wins required to achieve exactly j good days by the current day. Strict inequality w / S_i > dp[j-1] / S_{i-1} requires minimum wins w = floor(dp[j-1] * S_i / S_{i-1}) + 1. If K == sum(a_i), win rate is permanently 1.0, yielding answer 1.
- Common Reductions: Across N days with a_i games on day i, Takahashi wins exactly K total games. Mood strictly increases on days where the cumulative win rate strictly exceeds the previous day. Maximize the number of good days.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc057_b`](../../analysis/AtCoder-arc057_b.md) | 高橋君ゲーム | 2220 | Across N days with a_i games on day i, Takahashi wins exactly K total games. Mood strictly increases on days where the c... |
