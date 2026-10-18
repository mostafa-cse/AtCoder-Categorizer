# POSET ft Dilworth's and Mirsky's Theorem

**Taxonomy Path**: `Graph Theory` > `Partially Ordered Set (POSET)` > `POSET ft Dilworth's and Mirsky's Theorem`

## Description
This topic focuses on poset ft dilworth's and mirsky's theorem techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Construct a poset DAG on vertices $i \in [L, R]$ with directed edges $i \to j$ when $i < j$ and $\operatorname{popcount}(i) < \operatorname{popcount}(j)$. By Dilworth's Theorem, the minimum path cover equals the size of the maximum antichain, which corresponds to choosing elements in $[L, R]$ with non-increasing popcounts. Decomposing $[L, R+1)$ into $O(\log R)$ canonical dyadic intervals $[l, l + 2^c)$ allows DP over popcounts using Sperner's theorem / binomial coefficients in $O(\log^2 R)$ time.
- Common Reductions: Find the minimum maximum label of a sequence on $[L, R]$ where identical values must have strictly increasing popcounts.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc476_g`](../../analysis/AtCoder-abc476_g.md) | G - Increasing Popcount | 2477 | Find the minimum maximum label of a sequence on $[L, R]$ where identical values must have strictly increasing popcounts.... |
