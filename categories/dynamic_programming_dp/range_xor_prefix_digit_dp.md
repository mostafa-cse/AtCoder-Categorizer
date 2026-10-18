# Digit DP

**Taxonomy Path**: `Dynamic Programming (DP)` > `Digit DP` > `Digit DP`

## Description
This topic focuses on digit dp techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: The prefix XOR function f(n) depends only on n mod 4: n (if 0), 1 (if 1), n+1 (if 2), and 0 (if 3). For pairs (x, y) = (l-1, r), cases where both variables depend on n reduce to counting pairs (u, v) with u ^ v = K and u < v within 2D rectangular bounds [u_1, u_2] x [v_1, v_2]. Digit DP on bit positions with state (bit, tight_u, tight_v, cmp) evaluates these in O(log(max R)) time.
- Common Reductions: Counting pairs (l, r) with prefix XOR sum f(r) ^ f(l-1) = V reduces via the period-4 property of prefix XORs to 16 arithmetic cases, 4 of which are solved using 2D bitwise Digit DP.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc133_d`](../../analysis/AtCoder-arc133_d.md) | Range XOR | 2658 | Counting pairs (l, r) with prefix XOR sum f(r) ^ f(l-1) = V reduces via the period-4 property of prefix XORs to 16 arith... |
