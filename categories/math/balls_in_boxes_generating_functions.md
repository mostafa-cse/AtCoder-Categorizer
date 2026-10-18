# Generating Functions

**Taxonomy Path**: `Math` > `Polynomial` > `Generating Functions`

## Description
This topic focuses on generating functions techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Expanding prod (A_i + c_i) expresses the expected product as sum_{m=0}^N [x^m] P(x) * (K^{\underline{m}} / N^m), where P(x) = prod_{i=1}^N (x + A_i) and K^{\underline{m}} is the falling factorial.
- Common Reductions: There are N boxes with A_i balls. In each of K steps, add 1 ball to a uniformly random box. Find the expected value of prod B_i, the product of final ball counts, modulo 998244353.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc231_g`](../../analysis/AtCoder-abc231_g.md) | G. Balls in Boxes | 2606 | There are N boxes with A_i balls. In each of K steps, add 1 ball to a uniformly random box. Find the expected value of p... |
