# AtCoder Deep Problem Analysis & Algorithmic Classification

This document contains exhaustive problem-by-problem analysis for curated AtCoder problems.
Every selected problem has been independently analyzed, solved, verified against constraints, and compared with official editorials.

---

## Problem: AtCoder-dp_a — Frog 1

**Problem ID**: `AtCoder-dp_a`  
**Contest**: `dp`  
**Rating / Difficulty**: 600  
**URL**: https://atcoder.jp/contests/dp/tasks/dp_a  
**VJudge Tag**: `[problem:AtCoder-dp_a]`  

**Primary Tag (Domain)**: `Dynamic Programming (DP)`  
**Subtopic**: `Intro to DP`  
**Detailed Topic / Skill**: `1D State Recurrence / Bounded Lookahead`  

**Independent Solution**: Yes  
**Editorial Verified**: Yes  

### 1. Key Idea
Represent the minimum cost to reach stone i using optimal substructure from the previous two stones.

### 2. Core Observation & Invariant
At any stone i, the frog can only arrive from i-1 or i-2. The state space is linear O(N) and transitions depend only on local height differences |h_i - h_{i-k}|.

### 3. Step-by-Step Algorithm
1. Initialize dp[1] = 0, dp[2] = |h_2 - h_1|.
2. For i from 3 to N: dp[i] = min(dp[i-1] + |h_i - h_{i-1}|, dp[i-2] + |h_i - h_{i-2}|).
3. Answer is dp[N].

### 4. Complexity Analysis
Time: O(N), Space: O(N) or O(1) rolling state.

### 5. Editorial Comparison & Alignment
Directly matches canonical DP forward/backward relaxation.

### 6. What This Problem Teaches
Foundational DP state definition, base cases, and optimal substructure.

### 7. Novel Learning Value
Minimalist transition dependency and state compression.

**Selection Status**: `SELECTED`  
**Workbook Inclusion**: Yes  

---

## Problem: AtCoder-dp_b — Frog 2

**Problem ID**: `AtCoder-dp_b`  
**Contest**: `dp`  
**Rating / Difficulty**: 700  
**URL**: https://atcoder.jp/contests/dp/tasks/dp_b  
**VJudge Tag**: `[problem:AtCoder-dp_b]`  

**Primary Tag (Domain)**: `Dynamic Programming (DP)`  
**Subtopic**: `Intro to DP`  
**Detailed Topic / Skill**: `1D DP with K-Step Transitions`  

**Independent Solution**: Yes  
**Editorial Verified**: Yes  

### 1. Key Idea
Generalize linear transitions to arbitrary step sizes K <= 100.

### 2. Core Observation & Invariant
Each dp[i] is computed by taking the minimum over the preceding K states: dp[i] = min_{1 <= j <= K} (dp[i-j] + |h_i - h_{i-j}|).

### 3. Step-by-Step Algorithm
1. Set dp[1] = 0, all other dp[i] = INF.
2. Loop i from 1 to N-1; loop step j from 1 to K: relax dp[i+j] = min(dp[i+j], dp[i] + |h_{i+j} - h_i|).
3. Result is dp[N].

### 4. Complexity Analysis
Time: O(N * K), Space: O(N).

### 5. Editorial Comparison & Alignment
Matches push-based / pull-based relaxation over lookback window.

### 6. What This Problem Teaches
Parametric transition loops in DP and push-style vs pull-style relaxation.

### 7. Novel Learning Value
Transitions with variable bounds min(i+K, N).

**Selection Status**: `SELECTED`  
**Workbook Inclusion**: Yes  

---

## Problem: AtCoder-dp_c — Vacation

**Problem ID**: `AtCoder-dp_c`  
**Contest**: `dp`  
**Rating / Difficulty**: 900  
**URL**: https://atcoder.jp/contests/dp/tasks/dp_c  
**VJudge Tag**: `[problem:AtCoder-dp_c]`  

**Primary Tag (Domain)**: `Dynamic Programming (DP)`  
**Subtopic**: `Intro to DP`  
**Detailed Topic / Skill**: `Multi-State DP / State-Machine DP`  

**Independent Solution**: Yes  
**Editorial Verified**: Yes  

### 1. Key Idea
Maintain happiness while enforcing non-repeating consecutive activity constraints.

### 2. Core Observation & Invariant
The valid choice on day i depends exclusively on the specific activity chosen on day i-1. Encoding the previous choice into the state resolves the constraint.

### 3. Step-by-Step Algorithm
1. dp[i][act] = maximum happiness up to day i ending with activity act in {A, B, C}.
2. dp[i][A] = a_i + max(dp[i-1][B], dp[i-1][C]), and symmetrically for B and C.
3. Answer is max(dp[N][A], dp[N][B], dp[N][C]).

### 4. Complexity Analysis
Time: O(N * 3), Space: O(3) using rolling variables.

### 5. Editorial Comparison & Alignment
Standard 3-state transition graph.

