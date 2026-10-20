# Monotonic Stack: All Nearest Smaller Values and All Subarray Maximum/Minimum

**Taxonomy Path**: `Data Structures (DS)` > `Monotonic Data Structures` > `Monotonic Stack: All Nearest Smaller Values and All Subarray Maximum/Minimum`

## Description
This topic focuses on monotonic stack: all nearest smaller values and all subarray maximum/minimum techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Filter operations using a monotonic stack so that prefix lengths strictly increase: q_1 < q_2 < ... < q_M. Any prefix length a_k can be decomposed into c copies of a_{k-1} plus a remainder r = a_k % a_{k-1}. The frequency contribution of length a_k recursively cascades: cnt[k-1] += cnt[k] * c, while the remainder r is binary searched in the prefix array to find the largest a_j <= r and distributed backwards until r < N.
- Common Reductions: Starting with sequence 1, 2, ..., N, repeatedly replace the sequence with its prefix of length q_i (repeating cyclically as needed). Find the count of each number 1 to N in the final sequence.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc003_e`](../../analysis/AtCoder-agc003_e.md) | E - Sequential operations on Sequence | 2983 | Starting with sequence 1, 2, ..., N, repeatedly replace the sequence with its prefix of length q_i (repeating cyclically... |
