# DP Optimization using Data Structures [Some Practice Problems]

**Taxonomy Path**: `Dynamic Programming (DP)` > `DP Optimizations` > `DP Optimization using Data Structures [Some Practice Problems]`

## Description
This topic focuses on dp optimization using data structures [some practice problems] techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Each position i has an upper bound B_i = min {X_j : i in [L_j, R_j]}. If for some condition max_{i in [L_j, R_j]} B_i < X_j, the answer is 0. Otherwise, conditions with different values X are independent with respect to reaching their maximum: for a fixed X, only positions with B_i = X can achieve X, while other positions must be < X. For each distinct X, we perform an interval DP using a lazy segment tree with range multiplication, range clearing, and point addition.
- Common Reductions: Count sequences A_1, ..., A_N with 0 <= A_i <= M satisfying Q conditions: max_{L_j <= i <= R_j} A_i = X_j, modulo 998244353.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc262_h`](../../analysis/AtCoder-abc262_h.md) | Ex - Max Limited Sequence | 2969 | Count sequences A_1, ..., A_N with 0 <= A_i <= M satisfying Q conditions: max_{L_j <= i <= R_j} A_i = X_j, modulo 998244... |
