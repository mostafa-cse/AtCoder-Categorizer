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

- **Role**: *1D State Recurrence / Bounded Lookahead*
- **Rating**: `600` | **Contest**: [`dp`](https://atcoder.jp/contests/dp/tasks/dp_a)
- **Full Analysis**: [AtCoder-dp_a Analysis](../../analysis/AtCoder-dp_a.md)

#### Problem Statement & Task
N stones are numbered 1 to N with heights h_i. Starting from stone 1, the frog can jump to stone i+1 or i+2 with cost |h_i - h_j|. Find minimum total cost to reach stone N.

#### Core Invariant & Observation
At stone i, arrival is possible exclusively from i-1 or i-2. The state depends only on local height differences and optimal prefix solutions. Space compresses to O(1).

#### Algorithmic Formulation
1. Initialize dp[1] = 0, dp[2] = |h_2 - h_1|.
2. For i from 3 to N: dp[i] = min(dp[i-1] + |h_i - h_{i-1}|, dp[i-2] + |h_i - h_{i-2}|).
3. Result is dp[N].

**Complexity**: `Time: O(N), Space: O(1) rolling state.`  
**Editorial Alignment**: Standard 1D forward relaxation recurrence.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: Optimal substructure, state initialization, and memory-compressed transitions.
- **Reusable Pattern**: `Linear 1D DP with constant lookback window.`

---

### 2. Frog 2 (`[problem:AtCoder-dp_b]`)

- **Role**: *1D DP with K-Step Transitions*
- **Rating**: `700` | **Contest**: [`dp`](https://atcoder.jp/contests/dp/tasks/dp_b)
- **Full Analysis**: [AtCoder-dp_b Analysis](../../analysis/AtCoder-dp_b.md)

#### Problem Statement & Task
Similar to Frog 1, but the frog can jump up to K stones forward (from i to i+j for 1 <= j <= K). Find min cost to reach stone N.

#### Core Invariant & Observation
Each state dp[i] is relaxed over a sliding window of the previous K states: dp[i] = min_{1 <= j <= K} (dp[i-j] + |h_i - h_{i-j}|).

#### Algorithmic Formulation
1. Set dp[1] = 0, others INF.
2. For i from 1 to N-1: for step in 1..K with i+step <= N: dp[i+step] = min(dp[i+step], dp[i] + |h_{i+step} - h_i|).
3. Result is dp[N].

**Complexity**: `Time: O(N * K), Space: O(N).`  
**Editorial Alignment**: Standard push-based relaxation over parameterized lookahead.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: Parameterized transition loops and boundary-bounded relaxation.
- **Reusable Pattern**: `Push DP over variable-sized transition intervals.`

---

### 3. Vacation (`[problem:AtCoder-dp_c]`)

- **Role**: *Multi-State DP / Consecutive Constraints*
- **Rating**: `900` | **Contest**: [`dp`](https://atcoder.jp/contests/dp/tasks/dp_c)
- **Full Analysis**: [AtCoder-dp_c Analysis](../../analysis/AtCoder-dp_c.md)

#### Problem Statement & Task
Choose activities A, B, or C over N days maximizing happiness, with the constraint that Taro cannot do the same activity two days in a row.

#### Core Invariant & Observation
Enforcing the constraint 'no two consecutive identical choices' requires augmenting the state with the identity of the last chosen activity.

#### Algorithmic Formulation
1. State: dp[day][act] where act in {0, 1, 2}.
2. dp[i][0] = a_i + max(dp[i-1][1], dp[i-1][2]), and symmetrically for 1 and 2.
3. Return max_{act} dp[N][act].

**Complexity**: `Time: O(N), Space: O(1) rolling state.`  
**Editorial Alignment**: Classic 3-state Markov transition graph.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: State augmentation for path-dependent constraints and state-machine DP.
- **Reusable Pattern**: `Categorical state-machine DP with mutually exclusive transitions.`

---

[Back to Dynamic Programming (DP) Index](README.md) | [Back to Master Categories](../../README.md)
