#!/usr/bin/env python3
"""
AtCoder Hierarchical Category Markdown Builder
==============================================
Creates topic-level `.md` files organized inside tag/domain folders:
categories/
├── dp/
│   ├── dp_on_trees.md
│   ├── bitmask_dp.md
│   ├── digit_dp.md
│   ├── knapsack.md
│   ├── interval_dp.md
│   ├── prefix_sum_dp.md
│   ├── convex_hull_trick.md
│   ├── 1d_dp.md
│   ├── probability_expected_value_dp.md
│   └── matrix_exponentiation_dp.md
├── graph_theory/
│   ├── connected_components_dsu.md
│   ├── tree_diameter.md
│   ├── shortest_paths_dijkstra.md
│   └── topological_sort_cycles.md
├── data_structures/
│   ├── online_grid_dsu.md
│   ├── fenwick_segment_tree.md
│   └── priority_queue_buffers.md
├── basics/
│   ├── binary_search_on_answer.md
│   └── dual_index_mapping.md
├── game_theory/
│   └── sprague_grundy_impartial_games.md
├── number_theory/
│   ├── modular_linear_congruence.md
│   └── cubic_root_prime_factorization.md
└── strings/
    └── lexicographically_smallest_subsequence.md
"""

import os
import json
import re
from collections import defaultdict
from typing import Dict, List, Any

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
CATEGORIES_DIR = os.path.join(BASE_DIR, "categories")

