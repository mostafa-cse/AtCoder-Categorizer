# DP on Trees and DAGs

**Taxonomy Path**: `Dynamic Programming (DP)` > `Dp on Different Structures` > `DP on Trees and DAGs`

## Description
This topic focuses on dp on trees and dags techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Two operation sequences produce identical permutations iff the set of used edges E' is identical AND for every vertex v, the relative order of use of incident edges in E' is identical. Since any local edge ordering at vertices is realizable, each spanning subgraph (V, E') contributes exactly prod_{v in V} (deg_{E'}(v))! distinct permutations. Summing this product over all 2^{N-1} edge subsets reduces to tree DP combining children polynomials.
- Common Reductions: Count the number of distinct permutations obtainable by repeatedly choosing an edge on a tree, swapping pieces on its endpoints, and deleting the edge.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc171_c`](../../analysis/AtCoder-arc171_c.md) | Swap on Tree | 2244 | Count the number of distinct permutations obtainable by repeatedly choosing an edge on a tree, swapping pieces on its en... |
