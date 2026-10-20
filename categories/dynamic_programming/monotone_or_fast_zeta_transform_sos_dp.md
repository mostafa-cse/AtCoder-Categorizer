# Sum Over Subsets DP (SOS DP)

**Taxonomy Path**: `Dynamic Programming (DP)` > `Bit Related DP` > `Sum Over Subsets DP (SOS DP)`

## Description
This topic focuses on sum over subsets dp (sos dp) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Define mask(a) as the number of elements s in S that are subsets of a, computed via SOS DP (Fast Zeta Transform) in O(N 2^N). Let f(l, r) be the number of ways to start at l and end at r. At the base case r = l + 1, f(l, l+1) = mask(l). For aligned blocks of length 2^{d+1}, with L = f(l, l + 2^d) and R = f(l + 2^d, r), paths either pass through l + 2^d (L * R ways) or bypass it with non-zero d-th bit ((R - L) ways), yielding the recurrence f(l, r) = L * R + R - L.
- Common Reductions: Starting with x = 0, repeatedly replace x with (x OR s_i) + 1 using elements from set S. Find the number of ways to reach exactly x = 2^N modulo 998244353.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc198_e`](../../analysis/AtCoder-arc198_e.md) | E - Monotone OR | 2988 | Starting with x = 0, repeatedly replace x with (x OR s_i) + 1 using elements from set S. Find the number of ways to reac... |
