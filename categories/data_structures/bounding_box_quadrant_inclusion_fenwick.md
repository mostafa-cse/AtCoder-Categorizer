# BIT / Fenwick Tree

**Taxonomy Path**: `Data Structures (DS)` > `Binary Indexed Tree (BIT)` > `BIT / Fenwick Tree`

## Description
This topic focuses on bit / fenwick tree techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: A point $P$ is inside the bounding box of subset $T$ if and only if $T$ contains $P$ or $T$ has points in opposing quadrants relative to $P$. By complementary counting, $P$ is covered in all non-empty subsets except those strictly contained within any single half-plane (North, South, East, West).
- Common Reductions: Sum the number of points enclosed in bounding boxes over all non-empty subsets. By quadrant complementary counting, a point $P$ is enclosed unless all chosen points lie in a single half-plane, computed via Fenwick sweep in $O(N \log N)$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc136_f`](../../analysis/AtCoder-abc136_f.md) | F. Enclosed Points | 2334 | Sum the number of points enclosed in bounding boxes over all non-empty subsets. By quadrant complementary counting, a po... |
