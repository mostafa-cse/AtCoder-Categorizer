# 📖 Prefix Sum Optimized DP

- **Tag / Domain**: `Dynamic Programming (DP)`
- **Subtopic**: `DP Optimizations`
- **Total Curated Problems**: 2

---

## 💡 Topic Overview
Accelerating contiguous state transitions from O(K) to O(1) via prefix sum maintenance on previous DP layers.

---

## 🏆 Curated High-Value Problems

### 1. Candies (`[problem:AtCoder-dp_m]`)

- **Role**: *Prefix Sum Optimized DP*
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

### 2. Permutation (`[problem:AtCoder-dp_t]`)

- **Role**: *Relative Order Insertion DP with Prefix Sums*
- **Rating**: `1950` | **Contest**: [`dp`](https://atcoder.jp/contests/dp/tasks/dp_t)
- **Full Analysis**: [AtCoder-dp_t Analysis](../../analysis/AtCoder-dp_t.md)

#### Problem Statement & Task
Given a signature string S of length N-1 with characters '<' and '>', count permutations p of 1..N satisfying p_i < p_{i+1} if S_i == '<' and p_i > p_{i+1} if S_i == '>'.

#### Core Invariant & Observation
If S[i-1] == '<', j must be greater than previous element's rank k. If '>', j must be <= k. Prefix sums evaluate the transition sum in O(1).

#### Algorithmic Formulation
1. dp[1][1] = 1.
2. For i from 2 to N: compute prefix sums pref of dp[i-1].
3. If S[i-2] == '<': dp[i][j] = pref[j-1]. If S[i-2] == '>': dp[i][j] = pref[i-1] - pref[j-1].
4. Return sum_{j=1}^N dp[N][j] mod MOD.

**Complexity**: `Time: O(N^2), Space: O(N).`  
**Editorial Alignment**: Relative order insertion DP with prefix sum acceleration.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: Constructing permutations by inserting elements into relative rank slots and optimizing transitions with prefix sums.
- **Reusable Pattern**: `Relative rank insertion DP + prefix sum acceleration.`

---

[Back to Dynamic Programming (DP) Index](README.md) | [Back to Master Categories](../../README.md)
