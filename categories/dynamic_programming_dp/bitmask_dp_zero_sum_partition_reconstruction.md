# Bitmask DP

**Taxonomy Path**: `Dynamic Programming (DP)` > `Bit Related DP` > `Bitmask DP`

## Description
This topic focuses on bitmask dp techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Let target $T = \frac{\sum A_i}{N}$ (if total not divisible by $N$, impossible). Define net deficits $D_i = A_i - T$. Any valid redistribution partitions children into disjoint zero-sum subsets $\sum_{i \in S_j} D_i = 0$. In each connected component $S_j$, $|S_j| - 1$ operations suffice to balance candies using a star graph rooted at an arbitrary child $r \in S_j$: children with excess first send to $r$, then $r$ sends to children with deficits. Total operations is $\sum (|S_j| - 1) = N - k$, where $k$ is the number of zero-sum subsets. Minimizing operations is equivalent to maximizing $k$. Since $N \le 20$, `dp[mask]` = max zero-sum subsets in `mask` can be computed in $O(N 2^N)$.
- Common Reductions: $N \le 20$ children have candies $A_i$. In one operation, child $x$ can give $z \le A_x$ candies to child $y$. Find the minimum operations to make all children have equal candies, and reconstruct the sequence of transfers.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc432_f`](../../analysis/AtCoder-abc432_f.md) | F. Candy Redistribution | 2273 | $N \le 20$ children have candies $A_i$. In one operation, child $x$ can give $z \le A_x$ candies to child $y$. Find the ... |
