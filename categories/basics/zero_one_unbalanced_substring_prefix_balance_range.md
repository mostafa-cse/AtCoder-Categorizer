# Basic Greedy Algorithms

**Taxonomy Path**: `Basics` > `Greedy and Constructive` > `Basic Greedy Algorithms`

## Description
This topic focuses on basic greedy algorithms techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Mapping 0 -> -1 and 1 -> +1, the unbalancedness is max P - min P where P are prefix sums. Let Z be the minimum possible max P (achieved by setting all ? to -1). For a bound M = max P >= Z, the best minimum prefix sum f(M) is found greedily by a backward-forward pass. Furthermore, M - f(M) is convex in steps of 2, so the global minimum occurs at either M = Z or M = Z + 1.
- Common Reductions: Given string S of 0, 1, ? of length <= 10^6, replace each ? with 0 or 1 to minimize the maximum absolute difference between the count of 0s and 1s in any substring.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc045_b`](../../analysis/AtCoder-agc045_b.md) | B - 01 Unbalanced | 2873 | Given string S of 0, 1, ? of length <= 10^6, replace each ? with 0 or 1 to minimize the maximum absolute difference betw... |
