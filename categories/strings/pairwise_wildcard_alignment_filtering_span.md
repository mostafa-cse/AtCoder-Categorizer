# String Matching using Bitsets

**Taxonomy Path**: `Strings` > `String Matching` > `String Matching using Bitsets`

## Description
This topic focuses on string matching using bitsets techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Three strings $a, b, c$ can be embedded at relative offsets $(0, i, j)$ if and only if all three pairwise overlaps $(a, b)$ at $i$, $(a, c)$ at $j$, and $(b, c)$ at $j - i$ are mutually consistent.
- Common Reductions: Given three strings $a, b, c$ with wildcards '?', find the minimum length of a string containing all three as substrings.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-panasonic2020_e`](../../analysis/AtCoder-panasonic2020_e.md) | E. Three Substrings | 2309 | Given three strings $a, b, c$ with wildcards '?', find the minimum length of a string containing all three as substrings... |
