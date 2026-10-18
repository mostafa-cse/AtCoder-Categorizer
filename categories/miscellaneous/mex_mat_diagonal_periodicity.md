# Invariants and Monovariants

**Taxonomy Path**: `Miscellaneous` > `Techniques` > `Invariants and Monovariants`

## Description
This topic focuses on invariants and monovariants techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: For all i, j >= 4 (1-indexed), the values along each diagonal are invariant: a_{i,j} = a_{i-1,j-1}. Thus the matrix values stabilize into constant diagonals after the 4th row and 4th column.
- Common Reductions: An N x N matrix has entries in {0, 1, 2}. The first row and column are given. Remaining entries satisfy a_{i,j} = mex(a_{i-1,j}, a_{i,j-1}). Count the total occurrences of 0, 1, and 2 in the entire matrix for N <= 5 * 10^5.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc107_e`](../../analysis/AtCoder-arc107_e.md) | E. Mex Mat | 2604 | An N x N matrix has entries in {0, 1, 2}. The first row and column are given. Remaining entries satisfy a_{i,j} = mex(a_... |
