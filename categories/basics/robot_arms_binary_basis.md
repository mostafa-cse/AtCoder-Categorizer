# Basic Constructive Algorithms

**Taxonomy Path**: `Basics` > `Greedy and Constructive` > `Basic Constructive Algorithms`

## Description
This topic focuses on basic constructive algorithms techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Each step in {R, L, U, D} by length d shifts (u, v) by (+d, +d), (-d, -d), (+d, -d), and (-d, +d), completely decoupling the signs of u and v. All target points must share the same parity of |X_i| + |Y_i|. Using arm lengths d = {2^30, 2^29, ..., 2^0} (appended with 1 if parity is even), any odd coordinate in [-2*10^9, 2*10^9] is greedily reachable from top to bottom.
- Common Reductions: Reach all given target coordinates using at most 40 robot arms by rotating coordinates by 45 degrees into u = x + y and v = x - y, constructing a binary basis of powers of 2.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc103_b`](../../analysis/AtCoder-arc103_b.md) | Robot Arms | 2677 | Reach all given target coordinates using at most 40 robot arms by rotating coordinates by 45 degrees into u = x + y and ... |
