# Knapsack and Basic Dynamic Programming

**Taxonomy Path**: `Dynamic Programming (DP)` > `Intro to DP` > `Knapsack and Basic Dynamic Programming`

## Description
This topic focuses on knapsack and basic dynamic programming techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Two consecutive values $\ge 2$ in the sequence lock all subsequent values into an identical constant. A sequence avoids locking up to length $i$ if and only if it consists of 1s separated by isolated numbers $\ge 2$, leading to linear DP $dp[i] = dp[i-1] + \sum_{j=0}^{i-3} dp[j]$.
- Common Reductions: Count valid infinite sequences where each value $a_i$ forces the next $a_i$ elements to be identical and stabilizes at step $n$. Two consecutive values $\ge 2$ lock the sequence, yielding a linear DP solved with prefix sums in $O(n)$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc071_d`](../../analysis/AtCoder-arc071_d.md) | F. Infinite Sequence | 2336 | Count valid infinite sequences where each value $a_i$ forces the next $a_i$ elements to be identical and stabilizes at s... |
