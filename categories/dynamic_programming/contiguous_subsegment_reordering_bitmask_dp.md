# Bitmask DP

**Taxonomy Path**: `Dynamic Programming (DP)` > `Bit Related DP` > `Bitmask DP`

## Description
This topic focuses on bitmask dp techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Any partition of B into contiguous pieces of A can be achieved in a single cut-and-rearrange operation costing (X-1)C. Since segments [l..r] can be extended while bits r are not in S, the total number of transitions across all masks is sum_{L=1}^N (N - L + 1) 2^{N-L} = O(N * 2^N) approx 8.8e7 ops, easily running in 0.15s.
- Common Reductions: Partition sequence B into contiguous segments, each matching an unused contiguous subsegment A[l..r]. Mask S tracks elements of A already used; k = popcount(S) indicates the next prefix of B being filled. We iterate over unused contiguous ranges [l..r] in O(N * 2^N) total operations.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc328_g`](../../analysis/AtCoder-abc328_g.md) | G. Cut and Reorder | 2193 | Partition sequence B into contiguous segments, each matching an unused contiguous subsegment A[l..r]. Mask S tracks elem... |
