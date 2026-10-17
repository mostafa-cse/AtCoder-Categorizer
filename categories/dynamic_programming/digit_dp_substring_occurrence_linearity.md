# Digit DP

**Taxonomy Path**: `Dynamic Programming (DP)` > `Digit DP` > `Digit DP`

## Description
This topic focuses on digit dp techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: By linearity of occurrences, the total occurrences of $S$ in numbers $\le N$ equals the sum over all possible total lengths $D$ and starting offsets $p$ of the number of integers matching $S$ at position $p$.
- Common Reductions: Given digit string $S$ of length $\le 16$, compute the total occurrences of $S$ as substrings among all integers in $[L, R]$ for $T$ queries.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc295_f`](../../analysis/AtCoder-abc295_f.md) | F. substr = S | 2306 | Given digit string $S$ of length $\le 16$, compute the total occurrences of $S$ as substrings among all integers in $[L,... |
