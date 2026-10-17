# Basic Constructive Algorithms

**Taxonomy Path**: `Basics` > `Greedy and Constructive` > `Basic Constructive Algorithms`

## Description
This topic focuses on basic constructive algorithms techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: In any rooted tree, extending the LIS at vertex $u$ increments the LIS value of all vertices in its subtree $T_u$, contributing exactly $|T_u|$ to $\sum L_i$. Since subtree sizes form an additive hierarchy, greedy selection by descending subtree size solves the subset sum exactly, and ranking vertices by signed depths $x_u = \pm d_u$ reconstructs the permutation.
- Common Reductions: Given a tree of $N$ vertices and a target integer $K$, construct a permutation $P$ of $1, \dots, N$ such that the sum of lengths of longest increasing subsequences over all simple paths starting from the root equals $K$, or determine it is impossible.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc175_d`](../../analysis/AtCoder-arc175_d.md) | D. LIS on Tree 2 | 2276 | Given a tree of $N$ vertices and a target integer $K$, construct a permutation $P$ of $1, \dots, N$ such that the sum of... |
