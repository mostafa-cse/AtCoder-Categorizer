# Centroid Decomposition

**Taxonomy Path**: `Data Structures (DS)` > `Centroid Decomposition` > `Centroid Decomposition`

## Description
This topic focuses on centroid decomposition techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Root the tree at its centroid R. In any tree with a unique perfect matching, removing leaves in a valid order preserves matchings. Because R is the centroid, each branch has size <= N/2. By repeatedly removing one leaf from the largest branch and one leaf from another branch, every removed pair traverses the centroid R, achieving the theoretical upper bound on total distance.
- Common Reductions: Given a tree with N vertices (even N) with a perfect matching, repeatedly remove two leaves such that the remaining tree preserves a perfect matching, maximizing the sum of distances between removed pairs.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc183_d`](../../analysis/AtCoder-arc183_d.md) | D. Keep Perfectly Matched | 2880 | Given a tree with N vertices (even N) with a perfect matching, repeatedly remove two leaves such that the remaining tree... |