### 6. What This Problem Teaches
State augmentation to satisfy Markovian transition constraints.

### 7. Novel Learning Value
Canonical state-machine DP with categorical transitions.

**Selection Status**: `SELECTED`  
**Workbook Inclusion**: Yes  

---

## Problem: AtCoder-dp_d — Knapsack 1

**Problem ID**: `AtCoder-dp_d`  
**Contest**: `dp`  
**Rating / Difficulty**: 1150  
**URL**: https://atcoder.jp/contests/dp/tasks/dp_d  
**VJudge Tag**: `[problem:AtCoder-dp_d]`  

**Primary Tag (Domain)**: `Dynamic Programming (DP)`  
**Subtopic**: `Intro to DP`  
**Detailed Topic / Skill**: `Knapsack and Basic Dynamic Programming`  

**Independent Solution**: Yes  
**Editorial Verified**: Yes  

### 1. Key Idea
Classical 0/1 Knapsack where capacity W <= 10^5 serves as the DP state index.

### 2. Core Observation & Invariant
Each item can be taken at most once. Traversing capacity downwards (from W down to w_i) prevents using the same item multiple times in 1D memory.

### 3. Step-by-Step Algorithm
1. Initialize dp[0..W] = 0.
2. For each item (w_i, v_i): for w from W down to w_i: dp[w] = max(dp[w], dp[w - w_i] + v_i).
3. Answer is max(dp[0..W]).

### 4. Complexity Analysis
Time: O(N * W), Space: O(W).

### 5. Editorial Comparison & Alignment
Identical to standard 1D reverse-iteration 0/1 Knapsack.

### 6. What This Problem Teaches
0/1 Knapsack state optimization and 1D space reduction technique.

### 7. Novel Learning Value
Reverse loop space compression.

**Selection Status**: `SELECTED`  
**Workbook Inclusion**: Yes  

---

## Problem: AtCoder-dp_e — Knapsack 2

**Problem ID**: `AtCoder-dp_e`  
**Contest**: `dp`  
**Rating / Difficulty**: 1450  
**URL**: https://atcoder.jp/contests/dp/tasks/dp_e  
**VJudge Tag**: `[problem:AtCoder-dp_e]`  

**Primary Tag (Domain)**: `Dynamic Programming (DP)`  
**Subtopic**: `Intro to DP`  
**Detailed Topic / Skill**: `Knapsack Dual State / Value as State`  

**Independent Solution**: Yes  
**Editorial Verified**: Yes  

### 1. Key Idea
When weight capacity W is up to 10^9, invert the state: define dp[v] as the minimum weight required to achieve exact value v.

### 2. Core Observation & Invariant
N <= 100 and v_i <= 1000 implies total value V_max <= 10^5. The value dimension is small enough for pseudopolynomial DP, whereas weight is not.

### 3. Step-by-Step Algorithm
1. Let V_sum = sum(v_i) <= 10^5. Set dp[0] = 0, dp[1..V_sum] = INF.
2. For each item (w_i, v_i): for v from V_sum down to v_i: dp[v] = min(dp[v], dp[v - v_i] + w_i).
3. Answer is max value v such that dp[v] <= W.

### 4. Complexity Analysis
Time: O(N * sum(V)), Space: O(sum(V)).

### 5. Editorial Comparison & Alignment
Classic state-inversion paradigm in competitive programming.

### 6. What This Problem Teaches
Dual problem formulation and state parameter swapping.

### 7. Novel Learning Value
Inverting objective and constraint when constraint space is too large.

**Selection Status**: `SELECTED`  
**Workbook Inclusion**: Yes  

---

## Problem: AtCoder-dp_f — LCS

**Problem ID**: `AtCoder-dp_f`  
**Contest**: `dp`  
**Rating / Difficulty**: 1250  
**URL**: https://atcoder.jp/contests/dp/tasks/dp_f  
**VJudge Tag**: `[problem:AtCoder-dp_f]`  

**Primary Tag (Domain)**: `Dynamic Programming (DP)`  
**Subtopic**: `Classic DP`  
**Detailed Topic / Skill**: `Longest Common Subsequence & Backtracking`  

**Independent Solution**: Yes  
**Editorial Verified**: Yes  

### 1. Key Idea
Find the actual string corresponding to the Longest Common Subsequence of s and t.

### 2. Core Observation & Invariant
Table dp[i][j] stores the length of LCS for prefixes s[1..i] and t[1..j]. Once filled, the actual string can be reconstructed by backtracking from (len(s), len(t)).

### 3. Step-by-Step Algorithm
1. Fill standard LCS table: if s[i-1] == t[j-1]: dp[i][j] = dp[i-1][j-1] + 1; else max(dp[i-1][j], dp[i][j-1]).
2. Traceback: while i > 0 and j > 0: if s[i-1] == t[j-1], append char, i--, j--; else if dp[i-1][j] >= dp[i][j-1], i--; else j--.
3. Reverse reconstructed characters.

