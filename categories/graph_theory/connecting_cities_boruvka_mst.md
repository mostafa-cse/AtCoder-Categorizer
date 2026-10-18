# Boruvka's Algorithm

**Taxonomy Path**: `Graph Theory` > `Minimum Spanning Tree (MST)` > `Boruvka's Algorithm`

## Description
This topic focuses on boruvka's algorithm techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Boruvka's algorithm runs in at most ceil(log_2 N) contraction rounds. In each round, every component seeks its cheapest outgoing edge. Because the edge weight separates into (A_i - i D) + (A_j + j D) for i < j, maintaining the top 2 components with minimum A_i - i D in a prefix sweep and minimum A_j + j D in a suffix sweep identifies the cheapest outgoing edge for all components in O(N) time.
- Common Reductions: In a complete graph of N cities on a line, the edge weight between i < j is (A_i - i D) + (A_j + j D). Find the minimum spanning tree weight.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-keyence2019_e`](../../analysis/AtCoder-keyence2019_e.md) | E - Connecting Cities | 2623 | In a complete graph of N cities on a line, the edge weight between i < j is (A_i - i D) + (A_j + j D). Find the minimum ... |
