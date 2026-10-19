# Exchange Arguments

**Taxonomy Path**: `Miscellaneous` > `Greedy Algorithms` > `Exchange Arguments`

## Description
This topic focuses on exchange arguments techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: This is the classic '01 on Tree' / job sequencing with tree precedence constraints. For any two blocks of vertices A and B, processing A before B has relative advantage determined by the ratio P(A) / C(A) vs P(B) / C(B). The block with the largest ratio must be processed immediately after its parent block is processed. By maintaining a max-heap of components and merging each maximal component into its parent component using DSU, the optimal total cost is obtained.
- Common Reductions: On a tree rooted at 0 with edge probabilities p_i and search times c_i, search vertices starting from the root such that a vertex can only be searched after its parent. Find the optimal search permutation to minimize expected search cost modulo 998244353.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc376_g`](../../analysis/AtCoder-abc376_g.md) | G - Treasure Hunting | 2858 | On a tree rooted at 0 with edge probabilities p_i and search times c_i, search vertices starting from the root such that... |
