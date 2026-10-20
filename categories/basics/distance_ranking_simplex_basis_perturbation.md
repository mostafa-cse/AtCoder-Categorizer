# Basic Constructive Algorithms

**Taxonomy Path**: `Basics` > `Greedy and Constructive` > `Basic Constructive Algorithms`

## Description
This topic focuses on basic constructive algorithms techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Start from a regular simplex where all pairwise distances are equal to sqrt(2) * L: p_i[i] = L and 0 elsewhere. Perturb the coordinates: for each pair (i, j) with i < j, set p_i[j] = r_{i, j} where r_{i, j} in [1, M] is the rank of (i, j) from farthest to closest. The distance squared between p_i and p_j expands as 2L^2 - 2 L r_{i, j} + O(N M^2). For sufficiently large L (e.g. L = 5 * 10^7), the linear term -2 L r_{i, j} dominates all quadratic error terms, strictly ordering all pairwise distances as desired.
- Common Reductions: In N-dimensional space, place N points with integer coordinates in [0, 10^8] such that their pairwise Euclidean distances strictly follow a given ranking order: d(p_{A_1}, p_{B_1}) < d(p_{A_2}, p_{B_2}) < ...

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc172_d`](../../analysis/AtCoder-arc172_d.md) | D. Distance Ranking | 2936 | In N-dimensional space, place N points with integer coordinates in [0, 10^8] such that their pairwise Euclidean distance... |
