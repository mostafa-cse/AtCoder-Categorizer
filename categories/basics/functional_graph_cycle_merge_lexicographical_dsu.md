# Basic Constructive Algorithms

**Taxonomy Path**: `Basics` > `Greedy and Constructive` > `Basic Constructive Algorithms`

## Description
This topic focuses on basic constructive algorithms techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Merging $C$ disjoint cycles into a single $N$-cycle requires exactly $M = C - 1$ transpositions. Lexicographical minimization requires swapping $P_i$ with the smallest available element $r$ in a disjoint component as early as possible, or whenever $i$ is the maximum index of the current component containing 1.
- Common Reductions: Given a permutation $P$ of length $N$, you can swap elements within existing cycles at most $C-1$ times to connect all elements into a single cycle. Find the lexicographically smallest permutation achievable.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc167_d`](../../analysis/AtCoder-arc167_d.md) | D. Good Permutation | 2313 | Given a permutation $P$ of length $N$, you can swap elements within existing cycles at most $C-1$ times to connect all e... |
