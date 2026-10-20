# Contribution Technique

**Taxonomy Path**: `Combinatorics` > `Techniques` > `Contribution Technique`

## Description
This topic focuses on contribution technique techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: A sequence CANNOT be rearranged to avoid sum = 0 (mod P) prefixes if and only if either: (1) total sum is divisible by P, or (2) one value v appears as an overwhelming majority such that the other elements cannot buffer the wraps modulo P. Scaling so that majority element is 1, the bad condition is M - sum(P - y_j) >= P, where M is the count of 1s and y_j are other elements. We count the complement using generating functions and contribution technique.
- Common Reductions: Given N and prime P, count sequences A in {1, ..., P-1}^N that can be rearranged so that no prefix sum is divisible by P, modulo 998244353.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc052_c`](../../analysis/AtCoder-agc052_c.md) | C. Nondivisible Prefix Sums | 2936 | Given N and prime P, count sequences A in {1, ..., P-1}^N that can be rearranged so that no prefix sum is divisible by P... |
