# 🧩 AtCoder Curriculum: Dynamic Programming (DP)

Curated collection of high-value problems in **Dynamic Programming (DP)** selected for teaching reusable competitive programming algorithms, structural observations, and mathematical invariants.

- **Total Curated Problems**: 24
- **Taxonomy Tier**: Tag (Domain Level)

---

## 📑 Table of Contents

- [Bit Related DP](#bit-related-dp)
  - [Bitmask DP](#bitmask-dp) (1 problems)
  - [Bitmask DP / O(3^N) Submask Enumeration](#bitmask-dp-o-3-n-submask-enumeration) (1 problems)
- [Classic DP](#classic-dp)
  - [Grid DP / Path Counting with Obstacles](#grid-dp-path-counting-with-obstacles) (1 problems)
  - [Interval DP / Range DP / Matrix Chain Multiplication (MCM)](#interval-dp-range-dp-matrix-chain-multiplication-mcm) (2 problems)
  - [Longest Common Subsequence & Backtracking](#longest-common-subsequence-backtracking) (1 problems)
- [Convex Hull Trick (CHT)](#convex-hull-trick-cht)
  - [Convex Hull Trick (CHT) and Dynamic CHT](#convex-hull-trick-cht-and-dynamic-cht) (1 problems)
- [DP Optimizations](#dp-optimizations)
  - [DP Optimization using Data Structures [Some Practice Problems]](#dp-optimization-using-data-structures-some-practice-problems) (1 problems)
  - [Lazy Segment Tree Range-Add Point-Query DP](#lazy-segment-tree-range-add-point-query-dp) (1 problems)
  - [Prefix Sum Optimized DP](#prefix-sum-optimized-dp) (1 problems)
  - [Relative Order Insertion DP with Prefix Sums](#relative-order-insertion-dp-with-prefix-sums) (1 problems)
- [Digit DP](#digit-dp)
  - [Digit DP with Remainder State](#digit-dp-with-remainder-state) (1 problems)
- [Dp on Different Structures](#dp-on-different-structures)
  - [DP on Trees and DAGs](#dp-on-trees-and-dags) (2 problems)
  - [Matrix Exponentiation DP](#matrix-exponentiation-dp) (1 problems)
  - [Tree DP with Subtree Rerooting without Division](#tree-dp-with-subtree-rerooting-without-division) (1 problems)
- [Intro to DP](#intro-to-dp)
  - [1D DP with K-Step Transitions](#1d-dp-with-k-step-transitions) (1 problems)
  - [1D State Recurrence / Bounded Lookahead](#1d-state-recurrence-bounded-lookahead) (1 problems)
  - [Expected Value DP with Multi-Frequency States](#expected-value-dp-with-multi-frequency-states) (1 problems)
  - [Greedy Exchange Argument + 0/1 Knapsack DP](#greedy-exchange-argument-0-1-knapsack-dp) (1 problems)
  - [Knapsack Dual State / Value as State](#knapsack-dual-state-value-as-state) (1 problems)
  - [Knapsack and Basic Dynamic Programming](#knapsack-and-basic-dynamic-programming) (1 problems)
  - [Multi-State DP / Consecutive Constraints](#multi-state-dp-consecutive-constraints) (1 problems)
  - [Probability and Expected Value DP](#probability-and-expected-value-dp) (1 problems)

---

## Bit Related DP

### Bitmask DP

#### Matching (`[problem:AtCoder-dp_o]`)
- **Rating / Difficulty**: 1650
- **Contest**: `dp` | [AtCoder Link](https://atcoder.jp/contests/dp/tasks/dp_o)
- **Detailed Analysis**: [`analysis/AtCoder-dp_o.md`](../analysis/AtCoder-dp_o.md)
- **Key Idea**: When matching men 0, 1, ..., i-1, exactly i women must be chosen. Thus, i = popcount(mask). The index of the active man is implicit in the bitmask!
- **Core Observation**: By iterating masks by popcount or sequentially from 0 to 2^N - 1, we eliminate the man dimension entirely: dp[mask | (1 << j)] += dp[mask].
- **Algorithm & Complexity**: Time: O(N * 2^N), Space: O(2^N).
- **What This Problem Teaches**: Dimension reduction in Bitmask DP using subset cardinality invariants.
- **Reusable Pattern**: `Popcount implicit state matching: i = popcount(mask).`

### Bitmask DP / O(3^N) Submask Enumeration

#### Grouping (`[problem:AtCoder-dp_u]`)
- **Rating / Difficulty**: 1850
- **Contest**: `dp` | [AtCoder Link](https://atcoder.jp/contests/dp/tasks/dp_u)
- **Detailed Analysis**: [`analysis/AtCoder-dp_u.md`](../analysis/AtCoder-dp_u.md)
- **Key Idea**: Precompute standalone group scores in O(N^2 * 2^N). Then dp[mask] = max_{sub is submask of mask} (score[sub] + dp[mask ^ sub]).
- **Core Observation**: Iterating submasks via `sub = (sub - 1) & mask` visits each submask without redundant branches. Over all 2^N masks, total operations equal sum_{k=0}^N binom(N, k) 2^k = 3^N.
- **Algorithm & Complexity**: Time: O(3^N + N^2 * 2^N), Space: O(2^N).
- **What This Problem Teaches**: The (sub - 1) & mask bit trick and set partition dynamic programming.
- **Reusable Pattern**: `O(3^N) submask iteration: sub = (sub - 1) & mask.`

---

## Classic DP

### Grid DP / Path Counting with Obstacles

#### Grid 1 (`[problem:AtCoder-dp_h]`)
- **Rating / Difficulty**: 1050
- **Contest**: `dp` | [AtCoder Link](https://atcoder.jp/contests/dp/tasks/dp_h)
- **Detailed Analysis**: [`analysis/AtCoder-dp_h.md`](../analysis/AtCoder-dp_h.md)
- **Key Idea**: Transitions are purely local: dp[r][c] = (dp[r-1][c] + dp[r][c-1]) mod (10^9+7). Any obstacle cell '#' strictly resets dp[r][c] to 0.
- **Core Observation**: Transitions are purely local: dp[r][c] = (dp[r-1][c] + dp[r][c-1]) mod (10^9+7). Any obstacle cell '#' strictly resets dp[r][c] to 0.
- **Algorithm & Complexity**: Time: O(H * W), Space: O(W).
- **What This Problem Teaches**: Grid boundary enforcement, obstacle nullification, and modulo arithmetic accumulation.
- **Reusable Pattern**: `2D additive grid DP.`

### Interval DP / Range DP / Matrix Chain Multiplication (MCM)

#### Deque (`[problem:AtCoder-dp_l]`)
- **Rating / Difficulty**: 1400
- **Contest**: `dp` | [AtCoder Link](https://atcoder.jp/contests/dp/tasks/dp_l)
- **Detailed Analysis**: [`analysis/AtCoder-dp_l.md`](../analysis/AtCoder-dp_l.md)
- **Key Idea**: Over remaining subsegment [l, r], the active player chooses either a_l or a_r: dp[l][r] = max(a_l - dp[l+1][r], a_r - dp[l][r-1]).
- **Core Observation**: Zero-sum game with symmetric negation: your advantage equals your chosen element minus opponent's optimal advantage from remaining subinterval.
- **Algorithm & Complexity**: Time: O(N^2), Space: O(N^2).
- **What This Problem Teaches**: Interval dynamic programming evaluated by segment length and minimax negation.
- **Reusable Pattern**: `Minimax interval DP: dp[l][r] = max(opt_left - dp[l+1][r], opt_right - dp[l][r-1]).`

#### Slimes (`[problem:AtCoder-dp_n]`)
- **Rating / Difficulty**: 1600
- **Contest**: `dp` | [AtCoder Link](https://atcoder.jp/contests/dp/tasks/dp_n)
- **Detailed Analysis**: [`analysis/AtCoder-dp_n.md`](../analysis/AtCoder-dp_n.md)
- **Key Idea**: The final combine step joins two sub-blocks [l, k] and [k+1, r] with cost sum(a[l..r]).
- **Core Observation**: dp[l][r] = sum(a[l..r]) + min_{l <= k < r} (dp[l][k] + dp[k+1][r]). Prefix sums yield sum(a[l..r]) in O(1).
- **Algorithm & Complexity**: Time: O(N^3) standard, O(N^2) via Knuth optimization.
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
- **Key Idea**: Expand (h_j - h_i)^2 + C = h_j^2 + C + (h_i^2 + dp[i]) - 2 * h_j * h_i. For fixed j, this is min_i (m_i * x + b_i) with slope m_i = -2 * h_i and x = h_j.
- **Core Observation**: Since heights h_i are strictly increasing, slopes are strictly decreasing and query points are strictly increasing. A deque maintains the lower convex hull in O(1) amortized time per query.
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
- **Key Idea**: dp[h_i] = a_i + max_{0 <= h < h_i} dp[h]. Querying max in [0, h_i - 1] and updating point h_i is dynamically solved in O(log N) by a Fenwick or Segment Tree.
- **Core Observation**: Transforming quadratic inner-loop search into dynamic range queries via data structures.
- **Algorithm & Complexity**: Time: O(N log N), Space: O(N).
- **What This Problem Teaches**: Transforming quadratic inner-loop search into dynamic range queries via data structures.
- **Reusable Pattern**: `BIT/Segment Tree accelerated DP.`

### Lazy Segment Tree Range-Add Point-Query DP

#### Intervals (`[problem:AtCoder-dp_w]`)
- **Rating / Difficulty**: 2350
- **Contest**: `dp` | [AtCoder Link](https://atcoder.jp/contests/dp/tasks/dp_w)
- **Detailed Analysis**: [`analysis/AtCoder-dp_w.md`](../analysis/AtCoder-dp_w.md)
- **Key Idea**: DP where state is the position of the last '1'. Maintain dp[j] in a Lazy Segment Tree. When scanning i from 1 to N, for each interval ending at i, add its score a to range [l, i].
- **Core Observation**: If the previous '1' is at position j in [l, i], the interval is satisfied. Adding a to range [l, i] updates all valid previous positions in O(log N). dp[i] = max_{0 <= j < i} dp[j].
- **Algorithm & Complexity**: Time: O((N + M) log N), Space: O(N).
- **What This Problem Teaches**: Using Lazy Segment Tree to dynamically update previous state transitions across ranges of active intervals.
- **Reusable Pattern**: `Lazy Segment Tree accelerated range-event DP.`

### Prefix Sum Optimized DP

#### Candies (`[problem:AtCoder-dp_m]`)
- **Rating / Difficulty**: 1550
- **Contest**: `dp` | [AtCoder Link](https://atcoder.jp/contests/dp/tasks/dp_m)
- **Detailed Analysis**: [`analysis/AtCoder-dp_m.md`](../analysis/AtCoder-dp_m.md)
- **Key Idea**: The naive transition dp[i][j] = sum_{k=0}^{a_i} dp[i-1][j-k] is over a contiguous range [j - a_i, j] in dp[i-1].
- **Core Observation**: Prefix sums of the previous row evaluate the contiguous range sum in O(1), dropping overall complexity from O(N * K^2) to O(N * K).
- **Algorithm & Complexity**: Time: O(N * K), Space: O(K).
- **What This Problem Teaches**: Sliding window range sum optimization reducing quadratic transitions to linear.
- **Reusable Pattern**: `Prefix sum acceleration of contiguous state transitions.`

### Relative Order Insertion DP with Prefix Sums

#### Permutation (`[problem:AtCoder-dp_t]`)
- **Rating / Difficulty**: 1950
- **Contest**: `dp` | [AtCoder Link](https://atcoder.jp/contests/dp/tasks/dp_t)
- **Detailed Analysis**: [`analysis/AtCoder-dp_t.md`](../analysis/AtCoder-dp_t.md)
- **Key Idea**: Construct permutation of 1..N element by element. When inserting element i, insert it into relative rank j in [1, i] among previously placed elements.
- **Core Observation**: If S[i-1] == '<', j must be greater than previous element's rank k. If '>', j must be <= k. Prefix sums evaluate the transition sum in O(1).
- **Algorithm & Complexity**: Time: O(N^2), Space: O(N).
- **What This Problem Teaches**: Constructing permutations by inserting elements into relative rank slots and optimizing transitions with prefix sums.
- **Reusable Pattern**: `Relative rank insertion DP + prefix sum acceleration.`

---

## Digit DP

### Digit DP with Remainder State

#### Digit Sum (`[problem:AtCoder-dp_s]`)
- **Rating / Difficulty**: 1750
- **Contest**: `dp` | [AtCoder Link](https://atcoder.jp/contests/dp/tasks/dp_s)
- **Detailed Analysis**: [`analysis/AtCoder-dp_s.md`](../analysis/AtCoder-dp_s.md)
- **Key Idea**: Process K as a string of up to 10,000 digits. Maintain state (index, remainder_mod_D, tight_flag).
- **Core Observation**: At index i, if tight is True, the next digit can only range from 0 to K[i]. If tight is False, the next digit can range from 0 to 9 freely.
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
- **Key Idea**: Since the graph has no directed cycles, topological ordering exists. The longest path starting at u is dp[u] = 1 + max_{(u, v) in E} dp[v].
- **Core Observation**: Acyclic structure guarantees no circular dependencies. Memoized DFS evaluates each vertex and edge exactly once.
- **Algorithm & Complexity**: Time: O(V + E), Space: O(V + E).
- **What This Problem Teaches**: Topological ordering as the fundamental validity condition for DAG DP.
- **Reusable Pattern**: `Memoized DFS transition over DAG edges.`

#### Independent Set (`[problem:AtCoder-dp_p]`)
- **Rating / Difficulty**: 1500
- **Contest**: `dp` | [AtCoder Link](https://atcoder.jp/contests/dp/tasks/dp_p)
- **Detailed Analysis**: [`analysis/AtCoder-dp_p.md`](../analysis/AtCoder-dp_p.md)
- **Key Idea**: Root tree arbitrarily. Maintain two states: dp[u][White] and dp[u][Black].
- **Core Observation**: If node u is Black, all children must be White. If u is White, each child can be independently either Black or White.
- **Algorithm & Complexity**: Time: O(N), Space: O(N).
- **What This Problem Teaches**: Subtree DP, state-color branching, and product-rule combination over tree children.
- **Reusable Pattern**: `Two-state subtree product DP on trees.`

### Matrix Exponentiation DP

#### Walk (`[problem:AtCoder-dp_r]`)
- **Rating / Difficulty**: 1700
- **Contest**: `dp` | [AtCoder Link](https://atcoder.jp/contests/dp/tasks/dp_r)
- **Detailed Analysis**: [`analysis/AtCoder-dp_r.md`](../analysis/AtCoder-dp_r.md)
- **Key Idea**: The number of paths of length K between all pairs of vertices is given by A^K, where A is the adjacency matrix.
- **Core Observation**: Matrix multiplication computes transitions; binary exponentiation solves K <= 10^18 in O(N^3 log K) steps.
- **Algorithm & Complexity**: Time: O(N^3 log K), Space: O(N^2).
- **What This Problem Teaches**: Formulating linear state recurrences as matrix products and exponentiating large step counts.
- **Reusable Pattern**: `Matrix exponentiation DP for enormous transition steps.`

### Tree DP with Subtree Rerooting without Division

#### Subtree (`[problem:AtCoder-dp_v]`)
- **Rating / Difficulty**: 2100
- **Contest**: `dp` | [AtCoder Link](https://atcoder.jp/contests/dp/tasks/dp_v)
- **Detailed Analysis**: [`analysis/AtCoder-dp_v.md`](../analysis/AtCoder-dp_v.md)
- **Key Idea**: Reroot the tree in O(N) using two DFS passes. Because M is composite, division by (down[child] + 1) is illegal; prefix and suffix products of children answers exclude a child in O(1) without division.
- **Core Observation**: For each node, children values can be preprocessed into prefix and suffix cumulative products. Excluded child contribution is calculated by multiplying prefix[:i-1] * suffix[i+1:].
- **Algorithm & Complexity**: Time: O(N), Space: O(N).
- **What This Problem Teaches**: Tree rerooting technique without modular division via prefix/suffix product arrays.
- **Reusable Pattern**: `Division-free prefix/suffix rerooting on trees.`

---

## Intro to DP

### 1D DP with K-Step Transitions

#### Frog 2 (`[problem:AtCoder-dp_b]`)
- **Rating / Difficulty**: 700
- **Contest**: `dp` | [AtCoder Link](https://atcoder.jp/contests/dp/tasks/dp_b)
- **Detailed Analysis**: [`analysis/AtCoder-dp_b.md`](../analysis/AtCoder-dp_b.md)
- **Key Idea**: Generalize jumps to up to K stones with minimum total energy cost.
- **Core Observation**: Each state dp[i] is relaxed over a sliding window of the previous K states: dp[i] = min_{1 <= j <= K} (dp[i-j] + |h_i - h_{i-j}|).
- **Algorithm & Complexity**: Time: O(N * K), Space: O(N).
- **What This Problem Teaches**: Parameterized transition loops and boundary-bounded relaxation.
- **Reusable Pattern**: `Push DP over variable-sized transition intervals.`

### 1D State Recurrence / Bounded Lookahead

#### Frog 1 (`[problem:AtCoder-dp_a]`)
- **Rating / Difficulty**: 600
- **Contest**: `dp` | [AtCoder Link](https://atcoder.jp/contests/dp/tasks/dp_a)
- **Detailed Analysis**: [`analysis/AtCoder-dp_a.md`](../analysis/AtCoder-dp_a.md)
- **Key Idea**: Represent the minimum cost to reach stone i using optimal substructure from the previous two stones.
- **Core Observation**: At stone i, arrival is possible exclusively from i-1 or i-2. The state depends only on local height differences and optimal prefix solutions. Space compresses to O(1).
- **Algorithm & Complexity**: Time: O(N), Space: O(1) rolling state.
- **What This Problem Teaches**: Optimal substructure, state initialization, and memory-compressed transitions.
- **Reusable Pattern**: `Linear 1D DP with constant lookback window.`

### Expected Value DP with Multi-Frequency States

#### Sushi (`[problem:AtCoder-dp_j]`)
- **Rating / Difficulty**: 1650
- **Contest**: `dp` | [AtCoder Link](https://atcoder.jp/contests/dp/tasks/dp_j)
- **Detailed Analysis**: [`analysis/AtCoder-dp_j.md`](../analysis/AtCoder-dp_j.md)
- **Key Idea**: Plate identity is irrelevant; state is the count of plates with 1, 2, and 3 sushi (c1, c2, c3). Picking an empty plate loops back to the same state (self-loop).
- **Core Observation**: Self-loop equation E = 1 + sum(P_i E_i) + P_empty E solves algebraically: E = (N + c1*E1 + c2*E2 + c3*E3) / (c1 + c2 + c3).
- **Algorithm & Complexity**: Time: O(N^3), Space: O(N^3).
- **What This Problem Teaches**: Multi-frequency state compression and algebraic self-loop elimination in expected value DP.
- **Reusable Pattern**: `Self-loop elimination: E = (1 + \sum P_i E_i) / (1 - P_{self}).`

### Greedy Exchange Argument + 0/1 Knapsack DP

#### Tower (`[problem:AtCoder-dp_x]`)
- **Rating / Difficulty**: 2250
- **Contest**: `dp` | [AtCoder Link](https://atcoder.jp/contests/dp/tasks/dp_x)
- **Detailed Analysis**: [`analysis/AtCoder-dp_x.md`](../analysis/AtCoder-dp_x.md)
- **Key Idea**: Exchange Argument: Block i should be placed below block j if s_i - w_j >= s_j - w_i, which rearranges to s_i + w_i >= s_j + w_j. Sorting blocks by w_i + s_i fixes the optimal stacking order!
- **Core Observation**: Once sorted by w_i + s_i, the problem reduces to a 0/1 Knapsack where a block can only be added if accumulated weight w <= s_i.
- **Algorithm & Complexity**: Time: O(N log N + N * max(S)), Space: O(max(S)).
- **What This Problem Teaches**: Pairwise exchange arguments (deriving s_i + w_i invariant) combined with 0/1 knapsack.
- **Reusable Pattern**: `Exchange argument pre-sorting + Knapsack DP.`

### Knapsack Dual State / Value as State

#### Knapsack 2 (`[problem:AtCoder-dp_e]`)
- **Rating / Difficulty**: 1450
- **Contest**: `dp` | [AtCoder Link](https://atcoder.jp/contests/dp/tasks/dp_e)
- **Detailed Analysis**: [`analysis/AtCoder-dp_e.md`](../analysis/AtCoder-dp_e.md)
- **Key Idea**: When capacity W is up to 10^9, weight cannot be an array index. Invert the state: define dp[v] as the minimum weight required to achieve exact value v.
- **Core Observation**: Total value sum <= 100 * 1000 = 10^5. The value dimension is pseudopolynomial while weight is not.
- **Algorithm & Complexity**: Time: O(N * sum(V)), Space: O(sum(V)).
- **What This Problem Teaches**: Swapping objective function and state dimension when constraints are large but values are compact.
- **Reusable Pattern**: `Dual DP parameter inversion.`

### Knapsack and Basic Dynamic Programming

#### Knapsack 1 (`[problem:AtCoder-dp_d]`)
- **Rating / Difficulty**: 1150
- **Contest**: `dp` | [AtCoder Link](https://atcoder.jp/contests/dp/tasks/dp_d)
- **Detailed Analysis**: [`analysis/AtCoder-dp_d.md`](../analysis/AtCoder-dp_d.md)
- **Key Idea**: Classical 0/1 Knapsack where capacity W <= 10^5 serves as the DP state index.
- **Core Observation**: By iterating weight downwards from W to w_i, 1D array space is sufficient without using an item multiple times.
- **Algorithm & Complexity**: Time: O(N * W), Space: O(W).
- **What This Problem Teaches**: Reverse-order state traversal to prevent unbounded repetition in subset selection.
- **Reusable Pattern**: `1D space-optimized 0/1 knapsack.`

### Multi-State DP / Consecutive Constraints

#### Vacation (`[problem:AtCoder-dp_c]`)
- **Rating / Difficulty**: 900
- **Contest**: `dp` | [AtCoder Link](https://atcoder.jp/contests/dp/tasks/dp_c)
- **Detailed Analysis**: [`analysis/AtCoder-dp_c.md`](../analysis/AtCoder-dp_c.md)
- **Key Idea**: Maintain happiness while enforcing non-repeating consecutive activity constraints.
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
- **Core Observation**: Let dp[i][j] be probability of exactly j heads after i coin tosses. Outcome partitions probability mass into two events: heads (p_i) or tails (1 - p_i).
- **Algorithm & Complexity**: Time: O(N^2), Space: O(N).
- **What This Problem Teaches**: Probability mass conservation and floating-point accumulation in discrete trial DP.
- **Reusable Pattern**: `Probability convolution DP over independent Bernoulli trials.`

---
