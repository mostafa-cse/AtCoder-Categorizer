# 📖 Bitmask DP & Submask Enumeration

- **Tag / Domain**: `Dynamic Programming (DP)`
- **Subtopic**: `Bit Related DP`
- **Total Curated Problems**: 2

---

## 💡 Topic Overview
Dynamic programming where subsets of elements are represented as integer bitmasks. Key techniques include popcount-based dimension reduction and exhaustive O(3^N) submask iteration.

---

## 🏆 Curated High-Value Problems

### 1. Matching (`[problem:AtCoder-dp_o]`)

- **Role**: *Bitmask DP*
- **Rating**: `1650` | **Contest**: [`dp`](https://atcoder.jp/contests/dp/tasks/dp_o)
- **Full Analysis**: [AtCoder-dp_o Analysis](../../analysis/AtCoder-dp_o.md)

#### Problem Statement & Task
Count perfect matchings in a bipartite graph with N men and N women (N <= 21).

#### Core Invariant & Observation
By iterating masks by popcount or sequentially from 0 to 2^N - 1, we eliminate the man dimension entirely: dp[mask | (1 << j)] += dp[mask].

#### Algorithmic Formulation
1. dp[0] = 1, all other dp = 0.
2. For mask from 0 to 2^N - 1: let i = popcount(mask). If i == N, continue.
3. For each woman j in 0..N-1: if compatible(i, j) and not (mask & (1 << j)): dp[mask | (1 << j)] = (dp[mask | (1 << j)] + dp[mask]) mod MOD.
4. Return dp[(1<<N) - 1].

**Complexity**: `Time: O(N * 2^N), Space: O(2^N).`  
**Editorial Alignment**: Popcount dimension-reduced bitmask DP.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: Dimension reduction in Bitmask DP using subset cardinality invariants.
- **Reusable Pattern**: `Popcount implicit state matching: i = popcount(mask).`

---

### 2. Grouping (`[problem:AtCoder-dp_u]`)

- **Role**: *Bitmask DP / O(3^N) Submask Enumeration*
- **Rating**: `1850` | **Contest**: [`dp`](https://atcoder.jp/contests/dp/tasks/dp_u)
- **Full Analysis**: [AtCoder-dp_u Analysis](../../analysis/AtCoder-dp_u.md)

#### Problem Statement & Task
Partition N rabbits into arbitrary groups to maximize total compatibility score (N <= 16).

#### Core Invariant & Observation
Iterating submasks via `sub = (sub - 1) & mask` visits each submask without redundant branches. Over all 2^N masks, total operations equal sum_{k=0}^N binom(N, k) 2^k = 3^N.

#### Algorithmic Formulation
1. Precompute score[mask] for all 2^N subsets.
2. Loop mask from 1 to 2^N - 1:
   sub = mask; while sub > 0: dp[mask] = max(dp[mask], score[sub] + dp[mask ^ sub]); sub = (sub - 1) & mask.
3. Return dp[(1<<N) - 1].

**Complexity**: `Time: O(3^N + N^2 * 2^N), Space: O(2^N).`  
**Editorial Alignment**: Textbook submask enumeration.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: The (sub - 1) & mask bit trick and set partition dynamic programming.
- **Reusable Pattern**: `O(3^N) submask iteration: sub = (sub - 1) & mask.`

---

[Back to Dynamic Programming (DP) Index](README.md) | [Back to Master Categories](../../README.md)
