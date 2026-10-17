# Knapsack and Basic Dynamic Programming

**Taxonomy Path**: `Dynamic Programming (DP)` > `Intro to DP` > `Knapsack and Basic Dynamic Programming`

## Description
This topic focuses on knapsack and basic dynamic programming techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Side lengths R, G, B form a non-degenerate triangle iff max(R, G, B) < S / 2 where S = sum A_i. By complementary counting, subtract invalid colorings where some color has sum >= ceil(S / 2). By symmetry, colorings with R >= ceil(S / 2) can be multiplied by 3. If S is even, colorings with two colors equal to S / 2 (and the third 0) are double-counted in 3 * invalid1 and must be added back via PIE. Both counts reduce to 0/1 knapsack dynamic programming.
- Common Reductions: Count the number of ways to paint N integers with Red, Green, or Blue so that the sum of each color can form a non-degenerate triangle.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-tenka1_2019_d`](../../analysis/AtCoder-tenka1_2019_d.md) | Three Colors | 2237 | Count the number of ways to paint N integers with Red, Green, or Blue so that the sum of each color can form a non-degen... |
