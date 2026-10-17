# Randomized Algorithms

**Taxonomy Path**: `Miscellaneous` > `Randomized` > `Randomized Algorithms`

## Description
This topic focuses on randomized algorithms techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: If a majority remainder modulo M exists, it occupies at least floor(N/2) + 1 elements (> 50%). Two randomly selected distinct elements both belong to the majority group with probability > 1/4. When they do, M divides |A_i - A_j|. Factoring |A_i - A_j| and verifying each odd prime factor (and 4) across all N elements takes O(N) per test. Repeating for 40 random pairs reduces failure probability to (3/4)^{40} < 10^{-5}.
- Common Reductions: Given N <= 5000 distinct integers, find an integer M in [3, 10^9] such that some remainder modulo M occurs strictly more than N/2 times. Randomly sampling pairs and testing prime factors of their differences identifies M with high probability.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc272_g`](../../analysis/AtCoder-abc272_g.md) | G. Yet Another mod M | 2187 | Given N <= 5000 distinct integers, find an integer M in [3, 10^9] such that some remainder modulo M occurs strictly more... |
