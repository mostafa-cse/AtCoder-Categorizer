# Binary Lifting and LCA

**Taxonomy Path**: `Graph Theory` > `Lowest Common Ancestor (LCA)` > `Binary Lifting and LCA`

## Description
This topic focuses on binary lifting and lca techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: A jump of length 2^d from u splits into a jump of length 2^{d-1} from u and a jump of length 2^{d-1} from f^{2^{d-1}}(u). Thus, any interval update on tree/functional paths decomposes dyadically and propagates downwards like a segment tree on powers of two.
- Common Reductions: Ball passing game on functional graph where each ball at node j visits f^1(j), f^2(j), ..., f^K(j). By linearity of expectation, each node i receives B_j / K whenever f^x(j) = i. Decomposing paths of length K into dyadic power-of-two jump intervals allows assigning tags to binary lifting intervals and pushing them down from 2^d to 2^{d-1} in O(N log K) time.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc310_g`](../../analysis/AtCoder-abc310_g.md) | Takahashi Takahashi | 2696 | Ball passing game on functional graph where each ball at node j visits f^1(j), f^2(j), ..., f^K(j). By linearity of expe... |
