# Broken Profile DP / Plug DP

**Taxonomy Path**: `Miscellaneous` > `General` > `Broken Profile DP / Plug DP`

## Description
This topic focuses on broken profile dp / plug dp techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Since $H \times W \le 200$, transposing ensures $W \le 14$. The frontier profile of the last $W$ assigned cells completely determines validity of subsequent cell assignments.
- Common Reductions: Given an $H \times W$ grid ($HW \le 200$) with characters in $\{1, 2, 3, ?\}$, count valid 3-colorings where adjacent cells differ, modulo 998244353.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc379_g`](../../analysis/AtCoder-abc379_g.md) | G. Count Grid 3-coloring | 2304 | Given an $H \times W$ grid ($HW \le 200$) with characters in $\{1, 2, 3, ?\}$, count valid 3-colorings where adjacent ce... |
