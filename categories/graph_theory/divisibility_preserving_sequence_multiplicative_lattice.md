# POSET ft Dilworth's and Mirsky's Theorem

**Taxonomy Path**: `Graph Theory` > `Partially Ordered Set (POSET)` > `POSET ft Dilworth's and Mirsky's Theorem`

## Description
This topic focuses on poset ft dilworth's and mirsky's theorem techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Divisibility preservation a_n | a_m <=> n | m defines a lattice embedding from the divisibility poset of integers into itself. The linear bound constraint a_n <= C * n forces the prime valuations v_p(a_x) to strictly respect the valuation layers of x: for every prime p <= N, if v_p(x) > v_p(y), then v_p(a_x) > v_p(a_y). Thus, each valuation layer {x : v_p(x) = k} must map to values with v_p(a_x) strictly greater than all values in layer k-1.
- Common Reductions: Determine whether a prefix sequence (A_1, ..., A_N) of positive integers can be extended to an infinite sequence satisfying a_n <= C * n and a_n | a_m <=> n | m.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc067_c`](../../analysis/AtCoder-agc067_c.md) | C - Divisibility Homomorphism | 2829 | Determine whether a prefix sequence (A_1, ..., A_N) of positive integers can be extended to an infinite sequence satisfy... |
