# Persistent Treap

**Taxonomy Path**: `Data Structures (DS)` > `Balanced Binary Search Tree (BBST)` > `Persistent Treap`

## Description
This topic focuses on persistent treap techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Elements in every array preserve their original index $pos$. Represent each array as dual balanced sets sorted by $pos$ and by $val$. For both split-by-index and split-by-value, identify the smaller side using bidirectional finger search. Extract the smaller side and insert into the target array, swapping pointers if the left side was smaller. By small-to-large splitting, each element moves at most $O(\log N)$ times.
- Common Reductions: Maintain arrays under operations: split by prefix length (type 1) and split by value threshold (type 2). Output the size of each newly generated array.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc324_g`](../../analysis/AtCoder-abc324_g.md) | G. Generate Arrays | 2501 | Maintain arrays under operations: split by prefix length (type 1) and split by value threshold (type 2). Output the size... |
