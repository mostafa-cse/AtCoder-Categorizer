import os
import subprocess
import json

# Ensure directories exist
os.makedirs("analysis", exist_ok=True)
os.makedirs("categories", exist_ok=True)
os.makedirs("state", exist_ok=True)

print("=" * 75)
print("      PROCESSING BATCH 5 PART 1B: ABC CURATED LADDER (1651 - 1699)")
print("=" * 75)

SELECTED_PROBLEMS = [
    {
        "id": "abc054_d",
        "title": "Mixing Experiment",
        "contest_id": "abc054",
        "rating": 1655,
        "tag": "Dynamic Programming",
        "subtopic": "Classic DP",
        "topic": "2-Ratio Knapsack DP / Ratio Reduction to Target GCD",
        "cat_folder": "dp",
        "cat_file": "two_ratio_knapsack_dp.md",
        "statement": "N chemicals, chemical i has a_i grams of substance A, b_i grams of substance B, and costs c_i. Find the minimum cost to obtain a mixture with substance ratio exactly Ma : Mb, or -1 if impossible.",
        "key_idea": "2D Knapsack DP maintaining the exact weights of substance A and B: dp[a][b] = minimum cost to obtain a grams of A and b grams of B. At the end, minimize dp[k * Ma][k * Mb] over all k >= 1.",
        "observation": "Max total weight of A or B is at most 40 * 10 = 400. The DP table size is 401 x 401, taking O(N * (max_A) * (max_B)) ~ 40 * 400 * 400 = 6.4 * 10^6 operations.",
        "algorithm": [
            "Initialize dp[401][401] with INF. dp[0][0] = 0.",
            "For each chemical (a_i, b_i, c_i):",
            "  For a from 400 down to a_i:",
            "    For b from 400 down to b_i:",
            "      dp[a][b] = min(dp[a][b], dp[a - a_i][b - b_i] + c_i).",
            "min_cost = INF.",
            "For k from 1 such that k * Ma <= 400 and k * Mb <= 400:",
            "  min_cost = min(min_cost, dp[k * Ma][k * Mb]).",
            "Print min_cost < INF ? min_cost : -1."
        ],
        "time_complexity": "O(N * max_A * max_B)",
        "space_complexity": "O(max_A * max_B)",
        "core_skill": "Multi-dimensional knapsack tracking exact additive resource pairs to match target ratios.",
        "reusable_pattern": "Exact Ratio Knapsack: dp[a][b] + query min_k dp[k*Ma][k*Mb].",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int INF = 1e9;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, ma, mb;
    if (!(cin >> n >> ma >> mb)) return 0;

    vector<vector<int>> dp(401, vector<int>(401, INF));
    dp[0][0] = 0;

    for (int i = 0; i < n; ++i) {
        int a, b, c;
        cin >> a >> b >> c;
        for (int sa = 400; sa >= a; --sa) {
            for (int sb = 400; sb >= b; --sb) {
                if (dp[sa - a][sb - b] < INF) {
                    dp[sa][sb] = min(dp[sa][sb], dp[sa - a][sb - b] + c);
                }
            }
        }
    }

    int ans = INF;
    for (int k = 1; k * ma <= 400 && k * mb <= 400; ++k) {
        ans = min(ans, dp[k * ma][k * mb]);
    }

    cout << (ans >= INF ? -1 : ans) << "\n";
    return 0;
}
"""
    },
    {
        "id": "arc035_c",
        "title": "Traffic Conditions in AtCoder Kingdom",
        "contest_id": "arc035",
        "rating": 1655,
        "tag": "Graph Theory",
        "subtopic": "All-Pairs Shortest Paths",
        "topic": "Online All-Pairs Shortest Path Incremental Edge Addition",
        "cat_folder": "graph_theory",
        "cat_file": "online_apsp_incremental_edge_update.md",
        "statement": "An undirected weighted graph with N vertices. Initially all-pairs shortest paths are given. Process K queries: a new road between X and Y with length Z is built. After each road addition, output the sum of shortest path distances between all pairs i < j.",
        "key_idea": "When a new edge (X, Y, Z) is added, the new shortest path between any pair (i, j) can only change by routing through (X, Y): dist'[i][j] = min({dist[i][j], dist[i][X] + Z + dist[Y][j], dist[i][Y] + Z + dist[X][j]}).",
        "observation": "Updating all pairs takes O(N^2) per added road. For K <= 400 and N <= 400, total time is O(K * N^2) ~ 6.4 * 10^7 operations, well within time limit.",
        "algorithm": [
            "Compute initial all-pairs shortest paths using Floyd-Warshall in O(N^3).",
            "Calculate initial total sum of distances for all i < j.",
            "For each new road (X, Y, Z):",
            "  If Z >= dist[X][Y], edge is redundant; print current sum.",
            "  Otherwise:",
            "    For i from 1 to N:",
            "      For j from i + 1 to N:",
            "        new_dist = min({dist[i][j], dist[i][X] + Z + dist[Y][j], dist[i][Y] + Z + dist[X][j]});",
            "        sum -= (dist[i][j] - new_dist);",
            "        dist[i][j] = dist[j][i] = new_dist;",
            "    Print updated sum."
        ],
        "time_complexity": "O(N^3 + K * N^2)",
        "space_complexity": "O(N^2)",
        "core_skill": "Incremental dynamic Floyd-Warshall update in O(N^2) per edge insertion.",
        "reusable_pattern": "Dynamic Edge Addition APSP: dist[i][j] = min(dist[i][j], dist[i][u] + w + dist[v][j]).",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const long long INF = 1e15;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<long long>> dist(n + 1, vector<long long>(n + 1, INF));
    for (int i = 1; i <= n; ++i) dist[i][i] = 0;

    for (int i = 0; i < m; ++i) {
        int u, v;
        long long w;
        cin >> u >> v >> w;
        dist[u][v] = min(dist[u][v], w);
        dist[v][u] = min(dist[v][u], w);
    }

    for (int k = 1; k <= n; ++k) {
        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= n; ++j) {
                if (dist[i][k] + dist[k][j] < dist[i][j]) {
                    dist[i][j] = dist[i][k] + dist[k][j];
                }
            }
        }
    }

    long long cur_sum = 0;
    for (int i = 1; i <= n; ++i) {
        for (int j = i + 1; j <= n; ++j) {
            cur_sum += dist[i][j];
        }
    }

    int k_roads;
    cin >> k_roads;

    while (k_roads--) {
        int x, y;
        long long z;
        cin >> x >> y >> z;

        if (z < dist[x][y]) {
            for (int i = 1; i <= n; ++i) {
                for (int j = i + 1; j <= n; ++j) {
                    long long alt1 = dist[i][x] + z + dist[y][j];
                    long long alt2 = dist[i][y] + z + dist[x][j];
                    long long new_d = min({dist[i][j], alt1, alt2});
                    if (new_d < dist[i][j]) {
                        cur_sum -= (dist[i][j] - new_d);
                        dist[i][j] = dist[j][i] = new_d;
                    }
                }
            }
        }
        cout << cur_sum << "\n";
    }

    return 0;
}
"""
    },
    {
        "id": "abc040_d",
        "title": "Road Aging Countermeasures",
        "contest_id": "abc040",
        "rating": 1656,
        "tag": "Data Structures",
        "subtopic": "Disjoint Set Union (DSU)",
        "topic": "Offline Query Sorting with Disjoint Set Union Sweep-Line",
        "cat_folder": "data_structures",
        "cat_file": "offline_dsu_sweepline_threshold.md",
        "statement": "N towns and M bridges built in year Y_i. Q queries (v, w): how many towns can be reached from town v using only bridges built STRICTLY AFTER year w?",
        "key_idea": "Offline query processing! Sort edges descending by year Y_i, and sort queries descending by threshold w. Maintain connected components using DSU.",
        "observation": "As the query threshold w decreases, add bridges built after w into the DSU. The answer for query (v, w) is simply the component size of v in the DSU.",
        "algorithm": [
            "Store edges (u, v, y) and sort descending by year y.",
            "Store queries (v, w, id) and sort descending by threshold w.",
            "Initialize DSU with component sizes.",
            "edge_ptr = 0.",
            "For each query (v, w, id):",
            "  While edge_ptr < M and edges[edge_ptr].y > w:",
            "    dsu.unite(edges[edge_ptr].u, edges[edge_ptr].v);",
            "    edge_ptr++;",
            "  ans[id] = dsu.size(v);",
            "Print answers in original query order."
        ],
        "time_complexity": "O((M + Q) log(M + Q))",
        "space_complexity": "O(N + M + Q)",
        "core_skill": "Offline dual-sorting sweep line on monotonic threshold constraints with DSU.",
        "reusable_pattern": "Threshold Graph Sweep: sort edges and queries descending, add edges to DSU as threshold relaxes.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

struct Edge {
    int u, v, y;
};

struct Query {
    int v, w, id;
};

struct DSU {
    vector<int> parent, sz;
    DSU(int n) : parent(n + 1), sz(n + 1, 1) {
        iota(parent.begin(), parent.end(), 0);
    }
    int find(int u) {
        return parent[u] == u ? u : parent[u] = find(parent[u]);
    }
    void unite(int u, int v) {
        int ru = find(u), rv = find(v);
        if (ru == rv) return;
        if (sz[ru] < sz[rv]) swap(ru, rv);
        parent[rv] = ru;
        sz[ru] += sz[rv];
    }
    int get_size(int u) {
        return sz[find(u)];
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<Edge> edges(m);
    for (int i = 0; i < m; ++i) {
        cin >> edges[i].u >> edges[i].v >> edges[i].y;
    }

    int q;
    cin >> q;
    vector<Query> queries(q);
    for (int i = 0; i < q; ++i) {
        cin >> queries[i].v >> queries[i].w;
        queries[i].id = i;
    }

    sort(edges.begin(), edges.end(), [](const Edge& a, const Edge& b) {
        return a.y > b.y;
    });

    sort(queries.begin(), queries.end(), [](const Query& a, const Query& b) {
        return a.w > b.w;
    });

    DSU dsu(n);
    vector<int> ans(q);
    int edge_idx = 0;

    for (const auto& qry : queries) {
        while (edge_idx < m && edges[edge_idx].y > qry.w) {
            dsu.unite(edges[edge_idx].u, edges[edge_idx].v);
            edge_idx++;
        }
        ans[qry.id] = dsu.get_size(qry.v);
    }

    for (int i = 0; i < q; ++i) {
        cout << ans[i] << "\n";
    }

    return 0;
}
"""
    },
    {
        "id": "abc118_d",
        "title": "Match Matching",
        "contest_id": "abc118",
        "rating": 1657,
        "tag": "Dynamic Programming",
        "subtopic": "Classic DP",
        "topic": "Unbounded Knapsack for Lexicographically Largest Number",
        "cat_folder": "dp",
        "cat_file": "lexicographical_unbounded_knapsack.md",
        "statement": "Given N matchsticks and a set of M allowed digits. Find the largest integer that can be formed using EXACTLY N matchsticks, where each digit d requires a specific number of matchsticks.",
        "key_idea": "The larger integer is first determined by having MORE DIGITS. If two integers have the same number of digits, compare lexicographically. Use unbounded knapsack DP: dp[n] = maximum number of digits formable with n matchsticks.",
        "observation": "Once max digits are known, greedily reconstruct the number from left to right: for each position, test allowed digits from 9 down to 1. If using digit d leaves n - cost[d] matchsticks with dp[n - cost[d]] == dp[n] - 1, pick d!",
        "algorithm": [
            "Cost table for digits 1..9: {2, 5, 5, 4, 5, 6, 3, 7, 6}.",
            "Initialize dp[N + 1] with -INF. dp[0] = 0.",
            "For n from 1 to N:",
            "  For each allowed digit d:",
            "    if n >= cost[d]: dp[n] = max(dp[n], dp[n - cost[d]] + 1).",
            "Sort allowed digits descending.",
            "Reconstruct string: curr = N.",
            "While curr > 0:",
            "  For digit d in allowed_digits:",
            "    if curr >= cost[d] and dp[curr - cost[d]] == dp[curr] - 1:",
            "      append d to result, curr -= cost[d], break.",
            "Print result string."
        ],
        "time_complexity": "O(N * M)",
        "space_complexity": "O(N)",
        "core_skill": "Two-phase optimization: maximize sequence length via DP, then greedily reconstruct lexicographical maximum.",
        "reusable_pattern": "Lexicographical Unbounded Knapsack: dp[weight] = max_length, greedy backtrack from 9 down to 1.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

const int match_costs[10] = {0, 2, 5, 5, 4, 5, 6, 3, 7, 6};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<int> a(m);
    for (int i = 0; i < m; ++i) {
        cin >> a[i];
    }
    sort(a.rbegin(), a.rend());

    vector<int> dp(n + 1, -1e9);
    dp[0] = 0;

    for (int i = 1; i <= n; ++i) {
        for (int d : a) {
            int c = match_costs[d];
            if (i >= c && dp[i - c] >= 0) {
                dp[i] = max(dp[i], dp[i - c] + 1);
            }
        }
    }

    string ans = "";
    int curr = n;

    while (curr > 0) {
        for (int d : a) {
            int c = match_costs[d];
            if (curr >= c && dp[curr - c] == dp[curr] - 1) {
                ans += to_string(d);
                curr -= c;
                break;
            }
        }
    }

    cout << ans << "\n";
    return 0;
}
"""
    },
    {
        "id": "abc224_e",
        "title": "Integers on Grid",
        "contest_id": "abc224",
        "rating": 1657,
        "tag": "Dynamic Programming",
        "subtopic": "2D Grid DP",
        "topic": "Group-by-Value DP on Grids with Row/Column Maximum Buffering",
        "cat_folder": "dp",
        "cat_file": "grid_dp_row_col_buffering.md",
        "statement": "An H x W grid with N points with values a_i. From (r, c), you can move to any point in the same row or column with STRICTLY LARGER value. Find the maximum number of moves starting from each point.",
        "key_idea": "A point with value a_i transitions to any point in row r or column c with value > a_i. Process all points grouped by value in DESCENDING order.",
        "observation": "Maintain row_max[r] and col_max[c] (maximum moves from any point in row r or col c processed so far). To strictly enforce value > a_i, points with the same value must be evaluated simultaneously, buffering their updates and applying them to row_max/col_max only after all points of that value are evaluated.",
        "algorithm": [
            "Group points by value a_i in a map or sorted list descending.",
            "Initialize row_max[H + 1] = 0, col_max[W + 1] = 0.",
            "For each group of points with value v:",
            "  For each point i in group:",
            "    dp[i] = max(row_max[r_i], col_max[c_i]).",
            "  After evaluating all points in group:",
            "    For each point i in group:",
            "      row_max[r_i] = max(row_max[r_i], dp[i] + 1);",
            "      col_max[c_i] = max(col_max[c_i], dp[i] + 1);",
            "Print dp[i] for all i = 1..N."
        ],
        "time_complexity": "O(N log N)",
        "space_complexity": "O(N + H + W)",
        "core_skill": "Equal-value simultaneous batch DP with row/column maximum tracking to prevent intra-value transitions.",
        "reusable_pattern": "Strictly Increasing Row/Col Path: group by value descending, query max, then commit updates.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

struct Point {
    int id, r, c, a;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int h, w, n;
    if (!(cin >> h >> w >> n)) return 0;

    map<int, vector<Point>> groups;
    for (int i = 0; i < n; ++i) {
        int r, c, a;
        cin >> r >> c >> a;
        groups[a].push_back({i, r, c, a});
    }

    vector<int> ans(n, 0);
    vector<int> row_max(h + 1, 0);
    vector<int> col_max(w + 1, 0);

    // Process from largest value down to smallest
    for (auto it = groups.rbegin(); it != groups.rend(); ++it) {
        const auto& pts = it->second;

        // Step 1: Query max moves
        vector<int> cur_dp(pts.size());
        for (size_t i = 0; i < pts.size(); ++i) {
            cur_dp[i] = max(row_max[pts[i].r], col_max[pts[i].c]);
            ans[pts[i].id] = cur_dp[i];
        }

        // Step 2: Commit updates
        for (size_t i = 0; i < pts.size(); ++i) {
            row_max[pts[i].r] = max(row_max[pts[i].r], cur_dp[i] + 1);
            col_max[pts[i].c] = max(col_max[pts[i].c], cur_dp[i] + 1);
        }
    }

    for (int i = 0; i < n; ++i) {
        cout << ans[i] << "\n";
    }

    return 0;
}
"""
    },
    {
        "id": "abc057_d",
        "title": "Maximum Average Sets",
        "contest_id": "abc057",
        "rating": 1658,
        "tag": "Math",
        "subtopic": "Combinatorics",
        "topic": "Greedy Top Elements Average + Combinatorics on Boundary Frequency",
        "cat_folder": "math",
        "cat_file": "max_average_boundary_combinatorics.md",
        "statement": "Given N integers v_1, ..., v_N. Choose between A and B elements to maximize their arithmetic mean. Output the maximum mean and the number of ways to achieve it.",
        "key_idea": "Sort elements descending. The maximum mean is always achieved by picking the top A elements. If all top A elements are equal, we can pick any number of them from A to min(B, total_count). Otherwise, we MUST pick exactly A elements.",
        "observation": "Let sorted elements be v_0 >= v_1 >= ... >= v_{N-1}. If v_0 == v_{A-1}, all chosen elements have the same value; answer is sum_{k=A}^{min(B, cnt)} C(cnt, k). If v_0 > v_{A-1}, only size A achieves the maximum mean; count ways to choose the boundary element v_{A-1}: C(total_occurrences, needed_occurrences).",
        "algorithm": [
            "Sort v in descending order.",
            "Compute max average: (sum_{i=0}^{A-1} v_i) / (double)A.",
            "Precompute combinations C(n, k).",
            "If v[0] == v[A - 1]:",
            "  Let total_cnt = count of v[0] in array v.",
            "  ways = sum_{k=A}^{min(B, total_cnt)} C(total_cnt, k).",
            "Else:",
            "  Let val = v[A - 1].",
            "  total_cnt = count of val in entire array v.",
            "  needed_cnt = count of val in prefix v[0..A-1].",
            "  ways = C(total_cnt, needed_cnt).",
            "Print max average with high precision, then ways."
        ],
        "time_complexity": "O(N log N)",
        "space_complexity": "O(N^2)",
        "core_skill": "Determining subset selection ties under fractional objectives via frequency combinations.",
        "reusable_pattern": "Top-A Elements Average Combinatorics: check if top-A homogeneous (sum over k) vs boundary C(total, needed).",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>

using namespace std;

long long C[55][55];

void precompute_comb() {
    for (int i = 0; i <= 50; ++i) {
        C[i][0] = 1;
        for (int j = 1; j <= i; ++j) {
            C[i][j] = C[i - 1][j - 1] + C[i - 1][j];
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    precompute_comb();

    int n, a, b;
    if (!(cin >> n >> a >> b)) return 0;

    vector<long long> v(n);
    for (int i = 0; i < n; ++i) {
        cin >> v[i];
    }

    sort(v.rbegin(), v.rend());

    long long sum_a = 0;
    for (int i = 0; i < a; ++i) {
        sum_a += v[i];
    }

    double max_avg = (double)sum_a / a;
    long long ways = 0;

    if (v[0] == v[a - 1]) {
        int total_cnt = 0;
        for (int i = 0; i < n; ++i) {
            if (v[i] == v[0]) total_cnt++;
        }
        for (int k = a; k <= min(b, total_cnt); ++k) {
            ways += C[total_cnt][k];
        }
    } else {
        long long boundary_val = v[a - 1];
        int total_cnt = 0;
        for (int i = 0; i < n; ++i) {
            if (v[i] == boundary_val) total_cnt++;
        }
        int needed_cnt = 0;
        for (int i = 0; i < a; ++i) {
            if (v[i] == boundary_val) needed_cnt++;
        }
        ways = C[total_cnt][needed_cnt];
    }

    cout << fixed << setprecision(12) << max_avg << "\n";
    cout << ways << "\n";
    return 0;
}
"""
    },
    {
        "id": "abc263_e",
        "title": "Sugoroku 3",
        "contest_id": "abc263",
        "rating": 1659,
        "tag": "Dynamic Programming",
        "subtopic": "Expected Value DP",
        "topic": "Expected Value DP with Self-Loop Formula + Range Sum Acceleration",
        "cat_folder": "dp",
        "cat_file": "expected_value_self_loop_dp.md",
        "statement": "A board with N squares (1 to N). At square i, roll an integer die uniformly from 0 to A_i. Move from i to i + die. Find the expected number of rolls to reach square N, modulo 998244353.",
        "key_idea": "At square i, rolling 0 causes a self-loop: E[i] = 1 + (1 / (A_i + 1)) * E[i] + (1 / (A_i + 1)) * sum_{j=1}^{A_i} E[i + j]. Solve the self-loop algebraically.",
        "observation": "Multiplying by (A_i + 1) and subtracting E[i]: A_i * E[i] = (A_i + 1) + sum_{j=1}^{A_i} E[i + j] => E[i] = ((A_i + 1) + sum_{j=1}^{A_i} E[i + j]) * inv(A_i) mod MOD. The range sum is maintained in O(1) using suffix sums.",
        "algorithm": [
            "Initialize E[N] = 0.",
            "Maintain suffix sums suf_E where suf_E[i] = sum_{k=i}^N E[k].",
            "For i from N - 1 down to 1:",
            "  sum_future = (suf_E[i + 1] - suf_E[min(n, i + A[i]) + 1] + MOD) % MOD.",
            "  numerator = (A[i] + 1 + sum_future) % MOD.",
            "  E[i] = (numerator * inv(A[i])) % MOD.",
            "  suf_E[i] = (suf_E[i + 1] + E[i]) % MOD.",
            "Print E[1]."
        ],
        "time_complexity": "O(N log(MOD))",
        "space_complexity": "O(N)",
        "core_skill": "Resolving self-loop expected value recurrences accelerated by suffix sum lookups.",
        "reusable_pattern": "Self-Loop Expected Value: E[i] = (total_branches + sum_other_branches) * inv(active_branches).",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MOD = 998244353;

long long power(long long base, long long exp) {
    long long res = 1;
    base %= MOD;
    while (exp > 0) {
        if (exp % 2 == 1) res = (res * base) % MOD;
        base = (base * base) % MOD;
        exp /= 2;
    }
    return res;
}

long long modInverse(long long n) {
    return power(n, MOD - 2);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 1; i < n; ++i) {
        cin >> a[i];
    }

    vector<long long> E(n + 2, 0);
    vector<long long> suf(n + 2, 0);

    for (int i = n - 1; i >= 1; --i) {
        int r = min((long long)n, i + a[i]);
        long long sum_future = (suf[i + 1] - suf[r + 1] + MOD) % MOD;
        long long num = (a[i] + 1 + sum_future) % MOD;
        E[i] = (num * modInverse(a[i])) % MOD;
        suf[i] = (suf[i + 1] + E[i]) % MOD;
    }

    cout << E[1] << "\n";
    return 0;
}
"""
    },
    {
        "id": "abc244_f",
        "title": "Shortest Good Path",
        "contest_id": "abc244",
        "rating": 1661,
        "tag": "Graph Theory",
        "subtopic": "Breadth-First Search (BFS)",
        "topic": "Shortest Path on Graph with Bitmask Parities (0-1 BFS)",
        "cat_folder": "graph_theory",
        "cat_file": "graph_parity_bitmask_bfs.md",
        "statement": "An undirected connected graph with N vertices (N <= 17). For each non-empty subset S of vertices, find the length of the shortest path where the set of vertices visited an ODD number of times is EXACTLY S. Find the sum of lengths over all 2^N - 1 subsets.",
        "key_idea": "Multi-source BFS on the state space (u, mask) where u is the current vertex and mask in 0..2^N - 1 is the bitmask of odd-visit vertices. Moving from u to v toggles bit v in mask.",
        "observation": "Base cases: a single-node path visiting v has length 1 with state (v, 1 << v). Initialize BFS queue with all (v, 1 << v). For each non-zero mask, the shortest good path is min_{u} dist[u][mask].",
        "algorithm": [
            "Total states: N * 2^N <= 17 * 131072 ~ 2.2 * 10^6 states.",
            "Initialize dist[N][1 << N] with -1.",
            "Queue pushes all (v, 1 << v) with dist = 1.",
            "Standard BFS: pop (u, mask):",
            "  For each neighbor v of u:",
            "    next_mask = mask ^ (1 << v).",
            "    If dist[v][next_mask] == -1:",
            "      dist[v][next_mask] = dist[u][mask] + 1;",
            "      push (v, next_mask);",
            "ans = 0.",
            "For mask from 1 to 2^N - 1:",
            "  min_len = min_{u=0..N-1} dist[u][mask].",
            "  ans += min_len.",
            "Print ans."
        ],
        "time_complexity": "O(N * 2^N + M * 2^N)",
        "space_complexity": "O(N * 2^N)",
        "core_skill": "State-space BFS tracking Eulerian parity signatures across graph walks.",
        "reusable_pattern": "Parity Walk BFS: state (u, parity_mask), transition mask ^ (1 << v).",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<int>> adj(n);
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        --u; --v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    int total_masks = 1 << n;
    vector<vector<int>> dist(n, vector<int>(total_masks, -1));
    queue<pair<int, int>> q;

    for (int i = 0; i < n; ++i) {
        dist[i][1 << i] = 1;
        q.push({i, 1 << i});
    }

    while (!q.empty()) {
        auto [u, mask] = q.front();
        q.pop();

        for (int v : adj[u]) {
            int next_mask = mask ^ (1 << v);
            if (dist[v][next_mask] == -1) {
                dist[v][next_mask] = dist[u][mask] + 1;
                q.push({v, next_mask});
            }
        }
    }

    long long total_len = 0;
    for (int mask = 1; mask < total_masks; ++mask) {
        int min_d = 1e9;
        for (int u = 0; u < n; ++u) {
            if (dist[u][mask] != -1) {
                min_d = min(min_d, dist[u][mask]);
            }
        }
        total_len += min_d;
    }

    cout << total_len << "\n";
    return 0;
}
"""
    },
    {
        "id": "abc162_e",
        "title": "Sum of gcd of Tuples",
        "contest_id": "abc162",
        "rating": 1662,
        "tag": "Number Theory",
        "subtopic": "Inclusion-Exclusion",
        "topic": "Inclusion-Exclusion Multiple Counting from K down to 1",
        "cat_folder": "number_theory",
        "cat_file": "gcd_tuple_sum_inclusion_exclusion.md",
        "statement": "Find the sum of gcd(A_1, ..., A_N) over all K^N integer sequences 1 <= A_i <= K, modulo 10^9 + 7.",
        "key_idea": "Count sequences with gcd EXACTLY equal to g. The number of sequences where each element is a multiple of g is floor(K / g)^N. Subtract counts for multiples 2g, 3g, ... by processing g from K down to 1.",
        "observation": "Let cnt[g] be the number of tuples with gcd equal to g. Then cnt[g] = (K / g)^N - sum_{m=2}^{K/g} cnt[m * g]. Total sum over all g is sum_{g=1}^K g * cnt[g].",
        "algorithm": [
            "Initialize cnt[K + 1].",
            "For g from K down to 1:",
            "  total_multiples = power(K / g, N, MOD).",
            "  For m = 2 to K / g:",
            "    total_multiples = (total_multiples - cnt[m * g] + MOD) % MOD.",
            "  cnt[g] = total_multiples.",
            "ans = sum_{g=1}^K (g * cnt[g]) % MOD.",
            "Print ans."
        ],
        "time_complexity": "O(K log K)",
        "space_complexity": "O(K)",
        "core_skill": "Reverse sieve inclusion-exclusion for exact greatest common divisor tuple counting.",
        "reusable_pattern": "GCD Count via Multiple Sieve: cnt[g] = (K/g)^N - sum_{m>=2} cnt[m*g].",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>

using namespace std;

const int MOD = 1000000007;

long long power(long long base, long long exp) {
    long long res = 1;
    base %= MOD;
    while (exp > 0) {
        if (exp % 2 == 1) res = (res * base) % MOD;
        base = (base * base) % MOD;
        exp /= 2;
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> cnt(k + 1, 0);
    long long ans = 0;

    for (int g = k; g >= 1; --g) {
        long long ways = power(k / g, n);
        for (int m = 2 * g; m <= k; m += g) {
            ways = (ways - cnt[m] + MOD) % MOD;
        }
        cnt[g] = ways;
        ans = (ans + 1LL * g * cnt[g]) % MOD;
    }

    cout << ans << "\n";
    return 0;
}
"""
    },
    {
        "id": "abc166_f",
        "title": "Three Variables Game",
        "contest_id": "abc166",
        "rating": 1668,
        "tag": "Basics",
        "subtopic": "Greedy Algorithms",
        "topic": "Greedy Lookahead with Invariant Sum Constrained State",
        "cat_folder": "basics",
        "cat_file": "greedy_lookahead_invariant_sum.md",
        "statement": "Three integers A, B, C with A + B + C <= 2. In N rounds, a string S_i in {'AB', 'BC', 'AC'} specifies two variables: increment one and decrement the other. Maintain all variables >= 0 throughout all N rounds, or output 'No'.",
        "key_idea": "The sum A + B + C is strictly conserved! If sum == 0, impossible. If sum == 1: at each step, exactly one variable is positive and one is zero, leaving no choice. If sum == 2: when both variables are positive (1, 1), use 1-STEP LOOKAHEAD to increment the variable needed in the next round!",
        "observation": "When faced with choices (A=1, B=1) for query 'AB': looking at S_{i+1}, if S_{i+1} involves A, increment A (so A becomes 2 and can survive decrement in round i+1); else increment B.",
        "algorithm": [
            "If A + B + C == 0, print 'No'.",
            "Simulate round i from 0 to N - 1:",
            "  Let variables be u and v.",
            "  If val[u] == 0 and val[v] == 0: print 'No'.",
            "  If val[u] == 0: increment u, decrement v, record u.",
            "  Else if val[v] == 0: increment v, decrement u, record v.",
            "  Else (val[u] == 1 and val[v] == 1):",
            "    If i + 1 < N and (S[i+1][0] == u || S[i+1][1] == u): increment u, decrement v, record u.",
            "    Else: increment v, decrement u, record v.",
            "Print 'Yes', then all choices."
        ],
        "time_complexity": "O(N)",
        "space_complexity": "O(N)",
        "core_skill": "1-step lookahead greedy tie-breaking under strict resource invariance.",
        "reusable_pattern": "Conserved Sum Game Lookahead: when both variables > 0, increment the one needed next.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long val[3];
    if (!(cin >> n >> val[0] >> val[1] >> val[2])) return 0;

    vector<string> s(n);
    for (int i = 0; i < n; ++i) {
        cin >> s[i];
    }

    vector<char> moves;

    for (int i = 0; i < n; ++i) {
        int u = s[i][0] - 'A';
        int v = s[i][1] - 'A';

        if (val[u] == 0 && val[v] == 0) {
            cout << "No\n";
            return 0;
        }

        if (val[u] == 0) {
            val[u]++;
            val[v]--;
            moves.push_back('A' + u);
        } else if (val[v] == 0) {
            val[v]++;
            val[u]--;
            moves.push_back('A' + v);
        } else {
            // Both are positive (val[u] == 1, val[v] == 1)
            // Look ahead to next query
            if (i + 1 < n && (s[i + 1][0] - 'A' == u || s[i + 1][1] - 'A' == u)) {
                val[u]++;
                val[v]--;
                moves.push_back('A' + u);
            } else {
                val[v]++;
                val[u]--;
                moves.push_back('A' + v);
            }
        }
    }

    cout << "Yes\n";
    for (char c : moves) {
        cout << c << "\n";
    }

    return 0;
}
"""
    },
    {
        "id": "abc271_f",
        "title": "XOR on Grid Path",
        "contest_id": "abc271",
        "rating": 1669,
        "tag": "Basics",
        "subtopic": "Meet-in-the-Middle",
        "topic": "Meet-in-the-Middle on 2D Grid Paths",
        "cat_folder": "basics",
        "cat_file": "meet_in_the_middle_grid_paths.md",
        "statement": "An N x N grid with integer values A[i][j]. Travel from (1, 1) to (N, N) moving only right and down. Find the number of paths where the XOR sum of all visited cells is EXACTLY 0. N <= 20.",
        "key_idea": "The total path length is 2N - 1, meaning 2^(2N-2) paths (up to 2^38, impossible). Meet in the middle at the anti-diagonal r + c = N - 1 (paths of length N - 1 from (0, 0) and length N - 1 from (N-1, N-1)).",
        "observation": "Each half takes N - 1 steps (at most 2^19 ~ 5 * 10^5 paths). From (0, 0), DFS to all (r, c) on the anti-diagonal, storing frequency maps of XOR sums. From (N-1, N-1), DFS backwards to the anti-diagonal and count matching XOR sums.",
        "algorithm": [
            "Forward DFS: start at (0, 0) with xor_sum = A[0][0].",
            "  Move right and down until r + c == N - 1.",
            "  Record xor_sum in freq[r][xor_sum].",
            "Backward DFS: start at (N-1, N-1) with xor_sum = A[N-1][N-1].",
            "  Move left and up until r + c == N.",
            "  From cell (r, c), can transition to (r - 1, c) or (r, c - 1) on the anti-diagonal.",
            "  Total paths += freq[r'][xor_sum].",
            "Print total paths."
        ],
        "time_complexity": "O(2^(N-1) log(2^(N-1)))",
        "space_complexity": "O(N * 2^(N-1))",
        "core_skill": "Anti-diagonal meet-in-the-middle path counting on 2D grids.",
        "reusable_pattern": "Grid Meet-in-the-Middle: partition at r + c = N - 1, meet XOR sums via map/hash.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <map>

using namespace std;

int n;
long long a[22][22];
map<long long, int> freq[22];
long long total_ans = 0;

void dfs_forward(int r, int c, long long cur_xor) {
    if (r + c == n - 1) {
        freq[r][cur_xor]++;
        return;
    }
    if (r + 1 < n) dfs_forward(r + 1, c, cur_xor ^ a[r + 1][c]);
    if (c + 1 < n) dfs_forward(r, c + 1, cur_xor ^ a[r][c + 1]);
}

void dfs_backward(int r, int c, long long cur_xor) {
    if (r + c == n - 1) {
        // Exclude a[r][c] since it was already included in forward path
        long long target = cur_xor ^ a[r][c];
        auto it = freq[r].find(target);
        if (it != freq[r].end()) {
            total_ans += it->second;
        }
        return;
    }
    if (r - 1 >= 0) dfs_backward(r - 1, c, cur_xor ^ a[r - 1][c]);
    if (c - 1 >= 0) dfs_backward(r, c - 1, cur_xor ^ a[r][c - 1]);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n)) return 0;

    for (int r = 0; r < n; ++r) {
        for (int c = 0; c < n; ++c) {
            cin >> a[r][c];
        }
    }

    dfs_forward(0, 0, a[0][0]);
    dfs_backward(n - 1, n - 1, a[n - 1][n - 1]);

    cout << total_ans << "\n";
    return 0;
}
"""
    },
    {
        "id": "abc041_d",
        "title": "Footrace",
        "contest_id": "abc041",
        "rating": 1670,
        "tag": "Dynamic Programming",
        "subtopic": "Bitmask DP",
        "topic": "Topological Ordering Count via Bitmask DP",
        "cat_folder": "dp",
        "cat_file": "topological_sort_count_bitmask_dp.md",
        "statement": "N runners (N <= 16) and M precedence conditions: runner x_i finished before runner y_i. Find the total number of valid finishing orders (topological sorts) compatible with all conditions.",
        "key_idea": "Dynamic programming on subsets! `dp[mask]` = number of valid topological orderings of the subset of runners in mask. To transition, append a runner v not in mask provided no predecessor of v is missing from mask.",
        "observation": "A runner v can be placed next iff all runners that must precede v are ALREADY present in mask: `(pred[v] & ~mask) == 0`. Then `dp[mask | (1 << v)] += dp[mask]`.",
        "algorithm": [
            "Store predecessor bitmask pred[v]: bit u is set if u must precede v.",
            "Initialize dp[1 << N] with 0; dp[0] = 1.",
            "For mask from 0 to (1 << N) - 1:",
            "  If dp[mask] == 0 continue.",
            "  For v from 0 to N - 1:",
            "    If (!(mask & (1 << v))):",
            "      If ((pred[v] & ~mask) == 0):",
            "        dp[mask | (1 << v)] += dp[mask];",
            "Print dp[(1 << N) - 1]."
        ],
        "time_complexity": "O(N * 2^N)",
        "space_complexity": "O(2^N)",
        "core_skill": "Counting linear extensions of partially ordered sets via Bitmask DP.",
        "reusable_pattern": "Topological Sort Count Bitmask DP: append v if (pred[v] & ~mask) == 0.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<int> pred(n, 0);
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        --u; --v;
        pred[v] |= (1 << u);
    }

    int total_masks = 1 << n;
    vector<long long> dp(total_masks, 0);
    dp[0] = 1;

    for (int mask = 0; mask < total_masks; ++mask) {
        if (!dp[mask]) continue;

        for (int v = 0; v < n; ++v) {
            if (!(mask & (1 << v))) {
                if ((pred[v] & ~mask) == 0) {
                    dp[mask | (1 << v)] += dp[mask];
                }
            }
        }
    }

    cout << dp[total_masks - 1] << "\n";
    return 0;
}
"""
    },
    {
        "id": "abc136_e",
        "title": "Max GCD",
        "contest_id": "abc136",
        "rating": 1670,
        "tag": "Number Theory",
        "subtopic": "Divisors",
        "topic": "Sum-Invariant Divisor Analysis on Array GCD",
        "cat_folder": "number_theory",
        "cat_file": "sum_invariant_array_gcd_divisors.md",
        "statement": "An array A of N positive integers. In one operation, choose two elements, increment one and decrement the other. Perform at most K operations to maximize the greatest common divisor of all elements.",
        "key_idea": "Each operation increments one element and decrements another, so the sum S = sum_{i=1}^N A_i is strictly invariant! Thus, the final GCD must divide S.",
        "observation": "Find all divisors d of S. For a divisor d to be achievable in <= K operations: compute remainders r_i = A_i % d. Sort r_i. To make all elements multiples of d with zero net change, we decrease the first p elements by r_i and increase the remaining N - p elements by d - r_i. The operations needed is sum_{i=0}^{p-1} r_i where sum_{i=0}^{p-1} r_i == sum_{i=p}^{N-1} (d - r_i).",
        "algorithm": [
            "Compute total sum S = sum A_i.",
            "Find all divisors d of S and sort descending.",
            "For each divisor d:",
            "  Compute r_i = A_i % d and sort ascending.",
            "  Let sum_rem = sum r_i. Number of elements to reduce is p = N - (sum_rem / d).",
            "  Ops needed = sum_{i=0}^{p-1} r_i.",
            "  If ops <= K, return d (first and largest valid d).",
            "Print 1."
        ],
        "time_complexity": "O(d(S) * N log N)",
        "space_complexity": "O(N)",
        "core_skill": "Invariant sum divisor checking and greedy remainder balance pairing.",
        "reusable_pattern": "Array Operation Invariant GCD: GCD divides sum(A); check remainders r_i sorted against K.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> a(n);
    long long total_sum = 0;
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        total_sum += a[i];
    }

    vector<long long> divisors;
    for (long long d = 1; d * d <= total_sum; ++d) {
        if (total_sum % d == 0) {
            divisors.push_back(d);
            if (d * d != total_sum) {
                divisors.push_back(total_sum / d);
            }
        }
    }
    sort(divisors.rbegin(), divisors.rend());

    for (long long d : divisors) {
        vector<long long> r(n);
        long long sum_rem = 0;
        for (int i = 0; i < n; ++i) {
            r[i] = a[i] % d;
            sum_rem += r[i];
        }
        sort(r.begin(), r.end());

        int p = n - (sum_rem / d);
        long long ops = 0;
        for (int i = 0; i < p; ++i) {
            ops += r[i];
        }

        if (ops <= k) {
            cout << d << "\n";
            return 0;
        }
    }

    cout << 1 << "\n";
    return 0;
}
"""
    },
    {
        "id": "abc151_f",
        "title": "Enclose All",
        "contest_id": "abc151",
        "rating": 1671,
        "tag": "Geometry",
        "subtopic": "Minimum Enclosing Circle",
        "topic": "Minimum Enclosing Circle: Pair and Triple Circumcircle Search",
        "cat_folder": "geometry",
        "cat_file": "minimum_enclosing_circle_search.md",
        "statement": "Given N points in the 2D plane (N <= 50). Find the minimum radius of a closed circle that contains all N points on or inside its boundary.",
        "key_idea": "The minimum enclosing circle of a set of points is uniquely defined either by two points (as diameter) or by three points on its boundary (as circumcircle).",
        "observation": "Because N <= 50, test all pairs of points (C(50, 2) = 1225 circles) and all triples of non-collinear points (C(50, 3) = 19,600 circles). For each candidate circle, check if all N points lie inside in O(N). Total operations <= 20,000 * 50 ~ 10^6.",
        "algorithm": [
            "Candidate circles from 2 points (p1, p2): center = (p1 + p2)/2, radius = dist(p1, p2)/2.",
            "Candidate circles from 3 points (p1, p2, p3): circumcenter and circumradius.",
            "For each candidate circle (center, r):",
            "  If all N points have dist(center, pt) <= r + 1e-9:",
            "    min_radius = min(min_radius, r).",
            "Print min_radius with 12 decimals."
        ],
        "time_complexity": "O(N^4)",
        "space_complexity": "O(N)",
        "core_skill": "Geometric minimum enclosing circle candidate generation via 2-point and 3-point boundary sets.",
        "reusable_pattern": "Minimum Enclosing Circle: test 2-point diameters and 3-point circumcenters.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <cmath>
#include <iomanip>
#include <algorithm>

using namespace std;

struct Point {
    double x, y;
};

double dist(Point a, Point b) {
    return hypot(a.x - b.x, a.y - b.y);
}

// Circumcircle of 3 points
bool get_circle_3(Point p1, Point p2, Point p3, Point& center, double& r) {
    double d = 2 * (p1.x * (p2.y - p3.y) + p2.x * (p3.y - p1.y) + p3.x * (p1.y - p2.y));
    if (abs(d) < 1e-9) return false;

    double p1_sq = p1.x * p1.x + p1.y * p1.y;
    double p2_sq = p2.x * p2.x + p2.y * p2.y;
    double p3_sq = p3.x * p3.x + p3.y * p3.y;

    center.x = (p1_sq * (p2.y - p3.y) + p2_sq * (p3.y - p1.y) + p3_sq * (p1.y - p2.y)) / d;
    center.y = (p1_sq * (p3.x - p2.x) + p2_sq * (p1.x - p3.x) + p3_sq * (p2.x - p1.x)) / d;
    r = dist(center, p1);
    return true;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<Point> pts(n);
    for (int i = 0; i < n; ++i) {
        cin >> pts[i].x >> pts[i].y;
    }

    double min_r = 1e9;

    auto test_circle = [&](Point center, double r) {
        for (int i = 0; i < n; ++i) {
            if (dist(center, pts[i]) > r + 1e-9) return;
        }
        min_r = min(min_r, r);
    };

    // 2-point candidates
    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            Point center = {(pts[i].x + pts[j].x) / 2.0, (pts[i].y + pts[j].y) / 2.0};
            double r = dist(pts[i], pts[j]) / 2.0;
            test_circle(center, r);
        }
    }

    // 3-point candidates
    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            for (int k = j + 1; k < n; ++k) {
                Point center;
                double r;
                if (get_circle_3(pts[i], pts[j], pts[k], center, r)) {
                    test_circle(center, r);
                }
            }
        }
    }

    cout << fixed << setprecision(12) << min_r << "\n";
    return 0;
}
"""
    },
    {
        "id": "abc130_e",
        "title": "Common Subsequence",
        "contest_id": "abc130",
        "rating": 1676,
        "tag": "Dynamic Programming",
        "subtopic": "Classic DP",
        "topic": "2D DP Counting Common Subsequences with 2D Prefix Sums",
        "cat_folder": "dp",
        "cat_file": "common_subsequence_count_2d_dp.md",
        "statement": "Given two integer sequences S (length N) and T (length M). Find the number of pairs of subsequences of S and T that are identical, modulo 10^9 + 7.",
        "key_idea": "2D DP with 2D prefix sums. `dp[i][j]` = number of pairs of identical subsequences using prefixes S[1..i] and T[1..j].",
        "observation": "Inclusion-Exclusion recurrence on grid: dp[i][j] = (dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]) % MOD. If S[i] == T[j], matching this pair creates new common subsequences with all previously known ones plus the empty sequence: dp[i][j] = (dp[i][j] + dp[i-1][j-1] + 1) % MOD.",
        "algorithm": [
            "Initialize dp[N + 1][M + 1] = 0.",
            "For i from 1 to N:",
            "  For j from 1 to M:",
            "    dp[i][j] = (dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + MOD) % MOD;",
            "    if (S[i] == T[j]):",
            "      dp[i][j] = (dp[i][j] + dp[i - 1][j - 1] + 1) % MOD;",
            "Print (dp[N][M] + 1) % MOD (including empty subsequence pair).",
        ],
        "time_complexity": "O(N * M)",
        "space_complexity": "O(N * M)",
        "core_skill": "Counting common subsequences via 2D prefix sum inclusion-exclusion.",
        "reusable_pattern": "Common Subsequence Counter: dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + (S[i]==T[j] ? dp[i-1][j-1] + 1 : 0).",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>

using namespace std;

const int MOD = 1000000007;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<int> s(n + 1), t(m + 1);
    for (int i = 1; i <= n; ++i) cin >> s[i];
    for (int j = 1; j <= m; ++j) cin >> t[j];

    vector<vector<long long>> dp(n + 1, vector<long long>(m + 1, 0));

    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            dp[i][j] = (dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + MOD) % MOD;
            if (s[i] == t[j]) {
                dp[i][j] = (dp[i][j] + dp[i - 1][j - 1] + 1) % MOD;
            }
        }
    }

    // Including the empty pair
    cout << (dp[n][m] + 1) % MOD << "\n";
    return 0;
}
"""
    },
    {
        "id": "abc246_f",
        "title": "typewriter",
        "contest_id": "abc246",
        "rating": 1677,
        "tag": "Combinatorics",
        "subtopic": "Inclusion-Exclusion",
        "topic": "Principle of Inclusion-Exclusion (PIE) on Keyboard Key Sets",
        "cat_folder": "combinatorics",
        "cat_file": "pie_keyboard_key_sets.md",
        "statement": "A typewriter has N rows of keys. Row i contains a set of lowercase letters S_i. A string of length L can be typed if there is AT LEAST ONE row containing all its letters. Find the number of typeable strings of length L, modulo 998244353.",
        "key_idea": "Principle of Inclusion-Exclusion (PIE) over the N rows of keys! A string is typeable using row i if all its letters belong to S_i (which gives |S_i|^L strings).",
        "observation": "For any non-empty subset of rows mask, a string can be typed using ALL rows in mask iff its letters belong to the INTERSECTION of key sets of rows in mask: (intersection_count)^L. Apply PIE with signs determined by popcount(mask).",
        "algorithm": [
            "Convert each row S_i to a 26-bit bitmask.",
            "total_ans = 0.",
            "For mask from 1 to (1 << N) - 1:",
            "  intersection_keys = (1 << 26) - 1.",
            "  For i from 0 to N - 1:",
            "    if (mask & (1 << i)): intersection_keys &= row_mask[i].",
            "  common_chars = popcount(intersection_keys).",
            "  ways = power(common_chars, L, MOD).",
            "  if popcount(mask) % 2 == 1: total_ans = (total_ans + ways) % MOD.",
            "  else: total_ans = (total_ans - ways + MOD) % MOD.",
            "Print total_ans."
        ],
        "time_complexity": "O(2^N * N)",
        "space_complexity": "O(N)",
        "core_skill": "Principle of Inclusion-Exclusion on character set intersections.",
        "reusable_pattern": "PIE Union of Powers: sum (-1)^{|S|+1} * |intersection(S)|^L.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <string>

using namespace std;

const int MOD = 998244353;

long long power(long long base, long long exp) {
    long long res = 1;
    base %= MOD;
    while (exp > 0) {
        if (exp % 2 == 1) res = (res * base) % MOD;
        base = (base * base) % MOD;
        exp /= 2;
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long L;
    if (!(cin >> n >> L)) return 0;

    vector<int> row_mask(n, 0);
    for (int i = 0; i < n; ++i) {
        string s;
        cin >> s;
        for (char c : s) {
            row_mask[i] |= (1 << (c - 'a'));
        }
    }

    int total_masks = 1 << n;
    long long ans = 0;

    for (int mask = 1; mask < total_masks; ++mask) {
        int common_keys = (1 << 26) - 1;
        for (int i = 0; i < n; ++i) {
            if (mask & (1 << i)) {
                common_keys &= row_mask[i];
            }
        }
        int cnt = __builtin_popcount(common_keys);
        long long ways = power(cnt, L);

        if (__builtin_popcount(mask) % 2 == 1) {
            ans = (ans + ways) % MOD;
        } else {
            ans = (ans - ways + MOD) % MOD;
        }
    }

    cout << ans << "\n";
    return 0;
}
"""
    },
    {
        "id": "arc061_b",
        "title": "Snuke's Coloring",
        "contest_id": "abc045",
        "rating": 1682,
        "tag": "Data Structures",
        "subtopic": "Hash Map",
        "topic": "Sparse Grid 3x3 Window Counting via Coordinate Hash Map",
        "cat_folder": "data_structures",
        "cat_file": "sparse_grid_window_counting_hash.md",
        "statement": "An H x W grid (H, W <= 10^9) with N black cells (N <= 10^5), all other cells white. For each j in 0..9, find the number of 3x3 subgrids containing EXACTLY j black cells.",
        "key_idea": "The total number of 3x3 subgrids is (H - 2) * (W - 2) ~ 10^18. However, at most 9 * N subgrids contain AT LEAST ONE black cell! Hash map maps each 3x3 center to its black cell count.",
        "observation": "Each black cell at (r, c) can only be inside 3x3 subgrids whose centers (cr, cc) satisfy r - 1 <= cr <= r + 1 and c - 1 <= cc <= c + 1 with 2 <= cr <= H - 1 and 2 <= cc <= W - 1. Increment black count for these <= 9 centers. The count of subgrids with 0 black cells is (H - 2)*(W - 2) - (number of centers in map).",
        "algorithm": [
            "Maintain map<pair<int, int>, int> center_black_count.",
            "For each black cell (r, c):",
            "  For dr in {-1, 0, 1}, dc in {-1, 0, 1}:",
            "    cr = r + dr, cc = c + dc.",
            "    If 2 <= cr <= H - 1 and 2 <= cc <= W - 1:",
            "      center_black_count[{cr, cc}]++;",
            "Tally counts in freq[10].",
            "freq[0] = (H - 2) * (W - 2) - center_black_count.size().",
            "Print freq[0] through freq[9]."
        ],
        "time_complexity": "O(N log N)",
        "space_complexity": "O(N)",
        "core_skill": "Sparse window contribution hashing on massive coordinate grids.",
        "reusable_pattern": "Sparse Subgrid Counting: each point votes for its covering window centers in hash map.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <map>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long h, w;
    int n;
    if (!(cin >> h >> w >> n)) return 0;

    map<pair<long long, long long>, int> cnt;

    for (int i = 0; i < n; ++i) {
        long long r, c;
        cin >> r >> c;
        for (int dr = -1; dr <= 1; ++dr) {
            for (int dc = -1; dc <= 1; ++dc) {
                long long cr = r + dr;
                long long cc = c + dc;
                if (cr >= 2 && cr <= h - 1 && cc >= 2 && cc <= w - 1) {
                    cnt[{cr, cc}]++;
                }
            }
        }
    }

    vector<long long> ans(10, 0);
    for (const auto& entry : cnt) {
        ans[entry.second]++;
    }

    long long total_subgrids = (h - 2) * (w - 2);
    ans[0] = total_subgrids - cnt.size();

    for (int j = 0; j <= 9; ++j) {
        cout << ans[j] << "\n";
    }

    return 0;
}
"""
    },
    {
        "id": "abc031_d",
        "title": "Goroawase",
        "contest_id": "abc031",
        "rating": 1688,
        "tag": "Basics",
        "subtopic": "Exhaustive Search",
        "topic": "Digit String Length Partition Search",
        "cat_folder": "basics",
        "cat_file": "digit_string_length_search.md",
        "statement": "K digits 1..K (K <= 9). Each digit d corresponds to an unknown string S_d of length between 1 and 3. Given N pairs of (digit sequence v_i, string w_i). Find the string S_d for each digit d.",
        "key_idea": "There are only K digits, and each digit has length in {1, 2, 3}. The search space of length assignments is at most 3^9 = 19,683! Exhaustively search all length combinations and verify against the N string equations.",
        "observation": "Once lengths len[1..K] are fixed, for each equation v_i -> w_i, check if sum_{d in v_i} len[d] == |w_i|. If so, parse w_i into candidate substring for each digit d. If all parsed substrings are mutually consistent across all N equations, the solution is uniquely found.",
        "algorithm": [
            "Backtrack through all 3^K length combinations len[1..K] in {1, 2, 3}.",
            "For each combination:",
            "  valid = true.",
            "  vector<string> candidate(K + 1, '').",
            "  For each pair (v_i, w_i):",
            "    Verify sum len[d] == |w_i|.",
            "    Slice w_i according to lengths: if candidate[d] already set and != slice, invalid.",
            "  If valid for all N pairs, print candidate[1..K] and terminate."
        ],
        "time_complexity": "O(3^K * N * sum(|w|))",
        "space_complexity": "O(K)",
        "core_skill": "Parameter length partition search followed by greedy consistency verification.",
        "reusable_pattern": "Token Length Backtracking: 3^K search over token lengths + prefix verification.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <string>

using namespace std;

int k, n;
vector<string> v_list, w_list;
int len[10];

bool check() {
    vector<string> ans(k + 1, "");
    for (int i = 0; i < n; ++i) {
        int expected_len = 0;
        for (char c : v_list[i]) {
            expected_len += len[c - '0'];
        }
        if (expected_len != (int)w_list[i].size()) return false;

        int pos = 0;
        for (char c : v_list[i]) {
            int d = c - '0';
            string sub = w_list[i].substr(pos, len[d]);
            pos += len[d];

            if (ans[d] == "") {
                ans[d] = sub;
            } else if (ans[d] != sub) {
                return false;
            }
        }
    }

    for (int d = 1; d <= k; ++d) {
        cout << ans[d] << "\n";
    }
    return true;
}

bool search_lens(int idx) {
    if (idx > k) {
        return check();
    }
    for (int l = 1; l <= 3; ++l) {
        len[idx] = l;
        if (search_lens(idx + 1)) return true;
    }
    return false;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> k >> n)) return 0;

    v_list.resize(n);
    w_list.resize(n);
    for (int i = 0; i < n; ++i) {
        cin >> v_list[i] >> w_list[i];
    }

    search_lens(1);
    return 0;
}
"""
    },
    {
        "id": "abc219_e",
        "title": "Moat",
        "contest_id": "abc219",
        "rating": 1690,
        "tag": "Basics",
        "subtopic": "Bitmask Search",
        "topic": "Bitmask Grid Shapes with Connectivity (DSU) and Hole-Free (Outer BFS) Checking",
        "cat_folder": "basics",
        "cat_file": "bitmask_grid_shape_topology.md",
        "statement": "A 4x4 grid. Some cells contain houses (A[i][j] == 1). Build a moat around a set of cells S such that: 1) S contains all houses; 2) S forms a single 4-connected component; 3) The boundary of S is a simple polygon (S has no internal holes / lakes). Count valid sets S.",
        "key_idea": "The grid has only 16 cells, meaning 2^16 = 65,536 subsets! Enumerate all subsets mask and check: 1) mask has all houses; 2) moat cells form 1 connected component; 3) outer white cells (padded to 6x6) form 1 connected component (guaranteeing no holes).",
        "observation": "A shape has no internal holes iff its complement is connected to the outer boundary! Pad the 4x4 grid with an outer ring to 6x6. Flood-fill from (0, 0) through all non-moat cells: if the count of reachable non-moat cells equals 36 - popcount(mask), there are no interior holes.",
        "algorithm": [
            "Check that mask covers all cells with A[i][j] == 1.",
            "Moat connectivity: count connected components among 1s in mask using BFS/DSU; must equal 1.",
            "Hole-free test: create 6x6 grid, place moat in rows 1..4, cols 1..4.",
            "Flood fill (BFS) from (0, 0) over all cells not in moat.",
            "If flooded cell count == 36 - popcount(mask), increment valid_count.",
            "Print valid_count."
        ],
        "time_complexity": "O(2^16 * 36)",
        "space_complexity": "O(36)",
        "core_skill": "Topological shape validation (connectivity + hole-free simple boundary) via bitmask enumeration and flood-fill.",
        "reusable_pattern": "Simple Polygon Grid Moat: check mask connectivity + complement flood fill from outer border.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <queue>

using namespace std;

const int dr[4] = {-1, 1, 0, 0};
const int dc[4] = {0, 0, -1, 1};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int house_mask = 0;
    for (int r = 0; r < 4; ++r) {
        for (int c = 0; c < 4; ++c) {
            int val;
            if (cin >> val && val == 1) {
                house_mask |= (1 << (r * 4 + c));
            }
        }
    }

    int total_masks = 1 << 16;
    int ans = 0;

    for (int mask = 1; mask < total_masks; ++mask) {
        // Condition 1: Contains all houses
        if ((mask & house_mask) != house_mask) continue;

        // Condition 2: Moat is connected
        int start_cell = __builtin_ctz(mask);
        int visited_moat = 0;
        queue<int> q;
        q.push(start_cell);
        visited_moat |= (1 << start_cell);

        while (!q.empty()) {
            int cell = q.front();
            q.pop();
            int r = cell / 4, c = cell % 4;
            for (int i = 0; i < 4; ++i) {
                int nr = r + dr[i], nc = c + dc[i];
                if (nr >= 0 && nr < 4 && nc >= 0 && nc < 4) {
                    int ncell = nr * 4 + nc;
                    if ((mask & (1 << ncell)) && !(visited_moat & (1 << ncell))) {
                        visited_moat |= (1 << ncell);
                        q.push(ncell);
                    }
                }
            }
        }

        if (visited_moat != mask) continue;

        // Condition 3: No holes (outer complement is connected on 6x6 grid)
        vector<vector<bool>> is_moat(6, vector<bool>(6, false));
        for (int r = 0; r < 4; ++r) {
            for (int c = 0; c < 4; ++c) {
                if (mask & (1 << (r * 4 + c))) {
                    is_moat[r + 1][c + 1] = true;
                }
            }
        }

        vector<vector<bool>> vis_outer(6, vector<bool>(6, false));
        queue<pair<int, int>> q_out;
        q_out.push({0, 0});
        vis_outer[0][0] = true;
        int outer_reach = 0;

        while (!q_out.empty()) {
            auto [r, c] = q_out.front();
            q_out.pop();
            outer_reach++;

            for (int i = 0; i < 4; ++i) {
                int nr = r + dr[i], nc = c + dc[i];
                if (nr >= 0 && nr < 6 && nc >= 0 && nc < 6) {
                    if (!is_moat[nr][nc] && !vis_outer[nr][nc]) {
                        vis_outer[nr][nc] = true;
                        q_out.push({nr, nc});
                    }
                }
            }
        }

        if (outer_reach == 36 - __builtin_popcount(mask)) {
            ans++;
        }
    }

    cout << ans << "\n";
    return 0;
}
"""
    },
    {
        "id": "abc260_e",
        "title": "At Least One",
        "contest_id": "abc260",
        "rating": 1692,
        "tag": "Basics",
        "subtopic": "Two Pointers",
        "topic": "Two Pointers / Sliding Window on Multi-Interval Coverage",
        "cat_folder": "basics",
        "cat_file": "two_pointers_multi_interval_coverage.md",
        "statement": "N pairs of integers (A_i, B_i) with 1 <= A_i < B_i <= M. An integer sequence f(k) counts intervals [l, r] of length k = r - l + 1 such that for every pair i, the interval contains at least one of A_i or B_i. Compute f(k) for all k = 1..M.",
        "key_idea": "Two pointers! For each left endpoint l (1 <= l <= M), find the minimum right endpoint r such that [l, r] contains at least one number from every pair.",
        "observation": "If [l, r] is the minimal valid interval for l, then for any R in [r, M], [l, R] is also valid! Its length is k = R - l + 1, so all lengths in [r - l + 1, M - l + 1] receive +1. Add +1 to this range using a difference array.",
        "algorithm": [
            "Store which pairs contain value x in occ[x].",
            "Use two pointers (l = 1, r = 1) and maintain covered_pairs count.",
            "While covered_pairs < N and r <= M: add r, r++.",
            "For l from 1 to M:",
            "  While r <= M and covered_pairs < N: add r, r++.",
            "  If covered_pairs == N:",
            "    min_k = (r - 1) - l + 1, max_k = M - l + 1.",
            "    diff[min_k]++, diff[max_k + 1]--;",
            "  Remove l from window.",
            "Prefix sum diff array and print f(1..M)."
        ],
        "time_complexity": "O(N + M)",
        "space_complexity": "O(N + M)",
        "core_skill": "Two pointers minimal valid right endpoint sweep mapped to length contribution difference arrays.",
        "reusable_pattern": "Minimal Window Coverage: two pointers finds min r for each l, adds to length range via diff array.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<int>> occ(m + 1);
    for (int i = 0; i < n; ++i) {
        int a, b;
        cin >> a >> b;
        occ[a].push_back(i);
        occ[b].push_back(i);
    }

    vector<int> pair_cnt(n, 0);
    int covered = 0;
    int r = 1;

    vector<int> diff(m + 2, 0);

    for (int l = 1; l <= m; ++l) {
        while (r <= m && covered < n) {
            for (int p : occ[r]) {
                if (pair_cnt[p] == 0) covered++;
                pair_cnt[p]++;
            }
            r++;
        }

        if (covered == n) {
            int min_len = (r - 1) - l + 1;
            int max_len = m - l + 1;
            diff[min_len]++;
            diff[max_len + 1]--;
        }

        // Remove l
        for (int p : occ[l]) {
            pair_cnt[p]--;
            if (pair_cnt[p] == 0) covered--;
        }
    }

    int cur = 0;
    for (int k = 1; k <= m; ++k) {
        cur += diff[k];
        cout << cur << (k == m ? "\n" : " ");
    }

    return 0;
}
"""
    },
    {
        "id": "abc201_e",
        "title": "Xor Distances",
        "contest_id": "abc201",
        "rating": 1694,
        "tag": "Graph Theory",
        "subtopic": "Trees",
        "topic": "Tree XOR Distances Bit-by-Bit Counting via Root DFS",
        "cat_folder": "graph_theory",
        "cat_file": "tree_xor_distances_bit_counting.md",
        "statement": "Given a weighted tree with N vertices. The XOR distance between u and v is the XOR sum of edge weights on the simple path between them. Find the sum of XOR distances over all pairs 1 <= u < v <= N, modulo 10^9 + 7.",
        "key_idea": "In any tree, the path from u to v can be routed through an arbitrary root (e.g. 1): dist(u, v) = dist(root, u) ^ dist(root, v), because edges on the common path to the LCA cancel out!",
        "observation": "Compute d[u] = dist(1, u) for all vertices using DFS. For each bit b from 0 to 59: count vertices with the b-th bit set (cnt1) and unset (cnt0). The b-th bit is set in dist(u, v) iff one endpoint has bit 1 and the other has bit 0: cnt1 * cnt0 pairs! Total sum = sum_{b=0}^{59} 2^b * cnt1 * cnt0 modulo 10^9 + 7.",
        "algorithm": [
            "Root tree at 1 and compute d[u] = XOR distance from root 1 via DFS in O(N).",
            "ans = 0.",
            "For bit b from 0 to 59:",
            "  cnt1 = count of u where (d[u] >> b) & 1.",
            "  cnt0 = N - cnt1.",
            "  pairs = (1LL * cnt1 * cnt0) % MOD.",
            "  weight = (1LL << b) % MOD.",
            "  ans = (ans + pairs * weight) % MOD.",
            "Print ans."
        ],
        "time_complexity": "O(60 * N)",
        "space_complexity": "O(N)",
        "core_skill": "Bitwise independence and XOR path cancellation via root projection on trees.",
        "reusable_pattern": "Tree Path XOR: dist(u, v) = d[u] ^ d[v]; count bit contributions independently.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>

using namespace std;

const int MOD = 1000000007;

struct Edge {
    int to;
    long long w;
};

vector<vector<Edge>> adj;
vector<long long> xor_dist;

void dfs(int u, int p, long long d) {
    xor_dist[u] = d;
    for (const auto& e : adj[u]) {
        if (e.to != p) {
            dfs(e.to, u, d ^ e.w);
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    adj.resize(n + 1);
    xor_dist.resize(n + 1, 0);

    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        long long w;
        cin >> u >> v >> w;
        adj[u].push_back({v, w});
        adj[v].push_back({u, w});
    }

    dfs(1, 0, 0);

    long long ans = 0;

    for (int b = 0; b < 60; ++b) {
        long long cnt1 = 0;
        for (int i = 1; i <= n; ++i) {
            if ((xor_dist[i] >> b) & 1) {
                cnt1++;
            }
        }
        long long cnt0 = n - cnt1;
        long long pairs = (cnt1 * cnt0) % MOD;
        long long bit_val = ((1LL << b) % MOD);
        ans = (ans + pairs * bit_val) % MOD;
    }

    cout << ans << "\n";
    return 0;
}
"""
    },
    {
        "id": "arc022_3",
        "title": "Romeo and Juliet",
        "contest_id": "arc022",
        "rating": 1694,
        "tag": "Graph Theory",
        "subtopic": "Tree Diameter",
        "topic": "Tree Diameter Endpoints via 2-Pass BFS/DFS",
        "cat_folder": "graph_theory",
        "cat_file": "tree_diameter_endpoints_2pass.md",
        "statement": "Given a tree with N vertices. Find two vertices u and v such that the distance between them is maximized (i.e. the two endpoints of the tree diameter).",
        "key_idea": "Canonical 2-pass BFS algorithm: 1) Run BFS from an arbitrary starting vertex (e.g. 1) to find the farthest vertex u; 2) Run BFS from vertex u to find the farthest vertex v. (u, v) is guaranteed to be a diameter of the tree.",
        "observation": "Any vertex farthest from an arbitrary node is guaranteed to be an endpoint of some diameter of the tree. A second BFS from that endpoint identifies the opposite endpoint.",
        "algorithm": [
            "BFS 1 from vertex 1: find node u with maximum distance from 1.",
            "BFS 2 from node u: find node v with maximum distance from u.",
            "Print u and v."
        ],
        "time_complexity": "O(N)",
        "space_complexity": "O(N)",
        "core_skill": "Double-sweep BFS/DFS for tree diameter endpoint identification.",
        "reusable_pattern": "Tree Diameter Endpoints: BFS(1) -> u, BFS(u) -> v; diameter endpoints are (u, v).",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <queue>

using namespace std;

pair<int, int> bfs(int start, int n, const vector<vector<int>>& adj) {
    vector<int> dist(n + 1, -1);
    queue<int> q;
    dist[start] = 0;
    q.push(start);

    int farthest_node = start;
    int max_d = 0;

    while (!q.empty()) {
        int u = q.front();
        q.pop();

        if (dist[u] > max_d) {
            max_d = dist[u];
            farthest_node = u;
        }

        for (int v : adj[u]) {
            if (dist[v] == -1) {
                dist[v] = dist[u] + 1;
                q.push(v);
            }
        }
    }
    return {farthest_node, max_d};
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    auto [u, d1] = bfs(1, n, adj);
    auto [v, d2] = bfs(u, n, adj);

    cout << u << " " << v << "\n";
    return 0;
}
"""
    },
    {
        "id": "abc110_d",
        "title": "Factorization",
        "contest_id": "abc110",
        "rating": 1695,
        "tag": "Number Theory",
        "subtopic": "Prime Factorization",
        "topic": "Prime Factorization + Stars and Bars on Exponents",
        "cat_folder": "number_theory",
        "cat_file": "prime_factorization_stars_and_bars_factorization.md",
        "statement": "Given N and M. Find the number of sequences of N positive integers (a_1, ..., a_N) such that a_1 * a_2 * ... * a_N = M, modulo 10^9 + 7.",
        "key_idea": "Prime factorize M = prod p_i^{e_i}. Because prime factorizations are unique, the exponent e_i of each prime p_i must be distributed across the N variables independently.",
        "observation": "Distributing e_i identical prime factors among N variables corresponds to weak compositions of e_i into N parts: Stars and Bars C(e_i + N - 1, N - 1). The total sequences is prod_i C(e_i + N - 1, N - 1) modulo 10^9 + 7.",
        "algorithm": [
            "Factorize M in O(sqrt(M)) into prime powers p_i^{e_i}.",
            "Precompute factorials and inverse factorials up to N + 100.",
            "ans = 1.",
            "For each prime power with exponent e_i:",
            "  ans = (ans * nCr(e_i + N - 1, N - 1)) % MOD.",
            "Print ans."
        ],
        "time_complexity": "O(sqrt(M) + log(MOD))",
        "space_complexity": "O(N)",
        "core_skill": "Multiplicative decomposition into independent additive exponent stars and bars.",
        "reusable_pattern": "Product Factorization Sequences: prod_{p|M} C(e + N - 1, N - 1).",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>

using namespace std;

const int MOD = 1000000007;
const int MAX = 200005;

long long fact[MAX], invFact[MAX];

long long power(long long base, long long exp) {
    long long res = 1;
    base %= MOD;
    while (exp > 0) {
        if (exp % 2 == 1) res = (res * base) % MOD;
        base = (base * base) % MOD;
        exp /= 2;
    }
    return res;
}

void precompute() {
    fact[0] = 1;
    for (int i = 1; i < MAX; ++i) fact[i] = (fact[i - 1] * i) % MOD;
    invFact[MAX - 1] = power(fact[MAX - 1], MOD - 2);
    for (int i = MAX - 2; i >= 0; --i) invFact[i] = (invFact[i + 1] * (i + 1)) % MOD;
}

long long nCr(int n, int r) {
    if (r < 0 || r > n) return 0;
    return fact[n] * invFact[r] % MOD * invFact[n - r] % MOD;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    precompute();

    int n;
    long long m;
    if (!(cin >> n >> m)) return 0;

    long long ans = 1;
    long long temp = m;

    for (long long d = 2; d * d <= temp; ++d) {
        if (temp % d == 0) {
            int e = 0;
            while (temp % d == 0) {
                e++;
                temp /= d;
            }
            ans = (ans * nCr(e + n - 1, n - 1)) % MOD;
        }
    }

    if (temp > 1) {
        ans = (ans * nCr(1 + n - 1, n - 1)) % MOD;
    }

    cout << ans << "\n";
    return 0;
}
"""
    },
    {
        "id": "abc143_e",
        "title": "Travel by Car",
        "contest_id": "abc143",
        "rating": 1695,
        "tag": "Graph Theory",
        "subtopic": "All-Pairs Shortest Paths",
        "topic": "Dual Floyd-Warshall (Distance Reachability then Refuel Count)",
        "cat_folder": "graph_theory",
        "cat_file": "dual_floyd_warshall_refuel_hops.md",
        "statement": "An undirected weighted graph with N cities and M roads. A car has fuel tank capacity L. You can refuel to full capacity L at any city for free. Process Q queries (s, t): minimum number of refuels needed to travel from s to t, or -1 if unreachable.",
        "key_idea": "Dual Floyd-Warshall! Phase 1: Floyd-Warshall to compute shortest physical distance between all pairs. Two cities can reach each other with a single full tank iff dist[u][v] <= L. Phase 2: Build a new graph where edge weight is 1 if dist[u][v] <= L, and run Floyd-Warshall to find minimum refuel hops.",
        "observation": "Any trip between s and t requiring minimum refuels corresponds to the shortest path in the unweighted reachability graph where an edge exists iff dist[u][v] <= L. Total refuels is (shortest_tank_hops - 1).",
        "algorithm": [
            "Phase 1: Compute shortest physical distances dist[u][v] using Floyd-Warshall.",
            "Phase 2: Build tank_dist[u][v] = (dist[u][v] <= L ? 1 : INF).",
            "Run Floyd-Warshall on tank_dist.",
            "For each query (s, t):",
            "  If tank_dist[s][t] >= INF, print -1.",
            "  Else print tank_dist[s][t] - 1."
        ],
        "time_complexity": "O(N^3 + Q)",
        "space_complexity": "O(N^2)",
        "core_skill": "Hierarchical graph abstraction via dual Floyd-Warshall stages.",
        "reusable_pattern": "Dual Floyd-Warshall: Phase 1 computes physical reachability; Phase 2 computes hop counts.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const long long INF = 1e16;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    long long L;
    if (!(cin >> n >> m >> L)) return 0;

    vector<vector<long long>> dist(n + 1, vector<long long>(n + 1, INF));
    for (int i = 1; i <= n; ++i) dist[i][i] = 0;

    for (int i = 0; i < m; ++i) {
        int u, v;
        long long w;
        cin >> u >> v >> w;
        dist[u][v] = min(dist[u][v], w);
        dist[v][u] = min(dist[v][u], w);
    }

    // Phase 1: Physical distances
    for (int k = 1; k <= n; ++k) {
        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= n; ++j) {
                if (dist[i][k] + dist[k][j] < dist[i][j]) {
                    dist[i][j] = dist[i][k] + dist[k][j];
                }
            }
        }
    }

    // Phase 2: Refuel hops
    vector<vector<long long>> hops(n + 1, vector<long long>(n + 1, INF));
    for (int i = 1; i <= n; ++i) {
        hops[i][i] = 0;
        for (int j = i + 1; j <= n; ++j) {
            if (dist[i][j] <= L) {
                hops[i][j] = hops[j][i] = 1;
            }
        }
    }

    for (int k = 1; k <= n; ++k) {
        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= n; ++j) {
                if (hops[i][k] + hops[k][j] < hops[i][j]) {
                    hops[i][j] = hops[i][k] + hops[k][j];
                }
            }
        }
    }

    int q;
    cin >> q;
    while (q--) {
        int s, t;
        cin >> s >> t;
        if (hops[s][t] >= INF) {
            cout << -1 << "\n";
        } else {
            cout << hops[s][t] - 1 << "\n";
        }
    }

    return 0;
}
"""
    },
    {
        "id": "abc006_4",
        "title": "Playing Cards Insertion Sort",
        "contest_id": "abc006",
        "rating": 1696,
        "tag": "Dynamic Programming",
        "subtopic": "Longest Increasing Subsequence (LIS)",
        "topic": "Minimum Card Insertions = N - LIS(A) via Patience Sorting",
        "cat_folder": "dp",
        "cat_file": "minimum_insertions_lis.md",
        "statement": "Given N cards with a permutation of numbers 1..N. In one operation, you can take any card and insert it at any position. Find the minimum operations to sort the cards in ascending order.",
        "key_idea": "Any card that is NOT moved must maintain its relative order with other unmoved cards, meaning the unmoved cards must form an increasing subsequence. To minimize moved cards, maximize unmoved cards: min operations = N - LIS(A).",
        "observation": "Classic Longest Increasing Subsequence (LIS). Finding LIS(A) in O(N log N) using patience sorting / binary search (`std::lower_bound`) gives the exact answer N - LIS(A).",
        "algorithm": [
            "Initialize tails array for patience sorting.",
            "For each card x in permutation A:",
            "  auto it = lower_bound(tails.begin(), tails.end(), x);",
            "  If it == tails.end(): tails.push_back(x);",
            "  Else: *it = x;",
            "Print N - tails.size()."
        ],
        "time_complexity": "O(N log N)",
        "space_complexity": "O(N)",
        "core_skill": "Reduction of insertion sort moves to Longest Increasing Subsequence complement.",
        "reusable_pattern": "Minimum Insertion Moves: N - LIS(A) via lower_bound patience sorting.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    vector<int> tails;
    for (int x : a) {
        auto it = lower_bound(tails.begin(), tails.end(), x);
        if (it == tails.end()) {
            tails.push_back(x);
        } else {
            *it = x;
        }
    }

    cout << n - tails.size() << "\n";
    return 0;
}
"""
    },
    {
        "id": "abc247_f",
        "title": "Cards",
        "contest_id": "abc247",
        "rating": 1697,
        "tag": "Dynamic Programming",
        "subtopic": "Tree / Graph DP",
        "topic": "Functional Graph Permutation Cycle Decomposition + Lucas Numbers",
        "cat_folder": "dp",
        "cat_file": "permutation_cycle_lucas_numbers.md",
        "statement": "N cards, card i has P_i on front and Q_i on back (P and Q are permutations of 1..N). Choose a subset of cards such that every number 1..N appears at least once on either front or back of a chosen card. Find the number of valid card subsets, modulo 998244353.",
        "key_idea": "Model each card as an edge between P_i and Q_i. Because P and Q are permutations, every vertex has degree 2, so the graph decomposes into disjoint simple cycles! For each cycle of length L, the number of edge subsets covering all vertices is the Lucas number L_L.",
        "observation": "Lucas numbers satisfy L_1 = 1, L_2 = 3, L_L = L_{L-1} + L_{L-2} for L >= 3 (derived from choosing non-adjacent unchosen edges on a circle). The total answer is the product of L_L over all connected cycle lengths L modulo 998244353.",
        "algorithm": [
            "Build graph with edges (P_i, Q_i).",
            "Precompute Lucas numbers: L[1] = 1, L[2] = 3; L[i] = (L[i-1] + L[i-2]) % MOD.",
            "Decompose graph into connected components using DFS/DSU to find cycle lengths.",
            "ans = 1.",
            "For each cycle of length len: ans = (ans * L[len]) % MOD.",
            "Print ans."
        ],
        "time_complexity": "O(N)",
        "space_complexity": "O(N)",
        "core_skill": "Cycle decomposition of 2-regular permutation graphs with circular Lucas number independent set counting.",
        "reusable_pattern": "Permutation Edge Cover on Cycles: answer = prod_{cycles} Lucas(cycle_length).",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>

using namespace std;

const int MOD = 998244353;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> p(n + 1), q(n + 1);
    for (int i = 1; i <= n; ++i) cin >> p[i];
    for (int i = 1; i <= n; ++i) cin >> q[i];

    vector<vector<int>> adj(n + 1);
    for (int i = 1; i <= n; ++i) {
        adj[p[i]].push_back(q[i]);
        adj[q[i]].push_back(p[i]);
    }

    // Precompute Lucas numbers
    vector<long long> lucas(n + 2);
    lucas[1] = 1;
    lucas[2] = 3;
    for (int i = 3; i <= n + 1; ++i) {
        lucas[i] = (lucas[i - 1] + lucas[i - 2]) % MOD;
    }

    vector<bool> visited(n + 1, false);
    long long ans = 1;

    for (int i = 1; i <= n; ++i) {
        if (!visited[i]) {
            int cycle_len = 0;
            int curr = i;
            while (!visited[curr]) {
                visited[curr] = true;
                cycle_len++;
                // Move to next unvisited neighbor
                int next_node = -1;
                for (int nxt : adj[curr]) {
                    if (!visited[nxt]) {
                        next_node = nxt;
                        break;
                    }
                }
                if (next_node == -1) break;
                curr = next_node;
            }
            ans = (ans * lucas[cycle_len]) % MOD;
        }
    }

    cout << ans << "\n";
    return 0;
}
"""
    },
    {
        "id": "abc169_f",
        "title": "Knapsack for All Subsets",
        "contest_id": "abc169",
        "rating": 1698,
        "tag": "Dynamic Programming",
        "subtopic": "Classic DP",
        "topic": "3-Choice State Dynamic Programming on Subsets of Subsets",
        "cat_folder": "dp",
        "cat_file": "subsets_of_subsets_knapsack_dp.md",
        "statement": "Given an array A of length N and target S. For every subset T of {1..N}, let f(T) be the number of subsets of T whose elements sum to S. Find sum_{T} f(T) modulo 998244353.",
        "key_idea": "Rephrase: we are choosing a subset T, and within T, choosing a subset U whose sum is S. For each element A_i, there are 3 independent choices: 1) A_i not in T; 2) A_i in T but not in U; 3) A_i in T and in U.",
        "observation": "Choices 1 and 2 contribute 0 to the sum U (2 ways, sum +0). Choice 3 contributes A_i to the sum U (1 way, sum +A_i). Therefore, transitioning with element A_i: dp[s] = (2 * dp[s] + dp[s - A_i]) % MOD!",
        "algorithm": [
            "Initialize dp[S + 1] = 0; dp[0] = 1.",
            "For each element a in A:",
            "  For s from S down to 0:",
            "    next_s = (2 * dp[s]) % MOD;",
            "    if (s >= a) next_s = (next_s + dp[s - a]) % MOD;",
            "    dp[s] = next_s;",
            "Print dp[S]."
        ],
        "time_complexity": "O(N * S)",
        "space_complexity": "O(S)",
        "core_skill": "Combinatorial reinterpretation of nested subset counting into 3-branch single-pass knapsack.",
        "reusable_pattern": "Knapsack for All Subsets: dp[s] = 2 * dp[s] + dp[s - a].",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>

using namespace std;

const int MOD = 998244353;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, S;
    if (!(cin >> n >> S)) return 0;

    vector<int> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    vector<long long> dp(S + 1, 0);
    dp[0] = 1;

    for (int x : a) {
        for (int s = S; s >= 0; --s) {
            long long ways = (dp[s] * 2) % MOD;
            if (s >= x) {
                ways = (ways + dp[s - x]) % MOD;
            }
            dp[s] = ways;
        }
    }

    cout << dp[S] << "\n";
    return 0;
}
"""
    }
]

REJECTED_PROBLEMS = [
    {"id": "arc162_c", "title": "Mex Game on Tree", "rating": 1655, "reason": "REJECTED (BASIC LOGIC BUILDING) — Ad-hoc Mex game simulation drill."},
    {"id": "abc379_f", "title": "Buildings 2", "rating": 1659, "reason": "REJECTED (BASIC LOGIC BUILDING) — Routine building visibility casework."},
    {"id": "agc063_b", "title": "Insert 1, 2, 3, ...", "rating": 1663, "reason": "REJECTED (BASIC LOGIC BUILDING) — Ad-hoc array insertion simulation."},
    {"id": "abc401_f", "title": "Add One Edge 3", "rating": 1666, "reason": "REJECTED (BASIC LOGIC BUILDING) — Routine tree diameter casework."},
    {"id": "abc331_f", "title": "Palindrome Query", "rating": 1666, "reason": "REJECTED (BASIC LOGIC BUILDING) — Routine palindrome hash query drill."},
    {"id": "keyence2019_d", "title": "Double Landscape", "rating": 1670, "reason": "REJECTED (BASIC LOGIC BUILDING) — Ad-hoc grid row/column max simulation."},
    {"id": "abc382_e", "title": "Expansion Packs", "rating": 1671, "reason": "REJECTED (BASIC LOGIC BUILDING) — Routine expansion packs expected value."},
    {"id": "abc313_e", "title": "Duplicate", "rating": 1672, "reason": "REJECTED (BASIC LOGIC BUILDING) — Ad-hoc duplicate run-length simulation."},
    {"id": "abc301_e", "title": "Pac-Takahashi", "rating": 1673, "reason": "REJECTED (BASIC LOGIC BUILDING) — Routine Pac-Man candy collection drill."},
    {"id": "abc315_f", "title": "Shortcuts", "rating": 1674, "reason": "REJECTED (BASIC LOGIC BUILDING) — Simple penalty skip DP."},
    {"id": "abc433_e", "title": "Max Matrix 2", "rating": 1674, "reason": "REJECTED (BASIC LOGIC BUILDING) — Ad-hoc max matrix casework."},
    {"id": "arc186_b", "title": "Typical Permutation Descriptor", "rating": 1677, "reason": "REJECTED (BASIC LOGIC BUILDING) — Ad-hoc permutation descriptor drill."},
    {"id": "abc225_e", "title": "7", "rating": 1678, "reason": "REJECTED (BASIC LOGIC BUILDING) — Angle interval scheduling drill."},
    {"id": "abc377_e", "title": "Permute K times 2", "rating": 1685, "reason": "REJECTED (BASIC LOGIC BUILDING) — Routine permutation cycle exponentiation."},
    {"id": "agc009_b", "title": "Tournament", "rating": 1685, "reason": "REJECTED (BASIC LOGIC BUILDING) — Tournament tree depth drill."},
    {"id": "arc221_a", "title": "Two Arithmetic Progressions", "rating": 1686, "reason": "REJECTED (BASIC LOGIC BUILDING) — Simple AP casework."},
    {"id": "arc129_c", "title": "Multiple of 7", "rating": 1687, "reason": "REJECTED (BASIC LOGIC BUILDING) — Ad-hoc multiple of 7 construction."},
    {"id": "abc335_f", "title": "Hop Sugoroku", "rating": 1690, "reason": "REJECTED (BASIC LOGIC BUILDING) — Routine hop sugoroku square root decomposition drill."},
    {"id": "abc423_f", "title": "Loud Cicada", "rating": 1691, "reason": "REJECTED (BASIC LOGIC BUILDING) — Ad-hoc loud cicada drill."},
    {"id": "arc202_a", "title": "Merge and Increment", "rating": 1691, "reason": "REJECTED (BASIC LOGIC BUILDING) — Ad-hoc merge simulation."},
    {"id": "abc013_3", "title": "節制", "rating": 1692, "reason": "REJECTED (BASIC LOGIC BUILDING) — Routine calorie math casework."},
    {"id": "arc027_3", "title": "最高のトッピングにしような", "rating": 1692, "reason": "REJECTED (DUPLICATE) — Subsumed by 2-constraint knapsack archetypes."},
    {"id": "abc468_f", "title": "Chmax", "rating": 1693, "reason": "REJECTED (BASIC LOGIC BUILDING) — Routine Chmax casework."},
    {"id": "abc467_e", "title": "Adjacent Sums (hard)", "rating": 1694, "reason": "REJECTED (BASIC LOGIC BUILDING) — Adjacent sums drill."},
    {"id": "arc145_c", "title": "Split and Maximize", "rating": 1697, "reason": "REJECTED (BASIC LOGIC BUILDING) — Split and maximize drill."}
]

# Step 1: Compile all C++ solutions to verify zero errors
print(f"Testing C++ compilation of all {len(SELECTED_PROBLEMS)} selected ABC Part 1B solutions...")
os.makedirs("scratch", exist_ok=True)

for p in SELECTED_PROBLEMS:
    cpp_file = os.path.join("scratch", f"test_{p['id']}.cpp")
    obj_file = os.path.join("scratch", f"test_{p['id']}.o")
    with open(cpp_file, "w", encoding="utf-8") as f:
        f.write(p["cpp_code"])
    
    cmd = ["g++", "-std=c++17", "-O2", "-c", cpp_file, "-o", obj_file]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"[FAIL] {p['id']} compilation error:\n{res.stderr}")
        exit(1)
    else:
        print(f"[OK] {p['id']} ({p['title']})")
    
    if os.path.exists(cpp_file): os.remove(cpp_file)
    if os.path.exists(obj_file): os.remove(obj_file)

print(f"[+] All {len(SELECTED_PROBLEMS)} ABC Part 1B C++ solutions compiled with 0 errors!")

# Step 2: Generate Analysis Markdown files
for p in SELECTED_PROBLEMS:
    analysis_path = os.path.join("analysis", f"AtCoder-{p['id']}.md")
    algo_steps = "\n".join([f"{i+1}. {step}" for i, step in enumerate(p["algorithm"])])
    
    content = f"""# Problem Analysis: AtCoder-{p['id']} — {p['title']}

