# Contribution Technique

**Taxonomy Path**: `Combinatorics` > `Techniques` > `Contribution Technique`

## Description
This topic focuses on contribution technique techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: For any vertex v at depth d_v (root has depth 1), operations choosing vertices outside the 1-to-v path do not affect v's state. On the path of length d_v, all nodes are chosen uniformly until all d_v nodes are collected. By symmetry, the expected number of times vertex v is selected is exactly the d_v-th harmonic number H_{d_v} = sum_{i=1}^{d_v} 1/i.
- Common Reductions: Compute the expected number of operations to turn all vertices good by repeatedly selecting bad vertices uniformly at random. By Linearity of Expectation, sum the expected selection count of each individual vertex, which reduces to the classic Coupon Collector's Problem.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc150_d`](../../analysis/AtCoder-arc150_d.md) | D. Removing Gacha | 2407 | Compute the expected number of operations to turn all vertices good by repeatedly selecting bad vertices uniformly at ra... |
