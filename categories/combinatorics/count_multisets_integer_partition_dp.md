# Partitions of an Integer, Partition Function and Pentagonal Number Theorem

**Taxonomy Path**: `Combinatorics` > `Partitions` > `Partitions of an Integer, Partition Function and Pentagonal Number Theorem`

## Description
This topic focuses on partitions of an integer, partition function and pentagonal number theorem techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: A partition of n into k parts corresponds to a Young diagram. In the conjugate partition, parts are bounded and adjacent differences are bounded. Alternatively, we can use the standard partition DP where dp[k][n] is the number of partitions of n into k parts with multiplicity <= M. Transitions:
1. Increment all k parts by 1: dp[k][n - k]
2. Add a new part of size 1: dp[k - 1][n - 1]
3. Subtract invalid configurations where the part 1 was repeated > M times: dp[k - 1 - M][n - k].
This yields a 3-term recurrence computable in O(N^2) time.
- Common Reductions: Find the number of multisets of positive integers with sum N such that each element has multiplicity at most M, for each multiset size k from 1 to N. Output the count for each k modulo 998244353.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc221_h`](../../analysis/AtCoder-abc221_h.md) | H - Count Multiset | 2793 | Find the number of multisets of positive integers with sum N such that each element has multiplicity at most M, for each... |
