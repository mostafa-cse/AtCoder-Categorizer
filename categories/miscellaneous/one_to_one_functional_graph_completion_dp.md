# Functional Graphs

**Taxonomy Path**: `Miscellaneous` > `General` > `Functional Graphs`

## Description
This topic focuses on functional graphs techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: The sum $\sum_{|S|=m} \prod_{j \in S} s_j$ is the coefficient $[x^m] \prod_{j=1}^K (1 + s_j x)$. Computing this polynomial in $O(K^2)$ evaluates the cycle contribution across all subset sizes $m$.
- Common Reductions: In a functional graph where each vertex has one outgoing edge $i \to X_i$, each connected component contains exactly one cycle. Known edges partition the graph into fixed cycle components and $K$ rooted tree components with roots having $A_r = -1$. Fixed cycle components contribute $c_{fixed} \times N^K$ to the total component count. New cycles formed by $m$ tree components contribute $(m - 1)! \prod_{j \in S} s_j \times N^{K - m}$, which is evaluated using polynomial DP on tree sizes.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc140_d`](../../analysis/AtCoder-arc140_d.md) | D. One to One | 2443 | In a functional graph where each vertex has one outgoing edge $i \to X_i$, each connected component contains exactly one... |
