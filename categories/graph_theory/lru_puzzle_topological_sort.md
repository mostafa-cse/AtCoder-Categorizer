# Topological Sorting

**Taxonomy Path**: `Graph Theory` > `Graph Traversal` > `Topological Sorting`

## Description
This topic focuses on topological sorting techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: If all operations were performed on a single array, looking at the operations in reverse order, elements appear in the final array in order of their last access, followed by untouched elements in increasing order 1..M. In the target array V, any trailing suffix that remains in increasing order does not need to be actively moved because untouched elements in each array are already in increasing order. Trimming this increasing suffix leaves a mandatory prefix of V that every array must construct. Simulating backwards, we track how many arrays have currently matched each prefix length of V, advancing an array whenever the corresponding operation a_i is encountered.
- Common Reductions: Given N arrays initially identical to (1, 2, ..., M), we perform Q operations where each operation chooses one array and moves element a_i to the front. Determine whether all N arrays can end up completely identical.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-codefestival_2016_qualA_e`](../../analysis/AtCoder-codefestival_2016_qualA_e.md) | E - LRU Puzzle | 2723 | Given N arrays initially identical to (1, 2, ..., M), we perform Q operations where each operation chooses one array and... |
