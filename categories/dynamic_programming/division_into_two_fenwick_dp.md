# DP Optimization using Data Structures [Some Practice Problems]

**Taxonomy Path**: `Dynamic Programming (DP)` > `DP Optimizations` > `DP Optimization using Data Structures [Some Practice Problems]`

## Description
This topic focuses on dp optimization using data structures [some practice problems] techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Only the position of the last element in the other set matters. Valid transitions from $dpX$ to $dpY$ require $S_j \le S_{k+1} - B$, corresponding to a binary search prefix on the Fenwick tree. Clearing the DP data structure takes $O(1)$ amortized or reset.
- Common Reductions: Partition a sorted set $S_1 < S_2 < \dots < S_N$ into sets $X$ and $Y$ with minimum differences $A$ and $B$. In a prefix $1 \dots k$, if $S_k \in X$, the last element in $Y$ was $S_j$ ($j < k$), and all intervening elements were in $X$. Transitioning $S_{k+1}$ into $Y$ requires $S_{k+1} - S_j \ge B$, which is a prefix sum of valid $j$'s on $dpX$. Adjacent violations ($S_{k+1} - S_k < A$) wipe out all states in $dpX$, which is efficiently maintained using Fenwick trees.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc009_c`](../../analysis/AtCoder-agc009_c.md) | C. Division into Two | 2437 | Partition a sorted set $S_1 < S_2 < \dots < S_N$ into sets $X$ and $Y$ with minimum differences $A$ and $B$. In a prefix... |
