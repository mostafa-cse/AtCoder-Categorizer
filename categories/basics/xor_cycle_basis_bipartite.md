# The XOR Trick

**Taxonomy Path**: `Basics` > `Bit Manipulation` > `The XOR Trick`

## Description
This topic focuses on the xor trick techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: For any spanning tree $T$ and cycle basis formed by non-tree edges, assigning a value $x_e \in \{1, 2\}$ to each non-tree edge $e$ and setting tree edge values such that the total sum along fundamental cycles matches the parity requirement reduces to a linear system over $\mathbb{F}_2$. A valid bipartite decomposition exists if and only if each connected component's induced subgraphs can be partitioned into two sets of even cycles.
- Common Reductions: Given $N$ vertices with $M$ red edges and $M$ blue edges, each forming an Eulerian graph, partition the red and blue edges into two equal sets such that both subgraphs have equal degrees at every vertex.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc199_a`](../../analysis/AtCoder-arc199_a.md) | A. Graph Division | 2285 | Given $N$ vertices with $M$ red edges and $M$ blue edges, each forming an Eulerian graph, partition the red and blue edg... |
