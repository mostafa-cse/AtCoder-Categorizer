import sys
sys.stdout.reconfigure(encoding='utf-8')
import json

with open('scratch/part3f1_scraped_tasks.json', 'r', encoding='utf-8') as f:
    scraped = json.load(f)

# Read the C++ solutions we already verified
with open('scratch/sol_abc227_e.cpp', 'r', encoding='utf-8') as f: cpp_227 = f.read()
with open('scratch/sol_abc373_g.cpp', 'r', encoding='utf-8') as f: cpp_373 = f.read()
with open('scratch/sol_arc171_d.cpp', 'r', encoding='utf-8') as f: cpp_171 = f.read()
with open('scratch/sol_arc188_c.cpp', 'r', encoding='utf-8') as f: cpp_188 = f.read()
with open('scratch/sol_agc039_c.cpp', 'r', encoding='utf-8') as f: cpp_039 = f.read()
with open('scratch/sol_abc303_f.cpp', 'r', encoding='utf-8') as f: cpp_303 = f.read()
with open('scratch/sol_arc152_d.cpp', 'r', encoding='utf-8') as f: cpp_152 = f.read()
with open('scratch/sol_donuts_2015_4.cpp', 'r', encoding='utf-8') as f: cpp_donuts = f.read()
with open('scratch/sol_dwango2016qual_c.cpp', 'r', encoding='utf-8') as f: cpp_dwango = f.read()
with open('scratch/sol_abc337_f.cpp', 'r', encoding='utf-8') as f: cpp_337 = f.read()
with open('scratch/sol_abc479_g.cpp', 'r', encoding='utf-8') as f: cpp_479 = f.read()
with open('scratch/sol_abc135_f.cpp', 'r', encoding='utf-8') as f: cpp_135 = f.read()
with open('scratch/sol_abc325_g.cpp', 'r', encoding='utf-8') as f: cpp_325 = f.read()

