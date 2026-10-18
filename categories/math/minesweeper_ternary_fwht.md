# Fast Walsh Hadamard Transform (FWHT) and its Variations

**Taxonomy Path**: `Math` > `Convolution` > `Fast Walsh Hadamard Transform (FWHT) and its Variations`

## Description
This topic focuses on fast walsh hadamard transform (fwht) and its variations techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: The adjacency matrix along each 1D coordinate is M = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]. Its exact inverse is M^{-1} = [[0, 1, -1], [-1, 1, -1], [-1, 1, 0]]. The full N-dimensional operator is the Kronecker product of N copies of M.
- Common Reductions: In a ternary hypercube of size 3^N, A_x is the sum of bombs at positions y differing by at most 1 in each ternary coordinate. Recover the bomb configuration B from A.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc288_g`](../../analysis/AtCoder-abc288_g.md) | G. 3^N Minesweeper | 2606 | In a ternary hypercube of size 3^N, A_x is the sum of bombs at positions y differing by at most 1 in each ternary coordi... |
