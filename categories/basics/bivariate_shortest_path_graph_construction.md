# Basic Constructive Algorithms

**Taxonomy Path**: `Basics` > `Greedy and Constructive` > `Basic Constructive Algorithms`

## Description
This topic focuses on basic constructive algorithms techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: A path using i edges of type X and j edges of type Y with direct bridge cost c has length i*x + j*y + c. By building a canonical ladder graph with 101 vertices u_0..u_{100} connected by X-edges and 101 vertices v_{100}..v_0 connected by Y-edges, edge u_i -> v_j can be assigned weight c_{i, j} = max(0, max_{x, y} (d_{x, y} - i*x - j*y)). The construction is valid iff min_{i, j} (i*x + j*y + c_{i, j}) == d_{x, y} for all (x, y).
- Common Reductions: Construct a directed graph with at most 300 vertices whose shortest path distance from S to T equals d_{x, y} whenever edge weights X=x and Y=y, or report Impossible.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc089_c`](../../analysis/AtCoder-arc089_c.md) | E - GraphXY | 2816 | Construct a directed graph with at most 300 vertices whose shortest path distance from S to T equals d_{x, y} whenever e... |
