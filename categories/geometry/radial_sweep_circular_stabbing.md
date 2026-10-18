# Sweep Line Algorithm and Radial Sweep

**Taxonomy Path**: `Geometry` > `Sweep Line` > `Sweep Line Algorithm and Radial Sweep`

## Description
This topic focuses on sweep line algorithm and radial sweep techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Each obstacle line segment subtends an angular interval $[L_i, R_i]$ from the origin on the circle $S^1$. In an optimal stabbing ray set, at least one ray can be assumed to pass through the right endpoint $R_k$ of some obstacle without loss of generality. Cutting the circle at this ray reduces the remaining obstacles to a linear greedy interval stabbing problem on $[R_k, R_k + 2\pi)$.
- Common Reductions: Line obstacles subtend angular intervals on the circle. Fixing the rightmost endpoint of an obstacle as the first ray reduces the circular stabbing problem to linear greedy interval stabbing in $O(N^2 \log N)$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-tenka1_2014_qualA_d`](../../analysis/AtCoder-tenka1_2014_qualA_d.md) | D. 秘密結社 | 2341 | Line obstacles subtend angular intervals on the circle. Fixing the rightmost endpoint of an obstacle as the first ray re... |
