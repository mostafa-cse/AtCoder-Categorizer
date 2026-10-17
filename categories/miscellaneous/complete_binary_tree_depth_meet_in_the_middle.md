# Meet in the Middle

**Taxonomy Path**: `Miscellaneous` > `Techniques` > `Meet in the Middle`

## Description
This topic focuses on meet in the middle techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Splitting the path at depth 9 limits both the top ancestor path and the bottom path to at most 9 items. For nodes u < 512, precalculating the Pareto frontier of non-dominated (weight, value) pairs takes negligible memory (< 2 MB) and O(2^9) operations per node. For any query (v, L), bottom subsets (<= 256) are combined with top Pareto pairs via binary search in O(2^k log S).
- Common Reductions: Complete binary tree of depth <= 18 with 0-1 knapsack queries on paths from v to root. Sqrt decomposition / Meet-in-the-Middle on tree depth: precalculate Pareto frontiers for the top 9 levels, and enumerate 2^k subsets for the bottom <= 9 levels.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| `[problem:AtCoder-tokiomarine2020_d]` | Knapsack Queries on a tree | 2158 | Complete binary tree of depth <= 18 with 0-1 knapsack queries on paths from v to root. Sqrt decomposition / Meet-in-the-... |
