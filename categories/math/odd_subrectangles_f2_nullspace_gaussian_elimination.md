# Gaussian Elimination Modulo 2

**Taxonomy Path**: `Math` > `Linear Algebra` > `Gaussian Elimination Modulo 2`

## Description
This topic focuses on gaussian elimination modulo 2 techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Represent row and column choices as binary vectors $\mathbf{x} \in \mathbb{F}_2^N, \mathbf{y} \in \mathbb{F}_2^M$. The sum is $\mathbf{x}^T A \mathbf{y} \pmod 2$. For any row combination with $\mathbf{x}^T A \ne \mathbf{0}$, exactly $2^{M - 1}$ choices of $\mathbf{y}$ yield an odd sum. The number of $\mathbf{x}$ with $\mathbf{x}^T A = \mathbf{0}$ is $2^{N - r}$, where $r = \text{rank}(A)$ over $\mathbb{F}_2$.
- Common Reductions: Count pairs of row subset $A$ and column subset $B$ whose intersection has an odd sum in a binary matrix $a_{ij}$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-yahoo_procon2019_qual_e`](../../analysis/AtCoder-yahoo_procon2019_qual_e.md) | E. Odd Subrectangles | 2585 | Count pairs of row subset $A$ and column subset $B$ whose intersection has an odd sum in a binary matrix $a_{ij}$.... |
