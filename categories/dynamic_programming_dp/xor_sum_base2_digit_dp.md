# Digit DP

**Taxonomy Path**: `Dynamic Programming (DP)` > `Digit DP` > `Digit DP`

## Description
This topic focuses on digit dp techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Since a + b = (a xor b) + 2(a and b) and (a xor b) and (a and b) = 0, every valid pair (u, v) corresponds bijectively to a choice of base-2 digits c_i in {0, 1, 2} such that sum c_i 2^i <= N.
- Common Reductions: Count pairs (u, v) with 0 <= u, v <= N such that there exist non-negative integers a, b with a xor b = u and a + b = v, modulo 10^9+7.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc066_b`](../../analysis/AtCoder-arc066_b.md) | D. Xor Sum | 2606 | Count pairs (u, v) with 0 <= u, v <= N such that there exist non-negative integers a, b with a xor b = u and a + b = v, ... |
