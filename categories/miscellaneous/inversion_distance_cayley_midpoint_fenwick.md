# Inversions

**Taxonomy Path**: `Miscellaneous` > `General` > `Inversions`

## Description
This topic focuses on inversions techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Renumbering elements so A = (1, 2, ..., N), the distance dist(A, B) is the standard inversion count of B. If I is odd, no midpoint exists. If I is even, any permutation on the shortest path from A to B with I/2 inversions relative to A satisfies dist(A, C) = dist(B, C) = I/2.
- Common Reductions: Given permutations A and B, find a permutation C equidistant from both in terms of inversion distance. Parity requires total inversion count I(A, B) to be even, and C is constructed on the Cayley shortest path with distance I/2 using a Fenwick Tree.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc043_c`](../../analysis/AtCoder-arc043_c.md) | C. 転倒距離 | 2409 | Given permutations A and B, find a permutation C equidistant from both in terms of inversion distance. Parity requires t... |
