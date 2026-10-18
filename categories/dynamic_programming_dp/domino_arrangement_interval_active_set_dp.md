# Open and Close Interval Trick

**Taxonomy Path**: `Dynamic Programming (DP)` > `More Tricks` > `Open and Close Interval Trick`

## Description
This topic focuses on open and close interval trick techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Let $C_k$ be the colors available for both cells $k-1$ and $k$. DP recurrence states: $S_k = S_{k-1} + |C_k| S_{k-2} - \sum_{c \in C_k} \mathrm{dp}[k-2][c]$. Because $k$ only interacts with $k-2$, even and odd $k$ form two completely separate parity systems. In each system, advancing $k \to k+2$ applies a global affine transformation $T_{new} = S_{k-4} - T_{old}$ to active colors, which is maintained in $O(1)$ time with global slope/intercept tags while inserting/removing colors at their interval endpoints ($2M$ events total).
- Common Reductions: Count the number of valid cell colorings where every colored cell is part of an identical 2-cell domino of color $c \in [1, M]$, given color availability intervals $[L_c, R_c]$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc435_g`](../../analysis/AtCoder-abc435_g.md) | G - Domino Arrangement | 2519 | Count the number of valid cell colorings where every colored cell is part of an identical 2-cell domino of color $c \in ... |
