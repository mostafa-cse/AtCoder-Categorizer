# Kirchoffs Theorem ft Number of MSTs

**Taxonomy Path**: `Graph Theory` > `Minimum Spanning Tree (MST)` > `Kirchoffs Theorem ft Number of MSTs`

## Description
This topic focuses on kirchoffs theorem ft number of msts techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Forced edges must not form a cycle; if they do, the answer is 0. Otherwise, contract all forced edges using Disjoint Set Union (DSU) to form $K$ components. An optional edge between original vertices translates into an edge between their corresponding contracted components. The number of spanning trees completing the contracted multigraph into a connected tree equals the cofactor determinant of its Laplacian matrix via Kirchhoff's Matrix Tree Theorem.
- Common Reductions: Count the number of spanning trees in a multigraph subject to forced edges (value 1), forbidden edges (value 0), and optional edges (value -1).

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-jsc2021_g`](../../analysis/AtCoder-jsc2021_g.md) | G - Spanning Tree | 2451 | Count the number of spanning trees in a multigraph subject to forced edges (value 1), forbidden edges (value 0), and opt... |
