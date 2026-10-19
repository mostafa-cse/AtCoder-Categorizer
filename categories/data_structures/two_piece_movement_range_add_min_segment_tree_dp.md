# Segment Tree with Lazy Propagation

**Taxonomy Path**: `Data Structures (DS)` > `Segment Tree` > `Segment Tree with Lazy Propagation`

## Description
This topic focuses on segment tree with lazy propagation techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: After processing a query at x, one piece is at x while the other is at some square j. Let DP[j] be the minimum cost with the other piece at j. When moving to the next query x' from previous query p: (1) moving the piece at p to x' adds |p - x'| to all DP[j]; (2) moving the other piece from j to x' updates DP[p] with min_j (DP[j] + |j - x'|). Splitting |j - x'| into j <= x' and j > x', this is maintained dynamically using a lazy segment tree storing min(DP[j] - j) and min(DP[j] + j).
- Common Reductions: Two pieces are initially at squares A and B on a line of N squares. For each of Q queries x_i, move one piece to x_i. Minimize the total movement distance.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc073_d`](../../analysis/AtCoder-arc073_d.md) | F - Many Moves | 2867 | Two pieces are initially at squares A and B on a line of N squares. For each of Q queries x_i, move one piece to x_i. Mi... |
