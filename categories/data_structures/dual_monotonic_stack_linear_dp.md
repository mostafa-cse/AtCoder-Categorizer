# Segment Tree with Lazy Propagation

**Taxonomy Path**: `Data Structures (DS)` > `Segment Tree` > `Segment Tree with Lazy Propagation`

## Description
This topic focuses on segment tree with lazy propagation techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: The product sum over partition blocks factors into $(\max(B) - \min(B)) dp[j] = \max(B) dp[j] - \min(B) dp[j]$, decoupling the maximum and minimum contributions independently.
- Common Reductions: Given array $A$, compute $\sum \prod (\max(B_i) - \min(B_i))$ over all $2^{N-1}$ compositions of $A$ into contiguous blocks, modulo 998244353.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc234_g`](../../analysis/AtCoder-abc234_g.md) | G. Divide a Sequence | 2306 | Given array $A$, compute $\sum \prod (\max(B_i) - \min(B_i))$ over all $2^{N-1}$ compositions of $A$ into contiguous blo... |
