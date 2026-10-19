# Convex Hull(2D)

**Taxonomy Path**: `Geometry` > `Geometry 2D` > `Convex Hull(2D)`

## Description
This topic focuses on convex hull(2d) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Notice that 2^{n - |S|} is the number of subsets of points from the interior/boundary of the convex hull of S (excluding S itself). Every subset P of points whose convex hull has positive area has a unique set of extreme vertices S = ext(conv(P)), and P can be any of the 2^{n - |S|} subsets containing S. Therefore, the sum of 2^{n - |S|} over all convex polygons S is EXACTLY the number of non-collinear subsets P of size >= 3! Using complementary counting, the answer is 2^N - 1 - N - binom(N, 2) - sum_{collinear lines L, |L| >= 3} (2^{|L|} - 1 - |L| - binom(|L|, 2)).
- Common Reductions: Given N points in the 2D plane (N <= 200). For each subset S that forms a convex polygon with positive area, its score is 2^{n - |S|}, where n is the number of points in the convex hull of S. Find the sum of scores over all convex polygons modulo 998244353.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc082_c`](../../analysis/AtCoder-arc082_c.md) | E - ConvexScore | 2729 | Given N points in the 2D plane (N <= 200). For each subset S that forms a convex polygon with positive area, its score i... |
