# Inversions

**Taxonomy Path**: `Miscellaneous` > `General` > `Inversions`

## Description
This topic focuses on inversions techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Right-shifting P by 1 increases inversion count by 2 P_N - (N+1). Summing over all cyclic shifts yields sum I_i = N I_0 + sum_{k=1}^N (k - 1)(2 P_k - (N+1)). Swapping P_x and P_{x+1} changes this sum by exactly 2(P_x - P_{x+1}) in O(1) time.
- Common Reductions: The operation 'reverse prefix of length i and suffix of length N-i' decomposes into a right-shift by i followed by a reversal. After K steps, the distribution of shift amounts modulo N is uniform except at 0 ((N-1)^K +- 1)/N, and odd K incurs a final reversal. Maintaining total inversions under adjacent swaps reduces to maintaining initial inversions I_0 and the shift moment sum S_shift = sum (k-1)(2 P_k - (N+1)), which updates in O(1) per swap query.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc218_e`](../../analysis/AtCoder-arc218_e.md) | Reverse and Reverse | 2705 | The operation 'reverse prefix of length i and suffix of length N-i' decomposes into a right-shift by i followed by a rev... |
