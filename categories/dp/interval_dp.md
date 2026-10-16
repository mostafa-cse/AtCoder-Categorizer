# 📖 Interval DP & Range Merging

- **Tag / Domain**: `Dynamic Programming (DP)`
- **Subtopic**: `Classic DP`
- **Total Curated Problems**: 3

---

## 💡 Topic Overview
Subproblems defined over contiguous intervals [l, r], solved by increasing interval length. Covers minimax game intervals, LCS backtracking, and optimal split-point merges.

---

## 🏆 Curated High-Value Problems

### 1. LCS (`[problem:AtCoder-dp_f]`)

- **Role**: *Longest Common Subsequence & Backtracking*
- **Rating**: `1250` | **Contest**: [`dp`](https://atcoder.jp/contests/dp/tasks/dp_f)
- **Full Analysis**: [AtCoder-dp_f Analysis](../../analysis/AtCoder-dp_f.md)

#### Problem Statement & Task
Given two strings s and t, find and print the actual string corresponding to their Longest Common Subsequence.

#### Core Invariant & Observation
Standard 2D table computes optimal lengths. The sequence itself is uniquely extracted by tracing back from (len(s), len(t)) following optimal transition choices.

#### Algorithmic Formulation
1. Compute dp[i][j]: if s[i-1] == t[j-1] -> dp[i-1][j-1]+1; else max(dp[i-1][j], dp[i][j-1]).
2. Traceback: if s[i-1] == t[j-1]: append s[i-1], i--, j--; else if dp[i-1][j] >= dp[i][j-1]: i--; else j--.
3. Reverse characters.

**Complexity**: `Time: O(|s| * |t|), Space: O(|s| * |t|).`  
**Editorial Alignment**: Full 2D DP matrix traceback.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: State path reconstruction and multi-dimensional backtracking.
- **Reusable Pattern**: `Optimal decision matrix traceback.`

---

### 2. Deque (`[problem:AtCoder-dp_l]`)

- **Role**: *Interval DP / Range DP / Matrix Chain Multiplication (MCM)*
- **Rating**: `1400` | **Contest**: [`dp`](https://atcoder.jp/contests/dp/tasks/dp_l)
- **Full Analysis**: [AtCoder-dp_l Analysis](../../analysis/AtCoder-dp_l.md)

#### Problem Statement & Task
Two players remove numbers from either end of an array. Player 1 maximizes X - Y, Player 2 minimizes it.

#### Core Invariant & Observation
Zero-sum game with symmetric negation: your advantage equals your chosen element minus opponent's optimal advantage from remaining subinterval.

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

### 3. Slimes (`[problem:AtCoder-dp_n]`)

- **Role**: *Interval DP / Range DP / Matrix Chain Multiplication (MCM)*
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


### Pick Two (`[problem:AtCoder-typical90_s]`)

- **Role**: *Interval DP / Elimination and Outer Pairing*
- **Rating**: `2100` (★6) | **Contest**: [`typical90`](https://atcoder.jp/contests/typical90/tasks/typical90_s)
- **Full Analysis**: [AtCoder-typical90_s Analysis](../../analysis/AtCoder-typical90_s.md)

#### Problem Statement & Task
2N integers are arranged in a row. Repeatedly remove an adjacent pair (x, y) with cost |x - y| until all numbers are removed. Find minimum total cost.

#### Core Invariant & Observation
For an interval [l, r] of even length, either the boundary elements l and r are matched together at cost |A[l] - A[r]| + dp[l+1][r-1], or the interval decomposes into two independent sub-eliminations dp[l][k] + dp[k+1][r].

#### Algorithmic Formulation
1. dp[l][r]: min cost to eliminate subarray A[l..r].
2. Base: dp[i][i+1] = |A[i] - A[i+1]|.
3. Loop len from 4 to 2N by 2:
   - Loop l from 1 to 2N - len + 1, r = l + len - 1:
     - dp[l][r] = |A[l] - A[r]| + dp[l+1][r-1]
     - for k in l+1..r-2 step 2: dp[l][r] = min(dp[l][r], dp[l][k] + dp[k+1][r])
4. Output dp[1][2N].

**Complexity**: `Time: O((2N)^3) = O(N^3), Space: O(N^2).`  
**Editorial Alignment**: Interval dynamic programming with boundary pairing and split-point relaxation.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: Interval DP formulation for nested reduction problems and optimal pairing structures.
- **Reusable Pattern**: `Boundary Pairing & Split Interval DP.`

---

[Back to Dynamic Programming (DP) Index](README.md) |
