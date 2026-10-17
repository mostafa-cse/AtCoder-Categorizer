# Min Cost Max Flow (MCMF)

**Taxonomy Path**: `Graph Theory` > `Flow and Min Cut` > `Min Cost Max Flow (MCMF)`

## Description
This topic focuses on min cost max flow (mcmf) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Grid cells form a bipartite graph (L, R) partitioned by (r + c) mod 2. With shifted costs (A_u + A_v + OFFSET >= 0), augmenting path distances are non-decreasing. Augmenting a path of length dist < OFFSET saves (OFFSET - dist) > 0. The moment dist >= OFFSET, any further augmentation yields non-positive gain, giving the global maximum.
- Common Reductions: Place zero or more disjoint dominoes on an H x W grid to maximize the sum of uncovered cells. Uncovered sum equals total sum minus covered sum, so covering adjacent (u, v) yields a net gain of -(A_u + A_v). Shifting edge costs by OFFSET = 2e12 + 5 ensures non-negative edge costs, allowing Primal-Dual MCMF (Dijkstra with Johnson potentials) to find the optimum, terminating when path cost reaches OFFSET.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc407_g`](../../analysis/AtCoder-abc407_g.md) | G. Domino Covering SUM | 2190 | Place zero or more disjoint dominoes on an H x W grid to maximize the sum of uncovered cells. Uncovered sum equals total... |
