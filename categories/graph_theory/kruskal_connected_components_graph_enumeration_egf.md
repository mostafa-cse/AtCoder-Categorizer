# Counting Labeled Graphs

**Taxonomy Path**: `Graph Theory` > `Graph Counting` > `Counting Labeled Graphs`

## Description
This topic focuses on counting labeled graphs techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: By Kruskal's algorithm, the MST weight is determined by the number of connected components c_w after considering edges of weight <= w: weight(MST) = sum_{w=1}^M (c_{w-1} - 1). We enumerate graphs with prescribed component counts across edge-weight thresholds via exponential generating functions (EGF) of connected graphs and polynomial interpolation.
- Common Reductions: Count connected graphs with N labeled vertices and edge weights in {1, ..., M} whose MST weight is at most K.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc386_g`](../../analysis/AtCoder-abc386_g.md) | G. Many MST | 2930 | Count connected graphs with N labeled vertices and edge weights in {1, ..., M} whose MST weight is at most K.... |
