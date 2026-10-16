# 📖 Knapsack DP & Dual State Inversion

- **Tag / Domain**: `Dynamic Programming (DP)`
- **Subtopic**: `Intro to DP`
- **Total Curated Problems**: 2

---

## 💡 Topic Overview
The knapsack paradigm, covering classic 0/1 knapsack with weight as state, and dual knapsack where weight capacity is astronomical and value is inverted into the state index.

---

## 🏆 Curated High-Value Problems

### 1. Knapsack 1 (`[problem:AtCoder-dp_d]`)

- **Role**: *0/1 Knapsack with 1D Memory Compression*
- **Rating**: `1150` | **Contest**: [`dp`](https://atcoder.jp/contests/dp/tasks/dp_d)
- **Full Analysis**: [AtCoder-dp_d Analysis](../../analysis/AtCoder-dp_d.md)

#### Problem Statement & Task
Maximize value of items with total weight <= W (W <= 10^5, N <= 100).

#### Core Invariant & Observation
Looping weight downwards from W to w_i ensures each item is included at most once in a 1D DP array.

#### Algorithmic Formulation
1. dp[0..W] = 0.
2. For each item (w_i, v_i): for cap from W down to w_i: dp[cap] = max(dp[cap], dp[cap - w_i] + v_i).
3. Result is max(dp).

**Complexity**: `Time: O(N * W), Space: O(W).`  
**Editorial Alignment**: Standard 1D reverse-iteration 0/1 Knapsack.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: 0/1 Knapsack state optimization and 1D space reduction technique.
- **Reusable Pattern**: `1D space-optimized 0/1 knapsack.`

---

### 2. Knapsack 2 (`[problem:AtCoder-dp_e]`)

- **Role**: *Dual Knapsack / Value as State*
- **Rating**: `1450` | **Contest**: [`dp`](https://atcoder.jp/contests/dp/tasks/dp_e)
- **Full Analysis**: [AtCoder-dp_e Analysis](../../analysis/AtCoder-dp_e.md)

#### Problem Statement & Task
Solve 0/1 Knapsack when capacity W <= 10^9 is enormous, but v_i <= 1000 and N <= 100.

#### Core Invariant & Observation
Total value sum <= 100 * 1000 = 10^5. The value dimension is pseudopolynomial while weight is not.

#### Algorithmic Formulation
1. V_sum = sum(v_i). dp[0] = 0, dp[1..V_sum] = INF.
2. For each item (w_i, v_i): for v from V_sum down to v_i: dp[v] = min(dp[v], dp[v - v_i] + w_i).
3. Return max v such that dp[v] <= W.

**Complexity**: `Time: O(N * sum(V)), Space: O(sum(V)).`  
**Editorial Alignment**: Dual problem formulation and state parameter swapping.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: Swapping objective function and state dimension when constraints are large but values are compact.
- **Reusable Pattern**: `Dual DP parameter inversion.`

---

[Back to Dynamic Programming (DP) Index](README.md) | [Back to Master Categories](../../README.md)
