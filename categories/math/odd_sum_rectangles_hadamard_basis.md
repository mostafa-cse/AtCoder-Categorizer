# Vector Space and XOR Basis

**Taxonomy Path**: `Math` > `Linear Algebra` > `Vector Space and XOR Basis`

## Description
This topic focuses on vector space and xor basis techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: The 2D prefix sums of the grid modulo 2 can be viewed as evaluating a 2D parity function f(r, c) on a (2^N) x (2^M) grid. The oddness is maximized when each pair of column indices produces an optimal balance of odd/even row differences, reaching the theoretical upper bound (2^{2*max(N,M)} / 4) * (2^min(N,M) * (2^min(N,M) - 1) / 2). This upper bound is constructively achieved using a recursive Hadamard-style fractal construction: start with a 1x1 grid [1] for K=1; for K+1, place the solution of size 2^K - 1 in all four corners, set the center cell (2^K, 2^K) to 1, and fill the rest of the center row and column with 0.
- Common Reductions: In a grid of (2^N - 1) rows and (2^M - 1) columns (N, M <= 10), fill each cell with 0 or 1 to maximize the number of subrectangles with odd sum.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-hitachi2020_e`](../../analysis/AtCoder-hitachi2020_e.md) | E - Odd Sum Rectangles | 2732 | In a grid of (2^N - 1) rows and (2^M - 1) columns (N, M <= 10), fill each cell with 0 or 1 to maximize the number of sub... |