### 4. Complexity Analysis
Time: O(|s| * |t|), Space: O(|s| * |t|).

### 5. Editorial Comparison & Alignment
Standard DP table traceback.

### 6. What This Problem Teaches
DP solution path reconstruction and parent/transition backtracking.

### 7. Novel Learning Value
Two-pointer matrix reconstruction of optimal decisions.

**Selection Status**: `SELECTED`  
**Workbook Inclusion**: Yes  

---

## Problem: AtCoder-dp_g — Longest Path

**Problem ID**: `AtCoder-dp_g`  
**Contest**: `dp`  
**Rating / Difficulty**: 1350  
**URL**: https://atcoder.jp/contests/dp/tasks/dp_g  
**VJudge Tag**: `[problem:AtCoder-dp_g]`  

**Primary Tag (Domain)**: `Dynamic Programming (DP)`  
**Subtopic**: `Dp on Different Structures`  
**Detailed Topic / Skill**: `DP on Trees and DAGs`  

**Independent Solution**: Yes  
**Editorial Verified**: Yes  

### 1. Key Idea
Find the length of the longest directed path in a Directed Acyclic Graph (DAG).

### 2. Core Observation & Invariant
Since the graph is acyclic, a topological ordering exists. The longest path starting at vertex u is dp[u] = 1 + max_{(u, v) in E} dp[v].

### 3. Step-by-Step Algorithm
1. Compute out-degrees or use memoized DFS: memo[u] = -1.
2. DFS(u): if memo[u] != -1 return memo[u]. ans = 0. For each neighbor v of u: ans = max(ans, 1 + DFS(v)). memo[u] = ans.
3. Answer is max_{u in V} DFS(u).

### 4. Complexity Analysis
Time: O(V + E), Space: O(V + E).

### 5. Editorial Comparison & Alignment
Equivalent to topological sort DP or memoized DFS.

### 6. What This Problem Teaches
Topological order as the fundamental validity condition for DAG DP.

### 7. Novel Learning Value
Connecting graph traversals directly to DP state transition graphs.

**Selection Status**: `SELECTED`  
**Workbook Inclusion**: Yes  

---

## Problem: AtCoder-dp_h — Grid 1

**Problem ID**: `AtCoder-dp_h`  
**Contest**: `dp`  
**Rating / Difficulty**: 1050  
**URL**: https://atcoder.jp/contests/dp/tasks/dp_h  
**VJudge Tag**: `[problem:AtCoder-dp_h]`  

**Primary Tag (Domain)**: `Dynamic Programming (DP)`  
**Subtopic**: `Classic DP`  
**Detailed Topic / Skill**: `Grid DP / Path Counting with Obstacles`  

**Independent Solution**: Yes  
**Editorial Verified**: Yes  

### 1. Key Idea
Count paths from top-left (1,1) to bottom-right (H,W) moving only right and down, avoiding walls.

### 2. Core Observation & Invariant
Number of ways to reach (r, c) is dp[r][c] = (dp[r-1][c] + dp[r][c-1]) mod (10^9 + 7). If cell (r, c) is '#', dp[r][c] = 0.

### 3. Step-by-Step Algorithm
1. dp[1][1] = 1.
2. For r from 1 to H: for c from 1 to W: if grid[r][c] == '#': dp[r][c] = 0; else add dp[r-1][c] and dp[r][c-1] mod 10^9+7.
3. Output dp[H][W].

### 4. Complexity Analysis
Time: O(H * W), Space: O(W) rolling array.

### 5. Editorial Comparison & Alignment
Canonical grid combinatorial DP.

### 6. What This Problem Teaches
Modular arithmetic integration into DP transitions and grid boundary conditions.

### 7. Novel Learning Value
Translating geometric movement constraints into 2D recurrences.

**Selection Status**: `SELECTED`  
**Workbook Inclusion**: Yes  

---

## Problem: AtCoder-dp_i — Coins

**Problem ID**: `AtCoder-dp_i`  
**Contest**: `dp`  
**Rating / Difficulty**: 1150  
**URL**: https://atcoder.jp/contests/dp/tasks/dp_i  
**VJudge Tag**: `[problem:AtCoder-dp_i]`  

**Primary Tag (Domain)**: `Dynamic Programming (DP)`  
**Subtopic**: `Intro to DP`  
**Detailed Topic / Skill**: `Probability and Expected Value DP`  

**Independent Solution**: Yes  
**Editorial Verified**: Yes  

### 1. Key Idea
Calculate the probability that more heads than tails appear when tossing N biased coins.

### 2. Core Observation & Invariant
Let dp[i][j] be the probability of having exactly j heads after tossing the first i coins. dp[i][j] = dp[i-1][j-1] * p_i + dp[i-1][j] * (1 - p_i).

### 3. Step-by-Step Algorithm
1. dp[0][0] = 1.0; all others 0.0.
2. For i from 1 to N: for j from 0 to i: dp[i][j] = (j > 0 ? dp[i-1][j-1] * p_i : 0) + dp[i-1][j] * (1 - p_i).
3. Sum dp[N][j] for all j > N / 2.

