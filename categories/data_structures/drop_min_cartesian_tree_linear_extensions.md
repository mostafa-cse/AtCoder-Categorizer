# Cartesian Tree

**Taxonomy Path**: `Data Structures (DS)` > `More Tree Data Structures` > `Cartesian Tree`

## Description
This topic focuses on cartesian tree techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: In the max Cartesian tree of $P$, any node $u \neq \text{root}$ can be deleted if and only if all elements of its left subtree are deleted before $u$ (if an ancestor exists to its left) or all elements of its right subtree are deleted before $u$ (if an ancestor exists to its right).
- Common Reductions: Given an array $P$ of length $N$, elements are deleted in a valid order corresponding to tree hook-length independence on the Cartesian tree. Find the expected eliminations or total valid topological orderings modulo 998244353.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc212_e`](../../analysis/AtCoder-arc212_e.md) | E. Drop Min | 2324 | Given an array $P$ of length $N$, elements are deleted in a valid order corresponding to tree hook-length independence o... |
