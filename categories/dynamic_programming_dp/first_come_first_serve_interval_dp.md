# Open and Close Interval Trick

**Taxonomy Path**: `Dynamic Programming (DP)` > `More Tricks` > `Open and Close Interval Trick`

## Description
This topic focuses on open and close interval trick techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: For two problem intervals [L_i, R_i] and [L_j, R_j] with i < j, if R_i >= L_j, they impose contradictory requirements on overlapping elements, so valid PIE configurations consist strictly of disjoint intervals [L_i, R_i]. Uncovered indices have 2 choices, each interval contributes factor (-1).
- Common Reductions: Customers choose arrival A_i (C_i = 0) or departure B_i (C_i = 1). Two choices yield the same permutation iff one can flip C_i from 1 to 0 without changing relative order, which occurs iff interval (A_i, B_i) contains no other entries ('a problem at i'). Using Principle of Inclusion-Exclusion (PIE) over sets of simultaneous problems, each problem at i forces C_j = 0 for j in [L_i, i-1] and C_j = 1 for j in [i, R_i]. Simultaneous problems must be disjoint intervals, leading to an O(N) DP.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc061_c`](../../analysis/AtCoder-agc061_c.md) | First Come First Served | 2697 | Customers choose arrival A_i (C_i = 0) or departure B_i (C_i = 1). Two choices yield the same permutation iff one can fl... |
