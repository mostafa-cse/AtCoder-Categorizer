# Bitmask DP

**Taxonomy Path**: `Dynamic Programming (DP)` > `Bit Related DP` > `Bitmask DP`

## Description
This topic focuses on bitmask dp techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: The cost to bring $K$ chosen elements together and sort them equals the number of inversions between them plus the number of skips required to cluster them adjacent to their median. In a bitmask DP over the set of chosen values, skipping an unchosen element costs $\min(c, K - c)$ where $c = \text{popcount}(mask)$.
- Common Reductions: Find the minimum operations to form a contiguous subsegment containing a permutation of $1 \dots K$. Bitmask DP over subset of chosen elements adds inversion counts and median clustering costs in $O(N 2^K)$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc126_d`](../../analysis/AtCoder-arc126_d.md) | D. Pure Permutation | 2332 | Find the minimum operations to form a contiguous subsegment containing a permutation of $1 \dots K$. Bitmask DP over sub... |