### 4. Complexity Analysis
Time: O(N^2), Space: O(N).

### 5. Editorial Comparison & Alignment
Matches Poisson binomial distribution DP.

### 6. What This Problem Teaches
Probability DP state independence and floating-point stability.

### 7. Novel Learning Value
Discrete event convolution over independent trials.

**Selection Status**: `SELECTED`  
**Workbook Inclusion**: Yes  

---

## Problem: AtCoder-dp_k — Stones

**Problem ID**: `AtCoder-dp_k`  
**Contest**: `dp`  
**Rating / Difficulty**: 1100  
**URL**: https://atcoder.jp/contests/dp/tasks/dp_k  
**VJudge Tag**: `[problem:AtCoder-dp_k]`  

**Primary Tag (Domain)**: `Game Theory`  
**Subtopic**: `Impartial Games`  
**Detailed Topic / Skill**: `Sprague-Grundy / Combinatorial Game DP`  

**Independent Solution**: Yes  
**Editorial Verified**: Yes  

### 1. Key Idea
Determine whether First or Second player wins an impartial subtract-a-stone game from pile of size K.

### 2. Core Observation & Invariant
A state x is a Winning state (First wins) if there exists a valid move a_i <= x such that x - a_i is a Losing state (Second wins). If all valid moves lead to Winning states, x is Losing.

### 3. Step-by-Step Algorithm
1. dp[0] = False (Losing state).
2. For x from 1 to K: dp[x] = True if any(a_i <= x and not dp[x - a_i] for a_i in A) else False.
3. Output 'First' if dp[K] else 'Second'.

### 4. Complexity Analysis
Time: O(N * K), Space: O(K).

### 5. Editorial Comparison & Alignment
Classic backward induction on finite game graph.

### 6. What This Problem Teaches
Backward induction, P-positions and N-positions, and impartial game theory.

### 7. Novel Learning Value
Boolean state alternation under optimal play.

**Selection Status**: `SELECTED`  
**Workbook Inclusion**: Yes  

---

## Problem: AtCoder-dp_l — Deque

**Problem ID**: `AtCoder-dp_l`  
**Contest**: `dp`  
**Rating / Difficulty**: 1400  
**URL**: https://atcoder.jp/contests/dp/tasks/dp_l  
**VJudge Tag**: `[problem:AtCoder-dp_l]`  

**Primary Tag (Domain)**: `Dynamic Programming (DP)`  
**Subtopic**: `Classic DP`  
**Detailed Topic / Skill**: `Interval DP / Range DP / Matrix Chain Multiplication (MCM)`  

**Independent Solution**: Yes  
**Editorial Verified**: Yes  

### 1. Key Idea
Two players take turns removing elements from either end of a deque. Maximize X - Y.

### 2. Core Observation & Invariant
For subsegment [l, r], the active player chooses either a_l or a_r to maximize their margin over the remaining subsegment: dp[l][r] = max(a_l - dp[l+1][r], a_r - dp[l][r-1]).

### 3. Step-by-Step Algorithm
1. Base case: for i in 1..N: dp[i][i] = a_i.
2. Iterate interval length len from 2 to N: for l from 1 to N - len + 1: r = l + len - 1: dp[l][r] = max(a_l - dp[l+1][r], a_r - dp[l][r-1]).
3. Answer is dp[1][N].

### 4. Complexity Analysis
Time: O(N^2), Space: O(N^2).

### 5. Editorial Comparison & Alignment
Minimax dynamic programming over intervals.

### 6. What This Problem Teaches
Interval DP structure (solving by increasing segment length) and minimax evaluation.

### 7. Novel Learning Value
Symmetric negation optimization in zero-sum sequential games.

**Selection Status**: `SELECTED`  
**Workbook Inclusion**: Yes  

---

## Problem: AtCoder-dp_m — Candies

**Problem ID**: `AtCoder-dp_m`  
**Contest**: `dp`  
**Rating / Difficulty**: 1550  
**URL**: https://atcoder.jp/contests/dp/tasks/dp_m  
**VJudge Tag**: `[problem:AtCoder-dp_m]`  

**Primary Tag (Domain)**: `Dynamic Programming (DP)`  
**Subtopic**: `DP Optimizations`  
**Detailed Topic / Skill**: `Prefix Sum Optimized DP`  

**Independent Solution**: Yes  
**Editorial Verified**: Yes  

### 1. Key Idea
Distribute K candies among N children such that child i receives at most a_i candies.

### 2. Core Observation & Invariant
Direct transition dp[i][j] = sum_{k=0}^{min(j, a_i)} dp[i-1][j-k] takes O(N * K^2). The inner sum is over a contiguous range [j - a_i, j] in dp[i-1], which prefix sums evaluate in O(1).

