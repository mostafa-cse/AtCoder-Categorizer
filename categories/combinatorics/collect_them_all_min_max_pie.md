# Principle of Inclusion and Exclusion (PIE)

**Taxonomy Path**: `Combinatorics` > `Inclusion Exclusion` > `Principle of Inclusion and Exclusion (PIE)`

## Description
This topic focuses on principle of inclusion and exclusion (pie) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: The term (-1)^{|S|} * x^{sum_{i in S} C_i} corresponds to the expansion of prod_{i=1}^N (1 - x^{C_i}). The coefficient of x^k in -P(x) directly yields sum_{S: sum C_i = k} (-1)^{|S|+1}. Multiplying by M / k where M = sum C_i produces the exact expected value.
- Common Reductions: Bags contain C_i items of color i. Items are drawn with replacement proportional to count. By Min-Max Inclusion-Exclusion, the expected time to see all N colors is sum_{empty != S} (-1)^{|S|+1} * (sum C_j) / (sum_{i in S} C_i). The polynomial generating function prod_{i=1}^N (1 - x^{C_i}) computes the coefficients of x^W in O(M log^2 M) via divide-and-conquer NTT.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc331_g`](../../analysis/AtCoder-abc331_g.md) | Collect Them All | 2668 | Bags contain C_i items of color i. Items are drawn with replacement proportional to count. By Min-Max Inclusion-Exclusio... |
