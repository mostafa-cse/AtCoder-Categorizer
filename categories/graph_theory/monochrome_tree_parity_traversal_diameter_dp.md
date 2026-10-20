# Euler Tour Technique

**Taxonomy Path**: `Graph Theory` > `Graph Traversal` > `Euler Tour Technique`

## Description
This topic focuses on euler tour technique techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Prune all black leaves repeatedly until all leaves are white. In a closed Euler tour of the pruned tree with E edges, each edge is traversed twice and each vertex v is flipped deg(v) times. A vertex ending white requires 1 extra flip. An open walk from S to T traverses the simple path P once instead of twice, reducing edge traversals by 1 per edge and flips by 1 for all vertices along the path except T. Setting vertex weight to 2 if (col[v] + deg(v)) is odd and 0 if even, the savings from choosing path P equals the sum of vertex weights on P. Maximizing savings reduces to finding the weighted tree diameter!
- Common Reductions: Given a black/white colored tree, a cat moves between adjacent vertices (flipping destination) or flips current vertex. Find minimum seconds to make all vertices black starting and ending anywhere.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc097_d`](../../analysis/AtCoder-arc097_d.md) | F. Monochrome Cat | 2948 | Given a black/white colored tree, a cat moves between adjacent vertices (flipping destination) or flips current vertex. ... |
