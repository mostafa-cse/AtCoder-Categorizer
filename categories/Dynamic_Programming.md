# 🧩 AtCoder Curriculum: Dynamic Programming (DP)

Curated collection of high-value problems in **Dynamic Programming (DP)** selected for teaching reusable competitive programming algorithms, structural observations, and mathematical invariants.

- **Total Curated Problems**: 21
- **Taxonomy Tier**: Tag (Domain Level)

---

## 📑 Table of Contents

- [Bit Related DP](#bit-related-dp)
  - [Bitmask DP](#bitmask-dp) (1 problems)
  - [Bitmask DP / O(3^N) Submask Enumeration](#bitmask-dp--o3n-submask-enumeration) (1 problems)
- [Classic DP](#classic-dp)
  - [Grid DP / Path Counting with Obstacles](#grid-dp--path-counting-with-obstacles) (1 problems)
  - [Interval DP / Range DP / Matrix Chain Multiplication (MCM)](#interval-dp--range-dp--matrix-chain-multiplication-mcm) (2 problems)
  - [Longest Common Subsequence & Backtracking](#longest-common-subsequence--backtracking) (1 problems)
- [Convex Hull Trick (CHT)](#convex-hull-trick-cht)
  - [Convex Hull Trick (CHT) and Dynamic CHT](#convex-hull-trick-cht-and-dynamic-cht) (1 problems)
- [DP Optimizations](#dp-optimizations)
  - [DP Optimization using Data Structures [Some Practice Problems]](#dp-optimization-using-data-structures-some-practice-problems) (1 problems)
  - [Prefix Sum Optimized DP](#prefix-sum-optimized-dp) (1 problems)
- [Digit DP](#digit-dp)
  - [Digit DP with Remainder State](#digit-dp-with-remainder-state) (1 problems)
- [Dp on Different Structures](#dp-on-different-structures)
  - [DP on Trees and DAGs](#dp-on-trees-and-dags) (2 problems)
  - [Matrix Exponentiation DP](#matrix-exponentiation-dp) (1 problems)
  - [Tree DP with Subtree Rerooting without Division](#tree-dp-with-subtree-rerooting-without-division) (1 problems)
- [Intro to DP](#intro-to-dp)
  - [1D DP with K-Step Transitions](#1d-dp-with-k-step-transitions) (1 problems)
  - [1D State Recurrence / Bounded Lookahead](#1d-state-recurrence--bounded-lookahead) (1 problems)
  - [Expected Value DP with Multi-Frequency States](#expected-value-dp-with-multi-frequency-states) (1 problems)
  - [Knapsack Dual State / Value as State](#knapsack-dual-state--value-as-state) (1 problems)
  - [Knapsack and Basic Dynamic Programming](#knapsack-and-basic-dynamic-programming) (1 problems)
  - [Multi-State DP / Consecutive Constraints](#multi-state-dp--consecutive-constraints) (1 problems)
  - [Probability and Expected Value DP](#probability-and-expected-value-dp) (1 problems)

---

## Bit Related DP

### Bitmask DP

#### Matching (`[problem:AtCoder-dp_o]`)
- **Rating / Difficulty**: 1650
- **Contest**: `dp` | [AtCoder Link](https://atcoder.jp/contests/dp/tasks/dp_o)
- **Detailed Analysis**: [`analysis/AtCoder-dp_o.md`](../analysis/AtCoder-dp_o.md)
- **Key Idea**: Count perfect matchings in a bipartite graph with N men and N women (N <= 21).
- **Core Observation**: When matching men 0, 1, ..., i-1, exactly i women must be matched. Thus, i = popcount(mask). The index of the active man is completely implicit in the bitmask!
- **Algorithm & Complexity**: Time: O(N * 2^N), Space: O(2^N).
- **What This Problem Teaches**: Eliminating a state dimension using subset cardinality invariants in bitmask DP.
- **Reusable Pattern**: `Popcount implicit state matching: i = popcount(mask).`

### Bitmask DP / O(3^N) Submask Enumeration

#### Grouping (`[problem:AtCoder-dp_u]`)
- **Rating / Difficulty**: 1850
- **Contest**: `dp` | [AtCoder Link](https://atcoder.jp/contests/dp/tasks/dp_u)
- **Detailed Analysis**: [`analysis/AtCoder-dp_u.md`](../analysis/AtCoder-dp_u.md)
- **Key Idea**: Partition N rabbits into arbitrary disjoint groups maximizing total compatibility score (N <= 16).
- **Core Observation**: Precompute standalone group scores in O(N^2 * 2^N). Then dp[mask] = max_{sub is submask of mask} (cost[sub] + dp[mask ^ sub]). The submask loop `sub = (sub - 1) & mask` iterates all submasks in sum_{k=0}^N binom(N, k) 2^k = 3^N total operations.
- **Algorithm & Complexity**: Time: O(3^N + N^2 * 2^N), Space: O(2^N).
- **What This Problem Teaches**: The (sub - 1) & mask bitwise trick and set partition dynamic programming.
- **Reusable Pattern**: `O(3^N) submask iteration: sub = (sub - 1) & mask.`

---

## Classic DP

### Grid DP / Path Counting with Obstacles

#### Grid 1 (`[problem:AtCoder-dp_h]`)
- **Rating / Difficulty**: 1050
- **Contest**: `dp` | [AtCoder Link](https://atcoder.jp/contests/dp/tasks/dp_h)
- **Detailed Analysis**: [`analysis/AtCoder-dp_h.md`](../analysis/AtCoder-dp_h.md)
- **Key Idea**: Count paths from top-left (1,1) to bottom-right (H,W) moving only right and down, avoiding obstacle walls.
- **Core Observation**: Transitions are purely local: dp[r][c] = (dp[r-1][c] + dp[r][c-1]) mod (10^9+7). Any obstacle cell '#' strictly resets dp[r][c] to 0.
- **Algorithm & Complexity**: Time: O(H * W), Space: O(W).
- **What This Problem Teaches**: Grid boundary enforcement, obstacle nullification, and modulo arithmetic accumulation.
- **Reusable Pattern**: `2D additive grid DP.`

### Interval DP / Range DP / Matrix Chain Multiplication (MCM)

#### Deque (`[problem:AtCoder-dp_l]`)
- **Rating / Difficulty**: 1400
- **Contest**: `dp` | [AtCoder Link](https://atcoder.jp/contests/dp/tasks/dp_l)
- **Detailed Analysis**: [`analysis/AtCoder-dp_l.md`](../analysis/AtCoder-dp_l.md)
- **Key Idea**: Two players take turns removing numbers from either end of an array. Player 1 maximizes X - Y, Player 2 minimizes it.
- **Core Observation**: For any remaining subsegment [l, r], the active player chooses either a_l or a_r to maximize their gain minus the opponent's outcome from the remaining interval: dp[l][r] = max(a_l - dp[l+1][r], a_r - dp[l][r-1]).
- **Algorithm & Complexity**: Time: O(N^2), Space: O(N^2).
- **What This Problem Teaches**: Interval dynamic programming (order of evaluation by length) and zero-sum minimax negation.
- **Reusable Pattern**: `Minimax interval DP: dp[l][r] = max(opt_left - dp[l+1][r], opt_right - dp[l][r-1]).`

#### Slimes (`[problem:AtCoder-dp_n]`)
- **Rating / Difficulty**: 1600
- **Contest**: `dp` | [AtCoder Link](https://atcoder.jp/contests/dp/tasks/dp_n)
- **Detailed Analysis**: [`analysis/AtCoder-dp_n.md`](../analysis/AtCoder-dp_n.md)
- **Key Idea**: Merge N slimes adjacent in a line into a single slime minimizing the sum of merging costs.
- **Core Observation**: The final merge combines two adjacent contiguous blocks [l, k] and [k+1, r]. The merge cost is always sum(a[l..r]). Therefore: dp[l][r] = sum(a[l..r]) + min_{l <= k < r} (dp[l][k] + dp[k+1][r]).
- **Algorithm & Complexity**: Time: O(N^3) standard, O(N^2) via Knuth's optimization.
- **What This Problem Teaches**: Interval DP with split-point minimization and cost of merging subproblems.
- **Reusable Pattern**: `Split-point interval DP.`

### Longest Common Subsequence & Backtracking

#### LCS (`[problem:AtCoder-dp_f]`)
- **Rating / Difficulty**: 1250
- **Contest**: `dp` | [AtCoder Link](https://atcoder.jp/contests/dp/tasks/dp_f)
- **Detailed Analysis**: [`analysis/AtCoder-dp_f.md`](../analysis/AtCoder-dp_f.md)
- **Key Idea**: Reconstruct and print the actual string corresponding to the Longest Common Subsequence of strings s and t.
- **Core Observation**: Standard 2D table computes optimal lengths. The sequence itself is uniquely extracted by tracing back from (len(s), len(t)) following optimal transition choices.
- **Algorithm & Complexity**: Time: O(|s| * |t|), Space: O(|s| * |t|).
- **What This Problem Teaches**: State path reconstruction and multi-dimensional backtracking.
- **Reusable Pattern**: `Optimal decision matrix traceback.`

---

## Convex Hull Trick (CHT)

### Convex Hull Trick (CHT) and Dynamic CHT

#### Frog 3 (`[problem:AtCoder-dp_z]`)
- **Rating / Difficulty**: 2200
- **Contest**: `dp` | [AtCoder Link](https://atcoder.jp/contests/dp/tasks/dp_z)
- **Detailed Analysis**: [`analysis/AtCoder-dp_z.md`](../analysis/AtCoder-dp_z.md)
- **Key Idea**: Jump between stones with quadratic cost (h_j - h_i)^2 + C where heights h_i are strictly increasing.
- **Core Observation**: Expanding (h_j - h_i)^2 + C gives h_j^2 + C + (h_i^2 + dp[i]) - 2 * h_j * h_i. This is a family of lines y = m_i * x + b_i where slope m_i = -2 * h_i is strictly decreasing. Slopes and query points x = h_j are both monotonic, allowing O(1) amortized deque maintenance.
- **Algorithm & Complexity**: Time: O(N), Space: O(N).
- **What This Problem Teaches**: Geometric line lower envelope maintenance, convex hull deque operations, and linearizing quadratic DP costs.
- **Reusable Pattern**: `Monotonic Convex Hull Trick (CHT).`

---

## DP Optimizations

### DP Optimization using Data Structures [Some Practice Problems]

#### Flowers (`[problem:AtCoder-dp_q]`)
- **Rating / Difficulty**: 1600
- **Contest**: `dp` | [AtCoder Link](https://atcoder.jp/contests/dp/tasks/dp_q)
- **Detailed Analysis**: [`analysis/AtCoder-dp_q.md`](../analysis/AtCoder-dp_q.md)
- **Key Idea**: Find an increasing subsequence of flower heights that maximizes total beauty.
- **Core Observation**: dp[h_i] = a_i + max_{0 <= h < h_i} dp[h]. Querying max in [0, h_i - 1] and updating point h_i is dynamically solved in O(log N) by a Fenwick or Segment Tree.
- **Algorithm & Complexity**: Time: O(N log N), Space: O(N).
- **What This Problem Teaches**: Transforming quadratic inner-loop search into dynamic range queries via data structures.
- **Reusable Pattern**: `BIT/Segment Tree accelerated DP.`

### Prefix Sum Optimized DP

#### Candies (`[problem:AtCoder-dp_m]`)
- **Rating / Difficulty**: 1550
- **Contest**: `dp` | [AtCoder Link](https://atcoder.jp/contests/dp/tasks/dp_m)
- **Detailed Analysis**: [`analysis/AtCoder-dp_m.md`](../analysis/AtCoder-dp_m.md)
- **Key Idea**: Distribute K candies among N children such that child i receives at most a_i candies.
- **Core Observation**: Naively, dp[i][j] = sum_{k=0}^{a_i} dp[i-1][j-k] requires O(N * K^2). The inner sum is over a contiguous range [max(0, j - a_i), j] in the previous row, which prefix sums compute in O(1).
- **Algorithm & Complexity**: Time: O(N * K), Space: O(K).
- **What This Problem Teaches**: Sliding window range sum optimization reducing quadratic transitions to linear.
- **Reusable Pattern**: `Prefix sum acceleration of contiguous state transitions.`

---

## Digit DP

### Digit DP with Remainder State

#### Digit Sum (`[problem:AtCoder-dp_s]`)
- **Rating / Difficulty**: 1750
- **Contest**: `dp` | [AtCoder Link](https://atcoder.jp/contests/dp/tasks/dp_s)
- **Detailed Analysis**: [`analysis/AtCoder-dp_s.md`](../analysis/AtCoder-dp_s.md)
- **Key Idea**: Count positive integers up to K (K <= 10^10000) whose sum of digits is a multiple of D.
- **Core Observation**: K has up to 10,000 digits! Process digits from most significant to least significant, maintaining the remainder of the digit sum mod D, and a boolean flag `tight` indicating whether the prefix matches K.
- **Algorithm & Complexity**: Time: O(|K| * D * 10), Space: O(|K| * D).
- **What This Problem Teaches**: Digit-by-digit construction, tight prefix bound handling, and large integer parsing.
- **Reusable Pattern**: `Standard Digit DP state tuple (index, remainder, is_tight).`

---

## Dp on Different Structures

### DP on Trees and DAGs

#### Longest Path (`[problem:AtCoder-dp_g]`)
- **Rating / Difficulty**: 1350
- **Contest**: `dp` | [AtCoder Link](https://atcoder.jp/contests/dp/tasks/dp_g)
- **Detailed Analysis**: [`analysis/AtCoder-dp_g.md`](../analysis/AtCoder-dp_g.md)
- **Key Idea**: Find the length of the longest directed path in a Directed Acyclic Graph (DAG).
- **Core Observation**: In a DAG, cycles are absent; topological ordering guarantees a well-founded recursion. The longest path starting at u is dp[u] = 1 + max_{(u, v) in E} dp[v].
- **Algorithm & Complexity**: Time: O(V + E), Space: O(V + E).
- **What This Problem Teaches**: Topological order as the universal prerequisite for acyclic graph dynamic programming.
- **Reusable Pattern**: `DAG memoized DFS transition.`

#### Independent Set (`[problem:AtCoder-dp_p]`)
- **Rating / Difficulty**: 1500
- **Contest**: `dp` | [AtCoder Link](https://atcoder.jp/contests/dp/tasks/dp_p)
- **Detailed Analysis**: [`analysis/AtCoder-dp_p.md`](../analysis/AtCoder-dp_p.md)
- **Key Idea**: Count ways to paint vertices of a tree black or white such that no two adjacent vertices are both black.
- **Core Observation**: Root tree arbitrarily. If node u is Black, all children must be White. If u is White, each child can be independently either Black or White.
- **Algorithm & Complexity**: Time: O(N), Space: O(N).
- **What This Problem Teaches**: Subtree DP, child product combinations, and color state branching on trees.
- **Reusable Pattern**: `Two-state subtree product DP on trees.`

### Matrix Exponentiation DP

#### Walk (`[problem:AtCoder-dp_r]`)
- **Rating / Difficulty**: 1700
- **Contest**: `dp` | [AtCoder Link](https://atcoder.jp/contests/dp/tasks/dp_r)
- **Detailed Analysis**: [`analysis/AtCoder-dp_r.md`](../analysis/AtCoder-dp_r.md)
- **Key Idea**: Count paths of exact length K (K <= 10^18) in a directed graph of N vertices (N <= 50).
- **Core Observation**: The number of paths of length K between all pairs of vertices is given by A^K, where A is the adjacency matrix of the graph. Matrix multiplication computes transitions; binary exponentiation solves K <= 10^18 in O(log K) steps.
- **Algorithm & Complexity**: Time: O(N^3 log K), Space: O(N^2).
- **What This Problem Teaches**: Formulating linear state recurrences as matrix products and exponentiating large step counts.
- **Reusable Pattern**: `Matrix exponentiation DP for enormous transition steps.`

### Tree DP with Subtree Rerooting without Division

#### Subtree (`[problem:AtCoder-dp_v]`)
- **Rating / Difficulty**: 2100
- **Contest**: `dp` | [AtCoder Link](https://atcoder.jp/contests/dp/tasks/dp_v)
- **Detailed Analysis**: [`analysis/AtCoder-dp_v.md`](../analysis/AtCoder-dp_v.md)
- **Key Idea**: For every node v in a tree, compute the number of black-connected components containing v modulo M (M may not be prime).
- **Core Observation**: Because M is not necessarily prime, division by (down[child] + 1) is invalid! Computing prefix and suffix products of children values allows excluding a child in O(1) without modular division.
- **Algorithm & Complexity**: Time: O(N), Space: O(N).
- **What This Problem Teaches**: Tree rerooting without modular division via prefix/suffix product arrays.
- **Reusable Pattern**: `Division-free prefix/suffix rerooting on trees.`

---

## Intro to DP

### 1D DP with K-Step Transitions

#### Frog 2 (`[problem:AtCoder-dp_b]`)
- **Rating / Difficulty**: 700
- **Contest**: `dp` | [AtCoder Link](https://atcoder.jp/contests/dp/tasks/dp_b)
- **Detailed Analysis**: [`analysis/AtCoder-dp_b.md`](../analysis/AtCoder-dp_b.md)
- **Key Idea**: Generalize jumps from 2 stones to up to K stones with minimum total energy cost.
- **Core Observation**: Each state dp[i] is relaxed over a sliding window of the previous K states: dp[i] = min_{1 <= j <= K} (dp[i-j] + |h_i - h_{i-j}|).
- **Algorithm & Complexity**: Time: O(N * K), Space: O(N).
- **What This Problem Teaches**: Parameterized transition loops and boundary-bounded relaxation.
- **Reusable Pattern**: `Push DP over variable-sized transition intervals.`

### 1D State Recurrence / Bounded Lookahead

#### Frog 1 (`[problem:AtCoder-dp_a]`)
- **Rating / Difficulty**: 600
- **Contest**: `dp` | [AtCoder Link](https://atcoder.jp/contests/dp/tasks/dp_a)
- **Detailed Analysis**: [`analysis/AtCoder-dp_a.md`](../analysis/AtCoder-dp_a.md)
- **Key Idea**: Determine the minimum jump cost to reach stone N where each jump can span 1 or 2 stones.
- **Core Observation**: At stone i, arrival is possible exclusively from i-1 or i-2. The state depends only on local height differences |h_i - h_{i-k}| and optimal prefix solutions.
- **Algorithm & Complexity**: Time: O(N), Space: O(1) rolling state.
- **What This Problem Teaches**: Optimal substructure, state initialization, and memory-compressed transitions.
- **Reusable Pattern**: `Linear 1D DP with constant lookback window.`

### Expected Value DP with Multi-Frequency States

#### Sushi (`[problem:AtCoder-dp_j]`)
- **Rating / Difficulty**: 1650
- **Contest**: `dp` | [AtCoder Link](https://atcoder.jp/contests/dp/tasks/dp_j)
- **Detailed Analysis**: [`analysis/AtCoder-dp_j.md`](../analysis/AtCoder-dp_j.md)
- **Key Idea**: N plates have 1, 2, or 3 sushi. Repeatedly pick a random plate until all sushi are eaten. Find expected number of operations.
- **Core Observation**: The plate identity does not matter! Only the count of plates having 1 sushi (c1), 2 sushi (c2), and 3 sushi (c3) determines the system state. Picking an empty plate loops back to the same state (self-loop), which can be eliminated algebraically.
- **Algorithm & Complexity**: Time: O(N^3), Space: O(N^3).
- **What This Problem Teaches**: State compression by value multiplicity and algebraic self-loop elimination in expected value DP.
- **Reusable Pattern**: `Self-loop elimination: E = (1 + \sum P_i E_i) / (1 - P_{self}).`

### Knapsack Dual State / Value as State

#### Knapsack 2 (`[problem:AtCoder-dp_e]`)
- **Rating / Difficulty**: 1450
- **Contest**: `dp` | [AtCoder Link](https://atcoder.jp/contests/dp/tasks/dp_e)
- **Detailed Analysis**: [`analysis/AtCoder-dp_e.md`](../analysis/AtCoder-dp_e.md)
- **Key Idea**: Solve 0/1 Knapsack when capacity W <= 10^9 is enormous, but item values v_i <= 1000 and N <= 100.
- **Core Observation**: Max total value V_max <= 100 * 1000 = 10^5. Invert the DP formulation: define dp[v] as the minimum weight required to achieve exact total value v.
- **Algorithm & Complexity**: Time: O(N * sum(V)), Space: O(sum(V)).
- **What This Problem Teaches**: Swapping objective function and state dimension when constraints are large but values are compact.
- **Reusable Pattern**: `Dual DP parameter inversion.`

### Knapsack and Basic Dynamic Programming

#### Knapsack 1 (`[problem:AtCoder-dp_d]`)
- **Rating / Difficulty**: 1150
- **Contest**: `dp` | [AtCoder Link](https://atcoder.jp/contests/dp/tasks/dp_d)
- **Detailed Analysis**: [`analysis/AtCoder-dp_d.md`](../analysis/AtCoder-dp_d.md)
- **Key Idea**: Maximize total value of items within knapsack capacity W <= 10^5 where each item can be selected at most once.
- **Core Observation**: Capacity is moderate (W <= 10^5). By iterating weight downwards from W to w_i, 1D array space is sufficient without using an item multiple times.
- **Algorithm & Complexity**: Time: O(N * W), Space: O(W).
- **What This Problem Teaches**: Reverse-order state traversal to prevent unbounded repetition in subset selection.
- **Reusable Pattern**: `1D space-optimized 0/1 knapsack.`

### Multi-State DP / Consecutive Constraints

#### Vacation (`[problem:AtCoder-dp_c]`)
- **Rating / Difficulty**: 900
- **Contest**: `dp` | [AtCoder Link](https://atcoder.jp/contests/dp/tasks/dp_c)
- **Detailed Analysis**: [`analysis/AtCoder-dp_c.md`](../analysis/AtCoder-dp_c.md)
- **Key Idea**: Maximize vacation happiness over N days choosing between three activities (A, B, C) without doing the same activity two days in a row.
- **Core Observation**: Enforcing the constraint 'no two consecutive identical choices' requires augmenting the state with the identity of the last chosen activity.
- **Algorithm & Complexity**: Time: O(N), Space: O(1) rolling state.
- **What This Problem Teaches**: State augmentation for path-dependent constraints and state-machine DP.
- **Reusable Pattern**: `Categorical state-machine DP with mutually exclusive transitions.`

### Probability and Expected Value DP

#### Coins (`[problem:AtCoder-dp_i]`)
- **Rating / Difficulty**: 1150
- **Contest**: `dp` | [AtCoder Link](https://atcoder.jp/contests/dp/tasks/dp_i)
- **Detailed Analysis**: [`analysis/AtCoder-dp_i.md`](../analysis/AtCoder-dp_i.md)
- **Key Idea**: Calculate the exact probability that more heads than tails appear when tossing N independent biased coins.
- **Core Observation**: Let dp[i][j] be the probability of obtaining exactly j heads after i coin tosses. The outcome of coin i partitions probability mass into two independent events: heads (prob p_i) or tails (prob 1 - p_i).
- **Algorithm & Complexity**: Time: O(N^2), Space: O(N).
- **What This Problem Teaches**: Probability mass conservation and floating-point accumulation in discrete trial DP.
- **Reusable Pattern**: `Probability convolution DP over independent Bernoulli trials.`

---
