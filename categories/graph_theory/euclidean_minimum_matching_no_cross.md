# Min Cost Max Flow (MCMF)

**Taxonomy Path**: `Graph Theory` > `Flow and Min Cut` > `Min Cost Max Flow (MCMF)`

## Description
This topic focuses on min cost max flow (mcmf) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: In any bipartite matching of N points to N points where no three points are collinear, if any two segments cross at an intersection point X, the triangle inequality guarantees that uncrossing their endpoints strictly decreases the total Euclidean length. Therefore, the minimum Euclidean distance matching cannot contain any crossing segments.
- Common Reductions: Given N red and N blue points with no three collinear, find a non-crossing bipartite matching. By the triangle inequality, any crossing pair of segments can be uncrossed to strictly decrease total Euclidean length; thus, the minimum Euclidean distance matching guarantees zero crossings, solved via the Hungarian algorithm in O(N^3) time.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc373_g`](../../analysis/AtCoder-abc373_g.md) | G. No Cross Matching | 2377 | Given N red and N blue points with no three collinear, find a non-crossing bipartite matching. By the triangle inequalit... |