### 3. Step-by-Step Algorithm
1. dp[0] = 1, all others 0.
2. For each child i: compute prefix sums pref of current dp: pref[x+1] = (pref[x] + dp[x]) mod M.
3. New dp[j] = (pref[j+1] - pref[max(0, j - a_i)]) mod M.
4. Answer is dp[K].

### 4. Complexity Analysis
Time: O(N * K), Space: O(K).

### 5. Editorial Comparison & Alignment
Prefix sum acceleration of polynomial transitions.

### 6. What This Problem Teaches
Transition acceleration from O(K) to O(1) via prefix sums on DP states.

### 7. Novel Learning Value
Sliding window range-sum transition optimization.

**Selection Status**: `SELECTED`  
**Workbook Inclusion**: Yes  

---

## Problem: AtCoder-dp_n — Slimes

**Problem ID**: `AtCoder-dp_n`  
**Contest**: `dp`  
**Rating / Difficulty**: 1600  
**URL**: https://atcoder.jp/contests/dp/tasks/dp_n  
**VJudge Tag**: `[problem:AtCoder-dp_n]`  

**Primary Tag (Domain)**: `Dynamic Programming (DP)`  
**Subtopic**: `Classic DP`  
**Detailed Topic / Skill**: `Interval DP / Range DP / Matrix Chain Multiplication (MCM)`  

**Independent Solution**: Yes  
**Editorial Verified**: Yes  

### 1. Key Idea
Merge N slimes pairwise into one slime with minimum total combining cost.

### 2. Core Observation & Invariant
The final merge combines two sub-blocks [l, k] and [k+1, r]. The cost incurred at the final step is sum_{i=l}^r a_i. dp[l][r] = sum(a[l..r]) + min_{l <= k < r} (dp[l][k] + dp[k+1][r]).

### 3. Step-by-Step Algorithm
1. Precompute prefix sums of array a.
2. dp[i][i] = 0.
3. Loop length len from 2 to N: loop left l from 1 to N-len+1: r = l+len-1: dp[l][r] = min_{k=l}^{r-1}(dp[l][k] + dp[k+1][r]) + (pref[r] - pref[l-1]).
4. Output dp[1][N].

### 4. Complexity Analysis
Time: O(N^3) standard, reducible to O(N^2) via Knuth's Optimization.

### 5. Editorial Comparison & Alignment
Direct equivalent to Matrix Chain Multiplication / optimal binary search tree.

### 6. What This Problem Teaches
Interval merging DP and partition point split optimization.

### 7. Novel Learning Value
Prefix sum cost addition over nested subproblem partitions.

**Selection Status**: `SELECTED`  
**Workbook Inclusion**: Yes  

---

## Problem: AtCoder-dp_o — Matching

**Problem ID**: `AtCoder-dp_o`  
**Contest**: `dp`  
**Rating / Difficulty**: 1650  
**URL**: https://atcoder.jp/contests/dp/tasks/dp_o  
**VJudge Tag**: `[problem:AtCoder-dp_o]`  

**Primary Tag (Domain)**: `Dynamic Programming (DP)`  
**Subtopic**: `Bit Related DP`  
**Detailed Topic / Skill**: `Bitmask DP`  

**Independent Solution**: Yes  
**Editorial Verified**: Yes  

### 1. Key Idea
Count the number of perfect matchings in a bipartite graph with N men and N women (N <= 21).

### 2. Core Observation & Invariant
When matching men 0, 1, ..., i-1, the number of matched women is exactly i = popcount(mask). Hence the man's index is implicit in the bitmask of chosen women!

### 3. Step-by-Step Algorithm
1. dp[0] = 1, all other dp[mask] = 0.
2. For mask from 0 to 2^N - 1: let i = popcount(mask). If i == N, continue.
3. For each woman j in 0..N-1: if not (mask & (1 << j)) and compatible(i, j): dp[mask | (1 << j)] = (dp[mask | (1 << j)] + dp[mask]) mod (10^9 + 7).
4. Answer is dp[(1 << N) - 1].

### 4. Complexity Analysis
Time: O(N * 2^N), Space: O(2^N).

### 5. Editorial Comparison & Alignment
Canonical popcount bitmask reduction.

### 6. What This Problem Teaches
Dimension reduction in Bitmask DP using state invariants (popcount).

### 7. Novel Learning Value
Implicit step derivation from subset cardinality.

**Selection Status**: `SELECTED`  
**Workbook Inclusion**: Yes  

---

## Problem: AtCoder-dp_p — Independent Set

**Problem ID**: `AtCoder-dp_p`  
**Contest**: `dp`  
**Rating / Difficulty**: 1500  
**URL**: https://atcoder.jp/contests/dp/tasks/dp_p  
**VJudge Tag**: `[problem:AtCoder-dp_p]`  

**Primary Tag (Domain)**: `Dynamic Programming (DP)`  
**Subtopic**: `Dp on Different Structures`  
**Detailed Topic / Skill**: `DP on Trees and DAGs`  

**Independent Solution**: Yes  
**Editorial Verified**: Yes  

