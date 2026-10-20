# DP on Trees and DAGs

**Taxonomy Path**: `Dynamic Programming (DP)` > `Dp on Different Structures` > `DP on Trees and DAGs`

## Description
This topic focuses on dp on trees and dags techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: The visibility vector C corresponds to the gap depths of the Cartesian tree of H. Removing the minimum element replaces two adjacent maximums x with x - 1, preserving the invariant sum_{i=0}^N 2^{-C_i} = 1. Thus 2^{-C_0} + 2^{-C_N} = 1 - sum_{i=1}^{N-1} 2^{-C_i}. Writing the remainder in binary yields at most 2 candidates for (C_0, C_N). For each candidate, verify and reconstruct the Cartesian tree using a stack in O(N) time. The number of permutations matching a Cartesian tree is N! / prod_v S_v, where S_v is subtree size.
- Common Reductions: Given C_1, ..., C_{N-1} where C_x is the number of buildings visible from gap x + 0.5, count permutations of heights (H_1, ..., H_N) matching these counts modulo 998244353.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc230_c`](../../analysis/AtCoder-arc230_c.md) | C. Buildings | 2947 | Given C_1, ..., C_{N-1} where C_x is the number of buildings visible from gap x + 0.5, count permutations of heights (H_... |
