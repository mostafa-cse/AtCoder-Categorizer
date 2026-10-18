# Segment Tree with Lazy Propagation

**Taxonomy Path**: `Data Structures (DS)` > `Segment Tree` > `Segment Tree with Lazy Propagation`

## Description
This topic focuses on segment tree with lazy propagation techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Inversion count in any range is $inv[1][0] + inv[2][0] + inv[2][1]$. When two segments $L$ and $R$ merge, cross-pairs contribute $L.cnt[x] \times R.cnt[y]$. Applying mapping $P$ permutes the counts and cross-inversion matrices in $O(3^2) = O(1)$ time.
- Common Reductions: Maintain a sequence of values in $\{0, 1, 2\}$ under range substitutions $0 \to S, 1 \to T, 2 \to U$ and range inversion queries. A Lazy Segment Tree maintains counts of 0s, 1s, and 2s, along with the 9 cross-inversion pair counts $inv[x][y]$. Lazy tags represent mapping functions $P: \{0, 1, 2\} \to \{0, 1, 2\}$, which compose via function substitution.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc265_g`](../../analysis/AtCoder-abc265_g.md) | G. 012 Inversion | 2436 | Maintain a sequence of values in $\{0, 1, 2\}$ under range substitutions $0 \to S, 1 \to T, 2 \to U$ and range inversion... |
