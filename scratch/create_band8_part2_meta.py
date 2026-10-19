import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/band8_p2_samples.json', 'r', encoding='utf-8') as f:
    samples_db = json.load(f)

meta_definitions = [
    {
        "id": "arc184_d",
        "name": "D - Erase Balls 2D",
        "contest": "arc184",
        "rating": 2804,
        "domain": "Dynamic Programming (DP)",
        "subtopic": "Dp on Different Structures",
        "topic": "DP on Trees and DAGs",
        "category_file": "categories/dynamic_programming/quadrant_erasure_antichain_grid_dp.md",
        "key_idea": "Given N balls on a 2D grid with permutation coordinates (X_i, Y_i), any chosen ball k erases all balls in its bottom-left and top-right quadrants. Find the number of distinct subsets of balls that can remain after any sequence of operations modulo 998244353.",
        "observation": "Any non-empty remaining set must form an antichain (strictly decreasing sequence of Y coordinates when ordered by X). Furthermore, a set is reachable if and only if it is maximal among antichains: no omitted ball between adjacent elements i and j could have survived without being erased by one of the selected balls. By adding sentinel boundary points at (0, N+1) and (N+1, 0), transition from i to j (with i < j, P_i > P_j) is valid if and only if no point k in between has empty rectangular regions (i, k, P_j, P_k) and (k+1, j, P_k+1, P_i). This yields an O(N^3) DP over the DAG of valid transitions.",
        "algorithm": "1. Add boundary sentinel points (0, N+1) and (N+1, 0) and sort points by X.\n2. Precompute 2D prefix sums for rectangle point counts rect_sum(xl, xr, yl, yr).\n3. Define dp[j] as the number of reachable maximal prefixes ending at point j, with dp[0] = 1.\n4. For each pair (i, j) with i < j and P_i > P_j, test if transition is maximal: for every intermediate k in (i, j) with P_j < P_k < P_i, verify that either rect_sum(i, k, P_j, P_k) > 0 or rect_sum(k+1, j, P_k+1, P_i) > 0.\n5. If maximal, add dp[i] to dp[j] modulo 998244353.\n6. Output dp[N+1].",
        "time_complexity": "O(N^3)",
        "space_complexity": "O(N^2)"
    },
    {
        "id": "agc064_d",
        "name": "D - Red and Blue Chips",
        "contest": "agc064",
        "rating": 2808,
        "domain": "Miscellaneous",
        "subtopic": "General",
        "topic": "Functional Graphs",
        "category_file": "categories/miscellaneous/colored_chips_functional_graph_cycles.md",
        "key_idea": "Given an N-character string S of R and B chips with square N guaranteed to be blue, chips at square i are repeatedly merged onto higher-indexed blue squares j. Determine the number of distinct color sequences in the final stack at square N modulo 998244353.",
        "observation": "Deleting the last B and stripping trailing Rs leaves S = R^{c_B} B ... R^{c_1} B. The final pile corresponds to partitioning the R chips into B blocks of sizes (l_1, ..., l_B) extracted greedily. Sorting l into descending order l'_1 >= ... >= l'_B >= 0, dominance inequalities require sum_{q=0}^p l'_q >= sum_{q=0}^p c_q for all p, where l'_0 = R - sum l'_i. Equivalently, the suffix sums of l' are bounded by the suffix sums of c. Counting permutations with multiplicity factor B! / prod(f_i!) reduces to an integer partition DP in O(R^3) time.",
        "algorithm": "1. Strip the final 'B' and all trailing 'R's from S. If empty or no 'B' remains, return 1.\n2. Split the remaining string by 'B' to extract block sizes c_1, ..., c_B of 'R's and compute total R.\n3. Compute suffix sums suf_c[m] = sum_{q=B-m+1}^B c_q.\n4. Define dp[m][s] as the coefficient sum over placing m elements with sum s <= suf_c[m].\n5. For each value v from 0 to R, transition by choosing cnt copies of v, updating next_dp[m + cnt][s + cnt * v] += dp[m][s] / cnt!.\n6. Multiply dp[B][s] by B! and sum over valid total sums s <= suf_c[B] modulo 998244353.",
        "time_complexity": "O(R^3) = O(N^3)",
        "space_complexity": "O(B * R) = O(N^2)"
    },
    {
        "id": "arc139_d",
        "name": "D - Priority Queue",
        "contest": "arc139",
        "rating": 2816,
        "domain": "Math",
        "subtopic": "Probabilities and Expected Values",
        "topic": "Probabilities and Expected Values",
        "category_file": "categories/math/multiset_threshold_indicator_zero_one_principle.md",
        "key_idea": "Given a multiset A of N integers in [1, M], repeat K times: insert a uniformly chosen integer in [1, M] and erase the X-th smallest element. Find the sum of multiset element sums across all M^K operation sequences modulo 998244353.",
        "observation": "By the 0-1 principle, sum_{a in A} a = sum_{v=1}^M sum_{a in A} [a >= v]. For any fixed threshold v, map elements >= v to 1 and < v to 0. An inserted 1 increases the count of ones c by 1 iff c <= N - X, while an inserted 0 decreases c by 1 iff c > N - X + 1. Thus c = N - X + 1 is an absorbing boundary! Crucially, the final count of 1s depends solely on the total number of inserted 1s j, independent of insertion order: final_c = min(N - X + 1, c_0 + j) if c_0 <= N - X + 1, and max(N - X + 1, c_0 - (K - j)) otherwise.",
        "algorithm": "1. Compute prefix frequencies of initial elements >= v for all v in [1, M].\n2. Add the baseline contribution of v = 1: N * M^K mod 998244353.\n3. For each threshold v in [2, M], let c0 = count(A_i >= v), p1 = M - v + 1, p0 = v - 1.\n4. Iterate over the number of inserted 1s j from 0 to K. The probability weight is C(K, j) * p1^j * p0^(K - j).\n5. Determine the deterministic final count of 1s: min(N - X + 1, c0 + j) if c0 <= N - X + 1 else max(N - X + 1, c0 - (K - j)).\n6. Accumulate over all v and j modulo 998244353.",
        "time_complexity": "O(M * K)",
        "space_complexity": "O(K)"
    },
    {
        "id": "abc296_h",
        "name": "Ex - Unite",
        "contest": "abc296",
        "rating": 2822,
        "domain": "Miscellaneous",
        "subtopic": "General",
        "topic": "Broken Profile DP / Plug DP",
        "category_file": "categories/miscellaneous/grid_connected_component_plug_profile_dp.md",
        "key_idea": "Given an N x M grid (M <= 7) with black and white cells containing at least one black cell, find the minimum number of white cells to paint black so that all black cells form a single connected component.",
        "observation": "Because M <= 7, this is a canonical Broken Profile / Plug DP problem. When processing cell by cell (i, j), we maintain the connectivity profile of the frontier of length M+1 (the latest cell of each column). The partition of frontier black cells into connected components has at most B_7 = 877 states, which can be canonically renumbered. As cells are colored black or left white, components are merged or closed. A closed component cannot be abandoned if there are remaining original black cells.",
        "algorithm": "1. Generate all canonical frontier partition states for each boundary cut j in 0..M-1.\n2. Initialize DP table dp[state] = 0 for empty frontier state.\n3. For each cell (i, j) in row-major order, transition to cell (i, j+1) by considering both decisions (keep white if allowed, or paint black):\n   a. If keeping white, ensure no isolated black component in the frontier is prematurely abandoned if further black cells exist.\n   b. If painting black, connect with adjacent left and top frontier plugs and renumber the partition.\n4. At the grid end, take the minimum cost among states with at most 1 connected component.\n5. Subtract the original number of black cells to obtain newly painted cells.",
        "time_complexity": "O(N * M * States)",
        "space_complexity": "O(States)"
    },
    {
        "id": "arc104_e",
        "name": "E - Random LIS",
        "contest": "arc104",
        "rating": 2824,
        "domain": "Combinatorics",
        "subtopic": "Partitions",
        "topic": "Partitions of a Set / Bell Number",
        "category_file": "categories/combinatorics/ordered_set_partition_random_lis_expectation.md",
        "key_idea": "Given N <= 6 and upper bounds A_1, ..., A_N, random variables X_i are chosen uniformly from [1, A_i]. Compute the expected length of the Longest Increasing Subsequence (LIS) of X modulo 1000000007.",
        "observation": "For N <= 6, the relative order of elements X_1, ..., X_N is governed by one of the F(6) = 4683 ordered set partitions (weak orderings). For a fixed weak ordering, the LIS is deterministic. The number of integer assignments Y_1 < Y_2 < ... < Y_k satisfying Y_j <= min_{i in part j} A_i is computed using interval DP over the O(N) coordinate intervals formed by breakpoints {0} union {A_i}.",
        "algorithm": "1. Generate all set partitions of {0..N-1} into k parts, and all k! orderings of parts to obtain all 4683 ordered set partitions.\n2. For each ordered partition, determine its deterministic LIS value and upper bounds U_rank = min_{r[i] == rank} A_i.\n3. Discretize upper bounds into O(N) intervals (coords[m], coords[m+1]] of length L.\n4. Run interval DP: dp[j] is the number of ways to assign the first j ranks into intervals, choosing c ranks in interval m with comb(L, c) ways.\n5. Multiply dp[k] by the LIS length, accumulate total LIS sum, and divide by prod(A_i) mod 1000000007.",
        "time_complexity": "O(F(N) * N^2)",
        "space_complexity": "O(N^2)"
    },
    {
        "id": "arc106_e",
        "name": "E - Medals",
        "contest": "arc106",
        "rating": 2825,
        "domain": "Dynamic Programming (DP)",
        "subtopic": "Bit Related DP",
        "topic": "Sum Over Subsets DP (SOS DP)",
        "category_file": "categories/dynamic_programming/employee_schedule_halls_marriage_sos_dp.md",
        "key_idea": "N employees (N <= 18) cycle between working A_i days and resting A_i days. Each day, 1 working employee can receive a medal. Find the minimum days D so that every employee receives at least K medals.",
        "observation": "This is bipartite matching between N employees (demand K each) and days 1..D (capacity 1). By Hall's Marriage Theorem, a valid matching exists iff for every subset S of employees, the number of days where at least one employee in S works is at least |S| * K. Equivalently, the number of days where the working mask W(d) is a subset of S^c must be at most D - |S| * K. Since D <= 2NK <= 3.6 * 10^6, binary search on D with Fast Walsh-Hadamard / SOS DP on 2^18 masks checks Hall's condition in O(N * 2^N) per step.",
        "algorithm": "1. Precompute day_mask[d] for each day d in 1..2NK indicating which employees work on day d.\n2. Binary search D in [1, 2NK].\n3. For a candidate D, populate frequency array cnt[mask] for d in 1..D.\n4. Compute SOS DP over all 2^N masks: sos[mask] = sum_{sub in mask} cnt[sub] in O(N 2^N) time.\n5. For every mask T, verify sos[T] <= D - (N - popcount(T)) * K.\n6. Return the minimal valid D.",
        "time_complexity": "O(N * K + log(NK) * N * 2^N)",
        "space_complexity": "O(NK + 2^N)"
    },
    {
        "id": "arc123_e",
        "name": "E - Training",
        "contest": "arc123",
        "rating": 2828,
        "domain": "Number Theory",
        "subtopic": "Floor Sum",
        "topic": "Floor Sum and Mod Sum of Arithmetic Progression",
        "category_file": "categories/number_theory/arithmetic_level_intersection_floor_sum.md",
        "key_idea": "Two programmers with starting levels A_X, A_Y gain 1 level every B_X, B_Y menus. Count n in 1..N such that A_X + floor(n / B_X) == A_Y + floor(n / B_Y) across T test cases.",
        "observation": "Let f(x) = A_X + x/B_X and g(x) = A_Y + x/B_Y with floor functions F(x), G(x). F(x) == G(x) can only hold when f(x) - g(x) is in [-1, 1). In [-1, 0), F(x) in {G(x)-1, G(x)}, so the equality indicator is 1 - G(x) + F(x). In [0, 1), F(x) in {G(x), G(x)+1}, so the indicator is 1 - F(x) + G(x). The range bounds are solved linearly, and prefix sums of floor(A + x/B) over arithmetic progressions evaluate in O(1) time using block division.",
        "algorithm": "1. If B_X == B_Y, return N if A_X == A_Y else 0.\n2. WLOG assume B_X < B_Y (swapping X and Y if needed), making slope (B_Y - B_X) / (B_X B_Y) strictly positive.\n3. Compute boundary thresholds x_m1, x_0, x_p1 for f(x) - g(x) in [-1, 0) and [0, 1) using ceil division.\n4. For [x_m1, x_0) intersected with [1, N+1), add (R - L) - sum(G) + sum(F).\n5. For [x_0, x_p1) intersected with [1, N+1), add (R - L) - sum(F) + sum(G).\n6. Evaluate prefix floor sums sum_{x=0}^{n-1} floor(A + x/B) = n A + B * q*(q-1)/2 + r*q in O(1).",
        "time_complexity": "O(1) per test case, O(T) total",
        "space_complexity": "O(1)"
    },
    {
        "id": "agc067_c",
        "name": "C - Divisibility Homomorphism",
        "contest": "agc067",
        "rating": 2829,
        "domain": "Graph Theory",
        "subtopic": "Partially Ordered Set (POSET)",
        "topic": "POSET ft Dilworth's and Mirsky's Theorem",
        "category_file": "categories/graph_theory/divisibility_preserving_sequence_multiplicative_lattice.md",
        "key_idea": "Determine whether a prefix sequence (A_1, ..., A_N) of positive integers can be extended to an infinite sequence satisfying a_n <= C * n and a_n | a_m <=> n | m.",
        "observation": "Divisibility preservation a_n | a_m <=> n | m defines a lattice embedding from the divisibility poset of integers into itself. The linear bound constraint a_n <= C * n forces the prime valuations v_p(a_x) to strictly respect the valuation layers of x: for every prime p <= N, if v_p(x) > v_p(y), then v_p(a_x) > v_p(a_y). Thus, each valuation layer {x : v_p(x) = k} must map to values with v_p(a_x) strictly greater than all values in layer k-1.",
        "algorithm": "1. Verify that all elements in A are distinct.\n2. Check divisibility on all divisor pairs: for every x in 1..N and multiple y = 2x, 3x, ..., verify A_x | A_y.\n3. Sieve all primes p <= N.\n4. For each prime p, group indices x in 1..N by vx = v_p(x), and compute the minimum and maximum of vax = v_p(A_x) in each layer.\n5. Verify strict layer monotonicity: max v_p(A_x) in layer k must be strictly less than min v_p(A_y) in layer k+1.\n6. Output 'Yes' if all conditions hold, else 'No'.",
        "time_complexity": "O(N log N + N pi(N))",
        "space_complexity": "O(N)"
    },
    {
        "id": "abc293_h",
        "name": "Ex - Optimal Path Decomposition",
        "contest": "abc293",
        "rating": 2831,
        "domain": "Dynamic Programming (DP)",
        "subtopic": "Dp on Different Structures",
        "topic": "DP on Trees and DAGs",
        "category_file": "categories/dynamic_programming/tree_simple_path_coloring_decomposition_dp.md",
        "key_idea": "Partition vertices of an N-vertex tree into monochromatic simple paths such that any simple path in the tree intersects at most K colors. Find the minimum possible K.",
        "observation": "Color monochromatic edges 'black' (weight 0) and inter-color edges 'white' (weight 1). Black edges form vertex-disjoint paths, meaning each vertex has degree at most 2 in black edges. The maximum number of colors on any tree path is (diameter in {0, 1} weights) + 1. By HLD, the optimal K is at most 2 * floor(log2 N) + 1. For a fixed K, tree DP determines whether a {0, 1} weighting with diameter <= K - 1 exists in O(N) time.",
        "algorithm": "1. Binary search K in [1, N].\n2. Tree DP defines dp[u][0/1]: minimum maximum distance into subtree u when the parent edge has weight 0 or 1, requiring subtree diameter <= K - 1.\n3. For vertex u, sort children by dp[v][1] descending.\n4. Select at most 1 child (for dp0) or at most 2 children (for dp1) to have edge weight 0, keeping others at weight 1.\n5. Check that max1 + max2 <= K - 1 for path through u, minimizing max1.\n6. Binary search returns the minimal valid K.",
        "time_complexity": "O(N log N)",
        "space_complexity": "O(N)"
    },
    {
        "id": "panasonic2020_f",
        "name": "F - Fractal Shortest Path",
        "contest": "panasonic2020",
        "rating": 2834,
        "domain": "Basics",
        "subtopic": "Divide and Conquer",
        "topic": "Divide and Conquer",
        "category_file": "categories/basics/sierpinski_carpet_fractal_shortest_path.md",
        "key_idea": "Given a Level 30 Sierpinski carpet fractal of size 3^30 x 3^30 where center blocks of size 3^t x 3^t are solid black obstacles, answer Q queries finding the shortest path distance through white cells between (a, b) and (c, d).",
        "observation": "On a grid without obstacles, distance is L1 Manhattan distance |x1 - x2| + |y1 - y2|. Black squares form square obstacles of size 3^t for t in 0..30. A path between two points must detour around at most one maximal blocking obstacle of size 3^t at any level. The extra detour around an obstacle of size 3^t is 2 * min(min(x1%3^t, x2%3^t) + 1, 3^t - max(x1%3^t, x2%3^t)). The exact distance equals the Manhattan distance plus 2 * max(extra_x, extra_y).",
        "algorithm": "1. Convert coordinates to 0-indexed.\n2. Base distance is |x1 - x2| + |y1 - y2|.\n3. For each power of three 3^t for t in 0..34, check if an obstacle at level t lies strictly between (x1, y1) and (x2, y2) using base-3 ternary digit analysis.\n4. If an obstacle of size 3^t separates the coordinates along an axis, compute the minimal detour around its boundary.\n5. The answer is Manhattan distance + 2 * max(detour_x, detour_y).\n6. Answer each query in O(log_3(Grid)) = O(35) time.",
        "time_complexity": "O(Q * log_3(Grid))",
        "space_complexity": "O(1)"
    },
    {
        "id": "abc242_h",
        "name": "Ex - Random Painting",
        "contest": "abc242",
        "rating": 2835,
        "domain": "Combinatorics",
        "subtopic": "Inclusion Exclusion",
        "topic": "Principle of Inclusion and Exclusion (PIE)",
        "category_file": "categories/combinatorics/segment_coverage_min_max_expectation_interval_dp.md",
        "key_idea": "N cells initially white. M intervals [L_i, R_i] in a box. In each step, draw a random interval and paint its cells black. Find the expected number of steps until all N cells are black modulo 998244353.",
        "observation": "By Min-Max Expectation, E[max T_i] = sum_{empty != S} (-1)^{|S|+1} E[min_{i in S} T_i]. The time to hit at least one cell in S is a geometric random variable with expectation M / c(S), where c(S) is the number of intervals intersecting S. Crucially, c(S) = M - (intervals disjoint from S). For a chosen subset S = {s_1 < ... < s_k}, an interval is disjoint from S iff it lies entirely within one gap [s_j + 1, s_{j+1} - 1]. An interval DP computes the signed weights sum_{S: c(S) = c} (-1)^{|S|+1} in O(N^2 M) time.",
        "algorithm": "1. Precompute cnt[l][r]: number of given intervals completely contained in [l, r].\n2. Define dp[i][k]: last chosen element of S is i, with k total disjoint intervals so far, storing sum of (-1)^|S|.\n3. Initialize dp[0][0] = 1.\n4. Transition from i to j in i+1..N+1: add cnt[i+1][j-1] to disjoint count k, multiplying by -1 if j <= N (adding an element to S).\n5. For each disjoint count k, c(S) = M - k. Extract ways = dp[N+1][k] (excluding empty set).\n6. Multiply by (-1) to obtain (-1)^{|S|+1}, and accumulate ways * M * inv(c) modulo 998244353.",
        "time_complexity": "O(N^2 * M)",
        "space_complexity": "O(N * M)"
    },
    {
        "id": "arc065_c",
        "name": "E - Manhattan Compass",
        "contest": "arc065",
        "rating": 2835,
        "domain": "Geometry",
        "subtopic": "Sweep Line",
        "topic": "Sweep Line Algorithm and Radial Sweep",
        "category_file": "categories/geometry/manhattan_chebyshev_rotation_connected_pairs_bfs.md",
        "key_idea": "N points on the plane. A Manhattan compass points to a pair of points with fixed distance D = d(a, b). Compass can move from (p, q) to (p, r) if d(p, r) == d(p, q) == D. Find the number of reachable pairs.",
        "observation": "Rotate coordinates 45 degrees: (X, Y) = (x + y, x - y), so Manhattan distance becomes Chebyshev distance max(|X_1 - X_2|, |Y_1 - Y_2|) = D. Vertices reachable by the compass are exactly the connected component of {a, b} in the distance-D graph. To run BFS in O(N log N) time, store unvisited points in balanced BSTs ordered by X and Y; deleting visited points ensures each vertex is visited once. Counting distance-D pairs in the component uses binary search on 1D slices.",
        "algorithm": "1. Rotate points (x, y) -> (x+y, x-y) and compute target distance D = max(|Xa - Xb|, |Ya - Yb|).\n2. Insert all points into two std::map<ll, set<pair<ll, int>>> indexed by X and Y.\n3. Run BFS from a and b: for point (xu, yu), query lines X = xu +- D for Y in [yu - D, yu + D] and lines Y = yu +- D for X in [xu - D, xu + D], queuing and erasing visited points.\n4. Group component points into sorted vectors by X and by Y.\n5. For each point in the component, count pairs with X' = X + D and Y' in [Y - D, Y + D], plus pairs with Y' = Y + D and X' in [X - D + 1, X + D - 1] to avoid corner double-counting.\n6. Output total pair count.",
        "time_complexity": "O(N log N)",
        "space_complexity": "O(N)"
    },
    {
        "id": "arc103_d",
        "name": "F - Distance Sums on a Tree",
        "contest": "arc103",
        "rating": 2836,
        "domain": "Graph Theory",
        "subtopic": "More Tree Stuff",
        "topic": "Rerooting Technique",
        "category_file": "categories/graph_theory/tree_reconstruction_distance_sum_centroid_greedy.md",
        "key_idea": "Given N distinct integers D_1, ..., D_N representing the sum of tree distances from each vertex to all other vertices, reconstruct the tree or determine that none exists.",
        "observation": "By tree distance properties, moving across edge (u, v) changes the distance sum by D(u) - D(v) = N - 2 * sz(u), where sz(u) is the subtree size of u directed away from v. The vertex with the maximum D_u must be a leaf (sz(u) = 1). Its parent v must uniquely have D(v) = D(u) - (N - 2 * sz(u)). Processing vertices in descending order of D greedily identifies each parent, accumulating subtree sizes. Finally, verifying the distance sum of the centroid/root on the reconstructed tree confirms correctness.",
        "algorithm": "1. Map each D_i to vertex id i, and sort vertices in descending order of D_i.\n2. Initialize subtree size sz[u] = 1 for all vertices.\n3. For each vertex u from largest to second smallest D:\n   a. Target parent distance is target_D = D[u] - (N - 2 * sz[u]).\n   b. Look up target_D in hash map. If not found or v == u, return -1.\n   c. Add edge (u, v) and update sz[v] += sz[u].\n4. Verify that root (minimum D) has sz[root] == N.\n5. Run BFS from root to compute actual distance sum and verify it matches D[root].\n6. Print the N-1 edges if valid, else -1.",
        "time_complexity": "O(N log N)",
        "space_complexity": "O(N)"
    },
    {
        "id": "abc280_g",
        "name": "G - Do Use Hexagon Grid 2",
        "contest": "abc280",
        "rating": 2842,
        "domain": "Basics",
        "subtopic": "Leveraging Monotonicity",
        "topic": "Two Pointers",
        "category_file": "categories/basics/hexagonal_coordinate_transformation_bounding_box_sweep.md",
        "key_idea": "On a hexagonal grid, distance is d((i1, j1), (i2, j2)) = max(|i1 - i2|, |j1 - j2|, |(i1 - j1) - (i2 - j2)|). Given N points, count non-empty subsets where all pairwise distances are <= D modulo 998244353.",
        "observation": "Mapping (X, Y) -> (X, Y, X - Y) embeds the hexagonal metric into 3D Chebyshev space. By Helly's property for L_infinity balls, all pairwise distances are <= D iff all points fit in a bounding box [X, X+D] x [Y, Y+D] x [Z, Z+D]. Subsets are uniquely counted by their coordinate minima (X, Y, Z). For fixed X and Y, maintaining points in the Z-window [Z, Z+D] with two pointers allows evaluating PIE over the 8 boundary conditions in O(1) per step, yielding an O(N^3) total algorithm.",
        "algorithm": "1. Transform points (X, Y) -> (X, Y, X - Y) and extract unique X and Y coordinates.\n2. Precompute powers of 2 modulo 998244353.\n3. Loop over unique X and filter points in [X, X + D]. Loop over unique Y and filter points in [Y, Y + D].\n4. Sort remaining candidates by z. Use two pointers [l, r) to slide the window [Z, Z + D].\n5. For each distinct Z = z_l, expand r to include z <= Z + D.\n6. Use PIE over 8 subsets of {x > X, y > Y, z > Z} to count valid non-empty subsets with exact minima X, Y, Z.\n7. Sum contributions modulo 998244353.",
        "time_complexity": "O(N^3)",
        "space_complexity": "O(N)"
    },
    {
        "id": "agc071_b",
        "name": "B - Maximum Bracket Subsequence",
        "contest": "agc071",
        "rating": 2842,
        "domain": "Dynamic Programming (DP)",
        "subtopic": "Digit DP",
        "topic": "Digit DP",
        "category_file": "categories/dynamic_programming/bracket_sequence_subsequence_dfa_prefix_balance_dp.md",
        "key_idea": "Given N, K and a valid bracket sequence S of length K, count strings T of length N whose lexicographically largest valid bracket subsequence of length K is S modulo 998244353.",
        "observation": "Valid bracket sequences prefer ')' over '(' for lexicographical maximality. Decompose S into a copies of '()' followed by b prime/splendid bracket sequences (where the first is not '()'). If S = ()^{K/2}, T needs only contain S as a subsequence, yielding sum_{j=K}^N C(j-1, K-1) 2^{N-j}. Otherwise, analyzing the insertion positions of '(' and ')' into the prime components yields rational generating functions: b x^2 / (1-x)^{2a+b+3} for >= 1 insertions, and (b x + 1) / (1-x)^{2a+b+2} for 0 insertions. Extracting coefficients via negative binomial expansion solves the problem in O(1) or O(N) time.",
        "algorithm": "1. If S equals () repeated K/2 times, compute sum_{j=K}^N C(j-1, K-1) * 2^(N-j) iteratively in O(N) time.\n2. Otherwise, count leading '()' blocks to determine a, and decompose the remainder of S into b prime components.\n3. Let m = N - K be the number of inserted characters.\n4. Contribution from >= 1 insertions is b * C(m - 2 + (2a + b + 3) - 1, (2a + b + 3) - 1).\n5. Contribution from 0 insertions is C(m + (2a + b + 2) - 1, (2a + b + 2) - 1) + b * C(m - 1 + (2a + b + 2) - 1, (2a + b + 2) - 1).\n6. Output the sum modulo 998244353.",
        "time_complexity": "O(N) for repetitive case, O(K) for general case",
        "space_complexity": "O(1)"
    },
    {
        "id": "abc297_h",
        "name": "Ex - Diff Adjacent",
        "contest": "abc297",
        "rating": 2855,
        "domain": "Math",
        "subtopic": "Polynomial",
        "topic": "Generating Functions",
        "category_file": "categories/math/splendid_compositions_adjacent_diff_generating_function.md",
        "key_idea": "A sequence of positive integers is splendid if all adjacent terms are distinct. Find the sum of lengths of all splendid sequences whose sum of elements is N modulo 998244353.",
        "observation": "Let f(x, y) be the bivariate generating function where [x^N y^M] f(x, y) is the count of splendid compositions of N with length M. By PIE on adjacent equal elements, g(x, y) = sum_{i=1}^inf x^i y / (1 + x^i y), so f(x, y) = 1 / (1 - g(x, y)). The sum of lengths is given by d/dy f(x, y)|_{y=1} = P(x) / Q(x)^2, where Q(x) = 1 - sum_{i=1}^inf x^i / (1 + x^i) and P(x) = sum_{i=1}^inf x^i / (1 + x^i)^2. Expanding P(x) and Q(x) via divisor sums takes O(N log N) time, followed by NTT polynomial inversion and multiplication.",
        "algorithm": "1. Compute coefficients of Q(x) = 1 - sum_{i=1}^N sum_{k=1}^{N/i} (-1)^{k-1} x^{ik} in O(N log N) via sieve.\n2. Compute coefficients of P(x) = sum_{i=1}^N sum_{k=1}^{N/i} k * (-1)^{k-1} x^{ik} in O(N log N) via sieve.\n3. Compute polynomial inverse inv_Q = 1 / Q mod x^{N+1} using Newton's method with NTT in O(N log N).\n4. Compute inv_Q2 = inv_Q^2 mod x^{N+1} using NTT multiplication.\n5. Compute h(x) = P(x) * inv_Q2 mod x^{N+1} using NTT.\n6. Output h[N] modulo 998244353.",
        "time_complexity": "O(N log N)",
        "space_complexity": "O(N)"
    }
]

# Enrich with cpp_solution and samples
for p in meta_definitions:
    pid = p['id']
    cpp_path = f"scratch/test_{pid}.cpp"
    with open(cpp_path, 'r', encoding='utf-8') as f:
        p['cpp_solution'] = f.read()
    p['samples'] = samples_db[pid]['samples']

with open('scratch/band8_part2_meta.json', 'w', encoding='utf-8') as f:
    json.dump(meta_definitions, f, indent=2, ensure_ascii=False)

print(f"Successfully generated scratch/band8_part2_meta.json with {len(meta_definitions)} problems!")
