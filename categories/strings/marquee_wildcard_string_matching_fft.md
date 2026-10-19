# String Matching with FFT ft Wildcard Matching

**Taxonomy Path**: `Strings` > `String Matching` > `String Matching with FFT ft Wildcard Matching`

## Description
This topic focuses on string matching with fft ft wildcard matching techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: String matching with wildcards can be evaluated algebraically. Assign each letter A-Z a non-zero integer v(c) in 1..26, and map wildcard '_' to 0. A match occurs at offset k if and only if sum_{i=0}^{W-1} v(P[i]) * (v(P[i]) - v(T[k+i]))^2 = 0. Expanding the square yields three terms: sum v(P[i])^3 - 2 sum v(P[i])^2 v(T[k+i]) + sum v(P[i]) v(T[k+i])^2. Each term is a cross-correlation, which can be computed via NTT polynomial multiplication modulo 998244353 and a second NTT modulo 1004535809 to avoid false positives.
- Common Reductions: Given a pattern P of length W (consisting of uppercase letters and wildcard '_') and a string S of length L, consider repeating S infinitely. We want to find the number of starting positions in a single period where P matches S (wildcard '_' matches any letter).

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc307_h`](../../analysis/AtCoder-abc307_h.md) | H - Marquee | 2750 | Given a pattern P of length W (consisting of uppercase letters and wildcard '_') and a string S of length L, consider re... |
