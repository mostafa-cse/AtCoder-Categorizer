# Knapsack and Basic Dynamic Programming

**Taxonomy Path**: `Dynamic Programming (DP)` > `Intro to DP` > `Knapsack and Basic Dynamic Programming`

## Description
This topic focuses on knapsack and basic dynamic programming techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Let DP[t][k] be the winning probability from turn t with k winning presses so far. At each turn, Takahashi chooses press counts c_1 + ... + c_N = M. Since the winning button is uniformly random, the winning probability is (1/N) sum DP[t+1][k + c_i]. Non-zero presses occur on at most min(N, M) buttons; the optimal choice of positive parts is found via an integer partition knapsack.
- Common Reductions: Sequential decision game with N buttons (1 winner) and T turns of M presses. Takahashi maximizes probability of winning >= K times. Backward induction on turns and presses solved via bounded integer partition knapsack DP.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| `[problem:AtCoder-abc404_f]` | Lost and Pound | 2162 | Sequential decision game with N buttons (1 winner) and T turns of M presses. Takahashi maximizes probability of winning ... |
