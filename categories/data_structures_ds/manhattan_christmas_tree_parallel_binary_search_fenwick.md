# Persistent Segment Tree

**Taxonomy Path**: `Data Structures (DS)` > `Segment Tree` > `Persistent Segment Tree`

## Description
This topic focuses on persistent segment tree techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: The number of points in $[u - D, u + D] \times [v - D, v + D]$ is monotonic with respect to $D \in [0, 4 \times 10^5]$. We can binary search $D$ for all $Q$ queries simultaneously using Parallel Binary Search. In each round, testing if box contains $\ge K$ points is equivalent to 2D range counting, solved by a sweep-line with a Fenwick Tree in $O((N + Q) \log(\max V))$ time.
- Common Reductions: Given $N$ points $(x_i, y_i)$, answer $Q$ queries: for query point $(x, y)$ and integer $K$, find the $K$-th smallest Manhattan distance $|x - x_i| + |y - y_i|$ to any of the $N$ points. Rotate coordinates by $45^\circ$: let $u = x + y, v = x - y$. The Manhattan metric becomes Chebyshev metric $\max(|u - u_i|, |v - v_i|)$. The condition $\max(|u - u_i|, |v - v_i|) \le D$ translates to a 2D axis-aligned bounding box $[u - D, u + D] \times [v - D, v + D]$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc233_h`](../../analysis/AtCoder-abc233_h.md) | Ex. Manhattan Christmas Tree | 2530 | Given $N$ points $(x_i, y_i)$, answer $Q$ queries: for query point $(x, y)$ and integer $K$, find the $K$-th smallest Ma... |
