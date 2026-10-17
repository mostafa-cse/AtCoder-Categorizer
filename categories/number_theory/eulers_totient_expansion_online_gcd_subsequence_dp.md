# Euler's Totient Function / Phi Function

**Taxonomy Path**: `Number Theory` > `Multiplicative Functions` > `Euler's Totient Function / Phi Function`

## Description
This topic focuses on euler's totient function / phi function techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Ans(m) = 2 * Ans(m-1) + sum_{i < m} gcd(A_i, A_m) 2^{i-1}. Using the identity gcd(a, b) = sum_{d | gcd(a, b)} phi(d), the new contribution rewrites as sum_{d | A_m} phi(d) sum_{i < m, d | A_i} 2^{i-1}. Maintaining Sum[d] = sum_{i < m, d | A_i} 2^{i-1} across all divisors d <= 10^5 evaluates the contribution and updates in O(d(A_m)) time per step.
- Common Reductions: Given sequence A of length N <= 5 * 10^5, for each prefix m = 1..N find the sum of sum_{i=1}^{k-1} gcd(B_i, B_{i+1}) over all 2^m - 1 non-empty subsequences modulo 998244353. Adjacent pairs (A_i, A_m) appear in 2^{i-1} subsequences ending at m, allowing an online recurrence via Euler totient expansion.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc185_e`](../../analysis/AtCoder-arc185_e.md) | E. Adjacent GCD | 2185 | Given sequence A of length N <= 5 * 10^5, for each prefix m = 1..N find the sum of sum_{i=1}^{k-1} gcd(B_i, B_{i+1}) ove... |
