# Halls Theorem

**Taxonomy Path**: `Graph Theory` > `Matching` > `Halls Theorem`

## Description
This topic focuses on halls theorem techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Chairs at coordinates <= 0 or >= M+1 satisfy all people. By Hall's Marriage Theorem, the matching deficiency equals max(0, max_S (|S| - |Gamma(S)|)). The unavailable chairs for any subset S form an intersection of forbidden intervals [L_i + 1, R_i - 1], which is a single interval [l + 1, r - 1] with l = max L_i, r = min R_i. Thus deficiency equals max_{0 <= l < r <= M+1} (count(L_i <= l, R_i >= r) - l + r - M - 1). Sweeping l and querying a lazy segment tree over r solves the problem in O((N + M) log M).
- Common Reductions: N people wish to sit in M chairs at 1..M, where person i demands a chair <= L_i or >= R_i. Additional chairs can be placed at arbitrary real coordinates. Find the minimum number of additional chairs needed.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc076_d`](../../analysis/AtCoder-arc076_d.md) | F - Exhausted? | 2824 | N people wish to sit in M chairs at 1..M, where person i demands a chair <= L_i or >= R_i. Additional chairs can be plac... |
