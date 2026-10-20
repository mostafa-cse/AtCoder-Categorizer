# Product Trick

**Taxonomy Path**: `Combinatorics` > `Techniques` > `Product Trick`

## Description
This topic focuses on product trick techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Model the drawing process as a grid walk in the (x, y) plane representing remaining red and blue balls. Different drawing orders can yield the same multiset or sequence of drawn balls. By analyzing the boundary of the reachable region, the distinct output sequences correspond bijectively to valid grid paths avoiding certain forbidden boundaries. The Product Trick / binomial convolution computes the number of non-overlapping configurations.
- Common Reductions: We have A red balls and B blue balls. C balls are drawn from the left and D from the right. Count the number of distinct sequences of colors drawn.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-code_festival_2017_qualb_e`](../../analysis/AtCoder-code_festival_2017_qualb_e.md) | E. Popping Balls | 2937 | We have A red balls and B blue balls. C balls are drawn from the left and D from the right. Count the number of distinct... |