# Organized Topic Definitions and Problem Mappings
TOPIC_MARKDOWNS = [
    # ==================== DYNAMIC PROGRAMMING ====================
    {
        "tag_folder": "dp",
        "tag_name": "Dynamic Programming (DP)",
        "file_name": "dp_on_trees.md",
        "topic_title": "DP on Trees & DAGs",
        "subtopic": "Dp on Different Structures",
        "overview": "Dynamic programming defined on tree structures and Directed Acyclic Graphs. Tree DP typically proceeds via bottom-up post-order DFS where each node aggregates optimal substructure from its subtrees, or via two-pass all-roots tree rerooting.",
        "problems": [
            {
                "id": "dp_p",
                "title": "Independent Set",
                "contest_id": "dp",
                "rating": 1500,
                "role": "Foundational Subtree Tree DP",
                "statement_summary": "Count ways to paint vertices of a tree black or white such that no two adjacent vertices are both black.",
                "key_idea": "Root the tree arbitrarily. Maintain two states per node u: dp[u][Black] and dp[u][White].",
                "core_observation": "If node u is Black, all children MUST be White. If u is White, each child v can independently be Black or White. Transitions combine via multiplication over children subtrees.",
                "algorithm": "1. Post-order DFS(u, parent).\n2. dp[u][Black] = prod_{v in children} dp[v][White].\n3. dp[u][White] = prod_{v in children} (dp[v][Black] + dp[v][White]).\n4. Return (dp[root][Black] + dp[root][White]) mod 10^9+7.",
                "complexity": "Time: O(N), Space: O(N).",
                "editorial": "Standard 2-state tree independent set counting.",
                "teaches": "Subtree DP, state-color branching, and product-rule combination over tree children.",
                "reusable_pattern": "Two-state subtree product DP on trees."
            },
            {
                "id": "dp_v",
                "title": "Subtree",
                "contest_id": "dp",
                "rating": 2100,
                "role": "Advanced All-Roots Tree Rerooting (Without Division)",
                "statement_summary": "For EVERY vertex v in a tree, count the number of black-connected components containing v modulo M (M may not be prime).",
                "key_idea": "Reroot the tree in O(N) using two DFS passes. Because M is composite, division by (down[child] + 1) is illegal; prefix and suffix products of children answers exclude a child in O(1) without division.",
                "core_observation": "For each node, children values can be preprocessed into prefix and suffix cumulative products. Excluded child contribution is calculated by multiplying prefix[:i-1] * suffix[i+1:].",
                "algorithm": "1. DFS1: down[u] = prod_{v in children} (down[v] + 1) mod M.\n2. DFS2: compute parent contribution up[u] using prefix and suffix products of sibling values.\n3. Ans[u] = down[u] * (up[u] + 1) mod M.",
                "complexity": "Time: O(N), Space: O(N).",
                "editorial": "All-roots tree DP rerooting with non-invertible operators.",
                "teaches": "Tree rerooting technique without modular division via prefix/suffix product arrays.",
                "reusable_pattern": "Division-free prefix/suffix rerooting on trees."
            },
            {
                "id": "dp_g",
                "title": "Longest Path",
                "contest_id": "dp",
                "rating": 1350,
                "role": "Topological Order DP on DAGs",
                "statement_summary": "Find the length of the longest directed path in a Directed Acyclic Graph (DAG).",
                "key_idea": "Since the graph has no directed cycles, topological ordering exists. The longest path starting at u is dp[u] = 1 + max_{(u, v) in E} dp[v].",
                "core_observation": "Acyclic structure guarantees no circular dependencies. Memoized DFS evaluates each vertex and edge exactly once.",
                "algorithm": "1. Memoized DFS: memo[u] = -1.\n2. DFS(u): if memo[u] != -1 return memo[u]. ans = 0. For each neighbor v: ans = max(ans, 1 + DFS(v)). memo[u] = ans.\n3. Return max_{u} DFS(u).",
                "complexity": "Time: O(V + E), Space: O(V + E).",
                "editorial": "Topological sort DP on DAG.",
                "teaches": "Topological ordering as the fundamental validity condition for DAG DP.",
                "reusable_pattern": "Memoized DFS transition over DAG edges."
            }
        ]
    },
    {
        "tag_folder": "dp",
        "tag_name": "Dynamic Programming (DP)",
        "file_name": "bitmask_dp.md",
        "topic_title": "Bitmask DP & Submask Enumeration",
        "subtopic": "Bit Related DP",
        "overview": "Dynamic programming where subsets of elements are represented as integer bitmasks. Key techniques include popcount-based dimension reduction and exhaustive O(3^N) submask iteration.",
        "problems": [
            {
                "id": "dp_o",
                "title": "Matching",
                "contest_id": "dp",
                "rating": 1650,
                "role": "Bipartite Matching Bitmask DP",
                "statement_summary": "Count perfect matchings in a bipartite graph with N men and N women (N <= 21).",
                "key_idea": "When matching men 0, 1, ..., i-1, exactly i women must be chosen. Thus, i = popcount(mask). The index of the active man is implicit in the bitmask!",
                "core_observation": "By iterating masks by popcount or sequentially from 0 to 2^N - 1, we eliminate the man dimension entirely: dp[mask | (1 << j)] += dp[mask].",
                "algorithm": "1. dp[0] = 1, all other dp = 0.\n2. For mask from 0 to 2^N - 1: let i = popcount(mask). If i == N, continue.\n3. For each woman j in 0..N-1: if compatible(i, j) and not (mask & (1 << j)): dp[mask | (1 << j)] = (dp[mask | (1 << j)] + dp[mask]) mod MOD.\n4. Return dp[(1<<N) - 1].",
                "complexity": "Time: O(N * 2^N), Space: O(2^N).",
                "editorial": "Popcount dimension-reduced bitmask DP.",
                "teaches": "Dimension reduction in Bitmask DP using subset cardinality invariants.",
                "reusable_pattern": "Popcount implicit state matching: i = popcount(mask)."
            },
            {
                "id": "dp_u",
                "title": "Grouping",
                "contest_id": "dp",
                "rating": 1850,
                "role": "O(3^N) Submask Partition DP",
                "statement_summary": "Partition N rabbits into arbitrary groups to maximize total compatibility score (N <= 16).",
                "key_idea": "Precompute standalone group scores in O(N^2 * 2^N). Then dp[mask] = max_{sub is submask of mask} (score[sub] + dp[mask ^ sub]).",
                "core_observation": "Iterating submasks via `sub = (sub - 1) & mask` visits each submask without redundant branches. Over all 2^N masks, total operations equal sum_{k=0}^N binom(N, k) 2^k = 3^N.",
                "algorithm": "1. Precompute score[mask] for all 2^N subsets.\n2. Loop mask from 1 to 2^N - 1:\n   sub = mask; while sub > 0: dp[mask] = max(dp[mask], score[sub] + dp[mask ^ sub]); sub = (sub - 1) & mask.\n3. Return dp[(1<<N) - 1].",
                "complexity": "Time: O(3^N + N^2 * 2^N), Space: O(2^N).",
                "editorial": "Textbook submask enumeration.",
                "teaches": "The (sub - 1) & mask bit trick and set partition dynamic programming.",
                "reusable_pattern": "O(3^N) submask iteration: sub = (sub - 1) & mask."
            }
        ]
    },
    {
        "tag_folder": "dp",
        "tag_name": "Dynamic Programming (DP)",
        "file_name": "digit_dp.md",
        "topic_title": "Digit DP",
        "subtopic": "Digit DP",
        "overview": "Constructing numbers digit by digit from most significant to least significant, maintaining prefix equality bounds (tight constraint) and modular properties.",
        "problems": [
            {
                "id": "dp_s",
                "title": "Digit Sum",
                "contest_id": "dp",
                "rating": 1750,
                "role": "Canonical Digit DP with Remainder State",
                "statement_summary": "Count positive integers up to K (K <= 10^10000) whose sum of digits is a multiple of D.",
                "key_idea": "Process K as a string of up to 10,000 digits. Maintain state (index, remainder_mod_D, tight_flag).",
                "core_observation": "At index i, if tight is True, the next digit can only range from 0 to K[i]. If tight is False, the next digit can range from 0 to 9 freely.",
                "algorithm": "1. dp[index][rem][tight]: count of valid prefix configurations.\n2. For each digit d in 0..(tight ? K[idx] : 9): dp[idx+1][(rem + d) % D][tight and (d == K[idx])] += dp[idx][rem][tight].\n3. Final count = (dp[len][0][0] + dp[len][0][1] - 1 + MOD) % MOD.",
                "complexity": "Time: O(|K| * D * 10), Space: O(|K| * D).",
                "editorial": "Textbook Digit DP with tight bound tracking.",
                "teaches": "Digit-by-digit construction, tight prefix bound handling, and large integer parsing.",
                "reusable_pattern": "Standard Digit DP state tuple (index, remainder, is_tight)."
            }
        ]
    },
    {
        "tag_folder": "dp",
        "tag_name": "Dynamic Programming (DP)",
        "file_name": "knapsack.md",
        "topic_title": "Knapsack DP & Dual State Inversion",
        "subtopic": "Intro to DP",
        "overview": "The knapsack paradigm, covering classic 0/1 knapsack with weight as state, and dual knapsack where weight capacity is astronomical and value is inverted into the state index.",
        "problems": [
            {
                "id": "dp_d",
                "title": "Knapsack 1",
                "contest_id": "dp",
                "rating": 1150,
                "role": "0/1 Knapsack with 1D Memory Compression",
                "statement_summary": "Maximize value of items with total weight <= W (W <= 10^5, N <= 100).",
                "key_idea": "Standard 0/1 Knapsack where capacity W is moderate enough to serve as array index.",
                "core_observation": "Looping weight downwards from W to w_i ensures each item is included at most once in a 1D DP array.",
                "algorithm": "1. dp[0..W] = 0.\n2. For each item (w_i, v_i): for cap from W down to w_i: dp[cap] = max(dp[cap], dp[cap - w_i] + v_i).\n3. Result is max(dp).",
                "complexity": "Time: O(N * W), Space: O(W).",
                "editorial": "Standard 1D reverse-iteration 0/1 Knapsack.",
                "teaches": "0/1 Knapsack state optimization and 1D space reduction technique.",
                "reusable_pattern": "1D space-optimized 0/1 knapsack."
            },
            {
                "id": "dp_e",
                "title": "Knapsack 2",
                "contest_id": "dp",
                "rating": 1450,
                "role": "Dual Knapsack / Value as State",
                "statement_summary": "Solve 0/1 Knapsack when capacity W <= 10^9 is enormous, but v_i <= 1000 and N <= 100.",
                "key_idea": "When capacity W is up to 10^9, weight cannot be an array index. Invert the state: define dp[v] as the minimum weight required to achieve exact value v.",
                "core_observation": "Total value sum <= 100 * 1000 = 10^5. The value dimension is pseudopolynomial while weight is not.",
                "algorithm": "1. V_sum = sum(v_i). dp[0] = 0, dp[1..V_sum] = INF.\n2. For each item (w_i, v_i): for v from V_sum down to v_i: dp[v] = min(dp[v], dp[v - v_i] + w_i).\n3. Return max v such that dp[v] <= W.",
                "complexity": "Time: O(N * sum(V)), Space: O(sum(V)).",
                "editorial": "Dual problem formulation and state parameter swapping.",
                "teaches": "Swapping objective function and state dimension when constraints are large but values are compact.",
                "reusable_pattern": "Dual DP parameter inversion."
            }
        ]
    },
    {
        "tag_folder": "dp",
        "tag_name": "Dynamic Programming (DP)",
        "file_name": "interval_dp.md",
        "topic_title": "Interval DP & Range Merging",
        "subtopic": "Classic DP",
        "overview": "Subproblems defined over contiguous intervals [l, r], solved by increasing interval length. Covers minimax game intervals and optimal split-point merges.",
        "problems": [
            {
                "id": "dp_l",
                "title": "Deque",
                "contest_id": "dp",
                "rating": 1400,
                "role": "Minimax Game Interval DP",
                "statement_summary": "Two players remove numbers from either end of an array. Player 1 maximizes X - Y, Player 2 minimizes it.",
                "key_idea": "Over remaining subsegment [l, r], the active player chooses either a_l or a_r: dp[l][r] = max(a_l - dp[l+1][r], a_r - dp[l][r-1]).",
                "core_observation": "The game is zero-sum. Negation accounts for player alternation: your score advantage equals your choice minus the opponent's optimal advantage from the remainder.",
                "algorithm": "1. Base: dp[i][i] = a_i.\n2. Loop len from 2 to N: loop l from 1 to N-len+1: r = l+len-1: dp[l][r] = max(a_l - dp[l+1][r], a_r - dp[l][r-1]).\n3. Return dp[1][N].",
                "complexity": "Time: O(N^2), Space: O(N^2).",
                "editorial": "Zero-sum minimax interval DP.",
                "teaches": "Interval dynamic programming evaluated by segment length and minimax negation.",
                "reusable_pattern": "Minimax interval DP: dp[l][r] = max(opt_left - dp[l+1][r], opt_right - dp[l][r-1])."
            },
            {
                "id": "dp_n",
                "title": "Slimes",
                "contest_id": "dp",
                "rating": 1600,
                "role": "Matrix Chain Multiplication / Split-Point Range DP",
                "statement_summary": "Merge adjacent slimes pairwise into one slime with minimum total combination cost.",
                "key_idea": "The final combine step joins two sub-blocks [l, k] and [k+1, r] with cost sum(a[l..r]).",
                "core_observation": "dp[l][r] = sum(a[l..r]) + min_{l <= k < r} (dp[l][k] + dp[k+1][r]). Prefix sums yield sum(a[l..r]) in O(1).",
                "algorithm": "1. Precompute prefix sums.\n2. For len = 2..N: for l = 1..N-len+1: r = l+len-1: dp[l][r] = min_{k=l}^{r-1}(dp[l][k] + dp[k+1][r]) + (pref[r] - pref[l-1]).\n3. Return dp[1][N].",
                "complexity": "Time: O(N^3) standard, O(N^2) via Knuth optimization.",
                "editorial": "Optimal binary search tree / matrix chain multiplication DP.",
                "teaches": "Interval DP with split-point minimization and cost of merging subproblems.",
                "reusable_pattern": "Split-point interval DP."
            }
        ]
    },
    {
        "tag_folder": "dp",
        "tag_name": "Dynamic Programming (DP)",
        "file_name": "convex_hull_trick.md",
        "topic_title": "Convex Hull Trick (CHT) & DP Optimization",
        "subtopic": "Convex Hull Trick (CHT)",
        "overview": "Optimizing transitions of the form dp[i] = min_{j < i} (dp[j] + cost(j, i)) where cost can be linearized into lines y = m*x + b.",
        "problems": [
            {
                "id": "dp_z",
                "title": "Frog 3",
                "contest_id": "dp",
                "rating": 2200,
                "role": "Monotonic Convex Hull Trick (CHT)",
                "statement_summary": "Frog jumps from stone i to j with quadratic cost (h_j - h_i)^2 + C where heights are strictly increasing.",
                "key_idea": "Expand (h_j - h_i)^2 + C = h_j^2 + C + (h_i^2 + dp[i]) - 2 * h_j * h_i. For fixed j, this is min_i (m_i * x + b_i) with slope m_i = -2 * h_i and x = h_j.",
                "core_observation": "Since heights h_i are strictly increasing, slopes are strictly decreasing and query points are strictly increasing. A deque maintains the lower convex hull in O(1) amortized time per query.",
                "algorithm": "1. Deque stores lines.\n2. For stone j: pop front while line[0].eval(h_j) >= line[1].eval(h_j).\n3. dp[j] = deque.front().eval(h_j) + h_j^2 + C.\n4. Add new line (slope = -2*h_j, intercept = h_j^2 + dp[j]) to back, popping non-convex lines.",
                "complexity": "Time: O(N), Space: O(N).",
                "editorial": "Canonical Convex Hull Trick with monotonic slopes and queries.",
                "teaches": "Geometric line lower envelope maintenance, convex hull deque operations, and linearizing quadratic DP costs.",
                "reusable_pattern": "Monotonic Convex Hull Trick (CHT)."
            }
        ]
    },
    {
        "tag_folder": "dp",
        "tag_name": "Dynamic Programming (DP)",
        "file_name": "prefix_sum_dp.md",
        "topic_title": "Prefix Sum Optimized DP",
        "subtopic": "DP Optimizations",
        "overview": "Accelerating polynomial transitions over contiguous state ranges from O(K) to O(1) using prefix sum arrays.",
        "problems": [
            {
                "id": "dp_m",
                "title": "Candies",
                "contest_id": "dp",
                "rating": 1550,
                "role": "Prefix Sum State Acceleration",
                "statement_summary": "Distribute K candies among N children such that child i receives at most a_i candies.",
                "key_idea": "The naive transition dp[i][j] = sum_{k=0}^{a_i} dp[i-1][j-k] is over a contiguous range [j - a_i, j] in dp[i-1].",
                "core_observation": "Prefix sums of the previous row evaluate the contiguous range sum in O(1), dropping overall complexity from O(N * K^2) to O(N * K).",
                "algorithm": "1. dp[0] = 1, others 0.\n2. For each child i: compute prefix sums pref of current dp.\n3. dp[j] = (pref[j+1] - pref[max(0, j - a_i)]) mod MOD.\n4. Return dp[K].",
                "complexity": "Time: O(N * K), Space: O(K).",
                "editorial": "Prefix sum acceleration of contiguous state transitions.",
                "teaches": "Sliding window range sum optimization reducing quadratic transitions to linear.",
                "reusable_pattern": "Prefix sum acceleration of contiguous state transitions."
            }
        ]
    },
    {
        "tag_folder": "dp",
        "tag_name": "Dynamic Programming (DP)",
        "file_name": "1d_dp.md",
        "topic_title": "1D State Recurrences & State Machines",
        "subtopic": "Intro to DP",
        "overview": "Foundational linear dynamic programming, bounded lookaheads, and categorical state machines enforcing consecutive action constraints.",
        "problems": [
            {
                "id": "dp_a",
                "title": "Frog 1",
                "contest_id": "dp",
                "rating": 600,
                "role": "Linear 1D DP with 2-Step Lookahead",
                "statement_summary": "Minimum jump cost to reach stone N jumping 1 or 2 stones.",
                "key_idea": "dp[i] = min(dp[i-1] + |h_i - h_{i-1}|, dp[i-2] + |h_i - h_{i-2}|).",
                "core_observation": "Arrival at stone i is strictly partitioned between i-1 and i-2.",
                "algorithm": "1. dp[1]=0, dp[2]=|h_2-h_1|.\n2. Loop i from 3 to N.\n3. Return dp[N].",
                "complexity": "Time: O(N), Space: O(1) rolling state.",
                "editorial": "Standard 1D forward relaxation.",
                "teaches": "Optimal substructure, state initialization, and memory-compressed transitions.",
                "reusable_pattern": "Linear 1D DP with constant lookback window."
            },
            {
                "id": "dp_b",
                "title": "Frog 2",
                "contest_id": "dp",
                "rating": 700,
                "role": "1D DP with K-Step Lookahead",
                "statement_summary": "Minimum jump cost jumping up to K stones.",
                "key_idea": "Relax over sliding window of previous K states.",
                "core_observation": "dp[i] = min_{1 <= j <= K} (dp[i-j] + |h_i - h_{i-j}|).",
                "algorithm": "Push DP forward from i to i+step for step in 1..K.",
                "complexity": "Time: O(N * K), Space: O(N).",
                "editorial": "Parameterized push-style relaxation.",
                "teaches": "Parameterized transition loops and boundary-bounded relaxation.",
                "reusable_pattern": "Push DP over variable-sized transition intervals."
            },
            {
                "id": "dp_c",
                "title": "Vacation",
                "contest_id": "dp",
                "rating": 900,
                "role": "State-Machine Categorical DP",
                "statement_summary": "Maximize vacation happiness without repeating the same activity two days in a row.",
                "key_idea": "State: dp[day][act] where act in {A, B, C}.",
                "core_observation": "The last choice fully captures all history required by the constraint.",
                "algorithm": "dp[i][A] = a_i + max(dp[i-1][B], dp[i-1][C]), symmetrically for B, C.",
                "complexity": "Time: O(N), Space: O(1).",
                "editorial": "3-state Markov transition graph.",
                "teaches": "State augmentation for path-dependent constraints and state-machine DP.",
                "reusable_pattern": "Categorical state-machine DP with mutually exclusive transitions."
            }
        ]
    },

    # ==================== GRAPH THEORY ====================
    {
        "tag_folder": "graph_theory",
        "tag_name": "Graph Theory",
        "file_name": "connected_components_dsu.md",
        "topic_title": "Connected Components & DSU Transitive Closure",
        "subtopic": "Connected Components",
        "overview": "Exploiting equivalence relations and transitive connectivity on undirected graphs using Disjoint Set Union (DSU) to compute component invariants and clique completions.",
        "problems": [
            {
                "id": "abc350_d",
                "title": "New Friends",
                "contest_id": "abc350",
                "rating": 1050,
                "role": "Transitive Closure & Clique Completion via DSU",
                "statement_summary": "If A-B and B-C are friends, A and C can become friends. Count maximum possible new friendships.",
                "key_idea": "The operation creates the transitive closure of the graph. Each connected component of size S will eventually become a complete graph (clique) with S*(S-1)/2 edges.",
                "core_observation": "Edges can never form between disconnected components. Within any component of size S, all missing edges will eventually be added.",
                "algorithm": "1. Build DSU over all N vertices and M edges.\n2. For each component root, find vertex count S and existing edge count E.\n3. Total new edges = sum_{components} (S * (S - 1) / 2 - E).",
                "complexity": "Time: O(N + M * alpha(N)), Space: O(N).",
                "editorial": "Transitive closure clique completion via DSU.",
                "teaches": "Transitive relations on graphs and component-wise clique maximization.",
                "reusable_pattern": "DSU component aggregation and clique edge counting."
            }
        ]
    },
    {
        "tag_folder": "graph_theory",
        "tag_name": "Graph Theory",
        "file_name": "tree_diameter.md",
        "topic_title": "Tree Diameter via Double BFS/DFS",
        "subtopic": "Trees",
        "overview": "Finding the longest simple path in an unweighted or weighted tree using two consecutive breadth-first or depth-first searches.",
        "problems": [
            {
                "id": "typical90_c",
                "title": "Longest Circular Road",
                "contest_id": "typical90",
                "rating": 1100,
                "role": "Canonical 2-Pass Tree Diameter",
                "statement_summary": "Add one edge between any two vertices in a tree to form the longest possible simple cycle.",
                "key_idea": "Adding edge (u, v) creates a cycle of length dist(u, v) + 1. The maximum distance between any two vertices in a tree is by definition the diameter of the tree.",
                "core_observation": "Running BFS from any arbitrary node 1 finds a node u on the diameter. Running a second BFS from u finds the opposite end v of the diameter.",
                "algorithm": "1. Run BFS from node 1 to find farthest node u.\n2. Run BFS from u to find farthest node v. dist(u, v) is the tree diameter.\n3. Output dist(u, v) + 1.",
                "complexity": "Time: O(N), Space: O(N).",
                "editorial": "Two-pass BFS tree diameter proof.",
                "teaches": "Tree diameter characterization and the canonical 2-BFS algorithm.",
                "reusable_pattern": "2-pass BFS tree diameter."
            }
        ]
    },
    {
        "tag_folder": "graph_theory",
        "tag_name": "Graph Theory",
        "file_name": "shortest_paths_dijkstra.md",
        "topic_title": "Two-Way Bidirectional Dijkstra",
        "subtopic": "Shortest Paths",
        "overview": "Decomposing intermediate node constraints along paths into independent single-source shortest path passes from source and target endpoints.",
        "problems": [
            {
                "id": "typical90_m",
                "title": "Passing",
                "contest_id": "typical90",
                "rating": 1350,
                "role": "Dual-Source Dijkstra Intermediate Distance Queries",
                "statement_summary": "For every vertex k from 1 to N, find the shortest path from vertex 1 to vertex N passing through k.",
                "key_idea": "Shortest path from 1 to N passing through k is dist(1, k) + dist(k, N). Since edges are undirected, dist(k, N) = dist(N, k).",
                "core_observation": "Running Dijkstra only twice (from vertex 1 and from vertex N) precomputes dist1 and distN, allowing O(1) query response for all k.",
                "algorithm": "1. Run Dijkstra from node 1 -> dist1 array.\n2. Run Dijkstra from node N -> distN array.\n3. For each k in 1..N: output dist1[k] + distN[k].",
                "complexity": "Time: O(M log N), Space: O(N + M).",
                "editorial": "Two-source bidirectional Dijkstra.",
                "teaches": "Decomposing multi-point shortest path queries into two independent single-source runs.",
                "reusable_pattern": "Dual Dijkstra intermediate point distance query."
            }
        ]
    },
    {
        "tag_folder": "graph_theory",
        "tag_name": "Graph Theory",
        "file_name": "topological_sort_cycles.md",
        "topic_title": "Directed Graph Cycle Detection & Topological Sort",
        "subtopic": "Directed Graphs",
        "overview": "Modeling dependency relations and handle transitions as directed graphs and detecting cycles via Kahn's algorithm or 3-color DFS.",
        "problems": [
            {
                "id": "abc285_d",
                "title": "Change of User Name",
                "contest_id": "abc285",
                "rating": 950,
                "role": "Dependency Resolution via Cycle Detection",
                "statement_summary": "N users want to change their handles from S_i to T_i. Determine if all changes can be performed without collisions.",
                "key_idea": "Build directed graph with edge S_i -> T_i. A valid order of renames exists if and only if the directed graph contains NO directed cycle.",
                "core_observation": "A directed cycle forms a deadlock where no user in the cycle can change without overwriting another user's existing handle.",
                "algorithm": "1. Build adjacency list of directed edges S_i -> T_i.\n2. Compute in-degrees and perform Kahn's Topological Sort.\n3. If all nodes can be topologically sorted, output 'Yes'; else 'No'.",
                "complexity": "Time: O(N), Space: O(N).",
                "editorial": "Topological sort cycle check on string handle transitions.",
                "teaches": "Modeling sequential dependencies as directed graph cycles and topological ordering.",
                "reusable_pattern": "Topological sort cycle detection for dependency resolution."
            }
        ]
    },

    # ==================== DATA STRUCTURES ====================
    {
        "tag_folder": "data_structures",
        "tag_name": "Data Structures (DS)",
        "file_name": "online_grid_dsu.md",
        "topic_title": "Online Grid Connectivity & 2D Linearization DSU",
        "subtopic": "Disjoint Set Union (DSU)",
        "overview": "Transforming 2D spatial coordinate grids into 1D arrays and maintaining dynamic component connectivity using Disjoint Set Union.",
        "problems": [
            {
                "id": "typical90_l",
                "title": "Red Painting",
                "contest_id": "typical90",
                "rating": 1250,
                "role": "2D Grid Coordinate Linearization with Dynamic DSU",
                "statement_summary": "Dynamically color grid cells red and answer reachability queries between red cells.",
                "key_idea": "Map (r, c) -> r * W + c. When a cell becomes red, unite it with adjacent red neighbors. Reachability is DSU root equality.",
                "core_observation": "DSU handles incremental edge additions in almost constant amortized time O(alpha(V)), eliminating the need to rerun BFS/DFS per query.",
                "algorithm": "1. Map (r, c) -> r * W + c. Initialize DSU and boolean is_red grid.\n2. On color query: set is_red[r][c] = True; for each neighbor (nr, nc) that is red: dsu.unite(idx(r,c), idx(nr,nc)).\n3. On reachability query: if is_red[a] and is_red[b] and dsu.same(idx_a, idx_b) -> 'Yes', else 'No'.",
                "complexity": "Time: O(Q * alpha(H * W)), Space: O(H * W).",
                "editorial": "Online dynamic connectivity on 2D grid via DSU.",
                "teaches": "2D-to-1D coordinate flattening and online component maintenance without BFS/DFS reruns.",
                "reusable_pattern": "Grid coordinate linearization + online DSU."
            }
        ]
    },
    {
        "tag_folder": "data_structures",
        "tag_name": "Data Structures (DS)",
        "file_name": "fenwick_segment_tree.md",
        "topic_title": "Fenwick Tree & Segment Tree Range Queries",
        "subtopic": "Segment Tree / Fenwick Tree",
        "overview": "Maintaining dynamic arrays subject to point updates and range queries in O(log N) time over monoids like XOR and maximum.",
        "problems": [
            {
                "id": "abc185_f",
                "title": "Range Xor Query",
                "contest_id": "abc185",
                "rating": 1150,
                "role": "Point Update Range XOR with Fenwick Tree",
                "statement_summary": "Support point XOR update A[X] ^= Y and range XOR query A[L] ^ ... ^ A[R].",
                "key_idea": "XOR is associative, commutative, and self-inverting. A Fenwick tree natively maintains prefix XORs in O(log N).",
                "core_observation": "Range XOR [L, R] = prefix_xor(R) ^ prefix_xor(L - 1).",
                "algorithm": "1. Build Fenwick tree with XOR combine operation.\n2. Update query: fenwick.update(X, Y).\n3. Range query: output fenwick.query(R) ^ fenwick.query(L - 1).",
                "complexity": "Time: O(Q log N), Space: O(N).",
                "editorial": "Fenwick tree XOR adaptation.",
                "teaches": "Applying Fenwick tree to any invertible commutative monoid (such as XOR).",
                "reusable_pattern": "Fenwick Tree point-update range-query."
            },
            {
                "id": "dp_q",
                "title": "Flowers",
                "contest_id": "dp",
                "rating": 1600,
                "role": "Fenwick Tree Accelerated LIS",
                "statement_summary": "Find strictly increasing subsequence of heights maximizing beauty.",
                "key_idea": "dp[h_i] = a_i + max_{0 <= h < h_i} dp[h]. Querying prefix maximum and point updating is solved by Fenwick/Segment Tree in O(log N).",
                "core_observation": "Transforming quadratic inner-loop search into dynamic range queries via data structures.",
                "algorithm": "1. Maintain Fenwick tree supporting point-update and prefix-max queries.\n2. For each flower i: best = fenwick.query(h_i - 1); fenwick.update(h_i, best + a_i).\n3. Return fenwick.query(N).",
                "complexity": "Time: O(N log N), Space: O(N).",
                "editorial": "Fenwick tree / Segment tree accelerated LIS.",
                "teaches": "Transforming quadratic inner-loop search into dynamic range queries via data structures.",
                "reusable_pattern": "BIT/Segment Tree accelerated DP."
            }
        ]
    },
    {
        "tag_folder": "data_structures",
        "tag_name": "Data Structures (DS)",
        "file_name": "priority_queue_buffers.md",
        "topic_title": "Amortized Hybrid Buffers (Queue + Priority Queue)",
        "subtopic": "Queue & Priority Queue",
        "overview": "Splitting collections into sorted and unsorted segments to achieve optimal amortized complexity across dynamic sorting and popping operations.",
        "problems": [
            {
                "id": "abc217_e",
                "title": "Sorting Queries",
                "contest_id": "abc217",
                "rating": 1200,
                "role": "Two-Stage Buffer (Queue + Min-Heap)",
                "statement_summary": "Support: append x, print and pop first element, and sort the entire array.",
                "key_idea": "Sorting repeatedly is too slow. Split storage: a min-heap holds sorted elements, and a FIFO queue holds newly appended unsorted elements.",
                "core_observation": "Sorted elements always precede newly appended unsorted elements. On sort query, transfer all FIFO queue elements into min-heap. Each element enters min-heap at most once!",
                "algorithm": "1. On append x: push to FIFO queue.\n2. On sort: move all elements from FIFO queue to min-heap.\n3. On pop: if min-heap is non-empty, pop min-heap; else pop FIFO queue.",
                "complexity": "Time: O(Q log Q) amortized, Space: O(Q).",
                "editorial": "Two-buffer amortized queue + priority queue split.",
                "teaches": "Amortized complexity and separating sorted vs unsorted segments using complementary data structures.",
                "reusable_pattern": "Hybrid Queue + Min-Heap amortized sorting."
            }
        ]
    },

    # ==================== BASICS & SEARCH ====================
    {
        "tag_folder": "basics",
        "tag_name": "Basics",
        "file_name": "binary_search_on_answer.md",
        "topic_title": "Binary Search on Answer / Greedy Feasibility",
        "subtopic": "Binary Search",
        "overview": "Transforming optimization problems ('maximize the minimum' or 'minimize the maximum') into monotonic decision problems solved by binary search.",
        "problems": [
            {
                "id": "typical90_a",
                "title": "Yokan Party",
                "contest_id": "typical90",
                "rating": 1200,
                "role": "The Canonical Maximize the Minimum Template",
                "statement_summary": "Cut a stick of length L at K positions to maximize the length of the shortest piece.",
                "key_idea": "Binary search on the minimum piece length M in range [1, L].",
                "core_observation": "The predicate 'Can we obtain at least K+1 pieces each of length >= M?' is monotonically decreasing with respect to M. Feasibility is verified greedily in O(N).",
                "algorithm": "1. Binary search M in [1, L].\n2. check(M): Greedily cut whenever current piece length >= M. If total pieces cut is >= K and remaining piece >= M, return True; else False.\n3. Upper boundary is the optimal answer.",
                "complexity": "Time: O(N log L), Space: O(1).",
                "editorial": "Textbook binary search on answer.",
                "teaches": "Formulating feasibility predicates, establishing monotonicity, and greedy cut verification.",
                "reusable_pattern": "Binary search on answer + greedy feasibility check."
            }
        ]
    },
    {
        "tag_folder": "basics",
        "tag_name": "Basics",
        "file_name": "dual_index_mapping.md",
        "topic_title": "Dual Index Mapping (Position <-> Value)",
        "subtopic": "Implementation / Simulation",
        "overview": "Maintaining bidirectional bijections between permutation values and their array indices to perform dynamic position lookups and swaps in O(1) time.",
        "problems": [
            {
                "id": "abc250_c",
                "title": "Adjacent Swaps",
                "contest_id": "abc250",
                "rating": 800,
                "role": "Bidirectional Permutation Bijection",
                "statement_summary": "Perform Q swaps where each query swaps ball with number x and its adjacent neighbor.",
                "key_idea": "Maintain two arrays: pos[x] = position of ball x, and val[p] = ball at position p.",
                "core_observation": "Locating ball x in an array naively takes O(N). Dual arrays allow O(1) lookup and O(1) swap update.",
                "algorithm": "1. Maintain pos[x] and val[p].\n2. For query x: p = pos[x]. Determine target p2 = (p < N ? p + 1 : p - 1). Let y = val[p2].\n3. Swap: val[p]=y, val[p2]=x. Update pos: pos[x]=p2, pos[y]=p.",
                "complexity": "Time: O(Q), Space: O(N).",
                "editorial": "Dual array bijection maintenance.",
                "teaches": "O(1) bidirectional lookup mapping and maintaining invertible permutations under swap operations.",
                "reusable_pattern": "Dual index mapping (Position <-> Value)."
            }
        ]
    },

    # ==================== GAME THEORY ====================
    {
        "tag_folder": "game_theory",
        "tag_name": "Game Theory",
        "file_name": "sprague_grundy_impartial_games.md",
        "topic_title": "Sprague-Grundy & Impartial Game Induction",
        "subtopic": "Impartial Games",
        "overview": "Finite impartial sequential games, normal play convention, P-positions (previous player winning) and N-positions (next player winning).",
        "problems": [
            {
                "id": "dp_k",
                "title": "Stones",
                "contest_id": "dp",
                "rating": 1100,
                "role": "Finite Game Backward Induction",
                "statement_summary": "Two players remove a_i stones from a pile of size K. Determine if First or Second player wins under optimal play.",
                "key_idea": "State x is Winning (First wins) if there exists a valid move a_i such that state x - a_i is Losing (Second wins). If all valid moves lead to Winning states, x is Losing.",
                "core_observation": "Game state graph is finite and directed acyclic. Backward induction computes boolean outcomes in O(N * K).",
                "algorithm": "1. dp[0] = False (Losing state).\n2. For x from 1 to K: dp[x] = True if any(a_i <= x and not dp[x - a_i] for a_i in A) else False.\n3. Output 'First' if dp[K] else 'Second'.",
                "complexity": "Time: O(N * K), Space: O(K).",
                "editorial": "Classic backward induction on impartial game graph.",
                "teaches": "P-positions and N-positions, finite state game backward induction, and Sprague-Grundy fundamentals.",
                "reusable_pattern": "Boolean game state induction: win(x) = \exists a, \neg win(x - a)."
            }
        ]
    },

    # ==================== NUMBER THEORY ====================
    {
        "tag_folder": "number_theory",
        "tag_name": "Number Theory",
        "file_name": "modular_linear_congruence.md",
        "topic_title": "Modular Linear Congruences & Extended GCD",
        "subtopic": "Modular Arithmetic",
        "overview": "Solving linear congruences ax = b (mod m) and computing modular inverses via the Extended Euclidean Algorithm.",
        "problems": [
            {
                "id": "abc186_e",
                "title": "Throne",
                "contest_id": "abc186",
                "rating": 1250,
                "role": "Extended Euclidean Algorithm for Linear Congruence",
                "statement_summary": "Move K steps clockwise on a circle of size N, starting at position S. Find minimum steps to reach 0.",
                "key_idea": "S + x * K = 0 (mod N) => K * x = -S (mod N). Solutions exist if and only if gcd(K, N) divides S.",
                "core_observation": "Dividing through by g = gcd(K, N) yields K' * x = -S' (mod N') where gcd(K', N') = 1. The modular inverse of K' mod N' gives the unique solution.",
                "algorithm": "1. g = gcd(K, N). If S % g != 0 return -1.\n2. K' = K/g, S' = S/g, N' = N/g.\n3. Find inv = mod_inv(K', N') via Extended GCD.\n4. Output (-S' * inv) mod N'.",
                "complexity": "Time: O(log(min(K, N))), Space: O(1).",
                "editorial": "Extended Euclidean Algorithm for modular inverse.",
                "teaches": "Modular linear congruences, solvability condition via GCD divisibility, and Extended Euclidean Algorithm.",
                "reusable_pattern": "Extended Euclidean linear congruence solver."
            }
        ]
    },
    {
        "tag_folder": "number_theory",
        "tag_name": "Number Theory",
        "file_name": "cubic_root_prime_factorization.md",
        "topic_title": "Cubic-Root Prime Factorization (N = p^2 * q)",
        "subtopic": "Prime Numbers",
        "overview": "Exploiting asymmetric algebraic power distributions in prime factorizations to bound search boundaries to O(N^(1/3)).",
        "problems": [
            {
                "id": "abc284_d",
                "title": "Happy New Year 2023",
                "contest_id": "abc284",
                "rating": 1050,
                "role": "O(N^(1/3)) Asymmetric Prime Search",
                "statement_summary": "Given N = p^2 * q where p and q are prime and N <= 9 * 10^18, find primes p and q.",
                "key_idea": "Because N = p^2 * q, at least one of p or q must be <= N^(1/3) <= 2.15 * 10^6.",
                "core_observation": "Testing trial divisors up to N^(1/3) is guaranteed to find either p or q in a few million operations.",
                "algorithm": "1. Loop d from 2 up to 3 * 10^6:\n   If N % d == 0: if N % (d * d) == 0 -> p = d, q = N / (d * d); else p = isqrt(N / d), q = d; break.\n2. Output p and q.",
                "complexity": "Time: O(N^(1/3)), Space: O(1).",
                "editorial": "Cubic root trial division for asymmetric prime powers.",
                "teaches": "Exploiting asymmetric algebraic power structures to bound search space to N^(1/3) rather than sqrt(N).",
                "reusable_pattern": "N^(1/3) trial division for p^2 * q factorization."
            }
        ]
    },

    # ==================== STRINGS ====================
    {
        "tag_folder": "strings",
        "tag_name": "Strings",
        "file_name": "lexicographically_smallest_subsequence.md",
        "topic_title": "Next-Occurrence Array & Lexicographical Subsequences",
        "subtopic": "Greedy on Strings",
        "overview": "Precomputing next-character occurrence lookup tables to greedily construct optimal subsequences.",
        "problems": [
            {
                "id": "typical90_f",
                "title": "Smallest Subsequence",
                "contest_id": "typical90",
                "rating": 1500,
                "role": "Next-Occurrence Table Subsequence Construction",
                "statement_summary": "Find the lexicographically smallest subsequence of length K from string S of length N.",
                "key_idea": "Greedily choose the smallest possible character ('a' through 'z') at each step that leaves enough remaining characters to complete length K.",
                "core_observation": "Precomputing next_pos[i][c] (earliest index >= i of character c) allows O(26) decision per position.",
                "algorithm": "1. Precompute next_pos[i][c] in O(26 * N).\n2. cur = 0.\n3. For step from 1 to K: for char c in 'a'..'z': pos = next_pos[cur][c]; if N - pos >= K - step: append c, cur = pos + 1, break.\n4. Output string.",
                "complexity": "Time: O(26 * N + 26 * K), Space: O(26 * N).",
                "editorial": "Next-character transition table with greedy lookahead.",
                "teaches": "Precomputing next-occurrence transition tables on strings and greedy lexicographical construction.",
                "reusable_pattern": "Next-occurrence array for subsequence queries."
            }
        ]
    }
]


