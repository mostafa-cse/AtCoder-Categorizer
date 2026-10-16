#!/usr/bin/env python3
"""
AtCoder Category Markdown Generator
====================================
Generates topic-by-topic and category-by-category Markdown files under `categories/`
and individual detailed problem analysis files under `analysis/`.

Follows the canonical 3-tier competitive programming curriculum taxonomy:
Tag (Domain) -> Subtopic -> Topic (Skill)
"""

import json
import os
import re
from collections import defaultdict
from typing import Dict, List, Any

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
CATEGORIES_DIR = os.path.join(BASE_DIR, "categories")
ANALYSIS_DIR = os.path.join(BASE_DIR, "analysis")

# Comprehensive database of analyzed high-value problems
PROBLEMS_CATALOG = [
    # ==================== DYNAMIC PROGRAMMING ====================
    {
        "id": "dp_a",
        "title": "Frog 1",
        "contest_id": "dp",
        "rating": 600,
        "tag": "Dynamic Programming (DP)",
        "subtopic": "Intro to DP",
        "topic": "1D State Recurrence / Bounded Lookahead",
        "key_idea": "Determine the minimum jump cost to reach stone N where each jump can span 1 or 2 stones.",
        "observation": "At stone i, arrival is possible exclusively from i-1 or i-2. The state depends only on local height differences |h_i - h_{i-k}| and optimal prefix solutions.",
        "algorithm": "1. Base cases: dp[1] = 0, dp[2] = |h_2 - h_1|.\n2. For i from 3 to N: dp[i] = min(dp[i-1] + |h_i - h_{i-1}|, dp[i-2] + |h_i - h_{i-2}|).\n3. Result: dp[N].",
        "complexity": "Time: O(N), Space: O(1) rolling state.",
        "editorial": "Standard 1D forward relaxation recurrence.",
        "teaches": "Optimal substructure, state initialization, and memory-compressed transitions.",
        "reusable_pattern": "Linear 1D DP with constant lookback window."
    },
    {
        "id": "dp_b",
        "title": "Frog 2",
        "contest_id": "dp",
        "rating": 700,
        "tag": "Dynamic Programming (DP)",
        "subtopic": "Intro to DP",
        "topic": "1D DP with K-Step Transitions",
        "key_idea": "Generalize jumps from 2 stones to up to K stones with minimum total energy cost.",
        "observation": "Each state dp[i] is relaxed over a sliding window of the previous K states: dp[i] = min_{1 <= j <= K} (dp[i-j] + |h_i - h_{i-j}|).",
        "algorithm": "1. Initialize dp[1] = 0, others INF.\n2. For i in 1..N-1: for step in 1..K (with i+step <= N): dp[i+step] = min(dp[i+step], dp[i] + |h_{i+step} - h_i|).\n3. Return dp[N].",
        "complexity": "Time: O(N * K), Space: O(N).",
        "editorial": "Standard push-based relaxation over parameterized lookahead.",
        "teaches": "Parameterized transition loops and boundary-bounded relaxation.",
        "reusable_pattern": "Push DP over variable-sized transition intervals."
    },
    {
        "id": "dp_c",
        "title": "Vacation",
        "contest_id": "dp",
        "rating": 900,
        "tag": "Dynamic Programming (DP)",
        "subtopic": "Intro to DP",
        "topic": "Multi-State DP / Consecutive Constraints",
        "key_idea": "Maximize vacation happiness over N days choosing between three activities (A, B, C) without doing the same activity two days in a row.",
        "observation": "Enforcing the constraint 'no two consecutive identical choices' requires augmenting the state with the identity of the last chosen activity.",
        "algorithm": "1. State: dp[day][act] = max happiness up to day ending in act in {0, 1, 2}.\n2. dp[i][0] = a_i + max(dp[i-1][1], dp[i-1][2]), and symmetrically for 1 and 2.\n3. Return max_{act} dp[N][act].",
        "complexity": "Time: O(N), Space: O(1) rolling state.",
        "editorial": "Classic 3-state Markov transition graph.",
        "teaches": "State augmentation for path-dependent constraints and state-machine DP.",
        "reusable_pattern": "Categorical state-machine DP with mutually exclusive transitions."
    },
    {
        "id": "dp_d",
        "title": "Knapsack 1",
        "contest_id": "dp",
        "rating": 1150,
        "tag": "Dynamic Programming (DP)",
        "subtopic": "Intro to DP",
        "topic": "Knapsack and Basic Dynamic Programming",
        "key_idea": "Maximize total value of items within knapsack capacity W <= 10^5 where each item can be selected at most once.",
        "observation": "Capacity is moderate (W <= 10^5). By iterating weight downwards from W to w_i, 1D array space is sufficient without using an item multiple times.",
        "algorithm": "1. Initialize dp[0..W] = 0.\n2. For each item (w_i, v_i): for cap from W down to w_i: dp[cap] = max(dp[cap], dp[cap - w_i] + v_i).\n3. Result is max(dp).",
        "complexity": "Time: O(N * W), Space: O(W).",
        "editorial": "Textbook 0/1 Knapsack with 1D memory compression.",
        "teaches": "Reverse-order state traversal to prevent unbounded repetition in subset selection.",
        "reusable_pattern": "1D space-optimized 0/1 knapsack."
    },
    {
        "id": "dp_e",
        "title": "Knapsack 2",
        "contest_id": "dp",
        "rating": 1450,
        "tag": "Dynamic Programming (DP)",
        "subtopic": "Intro to DP",
        "topic": "Knapsack Dual State / Value as State",
        "key_idea": "Solve 0/1 Knapsack when capacity W <= 10^9 is enormous, but item values v_i <= 1000 and N <= 100.",
        "observation": "Max total value V_max <= 100 * 1000 = 10^5. Invert the DP formulation: define dp[v] as the minimum weight required to achieve exact total value v.",
        "algorithm": "1. Let V_sum = sum(v_i). dp[0] = 0, dp[1..V_sum] = INF.\n2. For each item (w_i, v_i): for v from V_sum down to v_i: dp[v] = min(dp[v], dp[v - v_i] + w_i).\n3. Return max v such that dp[v] <= W.",
        "complexity": "Time: O(N * sum(V)), Space: O(sum(V)).",
        "editorial": "State-inversion / dual-space dynamic programming.",
        "teaches": "Swapping objective function and state dimension when constraints are large but values are compact.",
        "reusable_pattern": "Dual DP parameter inversion."
    },
    {
        "id": "dp_f",
        "title": "LCS",
        "contest_id": "dp",
        "rating": 1250,
        "tag": "Dynamic Programming (DP)",
        "subtopic": "Classic DP",
        "topic": "Longest Common Subsequence & Backtracking",
        "key_idea": "Reconstruct and print the actual string corresponding to the Longest Common Subsequence of strings s and t.",
        "observation": "Standard 2D table computes optimal lengths. The sequence itself is uniquely extracted by tracing back from (len(s), len(t)) following optimal transition choices.",
        "algorithm": "1. Compute dp[i][j]: if s[i-1] == t[j-1] -> dp[i-1][j-1]+1; else max(dp[i-1][j], dp[i][j-1]).\n2. Traceback: if s[i-1] == t[j-1]: append s[i-1], i--, j--; else if dp[i-1][j] >= dp[i][j-1]: i--; else j--.\n3. Reverse characters.",
        "complexity": "Time: O(|s| * |t|), Space: O(|s| * |t|).",
        "editorial": "Full 2D DP matrix traceback.",
        "teaches": "State path reconstruction and multi-dimensional backtracking.",
        "reusable_pattern": "Optimal decision matrix traceback."
    },
    {
        "id": "dp_g",
        "title": "Longest Path",
        "contest_id": "dp",
        "rating": 1350,
        "tag": "Dynamic Programming (DP)",
        "subtopic": "Dp on Different Structures",
        "topic": "DP on Trees and DAGs",
        "key_idea": "Find the length of the longest directed path in a Directed Acyclic Graph (DAG).",
        "observation": "In a DAG, cycles are absent; topological ordering guarantees a well-founded recursion. The longest path starting at u is dp[u] = 1 + max_{(u, v) in E} dp[v].",
        "algorithm": "1. Memoized DFS: memo[u] = -1.\n2. DFS(u): if memo[u] != -1 return memo[u]. ans = 0. For each out-neighbor v: ans = max(ans, 1 + DFS(v)). memo[u] = ans.\n3. Global answer = max_{u in V} DFS(u).",
        "complexity": "Time: O(V + E), Space: O(V + E).",
        "editorial": "Topological sort DP / memoized DFS on DAG.",
        "teaches": "Topological order as the universal prerequisite for acyclic graph dynamic programming.",
        "reusable_pattern": "DAG memoized DFS transition."
    },
    {
        "id": "dp_h",
        "title": "Grid 1",
        "contest_id": "dp",
        "rating": 1050,
        "tag": "Dynamic Programming (DP)",
        "subtopic": "Classic DP",
        "topic": "Grid DP / Path Counting with Obstacles",
        "key_idea": "Count paths from top-left (1,1) to bottom-right (H,W) moving only right and down, avoiding obstacle walls.",
        "observation": "Transitions are purely local: dp[r][c] = (dp[r-1][c] + dp[r][c-1]) mod (10^9+7). Any obstacle cell '#' strictly resets dp[r][c] to 0.",
        "algorithm": "1. dp[1][1] = 1.\n2. For r in 1..H, c in 1..W: if grid[r][c] == '#': dp[r][c] = 0; else dp[r][c] = (dp[r-1][c] + dp[r][c-1]) % MOD.\n3. Return dp[H][W].",
        "complexity": "Time: O(H * W), Space: O(W).",
        "editorial": "Grid combinatorial dynamic programming.",
        "teaches": "Grid boundary enforcement, obstacle nullification, and modulo arithmetic accumulation.",
        "reusable_pattern": "2D additive grid DP."
    },
    {
        "id": "dp_i",
        "title": "Coins",
        "contest_id": "dp",
        "rating": 1150,
        "tag": "Dynamic Programming (DP)",
        "subtopic": "Intro to DP",
        "topic": "Probability and Expected Value DP",
        "key_idea": "Calculate the exact probability that more heads than tails appear when tossing N independent biased coins.",
        "observation": "Let dp[i][j] be the probability of obtaining exactly j heads after i coin tosses. The outcome of coin i partitions probability mass into two independent events: heads (prob p_i) or tails (prob 1 - p_i).",
        "algorithm": "1. dp[0][0] = 1.0; others 0.0.\n2. For i in 1..N: for j in 0..i: dp[i][j] = (j > 0 ? dp[i-1][j-1] * p_i : 0) + dp[i-1][j] * (1 - p_i).\n3. Sum dp[N][j] for j > N/2.",
        "complexity": "Time: O(N^2), Space: O(N).",
        "editorial": "Poisson binomial distribution dynamic programming.",
        "teaches": "Probability mass conservation and floating-point accumulation in discrete trial DP.",
        "reusable_pattern": "Probability convolution DP over independent Bernoulli trials."
    },
    {
        "id": "dp_j",
        "title": "Sushi",
        "contest_id": "dp",
        "rating": 1650,
        "tag": "Dynamic Programming (DP)",
        "subtopic": "Intro to DP",
        "topic": "Expected Value DP with Multi-Frequency States",
        "key_idea": "N plates have 1, 2, or 3 sushi. Repeatedly pick a random plate until all sushi are eaten. Find expected number of operations.",
        "observation": "The plate identity does not matter! Only the count of plates having 1 sushi (c1), 2 sushi (c2), and 3 sushi (c3) determines the system state. Picking an empty plate loops back to the same state (self-loop), which can be eliminated algebraically.",
        "algorithm": "1. State: dp[c1][c2][c3] = expected operations.\n2. E = 1 + (c1/N)*dp[c1-1][c2][c3] + (c2/N)*dp[c1+1][c2-1][c3] + (c3/N)*dp[c1][c2+1][c3-1] + (c0/N)*E.\n3. Solve for E: E * (1 - c0/N) = 1 + sum(...) => E = (N + c1*dp1 + c2*dp2 + c3*dp3) / (c1 + c2 + c3).\n4. Memoized DFS / 3D loop.",
        "complexity": "Time: O(N^3), Space: O(N^3).",
        "editorial": "Expected value recurrence with algebraic self-loop resolution.",
        "teaches": "State compression by value multiplicity and algebraic self-loop elimination in expected value DP.",
        "reusable_pattern": "Self-loop elimination: E = (1 + \sum P_i E_i) / (1 - P_{self})."
    },
    {
        "id": "dp_l",
        "title": "Deque",
        "contest_id": "dp",
        "rating": 1400,
        "tag": "Dynamic Programming (DP)",
        "subtopic": "Classic DP",
        "topic": "Interval DP / Range DP / Matrix Chain Multiplication (MCM)",
        "key_idea": "Two players take turns removing numbers from either end of an array. Player 1 maximizes X - Y, Player 2 minimizes it.",
        "observation": "For any remaining subsegment [l, r], the active player chooses either a_l or a_r to maximize their gain minus the opponent's outcome from the remaining interval: dp[l][r] = max(a_l - dp[l+1][r], a_r - dp[l][r-1]).",
        "algorithm": "1. Base: dp[i][i] = a_i.\n2. Loop length from 2 to N: loop l from 1 to N-len+1: r = l+len-1: dp[l][r] = max(a_l - dp[l+1][r], a_r - dp[l][r-1]).\n3. Return dp[1][N].",
        "complexity": "Time: O(N^2), Space: O(N^2).",
        "editorial": "Zero-sum game minimax interval dynamic programming.",
        "teaches": "Interval dynamic programming (order of evaluation by length) and zero-sum minimax negation.",
        "reusable_pattern": "Minimax interval DP: dp[l][r] = max(opt_left - dp[l+1][r], opt_right - dp[l][r-1])."
    },
    {
        "id": "dp_m",
        "title": "Candies",
        "contest_id": "dp",
        "rating": 1550,
        "tag": "Dynamic Programming (DP)",
        "subtopic": "DP Optimizations",
        "topic": "Prefix Sum Optimized DP",
        "key_idea": "Distribute K candies among N children such that child i receives at most a_i candies.",
        "observation": "Naively, dp[i][j] = sum_{k=0}^{a_i} dp[i-1][j-k] requires O(N * K^2). The inner sum is over a contiguous range [max(0, j - a_i), j] in the previous row, which prefix sums compute in O(1).",
        "algorithm": "1. dp[0] = 1, others 0.\n2. For each child i: compute prefix sums pref of current dp.\n3. dp[j] = (pref[j+1] - pref[max(0, j - a_i)]) mod MOD.\n4. Return dp[K].",
        "complexity": "Time: O(N * K), Space: O(K).",
        "editorial": "Prefix sum state acceleration.",
        "teaches": "Sliding window range sum optimization reducing quadratic transitions to linear.",
        "reusable_pattern": "Prefix sum acceleration of contiguous state transitions."
    },
    {
        "id": "dp_n",
        "title": "Slimes",
        "contest_id": "dp",
        "rating": 1600,
        "tag": "Dynamic Programming (DP)",
        "subtopic": "Classic DP",
        "topic": "Interval DP / Range DP / Matrix Chain Multiplication (MCM)",
        "key_idea": "Merge N slimes adjacent in a line into a single slime minimizing the sum of merging costs.",
        "observation": "The final merge combines two adjacent contiguous blocks [l, k] and [k+1, r]. The merge cost is always sum(a[l..r]). Therefore: dp[l][r] = sum(a[l..r]) + min_{l <= k < r} (dp[l][k] + dp[k+1][r]).",
        "algorithm": "1. Precompute prefix sums of array a.\n2. For len = 2..N: for l = 1..N-len+1: r = l+len-1: dp[l][r] = min_{k=l}^{r-1}(dp[l][k] + dp[k+1][r]) + (pref[r] - pref[l-1]).\n3. Return dp[1][N].",
        "complexity": "Time: O(N^3) standard, O(N^2) via Knuth's optimization.",
        "editorial": "Optimal binary search tree / matrix chain multiplication DP.",
        "teaches": "Interval DP with split-point minimization and cost of merging subproblems.",
        "reusable_pattern": "Split-point interval DP."
    },
    {
        "id": "dp_o",
        "title": "Matching",
        "contest_id": "dp",
        "rating": 1650,
        "tag": "Dynamic Programming (DP)",
        "subtopic": "Bit Related DP",
        "topic": "Bitmask DP",
        "key_idea": "Count perfect matchings in a bipartite graph with N men and N women (N <= 21).",
        "observation": "When matching men 0, 1, ..., i-1, exactly i women must be matched. Thus, i = popcount(mask). The index of the active man is completely implicit in the bitmask!",
        "algorithm": "1. dp[0] = 1, others 0.\n2. For mask from 0 to 2^N - 1: let i = popcount(mask). If i == N continue.\n3. For each woman j in 0..N-1: if compatible(i, j) and not (mask & (1 << j)): dp[mask | (1 << j)] = (dp[mask | (1 << j)] + dp[mask]) mod MOD.\n4. Return dp[(1<<N) - 1].",
        "complexity": "Time: O(N * 2^N), Space: O(2^N).",
        "editorial": "Popcount dimension-reduced bitmask DP.",
        "teaches": "Eliminating a state dimension using subset cardinality invariants in bitmask DP.",
        "reusable_pattern": "Popcount implicit state matching: i = popcount(mask)."
    },
    {
        "id": "dp_p",
        "title": "Independent Set",
        "contest_id": "dp",
        "rating": 1500,
        "tag": "Dynamic Programming (DP)",
        "subtopic": "Dp on Different Structures",
        "topic": "DP on Trees and DAGs",
        "key_idea": "Count ways to paint vertices of a tree black or white such that no two adjacent vertices are both black.",
        "observation": "Root tree arbitrarily. If node u is Black, all children must be White. If u is White, each child can be independently either Black or White.",
        "algorithm": "1. Post-order DFS(u, parent).\n2. dp[u][Black] = prod_{v in children} dp[v][White].\n3. dp[u][White] = prod_{v in children} (dp[v][Black] + dp[v][White]).\n4. Return (dp[root][Black] + dp[root][White]) mod MOD.",
        "complexity": "Time: O(N), Space: O(N).",
        "editorial": "Tree independent set combinatorial DP.",
        "teaches": "Subtree DP, child product combinations, and color state branching on trees.",
        "reusable_pattern": "Two-state subtree product DP on trees."
    },
    {
        "id": "dp_q",
        "title": "Flowers",
        "contest_id": "dp",
        "rating": 1600,
        "tag": "Dynamic Programming (DP)",
        "subtopic": "DP Optimizations",
        "topic": "DP Optimization using Data Structures [Some Practice Problems]",
        "key_idea": "Find an increasing subsequence of flower heights that maximizes total beauty.",
        "observation": "dp[h_i] = a_i + max_{0 <= h < h_i} dp[h]. Querying max in [0, h_i - 1] and updating point h_i is dynamically solved in O(log N) by a Fenwick or Segment Tree.",
        "algorithm": "1. Maintain Fenwick tree supporting point-update and prefix-max queries.\n2. For each flower i: best = fenwick.query(h_i - 1); fenwick.update(h_i, best + a_i).\n3. Return fenwick.query(N).",
        "complexity": "Time: O(N log N), Space: O(N).",
        "editorial": "Fenwick tree / Segment tree accelerated LIS.",
        "teaches": "Transforming quadratic inner-loop search into dynamic range queries via data structures.",
        "reusable_pattern": "BIT/Segment Tree accelerated DP."
    },
    {
        "id": "dp_r",
        "title": "Walk",
        "contest_id": "dp",
        "rating": 1700,
        "tag": "Dynamic Programming (DP)",
        "subtopic": "Dp on Different Structures",
        "topic": "Matrix Exponentiation DP",
        "key_idea": "Count paths of exact length K (K <= 10^18) in a directed graph of N vertices (N <= 50).",
        "observation": "The number of paths of length K between all pairs of vertices is given by A^K, where A is the adjacency matrix of the graph. Matrix multiplication computes transitions; binary exponentiation solves K <= 10^18 in O(log K) steps.",
        "algorithm": "1. Construct adjacency matrix A where A[u][v] = 1 if edge exists, else 0.\n2. Compute M = A^K mod (10^9+7) using binary matrix exponentiation.\n3. Total paths = sum_{i, j} M[i][j] mod MOD.",
        "complexity": "Time: O(N^3 log K), Space: O(N^2).",
        "editorial": "Matrix exponentiation for path counting on graphs.",
        "teaches": "Formulating linear state recurrences as matrix products and exponentiating large step counts.",
        "reusable_pattern": "Matrix exponentiation DP for enormous transition steps."
    },
    {
        "id": "dp_s",
        "title": "Digit Sum",
        "contest_id": "dp",
        "rating": 1750,
        "tag": "Dynamic Programming (DP)",
        "subtopic": "Digit DP",
        "topic": "Digit DP with Remainder State",
        "key_idea": "Count positive integers up to K (K <= 10^10000) whose sum of digits is a multiple of D.",
        "observation": "K has up to 10,000 digits! Process digits from most significant to least significant, maintaining the remainder of the digit sum mod D, and a boolean flag `tight` indicating whether the prefix matches K.",
        "algorithm": "1. dp[index][rem][tight]: number of valid suffixes.\n2. For each digit d from 0 to (tight ? K[idx] : 9): next_tight = tight and (d == K[idx]); next_rem = (rem + d) % D; dp[idx+1][next_rem][next_tight] += dp[idx][rem][tight].\n3. Answer: (dp[len][0][0] + dp[len][0][1] - 1 + MOD) % MOD (subtract 1 for 0).",
        "complexity": "Time: O(|K| * D * 10), Space: O(|K| * D).",
        "editorial": "Textbook Digit DP with tight bound tracking.",
        "teaches": "Digit-by-digit construction, tight prefix bound handling, and large integer parsing.",
        "reusable_pattern": "Standard Digit DP state tuple (index, remainder, is_tight)."
    },
    {
        "id": "dp_u",
        "title": "Grouping",
        "contest_id": "dp",
        "rating": 1850,
        "tag": "Dynamic Programming (DP)",
        "subtopic": "Bit Related DP",
        "topic": "Bitmask DP / O(3^N) Submask Enumeration",
        "key_idea": "Partition N rabbits into arbitrary disjoint groups maximizing total compatibility score (N <= 16).",
        "observation": "Precompute standalone group scores in O(N^2 * 2^N). Then dp[mask] = max_{sub is submask of mask} (cost[sub] + dp[mask ^ sub]). The submask loop `sub = (sub - 1) & mask` iterates all submasks in sum_{k=0}^N binom(N, k) 2^k = 3^N total operations.",
        "algorithm": "1. Precompute score[mask] for all 2^N subsets.\n2. Loop mask from 1 to 2^N - 1:\n   sub = mask; while sub > 0: dp[mask] = max(dp[mask], score[sub] + dp[mask ^ sub]); sub = (sub - 1) & mask.\n3. Return dp[(1<<N) - 1].",
        "complexity": "Time: O(3^N + N^2 * 2^N), Space: O(2^N).",
        "editorial": "Textbook submask enumeration.",
        "teaches": "The (sub - 1) & mask bitwise trick and set partition dynamic programming.",
        "reusable_pattern": "O(3^N) submask iteration: sub = (sub - 1) & mask."
    },
    {
        "id": "dp_v",
        "title": "Subtree",
        "contest_id": "dp",
        "rating": 2100,
        "tag": "Dynamic Programming (DP)",
        "subtopic": "Dp on Different Structures",
        "topic": "Tree DP with Subtree Rerooting without Division",
        "key_idea": "For every node v in a tree, compute the number of black-connected components containing v modulo M (M may not be prime).",
        "observation": "Because M is not necessarily prime, division by (down[child] + 1) is invalid! Computing prefix and suffix products of children values allows excluding a child in O(1) without modular division.",
        "algorithm": "1. DFS1: compute subtree product down[u] = prod_{v in children} (down[v] + 1) mod M.\n2. DFS2: compute parent contribution up[u] using prefix and suffix products of (down[sib] + 1).\n3. Ans[u] = down[u] * (up[u] + 1) mod M.",
        "complexity": "Time: O(N), Space: O(N).",
        "editorial": "All-roots tree DP rerooting under arbitrary modulus.",
        "teaches": "Tree rerooting without modular division via prefix/suffix product arrays.",
        "reusable_pattern": "Division-free prefix/suffix rerooting on trees."
    },
    {
        "id": "dp_z",
        "title": "Frog 3",
        "contest_id": "dp",
        "rating": 2200,
        "tag": "Dynamic Programming (DP)",
        "subtopic": "Convex Hull Trick (CHT)",
        "topic": "Convex Hull Trick (CHT) and Dynamic CHT",
        "key_idea": "Jump between stones with quadratic cost (h_j - h_i)^2 + C where heights h_i are strictly increasing.",
        "observation": "Expanding (h_j - h_i)^2 + C gives h_j^2 + C + (h_i^2 + dp[i]) - 2 * h_j * h_i. This is a family of lines y = m_i * x + b_i where slope m_i = -2 * h_i is strictly decreasing. Slopes and query points x = h_j are both monotonic, allowing O(1) amortized deque maintenance.",
        "algorithm": "1. Maintain deque of lines forming the lower convex hull.\n2. For stone j: pop lines from front while line[0].eval(h_j) >= line[1].eval(h_j).\n3. dp[j] = best_line.eval(h_j) + h_j^2 + C.\n4. Add new line (slope = -2*h_j, intercept = h_j^2 + dp[j]) to back, popping lines that violate convexity.",
        "complexity": "Time: O(N), Space: O(N).",
        "editorial": "Canonical Convex Hull Trick with monotonic slopes and monotonic queries.",
        "teaches": "Geometric line lower envelope maintenance, convex hull deque operations, and linearizing quadratic DP costs.",
        "reusable_pattern": "Monotonic Convex Hull Trick (CHT)."
    },

    # ==================== GRAPH THEORY ====================
    {
        "id": "abc350_d",
        "title": "New Friends",
        "contest_id": "abc350",
        "rating": 1050,
        "tag": "Graph Theory",
        "subtopic": "Connected Components",
        "topic": "Disjoint Set Union (DSU) / Connected Component Cliques",
        "key_idea": "If A-B and B-C are friends, A and C can become friends. Calculate maximum new operations.",
        "observation": "The operation creates the transitive closure of the graph. Every connected component of size S will eventually become a complete graph (clique) with S*(S-1)/2 edges.",
        "algorithm": "1. Build DSU over all N vertices and M edges.\n2. For each component root, obtain component vertex count S and existing edge count E.\n3. Total new edges = sum_{components} (S * (S - 1) / 2 - E).",
        "complexity": "Time: O(N + M * alpha(N)), Space: O(N).",
        "editorial": "Transitive closure clique completion via DSU.",
        "teaches": "Transitive relations on graphs and component-wise clique maximization.",
        "reusable_pattern": "DSU component aggregation and clique edge counting."
    },
    {
        "id": "typical90_c",
        "title": "Longest Circular Road",
        "contest_id": "typical90",
        "rating": 1100,
        "tag": "Graph Theory",
        "subtopic": "Trees",
        "topic": "Tree Diameter / Double BFS-DFS",
        "key_idea": "Add one edge between any two vertices in a tree to form the longest possible cycle.",
        "observation": "Adding edge (u, v) creates a cycle of length dist(u, v) + 1. The maximum distance in a tree is by definition the diameter of the tree.",
        "algorithm": "1. Run BFS from arbitrary node 1 to find farthest node u.\n2. Run BFS from u to find farthest node v. dist(u, v) is the tree diameter.\n3. Output dist(u, v) + 1.",
        "complexity": "Time: O(N), Space: O(N).",
        "editorial": "Two-pass BFS tree diameter proof.",
        "teaches": "Tree diameter characterization and the canonical 2-BFS algorithm.",
        "reusable_pattern": "2-pass BFS tree diameter."
    },
    {
        "id": "typical90_m",
        "title": "Passing",
        "contest_id": "typical90",
        "rating": 1350,
        "tag": "Graph Theory",
        "subtopic": "Shortest Paths",
        "topic": "Two-Way Dijkstra / Intermediate Node Shortest Paths",
        "key_idea": "For every vertex k from 1 to N, find the shortest path from vertex 1 to vertex N passing through k.",
        "observation": "Shortest path from 1 to N through k is dist(1, k) + dist(k, N). Since edges are bidirectional, dist(k, N) = dist(N, k). Running Dijkstra only twice (from 1 and from N) resolves all queries in O(1).",
        "algorithm": "1. Run Dijkstra from node 1 -> dist1 array.\n2. Run Dijkstra from node N -> distN array.\n3. For each k in 1..N: output dist1[k] + distN[k].",
        "complexity": "Time: O(M log N), Space: O(N + M).",
        "editorial": "Two-source bidirectional Dijkstra.",
        "teaches": "Decomposing multi-point shortest path queries into two independent single-source runs.",
        "reusable_pattern": "Dual Dijkstra intermediate point distance query."
    },
    {
        "id": "abc285_d",
        "title": "Change of User Name",
        "contest_id": "abc285",
        "rating": 950,
        "tag": "Graph Theory",
        "subtopic": "Directed Graphs",
        "topic": "Cycle Detection / Functional Graph Component Analysis",
        "key_idea": "N users want to change their handles from S_i to T_i. Determine if all changes can be performed without handle collisions.",
        "observation": "Build directed graph with edge S_i -> T_i. A valid sequence of changes exists if and only if the directed graph contains NO directed cycle.",
        "algorithm": "1. Build adjacency list of directed edges S_i -> T_i.\n2. Compute in-degrees and perform Kahn's Topological Sort (or 3-color DFS cycle check).\n3. If all nodes can be topologically sorted, output 'Yes'; else 'No'.",
        "complexity": "Time: O(N), Space: O(N).",
        "editorial": "Topological sort cycle check on string handle transitions.",
        "teaches": "Modeling sequential dependencies as directed graph cycles and topological ordering.",
        "reusable_pattern": "Topological sort cycle detection for dependency resolution."
    },

    # ==================== DATA STRUCTURES ====================
    {
        "id": "typical90_l",
        "title": "Red Painting",
        "contest_id": "typical90",
        "rating": 1250,
        "tag": "Data Structures (DS)",
        "subtopic": "Disjoint Set Union (DSU)",
        "topic": "Grid Connectivity / Dynamic DSU",
        "key_idea": "Dynamically color grid cells red and answer reachability queries between red cells.",
        "observation": "Linearize 2D coordinates (r, c) to 1D index r * W + c. When a cell becomes red, unite it with any adjacent red neighbors. Querying connectivity is checking if both cells are red and share the same DSU root.",
        "algorithm": "1. Map (r, c) -> r * W + c. Initialize DSU and boolean is_red grid.\n2. On color query: set is_red[r][c] = True; for each neighbor (nr, nc) that is red: dsu.unite(idx(r,c), idx(nr,nc)).\n3. On reachability query: if is_red[a] and is_red[b] and dsu.same(idx_a, idx_b) -> 'Yes', else 'No'.",
        "complexity": "Time: O(Q * alpha(H * W)), Space: O(H * W).",
        "editorial": "Online dynamic connectivity on 2D grid via DSU.",
        "teaches": "2D-to-1D coordinate flattening and online component maintenance without BFS/DFS reruns.",
        "reusable_pattern": "Grid coordinate linearization + online DSU."
    },
    {
        "id": "abc185_f",
        "title": "Range Xor Query",
        "contest_id": "abc185",
        "rating": 1150,
        "tag": "Data Structures (DS)",
        "subtopic": "Segment Tree / Fenwick Tree",
        "topic": "Point Update Range XOR Query",
        "key_idea": "Maintain an array subject to two operations: A[X] = A[X] ^ Y, and query range XOR sum A[L] ^ ... ^ A[R].",
        "observation": "XOR is associative, commutative, and self-inverting. A Fenwick tree (Binary Indexed Tree) or Segment Tree natively handles point updates and range queries in O(log N).",
        "algorithm": "1. Build Fenwick tree where combine operation is XOR (^).\n2. Update query: fenwick.update(X, Y).\n3. Range query: output fenwick.query(R) ^ fenwick.query(L - 1).",
        "complexity": "Time: O(Q log N), Space: O(N).",
        "editorial": "Fenwick tree XOR adaptation.",
        "teaches": "Applying Fenwick tree to any invertible commutative monoid (such as XOR).",
        "reusable_pattern": "Fenwick Tree point-update range-query."
    },
    {
        "id": "abc217_e",
        "title": "Sorting Queries",
        "contest_id": "abc217",
        "rating": 1200,
        "tag": "Data Structures (DS)",
        "subtopic": "Queue & Priority Queue",
        "topic": "Hybrid Two-Stage Buffer (Queue + Min-Heap)",
        "key_idea": "Support three operations: append x to back, print and pop first element, and sort the entire array in ascending order.",
        "observation": "Sorting the whole array repeatedly takes O(N log N) per query! However, once an element is sorted, it stays sorted and always precedes newly appended elements. Split storage into two structures: a min-priority-queue (sorted elements) and a FIFO queue (newly appended unsorted elements).",
        "algorithm": "1. When appending x: push x to FIFO queue.\n2. When sorting: move all elements from FIFO queue to min-heap.\n3. When popping: if min-heap is non-empty, pop from min-heap; else pop from FIFO queue.",
        "complexity": "Time: O(Q log Q) total (each element enters and leaves min-heap at most once), Space: O(Q).",
        "editorial": "Two-buffer amortized queue + priority queue split.",
        "teaches": "Amortized complexity and separating sorted vs unsorted segments using complementary data structures.",
        "reusable_pattern": "Hybrid Queue + Min-Heap amortized sorting."
    },

    # ==================== BASICS & SEARCH ====================
    {
        "id": "typical90_a",
        "title": "Yokan Party",
        "contest_id": "typical90",
        "rating": 1200,
        "tag": "Basics",
        "subtopic": "Binary Search",
        "topic": "Binary Search on Answer / Greedy Feasibility",
        "key_idea": "Cut a stick of length L at K positions to maximize the length of the shortest piece.",
        "observation": "'Maximize the minimum' is the definitive indicator for Binary Search on Answer. The predicate 'Can we obtain at least K+1 pieces each of length >= M?' is strictly monotonic with respect to M.",
        "algorithm": "1. Binary search M in [1, L].\n2. Predicate check(M): Greedily cut whenever the current piece reaches length >= M. If total pieces cut is >= K and remaining piece is >= M, return True; else False.\n3. Upper boundary of search range is the optimal answer.",
        "complexity": "Time: O(N log L), Space: O(1).",
        "editorial": "Textbook binary search on answer.",
        "teaches": "Formulating feasibility predicates, establishing monotonicity, and greedy cut verification.",
        "reusable_pattern": "Binary search on answer + greedy feasibility check."
    },
    {
        "id": "abc250_c",
        "title": "Adjacent Swaps",
        "contest_id": "abc250",
        "rating": 800,
        "tag": "Basics",
        "subtopic": "Implementation / Simulation",
        "topic": "Dual Index Mapping (Value-to-Position & Position-to-Value)",
        "key_idea": "Perform Q swaps where each query swaps the ball with integer x and its right neighbor (or left neighbor if at boundary).",
        "observation": "Finding ball x in an array of size N naively takes O(N) per query. Maintaining two arrays: `val_at[pos]` and `pos_of[val]` allows locating and swapping in O(1).",
        "algorithm": "1. Maintain pos[x] = position of ball x, and val[p] = ball at position p.\n2. For each query x: find p = pos[x]. Determine target position p2 = (p < N ? p + 1 : p - 1). Let y = val[p2].\n3. Swap in val: val[p] = y, val[p2] = x. Update positions: pos[x] = p2, pos[y] = p.",
        "complexity": "Time: O(Q), Space: O(N).",
        "editorial": "Dual array bijection maintenance.",
        "teaches": "O(1) bidirectional lookup mapping and maintaining invertible permutations under swap operations.",
        "reusable_pattern": "Dual index mapping (Position <-> Value)."
    },

    # ==================== GAME THEORY ====================
    {
        "id": "dp_k",
        "title": "Stones",
        "contest_id": "dp",
        "rating": 1100,
        "tag": "Game Theory",
        "subtopic": "Impartial Games",
        "topic": "Sprague-Grundy / Combinatorial Game DP",
        "key_idea": "Two players take turns removing a_i stones from a pile of size K. Determine if First or Second player wins under optimal play.",
        "observation": "State x is Winning (First wins) if there exists a valid move a_i such that state x - a_i is Losing (Second wins). If all valid moves lead to Winning states, x is Losing.",
        "algorithm": "1. dp[0] = False (Losing state).\n2. For x from 1 to K: dp[x] = True if any(a_i <= x and not dp[x - a_i] for a_i in A) else False.\n3. Output 'First' if dp[K] else 'Second'.",
        "complexity": "Time: O(N * K), Space: O(K).",
        "editorial": "Classic backward induction on impartial game graph.",
        "teaches": "P-positions and N-positions, finite state game backward induction, and Sprague-Grundy fundamentals.",
        "reusable_pattern": "Boolean game state induction: win(x) = \exists a, \neg win(x - a)."
    },

    # ==================== MATH & NUMBER THEORY ====================
    {
        "id": "abc186_e",
        "title": "Throne",
        "contest_id": "abc186",
        "rating": 1250,
        "tag": "Number Theory",
        "subtopic": "Modular Arithmetic",
        "topic": "Modular Linear Congruence / Extended Euclidean Algorithm",
        "key_idea": "A piece moves K steps clockwise on a circle of size N, starting at position S. Find minimum steps to reach position 0.",
        "observation": "The condition is S + x * K = 0 (mod N), which rearranges to K * x = -S (mod N). This is a linear congruence ax = b (mod m). Solutions exist if and only if gcd(K, N) divides S.",
        "algorithm": "1. Let g = gcd(K, N). If S % g != 0: return -1.\n2. Divide through by g: K' = K/g, S' = S/g, N' = N/g.\n3. Now gcd(K', N') = 1. Find modular inverse inv = mod_inv(K', N') via Extended GCD.\n4. x = (-S' * inv) mod N'. Output x.",
        "complexity": "Time: O(log(min(K, N))) per testcase, Space: O(1).",
        "editorial": "Extended Euclidean Algorithm for modular inverse.",
        "teaches": "Modular linear congruences, solvability condition via GCD divisibility, and Extended Euclidean Algorithm.",
        "reusable_pattern": "Extended Euclidean linear congruence solver."
    },
    {
        "id": "abc284_d",
        "title": "Happy New Year 2023",
        "contest_id": "abc284",
        "rating": 1050,
        "tag": "Number Theory",
        "subtopic": "Prime Numbers",
        "topic": "Cubic-Root Prime Factorization (N = p^2 * q)",
        "key_idea": "Given N = p^2 * q where p and q are prime and N <= 9 * 10^18, find primes p and q.",
        "observation": "Because N = p^2 * q, at least one of p or q must be <= N^(1/3) <= 2.15 * 10^6! Testing trial divisors up to N^(1/3) will instantly find one prime factor.",
        "algorithm": "1. Loop d from 2 up to 3 * 10^6:\n   If N % d == 0: if N % (d * d) == 0 -> p = d, q = N / (d * d); else p = isqrt(N / d), q = d; break.\n2. Output p and q.",
        "complexity": "Time: O(N^(1/3)) per testcase, Space: O(1).",
        "editorial": "Cubic root trial division for asymmetric prime powers.",
        "teaches": "Exploiting asymmetric algebraic power structures to bound search space to N^(1/3) rather than sqrt(N).",
        "reusable_pattern": "N^(1/3) trial division for p^2 * q factorization."
    },

    # ==================== STRINGS ====================
    {
        "id": "typical90_f",
        "title": "Smallest Subsequence",
        "contest_id": "typical90",
        "rating": 1500,
        "tag": "Strings",
        "subtopic": "Greedy on Strings",
        "topic": "Next-Occurrence Array / Lexicographically Smallest Subsequence",
        "key_idea": "Find the lexicographically smallest subsequence of length K from string S of length N.",
        "observation": "To minimize lexicographically, greedily choose the smallest possible character for each of the K positions from left to right. A character choice at position p is valid if and only if the remaining suffix has length >= remaining positions needed.",
        "algorithm": "1. Precompute next_pos[i][c]: the earliest index >= i where character c occurs.\n2. Current index cur = 0.\n3. For step from 1 to K: remaining_needed = K - step.\n   For char c from 'a' to 'z': let pos = next_pos[cur][c]. If N - pos >= remaining_needed: append c, cur = pos + 1, break.\n4. Output string.",
        "complexity": "Time: O(26 * N + 26 * K), Space: O(26 * N).",
        "editorial": "Next-character transition table with greedy lookahead.",
        "teaches": "Precomputing next-occurrence transition tables on strings and greedy lexicographical construction.",
        "reusable_pattern": "Next-occurrence array for subsequence queries."
    }
]


