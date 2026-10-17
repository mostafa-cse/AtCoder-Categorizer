# Number Theoretic Transform (NTT)

**Taxonomy Path**: `Math` > `Convolution` > `Number Theoretic Transform (NTT)`

## Description
This topic focuses on number theoretic transform (ntt) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: This is a generalized derangement / rook polynomial problem. For each color c with a balls and b goal positions, the polynomial P_c(x) = sum_{j=0}^{min(a, b)} C(a, j) * C(b, j) * j! * x^j counts placements with j forbidden matches. The product polynomial Q(x) = prod_c P_c(x) = sum r_k x^k represents total ways to choose k forbidden matches across all colors. By the Principle of Inclusion and Exclusion, valid permutations with 0 matches equal sum_{k=0}^N (-1)^k * r_k * (N - k)!, and dividing by N! yields the probability.
- Common Reductions: Find the probability modulo 998244353 that drawing N colored balls without replacement yields zero matches against a target color sequence G.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc462_g`](../../analysis/AtCoder-abc462_g.md) | Completely Wrong | 2232 | Find the probability modulo 998244353 that drawing N colored balls without replacement yields zero matches against a tar... |
