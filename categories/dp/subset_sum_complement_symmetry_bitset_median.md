# Knapsack and Subset Sum Optimizations

**Taxonomy Path**: `Dynamic Programming (DP)` > `Intro to DP` > `Knapsack and Subset Sum Optimizations`

## Description
This topic focuses on knapsack and subset sum optimizations techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Complementary subset symmetry: each subset $X$ has complement $\bar{X}$ with $\text{sum}(X) + \text{sum}(\bar{X}) = \sum A$. This pairs up the $2^N$ subsets into complementary pairs summing to $T = \sum A$. The upper half of the subset sums consists of the larger element of each pair, all $\ge \lceil T / 2 \rceil$. The median of all non-empty subsets is therefore the smallest achievable subset sum $\ge \lceil T / 2 \rceil$, solved via `std::bitset`.
- Common Reductions: Given $N$ integers $A_1, \dots, A_N$, consider the $2^N - 1$ sums of non-empty subsequences. Find the median of this sorted list.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc020_c`](../../analysis/AtCoder-agc020_c.md) | C. Median Sum | 2259 | Given $N$ integers $A_1, \dots, A_N$, consider the $2^N - 1$ sums of non-empty subsequences. Find the median of this sor... |