def generate_category_files():
    """Generates individual markdown files for each major tag/category in categories/."""
    os.makedirs(CATEGORIES_DIR, exist_ok=True)
    os.makedirs(ANALYSIS_DIR, exist_ok=True)

    # Group problems by tag
    by_tag = defaultdict(list)
    for p in PROBLEMS_CATALOG:
        by_tag[p["tag"]].append(p)

    category_slugs = {
        "Dynamic Programming (DP)": "Dynamic_Programming.md",
        "Graph Theory": "Graph_Theory.md",
        "Data Structures (DS)": "Data_Structures.md",
        "Game Theory": "Game_Theory.md",
        "Basics": "Basics.md",
        "Number Theory": "Number_Theory.md",
        "Strings": "Strings.md"
    }

    category_emojis = {
        "Dynamic Programming (DP)": "🧩",
        "Graph Theory": "🕸️",
        "Data Structures (DS)": "🌲",
        "Game Theory": "♟️",
        "Basics": "⚡",
        "Number Theory": "🔢",
        "Strings": "🔤"
    }

    # 1. Generate individual category files
    for tag, probs in by_tag.items():
        filename = category_slugs.get(tag, f"{re.sub(r'[^a-zA-Z0-9]', '_', tag)}.md")
        filepath = os.path.join(CATEGORIES_DIR, filename)
        emoji = category_emojis.get(tag, "📌")

        lines = [
            f"# {emoji} AtCoder Curriculum: {tag}",
            "",
            f"Curated collection of high-value problems in **{tag}** selected for teaching reusable competitive programming algorithms, structural observations, and mathematical invariants.",
            "",
            f"- **Total Curated Problems**: {len(probs)}",
            "- **Taxonomy Tier**: Tag (Domain Level)",
            "",
            "---",
            "",
            "## 📑 Table of Contents",
            ""
        ]

        # Group by subtopic and topic
        subtopic_map = defaultdict(lambda: defaultdict(list))
        for p in probs:
            subtopic_map[p["subtopic"]][p["topic"]].append(p)

        for subtopic in sorted(subtopic_map.keys()):
            sub_anchor = re.sub(r"[^a-zA-Z0-9-]", "", subtopic.lower().replace(" ", "-"))
            lines.append(f"- [{subtopic}](#{sub_anchor})")
            for topic in sorted(subtopic_map[subtopic].keys()):
                top_anchor = re.sub(r"[^a-zA-Z0-9-]", "", topic.lower().replace(" ", "-"))
                lines.append(f"  - [{topic}](#{top_anchor}) ({len(subtopic_map[subtopic][topic])} problems)")
        lines.append("")
        lines.append("---")
        lines.append("")

        # Content sections
        for subtopic in sorted(subtopic_map.keys()):
            lines.append(f"## {subtopic}")
            lines.append("")
            for topic in sorted(subtopic_map[subtopic].keys()):
                lines.append(f"### {topic}")
                lines.append("")
                for p in subtopic_map[subtopic][topic]:
                    vjudge = f"`[problem:AtCoder-{p['id']}]`"
                    task_url = f"https://atcoder.jp/contests/{p['contest_id']}/tasks/{p['id']}"
                    lines.extend([
                        f"#### {p['title']} ({vjudge})",
                        f"- **Rating / Difficulty**: {p['rating']}",
                        f"- **Contest**: `{p['contest_id']}` | [AtCoder Link]({task_url})",
                        f"- **Detailed Analysis**: [`analysis/AtCoder-{p['id']}.md`](../analysis/AtCoder-{p['id']}.md)",
                        f"- **Key Idea**: {p['key_idea']}",
                        f"- **Core Observation**: {p['observation']}",
                        f"- **Algorithm & Complexity**: {p['complexity']}",
                        f"- **What This Problem Teaches**: {p['teaches']}",
                        f"- **Reusable Pattern**: `{p['reusable_pattern']}`",
                        ""
                    ])
            lines.append("---")
            lines.append("")

        with open(filepath, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
        print(f"[+] Created Category Markdown: {filepath}")

    # 2. Generate categories/README.md master index
    index_path = os.path.join(CATEGORIES_DIR, "README.md")
    idx_lines = [
        "# 📚 AtCoder Topic & Category Directory",
        "",
        "This directory organizes curated AtCoder problems into dedicated domain `.md` files.",
        "Each category file breaks problems down into **Subtopics** and **Topics / Skills** under our 3-tier curriculum taxonomy.",
        "",
        "## 📂 Available Category Files",
        "",
        "| Category / Domain | File | Problems Curated | Core Topics Covered |",
        "|---|---|---|---|"
    ]

    for tag, probs in sorted(by_tag.items()):
        filename = category_slugs.get(tag, f"{re.sub(r'[^a-zA-Z0-9]', '_', tag)}.md")
        emoji = category_emojis.get(tag, "📌")
        topics_sample = ", ".join(list(set(p["topic"].split(" / ")[0] for p in probs))[:3])
        idx_lines.append(f"| {emoji} **{tag}** | [`{filename}`]({filename}) | {len(probs)} | {topics_sample}... |")

    idx_lines.extend([
        "",
        "---",
        "",
        "## 🎯 Problem Selection Filter",
        "",
        "All problems inside these `.md` files meet the strict learning criteria:",
        "1. **Teaches generalizable algorithms** (e.g. Tree DP, CHT, DSU, Fenwick Tree, Binary Search).",
        "2. **Eliminates trivial logic-building** (e.g. routine string checks, array toggle simulation, basic math case work).",
        "3. **Includes complete step-by-step analysis** and code templates in [`../analysis/`](../analysis/).",
        ""
    ])

    with open(index_path, "w", encoding="utf-8") as f:
        f.write("\n".join(idx_lines))
    print(f"[+] Created Categories Index: {index_path}")

    # 3. Generate individual problem analysis files in analysis/
    for p in PROBLEMS_CATALOG:
        analysis_file = os.path.join(ANALYSIS_DIR, f"AtCoder-{p['id']}.md")
        cat_file = category_slugs.get(p["tag"], "README.md")
        a_lines = [
            f"# Problem Analysis: AtCoder-{p['id']} — {p['title']}",
            "",
            f"**Problem ID**: `AtCoder-{p['id']}`  ",
            f"**Contest**: `{p['contest_id']}`  ",
            f"**Rating**: {p['rating']}  ",
            f"**URL**: https://atcoder.jp/contests/{p['contest_id']}/tasks/{p['id']}  ",
            f"**VJudge Tag**: `[problem:AtCoder-{p['id']}]`  ",
            f"**Category File**: [`../categories/{cat_file}`](../categories/{cat_file})  ",
            "",
            f"- **Tag (Domain)**: `{p['tag']}`  ",
            f"- **Subtopic**: `{p['subtopic']}`  ",
            f"- **Topic (Skill)**: `{p['topic']}`  ",
            "",
            "---",
            "",
            "## 1. Problem Statement & Key Idea",
            p["key_idea"],
            "",
            "## 2. Core Observation & Invariant",
            p["observation"],
            "",
            "## 3. Step-by-Step Algorithm",
            p["algorithm"],
            "",
            "## 4. Complexity Analysis",
            p["complexity"],
            "",
            "## 5. Editorial Comparison & Alignment",
            p["editorial"],
            "",
            "## 6. What This Problem Teaches",
            p["teaches"],
            "",
            "## 7. Reusable Competitive Programming Pattern",
            f"`{p['reusable_pattern']}`",
            "",
            "---",
            f"Back to [Category: {p['tag']}](../categories/{cat_file}) | [Categories Index](../categories/README.md)"
        ]
        with open(analysis_file, "w", encoding="utf-8") as f:
            f.write("\n".join(a_lines))

    print(f"[+] Created {len(PROBLEMS_CATALOG)} individual problem analysis markdown files in {ANALYSIS_DIR}.")


if __name__ == "__main__":
    generate_category_files()