problems = [
    {
        "id": "abc227_e",
        "contest_id": "abc227",
        "title": "E. Swap",
        "rating": 2377,
        "domain": "Dynamic Programming (DP)",
        "subtopic": "Intro to DP",
        "topic": "Knapsack and Basic Dynamic Programming",
        "category_file": "categories/dynamic_programming/multinomial_inversion_adjacent_swaps_dp.md",
        "slug": "multinomial_inversion_adjacent_swaps_dp",
        "core_tags": [
            "Dynamic Programming (DP)",
            "Intro to DP",
            "Knapsack and Basic Dynamic Programming",
            "Permutations",
            "Counting Inversions",
            "String DP"
        ],
        "invariant": "Every distinct string T reachable from S corresponds uniquely to a permutation preserving identical characters' relative order. The minimum number of adjacent swaps to reach T is precisely the inversion count of this canonical permutation. State dp[cK][cE][cY][inv] tracks the number of prefixes with exact inversion count, transitioning by placing the next character and counting unplaced preceding characters.",
        "editorial_reduction": "Count frequencies of 'K', 'E', 'Y' in S (|S| <= 30) and record their 0-indexed positions.\nInitialize dp[0][0][0][0] = 1 with inv <= N(N-1)/2 <= 435.\nFor each state (i, j, k, inv), consider placing the next available character ('K', 'E', or 'Y'). The swap cost incurred is the number of already-placed characters of the other two types that originally appeared after it in S.\nAccumulate dp transitions and sum dp[nK][nE][nY][inv] for all inv <= min(K, 435).",
        "time_complexity": "O(|S|^5)",
        "space_complexity": "O(|S|^4)",
        "samples": scraped['abc227_e']['samples'],
        "cpp_solution": cpp_227
    },
    {
        "id": "abc373_g",
        "contest_id": "abc373",
        "title": "G. No Cross Matching",
        "rating": 2377,
        "domain": "Graph Theory",
        "subtopic": "Flow and Min Cut",
        "topic": "Min Cost Max Flow (MCMF)",
        "category_file": "categories/graph_theory/euclidean_minimum_matching_no_cross.md",
        "slug": "euclidean_minimum_matching_no_cross",
        "core_tags": [
            "Graph Theory",
            "Flow and Min Cut",
            "Min Cost Max Flow (MCMF)",
            "Hungarian Algorithm",
            "Bipartite Matching",
            "Computational Geometry"
        ],
        "invariant": "In any bipartite matching of N points to N points where no three points are collinear, if any two segments cross at an intersection point X, the triangle inequality guarantees that uncrossing their endpoints strictly decreases the total Euclidean length. Therefore, the minimum Euclidean distance matching cannot contain any crossing segments.",
        "editorial_reduction": "Construct an N x N cost matrix where cost[i][j] is the Euclidean distance hypot(A_i - C_j, B_i - D_j).\nRun the Hungarian algorithm in O(N^3) time to find the minimum-weight perfect bipartite matching.\nExtract the assigned permutation R[p[j]] = j and output the 1-based indices.",
        "time_complexity": "O(N^3)",
        "space_complexity": "O(N^2)",
        "samples": scraped['abc373_g']['samples'],
        "cpp_solution": cpp_373
    },
    {
        "id": "arc171_d",
        "contest_id": "arc171",
        "title": "D. Rolling Hash",
        "rating": 2377,
        "domain": "Graph Theory",
        "subtopic": "Graph Coloring",
        "topic": "Chromatic Number",
        "category_file": "categories/graph_theory/rolling_hash_difference_graph_chromatic_number.md",
        "slug": "rolling_hash_difference_graph_chromatic_number",
        "core_tags": [
            "Graph Theory",
            "Graph Coloring",
            "Chromatic Number",
            "Rolling Hash",
            "Fast Zeta Transform",
            "Inclusion-Exclusion"
        ],
        "invariant": "The rolling hash condition hash(A[L..R]) != 0 mod P is equivalent to (H_R - H_{L-1} B^{R-L+1}) != 0 mod P. Multiplying by B^{-R} yields y_R != y_{L-1} mod P where y_k = H_k B^{-k} mod P. Since any prefix hash assignment is achievable, the problem is equivalent to proper vertex coloring of the difference graph on N+1 vertices with at most P colors.",
        "editorial_reduction": "Number vertices 0 .. N (V = N + 1 <= 17). If P >= V, output Yes immediately.\nOtherwise, add an undirected edge between L_i - 1 and R_i for each pair.\nPrecompute whether each subset of vertices forms an independent set in O(2^V) time.\nCompute the number of independent subsets f(S) for each mask S using the Fast Zeta Transform (SOS DP) in O(V 2^V) time.\nEvaluate the chromatic polynomial sum_{S} (-1)^{V - |S|} (f(S))^P modulo two large 30-bit primes to verify that the number of proper P-colorings is strictly positive.",
        "time_complexity": "O(N 2^N)",
        "space_complexity": "O(2^N)",
        "samples": scraped['arc171_d']['samples'],
        "cpp_solution": cpp_171
    },
    {
        "id": "arc188_c",
        "contest_id": "arc188",
        "title": "C. Honest or Liar or Confused",
        "rating": 2377,
        "domain": "Graph Theory",
        "subtopic": "Satisfiability",
        "topic": "2 SAT",
        "category_file": "categories/graph_theory/villager_testimony_parity_consistency_2sat.md",
        "slug": "villager_testimony_parity_consistency_2sat",
        "core_tags": [
            "Graph Theory",
            "Satisfiability",
            "2 SAT",
            "DFS Traversal",
            "Bipartite Coloring",
            "Linear Equivalence"
        ],
        "invariant": "A statement by villager A about B being C is valid iff (H_A ^ D_A) = (H_B ^ C) <=> H_A ^ H_B = D_A ^ C. Because D_A only affects statements made by A, all outgoing targets B_j of A must satisfy H_{B_1} ^ H_{B_j} = C(A -> B_1) ^ C(A -> B_j). Once a consistent 2-coloring on H is found, D_A = H_A ^ H_{B_1} ^ C(A -> B_1) always satisfies all constraints.",
        "editorial_reduction": "For each villager u, connect its first outgoing neighbor v_0 to every other outgoing neighbor v_j with edge weight c_0 ^ c_j.\nCheck if the resulting graph is 2-colorable under the edge parity constraints using BFS/DFS. If any odd-parity cycle is found, output -1.\nOtherwise, assign H according to the 2-coloring, and for each villager u, compute D_u = H_u ^ H_v ^ c for its outgoing edge (or 0 if u made no statements).\nOutput the binary string D.",
        "time_complexity": "O(N + M)",
        "space_complexity": "O(N + M)",
        "samples": scraped['arc188_c']['samples'],
        "cpp_solution": cpp_188
    },
    {
        "id": "agc039_c",
        "contest_id": "agc039",
        "title": "C. Division by Two with Something",
        "rating": 2379,
        "domain": "Combinatorics",
        "subtopic": "Inclusion Exclusion",
        "topic": "Principle of Inclusion and Exclusion (PIE)",
        "category_file": "categories/combinatorics/negated_cyclic_shift_mobius_periods.md",
        "slug": "negated_cyclic_shift_mobius_periods",
        "core_tags": [
            "Combinatorics",
            "Inclusion Exclusion",
            "Principle of Inclusion and Exclusion (PIE)",
            "Mobius Inversion",
            "Bitwise Operations",
            "String Periods"
        ],
        "invariant": "The operation shifts bits right with the new MSB equal to 1 - LSB, which is a negated cyclic shift of string S. A sequence has return period 2d dividing 2N iff N/d is odd and S satisfies S[i+d] = 1 - S[i] for all i. The sequence is completely determined by its prefix of length d.",
        "editorial_reduction": "Find all divisors d of N such that N/d is odd.\nFor each divisor d, the number of valid sequences <= X is the binary value of X[0..d-1] plus 1 if the periodically generated string <= X.\nApply inclusion-exclusion over odd quotients: f[d] = C[d] - sum_{d' | d, d/d' odd, d' < d} f[d'].\nMultiply each count by its return period 2d and sum modulo 998244353.",
        "time_complexity": "O(N d(N))",
        "space_complexity": "O(N)",
        "samples": scraped['agc039_c']['samples'],
        "cpp_solution": cpp_039
    },
    {
        "id": "abc303_f",
        "contest_id": "abc303",
        "title": "F. Damage over Time",
        "rating": 2381,
        "domain": "Basics",
        "subtopic": "Leveraging Monotonicity",
        "topic": "Binary Search",
        "category_file": "categories/basics/damage_over_time_binary_search_convex.md",
        "slug": "damage_over_time_binary_search_convex",
        "core_tags": [
            "Basics",
            "Leveraging Monotonicity",
            "Binary Search",
            "Greedy Spells",
            "Convex Envelope",
            "Arithmetic Series"
        ],
        "invariant": "When evaluating whether a monster of health H can be defeated in T turns, casting spell i when k turns remain contributes min(t_i, k) * d_i damage. Since each turn's contribution is independent, the optimal strategy greedily maximizes F(k) = max(max_{t_i <= k}(t_i d_i), k * max_{t_i > k} d_i) at each remaining turn k.",
        "editorial_reduction": "Binary search on turn count T in [1, 2 * 10^18].\nPrecompute unique values of t_i, prefix maximum of t_i * d_i, and suffix maximum of d_i.\nBetween adjacent distinct values of t, F(k) = max(C_1, k * C_2) is piecewise linear, summed in O(1) using arithmetic progressions.\nSum across at most N intervals in O(N) using __int128 to test if total damage >= H.",
        "time_complexity": "O(N \\log(H))",
        "space_complexity": "O(N)",
        "samples": scraped['abc303_f']['samples'],
        "cpp_solution": cpp_303
    },
    {
        "id": "arc152_d",
        "contest_id": "arc152",
        "title": "D. Halftree",
        "rating": 2381,
        "domain": "Basics",
        "subtopic": "Greedy and Constructive",
        "topic": "Basic Constructive Algorithms",
        "category_file": "categories/basics/cyclic_shift_halftree_grid_construction.md",
        "slug": "cyclic_shift_halftree_grid_construction",
        "core_tags": [
            "Basics",
            "Greedy and Constructive",
            "Basic Constructive Algorithms",
            "Graph Theory",
            "Trees",
            "Cayley Graphs"
        ],
        "invariant": "Adding M edges doubles to 2M edges after the +K mod N shift. For the result to be a tree, 2M = N - 1, which requires N to be odd (impossible if N is even). For odd N, arranging vertices on an n x g torus grid where moving down a row represents +K mod N allows constructing a tree via interlaced vertical backbone paths and horizontal comb bridges.",
        "editorial_reduction": "If N is even, output -1.\nLet g = gcd(N, K), n = N / g. Construct an n x g grid with grid[r][c] = ((r * K) mod N + c) mod N.\nIn odd-numbered columns (0-indexed c even), add vertical edges between row 2r and 2r+1 for r in 0 .. (n-3)/2.\nFrom odd-numbered columns c < g - 1, add horizontal edges to c+1 at rows 2r for r in 0 .. (n-3)/2.\nFrom even-numbered columns c < g - 1, add a single horizontal edge to c+1 at row n - 2.\nOutput the (N-1)/2 constructed edges.",
        "time_complexity": "O(N)",
        "space_complexity": "O(N)",
        "samples": scraped['arc152_d']['samples'],
        "cpp_solution": cpp_152
    },
    {
        "id": "donuts_2015_4",
        "contest_id": "donuts-2015",
        "title": "D. ドーナツの箱詰め",
        "rating": 2383,
        "domain": "Basics",
        "subtopic": "Greedy and Constructive",
        "topic": "Basic Greedy Algorithms",
        "category_file": "categories/basics/nested_box_buffer_difference_multiset.md",
        "slug": "nested_box_buffer_difference_multiset",
        "core_tags": [
            "Basics",
            "Greedy and Constructive",
            "Basic Greedy Algorithms",
            "Multiset Maintenance",
            "Dynamic Queries",
            "Chains"
        ],
        "invariant": "Using all active boxes to package K donuts partitions the boxes into K nesting chains, where buffer material is sum (C_{outer} - C_{inner}). This is mathematically equivalent to partitioning the sorted active boxes into K intervals, minimizing span minus the sum of the K-1 largest adjacent differences.",
        "editorial_reduction": "Sort all initial box capacities and compute all adjacent differences.\nMaintain two multisets: top_diffs containing the K-1 largest differences (with running sum) and bot_diffs containing the rest.\nFor each box crush event, remove the box from the active set; update adjacent differences by erasing old differences and adding the merged difference.\nAnswer each query in O(log N) as (max_elem - min_elem) - sum_top (or 0 if remaining boxes <= K).",
        "time_complexity": "O((N + Q) \\log N)",
        "space_complexity": "O(N)",
        "samples": scraped['donuts_2015_4']['samples'],
        "cpp_solution": cpp_donuts
    },
    {
        "id": "dwango2016qual_c",
        "contest_id": "dwango2016-prelims",
        "title": "C. メンテナンス明け",
        "rating": 2384,
        "domain": "Graph Theory",
        "subtopic": "Shortest Paths",
        "topic": "Dijkstra's Algorithm",
        "category_file": "categories/graph_theory/sleep_risk_adversarial_dijkstra.md",
        "slug": "sleep_risk_adversarial_dijkstra",
        "core_tags": [
            "Graph Theory",
            "Shortest Paths",
            "Dijkstra's Algorithm",
            "Game DP",
            "Adversarial Search",
            "State Space Reduction"
        ],
        "invariant": "When riding an edge e = (u -> v) on line L, falling asleep carries the passenger to the terminus T in that direction with penalty P(e) = dist_L(u, T) + d_{normal}(T). The optimal adversarial step from u minimizes max(w(e) + dp(v), P(e)), which defines a monotonic Dijkstra operator backwards from dst.",
        "editorial_reduction": "Run Dijkstra from dst on the original network to compute d_{normal}(u) for all stations.\nFor each line L, precompute distances to both termini to obtain P(e) for all directed edges in O(1).\nReverse all edges and run a min-priority queue backwards from dst with dp[dst] = 0, relaxing dp[u] = min(dp[u], max(w + dp[v], P)) until src is settled.",
        "time_complexity": "O((N + \\sum L_i) \\log N)",
        "space_complexity": "O(N + \\sum L_i)",
        "samples": scraped['dwango2016qual_c']['samples'],
        "cpp_solution": cpp_dwango
    },
    {
        "id": "abc337_f",
        "contest_id": "abc337",
        "title": "F. Usual Color Ball Problems",
        "rating": 2386,
        "domain": "Basics",
        "subtopic": "Leveraging Monotonicity",
        "topic": "Two Pointers",
        "category_file": "categories/basics/cyclic_box_allocation_two_pointers.md",
        "slug": "cyclic_box_allocation_two_pointers",
        "core_tags": [
            "Basics",
            "Leveraging Monotonicity",
            "Two Pointers",
            "Sliding Window",
            "Greedy Allocation",
            "Amortized Analysis"
        ],
        "invariant": "When balls arrive, an empty box is allocated to color c on its 1st, (K+1)-th, (2K+1)-th ball until M boxes are full. Once b_c boxes are allocated to color c, exactly min(total_count[c], b_c * K) balls of color c are accepted. The set of balls allocating boxes forms a sliding window [L, R) on the doubled array, maintained via two pointers in O(N) amortized time.",
        "editorial_reduction": "Duplicate C to length 2N to handle cyclic shifts seamlessly.\nMaintain active counts in_win[c] and allocated boxes b[c] for each color in the current window [L, R).\nAdvance R while total_boxes < M; incrementing b[c] dynamically updates the accepted balls sum min(total_count[c], b[c] * K).\nSlide L from 0 to N-1: record the answer, remove ball C[L] (reclaiming a box if in_win[c] % K == 0), and expand R forward to reallocate.",
        "time_complexity": "O(N)",
        "space_complexity": "O(N)",
        "samples": scraped['abc337_f']['samples'],
        "cpp_solution": cpp_337
    },
    {
        "id": "abc479_g",
        "contest_id": "abc479",
        "title": "G. Tuning",
        "rating": 2386,
        "domain": "Miscellaneous",
        "subtopic": "Search Techniques",
        "topic": "Ternary Search",
        "category_file": "categories/miscellaneous/collinear_manhattan_weighted_median.md",
        "slug": "collinear_manhattan_weighted_median",
        "core_tags": [
            "Miscellaneous",
            "Search Techniques",
            "Ternary Search",
            "Weighted Median",
            "L1 Minimization",
            "Fractional Optimization"
        ],
        "invariant": "Perturbed points (A_i + c_i, B_i + d_i) lie on a line through the origin. The minimum Manhattan distance from (A_i, B_i) to line Y = s X (|s| <= 1) is |B_i - s A_i|, and to X = t Y (|t| <= 1) is |A_i - t B_i|. Both reduce to finding the weighted median of critical slope ratios in [-1, 1], evaluated exactly using __int128 rational arithmetic.",
        "editorial_reduction": "Case 1: Line Y = s X with s in [-1, 1]. For points with A_i != 0, critical points are B_i / A_i with weight |A_i|. Sort points in [-1, 1] and find the weighted median s, clamping to [-1, 1]. Evaluate sum |B_i - s A_i|.\nCase 2: Line X = t Y with t in [-1, 1]. For points with B_i != 0, critical points are A_i / B_i with weight |B_i|. Find weighted median t clamped to [-1, 1] and evaluate sum |A_i - t B_i|.\nTake the minimum of the two cases and output the exact irreducible fraction p / q.",
        "time_complexity": "O(N \\log N)",
        "space_complexity": "O(N)",
        "samples": scraped['abc479_g']['samples'],
        "cpp_solution": cpp_479
    },
    {
        "id": "abc135_f",
        "contest_id": "abc135",
        "title": "F. Strings of Eternity",
        "rating": 2388,
        "domain": "Strings",
        "subtopic": "String Matching",
        "topic": "Knuth Morris Pratt (KMP) and Prefix Automaton",
        "category_file": "categories/strings/infinite_string_matching_functional_graph_kmp.md",
        "slug": "infinite_string_matching_functional_graph_kmp",
        "core_tags": [
            "Strings",
            "String Matching",
            "Knuth Morris Pratt (KMP) and Prefix Automaton",
            "Functional Graph",
            "DAG Longest Path",
            "Cycle Detection"
        ],
        "invariant": "If string t matches in s^infinity at position p in [0, |s|-1], the next consecutive copy of t must start at (p + |t|) mod |s|. This defines a functional graph on |s| vertices where each vertex has out-degree <= 1. An infinite repetition exists iff there is a directed cycle; otherwise the maximum repetition count is the longest path in the DAG.",
        "editorial_reduction": "Repeat string s to length at least |t| + |s|.\nRun KMP prefix function on pattern t + '#' + s_repeated to identify all starting match indices p in [0, |s|-1].\nBuild directed edges p -> (p + |t|) mod |s| for all matching positions p.\nPerform DFS with 3-color states (unvisited, visiting, visited) to detect cycles (outputting -1) or compute memoized longest paths, returning the maximum path length.",
        "time_complexity": "O(|s| + |t|)",
        "space_complexity": "O(|s| + |t|)",
        "samples": scraped['abc135_f']['samples'],
        "cpp_solution": cpp_135
    },
    {
        "id": "abc325_g",
        "contest_id": "abc325",
        "title": "G. offence",
        "rating": 2388,
        "domain": "Dynamic Programming (DP)",
        "subtopic": "Classic DP",
        "topic": "Interval DP / Range DP / Matrix Chain Multiplication (MCM)",
        "category_file": "categories/dynamic_programming/interval_dp_of_elimination.md",
        "slug": "interval_dp_of_elimination",
        "core_tags": [
            "Dynamic Programming (DP)",
            "Classic DP",
            "Interval DP / Range DP / Matrix Chain Multiplication (MCM)",
            "String Reduction",
            "Greedy Elimination"
        ],
        "invariant": "For any substring S[l..r], optimal deletions preserve contiguous remaining subsequences. Whenever S[l]=='o' pairs with S[m]=='f' such that the enclosed interval S[l+1..m-1] is completely eliminated (dp[l+1][m-1] == 0), the formed 'of' can delete up to K remaining characters from S[m+1..r], leaving max(0, dp[m+1][r] - K) characters.",
        "editorial_reduction": "Compute interval DP dp[l][r] for substring length len from 1 to |S| (N <= 300).\nBase cases: dp[l][l] = 1, and dp[l][r] = 1 + dp[l+1][r].\nTransition 1: dp[l][r] = min_{m} (dp[l][m] + dp[m+1][r]).\nTransition 2: If S[l] == 'o', iterate m from l+1 to r: if S[m] == 'f' and dp[l+1][m-1] == 0, update dp[l][r] = min(dp[l][r], max(0, dp[m+1][r] - K)).\nReturn dp[0][N-1].",
        "time_complexity": "O(|S|^3)",
        "space_complexity": "O(|S|^2)",
        "samples": scraped['abc325_g']['samples'],
        "cpp_solution": cpp_325
    }
]

with open('scratch/part5_part3f1_meta.json', 'w', encoding='utf-8') as f:
    json.dump(problems, f, ensure_ascii=False, indent=2)

print(f"Generated scratch/part5_part3f1_meta.json with {len(problems)} problems successfully!")
