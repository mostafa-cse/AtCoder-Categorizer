# 📖 1D State Recurrences & State Machines

- **Tag / Domain**: `Dynamic Programming (DP)`
- **Subtopic**: `Intro to DP`
- **Total Curated Problems**: 3

---

## 💡 Topic Overview
Foundational linear dynamic programming, bounded lookaheads, and categorical state machines enforcing consecutive action constraints.

---

## 🏆 Curated High-Value Problems

### 1. Frog 1 (`[problem:AtCoder-dp_a]`)

- **Role**: *Linear 1D DP with 2-Step Lookahead*
- **Rating**: `600` | **Contest**: [`dp`](https://atcoder.jp/contests/dp/tasks/dp_a)
- **Full Analysis**: [AtCoder-dp_a Analysis](../../analysis/AtCoder-dp_a.md)

#### Problem Statement & Task
Minimum jump cost to reach stone N jumping 1 or 2 stones.

#### Core Invariant & Observation
Arrival at stone i is strictly partitioned between i-1 and i-2.

#### Algorithmic Formulation
1. dp[1]=0, dp[2]=|h_2-h_1|.
2. Loop i from 3 to N.
3. Return dp[N].

**Complexity**: `Time: O(N), Space: O(1) rolling state.`  
**Editorial Alignment**: Standard 1D forward relaxation.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: Optimal substructure, state initialization, and memory-compressed transitions.
- **Reusable Pattern**: `Linear 1D DP with constant lookback window.`

---

### 2. Frog 2 (`[problem:AtCoder-dp_b]`)

- **Role**: *1D DP with K-Step Lookahead*
- **Rating**: `700` | **Contest**: [`dp`](https://atcoder.jp/contests/dp/tasks/dp_b)
- **Full Analysis**: [AtCoder-dp_b Analysis](../../analysis/AtCoder-dp_b.md)

#### Problem Statement & Task
Minimum jump cost jumping up to K stones.

#### Core Invariant & Observation
dp[i] = min_{1 <= j <= K} (dp[i-j] + |h_i - h_{i-j}|).

#### Algorithmic Formulation
Push DP forward from i to i+step for step in 1..K.

**Complexity**: `Time: O(N * K), Space: O(N).`  
**Editorial Alignment**: Parameterized push-style relaxation.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: Parameterized transition loops and boundary-bounded relaxation.
- **Reusable Pattern**: `Push DP over variable-sized transition intervals.`

---

### 3. Vacation (`[problem:AtCoder-dp_c]`)

- **Role**: *State-Machine Categorical DP*
- **Rating**: `900` | **Contest**: [`dp`](https://atcoder.jp/contests/dp/tasks/dp_c)
- **Full Analysis**: [AtCoder-dp_c Analysis](../../analysis/AtCoder-dp_c.md)

#### Problem Statement & Task
Maximize vacation happiness without repeating the same activity two days in a row.

#### Core Invariant & Observation
The last choice fully captures all history required by the constraint.

#### Algorithmic Formulation
dp[i][A] = a_i + max(dp[i-1][B], dp[i-1][C]), symmetrically for B, C.

**Complexity**: `Time: O(N), Space: O(1).`  
**Editorial Alignment**: 3-state Markov transition graph.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: State augmentation for path-dependent constraints and state-machine DP.
- **Reusable Pattern**: `Categorical state-machine DP with mutually exclusive transitions.`

---

[Back to Dynamic Programming (DP) Index](README.md) | [Back to Master Categories](../../README.md)