def build_hierarchical_markdowns():
    """Generates all topic-level markdown files inside tag folders."""
    # Group by tag_folder
    tag_groups = defaultdict(list)
    for topic_data in TOPIC_MARKDOWNS:
        tag_groups[topic_data["tag_folder"]].append(topic_data)

    for tag_folder, topics_list in tag_groups.items():
        folder_path = os.path.join(CATEGORIES_DIR, tag_folder)
        os.makedirs(folder_path, exist_ok=True)
        tag_name = topics_list[0]["tag_name"]

        # 1. Create each topic markdown file
        for topic_data in topics_list:
            file_path = os.path.join(folder_path, topic_data["file_name"])
            lines = [
                f"# 📖 {topic_data['topic_title']}",
                "",
                f"- **Tag / Domain**: `{topic_data['tag_name']}`",
                f"- **Subtopic**: `{topic_data['subtopic']}`",
                f"- **Total Curated Problems**: {len(topic_data['problems'])}",
                "",
                "---",
                "",
                "## 💡 Topic Overview",
                topic_data["overview"],
                "",
                "---",
                "",
                "## 🏆 Curated High-Value Problems",
                ""
            ]

            for idx, p in enumerate(topic_data["problems"], 1):
                vjudge = f"`[problem:AtCoder-{p['id']}]`"
                task_url = f"https://atcoder.jp/contests/{p['contest_id']}/tasks/{p['id']}"
                analysis_link = f"../../analysis/AtCoder-{p['id']}.md"

                lines.extend([
                    f"### {idx}. {p['title']} ({vjudge})",
                    "",
                    f"- **Role**: *{p['role']}*",
                    f"- **Rating**: `{p['rating']}` | **Contest**: [`{p['contest_id']}`]({task_url})",
                    f"- **Full Analysis**: [AtCoder-{p['id']} Analysis]({analysis_link})",
                    "",
                    "#### Problem Statement & Task",
                    p["statement_summary"],
                    "",
                    "#### Core Invariant & Observation",
                    p["core_observation"],
                    "",
                    "#### Algorithmic Formulation",
                    p["algorithm"],
                    "",
                    f"**Complexity**: `{p['complexity']}`  ",
                    f"**Editorial Alignment**: {p['editorial']}  ",
                    "",
                    "#### What This Teaches & Reusable Pattern",
                    f"- **Skill Taught**: {p['teaches']}",
                    f"- **Reusable Pattern**: `{p['reusable_pattern']}`",
                    "",
                    "---",
                    ""
                ])

            lines.extend([
                f"[Back to {tag_name} Index](README.md) | [Back to Master Categories](../../README.md)",
                ""
            ])

            with open(file_path, "w", encoding="utf-8") as f:
                f.write("\n".join(lines))
            print(f"[+] Created Topic Markdown: {file_path}")

        # 2. Create tag folder README.md
        tag_readme_path = os.path.join(folder_path, "README.md")
        t_lines = [
            f"# {tag_name} Category Index",
            "",
            f"Curated collection of high-value problems in **{tag_name}** partitioned into modular, skill-specific topic Markdown files.",
            "",
            "## 📂 Topic Markdown Files",
            "",
            "| Topic File | Subtopic | Topic / Skill | Problems Count | Key Reusable Pattern |",
            "|---|---|---|---|---|"
        ]

        for topic_data in topics_list:
            fn = topic_data["file_name"]
            title = topic_data["topic_title"]
            sub = topic_data["subtopic"]
            cnt = len(topic_data["problems"])
            pattern = topic_data["problems"][0]["reusable_pattern"]
            t_lines.append(f"| [`{fn}`]({fn}) | {sub} | **{title}** | {cnt} | `{pattern}` |")

        t_lines.extend([
            "",
            "---",
            "",
            "[Back to Categories Directory](../README.md) | [Back to Main Repository](../../README.md)",
            ""
        ])

        with open(tag_readme_path, "w", encoding="utf-8") as f:
            f.write("\n".join(t_lines))
        print(f"[+] Created Tag README: {tag_readme_path}")


