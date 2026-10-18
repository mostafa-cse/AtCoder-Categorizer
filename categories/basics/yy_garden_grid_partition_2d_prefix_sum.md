# 2D Prefix Sum

**Taxonomy Path**: `Basics` > `2D Prefix Sum` > `2D Prefix Sum`

## Description
This topic focuses on 2d prefix sum techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Because fences span the entire grid, every row block must contain identical total 'Y' counts ($2c$), and every column block must contain $2r$ 'Y's. 2D prefix sums allow $O(1)$ verification of all $r \times c$ blocks across all divisors.
- Common Reductions: Partition an $H \times W$ grid into rectangular blocks using horizontal and vertical fences such that every block contains exactly 2 'Y's. If total 'Y's is $K$, then $K$ must be even and the blocks form an $r \times c$ grid with $r \cdot c = K/2$. For each divisor $r$ of $K/2$, the row fence positions are uniquely fixed by row sums of $2c$, and column fences by column sums of $2r$, with intervening empty lines providing multiple fence placement combinations.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc157_d`](../../analysis/AtCoder-arc157_d.md) | D. YY Garden | 2435 | Partition an $H \times W$ grid into rectangular blocks using horizontal and vertical fences such that every block contai... |