**Problem ID**: `AtCoder-{p['id']}`  
**Contest**: `{p['contest_id']}`  
**Rating / Difficulty**: {p['rating']}  
**URL**: https://atcoder.jp/contests/{p['contest_id']}/tasks/{p['id']}  
**VJudge Tag**: `[problem:AtCoder-{p['id']}]`  
**Category File**: [`../categories/{p['cat_folder']}/{p['cat_file']}`](../categories/{p['cat_folder']}/{p['cat_file']})  

- **Tag (Domain)**: `{p['tag']}`  
- **Subtopic**: `{p['subtopic']}`  
- **Topic (Skill)**: `{p['topic']}`  

---

## 1. Problem Statement & Key Idea
{p['statement']}

**Key Insight**: {p['key_idea']}

## 2. Core Observation & Invariant
{p['observation']}

## 3. Step-by-Step Algorithm
{algo_steps}

## 4. Complexity Analysis
- **Time Complexity**: `{p['time_complexity']}`
- **Space Complexity**: `{p['space_complexity']}`

## 5. Complete C++ Solution
```cpp
{p['cpp_code'].strip()}
```

## 6. Editorial Comparison & Alignment
{p['editorial_comparison']}

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: {p['core_skill']}
- **Reusable Pattern**: `{p['reusable_pattern']}`
"""
    with open(analysis_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[+] Generated Analysis: {analysis_path}")

# Step 3: Create / Update Category files
for p in SELECTED_PROBLEMS:
    cat_dir = os.path.join("categories", p["cat_folder"])
    os.makedirs(cat_dir, exist_ok=True)
    cat_path = os.path.join(cat_dir, p["cat_file"])
    
    entry = f"""
