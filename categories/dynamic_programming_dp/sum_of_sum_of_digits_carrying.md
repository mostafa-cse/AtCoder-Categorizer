# Digit DP

**Taxonomy Path**: `Dynamic Programming (DP)` > `Digit DP` > `Digit DP`

## Description
This topic focuses on digit dp techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: For a fixed digit position k, whether A_i + x produces a carry into digit k+1 depends solely on (A_i mod 10^k) + (x mod 10^k) >= 10^k. Sorting array A by A_i mod 10^k reveals that exactly the suffix of elements with the largest A_i mod 10^k generate carries. Thus, the DP state at step k requires only a single integer c in [0, N]: the number of carries propagated from the previous digit position.
- Common Reductions: Find non-negative integer x minimizing sum_{i=1}^N f(A_i + x), where f(v) is the sum of decimal digits. Minimizing sum f(A_i + x) is equivalent to maximizing the total carries, which can be computed via digit-by-digit DP from least to most significant digit, tracking the count of carries sorted by suffix modulo 10^k.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc153_d`](../../analysis/AtCoder-arc153_d.md) | Sum of Sum of Digits | 2664 | Find non-negative integer x minimizing sum_{i=1}^N f(A_i + x), where f(v) is the sum of decimal digits. Minimizing sum f... |
