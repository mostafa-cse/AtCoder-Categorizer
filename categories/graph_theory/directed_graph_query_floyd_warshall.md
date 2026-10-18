# Floyd Warshall

**Taxonomy Path**: `Graph Theory` > `Shortest Paths` > `Floyd Warshall`

## Description
This topic focuses on floyd warshall techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: The cost of a path is <= X iff there exists a path from s to t using only vertices from {1, 2, ..., X}. By processing vertices X = 1, 2, ..., N in increasing order, the reachable pairs within {1 ... X} can be updated dynamically using bitsets in O(N^2 / 64) per step, recording the minimum X where t becomes reachable from s.
- Common Reductions: Given a directed graph of N vertices, the cost of a path is the maximum vertex index visited on the path. Answer Q reachability cost queries (s_i, t_i).

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc287_h`](../../analysis/AtCoder-abc287_h.md) | Ex - Directed Graph Query | 2639 | Given a directed graph of N vertices, the cost of a path is the maximum vertex index visited on the path. Answer Q reach... |
