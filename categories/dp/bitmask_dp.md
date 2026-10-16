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


### Simple Grouping (`[problem:AtCoder-typical90_as]`)

- **Role**: *Minimax Subset Partition Bitmask DP with O(3^N) Submask Iteration*
- **Rating**: `2150` (★6) | **Contest**: [`typical90`](https://atcoder.jp/contests/typical90/tasks/typical90_as)
- **Full Analysis**: [AtCoder-typical90_as Analysis](../../analysis/AtCoder-typical90_as.md)

#### Problem Statement & Task
N points in 2D plane (N <= 15). Partition points into K non-empty groups. Cost of a group is the maximum squared distance between any pair of points in the group. Minimize the maximum cost among all K groups.

#### Core Invariant & Observation
dp[k][mask] = min_{sub in mask} max(dp[k - 1][mask ^ sub], cost[sub]). Submask iteration sub = (sub - 1) & mask iterates all submasks in sum binom(N, i) 2^i = 3^N operations.

#### Algorithmic Formulation
1. Precompute cost[mask] for all 2^N subsets.
2. dp[1][mask] = cost[mask].
3. For step from 2 to K: for mask from 1 to 2^N - 1:
   sub = (mask - 1) & mask; while sub > 0: dp[step][mask] = min(dp[step][mask], max(dp[step - 1][mask ^ sub], cost[sub])); sub = (sub - 1) & mask.
4. Output dp[K][(1<<N) - 1].

**Complexity**: `Time: O(K * 3^N + N^2 * 2^N), Space: O(K * 2^N).`  
**Editorial Alignment**: O(3^N) submask iteration for minimax set partition DP.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: Minimax set partition dynamic programming, submask iteration idiom, and precomputing subset metric diameters.
- **Reusable Pattern**: `O(3^N) Minimax Subset Partition DP.`

---

[Back to Dynamic Programming (DP) Index](README.md) |
