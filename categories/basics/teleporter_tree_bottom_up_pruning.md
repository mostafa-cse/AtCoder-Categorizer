# Basic Greedy Algorithms

**Taxonomy Path**: `Basics` > `Greedy and Constructive` > `Basic Greedy Algorithms`

## Description
This topic focuses on basic greedy algorithms techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: For every city to reach capital 1 in exactly $K$ steps, city 1 must have a self-loop ($a_1 = 1$), forming a directed rooted tree towards 1 where every node has depth $\le K$. Any redirected edge is optimally pointed directly to root 1. Pruning subtrees greedily from the bottom up whenever a node's subtree height reaches $K-1$ minimizes edge modifications.
- Common Reductions: Given a teleporter graph, find the minimum changes so every town reaches town 1 in exactly $K$ steps. Forces $a_1=1$ and prunes subtrees exceeding height $K-1$ greedily bottom-up in $O(N)$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc004_d`](../../analysis/AtCoder-agc004_d.md) | D. Teleporter | 2346 | Given a teleporter graph, find the minimum changes so every town reaches town 1 in exactly $K$ steps. Forces $a_1=1$ and... |
