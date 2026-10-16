# 📖 Prefix Sum Optimized DP

- **Tag / Domain**: `Dynamic Programming (DP)`
- **Subtopic**: `DP Optimizations`
- **Total Curated Problems**: 1

---

## 💡 Topic Overview
Accelerating polynomial transitions over contiguous state ranges from O(K) to O(1) using prefix sum arrays.

---

## 🏆 Curated High-Value Problems

### 1. Candies (`[problem:AtCoder-dp_m]`)

- **Role**: *Prefix Sum State Acceleration*
- **Rating**: `1550` | **Contest**: [`dp`](https://atcoder.jp/contests/dp/tasks/dp_m)
- **Full Analysis**: [AtCoder-dp_m Analysis](../../analysis/AtCoder-dp_m.md)

#### Problem Statement & Task
Distribute K candies among N children such that child i receives at most a_i candies.

#### Core Invariant & Observation
Prefix sums of the previous row evaluate the contiguous range sum in O(1), dropping overall complexity from O(N * K^2) to O(N * K).

#### Algorithmic Formulation
1. dp[0] = 1, others 0.
2. For each child i: compute prefix sums pref of current dp.
3. dp[j] = (pref[j+1] - pref[max(0, j - a_i)]) mod MOD.
4. Return dp[K].

**Complexity**: `Time: O(N * K), Space: O(K).`  
**Editorial Alignment**: Prefix sum acceleration of contiguous state transitions.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: Sliding window range sum optimization reducing quadratic transitions to linear.
- **Reusable Pattern**: `Prefix sum acceleration of contiguous state transitions.`

---

[Back to Dynamic Programming (DP) Index](README.md) | [Back to Master Categories](../../README.md)
