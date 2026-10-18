# Generating Functions

**Taxonomy Path**: `Math` > `Polynomial` > `Generating Functions`

## Description
This topic focuses on generating functions techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: During column processing, track the number of rows $j$ that still need 2 points. The number of rows that still need 1 point is uniquely determined by $\text{remaining\_sum} - 2j$. When placing a column with sum 0, 1, or 2, choose which rows receive 1 or 2 points, updating $j$. Transition coefficients are simple binomial coefficients representing choices among available rows.
- Common Reductions: Count $N \times N$ matrices with entries in $\{0, 1, 2\}$ having prescribed row sums $R_i \in \{0, 1, 2\}$ and column sums $C_j \in \{0, 1, 2\}$. If $\sum R_i \ne \sum C_j$, the answer is 0. Since rows and columns are symmetric with respect to their sum values, count the number of rows with sum 1 ($r_1$) and sum 2 ($r_2$), and process columns sequentially.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc273_g`](../../analysis/AtCoder-abc273_g.md) | G. Row Column Sums 2 | 2521 | Count $N \times N$ matrices with entries in $\{0, 1, 2\}$ having prescribed row sums $R_i \in \{0, 1, 2\}$ and column su... |
