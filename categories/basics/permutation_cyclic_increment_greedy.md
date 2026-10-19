# Basic Greedy Algorithms

**Taxonomy Path**: `Basics` > `Greedy and Constructive` > `Basic Greedy Algorithms`

## Description
This topic focuses on basic greedy algorithms techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Sorting A allows matching elements to target B_i = x + i - 1. The total required increment S = sum(B_i - A_i) must be divisible by M. Each element requires B_i >= A_i, establishing a lower bound on x. By cyclic difference analysis, the required operations are non-negative iff the maximum individual increment does not exceed S / M, and modular compatibility holds with gcd(N, M). If violated, jumping x by steps of M / gcd(N, M) finds the minimal valid configuration.
- Common Reductions: Given an array A and integer M, find the minimum number of cyclic range increment operations of size M to transform A into a permutation of (x, x+1, ..., x+N-1) for some integer x, or report -1.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc169_d`](../../analysis/AtCoder-arc169_d.md) | D - Add to Make a Permutation | 2812 | Given an array A and integer M, find the minimum number of cyclic range increment operations of size M to transform A in... |
