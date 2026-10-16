# 📖 Segment Tree Accelerated Range Knapsack DP

- **Tag / Domain**: `Dynamic Programming (DP)`
- **Subtopic**: `DP Optimizations`

---

## 💡 Topic Overview
High-value competitive programming techniques for **Segment Tree Accelerated Range Knapsack DP**.

---

## 🏆 Curated High-Value Problems

### Don't Leave the Spice (`[problem:AtCoder-typical90_ak]`)

- **Role**: *Segment Tree Accelerated Range Knapsack DP*
- **Rating**: `1750` (★5) | **Contest**: [`typical90`](https://atcoder.jp/contests/typical90/tasks/typical90_ak)
- **Full Analysis**: [AtCoder-typical90_ak Analysis](../../analysis/AtCoder-typical90_ak.md)

#### Problem Statement & Task
Dishes require exact weight W (W <= 10000). N spices with weight range [L_i, R_i] and value V_i. Find maximum value to achieve exact weight W, or -1 if impossible.

#### Core Invariant & Observation
The transition requires the maximum of dp[i-1][w - R_i .. w - L_i]. Maintaining the previous DP layer in a Segment Tree answers each range query in O(log W).

#### Algorithmic Formulation
1. Build Segment Tree over capacities [0, W] initialized to -1 (with seg[0] = 0).
2. For each spice (L, R, V):
   - For w from W down to 0: query range_max in [max(0, w - R), w - L]. If valid, next_dp[w] = max(dp[w], best + V).
   - Update Segment Tree with next_dp.
3. Output dp[W].

**Complexity**: `Time: O(N * W log W), Space: O(W).`  
**Editorial Alignment**: Segment Tree range-maximum query acceleration on range knapsack transitions.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: Accelerating sliding-window / range-interval DP transitions using dynamic range maximum data structures.
- **Reusable Pattern**: `Segment Tree Accelerated Range DP.`

---

[Back to Master Categories](../../README.md)
