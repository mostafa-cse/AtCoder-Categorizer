# BEST Theorem

**Taxonomy Path**: `Graph Theory` > `Graph Counting` > `BEST Theorem`

## Description
This topic focuses on best theorem techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: By the BEST Theorem, the number of Eulerian circuits in a directed graph is given by t_w(G) * prod_v (deg_in(v) - 1)!, where t_w(G) is the number of directed spanning trees rooted at w. In a 4-cycle S-T-U-V-S, directing x edges from S to T uniquely fixes the orientations of all remaining edges (y, z, w) via degree balance at each vertex. The number of directed trees kappa(G, S) is evaluated algebraically via the Matrix Tree Theorem cofactor as (a-x)(b-y)(c-z) + (a-x)(b-y)w + (a-x)zw + yzw.
- Common Reductions: Count Eulerian walks in a 4-cycle graph with undirected edge multiplicities a, b, c, d modulo 998244353.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc051_d`](../../analysis/AtCoder-agc051_d.md) | D - C4 | 2807 | Count Eulerian walks in a 4-cycle graph with undirected edge multiplicities a, b, c, d modulo 998244353.... |
