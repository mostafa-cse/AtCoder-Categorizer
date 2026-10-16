# 📖 Greedy Exchange Argument & Knapsack DP

- **Tag / Domain**: `Dynamic Programming (DP)`
- **Subtopic**: `Classic DP`
- **Total Curated Problems**: 1

---

## 💡 Topic Overview
Establishing a strict canonical processing order via adjacent exchange arguments before applying 0/1 Knapsack dynamic programming.

---

## 🏆 Curated High-Value Problems

### 1. Tower (`[problem:AtCoder-dp_x]`)

- **Role**: *Greedy Exchange Argument + 0/1 Knapsack DP*
- **Rating**: `2250` | **Contest**: [`dp`](https://atcoder.jp/contests/dp/tasks/dp_x)
- **Full Analysis**: [AtCoder-dp_x Analysis](../../analysis/AtCoder-dp_x.md)

#### Problem Statement & Task
N blocks have weight w_i, solidness s_i, and value v_i. Tower can be built if each block's solidness is >= sum of weights of blocks above it. Maximize total value.

#### Core Invariant & Observation
Once sorted by w_i + s_i, the problem reduces to a 0/1 Knapsack where a block can only be added if accumulated weight w <= s_i.

#### Algorithmic Formulation
1. Sort blocks ascending by w_i + s_i.
2. Maintain dp[weight] = max value.
3. For each block i: for w from s_i down to 0: dp[w + w_i] = max(dp[w + w_i], dp[w] + v_i).
4. Return max(dp).

**Complexity**: `Time: O(N log N + N * max(S)), Space: O(max(S)).`  
**Editorial Alignment**: Greedy exchange argument establishes canonical topological order for Knapsack DP.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: Pairwise exchange arguments (deriving s_i + w_i invariant) combined with 0/1 knapsack.
- **Reusable Pattern**: `Exchange argument pre-sorting + Knapsack DP.`

---

[Back to Dynamic Programming (DP) Index](README.md) | [Back to Master Categories](../../README.md)