### 1. Key Idea
Count ways to paint vertices of a tree black or white such that no two adjacent vertices are both black.

### 2. Core Observation & Invariant
Root the tree arbitrarily. For any node u, if u is painted Black, all children must be White. If u is painted White, each child can be either Black or White independently.

### 3. Step-by-Step Algorithm
1. Post-order DFS(u, parent).
2. dp[u][Black] = prod_{v in children(u)} dp[v][White].
3. dp[u][White] = prod_{v in children(u)} (dp[v][Black] + dp[v][White]).
4. Return (dp[root][Black] + dp[root][White]) mod 10^9+7.

### 4. Complexity Analysis
Time: O(N), Space: O(N).

### 5. Editorial Comparison & Alignment
Classic tree independent set counting.

### 6. What This Problem Teaches
Subtree DP, state-color branching, and product-rule combination over tree children.

### 7. Novel Learning Value
Independent combination of child subtree configurations.

**Selection Status**: `SELECTED`  
**Workbook Inclusion**: Yes  

---

## Problem: AtCoder-dp_q — Flowers

**Problem ID**: `AtCoder-dp_q`  
**Contest**: `dp`  
**Rating / Difficulty**: 1600  
**URL**: https://atcoder.jp/contests/dp/tasks/dp_q  
**VJudge Tag**: `[problem:AtCoder-dp_q]`  

**Primary Tag (Domain)**: `Dynamic Programming (DP)`  
**Subtopic**: `DP Optimizations`  
**Detailed Topic / Skill**: `DP Optimization using Data Structures [Some Practice Problems]`  

**Independent Solution**: Yes  
**Editorial Verified**: Yes  

### 1. Key Idea
Find a subsequence of flowers with strictly increasing heights that maximizes total beauty.

### 2. Core Observation & Invariant
Let dp[h] be the maximum beauty of an increasing subsequence ending at height h. For a flower with height h_i and beauty a_i, dp[h_i] = a_i + max_{0 <= h < h_i} dp[h]. This requires dynamic point update and prefix maximum query.

### 3. Step-by-Step Algorithm
1. Maintain a Fenwick tree (or Segment Tree) of size N storing max DP values.
2. For each flower i from 1 to N: best = query_prefix_max(h_i - 1); val = best + a_i; point_update(h_i, val).
3. Answer is query_prefix_max(N).

### 4. Complexity Analysis
Time: O(N log N), Space: O(N).

### 5. Editorial Comparison & Alignment
Data-structure accelerated LIS.

### 6. What This Problem Teaches
Accelerating O(N^2) DP to O(N log N) using Fenwick/Segment Tree on value domain.

### 7. Novel Learning Value
Transforming inner range search into dynamic range queries.

**Selection Status**: `SELECTED`  
**Workbook Inclusion**: Yes  

---

## Problem: AtCoder-dp_u — Grouping

**Problem ID**: `AtCoder-dp_u`  
**Contest**: `dp`  
**Rating / Difficulty**: 1850  
**URL**: https://atcoder.jp/contests/dp/tasks/dp_u  
**VJudge Tag**: `[problem:AtCoder-dp_u]`  

**Primary Tag (Domain)**: `Dynamic Programming (DP)`  
**Subtopic**: `Bit Related DP`  
**Detailed Topic / Skill**: `Bitmask DP`  

**Independent Solution**: Yes  
**Editorial Verified**: Yes  

### 1. Key Idea
Partition N rabbits into groups to maximize total compatibility score (N <= 16).

### 2. Core Observation & Invariant
Precompute the score of any standalone group submask in O(N^2 * 2^N). Then dp[mask] = max_{sub is submask of mask} (cost[sub] + dp[mask ^ sub]).

### 3. Step-by-Step Algorithm
1. Precompute cost[mask] for all 2^N masks.
2. Loop mask from 1 to 2^N - 1:
   Iterate submasks: sub = mask; while sub > 0: dp[mask] = max(dp[mask], cost[sub] + dp[mask ^ sub]); sub = (sub - 1) & mask.
3. Total submask transitions over all masks sum to 3^N.

### 4. Complexity Analysis
Time: O(3^N + N^2 * 2^N), Space: O(2^N).

### 5. Editorial Comparison & Alignment
Textbook submask enumeration (sub = (sub - 1) & mask).

### 6. What This Problem Teaches
O(3^N) submask iteration idiom and subset partition DP.

### 7. Novel Learning Value
The (sub - 1) & mask bit trick for exhaustive partition.

**Selection Status**: `SELECTED`  
**Workbook Inclusion**: Yes  

---

## Problem: AtCoder-dp_v — Subtree

**Problem ID**: `AtCoder-dp_v`  
**Contest**: `dp`  
**Rating / Difficulty**: 2100  
**URL**: https://atcoder.jp/contests/dp/tasks/dp_v  
**VJudge Tag**: `[problem:AtCoder-dp_v]`  

