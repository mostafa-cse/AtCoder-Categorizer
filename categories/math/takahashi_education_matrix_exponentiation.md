# Matrix Exponentiation

**Taxonomy Path**: `Math` > `Matrices` > `Matrix Exponentiation`

## Description
This topic focuses on matrix exponentiation techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: The decimal length d of terms ranges from 1 to 18. Within each block of terms having the same number of digits d, appending term s_i = s_0 + i B transforms running value V as V <- V * 10^d + s_i. The state vector (V, i, 1)^T transitions linearly via a 3x3 matrix T_d. Binary matrix exponentiation allows computing the transition over cnt terms in O(log cnt).
- Common Reductions: Concatenate the first L terms of an arithmetic progression A, A+B, ..., A+(L-1)B into a decimal integer and compute its value modulo M.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc129_f`](../../analysis/AtCoder-abc129_f.md) | F - Takahashi's Basics in Education and Learning | 2621 | Concatenate the first L terms of an arithmetic progression A, A+B, ..., A+(L-1)B into a decimal integer and compute its ... |
