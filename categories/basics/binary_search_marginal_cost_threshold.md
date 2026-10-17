# Binary Search

**Taxonomy Path**: `Basics` > `Leveraging Monotonicity` > `Binary Search`

## Description
This topic focuses on binary search techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: As marginal cost X increases, the number of available upgrades costing <= X is monotonically non-decreasing: sum_i max(0, (X - A_i)/D_i + 1). Binary searching for the smallest integer X where the total count is >= K isolates the K-th cheapest upgrade. Summing the closed-form arithmetic progressions c_i*A_i + c_i*(c_i-1)/2*D_i for all c_i upgrades with cost < X takes O(N) time.
- Common Reductions: Find the minimum cost to perform K building upgrades where building i starts at price A_i and increases by D_i per upgrade. The upgrade costs for building i form an arithmetic progression A_i + m*D_i. Binary search on the marginal upgrade cost threshold X. Upgrades with cost strictly below X are unconditionally taken, and the remaining upgrades needed to reach K are purchased at price exactly X.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc021_3`](../../analysis/AtCoder-arc021_3.md) | C. 増築王高橋君 | 2164 | Find the minimum cost to perform K building upgrades where building i starts at price A_i and increases by D_i per upgra... |
