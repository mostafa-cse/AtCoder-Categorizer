# Interval DP / Range DP / Matrix Chain Multiplication (MCM)

**Taxonomy Path**: `Dynamic Programming (DP)` > `Classic DP` > `Interval DP / Range DP / Matrix Chain Multiplication (MCM)`

## Description
This topic focuses on interval dp / range dp / matrix chain multiplication (mcm) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: For any substring $S[i..j]$ and budget of $t$ modifications, the length of the longest palindromic subsequence satisfies the Bellman equation: matching $S[i]$ and $S[j]$ costs $0$ modifications if $S[i] = S[j]$ and $1$ modification if $S[i] \ne S[j]$, yielding $2 + dp(i+1, j-1, t - \mathrm{cost})$.
- Common Reductions: Given a string $S$ of length up to 300 and at most $K$ character modifications, find the maximum possible length of the longest palindromic subsequence of the modified string.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc021_d`](../../analysis/AtCoder-agc021_d.md) | D. Crossing | 2287 | Given a string $S$ of length up to 300 and at most $K$ character modifications, find the maximum possible length of the ... |
