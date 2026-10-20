# Burnside's Lemma / Polya Enumeration Theorem

**Taxonomy Path**: `Miscellaneous` > `General` > `Burnside's Lemma / Polya Enumeration Theorem`

## Description
This topic focuses on burnside's lemma / polya enumeration theorem techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: The set of obtainable sequences is the union of cyclic shift orbits containing at least one palindrome. For an orbit with minimal period d (where d | N), the block of length d must itself be a palindrome of length d, so there are K^{ceil(d / 2)} palindromes of period dividing d. By Mobius inversion / divisor DP, we compute the number of palindromes f(d) with minimal period exactly d. If d is odd, the orbit has size d and contains exactly 1 palindrome, contributing f(d) * d. If d is even, the orbit contains 2 palindromes, contributing f(d) * (d / 2).
- Common Reductions: Takahashi creates a palindrome of length N with elements in {1, ..., K}. Aoki cyclically shifts it any number of times. Count the number of distinct possible final sequences modulo 10^9 + 7.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc064_d`](../../analysis/AtCoder-arc064_d.md) | F. Rotated Palindromes | 2949 | Takahashi creates a palindrome of length N with elements in {1, ..., K}. Aoki cyclically shifts it any number of times. ... |
