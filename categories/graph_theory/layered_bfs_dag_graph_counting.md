# Counting Labeled Graphs

**Taxonomy Path**: `Graph Theory` > `Graph Counting` > `Counting Labeled Graphs`

## Description
This topic focuses on counting labeled graphs techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: The condition that vertex $N$ has strictly greater distance from vertex 1 than all other vertices implies $N$ is the unique vertex in the final layer $D$ of the BFS DAG.
- Common Reductions: Count the number of connected undirected graphs with $N$ labeled vertices where vertex $N$ has strictly greater shortest path distance from vertex 1 than any other vertex, modulo $M$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc281_g`](../../analysis/AtCoder-abc281_g.md) | G. Farthest City | 2304 | Count the number of connected undirected graphs with $N$ labeled vertices where vertex $N$ has strictly greater shortest... |