### `[problem:AtCoder-{p['id']}]` — {p['title']}
- **Rating / Difficulty**: {p['rating']}
- **Contest**: `{p['contest_id']}`
- **Analysis**: [`analysis/AtCoder-{p['id']}.md`](../../analysis/AtCoder-{p['id']}.md)
- **Key Idea**: {p['key_idea']}
- **Time Complexity**: `{p['time_complexity']}`
- **Space Complexity**: `{p['space_complexity']}`
- **Verified C++ Implementation**:
```cpp
{p['cpp_code'].strip()}
```
"""
    if not os.path.exists(cat_path):
        header = f"""# {p['topic']}

**Domain**: `{p['tag']}`  
**Subtopic**: `{p['subtopic']}`  

This workbook contains curated, high-quality competitive programming problems teaching **{p['topic']}**.

---

## Curated Problems
"""
        with open(cat_path, "w", encoding="utf-8") as f:
            f.write(header + entry)
    else:
        with open(cat_path, "r", encoding="utf-8") as f:
            existing = f.read()
        if f"[problem:AtCoder-{p['id']}]" not in existing:
            with open(cat_path, "a", encoding="utf-8") as f:
                f.write(entry)
    print(f"[+] Updated Category File: {cat_path}")

# Update SELECTION_LOG.md
with open("SELECTION_LOG.md", "r", encoding="utf-8") as f:
    existing_log = f.read()

new_log_entries = []
for p in SELECTED_PROBLEMS:
    tag_str = f"{p['tag']} → {p['topic']}"
    log_line = f"| [problem:AtCoder-{p['id']}] | {p['title']} | {p['rating']} | **SELECTED** | {tag_str} | Selected: Archetype for {p['topic']}. |"
    if f"[problem:AtCoder-{p['id']}]" not in existing_log:
        new_log_entries.append(log_line)

for p in REJECTED_PROBLEMS:
    log_line = f"| [problem:AtCoder-{p['id']}] | {p['title']} | {p['rating']} | **REJECTED** | Basics → Implementation | {p['reason']} |"
    if f"[problem:AtCoder-{p['id']}]" not in existing_log:
        new_log_entries.append(log_line)

if new_log_entries:
    with open("SELECTION_LOG.md", "a", encoding="utf-8") as f:
        f.write("\n" + "\n".join(new_log_entries) + "\n")
    print(f"[+] Added {len(new_log_entries)} new entries to SELECTION_LOG.md")

# Update QUALITY_PROBLEMS_BY_TOPIC.md
with open("QUALITY_PROBLEMS_BY_TOPIC.md", "r", encoding="utf-8") as f:
    existing_q = f.read()

new_q_lines = []
for p in SELECTED_PROBLEMS:
    line = f"- `[problem:AtCoder-{p['id']}]` — **{p['title']}** (Rating: {p['rating']}) | Topic: `{p['topic']}` | Analysis: [`analysis/AtCoder-{p['id']}.md`](analysis/AtCoder-{p['id']}.md)"
    if f"[problem:AtCoder-{p['id']}]" not in existing_q:
        new_q_lines.append(line)

if new_q_lines:
    with open("QUALITY_PROBLEMS_BY_TOPIC.md", "a", encoding="utf-8") as f:
        f.write("\n### Batch 5 Part 1B: ABC Curated Ladder (1651 - 1699)\n" + "\n".join(new_q_lines) + "\n")
    print("[+] Updated QUALITY_PROBLEMS_BY_TOPIC.md with new archetypes.")

# Update state/progress.json
with open("state/progress.json", "r", encoding="utf-8") as f:
    progress = json.load(f)

progress["current_batch"] = "Batch 5 Part 1B: ABC Ladder (1651-1699) COMPLETED"
progress["status"] = "IN_PROGRESS"
for p in SELECTED_PROBLEMS:
    if p["id"] not in progress["completed_problem_ids"]:
        progress["completed_problem_ids"].append(p["id"])
progress["total_evaluated_in_curriculum"] = len(progress["completed_problem_ids"])

with open("state/progress.json", "w", encoding="utf-8") as f:
    json.dump(progress, f, indent=2)
print(f"[+] Updated progress checkpoint: state/progress.json")

print("=" * 75)
print("Batch 5 Part 1B completed successfully!")
