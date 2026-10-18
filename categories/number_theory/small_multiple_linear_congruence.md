# Linear Congruence Equation

**Taxonomy Path**: `Number Theory` > `Modular Arithmetic` > `Linear Congruence Equation`

## Description
This topic focuses on linear congruence equation techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Because K <= 10^9, the number of digits added is at most 10. For small digit lengths or small counts of digit A or B, the congruence 10^d X + Y == 0 (mod K) reduces to linear congruences solvable by Extended GCD, or BFS on remainder states modulo K.
- Common Reductions: Given K <= 10^9, find the smallest positive multiple of K whose decimal representation contains only the digits A and B.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc423_g`](../../analysis/AtCoder-abc423_g.md) | G - Small Multiple 2 | 2625 | Given K <= 10^9, find the smallest positive multiple of K whose decimal representation contains only the digits A and B.... |
