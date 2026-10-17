# Basic Greedy Algorithms

**Taxonomy Path**: `Basics` > `Greedy and Constructive` > `Basic Greedy Algorithms`

## Description
This topic focuses on basic greedy algorithms techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: A safe robot j (B_j < A_j) covers coordinate range [A_j - B_j, A_j - 1]. Precomputing suffix minimums min_{j > k, B_j < A_j} (A_j - B_j) identifies which dangerous robots are automatically covered. If we delete B_i - A_i + 1 balls from the rightmost modified dangerous robot i, it safely destroys all robots < A_i. The optimal answer is min over all dangerous i of max(B_i - A_i + 1, suffix_uncovered_dangerous[i + 1]).
- Common Reductions: Robots start at coordinates A_i and move B_i steps left, destroying encountered robots. Avoid destroying Robot 0 with minimum ball modifications. Robots with B_j < A_j can safely destroy other robots without reaching 0. Dangerous robots (B_i >= A_i) must either be destroyed by a safe robot to their right, or modified by deleting B_i - A_i + 1 balls (which sweeps and destroys all robots to its left).

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc049_c`](../../analysis/AtCoder-agc049_c.md) | C. Robots | 2177 | Robots start at coordinates A_i and move B_i steps left, destroying encountered robots. Avoid destroying Robot 0 with mi... |
