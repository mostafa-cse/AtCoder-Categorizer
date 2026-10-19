# Open and Close Interval Trick

**Taxonomy Path**: `Dynamic Programming (DP)` > `More Tricks` > `Open and Close Interval Trick`

## Description
This topic focuses on open and close interval trick techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Sort the elements of A. We can build the permutation by inserting elements using the open and close interval trick. Consider the smallest remaining element A[L] and largest remaining element A[R]. If A[L] + A[R] < K, then A[L] cannot be adjacent to any element <= A[R], so A[L] must be placed in a slot bounded by elements already inserted. Large elements create new slots, while small elements consume slots. The number of valid insertion positions at each step is determined purely by the number of currently active intervals S, leading to a greedy product formula in O(N log N) time.
- Common Reductions: Given an array A of N integers and an integer K, count the number of permutations P of A such that P_i + P_{i+1} >= K for all 1 <= i <= N - 1, modulo 998244353.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc148_e`](../../analysis/AtCoder-arc148_e.md) | E - ≥ K | 2785 | Given an array A of N integers and an integer K, count the number of permutations P of A such that P_i + P_{i+1} >= K fo... |
