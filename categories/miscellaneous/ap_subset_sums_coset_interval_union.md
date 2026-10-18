# Interval Set

**Taxonomy Path**: `Miscellaneous` > `General` > `Interval Set`

## Description
This topic focuses on interval set techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Choosing k elements from arithmetic progression A_i = X + (i-1)D yields sums S = k X + D * r, where r spans continuously across all integers in [k(k-1)/2, k(2N-k-1)/2]. Modulo D, values of S belong to independent cosets (k X) mod D. Within each coset, the set of achievable multiples q + r forms a union of integer intervals.
- Common Reductions: Subset sums of an arithmetic progression partition into independent cosets modulo D. For a fixed subset size k, achievable sums form a contiguous interval of multiples. Merging overlapping intervals per coset counts distinct sums in O(N log N) time.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc147_f`](../../analysis/AtCoder-abc147_f.md) | F. Sum Difference | 2393 | Subset sums of an arithmetic progression partition into independent cosets modulo D. For a fixed subset size k, achievab... |
