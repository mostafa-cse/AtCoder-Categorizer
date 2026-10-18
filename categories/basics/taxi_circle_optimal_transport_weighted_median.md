# Basic Greedy Algorithms

**Taxonomy Path**: `Basics` > `Greedy and Constructive` > `Basic Greedy Algorithms`

## Description
This topic focuses on basic greedy algorithms techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Let $d_i = b_i - c_i$ be net excess at city $i$. On a cut line, the net flow across arc $i$ of length $\Delta x_i$ is prefix sum $P_i = \sum_{j=1}^i d_j$. On a circle, adding a global circulation $F$ makes flow across arc $i$ equal $P_i + F$, with total cost $C(F) = \sum_{i=1}^N \Delta x_i |F - (-P_i)|$. Minimizing this continuous 1D convex sum is the weighted median problem with points $-P_i$ and weights $\Delta x_i$ summing to $L$. Sorting by $-P_i$ and picking the median where accumulated weight reaches $L/2$ yields the optimal circulation $F$ in $O(N \log N)$ time.
- Common Reductions: Find the minimum cost to transport participants on a circular line of length $L$ with $N$ cities so that supplies match demands.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-dwango2015_prelims_4`](../../analysis/AtCoder-dwango2015_prelims_4.md) | D - タクシー | 2495 | Find the minimum cost to transport participants on a circular line of length $L$ with $N$ cities so that supplies match ... |
