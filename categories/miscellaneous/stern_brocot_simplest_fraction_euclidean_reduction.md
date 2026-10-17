# Stern-Brocot Tree and Rational Approximation

**Taxonomy Path**: `Miscellaneous` > `General` > `Stern-Brocot Tree and Rational Approximation`

## Description
This topic focuses on stern-brocot tree and rational approximation techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: If floor(A/B) + 1 < C/D, an integer exists strictly between the fractions, so q = 1. Otherwise, floor(A/B) = k. Subtracting k gives 0 <= (A - kB)/B < p'/q < (C - kD)/D <= 1. Inverting the inequality yields D/(C - kD) < q/p' < B/(A - kB), which recursively asks for the simplest fraction (minimal numerator q) strictly between the inverted bounds.
- Common Reductions: Given positive integers A, B, C, D with A/B < C/D, find the smallest denominator q such that there exists an integer p with A/B < p/q < C/D. Solved in O(log(min(B, D))) using the Stern-Brocot Euclidean mediant reduction / continued fractions.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc408_g`](../../analysis/AtCoder-abc408_g.md) | G. A/B < p/q < C/D | 2167 | Given positive integers A, B, C, D with A/B < C/D, find the smallest denominator q such that there exists an integer p w... |
