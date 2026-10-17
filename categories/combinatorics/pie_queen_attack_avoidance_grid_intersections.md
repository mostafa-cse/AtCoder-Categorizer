# Principle of Inclusion and Exclusion (PIE)

**Taxonomy Path**: `Combinatorics` > `Inclusion Exclusion` > `Principle of Inclusion and Exclusion (PIE)`

## Description
This topic focuses on principle of inclusion and exclusion (pie) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Attacked squares form the union of <= M rows, <= M columns, <= M anti-diagonals (r + c = d), and <= M main-diagonals (r - c = d). The initial non-attacked count from row and column exclusions is (N - |R|) * (N - |C|). For each anti-diagonal, compute its total grid length and subtract previously accounted intersections with R and C. For each main-diagonal, compute its grid length and subtract intersections with R, C, and all anti-diagonals. Since line pairs intersect at most once, total intersections are O(M^2).
- Common Reductions: Count the number of empty squares not attacked by any of M <= 1000 queens in an N x N grid with N <= 10^9.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc377_f`](../../analysis/AtCoder-abc377_f.md) | Avoid Queen Attack | 2232 | Count the number of empty squares not attacked by any of M <= 1000 queens in an N x N grid with N <= 10^9.... |
