# Topological Sorting

**Taxonomy Path**: `Graph Theory` > `Graph Traversal` > `Topological Sorting`

## Description
This topic focuses on topological sorting techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: In a tree, every edge $(u, v)$ must be directed either $u \to v$ ($u$ removed before $v$) or $v \to u$ ($v$ removed before $u$). The required in-degree parity at every vertex uniquely determines the direction of all $N - 1$ tree edges! Root the tree arbitrarily and orient edges bottom-up from leaves to root. If the root's required parity matches its final in-degree, a valid DAG exists; otherwise, no valid sequence exists (output -1). Kahn's algorithm with a min-priority queue finds the lexicographically first topological sort.
- Common Reductions: Given a tree of $N$ vertices with black/white pieces, repeatedly select a white piece, remove it, and flip all adjacent pieces. Find the lexicographically smallest removal sequence of all $N$ vertices, or determine if impossible. A vertex $v$ receives flips from all neighbors removed before $v$. Hence, the parity of the number of neighbors removed before $v$ must match its initial color requirement: if initially white ('W'), it needs an even number of flips to remain white when removed; if black ('B'), it needs an odd number of flips.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc143_e`](../../analysis/AtCoder-arc143_e.md) | E. Reversi | 2521 | Given a tree of $N$ vertices with black/white pieces, repeatedly select a white piece, remove it, and flip all adjacent ... |