**Primary Tag (Domain)**: `Dynamic Programming (DP)`  
**Subtopic**: `Dp on Different Structures`  
**Detailed Topic / Skill**: `DP on Trees and DAGs`  

**Independent Solution**: Yes  
**Editorial Verified**: Yes  

### 1. Key Idea
For every node v in a tree, compute the number of black-connected components containing v modulo M.

### 2. Core Observation & Invariant
Recomputing tree DP for each root takes O(N^2). Since M is not necessarily prime, modular division is forbidden! Prefix and suffix products of children's answers allow O(1) rerooting without division.

### 3. Step-by-Step Algorithm
1. Post-order DFS1: compute subtree product down[u] = prod_{v in children} (down[v] + 1) mod M.
2. Pre-order DFS2: compute parent contribution up[u] using prefix and suffix products of sibling values (down[sib] + 1).
3. Final answer for u: down[u] * (up[u] + 1) mod M.

### 4. Complexity Analysis
Time: O(N), Space: O(N).

### 5. Editorial Comparison & Alignment
All-roots tree DP rerooting with non-invertible operators.

### 6. What This Problem Teaches
Tree rerooting technique without division using prefix/suffix product arrays.

### 7. Novel Learning Value
Rerooting under arbitrary modulus without modular inverses.

**Selection Status**: `SELECTED`  
**Workbook Inclusion**: Yes  

---

## Problem: AtCoder-dp_z — Frog 3

**Problem ID**: `AtCoder-dp_z`  
**Contest**: `dp`  
**Rating / Difficulty**: 2200  
**URL**: https://atcoder.jp/contests/dp/tasks/dp_z  
**VJudge Tag**: `[problem:AtCoder-dp_z]`  

**Primary Tag (Domain)**: `Dynamic Programming (DP)`  
**Subtopic**: `Convex Hull Trick (CHT)`  
**Detailed Topic / Skill**: `Convex Hull Trick (CHT) and Dynamic CHT`  

**Independent Solution**: Yes  
**Editorial Verified**: Yes  

### 1. Key Idea
Frog jumps from stone i to j with cost (h_j - h_i)^2 + C.

### 2. Core Observation & Invariant
Expanding (h_j - h_i)^2 + C yields h_j^2 + C + (h_i^2 + dp[i]) - 2 * h_j * h_i. For fixed j, this is min_i { m_i * x + b_i } where m_i = -2 * h_i and b_i = h_i^2 + dp[i]. Since heights h_i are strictly increasing, lines have monotonically decreasing slopes!

### 3. Step-by-Step Algorithm
1. Maintain a Convex Hull of lines in a deque.
2. Query optimal line for x = h_j by popping suboptimal lines from the front.
3. Compute dp[j].
4. Add new line (slope = -2*h_j, intercept = h_j^2 + dp[j]) to back, popping non-convex lines.

### 4. Complexity Analysis
Time: O(N) amortized with monotone deque (or O(N log N) via Li Chao Tree).

### 5. Editorial Comparison & Alignment
Canonical Convex Hull Trick with monotonic slopes and monotonic queries.

### 6. What This Problem Teaches
CHT line representation, geometric lower envelope maintenance, and linear time DP optimization.

### 7. Novel Learning Value
Linear-time optimization of quadratic transition costs.

**Selection Status**: `SELECTED`  
**Workbook Inclusion**: Yes  

---

## Problem: AtCoder-abc350_d — New Friends

**Problem ID**: `AtCoder-abc350_d`  
**Contest**: `abc350`  
**Rating / Difficulty**: 1050  
**URL**: https://atcoder.jp/contests/abc350/tasks/abc350_d  
**VJudge Tag**: `[problem:AtCoder-abc350_d]`  

**Primary Tag (Domain)**: `Graph Theory`  
**Subtopic**: `Connected Components`  
**Detailed Topic / Skill**: `Disjoint Set Union (DSU) / Connected Component Cliques`  

**Independent Solution**: Yes  
**Editorial Verified**: Yes  

### 1. Key Idea
If A-B and B-C are friends, A and C can become friends. Count maximum new operations.

### 2. Core Observation & Invariant
The friendship relation is transitive under repeated operations. Thus, each connected component of size S will eventually become a complete graph (clique) with S*(S-1)/2 edges.

### 3. Step-by-Step Algorithm
1. Build Disjoint Set Union (DSU) over all N vertices and M edges.
2. For each component root, obtain component size S and count existing edges E.
3. Total new edges = sum_{components} (S * (S - 1) / 2 - E).

### 4. Complexity Analysis
Time: O(N + M * alpha(N)), Space: O(N).

### 5. Editorial Comparison & Alignment
Standard DSU component aggregation.

### 6. What This Problem Teaches
Transitive closure on undirected graphs and component-wise clique completion.

### 7. Novel Learning Value
Translating local operation chains into global component invariants.

**Selection Status**: `SELECTED`  
**Workbook Inclusion**: Yes  

---

## Problem: AtCoder-typical90_a — Yokan Party

