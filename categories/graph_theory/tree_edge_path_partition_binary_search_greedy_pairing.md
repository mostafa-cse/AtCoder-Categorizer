# Union of Two Paths on a Tree

**Taxonomy Path**: `Graph Theory` > `More Tree Stuff` > `Union of Two Paths on a Tree`

## Description
This topic focuses on union of two paths on a tree techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Every vertex with odd degree must be an endpoint of at least one path, so minimum A is exactly O/2 where O is the count of odd-degree vertices. To minimize B, binary search over B in [1, N]. Root the tree at an arbitrary leaf. In tree DP, each vertex pairs up paths from its children with sums <= B, passing at most one path upwards to its parent. Validity of pairing is monotonic in the chosen upward path length, solved via binary search and two-pointer greedy pairing.
- Common Reductions: Decompose the edges of a tree with N vertices into a minimum number of paths A, and under this minimum A, minimize the maximum length B of any path.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc088_d`](../../analysis/AtCoder-arc088_d.md) | F - Christmas Tree | 2983 | Decompose the edges of a tree with N vertices into a minimum number of paths A, and under this minimum A, minimize the m... |
