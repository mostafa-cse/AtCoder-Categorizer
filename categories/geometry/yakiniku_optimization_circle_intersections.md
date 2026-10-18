# Circles, Circle Relations, Intersections, Inscribed Circles and Circumcircles(2D)

**Taxonomy Path**: `Geometry` > `Geometry 2D` > `Circles, Circle Relations, Intersections, Inscribed Circles and Circumcircles(2D)`

## Description
This topic focuses on circles, circle relations, intersections, inscribed circles and circumcircles(2d) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Binary search on time $T \in [0, 4 \times 10^5]$. For a fixed $T$, we have $N$ disks with radii $R_i = T / c_i$. An optimal point $P$ maximizing disk coverage can always be chosen either as one of the circle centers, or as an intersection point of the boundaries of two circles. With $N \le 60$, there are $O(N^2)$ candidate points. Testing coverage of all candidate points takes $O(N^3)$ per binary search step.
- Common Reductions: Given $N$ pieces of meat at coordinates $(x_i, y_i)$ with heat parameters $c_i$, cooking meat $i$ to level 1 takes time $c_i \cdot \text{dist}(P, (x_i, y_i))$. Placing a heat source at point $P$, cooking takes time $T$. The condition that meat $i$ is cooked in time $T$ is $c_i \cdot \text{dist}(P, (x_i, y_i)) \le T \iff \text{dist}(P, (x_i, y_i)) \le T / c_i$. That is, $P$ must lie inside the disk centered at $(x_i, y_i)$ with radius $R_i = T / c_i$. We must find the minimum $T$ such that some point $P$ is covered by at least $K$ disks.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc157_f`](../../analysis/AtCoder-abc157_f.md) | F. Yakiniku Optimization Problem | 2525 | Given $N$ pieces of meat at coordinates $(x_i, y_i)$ with heat parameters $c_i$, cooking meat $i$ to level 1 takes time ... |
