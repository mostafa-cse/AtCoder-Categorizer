# Combining Subtrees Technique

**Taxonomy Path**: `Dynamic Programming (DP)` > `More Tricks` > `Combining Subtrees Technique`

## Description
This topic focuses on combining subtrees technique techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Count the complement: when CANNOT the tree be reduced to 1? Removing all OR edges partitions the tree into AND-components. The tree cannot become 1 if and only if EVERY AND-component contains at least one vertex labeled 0! We count this bad condition using tree DP tracking whether the current component containing vertex u already contains a 0 or not.
- Common Reductions: Given a tree of N vertices with boolean vertex labels (0/1) and edge operators (AND/OR), count the number of labelings (2^{2N-1}) such that edge contractions can reduce the tree to a single vertex labeled 1.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc121_f`](../../analysis/AtCoder-arc121_f.md) | F. Logical Operations on Tree | 2940 | Given a tree of N vertices with boolean vertex labels (0/1) and edge operators (AND/OR), count the number of labelings (... |
