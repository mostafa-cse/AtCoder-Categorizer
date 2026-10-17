# Basic Constructive Algorithms

**Taxonomy Path**: `Basics` > `Greedy and Constructive` > `Basic Constructive Algorithms`

## Description
This topic focuses on basic constructive algorithms techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Any path from (1, 1) to (N, N) is uniquely characterized by its down-step column sequence 1 <= C_1 <= C_2 <= ... <= C_{N-1} <= N. The path sum is P(N, N) + sum_{i=1}^{N-1} D(i, C_i). By setting D(i, C_i) = C(C_i + i - 2, i), the sum equals the exact combinadics rank of the combination, mapping every path to a unique consecutive integer in [0, C(2N-2, N-1) - 1].
- Common Reductions: Exact combinadics rank mapping to grid path sums via independent diagonal difference integration.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc214_d`](../../analysis/AtCoder-arc214_d.md) | Distinct Sum Grid Path | 2205 | Exact combinadics rank mapping to grid path sums via independent diagonal difference integration.... |
