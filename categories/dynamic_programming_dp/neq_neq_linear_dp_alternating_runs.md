# Knapsack and Basic Dynamic Programming

**Taxonomy Path**: `Dynamic Programming (DP)` > `Intro to DP` > `Knapsack and Basic Dynamic Programming`

## Description
This topic focuses on knapsack and basic dynamic programming techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Because adjacent duplicates $A_k = A_{k+1}$ can never both be deleted, any valid $j$ must have $j \ge last\_dup$. Furthermore, an alternating sequence $a, b, a, b \dots$ has only 2 distinct values. By tracking $alt\_len[i]$, the start of the alternating suffix ending at $i$ is $i - alt\_len[i] + 1$. Thus, every $j \le i - alt\_len[i]$ has $\ge 3$ distinct values! Transitions for $j \le i - 3$ reduce to range sum $\max(0, last\_dup) \le j \le \min(i - 3, i - alt\_len[i])$.
- Common Reductions: Count reachable subsets of remaining elements when deleting $y$ from three consecutive elements $(x, y, z)$ with $x \ne y$ and $y \ne z$. An internal segment $A[j+1 \dots i-1]$ can be completely deleted leaving $A[j]$ and $A[i]$ adjacent iff: for $i - j = 1$ (always); for $i - j = 2$ (iff $A[j] \ne A[j+1] \ne A[i]$); and for $i - j \ge 3$ (iff $A[j \dots i]$ has no adjacent duplicates AND contains at least 3 distinct values).

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc128_d`](../../analysis/AtCoder-arc128_d.md) | D. Neq Neq | 2554 | Count reachable subsets of remaining elements when deleting $y$ from three consecutive elements $(x, y, z)$ with $x \ne ... |
