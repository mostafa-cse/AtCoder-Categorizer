# Topological Sorting

**Taxonomy Path**: `Graph Theory` > `Graph Traversal` > `Topological Sorting`

## Description
This topic focuses on topological sorting techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: A valid signpost orientation for each color forms a directed spanning tree rooted at that color's destination with no cycles, subject to the condition that no vertex points along the same directed edge in both trees.
- Common Reductions: Given an undirected graph of $N$ vertices and $M$ edges, place blue and yellow signposts at each vertex directed towards 1 and 2 respectively, such that following blue leads to 1, following yellow leads to 2, and no vertex has identical signpost orientations.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc211_d`](../../analysis/AtCoder-arc211_d.md) | D. Two Signposts | 2301 | Given an undirected graph of $N$ vertices and $M$ edges, place blue and yellow signposts at each vertex directed towards... |
