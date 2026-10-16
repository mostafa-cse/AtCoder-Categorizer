# 📖 Interval DP & Range Merging

- **Tag / Domain**: `Dynamic Programming (DP)`
- **Subtopic**: `Classic DP`
- **Total Curated Problems**: 2

---

## 💡 Topic Overview
Subproblems defined over contiguous intervals [l, r], solved by increasing interval length. Covers minimax game intervals and optimal split-point merges.

---

## 🏆 Curated High-Value Problems

### 1. Deque (`[problem:AtCoder-dp_l]`)

- **Role**: *Minimax Game Interval DP*
- **Rating**: `1400` | **Contest**: [`dp`](https://atcoder.jp/contests/dp/tasks/dp_l)
- **Full Analysis**: [AtCoder-dp_l Analysis](../../analysis/AtCoder-dp_l.md)

#### Problem Statement & Task
Two players remove numbers from either end of an array. Player 1 maximizes X - Y, Player 2 minimizes it.

#### Core Invariant & Observation
The game is zero-sum. Negation accounts for player alternation: your score advantage equals your choice minus the opponent's optimal advantage from the remainder.

#### Algorithmic Formulation
1. Base: dp[i][i] = a_i.
2. Loop len from 2 to N: loop l from 1 to N-len+1: r = l+len-1: dp[l][r] = max(a_l - dp[l+1][r], a_r - dp[l][r-1]).
3. Return dp[1][N].

**Complexity**: `Time: O(N^2), Space: O(N^2).`  
**Editorial Alignment**: Zero-sum minimax interval DP.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: Interval dynamic programming evaluated by segment length and minimax negation.
- **Reusable Pattern**: `Minimax interval DP: dp[l][r] = max(opt_left - dp[l+1][r], opt_right - dp[l][r-1]).`

---

### 2. Slimes (`[problem:AtCoder-dp_n]`)

- **Role**: *Matrix Chain Multiplication / Split-Point Range DP*
- **Rating**: `1600` | **Contest**: [`dp`](https://atcoder.jp/contests/dp/tasks/dp_n)
- **Full Analysis**: [AtCoder-dp_n Analysis](../../analysis/AtCoder-dp_n.md)

#### Problem Statement & Task
Merge adjacent slimes pairwise into one slime with minimum total combination cost.

#### Core Invariant & Observation
dp[l][r] = sum(a[l..r]) + min_{l <= k < r} (dp[l][k] + dp[k+1][r]). Prefix sums yield sum(a[l..r]) in O(1).

#### Algorithmic Formulation
1. Precompute prefix sums.
2. For len = 2..N: for l = 1..N-len+1: r = l+len-1: dp[l][r] = min_{k=l}^{r-1}(dp[l][k] + dp[k+1][r]) + (pref[r] - pref[l-1]).
3. Return dp[1][N].

**Complexity**: `Time: O(N^3) standard, O(N^2) via Knuth optimization.`  
**Editorial Alignment**: Optimal binary search tree / matrix chain multiplication DP.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: Interval DP with split-point minimization and cost of merging subproblems.
- **Reusable Pattern**: `Split-point interval DP.`

---

[Back to Dynamic Programming (DP) Index](README.md) | [Back to Master Categories](../../README.md)
