# DP Optimization using Data Structures [Some Practice Problems]

**Taxonomy Path**: `Dynamic Programming (DP)` > `DP Optimizations` > `DP Optimization using Data Structures [Some Practice Problems]`

## Description
This topic focuses on dp optimization using data structures [some practice problems] techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Shik collects coins in contiguous segments. If Shik gives candies to bears j+1 through i and then returns to collect their coins, the extra turnaround time is max(T, 2 * (x_i - x_{j+1})). The DP transition is: DP[i] = min_{0 <= j < i} (DP[j] - x_j + x_i + max(T, 2 * (x_i - x_{j+1}))). For a given i, the condition 2 * (x_i - x_{j+1}) <= T is monotonic in j. Thus, there is a threshold p such that for j < p, the turnaround cost is 2 * (x_i - x_{j+1}), and for j >= p, the cost is T. For j < p, the transition simplifies to DP[j] - x_j + 3 * x_i - 2 * x_{j+1}, which is optimized by maintaining the prefix minimum of DP[j] - x_j - 2 * x_{j+1}. For j >= p, it simplifies to DP[j] - x_j + x_i + T, optimized by maintaining the prefix minimum of DP[j] - x_j. This allows computing DP[i] in O(1) amortized time.
- Common Reductions: There are N bears at coordinates x_1 < x_2 < ... < x_N on a line of length E. When Shik gives a candy to a bear, it produces a coin after time T. Shik starts at 0, must collect all coins, and reach E. Find the minimum time to collect all coins and reach E.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc007_d`](../../analysis/AtCoder-agc007_d.md) | D - Shik and Game | 2754 | There are N bears at coordinates x_1 < x_2 < ... < x_N on a line of length E. When Shik gives a candy to a bear, it prod... |
