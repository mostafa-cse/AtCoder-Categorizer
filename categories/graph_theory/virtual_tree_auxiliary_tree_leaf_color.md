# Virtual Tree / Auxiliary Tree

**Taxonomy Path**: `Graph Theory` > `More Tree Stuff` > `Virtual Tree / Auxiliary Tree`

## Description
This topic focuses on virtual tree / auxiliary tree techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: A valid subgraph with all leaves of color c is an induced subtree on the virtual tree whose extremal nodes are all colored c. Compressing the tree via LCA and DFS entry time reduces the total nodes evaluated across all colors to sum(2 k_c) = O(N).
- Common Reductions: Count connected induced subgraphs whose leaves all share a given color c. For each color c with k_c occurrences, build an Auxiliary / Virtual Tree in O(k_c log N) and run DP on the compressed tree.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc340_g`](../../analysis/AtCoder-abc340_g.md) | G. Leaf Color | 2401 | Count connected induced subgraphs whose leaves all share a given color c. For each color c with k_c occurrences, build a... |
