# Sum Over Subsets DP (SOS DP)

**Taxonomy Path**: `Dynamic Programming (DP)` > `Bit Related DP` > `Sum Over Subsets DP (SOS DP)`

## Description
This topic focuses on sum over subsets dp (sos dp) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: An element A_i can only be used if A_i | M. For each prime factor p_j, the LCM reaches the exact power p_j^{e_j} iff at least one chosen element has exponent e_j. With k <= 15 distinct prime powers, submask counts F(S) = sum_{T subseteq S} cnt[T] are computed in O(k * 2^k) via SOS DP. By inclusion-exclusion, the number of full-OR subsets is sum_{S} (-1)^{k - |S|} 2^{F(S)}.
- Common Reductions: Find the number of non-empty subsequences with LCM equal to M. Factor M into distinct prime powers p_j^{e_j} (at most k <= 15 prime powers). Filter elements to those dividing M, mapping each to a k-bit mask indicating which prime power exponents match e_j. Count subsequences whose bitwise OR is full mask (1<<k)-1 using SOS DP and Principle of Inclusion-Exclusion.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc349_f`](../../analysis/AtCoder-abc349_f.md) | I. Subsequence LCM | 2169 | Find the number of non-empty subsequences with LCM equal to M. Factor M into distinct prime powers p_j^{e_j} (at most k ... |