**Problem ID**: `AtCoder-typical90_a`  
**Contest**: `typical90`  
**Rating / Difficulty**: 1200  
**URL**: https://atcoder.jp/contests/typical90/tasks/typical90_a  
**VJudge Tag**: `[problem:AtCoder-typical90_a]`  

**Primary Tag (Domain)**: `Basics`  
**Subtopic**: `Binary Search`  
**Detailed Topic / Skill**: `Binary Search on Answer / Greedy Feasibility`  

**Independent Solution**: Yes  
**Editorial Verified**: Yes  

### 1. Key Idea
Cut a stick of length L at K positions to maximize the minimum piece length.

### 2. Core Observation & Invariant
Maximizing the minimum of something is the hallmark signature of Binary Search on Answer. The predicate 'Can we obtain at least K+1 pieces of length >= M?' is monotonic in M.

### 3. Step-by-Step Algorithm
1. Binary search for M in [1, L].
2. Feasibility check check(M): Greedily cut whenever the accumulated piece length reaches >= M. If total pieces cut is >= K and remaining piece is >= M, return True; else False.
3. High boundary of binary search gives the maximum possible minimum length.

### 4. Complexity Analysis
Time: O(N log L), Space: O(1).

### 5. Editorial Comparison & Alignment
Archetypal binary search on answer.

### 6. What This Problem Teaches
Binary search on answer and greedy feasibility check.

### 7. Novel Learning Value
The canonical 'maximize the minimum' CP template.

**Selection Status**: `SELECTED`  
**Workbook Inclusion**: Yes  

---

## Problem: AtCoder-typical90_c — Longest Circular Road

**Problem ID**: `AtCoder-typical90_c`  
**Contest**: `typical90`  
**Rating / Difficulty**: 1100  
**URL**: https://atcoder.jp/contests/typical90/tasks/typical90_c  
**VJudge Tag**: `[problem:AtCoder-typical90_c]`  

**Primary Tag (Domain)**: `Graph Theory`  
**Subtopic**: `Trees`  
**Detailed Topic / Skill**: `Tree Diameter / Double BFS-DFS`  

**Independent Solution**: Yes  
**Editorial Verified**: Yes  

### 1. Key Idea
Adding an edge between two vertices u and v creates a cycle of length dist(u, v) + 1. Maximize this cycle length.

### 2. Core Observation & Invariant
Maximizing dist(u, v) in a tree is precisely finding the diameter of the tree! The maximum cycle length is diameter + 1.

### 3. Step-by-Step Algorithm
1. Run BFS from arbitrary node (e.g. node 1) to find the farthest node u.
2. Run BFS from node u to find the farthest node v. The distance dist(u, v) is the tree diameter.
3. Output dist(u, v) + 1.

### 4. Complexity Analysis
Time: O(N), Space: O(N).

### 5. Editorial Comparison & Alignment
Textbook 2-pass BFS tree diameter algorithm.

### 6. What This Problem Teaches
Tree diameter characterization and the 2-BFS proof.

### 7. Novel Learning Value
Connecting cycle maximization to tree diameter.

**Selection Status**: `SELECTED`  
**Workbook Inclusion**: Yes  

---

## Problem: AtCoder-typical90_l — Red Painting

**Problem ID**: `AtCoder-typical90_l`  
**Contest**: `typical90`  
**Rating / Difficulty**: 1250  
**URL**: https://atcoder.jp/contests/typical90/tasks/typical90_l  
**VJudge Tag**: `[problem:AtCoder-typical90_l]`  

**Primary Tag (Domain)**: `Data Structures (DS)`  
**Subtopic**: `Disjoint Set Union (DSU)`  
**Detailed Topic / Skill**: `Grid Connectivity / Dynamic DSU`  

**Independent Solution**: Yes  
**Editorial Verified**: Yes  

### 1. Key Idea
Dynamically color grid cells red and answer reachability queries between red cells.

### 2. Core Observation & Invariant
When a cell (r, c) is colored red, it unites with any adjacent red neighbors. Querying if two red cells are connected is equivalent to checking if they belong to the same DSU set.

### 3. Step-by-Step Algorithm
1. Map 2D grid coordinates (r, c) to 1D index r * W + c.
2. Initialize DSU and boolean grid is_red.
3. Query 1: Mark (r, c) red; for each neighbor (nr, nc) that is red, dsu.unite(idx(r,c), idx(nr,nc)).
4. Query 2: If both cells are red and dsu.same(idx(ra,ca), idx(rb,cb)), print 'Yes', else 'No'.

### 4. Complexity Analysis
Time: O(Q * alpha(H * W)), Space: O(H * W).

### 5. Editorial Comparison & Alignment
Incremental dynamic connectivity on grid.

### 6. What This Problem Teaches
2D-to-1D index linearization and online grid connectivity.

### 7. Novel Learning Value
Online union-find query handling without rebuilding components.

**Selection Status**: `SELECTED`  
**Workbook Inclusion**: Yes  

---
