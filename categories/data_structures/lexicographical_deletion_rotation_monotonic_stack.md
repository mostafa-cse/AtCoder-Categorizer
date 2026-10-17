# Monotonic Stack: All Nearest Smaller Values and All Subarray Maximum/Minimum

**Taxonomy Path**: `Data Structures (DS)` > `Monotonic Data Structures` > `Monotonic Stack: All Nearest Smaller Values and All Subarray Maximum/Minimum`

## Description
This topic focuses on monotonic stack: all nearest smaller values and all subarray maximum/minimum techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Rotating the array right by $r \ge 1$ positions requires $r$ operations, bringing $P[N-r]$ to the front. To minimize the leading element, $P[N-r]$ must be chosen as the minimum element in $P[N-K \dots N-1]$. The remaining budget $K - r$ is used greedily via a monotonic stack on the remaining prefix and suffix.
- Common Reductions: Find the lexicographically smallest permutation achievable by at most $K$ operations of deleting the first element or rotating the last element to the front. Evaluates 0 rotations vs optimal suffix minimum rotation via monotonic stack in $O(N)$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc262_f`](../../analysis/AtCoder-abc262_f.md) | F. Erase and Rotate | 2334 | Find the lexicographically smallest permutation achievable by at most $K$ operations of deleting the first element or ro... |
