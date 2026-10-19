# Generating Functions

**Taxonomy Path**: `Math` > `Polynomial` > `Generating Functions`

## Description
This topic focuses on generating functions techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Let f(x, y) be the bivariate generating function where [x^N y^M] f(x, y) is the count of splendid compositions of N with length M. By PIE on adjacent equal elements, g(x, y) = sum_{i=1}^inf x^i y / (1 + x^i y), so f(x, y) = 1 / (1 - g(x, y)). The sum of lengths is given by d/dy f(x, y)|_{y=1} = P(x) / Q(x)^2, where Q(x) = 1 - sum_{i=1}^inf x^i / (1 + x^i) and P(x) = sum_{i=1}^inf x^i / (1 + x^i)^2. Expanding P(x) and Q(x) via divisor sums takes O(N log N) time, followed by NTT polynomial inversion and multiplication.
- Common Reductions: A sequence of positive integers is splendid if all adjacent terms are distinct. Find the sum of lengths of all splendid sequences whose sum of elements is N modulo 998244353.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc297_h`](../../analysis/AtCoder-abc297_h.md) | Ex - Diff Adjacent | 2855 | A sequence of positive integers is splendid if all adjacent terms are distinct. Find the sum of lengths of all splendid ... |
