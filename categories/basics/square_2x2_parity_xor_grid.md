# The XOR Trick

**Taxonomy Path**: `Basics` > `Bit Manipulation` > `The XOR Trick`

## Description
This topic focuses on the xor trick techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Any subgrid from (i, i) to (j, j) contains cell (r, c) iff it contains (c, r). Thus only the sum a_{i,j} + a_{j,i} (mod 2) matters. Setting a_{i,i} = x_i, the 2x2 square condition forces a_{i, i+1} + a_{i+1, i} = x_i ^ x_{i+1}, the 3x3 square condition forces a_{i, i+2} + a_{i+2, i} = x_{i+1}, and larger squares force a_{i, j} + a_{j, i} = 0 for j - i >= 3. This reduces the problem to solving a linear system of XOR constraints on x_1..x_N using potential DSU. Unconstrained off-diagonal pairs (i, j) with i < j where neither (i, j) nor (j, i) was given contribute an independent factor of 2^{K_none}.
- Common Reductions: In an N x N grid (N <= 10^5), M cells have predetermined values in {0, 1}. Fill the remaining cells so that for all 1 <= i < j <= N, the subgrid from (i, i) to (j, j) contains an even number of 1s. Find the number of valid configurations modulo 998244353.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-caddi2018_d`](../../analysis/AtCoder-caddi2018_d.md) | F - Square | 2723 | In an N x N grid (N <= 10^5), M cells have predetermined values in {0, 1}. Fill the remaining cells so that for all 1 <=... |
