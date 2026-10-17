# [Problem] Matching Game On A Graph

**Taxonomy Path**: `Game Theory` > `Graph Games` > `[Problem] Matching Game On A Graph`

## Description
This topic focuses on [problem] matching game on a graph techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: A white vertex survives repainting if and only if all of its neighbors are white. If the tree possesses a perfect matching $M$ of size $N/2$, Aoki adopts a symmetric mirror strategy: whenever Takahashi colors vertex $u$, Aoki immediately colors the matched vertex $v$ where $(u, v) \in M$. At the end, every white vertex has an adjacent matched partner colored black, so every white vertex is repainted black and Aoki (Second) wins.
Conversely, if the tree lacks a perfect matching, Takahashi can force a win by repeatedly identifying an unmatched leaf and securing its parent, guaranteeing at least one white vertex with all-white neighbors. Hence, Aoki (Second) wins if and only if the tree has a perfect matching (which requires $N$ even and greedy leaf-parent matching covering all $N$ vertices).
- Common Reductions: Takahashi (white) and Aoki (black) alternately color uncolored vertices of a tree of $N$ vertices ($N \le 10^5$), Takahashi going first. At the end, every white vertex adjacent to at least one black vertex is repainted black. Takahashi wins if any white vertex remains; Aoki wins if all vertices turn black. Determine the winner with optimal play.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc014_d`](../../analysis/AtCoder-agc014_d.md) | D. Black and White Tree | 2266 | Takahashi (white) and Aoki (black) alternately color uncolored vertices of a tree of $N$ vertices ($N \le 10^5$), Takaha... |
