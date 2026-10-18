# L-R Flow

**Taxonomy Path**: `Graph Theory` > `Flow and Min Cut` > `L-R Flow`

## Description
This topic focuses on l-r flow techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Every cell not covered by a $1 \times 2$ domino is naturally covered by a $1 \times 1$ tile. Thus, the problem reduces to matching adjacent cells such that every cell marked '2' has degree exactly 1, every cell marked '?' has degree $\le 1$, and '1' has degree 0. In the bipartite grid graph, this is equivalent to circulation with demands / maximum flow with lower and upper bounds (L-R flow).
- Common Reductions: Cover an $H \times W$ grid with $1 \times 1$ and $1 \times 2$ tiles such that every '1' is covered by a $1 \times 1$ tile, every '2' is covered by a $1 \times 2$ tile, and '?' can be covered by either.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc285_g`](../../analysis/AtCoder-abc285_g.md) | G. Tatami | 2566 | Cover an $H \times W$ grid with $1 \times 1$ and $1 \times 2$ tiles such that every '1' is covered by a $1 \times 1$ til... |
