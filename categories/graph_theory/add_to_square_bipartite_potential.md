# Min Cost Max Flow (MCMF)

**Taxonomy Path**: `Graph Theory` > `Flow and Min Cut` > `Min Cost Max Flow (MCMF)`

## Description
This topic focuses on min cost max flow (mcmf) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Adding z to a 2x2 square preserves the alternating row sums R_i = sum_j (-1)^{i+j} A_{i,j} and alternating column sums C_j = sum_i (-1)^{i+j} A_{i,j}. Working backwards from bottom-right (r = H-1 down to 1, c = W-1 down to 1), we can eliminate A_{r,c} to 0, which pushes all remaining non-zero values into row 0 and column 0 without changing the alternating sums. After clearing the subgrid, the problem reduces to matching the residual row potentials R_i and column potentials C_j greedily to minimize sum |A_{0,j}| + sum |A_{i,0}| + |A_{0,0}|, which achieves the theoretical lower bound max(sum |R_i|, sum |C_j|).
- Common Reductions: Given an H x W integer grid A, we can choose any 2x2 square and add an arbitrary integer z to all four cells. We want to minimize the sum of absolute values sum |A_{i,j}| and output the resulting grid.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc135_d`](../../analysis/AtCoder-arc135_d.md) | D - Add to Square | 2744 | Given an H x W integer grid A, we can choose any 2x2 square and add an arbitrary integer z to all four cells. We want to... |
