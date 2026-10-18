# Min Cost Max Flow (MCMF)

**Taxonomy Path**: `Graph Theory` > `Flow and Min Cut` > `Min Cost Max Flow (MCMF)`

## Description
This topic focuses on min cost max flow (mcmf) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Let d_0 = A_1, d_i = A_{i+1} - A_i for 1 <= i < N. Monotonicity requires d_i >= 0 for all 0 <= i < N. An operation on [L_i, R_i] subtracts 1 from d_{R_i} and adds 1 to d_{L_i - 1}. Negative deficit nodes demand balls, positive nodes supply balls, and node N has infinite supply.
- Common Reductions: Add 1 to given intervals [L_i, R_i] to make array A non-decreasing with minimum total operations. In the difference array, each interval operation moves one unit of value from R_i to L_i - 1, which models directly as Minimum Cost Flow.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc421_g`](../../analysis/AtCoder-abc421_g.md) | G. Increase to make it Increasing | 2410 | Add 1 to given intervals [L_i, R_i] to make array A non-decreasing with minimum total operations. In the difference arra... |
