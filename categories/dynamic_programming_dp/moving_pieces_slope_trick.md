# Slope Trick

**Taxonomy Path**: `Dynamic Programming (DP)` > `More Tricks` > `Slope Trick`

## Description
This topic focuses on slope trick techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: The total movement cost depends only on the final piece positions b_1 <= b_2 <= ... <= b_N: cost = sum |a_i - b_i|. In the multiset union {a_1..a_N} U {b_1..b_N}, the odd-multiplicity vertices must match {t_1..t_K}. Thus, the multiset of odd-multiplicity elements of b is uniquely determined as C = odd(a) XOR {t_1..t_K}. The remaining N - |C| elements of b can appear with even multiplicity, which corresponds to pairing up the remaining pieces of a to move to the same point at cost a_{v} - a_{u}. We sort a and C and use DP: dp[j][f] is the minimum cost after matching j elements of C, where f in {0, 1} indicates whether an element of a is currently waiting to close a pair.
- Common Reductions: Given N pieces at positions a_1..a_N on an infinite line graph with all edges initially red. Moving a piece flips the color of traversed edges. We want to achieve a target pattern of blue intervals [t_1, t_2], ..., [t_{K-1}, t_K] with minimum total piece movements.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc114_d`](../../analysis/AtCoder-arc114_d.md) | D - Moving Pieces on Line | 2723 | Given N pieces at positions a_1..a_N on an infinite line graph with all edges initially red. Moving a piece flips the co... |
