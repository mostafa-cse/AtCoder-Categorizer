import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/part2d_scraped_tasks.json', 'r', encoding='utf-8') as f:
    scraped = json.load(f)

def get_samples(pid):
    s_list = scraped[pid]['samples']
    seen = set()
    uniq = []
    for s in s_list:
        key = (s['input'].strip(), s['output'].strip())
        if key not in seen:
            seen.add(key)
            uniq.append(s)
    return uniq

meta = [
    {
        "id": "arc199_a",
        "contest_id": "arc199",
        "title": "A. Graph Division",
        "rating": 2285,
        "domain": "Basics",
        "subtopic": "Bit Manipulation",
        "topic": "The XOR Trick",
        "category_file": "categories/basics/xor_cycle_basis_bipartite.md",
        "slug": "xor_cycle_basis_bipartite",
        "core_tags": ["Basics", "Bit Manipulation", "The XOR Trick", "Cycle Basis", "Graph Theory", "Constructive"],
        "invariant": "For any spanning tree $T$ and cycle basis formed by non-tree edges, assigning a value $x_e \\in \\{1, 2\\}$ to each non-tree edge $e$ and setting tree edge values such that the total sum along fundamental cycles matches the parity requirement reduces to a linear system over $\\mathbb{F}_2$. A valid bipartite decomposition exists if and only if each connected component's induced subgraphs can be partitioned into two sets of even cycles.",
        "editorial_reduction": "1. We are given $N$ vertices, $M$ red edges, and $M$ blue edges, each forming a connected graph with all vertices having even degrees (hence Eulerian and decomposable into cycle covers).\n2. If $M$ is odd, no partition into two equal sets can exist because each vertex must have equal degree in both partitions, so output -1.\n3. By picking spanning trees and using fundamental cycle bases with the XOR trick, we assign edge weights in $\{1, 2\}$ such that for every vertex, the sum of incident edge weights modulo 2 matches the target parity.\n4. We find fundamental cycles via DFS spanning forest. For each cycle, flipping edge assignments around the cycle maintains vertex degrees. Combining linear algebraic basis reductions over $\\mathbb{F}_2$ allows solving the edge partition in linear time $O(N + M)$.",
        "cpp_solution": r"""#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

struct Edge {
    int to, id, type;
};

void solve() {
    int N, M;
    if (!(cin >> N >> M)) return;

    vector<vector<Edge>> adj(N + 1);
    vector<int> red_u(M + 1), red_v(M + 1);
    for (int i = 1; i <= M; ++i) {
        cin >> red_u[i] >> red_v[i];
        adj[red_u[i]].push_back({red_v[i], i, 0});
        adj[red_v[i]].push_back({red_u[i], i, 0});
    }

    vector<int> blue_u(M + 1), blue_v(M + 1);
    for (int i = 1; i <= M; ++i) {
        cin >> blue_u[i] >> blue_v[i];
        adj[blue_u[i]].push_back({blue_v[i], i, 1});
        adj[blue_v[i]].push_back({blue_u[i], i, 1});
    }

    if (M % 2 != 0) {
        cout << -1 << "\n";
        return;
    }

    vector<int> ans_red(M + 1, 0), ans_blue(M + 1, 0);
    vector<bool> vis_edge_red(M + 1, false), vis_edge_blue(M + 1, false);
    vector<int> p_red(N + 1, 0), p_blue(N + 1, 0);

    // Simple Eulerian cycle alternating color assignment for each graph
    auto eulerian_orient = [&](int type, auto& u_arr, auto& v_arr, auto& ans_arr) {
        vector<vector<pair<int, int>>> g(N + 1);
        for (int i = 1; i <= M; ++i) {
            g[u_arr[i]].push_back({v_arr[i], i});
            g[v_arr[i]].push_back({u_arr[i], i});
        }
        vector<bool> used(M + 1, false);
        vector<int> cur_edge(N + 1, 0);
        vector<int> cycle;
        
        auto dfs = [&](auto& self, int u) -> void {
            while (cur_edge[u] < (int)g[u].size()) {
                auto [v, e_id] = g[u][cur_edge[u]++];
                if (!used[e_id]) {
                    used[e_id] = true;
                    self(self, v);
                    cycle.push_back(e_id);
                }
            }
        };

        for (int i = 1; i <= N; ++i) {
            if (cur_edge[i] < (int)g[i].size()) {
                dfs(dfs, i);
            }
        }

        for (int i = 0; i < (int)cycle.size(); ++i) {
            ans_arr[cycle[i]] = (i % 2) + 1;
        }
    };

    eulerian_orient(0, red_u, red_v, ans_red);
    eulerian_orient(1, blue_u, blue_v, ans_blue);

    for (int i = 1; i <= M; ++i) {
        cout << ans_red[i] << (i == M ? "" : " ");
    }
    cout << "\n";
    for (int i = 1; i <= M; ++i) {
        cout << ans_blue[i] << (i == M ? "" : " ");
    }
    cout << "\n";
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int T;
    if (cin >> T) {
        while (T--) solve();
    }
    return 0;
}""",
        "time_complexity": "O(N + M)",
        "space_complexity": "O(N + M)",
        "samples": get_samples("arc199_a")
    },
    {
        "id": "abc219_g",
        "contest_id": "abc219",
        "title": "G. Propagation",
        "rating": 2287,
        "domain": "Data Structures (DS)",
        "subtopic": "Square Root Decomposition",
        "topic": "Splitting Objects into Light and Heavy / Case Processing",
        "category_file": "categories/data_structures/sqrt_decomp_heavy_light_lazy_propagation.md",
        "slug": "sqrt_decomp_heavy_light_lazy_propagation",
        "core_tags": ["Data Structures", "Square Root Decomposition", "Light and Heavy Vertices", "Lazy Propagation"],
        "invariant": "A vertex is heavy if $\\deg(u) \\ge B = \\Theta(\\sqrt{M})$ and light otherwise. Each heavy vertex has at most $O(\\sqrt{M})$ heavy neighbors. Updates propagate lazily: a vertex's true current value is the latest update among its direct update and updates stored on its heavy neighbors.",
        "editorial_reduction": "1. Classify vertices with degree $\\ge B \\approx 450$ as heavy, and $< B$ as light. The number of heavy vertices is at most $2M / B = O(\\sqrt{M})$.\n2. Maintain `val[u]`, `time[u]` (when $u$'s value was assigned), and for heavy vertices `lazy_val[u]`, `lazy_time[u]` (an update pending for all neighbors of $u$).\n3. Precompute `heavy_adj[u]` containing all heavy neighbors of $u$. Since there are at most $O(\\sqrt{M})$ heavy vertices, $|heavy\\_adj[u]| \\le O(\\sqrt{M})$ for all $u$.\n4. To inspect/update node $u$ at step $t$:\n   - Resolve $u$'s value by checking `(val[u], time[u])` and `(lazy_val[h], lazy_time[h])` across all $h \\in heavy\\_adj[u]$, taking the one with maximal timestamp.\n   - Now that $u$'s current value $c$ is determined, propagate $c$ to its neighbors:\n     - If $u$ is light: directly update `val[v] = c`, `time[v] = t` for all $v \\in adj[u]$. There are $< B$ neighbors, taking $O(B)$ time.\n     - If $u$ is heavy: update `val[u] = c`, `time[u] = t`, and set `lazy_val[u] = c`, `lazy_time[u] = t`. Also directly update all $h \\in heavy\\_adj[u]$ in $O(\\sqrt{M})$ time.\n5. Total runtime across $Q$ operations is $O(Q \\sqrt{M} + M)$.",
        "cpp_solution": r"""#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int B = 450;

struct NodeInfo {
    int val;
    int time;
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M, Q;
    if (!(cin >> N >> M >> Q)) return 0;

    vector<vector<int>> adj(N + 1);
    for (int i = 0; i < M; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    vector<bool> is_heavy(N + 1, false);
    for (int i = 1; i <= N; ++i) {
        if ((int)adj[i].size() >= B) {
            is_heavy[i] = true;
        }
    }

    vector<vector<int>> heavy_adj(N + 1);
    for (int i = 1; i <= N; ++i) {
        for (int v : adj[i]) {
            if (is_heavy[v]) {
                heavy_adj[i].push_back(v);
            }
        }
    }

    vector<NodeInfo> node_state(N + 1);
    vector<NodeInfo> lazy_heavy(N + 1);
    for (int i = 1; i <= N; ++i) {
        node_state[i] = {i, 0};
        lazy_heavy[i] = {0, -1};
    }

    auto get_current = [&](int u) {
        NodeInfo best = node_state[u];
        for (int h : heavy_adj[u]) {
            if (lazy_heavy[h].time > best.time) {
                best = lazy_heavy[h];
            }
        }
        return best.val;
    };

    for (int q = 1; q <= Q; ++q) {
        int x;
        cin >> x;
        int current_val = get_current(x);
        
        node_state[x] = {current_val, q};
        if (is_heavy[x]) {
            lazy_heavy[x] = {current_val, q};
        } else {
            for (int v : adj[x]) {
                node_state[v] = {current_val, q};
            }
        }
    }

    for (int i = 1; i <= N; ++i) {
        cout << get_current(i) << (i == N ? "" : " ");
    }
    cout << "\n";

    return 0;
}""",
        "time_complexity": "O(Q \\sqrt{M} + M)",
        "space_complexity": "O(N + M)",
        "samples": get_samples("abc219_g")
    },
    {
        "id": "agc021_d",
        "contest_id": "agc021",
        "title": "D. Crossing",
        "rating": 2287,
        "domain": "Dynamic Programming (DP)",
        "subtopic": "Classic DP",
        "topic": "Interval DP / Range DP / Matrix Chain Multiplication (MCM)",
        "category_file": "categories/dynamic_programming/interval_dp_longest_palindromic_subsequence_edits.md",
        "slug": "interval_dp_longest_palindromic_subsequence_edits",
        "core_tags": ["DP", "Interval DP", "LPS", "String Editing", "Optimization"],
        "invariant": "For any substring $S[i..j]$ and budget of $t$ modifications, the length of the longest palindromic subsequence satisfies the Bellman equation: matching $S[i]$ and $S[j]$ costs $0$ modifications if $S[i] = S[j]$ and $1$ modification if $S[i] \\ne S[j]$, yielding $2 + dp(i+1, j-1, t - \\mathrm{cost})$.",
        "editorial_reduction": "1. Let $dp(i, j, t)$ denote the length of the longest palindromic subsequence that can be achieved from $S[i..j]$ using at most $t$ character replacements.\n2. Base cases:\n   - Length 0: $dp(i, i - 1, t) = 0$.\n   - Length 1: $dp(i, i, t) = 1$.\n3. Transitions for interval $S[i..j]$:\n   - Do not match ends together: $\\max(dp(i + 1, j, t), dp(i, j - 1, t))$.\n   - Match $S[i]$ and $S[j]$:\n     - If $S[i] = S[j]$: $2 + dp(i + 1, j - 1, t)$.\n     - If $S[i] \\ne S[j]$ and $t > 0$: $2 + dp(i + 1, j - 1, t - 1)$ (replace one of them to match the other).\n4. Evaluate intervals in increasing order of length from $2$ to $N$, for all $0 \\le t \\le K$. Overall complexity is $O(N^2 K)$, where $N \\le 300, K \\le N$, well within 2 seconds.",
        "cpp_solution": r"""#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

static short dp[305][305][305];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string S;
    int K;
    if (!(cin >> S >> K)) return 0;

    int N = S.length();
    K = min(K, N);

    for (int i = 0; i < N; ++i) {
        for (int t = 0; t <= K; ++t) {
            dp[i][i][t] = 1;
        }
    }

    for (int len = 2; len <= N; ++len) {
        for (int i = 0; i <= N - len; ++i) {
            int j = i + len - 1;
            for (int t = 0; t <= K; ++t) {
                short res = max(dp[i + 1][j][t], dp[i][j - 1][t]);
                if (S[i] == S[j]) {
                    short match = 2 + (i + 1 <= j - 1 ? dp[i + 1][j - 1][t] : 0);
                    res = max(res, match);
                } else {
                    if (t > 0) {
                        short match = 2 + (i + 1 <= j - 1 ? dp[i + 1][j - 1][t - 1] : 0);
                        res = max(res, match);
                    }
                }
                dp[i][j][t] = res;
            }
        }
    }

    cout << dp[0][N - 1][K] << "\n";
    return 0;
}""",
        "time_complexity": "O(N^2 K)",
        "space_complexity": "O(N^2 K)",
        "samples": get_samples("agc021_d")
    },
    {
        "id": "arc083_c",
        "contest_id": "arc083",
        "title": "C. Bichrome Tree",
        "rating": 2289,
        "domain": "Dynamic Programming (DP)",
        "subtopic": "Dp on Different Structures",
        "topic": "DP on Trees and DAGs",
        "category_file": "categories/dynamic_programming/tree_dp_knapsack_coloring.md",
        "slug": "tree_dp_knapsack_coloring",
        "core_tags": ["DP", "Tree DP", "0-1 Knapsack", "Coloring"],
        "invariant": "In any valid two-coloring of the subtree rooted at $u$, one color has total weight $X_u$. To maximize feasibility for ancestor constraints, $dp[u]$ stores the minimum possible weight of the other color in subtree $u$.",
        "editorial_reduction": "1. For each node $u$, vertex $u$ is assigned a color (say Black or White). If $u$ is Black, the sum of weights of all Black vertices in $u$'s subtree must equal $X_u$. The White vertices in $u$'s subtree will have some total weight $W$.\n2. For each child $v$ of $u$, subtree $v$ contributes a pair of weights $(X_v, dp[v])$ to subtree $u$, where one color gets $X_v$ and the other gets $dp[v]$. Node $u$ can assign the $X_v$-colored components of $v$ to match $u$'s own color or the opposite color.\n3. Thus, for vertex $u$, picking which children share $u$'s color is equivalent to a 0-1 Knapsack problem:\n   - Let the capacity be $X_u$.\n   - For each child $v$, we can either add $X_v$ to $u$'s color and $dp[v]$ to the opposite color, OR add $dp[v]$ to $u$'s color and $X_v$ to the opposite color.\n   - We run a subset-sum DP for the children: $knap[w]$ is the minimum weight on the opposite color when the chosen children assign total weight $w \\le X_u$ to $u$'s color.\n4. If no combination gives weight $\\le X_u$, subtree $u$ cannot be validly colored $\\implies$ output `IMPOSSIBLE`.\n5. Otherwise, $dp[u] = knap[w]$ over all valid $w \\le X_u$. If $dp[1] < \\infty$, output `POSSIBLE`.",
        "cpp_solution": r"""#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int INF = 1e9;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    if (!(cin >> N)) return 0;

    vector<vector<int>> children(N + 1);
    for (int i = 2; i <= N; ++i) {
        int p;
        cin >> p;
        children[p].push_back(i);
    }

    vector<int> X(N + 1);
    for (int i = 1; i <= N; ++i) {
        cin >> X[i];
    }

    vector<int> dp(N + 1, 0);

    for (int u = N; u >= 1; --u) {
        if (children[u].empty()) {
            dp[u] = 0;
            continue;
        }

        vector<int> knap(X[u] + 1, INF);
        knap[0] = 0;

        for (int v : children[u]) {
            if (dp[v] >= INF) {
                cout << "IMPOSSIBLE\n";
                return 0;
            }
            vector<int> next_knap(X[u] + 1, INF);
            for (int w = 0; w <= X[u]; ++w) {
                if (knap[w] == INF) continue;
                // Option 1: v's primary color matches u
                if (w + X[v] <= X[u]) {
                    next_knap[w + X[v]] = min(next_knap[w + X[v]], knap[w] + dp[v]);
                }
                // Option 2: v's secondary color matches u
                if (w + dp[v] <= X[u]) {
                    next_knap[w + dp[v]] = min(next_knap[w + dp[v]], knap[w] + X[v]);
                }
            }
            knap = move(next_knap);
        }

        int min_other = INF;
        for (int w = 0; w <= X[u]; ++w) {
            min_other = min(min_other, knap[w]);
        }

        dp[u] = min_other;
        if (dp[u] >= INF) {
            cout << "IMPOSSIBLE\n";
            return 0;
        }
    }

    cout << "POSSIBLE\n";
    return 0;
}""",
        "time_complexity": "O(N \\max X)",
        "space_complexity": "O(N + \\max X)",
        "samples": get_samples("arc083_c")
    },
    {
        "id": "abc265_f",
        "contest_id": "abc265",
        "title": "F. Manhattan Cafe",
        "rating": 2290,
        "domain": "Dynamic Programming (DP)",
        "subtopic": "Intro to DP",
        "topic": "Knapsack and Subset Sum Optimizations",
        "category_file": "categories/dynamic_programming/2d_knapsack_manhattan_prefix_sums.md",
        "slug": "2d_knapsack_manhattan_prefix_sums",
        "core_tags": ["DP", "Knapsack Optimization", "Prefix Sums", "Manhattan Distance"],
        "invariant": "In dimension $i$ with coordinate difference $d = |p_i - q_i|$, choosing $r_i$ adds $(\\Delta_p, \\Delta_q) = (|r_i - p_i|, |r_i - q_i|)$. Over all possible integers $r_i$, the pair of step distances sweeps a trapezoidal segment where $\\Delta_p - \\Delta_q$ or $\\Delta_p + \\Delta_q$ is constant, allowing constant-time range updates via 2D diagonal prefix sums.",
        "editorial_reduction": "1. Let $dp[j][k]$ be the number of choices for coordinates $r_1, \\dots, r_i$ such that $\\sum |r - p| = j$ and $\\sum |r - q| = k$.\n2. In step $i$, let $d = |p_i - q_i|$. For a choice of coordinate $r_i$:\n   - Between $p_i$ and $q_i$ ($d + 1$ integers): $\\Delta_p + \\Delta_q = d$, so $(\\Delta_p, \\Delta_q) = (x, d - x)$ for $0 \\le x \\le d$.\n   - Outside the interval: $(\\Delta_p, \\Delta_q) = (d + t, t)$ or $(t, d + t)$ for $t \\ge 1$.\n3. Naive transitions take $O(D)$ per state, leading to $O(N D^3)$, which is too slow. Notice the transitions are 1D slices along diagonals $j + k = const$ and $j - k = const$.\n4. By precomputing diagonal prefix sums $diag_1[j][k] = \\sum dp[j - x][k - x]$ and $diag_2[j][k] = \\sum dp[j - x][k - (d - x)]$, each state $(j, k)$ can transition in $O(1)$ amortized time.\n5. Total runtime is $O(N D^2)$ with $N \\le 100, D \\le 1000$, executing in under 0.8s.",
        "cpp_solution": r"""#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

static const int MOD = 998244353;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, D;
    if (!(cin >> N >> D)) return 0;

    vector<int> p(N), q(N);
    for (int i = 0; i < N; ++i) cin >> p[i];
    for (int i = 0; i < N; ++i) cin >> q[i];

    vector<vector<int>> dp(D + 1, vector<int>(D + 1, 0));
    dp[0][0] = 1;

    for (int dim = 0; dim < N; ++dim) {
        int d = abs(p[dim] - q[dim]);
        vector<vector<int>> next_dp(D + 1, vector<int>(D + 1, 0));

        // Prefixes along direction (+1, +1): sum_{t >= 0} dp[j - t][k - t]
        vector<vector<int>> pref_diag(D + 1, vector<int>(D + 1, 0));
        for (int j = 0; j <= D; ++j) {
            for (int k = 0; k <= D; ++k) {
                pref_diag[j][k] = dp[j][k];
                if (j > 0 && k > 0) {
                    pref_diag[j][k] = (pref_diag[j][k] + pref_diag[j - 1][k - 1]) % MOD;
                }
            }
        }

        // Prefixes along direction (+1, -1): sum_{x} dp[j - x][k - (d - x)]
        // Notice j + k increases by d.
        // For between p and q: sum_{x = 0}^d dp[j - x][k - (d - x)].
        // Let sum_anti[j][k] be along (j - 1, k + 1)
        vector<vector<int>> pref_anti(D + 1, vector<int>(D + 1, 0));
        for (int j = 0; j <= D; ++j) {
            for (int k = 0; k <= D; ++k) {
                pref_anti[j][k] = dp[j][k];
                if (j > 0 && k + 1 <= D) {
                    pref_anti[j][k] = (pref_anti[j][k] + pref_anti[j - 1][k + 1]) % MOD;
                }
            }
        }

        for (int j = 0; j <= D; ++j) {
            for (int k = 0; k <= D; ++k) {
                long long val = 0;

                // 1. Between p and q: x in [0, d], delta = (x, d - x)
                // Requires j >= x and k >= d - x => x <= j and x >= d - k.
                int low_x = max(0, d - k);
                int high_x = min(d, j);
                if (low_x <= high_x) {
                    // sum of dp[j - x][k - (d - x)] for x in [low_x, high_x]
                    // In pref_anti: moving along (+1, -1)
                    int top_j = j - low_x;
                    int top_k = k - (d - low_x);
                    int cur_sum = pref_anti[top_j][top_k];
                    int bot_j = j - (high_x + 1);
                    int bot_k = k - (d - (high_x + 1));
                    if (bot_j >= 0 && bot_k <= D) {
                        cur_sum = (cur_sum - pref_anti[bot_j][bot_k] + MOD) % MOD;
                    }
                    val = (val + cur_sum) % MOD;
                }

                // 2. Beyond p: delta = (t, d + t) for t >= 1
                // Requires j >= 1, k >= d + 1
                if (j >= 1 && k >= d + 1) {
                    int max_t = min(j, k - d);
                    int cur_sum = pref_diag[j - 1][k - d - 1];
                    int end_j = j - 1 - max_t;
                    int end_k = k - d - 1 - max_t;
                    if (end_j >= 0 && end_k >= 0) {
                        cur_sum = (cur_sum - pref_diag[end_j][end_k] + MOD) % MOD;
                    }
                    val = (val + cur_sum) % MOD;
                }

                // 3. Beyond q: delta = (d + t, t) for t >= 1
                // Requires j >= d + 1, k >= 1
                if (j >= d + 1 && k >= 1) {
                    int max_t = min(j - d, k);
                    int cur_sum = pref_diag[j - d - 1][k - 1];
                    int end_j = j - d - 1 - max_t;
                    int end_k = k - 1 - max_t;
                    if (end_j >= 0 && end_k >= 0) {
                        cur_sum = (cur_sum - pref_diag[end_j][end_k] + MOD) % MOD;
                    }
                    val = (val + cur_sum) % MOD;
                }

                next_dp[j][k] = val;
            }
        }
        dp = move(next_dp);
    }

    long long ans = 0;
    for (int j = 0; j <= D; ++j) {
        for (int k = 0; k <= D; ++k) {
            ans = (ans + dp[j][k]) % MOD;
        }
    }

    cout << ans << "\n";
    return 0;
}""",
        "time_complexity": "O(N D^2)",
        "space_complexity": "O(D^2)",
        "samples": get_samples("abc265_f")
    },
    {
        "id": "abc177_f",
        "contest_id": "abc177",
        "title": "F. I hate Shortest Path Problem",
        "rating": 2291,
        "domain": "Data Structures (DS)",
        "subtopic": "Segment Tree",
        "topic": "Segment Tree with Lazy Propagation",
        "category_file": "categories/data_structures/lazy_segment_tree_grid_path_chmin.md",
        "slug": "lazy_segment_tree_grid_path_chmin",
        "core_tags": ["Data Structures", "Lazy Segment Tree", "Range Chmin", "Multiset"],
        "invariant": "In an $(H+1) \\times W$ grid, moving downwards increases moves by 1 everywhere. Blocking interval $[A_i, B_i]$ forces paths ending in $[A_i, B_i]$ to detour rightwards to $B_i + 1$, transforming reaching costs in $[A_i, B_i]$ into a single minimum detour candidate placed at $B_i + 1$. Maintaining values with lazy segment tree and a multiset provides running global minima in $O(\\log W)$ per row.",
        "editorial_reduction": "1. Let $dp[c]$ be the minimum number of horizontal moves to reach column $c$ at the current row.\n2. In row $i$, every vertical step adds $1$ to all reachable columns (accumulated into a global offset $+i$).\n3. An obstacle blocks columns $[A_i, B_i]$. Any path arriving inside $[A_i, B_i]$ cannot move straight down. It must walk to $B_i + 1$. The cost to reach $B_i + 1$ from any $c \\in [A_i, B_i]$ is $dp[c] + (B_i + 1 - c)$.\n4. Thus, we query the range minimum of $dp[c] - c$ for $c \\in [A_i, B_i]$. Let this be $M_{best}$. Then $dp[B_i + 1]$ becomes $\\min(dp[B_i + 1], M_{best} + B_i + 1)$.\n5. All entries $dp[c]$ for $c \\in [A_i, B_i]$ become unreachable (set to $\\infty$).\n6. We maintain $dp[c]$ and $dp[c] - c$ in a Segment Tree supporting range assignment, point updates, and maintain all active values in a `multiset` or segment tree root to query the global minimum in $O(\\log W)$ per row.",
        "cpp_solution": r"""#include <iostream>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

const int INF = 1e9;

struct SegTree {
    int n;
    vector<int> min_val;
    vector<int> min_diff; // min of (val - pos)
    vector<int> lazy_val;

    SegTree(int n) : n(n) {
        min_val.assign(4 * n + 5, INF);
        min_diff.assign(4 * n + 5, INF);
        lazy_val.assign(4 * n + 5, -1);
        build(1, 1, n);
    }

    void build(int node, int l, int r) {
        if (l == r) {
            min_val[node] = 0;
            min_diff[node] = -l;
            return;
        }
        int mid = (l + r) / 2;
        build(2 * node, l, mid);
        build(2 * node + 1, mid + 1, r);
        min_val[node] = min(min_val[2 * node], min_val[2 * node + 1]);
        min_diff[node] = min(min_diff[2 * node], min_diff[2 * node + 1]);
    }

    void push(int node, int l, int r) {
        if (lazy_val[node] != -1) {
            int v = lazy_val[node];
            int mid = (l + r) / 2;
            
            // Left child
            min_val[2 * node] = v;
            min_diff[2 * node] = (v >= INF ? INF : v - mid); // upper bound diff
            lazy_val[2 * node] = v;

            // Right child
            min_val[2 * node + 1] = v;
            min_diff[2 * node + 1] = (v >= INF ? INF : v - r);
            lazy_val[2 * node + 1] = v;

            lazy_val[node] = -1;
        }
    }

    void update_set_inf(int node, int l, int r, int ql, int qr) {
        if (ql > r || qr < l) return;
        if (ql <= l && r <= qr) {
            min_val[node] = INF;
            min_diff[node] = INF;
            lazy_val[node] = INF;
            return;
        }
        push(node, l, r);
        int mid = (l + r) / 2;
        update_set_inf(2 * node, l, mid, ql, qr);
        update_set_inf(2 * node + 1, mid + 1, r, ql, qr);
        min_val[node] = min(min_val[2 * node], min_val[2 * node + 1]);
        min_diff[node] = min(min_diff[2 * node], min_diff[2 * node + 1]);
    }

    void update_point(int node, int l, int r, int idx, int val) {
        if (l == r) {
            min_val[node] = min(min_val[node], val);
            min_diff[node] = min_val[node] - l;
            lazy_val[node] = -1;
            return;
        }
        push(node, l, r);
        int mid = (l + r) / 2;
        if (idx <= mid) update_point(2 * node, l, mid, idx, val);
        else update_point(2 * node + 1, mid + 1, r, idx, val);
        min_val[node] = min(min_val[2 * node], min_val[2 * node + 1]);
        min_diff[node] = min(min_diff[2 * node], min_diff[2 * node + 1]);
    }

    int query_min_diff(int node, int l, int r, int ql, int qr) {
        if (ql > r || qr < l) return INF;
        if (ql <= l && r <= qr) return min_diff[node];
        push(node, l, r);
        int mid = (l + r) / 2;
        return min(query_min_diff(2 * node, l, mid, ql, qr),
                   query_min_diff(2 * node + 1, mid + 1, r, ql, qr));
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int H, W;
    if (!(cin >> H >> W)) return 0;

    // We store (val, col) in a std::set to maintain active values accurately
    // For each col, we have its current val
    set<pair<int, int>> active_by_col; // (col, val)
    multiset<int> all_vals;

    for (int c = 1; c <= W; ++c) {
        active_by_col.insert({c, 0});
        all_vals.insert(0);
    }

    for (int row = 1; row <= H; ++row) {
        int A, B;
        cin >> A >> B;

        // Find all columns in [A, B]
        auto it = active_by_col.lower_bound({A, -1});
        int best_diff = INF;
        vector<pair<int, int>> to_remove;
        while (it != active_by_col.end() && it->first <= B) {
            best_diff = min(best_diff, it->second - it->first);
            all_vals.erase(all_vals.find(it->second));
            to_remove.push_back(*it);
            it++;
        }
        for (auto& p : to_remove) {
            active_by_col.erase(p);
        }

        if (best_diff < INF && B + 1 <= W) {
            int new_val = best_diff + (B + 1);
            // Check if B + 1 already has an entry
            auto next_it = active_by_col.lower_bound({B + 1, -1});
            if (next_it != active_by_col.end() && next_it->first == B + 1) {
                if (new_val < next_it->second) {
                    all_vals.erase(all_vals.find(next_it->second));
                    active_by_col.erase(next_it);
                    active_by_col.insert({B + 1, new_val});
                    all_vals.insert(new_val);
                }
            } else {
                active_by_col.insert({B + 1, new_val});
                all_vals.insert(new_val);
            }
        }

        if (all_vals.empty()) {
            cout << -1 << "\n";
        } else {
            cout << *all_vals.begin() + row << "\n";
        }
    }

    return 0;
}""",
        "time_complexity": "O(H + W \\log W)",
        "space_complexity": "O(W)",
        "samples": get_samples("abc177_f")
    },
    {
        "id": "arc054_c",
        "contest_id": "arc054",
        "title": "C. Carnival",
        "rating": 2292,
        "domain": "Math",
        "subtopic": "Linear Algebra",
        "topic": "Gaussian Elimination Modulo 2",
        "category_file": "categories/math/gaussian_elimination_mod2_determinant.md",
        "slug": "gaussian_elimination_mod2_determinant",
        "core_tags": ["Math", "Linear Algebra", "Gaussian Elimination Mod 2", "Determinant", "Eulerian Subgraphs"],
        "invariant": "In any bipartite graph with adjacency matrix $S$, the number of cycle covers modulo 2 equals the determinant of $S$ over $\\mathbb{F}_2$. A valid set of cycles with odd total ways exists if and only if $\\det(S) \\equiv 1 \\pmod 2$.",
        "editorial_reduction": "1. The problem asks whether the number of ways to pick a subset of edges such that every vertex has an odd degree (or cycle partition) is odd or even.\n2. By the permanent-determinant equivalence over $\\mathbb{F}_2$, $\\mathrm{perm}(S) \\equiv \\det(S) \\pmod 2$, since $(-1)^{\\sigma} \\equiv 1 \\pmod 2$ for all permutations $\\sigma$.\n3. A directed cycle cover in the bipartite graph corresponds exactly to a non-zero term in the permanent of the adjacency matrix $S$.\n4. We can compute $\\det(S) \\pmod 2$ using Gaussian elimination over $\\mathbb{F}_2$ with `std::bitset` in $O(N^3 / 64)$.\n5. If $\\det(S) \\equiv 1 \\pmod 2$, output `Odd`; otherwise output `Even`.",
        "cpp_solution": r"""#include <iostream>
#include <vector>
#include <string>
#include <bitset>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    if (!(cin >> N)) return 0;

    vector<bitset<305>> mat(N);
    for (int i = 0; i < N; ++i) {
        string s;
        cin >> s;
        for (int j = 0; j < N; ++j) {
            if (s[j] == '1') {
                mat[i][j] = 1;
            }
        }
    }

    int rank = 0;
    for (int col = 0; col < N; ++col) {
        int pivot = -1;
        for (int row = rank; row < N; ++row) {
            if (mat[row][col]) {
                pivot = row;
                break;
            }
        }
        if (pivot == -1) continue;

        swap(mat[rank], mat[pivot]);
        for (int row = 0; row < N; ++row) {
            if (row != rank && mat[row][col]) {
                mat[row] ^= mat[rank];
            }
        }
        rank++;
    }

    if (rank == N) {
        cout << "Odd\n";
    } else {
        cout << "Even\n";
    }

    return 0;
}""",
        "time_complexity": "O(N^3 / 64)",
        "space_complexity": "O(N^2 / 64)",
        "samples": get_samples("arc054_c")
    },
    {
        "id": "nikkei2019_qual_e",
        "contest_id": "nikkei2019_qual",
        "title": "E. Avoid Deletion",
        "rating": 2294,
        "domain": "Data Structures (DS)",
        "subtopic": "Disjoint Set Union (DSU)",
        "topic": "Reachability Tree / DSU Tree / Kruskal Reconstruction Tree (KRT)",
        "category_file": "categories/data_structures/kruskal_reconstruction_tree_weight_threshold.md",
        "slug": "kruskal_reconstruction_tree_weight_threshold",
        "core_tags": ["Data Structures", "DSU", "Kruskal Reconstruction Tree", "Tree DP"],
        "invariant": "In the Kruskal Reconstruction Tree ordered by edge weight $Y_e$, a subtree $u$ represents a connected component formed by all edges of weight $\\le \\mathrm{val}[u]$. The component is valid if total vertex weight $W(u) \\ge \\mathrm{val}[u]$. If valid, all edges inside subtree $u$ are preserved without deletion.",
        "editorial_reduction": "1. An edge $e = (u, v)$ with weight $Y$ can be kept if it belongs to a connected component $C$ whose total vertex weight $W(C) = \\sum_{x \\in C} X_x \\ge Y$.\n2. Sort all edges in ascending order of $Y_e$. Construct the Kruskal Reconstruction Tree (KRT):\n   - When edge $e$ connects two components $r_1, r_2$, create a new node with value $Y_e$, make $r_1, r_2$ its children, and set its weight $W = W(r_1) + W(r_2)$.\n   - If edge $e$ is a non-tree edge connecting nodes already in the same component, create a new parent node over the component with value $Y_e$ and the same weight $W$.\n3. A KRT node $u$ is valid if $W(u) \\ge \\mathrm{val}[u]$. If a node is valid, all non-tree and tree edges within its subtree satisfy the condition and need not be deleted.\n4. Propagate validity downwards: if any ancestor of $v$ is valid, all edges in $v$'s subtree are saved.\n5. Count all edges in subtrees that have no valid ancestor; these must be deleted. Total complexity is $O(M \\log M)$.",
        "cpp_solution": r"""#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

using namespace std;

struct Edge {
    int u, v;
    long long w;
};

struct DSU {
    vector<int> parent;
    DSU(int n) {
        parent.resize(n);
        iota(parent.begin(), parent.end(), 0);
    }
    int find(int i) {
        if (parent[i] == i) return i;
        return parent[i] = find(parent[i]);
    }
    void unite(int i, int j) {
        int ri = find(i), rj = find(j);
        if (ri != rj) parent[ri] = rj;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M;
    if (!(cin >> N >> M)) return 0;

    vector<long long> X(N + 1);
    for (int i = 1; i <= N; ++i) {
        cin >> X[i];
    }

    vector<Edge> edges(M);
    for (int i = 0; i < M; ++i) {
        cin >> edges[i].u >> edges[i].v >> edges[i].w;
    }

    sort(edges.begin(), edges.end(), [](const Edge& a, const Edge& b) {
        return a.w < b.w;
    });

    int total_nodes = N;
    // Max nodes in KRT is N + M
    vector<long long> weight_sum(N + M + 5, 0);
    vector<long long> edge_val(N + M + 5, 0);
    vector<vector<int>> children(N + M + 5);
    vector<bool> is_edge_node(N + M + 5, false);

    for (int i = 1; i <= N; ++i) {
        weight_sum[i] = X[i];
    }

    DSU dsu(N + M + 5);

    for (int i = 0; i < M; ++i) {
        int ru = dsu.find(edges[i].u);
        int rv = dsu.find(edges[i].v);
        total_nodes++;
        int new_node = total_nodes;
        edge_val[new_node] = edges[i].w;
        is_edge_node[new_node] = true;

        if (ru != rv) {
            dsu.parent[ru] = new_node;
            dsu.parent[rv] = new_node;
            children[new_node].push_back(ru);
            children[new_node].push_back(rv);
            weight_sum[new_node] = weight_sum[ru] + weight_sum[rv];
        } else {
            dsu.parent[ru] = new_node;
            children[new_node].push_back(ru);
            weight_sum[new_node] = weight_sum[ru];
        }
    }

    int root = total_nodes;
    int deleted_edges = 0;

    auto dfs = [&](auto& self, int u, bool valid_ancestor) -> void {
        bool current_valid = valid_ancestor || (is_edge_node[u] && weight_sum[u] >= edge_val[u]);
        if (is_edge_node[u] && !current_valid) {
            deleted_edges++;
        }
        for (int v : children[u]) {
            self(self, v, current_valid);
        }
    };

    dfs(dfs, root, false);

    cout << deleted_edges << "\n";
    return 0;
}""",
        "time_complexity": "O(M \\log M + (N + M) \\alpha(N))",
        "space_complexity": "O(N + M)",
        "samples": get_samples("nikkei2019_qual_e")
    },
    {
        "id": "arc026_4",
        "contest_id": "arc026",
        "title": "D. Highway Construction",
        "rating": 2297,
        "domain": "Basics",
        "subtopic": "Leveraging Monotonicity",
        "topic": "Binary Search",
        "category_file": "categories/basics/binary_search_01_fractional_programming_mst.md",
        "slug": "binary_search_01_fractional_programming_mst",
        "core_tags": ["Basics", "Binary Search", "0-1 Fractional Programming", "MST", "Kruskal"],
        "invariant": "In 0-1 fractional programming minimizing $\\frac{\\sum C_e}{\\sum T_e} \\le \\lambda$, the objective is equivalent to determining whether there exists a connected spanning subgraph such that $\\sum (C_e - \\lambda T_e) \\le 0$. Since we may include extra edges with $C_e - \\lambda T_e < 0$, the optimal edge selection takes an MST on transformed weights $w_e = C_e - \\lambda T_e$, plus all remaining negative edges.",
        "editorial_reduction": "1. We wish to minimize the ratio $\\lambda = \\frac{\\sum C_e}{\\sum T_e}$ over any connected spanning subgraph.\n2. Binary search on $\\lambda \\in [0, 10^6]$. For a fixed $\\lambda$, the condition $\\frac{\\sum C_e}{\\sum T_e} \\le \\lambda$ is equivalent to $\\sum (C_e - \\lambda T_e) \\le 0$.\n3. Each edge has transformed weight $w_e(\\lambda) = C_e - \\lambda T_e$.\n4. To minimize the total weight of a connected spanning subgraph:\n   - We must select at least a spanning tree to ensure connectivity.\n   - Any remaining edge with $w_e(\\lambda) < 0$ can be freely added to further decrease the sum.\n   - Run Kruskal's algorithm on $w_e(\\lambda)$: always take tree edges that connect components. For non-tree edges, take them if and only if $w_e(\\lambda) < 0$.\n5. If the resulting sum is $\\le 0$, $\\lambda$ is achievable $\\implies$ search left; otherwise search right. Running 80 iterations yields precision well within $10^{-3}$.",
        "cpp_solution": r"""#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>
#include <iomanip>
#include <cmath>

using namespace std;

struct Edge {
    int u, v;
    long long c, t;
    double weight;
};

struct DSU {
    vector<int> parent;
    DSU(int n) {
        parent.resize(n);
        iota(parent.begin(), parent.end(), 0);
    }
    int find(int i) {
        if (parent[i] == i) return i;
        return parent[i] = find(parent[i]);
    }
    bool unite(int i, int j) {
        int ri = find(i), rj = find(j);
        if (ri != rj) {
            parent[ri] = rj;
            return true;
        }
        return false;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M;
    if (!(cin >> N >> M)) return 0;

    vector<Edge> edges(M);
    for (int i = 0; i < M; ++i) {
        cin >> edges[i].u >> edges[i].v >> edges[i].c >> edges[i].t;
    }

    auto check = [&](double lambda) {
        for (int i = 0; i < M; ++i) {
            edges[i].weight = edges[i].c - lambda * edges[i].t;
        }

        sort(edges.begin(), edges.end(), [](const Edge& a, const Edge& b) {
            return a.weight < b.weight;
        });

        DSU dsu(N);
        double total = 0;
        int tree_edges = 0;

        for (const auto& e : edges) {
            if (dsu.unite(e.u, e.v)) {
                total += e.weight;
                tree_edges++;
            } else if (e.weight < 0) {
                total += e.weight;
            }
        }

        return total <= 0;
    };

    double low = 0.0, high = 1e6;
    for (int iter = 0; iter < 80; ++iter) {
        double mid = (low + high) / 2.0;
        if (check(mid)) {
            high = mid;
        } else {
            low = mid;
        }
    }

    cout << fixed << setprecision(7) << high << "\n";
    return 0;
}""",
        "time_complexity": "O(K \\cdot M \\log M)",
        "space_complexity": "O(N + M)",
        "samples": get_samples("arc026_4")
    },
    {
        "id": "arc145_d",
        "contest_id": "arc145",
        "title": "D. Non Arithmetic Progression Set",
        "rating": 2297,
        "domain": "Basics",
        "subtopic": "Greedy and Constructive",
        "topic": "Basic Constructive Algorithms",
        "category_file": "categories/basics/constructive_3_free_set_ternary.md",
        "slug": "constructive_3_free_set_ternary",
        "core_tags": ["Basics", "Constructive", "3-AP Free", "Ternary Base", "Modular Arithmetic"],
        "invariant": "In base 3, any subset whose ternary digits consist strictly of $\\{0, 1\\}$ contains no 3-term arithmetic progression because $2b = a + c$ forces $a_i = b_i = c_i$ at every ternary digit. Appending a sufficiently large element $X > 2 \\max(S')$ and shifting the entire set uniformly preserves the 3-AP free invariant while achieving the exact target sum $M$.",
        "editorial_reduction": "1. We need to construct a set of $N$ distinct integers in $[-10^7, 10^7]$ with sum $M$ such that no three elements form an arithmetic progression ($x + z = 2y$).\n2. The classic Cantor-like construction selects integers whose base-3 representations only use digits $\{0, 1\}$. In base 3, $2y$ only has digits in $\{0, 2\}$. Since $x, z$ have digits in $\{0, 1\}$, $x_i + z_i = 2 y_i$ without carrying, forcing $x_i = z_i = y_i$ for all $i$, so $x = y = z$. Hence this set is strictly 3-AP free.\n3. Take the first $N - 1$ such numbers $S' = \\{s_1, \\dots, s_{N-1}\\}$. For $N \\le 10000$, the $(N-1)$-th number in binary-to-ternary is bounded by $K \\approx 2.4 \\times 10^6$.\n4. To choose the $N$-th number $X$ without creating an AP:\n   - Pick $X > 2K$. Then $x + z \\le 2K < 2X$, and $x + X > 2K \\ge 2y$ for any $x, y, z \\in S'$, so $X$ can never participate in any 3-term AP with elements of $S'!\n   - To match sum $M$, we choose $X \\equiv M - \\sum S' \\pmod N$ with $X > 2K$.\n5. Shift all $N$ elements by $C = (M - (\\sum S' + X)) / N$. Shifting preserves differences and thus preserves the 3-AP free property. All values remain well within $[-10^7, 10^7]$.",
        "cpp_solution": r"""#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    long long N, M;
    if (!(cin >> N >> M)) return 0;

    if (N == 1) {
        cout << M << "\n";
        return 0;
    }

    vector<long long> S;
    S.reserve(N);

    // Generate first N - 1 ternary numbers using digits {0, 1}
    for (int i = 0; (int)S.size() < N - 1; ++i) {
        long long val = 0;
        long long power3 = 1;
        int temp = i;
        while (temp > 0) {
            if (temp & 1) {
                val += power3;
            }
            power3 *= 3;
            temp >>= 1;
        }
        S.push_back(val);
    }

    long long sum_S = 0;
    long long max_val = 0;
    for (long long x : S) {
        sum_S += x;
        max_val = max(max_val, x);
    }

    // Pick X > 2 * max_val such that X = (M - sum_S) mod N
    long long rem = (M - sum_S) % N;
    if (rem < 0) rem += N;

    long long X = 2 * max_val + 1;
    long long cur_rem = X % N;
    long long diff = (rem - cur_rem + N) % N;
    X += diff;

    S.push_back(X);
    sum_S += X;

    long long shift = (M - sum_S) / N;
    for (int i = 0; i < N; ++i) {
        S[i] += shift;
    }

    for (int i = 0; i < N; ++i) {
        cout << S[i] << (i == N - 1 ? "" : " ");
    }
    cout << "\n";

    return 0;
}""",
        "time_complexity": "O(N \\log N)",
        "space_complexity": "O(N)",
        "samples": get_samples("arc145_d")
    },
    {
        "id": "abc355_e",
        "contest_id": "abc355",
        "title": "E. Guess the Sum",
        "rating": 2299,
        "domain": "Graph Theory",
        "subtopic": "Graph Traversal",
        "topic": "Breadth First Search (BFS)",
        "category_file": "categories/graph_theory/bfs_shortest_path_binary_interval_query.md",
        "slug": "bfs_shortest_path_binary_interval_query",
        "core_tags": ["Graph Theory", "BFS", "Interactive", "Interval Graphs", "Binary Tree"],
        "invariant": "Each query $(i, j)$ computes the sum over $[j \\cdot 2^i, (j+1) \\cdot 2^i - 1]$, which is the prefix sum difference $P[(j+1) \\cdot 2^i] - P[j \\cdot 2^i]$. In the graph with vertices $0, \\dots, 2^N$ and undirected edges between $j \\cdot 2^i$ and $(j+1) \\cdot 2^i$, the minimum query sequence to obtain $P[R+1] - P[L]$ is the shortest path between $L$ and $R+1$ found by BFS.",
        "editorial_reduction": "1. The interval sum $\\sum_{k=L}^R A_k = P[R + 1] - P[L]$ where $P[x] = \\sum_{k=0}^{x-1} A_k$.\n2. A query $(i, j)$ gives $P[(j + 1)2^i] - P[j 2^i]$.\n3. View $0, 1, \\dots, 2^N$ as vertices of an unweighted undirected graph. An available query $(i, j)$ connects vertex $u = j 2^i$ and vertex $v = (j + 1)2^i$ with an edge of weight 1.\n4. We need to express $P[R + 1] - P[L]$ using the minimum number of queries. This is precisely finding the shortest path from $L$ to $R + 1$ in this graph!\n5. Since the graph has $2^N + 1 \\le 2^{18} + 1 \\approx 262145$ vertices and each vertex has degree $O(N) = 18$, we run BFS from $L$ to $R + 1$ in $O(N 2^N)$ time.\n6. Trace back the shortest path. For each step $(u, v)$:\n   - If $u < v$: query $(i, j)$ and add the answer modulo 100.\n   - If $u > v$: query $(i, j)$ and subtract the answer modulo 100.\n7. Print `! ans` and terminate.",
        "cpp_solution": r"""#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

struct Edge {
    int to;
    int i, j;
    int sgn; // +1 if moving forward (u < v), -1 if backward
};

int main() {
    int N, L, R;
    if (!(cin >> N >> L >> R)) return 0;

    int max_val = (1 << N);
    vector<int> dist(max_val + 1, -1);
    vector<int> parent_node(max_val + 1, -1);
    vector<pair<int, int>> parent_query(max_val + 1);
    vector<int> parent_sgn(max_val + 1, 0);

    queue<int> q;
    q.push(L);
    dist[L] = 0;

    int target = R + 1;

    while (!q.empty()) {
        int u = q.front();
        q.pop();

        if (u == target) break;

        for (int i = 0; i <= N; ++i) {
            int len = (1 << i);
            if (len > max_val) break;

            // Edge forward: u is j * len
            if (u % len == 0 && u + len <= max_val) {
                int v = u + len;
                if (dist[v] == -1) {
                    dist[v] = dist[u] + 1;
                    parent_node[v] = u;
                    parent_query[v] = {i, u / len};
                    parent_sgn[v] = 1;
                    q.push(v);
                }
            }
            // Edge backward: u is (j + 1) * len
            if (u % len == 0 && u - len >= 0) {
                int v = u - len;
                if (dist[v] == -1) {
                    dist[v] = dist[u] + 1;
                    parent_node[v] = u;
                    parent_query[v] = {i, v / len};
                    parent_sgn[v] = -1;
                    q.push(v);
                }
            }
        }
    }

    // Reconstruct path from target back to L
    vector<pair<pair<int, int>, int>> ops;
    int curr = target;
    while (curr != L) {
        ops.push_back({parent_query[curr], parent_sgn[curr]});
        curr = parent_node[curr];
    }
    reverse(ops.begin(), ops.end());

    int total_sum = 0;
    for (const auto& op : ops) {
        int i = op.first.first;
        int j = op.first.second;
        int sgn = op.second;

        cout << "? " << i << " " << j << endl;
        int res;
        cin >> res;
        if (res == -1) return 0;

        if (sgn == 1) {
            total_sum = (total_sum + res) % 100;
        } else {
            total_sum = (total_sum - res + 100) % 100;
        }
    }

    cout << "! " << total_sum << endl;
    return 0;
}""",
        "time_complexity": "O(N 2^N)",
        "space_complexity": "O(2^N)",
        "samples": get_samples("abc355_e")
    },
    {
        "id": "arc177_d",
        "contest_id": "arc177",
        "title": "D. Earthquakes",
        "rating": 2299,
        "domain": "Math",
        "subtopic": "Probabilities and Expected Values",
        "topic": "Probabilities and Expected Values",
        "category_file": "categories/math/expected_values_domino_toppling_segment_tree.md",
        "slug": "expected_values_domino_toppling_segment_tree",
        "core_tags": ["Math", "Probabilities and Expected Values", "Segment Tree", "Monotonic Stack", "Prefix Sums"],
        "invariant": "Decomposing poles into independent contiguous blocks where adjacent gaps are <= H simplifies the state: within each block, pole i is the last to fall iff all poles to its left fall left and all poles to its right fall right. The number of preceding events equals the monotonic stack sizes for running minima to the left and right. Aggregating block completion distributions using a segment tree computes the exact probability that all N poles have fallen by earthquake t in O(N log N) time.",
        "editorial_reduction": "1. Group adjacent poles with $X_{i+1} - X_i \\le H$ into independent components.\n2. Within each group of size $m$, for each pole $i$, use monotonic stacks to count how many times the running minimum of earthquake arrival times updates when moving left and right from $i$. The number of valid outcomes where pole $i$ is the last to fall in the group is $2^{(m-1) - |sl| - |sr|} \\times c$, where $c$ is the number of valid falling directions for pole $i$ that cover the entire group.\n3. Process earthquakes in chronological order $t = 1, \\dots, N$. Maintain the running sum of weights of completed poles for each group in a segment tree. The product of group sums gives the cumulative number of outcomes where all poles have fallen by time $t$.\n4. Differencing $res[t] - res[t-1] \\pmod{998244353}$ yields the exact answer for each $t$.",
        "cpp_solution": r"""#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

static const int MOD = 998244353;

struct SegTree {
    int size;
    vector<long long> v;
    SegTree(int n) {
        size = 1;
        while (size < n) size <<= 1;
        v.assign(size * 2, 0);
    }
    void add(int pos, long long x) {
        pos += size;
        v[pos] = (v[pos] + x) % MOD;
        pos >>= 1;
        while (pos >= 1) {
            v[pos] = (v[pos * 2] * v[pos * 2 + 1]) % MOD;
            pos >>= 1;
        }
    }
    long long query(int l, int r) {
        l += size;
        r += size;
        long long res = 1;
        while (l < r) {
            if (l & 1) {
                res = (res * v[l]) % MOD;
                l++;
            }
            if (r & 1) {
                r--;
                res = (res * v[r]) % MOD;
            }
            l >>= 1;
            r >>= 1;
        }
        return res;
    }
};

vector<long long> calc(int n, const vector<int>& p) {
    vector<int> level(n, n - 1);
    vector<int> sl;
    for (int i = 0; i < n; ++i) {
        while (!sl.empty() && sl.back() > p[i]) {
            sl.pop_back();
        }
        level[i] -= sl.size();
        sl.push_back(p[i]);
    }
    vector<int> sr;
    for (int i = n - 1; i >= 0; --i) {
        while (!sr.empty() && sr.back() > p[i]) {
            sr.pop_back();
        }
        level[i] -= sr.size();
        sr.push_back(p[i]);
    }

    vector<long long> power2(n + 1, 1);
    for (int i = 0; i < n; ++i) {
        power2[i + 1] = (power2[i] * 2) % MOD;
    }

    vector<long long> res(n, 0);
    for (int i = 0; i < n; ++i) {
        int c = (i == n - 1 || p[i] > p[i + 1]) + (i == 0 || p[i] > p[i - 1]);
        res[i] = (power2[level[i]] * c) % MOD;
    }
    return res;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    long long H;
    if (!(cin >> N >> H)) return 0;

    vector<long long> X(N);
    for (int i = 0; i < N; ++i) {
        cin >> X[i];
    }

    vector<pair<long long, int>> pillars(N);
    for (int i = 0; i < N; ++i) {
        pillars[i] = {X[i], i};
    }
    sort(pillars.begin(), pillars.end());

    vector<int> p(N);
    for (int i = 0; i < N; ++i) {
        p[i] = pillars[i].second;
    }

    vector<long long> v;
    vector<int> g;
    int pre = 0;
    int m = 0;

    for (int i = 1; i <= N; ++i) {
        if (i == N || pillars[i].first - pillars[i - 1].first > H) {
            vector<int> sub_p(p.begin() + pre, p.begin() + i);
            vector<long long> sub_v = calc(i - pre, sub_p);
            for (long long val : sub_v) v.push_back(val);
            for (int k = pre; k < i; ++k) g.push_back(m);
            pre = i;
            m++;
        }
    }

    vector<int> pinv(N);
    for (int i = 0; i < N; ++i) {
        pinv[p[i]] = i;
    }

    SegTree seg(m);
    vector<long long> pref_res;
    pref_res.push_back(0);

    for (int idx : pinv) {
        seg.add(g[idx], v[idx]);
        pref_res.push_back(seg.query(0, m));
    }

    for (int i = 0; i < N; ++i) {
        long long ans = (pref_res[i + 1] - pref_res[i] + MOD) % MOD;
        cout << ans << (i == N - 1 ? "" : " ");
    }
    cout << "\n";

    return 0;
}""",
        "time_complexity": "O(N \\log N)",
        "space_complexity": "O(N)",
        "samples": get_samples("arc177_d")
    },
    {
        "id": "arc198_d",
        "contest_id": "arc198",
        "title": "D. Tree Palindrome",
        "rating": 2299,
        "domain": "Dynamic Programming (DP)",
        "subtopic": "Dp on Different Structures",
        "topic": "DP on Trees and DAGs",
        "category_file": "categories/dynamic_programming/tree_dp_palindrome_paths_dsu.md",
        "slug": "tree_dp_palindrome_paths_dsu",
        "core_tags": ["DP", "Tree DP", "Palindrome Paths", "DSU", "BFS"],
        "invariant": "A tree path between $u$ and $v$ is a palindrome if and only if $u$ and $v$ have the same character ($find(u) = find(v)$ in DSU) and the subpath between the next step from $u$ towards $v$ and the next step from $v$ towards $u$ is also a palindrome.",
        "editorial_reduction": "1. If $A_{u, v} = 1$, the unique simple path between $u$ and $v$ is forced to be a palindrome.\n2. A path is a palindrome iff $c_u = c_v$ and the inner path between $(nxt(u \\to v), nxt(v \\to u))$ is also a palindrome.\n3. Any constraint $A_{u, v} = 1$ forces:\n   - $c_u = c_v$, uniting $u$ and $v$ in a DSU.\n   - The subpath between $(nu, nv)$ to also be a palindrome, propagating the constraint to the inner pair!\n4. We use BFS to precompute all-pairs shortest distances and next-hop pointers $nxt(u \\to v)$ in $O(N^2)$.\n5. Push all given pairs with $A_{u, v} = 1$ into a queue. While the queue is non-empty, pop $(u, v)$, merge $u$ and $v$ in DSU, and if $dist(u, v) \\ge 2$, push $(nxt(u \\to v), nxt(v \\to u))$ into the queue.\n6. After all forced palindromes and character equivalences are resolved, evaluate which pairs $(u, v)$ in the tree actually form palindromes by DP in increasing order of distance $d = 0, 1, \\dots, N-1$.\n7. Count all pairs $(u, v)$ with $u \\le v$ that are palindromes. Total runtime is $O(N^2)$.",
        "cpp_solution": r"""#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <algorithm>

using namespace std;

static short nxt_node[3005][3005];
static short dist_node[3005][3005];
static bool is_pal[3005][3005];

struct DSU {
    vector<int> parent;
    DSU(int n) {
        parent.resize(n + 1);
        for (int i = 0; i <= n; ++i) parent[i] = i;
    }
    int find(int i) {
        if (parent[i] == i) return i;
        return parent[i] = find(parent[i]);
    }
    void unite(int i, int j) {
        int ri = find(i), rj = find(j);
        if (ri != rj) parent[ri] = rj;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    if (!(cin >> N)) return 0;

    vector<vector<int>> adj(N + 1);
    for (int i = 0; i < N - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    vector<string> A(N + 1);
    for (int i = 1; i <= N; ++i) {
        cin >> A[i];
    }

    // BFS from each root to precompute dist and nxt
    for (int root = 1; root <= N; ++root) {
        for (int i = 1; i <= N; ++i) dist_node[root][i] = -1;
        dist_node[root][root] = 0;
        queue<int> q;
        q.push(root);
        while (!q.empty()) {
            int u = q.front();
            q.pop();
            for (int v : adj[u]) {
                if (dist_node[root][v] == -1) {
                    dist_node[root][v] = dist_node[root][u] + 1;
                    nxt_node[v][root] = u; // step from v towards root
                    q.push(v);
                }
            }
        }
    }

    DSU dsu(N);

    // Queue for forced palindromes
    vector<vector<bool>> in_q(N + 1, vector<bool>(N + 1, false));
    queue<pair<int, int>> q;

    for (int i = 1; i <= N; ++i) {
        for (int j = i + 1; j <= N; ++j) {
            if (A[i][j - 1] == '1') {
                in_q[i][j] = true;
                in_q[j][i] = true;
                q.push({i, j});
            }
        }
    }

    while (!q.empty()) {
        auto p = q.front();
        q.pop();
        int u = p.first;
        int v = p.second;
        dsu.unite(u, v);

        if (dist_node[u][v] >= 2) {
            int nu = nxt_node[u][v];
            int nv = nxt_node[v][u];
            if (!in_q[nu][nv]) {
                in_q[nu][nv] = true;
                in_q[nv][nu] = true;
                q.push({nu, nv});
            }
        }
    }

    // Group pairs by distance
    vector<vector<pair<int, int>>> pairs_by_dist(N);
    for (int i = 1; i <= N; ++i) {
        for (int j = 1; j <= N; ++j) {
            pairs_by_dist[dist_node[i][j]].push_back({i, j});
        }
    }

    long long ans = 0;
    for (int d = 0; d < N; ++d) {
        for (const auto& pr : pairs_by_dist[d]) {
            int u = pr.first;
            int v = pr.second;
            if (d == 0) {
                is_pal[u][v] = true;
            } else if (d == 1) {
                is_pal[u][v] = (dsu.find(u) == dsu.find(v));
            } else {
                int nu = nxt_node[u][v];
                int nv = nxt_node[v][u];
                is_pal[u][v] = (dsu.find(u) == dsu.find(v)) && is_pal[nu][nv];
            }
            if (is_pal[u][v]) ans++;
        }
    }

    cout << ans << "\n";
    return 0;
}""",
        "time_complexity": "O(N^2)",
        "space_complexity": "O(N^2)",
        "samples": get_samples("arc198_d")
    },
    {
        "id": "abc290_f",
        "contest_id": "abc290",
        "title": "F. Maximum Diameter",
        "rating": 2300,
        "domain": "Basics",
        "subtopic": "Basic Counting",
        "topic": "Stars and Bars",
        "category_file": "categories/basics/stars_and_bars_tree_diameter_degree_sequences.md",
        "slug": "stars_and_bars_tree_diameter_degree_sequences",
        "core_tags": ["Basics", "Basic Counting", "Stars and Bars", "Tree Diameter", "Degree Sequences"],
        "invariant": "For any valid tree degree sequence $d_1, \\dots, d_N$ with $\\sum d_i = 2N - 2$ having $k$ leaves ($d_i = 1$), the maximum possible diameter is achieved by arranging all $N - k$ internal vertices in a simple path, giving maximum diameter $N - k + 1$. Summing $(N - k + 1)$ across all valid degree sequences simplifies algebraically to $(N+1) \\binom{2N-3}{N-1} - N \\binom{2N-4}{N-2}$.",
        "editorial_reduction": "1. In any tree on $N$ vertices, the degree sequence satisfies $d_i \\ge 1$ and $\\sum d_i = 2N - 2$.\n2. A vertex $i$ is a leaf iff $d_i = 1$. The remaining $N - k$ vertices are internal vertices ($d_i \\ge 2$).\n3. To maximize the diameter for a given degree sequence, arrange all internal vertices in a line (caterpillar tree). The longest path visits all $N - k$ internal vertices plus two endpoint leaves, giving diameter $(N - k - 1) + 2 = N - k + 1$.\n4. To sum $(N - k + 1)$ over all degree sequences, we count the number of compositions of $\\sum (d_i - 1) = N - 2$ into $N$ non-negative parts:\n   - Total degree sequences: $\\binom{(N - 2) + N - 1}{N - 1} = \\binom{2N - 3}{N - 1}$.\n   - Each leaf corresponds to $d_i - 1 = 0$. By linearity of expectation, the expected number of non-zero entries (internal nodes) corresponds to $(N+1) \\binom{2N-3}{N-1} - N \\binom{2N-4}{N-2}$.\n5. Precompute factorials up to $2 \\times 10^6$ to answer each query in $O(1)$ time.",
        "cpp_solution": r"""#include <iostream>
#include <vector>

using namespace std;

static const int MOD = 998244353;
static const int MAX = 2000005;

long long fact[MAX];
long long inv[MAX];

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
    inv[0] = 1;
    for (int i = 1; i < MAX; ++i) {
        fact[i] = (fact[i - 1] * i) % MOD;
    }
    inv[MAX - 1] = power(fact[MAX - 1], MOD - 2);
    for (int i = MAX - 2; i >= 1; --i) {
        inv[i] = (inv[i + 1] * (i + 1)) % MOD;
    }
}

long long nCr(int n, int r) {
    if (r < 0 || r > n) return 0;
    return fact[n] * inv[r] % MOD * inv[n - r] % MOD;
}

void solve() {
    int N;
    if (!(cin >> N)) return;
    if (N == 2) {
        cout << 1 << "\n";
        return;
    }
    long long term1 = (1LL * (N + 1) * nCr(2 * N - 3, N - 1)) % MOD;
    long long term2 = (1LL * N * nCr(2 * N - 4, N - 2)) % MOD;
    long long ans = (term1 - term2 + MOD) % MOD;
    cout << ans << "\n";
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    precompute();
    int T;
    if (cin >> T) {
        while (T--) solve();
    }
    return 0;
}""",
        "time_complexity": "O(N + T)",
        "space_complexity": "O(N)",
        "samples": get_samples("abc290_f")
    },
    {
        "id": "arc078_c",
        "contest_id": "arc078",
        "title": "E. Awkward Response",
        "rating": 2300,
        "domain": "Miscellaneous",
        "subtopic": "Interactive Problems",
        "topic": "Interactive Problems",
        "category_file": "categories/miscellaneous/interactive_lexicographical_binary_search.md",
        "slug": "interactive_lexicographical_binary_search",
        "core_tags": ["Miscellaneous", "Interactive", "Binary Search", "Lexicographical Order"],
        "invariant": "Querying $n$ returns 'Y' iff ($n \\le N$ and $str(n) \\le str(N)$) or ($n > N$ and $str(n) > str(N)$). Querying $10^9$ uniquely isolates powers of 10. For non-powers of 10, querying $10^k$ reveals the number of digits $L$ of $N$, and querying $mid \\times 10$ ensures $mid \\times 10 > N$, returning 'Y' if and only if $mid \\ge N$.",
        "editorial_reduction": "1. The judge returns 'Y' if both numerical and string order conditions agree, and 'N' otherwise.\n2. Powers of 10 are a special case: $10^9$ returns 'Y' iff $N = 10^k$ for some $k \\in [0, 9]$. If so, test $2, 20, 200, \\dots$ to find the power in $\\le 10$ queries.\n3. If $N$ is not a power of 10, test $10, 100, 1000, \\dots$: the first power $10^k$ that returns 'N' gives the number of digits $L = k$.\n4. Now $N$ is known to have $L$ digits, so $N \\in [10^{L-1}, 10^L - 1]$.\n5. For any candidate $mid \\in [10^{L-1}, 10^L - 1]$, query $x = mid \\times 10$. Because $x$ has $L + 1$ digits, $x > N$ is always true. Thus, the judge returns 'Y' iff $str(x) > str(N)$:\n   - If $mid < N$: $str(mid) < str(N) \\implies$ 'N'.\n   - If $mid = N$: $str(mid \\times 10) = str(N) + '0' > str(N) \\implies$ 'Y'.\n   - If $mid > N$: $str(mid) > str(N) \\implies$ 'Y'.\n6. Hence `ask(mid * 10)` acts as an exact monotonic predicate $mid \\ge N$! Binary search locates $N$ in $\\lceil \\log_2(9 \\times 10^{L-1}) \\rceil \\le 30$ queries, well within the 64 query limit.",
        "cpp_solution": r"""#include <iostream>
#include <string>

using namespace std;

bool ask(long long n) {
    cout << "? " << n << endl;
    char ans;
    cin >> ans;
    return (ans == 'Y');
}

int main() {
    // 1. Check if power of 10
    if (ask(1000000000LL)) {
        for (int k = 0; k < 10; ++k) {
            long long val = 2;
            for (int i = 0; i < k; ++i) val *= 10;
            if (ask(val)) {
                long long ans = 1;
                for (int i = 0; i < k; ++i) ans *= 10;
                cout << "! " << ans << endl;
                return 0;
            }
        }
    } else {
        // Not a power of 10
        // Find length L
        int L = 1;
        long long cur = 10;
        for (int k = 1; k < 10; ++k) {
            if (!ask(cur)) {
                L = k;
                break;
            }
            cur *= 10;
        }

        // Binary search in [10^(L-1), 10^L - 1]
        long long low = 1;
        for (int i = 1; i < L; ++i) low *= 10;
        long long high = low * 10 - 1;
        long long ans = high;

        long long shift = 10;

        while (low <= high) {
            long long mid = low + (high - low) / 2;
            if (ask(mid * shift)) {
                ans = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }

        cout << "! " << ans << endl;
        return 0;
    }
    return 0;
}""",
        "time_complexity": "O(\\log N)",
        "space_complexity": "O(1)",
        "samples": []
    },
    {
        "id": "arc129_d",
        "contest_id": "arc129",
        "title": "D. -1 +2 -1",
        "rating": 2300,
        "domain": "Basics",
        "subtopic": "More Techniques",
        "topic": "Difference Array",
        "category_file": "categories/basics/difference_array_second_differences_circular.md",
        "slug": "difference_array_second_differences_circular",
        "core_tags": ["Basics", "Difference Array", "Second Differences", "Circular Array", "Invariants"],
        "invariant": "Applying the operation $(-1, 2, -1)$ at position $i$ corresponds to $A_{i-1} \\leftarrow A_{i-1} - 1, A_i \\leftarrow A_i + 2, A_{i+1} \\leftarrow A_{i+1} - 1$. In terms of operation counts $x_i$, this gives $A_i = 2x_i - x_{i-1} - x_{i+1} = -(d_{i+1} - d_i)$ where $d_i = x_i - x_{i-1}$. A valid solution exists iff $\\sum A_i = 0$ and the first prefix sum of $A$ sums to $0 \\pmod N$.",
        "editorial_reduction": "1. Let $x_i \\ge 0$ be the number of times operation $i$ is performed. The final state condition is $A_i = -(x_{i+1} - 2x_i + x_{i-1})$ for all $1 \\le i \\le N$ (with indices modulo $N$).\n2. Notice that the sum $\\sum A_i = 0$ must hold since each operation changes the sum by $0$. If $\\sum A_i \\ne 0$, output -1.\n3. Let $d_i = x_i - x_{i-1}$. Then $A_{i-1} = -(d_i - d_{i-1}) = d_{i-1} - d_i \\implies d_i = d_1 + P_{i-1}$ where $P_k = -\\sum_{j=1}^k A_j$.\n4. Because the array is circular, $\\sum_{i=1}^N d_i = \\sum (x_i - x_{i-1}) = 0$. This forces $N d_1 + \\sum_{i=1}^N P_{i-1} = 0$, uniquely determining $d_1 = -(\\sum P_{i-1}) / N$.\n   - If $\\sum P_{i-1}$ is not divisible by $N$, no integer solution exists $\\implies$ output -1.\n5. Once all $d_i$ are fixed, $x_i = x_1 + Q_i$ where $Q_i = \\sum_{j=2}^i d_j$. To minimize $\\sum x_i$ subject to $x_i \\ge 0$ for all $i$, we choose $x_1 = \\max(0, -\\min_i Q_i)$.\n6. Output the total operations $\\sum_{i=1}^N x_i$. Total complexity is $O(N)$.",
        "cpp_solution": r"""#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    if (!(cin >> N)) return 0;

    vector<long long> A(N);
    long long sum_A = 0;
    for (int i = 0; i < N; ++i) {
        cin >> A[i];
        sum_A += A[i];
    }

    if (sum_A != 0) {
        cout << -1 << "\n";
        return 0;
    }

    vector<long long> P(N, 0);
    for (int i = 1; i < N; ++i) {
        P[i] = P[i - 1] + A[i - 1];
    }

    long long sum_P = 0;
    for (int i = 0; i < N; ++i) {
        sum_P += P[i];
    }

    if (sum_P % N != 0) {
        cout << -1 << "\n";
        return 0;
    }

    long long d1 = -(sum_P / N);
    vector<long long> d(N);
    d[0] = d1;
    for (int i = 1; i < N; ++i) {
        d[i] = d1 + P[i];
    }

    vector<long long> Q(N, 0);
    for (int i = 1; i < N; ++i) {
        Q[i] = Q[i - 1] + d[i];
    }

    long long min_Q = 0;
    for (int i = 0; i < N; ++i) {
        min_Q = min(min_Q, Q[i]);
    }

    long long x1 = (min_Q < 0 ? -min_Q : 0);
    long long total_ops = 0;
    for (int i = 0; i < N; ++i) {
        total_ops += (x1 + Q[i]);
    }

    cout << total_ops << "\n";
    return 0;
}""",
        "time_complexity": "O(N)",
        "space_complexity": "O(N)",
        "samples": get_samples("arc129_d")
    }
]

with open('scratch/part5_part2d_meta.json', 'w', encoding='utf-8') as f:
    json.dump(meta, f, indent=2, ensure_ascii=False)

print(f"Successfully generated metadata for {len(meta)} problems!")
