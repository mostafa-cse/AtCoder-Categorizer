# DSU / Union Find

**Taxonomy Path**: `Data Structures (DS)` > `Disjoint Set Union (DSU)` > `DSU / Union Find`

## Description
This topic focuses on dsu / union find techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Padding S with 0 at both ends gives array B = [0, S_1..S_M, 0]. The adjacent difference array D_i = (B_{i+1} - B_i) mod 26 tracks state changes: an operation [L, R] increments B_L..B_R, adding +1 to D_{L-1} and -1 to D_R. Thus, values can be transferred along edges (L-1, R). Furthermore, B is a palindrome iff D_i + D_{M-i} == 0 mod 26 for all i, equivalent to allowing transfers between i and M-i. In the resulting graph, values can be redistributed within each connected component. A palindrome is possible iff the sum of D_v mod 26 in every connected component is 0.
- Common Reductions: Given string S and N cyclic range increment operations [L_i, R_i] mod 26, determine whether S can be transformed into a palindrome.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-cf17_final_e`](../../analysis/AtCoder-cf17_final_e.md) | E - Combination Lock | 2816 | Given string S and N cyclic range increment operations [L_i, R_i] mod 26, determine whether S can be transformed into a ... |
