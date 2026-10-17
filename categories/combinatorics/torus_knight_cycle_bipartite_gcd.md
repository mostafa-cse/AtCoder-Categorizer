# Large Factorials and Binomial Coefficients

**Taxonomy Path**: `Combinatorics` > `Factorials and Binomial Coefficients (nCr)` > `Large Factorials and Binomial Coefficients`

## Description
This topic focuses on large factorials and binomial coefficients techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: The row move $(i - 2) \bmod H$ is deterministic. If $H$ is even, odd rows are unreachable, yielding 0 tours. If $H$ is odd, row visits are periodic. When $W$ is odd, all cells in row $r$ must choose the same direction, requiring $\gcd((2a - H) \bmod W, W) = 1$. When $W$ is even, direction is uniform on $2H$ buckets $(r, c \bmod 2)$, requiring $\gcd((a - H) \bmod (W/2), W/2) = 1$.
- Common Reductions: Count the number of tours visiting every cell of an $H \times W$ torus chessboard under knight moves $(i-2, j \pm 1)$. If $H$ is even, answer is 0. If $H$ is odd, row visits are periodic and column shifts must be coprime to $W$ or $W/2$, solved in $O(H \log W)$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc202_b`](../../analysis/AtCoder-arc202_b.md) | B. Tour | 2340 | Count the number of tours visiting every cell of an $H \times W$ torus chessboard under knight moves $(i-2, j \pm 1)$. I... |
