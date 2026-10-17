# Fast Walsh Hadamard Transform (FWHT) and its Variations

**Taxonomy Path**: `Math` > `Convolution` > `Fast Walsh Hadamard Transform (FWHT) and its Variations`

## Description
This topic focuses on fast walsh hadamard transform (fwht) and its variations techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Each query $(X_i, Y_i)$ applies an elementary $2 \times 2$ shear matrix along dimension $X_i$ on the $N$-dimensional hypercube. Transformations acting on distinct bit dimensions commute; matrix multiplication accumulates operations per bit $X$, which are then applied via the FWHT butterfly algorithm in $O(Q + N 2^N)$.
- Common Reductions: Given an array of size $2^N$ and $Q$ operations of the form $(x_i, y_i)$ which add $A_u$ to $A_v$ for indices whose $x_i$-th bit differs, compute the final array modulo 998244353.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc151_d`](../../analysis/AtCoder-arc151_d.md) | D. Binary Representations and Queries | 2282 | Given an array of size $2^N$ and $Q$ operations of the form $(x_i, y_i)$ which add $A_u$ to $A_v$ for indices whose $x_i... |
