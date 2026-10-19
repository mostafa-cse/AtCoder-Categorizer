# GCD and LCM

**Taxonomy Path**: `Basics` > `Very Basic Math` > `GCD and LCM`

## Description
This topic focuses on gcd and lcm techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: The condition f(S_i / S_{i+1}) = A_i decouples independently across distinct prime factors p! For a fixed prime p, let a_j be the exponent of p in A_j, and s_j be the exponent of p in S_j. Then |s_j - s_{j+1}| = a_j, and gcd(S) = 1 requires min(s_j) = 0. The contribution to the score for prime p is p^{sum s_j}. Since sum a_j <= N * log(max A), we can use DP for each prime p: dp[k][flag] represents the current exponent s_j = k and whether 0 has been reached (flag in {0, 1}). Transitions step by +a_j and -a_j, multiplying by p^k at each step. The final answer is the product of sum dp[k][1] over all prime factors.
- Common Reductions: For rational x = P/Q in lowest terms, f(x) = P * Q. Given sequence A of length N-1, find the sum of scores prod(S_i) modulo 998244353 over all good sequences S where f(S_i / S_{i+1}) = A_i and gcd(S_1, ..., S_N) = 1.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc192_d`](../../analysis/AtCoder-arc192_d.md) | D - Fraction Line | 2722 | For rational x = P/Q in lowest terms, f(x) = P * Q. Given sequence A of length N-1, find the sum of scores prod(S_i) mod... |