def update_master_categories_index():
    """Updates categories/README.md with links to all hierarchical folders and topic files."""
    index_path = os.path.join(CATEGORIES_DIR, "README.md")
    lines = [
        "# 📚 AtCoder Problem Categories Directory",
        "",
        "This directory organizes curated AtCoder problems into dedicated domain folders and skill-specific `.md` files.",
        "All problems inside these files teach **reusable competitive programming techniques and algorithms**, completely filtering out trivial logic-building and syntax simulations.",
        "",
        "---",
        "",
        "## 📁 Category Folders & Topic Markdown Files",
        "",
        "| Tag / Domain | Directory | Topic `.md` Files | Total Curated Problems |",
        "|---|---|---|---|"
    ]

    tag_meta = [
        ("Dynamic Programming (DP)", "dp", [
            ("1D DP & State Machines", "1d_dp.md"),
            ("Knapsack & Dual State", "knapsack.md"),
            ("Interval & Range DP", "interval_dp.md"),
            ("Prefix Sum Accelerated DP", "prefix_sum_dp.md"),
            ("Bitmask DP & Submask Enumeration", "bitmask_dp.md"),
            ("DP on Trees & DAGs", "dp_on_trees.md"),
            ("Digit DP", "digit_dp.md"),
            ("Convex Hull Trick (CHT)", "convex_hull_trick.md")
        ]),
        ("Graph Theory", "graph_theory", [
            ("Connected Components & DSU", "connected_components_dsu.md"),
            ("Tree Diameter (2-BFS)", "tree_diameter.md"),
            ("Bidirectional Dijkstra", "shortest_paths_dijkstra.md"),
            ("Topological Sort Cycle Detection", "topological_sort_cycles.md")
        ]),
        ("Data Structures (DS)", "data_structures", [
            ("Online Grid DSU", "online_grid_dsu.md"),
            ("Fenwick / Segment Tree", "fenwick_segment_tree.md"),
            ("Hybrid Priority Queue Buffers", "priority_queue_buffers.md")
        ]),
        ("Basics & Search", "basics", [
            ("Binary Search on Answer", "binary_search_on_answer.md"),
            ("Dual Index Permutation Mapping", "dual_index_mapping.md")
        ]),
        ("Game Theory", "game_theory", [
            ("Sprague-Grundy Impartial Games", "sprague_grundy_impartial_games.md")
        ]),
        ("Number Theory", "number_theory", [
            ("Modular Linear Congruence (ExtGCD)", "modular_linear_congruence.md"),
            ("Cubic-Root Prime Factorization", "cubic_root_prime_factorization.md")
        ]),
        ("Strings", "strings", [
            ("Next-Occurrence Lexicographical Subsequences", "lexicographically_smallest_subsequence.md")
        ])
    ]

    for tag_name, folder, files in tag_meta:
        total_p = 0
        topic_links = []
        for title, fn in files:
            topic_links.append(f"[`{fn}`]({folder}/{fn})")
            # find problem count
            for t in TOPIC_MARKDOWNS:
                if t["tag_folder"] == folder and t["file_name"] == fn:
                    total_p += len(t["problems"])

        files_formatted = "<br>".join(topic_links)
        lines.append(f"| **{tag_name}** | [`{folder}/`]({folder}/) | {files_formatted} | {total_p} |")

    lines.extend([
        "",
        "---",
        "",
        "## 🔬 Problem Evaluation Methodology",
        "Every problem categorized across these `.md` files is evaluated under the strict 6-step protocol:",
        "1. **Read**: Statement, limits, types, and constraints.",
        "2. **Analyze**: Identify hidden mathematical observations, monotonicity, subproblem independence.",
        "3. **Solve**: Formulate an optimal algorithm with proven time and space complexity.",
        "4. **Identify Tag & Topics**: Map to the standard 3-tier taxonomy.",
        "5. **Read Editorial**: Verify against official and community approaches.",
        "6. **Finalize**: Archive in dedicated topic `.md` file, update selection log, and provide individual analysis.",
        "",
        "[Back to Main Repository](../../README.md)"
    ])

    with open(index_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"[+] Updated Categories Master Index: {index_path}")


if __name__ == "__main__":
    print("=" * 70)
    print("      BUILDING HIERARCHICAL TOPIC MARKDOWN ECOSYSTEM")
    print("=" * 70)
    build_hierarchical_markdowns()
    update_master_categories_index()
    print("=" * 70)
    print("Hierarchical topic markdowns generated successfully!")
