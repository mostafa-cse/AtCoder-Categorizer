# Principle of Inclusion and Exclusion (PIE)

**Taxonomy Path**: `Combinatorics` > `Inclusion Exclusion` > `Principle of Inclusion and Exclusion (PIE)`

## Description
This topic focuses on principle of inclusion and exclusion (pie) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Because rooks of different colors attack along unobstructed lines, no row or column can contain both black and white rooks. Thus, black rooks occupy a subgrid of $r_1$ rows and $c_1$ columns, and white rooks occupy a subgrid of $r_2$ rows and $c_2$ columns, where the row subsets and column subsets are mutually disjoint: $r_1 + r_2 \le N$ and $c_1 + c_2 \le M$.
Let $f(R, C, K)$ denote the number of ways to place $K$ rooks on an $R \times C$ board such that every row and column has at least one rook. By 2D Principle of Inclusion and Exclusion (PIE): $f(R, C, K) = \sum_{i=0}^R \sum_{j=0}^C (-1)^{i+j} \binom{R}{i} \binom{C}{j} \binom{(R - i)(C - j)}{K}$. Precomputing $f$ and summing over disjoint row/col choices gives the total count.
- Common Reductions: Place $B$ black rooks and $W$ white rooks on an $N \times M$ grid ($N, M \le 50$) such that no black rook attacks any white rook (rooks attack horizontally/vertically unobstructed). Find the number of valid placements modulo 998244353.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc242_f`](../../analysis/AtCoder-abc242_f.md) | F. Black and White Rooks | 2268 | Place $B$ black rooks and $W$ white rooks on an $N \times M$ grid ($N, M \le 50$) such that no black rook attacks any wh... |
