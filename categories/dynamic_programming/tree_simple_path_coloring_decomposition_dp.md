# DP on Trees and DAGs

**Taxonomy Path**: `Dynamic Programming (DP)` > `Dp on Different Structures` > `DP on Trees and DAGs`

## Description
This topic focuses on dp on trees and dags techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Color monochromatic edges 'black' (weight 0) and inter-color edges 'white' (weight 1). Black edges form vertex-disjoint paths, meaning each vertex has degree at most 2 in black edges. The maximum number of colors on any tree path is (diameter in {0, 1} weights) + 1. By HLD, the optimal K is at most 2 * floor(log2 N) + 1. For a fixed K, tree DP determines whether a {0, 1} weighting with diameter <= K - 1 exists in O(N) time.
- Common Reductions: Partition vertices of an N-vertex tree into monochromatic simple paths such that any simple path in the tree intersects at most K colors. Find the minimum possible K.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc293_h`](../../analysis/AtCoder-abc293_h.md) | Ex - Optimal Path Decomposition | 2831 | Partition vertices of an N-vertex tree into monochromatic simple paths such that any simple path in the tree intersects ... |
