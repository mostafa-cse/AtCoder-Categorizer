# Topological Sorting

**Taxonomy Path**: `Graph Theory` > `Graph Traversal` > `Topological Sorting`

## Description
This topic focuses on topological sorting techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: A matrix can be sorted in row-major order iff (1) there exists a global column permutation making every row's non-zero elements non-decreasing, and (2) the intervals [min_i, max_i] of non-zero elements across rows can be ordered non-overlappingly. Column precedence constraints are modeled as directed edges between column groups via dummy nodes; a valid column permutation exists iff this graph is a DAG (acyclic).
- Common Reductions: Columns must satisfy precedence constraints from every row simultaneously. Inserting dummy nodes between consecutive value groups prevents O(W^2) edge explosion. A valid sort exists iff the column constraint graph is a DAG and row value intervals do not overlap, solved in O(H W log W) time.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc277_f`](../../analysis/AtCoder-abc277_f.md) | F. Sorting a Matrix | 2400 | Columns must satisfy precedence constraints from every row simultaneously. Inserting dummy nodes between consecutive val... |
