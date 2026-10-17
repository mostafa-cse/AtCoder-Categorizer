# Fast Walsh Hadamard Transform (FWHT) and its Variations

**Taxonomy Path**: `Math` > `Convolution` > `Fast Walsh Hadamard Transform (FWHT) and its Variations`

## Description
This topic focuses on fast walsh hadamard transform (fwht) and its variations techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: The total score for column mask C is sum_{u ^ v = C} A[u] * B[v]. Fast Walsh-Hadamard Transform transforms both arrays to Hadamard basis, multiplies point-wise, and inverts back in O(W * 2^W) approx 4.7e6 operations.
- Common Reductions: Given an H x W grid (W <= 18), we can flip any subset of rows and columns. For column flip mask C, row i achieves min(popcount(R_i ^ C), W - popcount(R_i ^ C)). Summing over all rows is an exact XOR convolution of row mask frequencies A and weight array B[mask] = min(popcount(mask), W - popcount(mask)), computed via FWHT in O(W * 2^W) time.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc396_g`](../../analysis/AtCoder-abc396_g.md) | G. Flip Row or Col | 2195 | Given an H x W grid (W <= 18), we can flip any subset of rows and columns. For column flip mask C, row i achieves min(po... |
