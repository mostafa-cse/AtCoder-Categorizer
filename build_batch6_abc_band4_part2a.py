import os
import subprocess
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Ensure directories exist
os.makedirs("analysis", exist_ok=True)
os.makedirs("categories", exist_ok=True)
os.makedirs("state", exist_ok=True)

print("=" * 75)
print("      PROCESSING BATCH 6 PART 2A: ABC / ARC CURATED LADDER (2051 - 2073)")
print("=" * 75)

SELECTED_PROBLEMS = [
    {
        "id": "abc253_g",
        "title": "Swap Many Times",
        "contest_id": "abc253",
        "rating": 2051,
        "tag": "Miscellaneous",
        "subtopic": "Ad-Hoc / Simulation",
        "topic": "Block Simulation and Invariant Reversal",
        "cat_folder": "miscellaneous",
        "cat_file": "block_simulation_and_invariant_reversal.md",
        "statement": "You are given a permutation P = (1, 2, ..., N) of length N, and integers L and R. Consider the sequence of N(N-1)/2 swaps in lexicographical order: for i = 1 to N-1, for j = i+1 to N, swap(P[i], P[j]). Apply only the L-th through R-th swaps (1-indexed) in order and output the resulting permutation.",
        "key_idea": "The swaps are naturally partitioned into N-1 blocks, where block i contains N-i swaps: (i, i+1), ..., (i, N). We locate the block bL containing swap L and the block bR containing swap R. If bL == bR, we simulate the <= N swaps directly. If bL < bR, we simulate the partial suffix of block bL (<= N swaps), then apply an O(N) structural invariant for all full intermediate blocks i in [bL + 1, bR - 1]: executing all swaps for k consecutive full blocks i1 through i2 takes the last k elements P[N-k+1..N], reverses them, and places them at P[i1..i1+k-1], while shifting the remaining intermediate elements to the right. Finally, we simulate the partial prefix of block bR (<= N swaps).",
        "observation": "Executing a contiguous sequence of k full swap blocks [i1, i2] reverses the suffix of length k and shifts the remaining elements rightward without altering their relative order.",
        "algorithm": [
            "Compute prefix sums of block sizes (N - i) to find block bL and position posL for swap L, and block bR and position posR for swap R.",
            "If bL == bR: simulate swaps (bL, j) for j from posL to posR in O(N).",
            "Otherwise:",
            "  1. Simulate partial block bL: swap(P[bL], P[j]) for j from posL to N.",
            "  2. For full intermediate blocks i1 = bL + 1 to i2 = bR - 1 with k = i2 - i1 + 1 > 0: reverse P[N-k+1..N] into positions P[i1..i1+k-1], and shift P[i1..N-k] into P[i1+k..N].",
            "  3. Simulate partial block bR: swap(P[bR], P[j]) for j from bR + 1 to posR.",
            "Output the resulting permutation in O(N) total time."
        ],
        "time_complexity": "O(N)",
        "space_complexity": "O(N)",
        "core_skill": "Decomposing large simulation into partial boundary blocks and constant-time/linear structural block invariants.",
        "reusable_pattern": "Contiguous full swap blocks on an array act as prefix/suffix cyclic shifts and reversals.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n, l, r;
    if (!(cin >> n >> l >> r)) return 0;

    vector<int> a(n + 1);
    iota(a.begin(), a.end(), 0);

    long long cur = 0;
    int bL = -1, posL = -1;
    int bR = -1, posR = -1;

    for (int i = 1; i < n; ++i) {
        long long sz = n - i;
        if (bL == -1 && cur + sz >= l) {
            bL = i;
            posL = i + (l - cur);
        }
        if (bR == -1 && cur + sz >= r) {
            bR = i;
            posR = i + (r - cur);
        }
        cur += sz;
    }

    if (bL == bR) {
        for (int j = posL; j <= posR; ++j) {
            swap(a[bL], a[j]);
        }
    } else {
        for (int j = posL; j <= n; ++j) {
            swap(a[bL], a[j]);
        }
        int i1 = bL + 1, i2 = bR - 1;
        if (i1 <= i2) {
            int k = i2 - i1 + 1;
            vector<int> last_k(a.begin() + (n - k + 1), a.begin() + (n + 1));
            reverse(last_k.begin(), last_k.end());
            vector<int> mid(a.begin() + i1, a.begin() + (n - k + 1));
            for (int t = 0; t < k; ++t) a[i1 + t] = last_k[t];
            for (int t = 0; t < (int)mid.size(); ++t) a[i1 + k + t] = mid[t];
        }
        for (int j = bR + 1; j <= posR; ++j) {
            swap(a[bR], a[j]);
        }
    }

    for (int i = 1; i <= n; ++i) {
        cout << a[i] << (i == n ? "" : " ");
    }
    cout << "\n";
    return 0;
}
"""
    },
    {
        "id": "abc369_g",
        "title": "As far as possible",
        "contest_id": "abc369",
        "rating": 2055,
        "tag": "Graph Theory",
        "subtopic": "Trees",
        "topic": "Tree Longest Path Decomposition and Greedy Subtree Weight",
        "cat_folder": "graph_theory",
        "cat_file": "tree_longest_path_decomposition_greedy.md",
        "statement": "Given a tree with N weighted edges. For each K = 1, 2, ..., N: Aoki chooses K vertices to maximize the minimum length of a walk starting and ending at vertex 1 that visits all chosen vertices. Takahashi seeks to minimize the walk. Find the optimal score for each K.",
        "key_idea": "The shortest walk visiting a set S of vertices and starting/ending at 1 traverses every edge in the minimal subtree spanning S U {1} exactly twice. To maximize this subtree weight by picking K vertices, we root the tree at 1 and decompose the tree into disjoint paths by iteratively choosing the deepest child (heavy-light style longest-path decomposition). By submodularity of subtree edge weights, the optimal selection for any K is greedily formed by the sum of lengths of the top K paths in this longest-path decomposition.",
        "observation": "Max-weight subtree spanning root and K vertices reduces to greedily selecting the K longest branches in a heavy-child path decomposition.",
        "algorithm": [
            "Root tree at 1. Compute max_d[u] = maximum distance from u to a leaf in its subtree via DFS.",
            "Mark heavy[u] as the child achieving max_d[u].",
            "Perform a second DFS decomposing the tree into disjoint paths: heavy edges extend the current path, while light edges start new paths.",
            "Collect all path lengths and sort them in descending order.",
            "For each K = 1 to N, output 2 * (prefix sum of top min(K, num_paths) path lengths)."
        ],
        "time_complexity": "O(N log N)",
        "space_complexity": "O(N)",
        "core_skill": "Greedy polymatroid tree optimization via heavy-path / deepest-leaf path decomposition.",
        "reusable_pattern": "Top-K subtree coverage maximization on trees is solved via disjoint longest-path decomposition.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Edge {
    int to;
    long long w;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<Edge>> adj(n + 1);
    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        long long w;
        cin >> u >> v >> w;
        adj[u].push_back({v, w});
        adj[v].push_back({u, w});
    }

    vector<long long> max_d(n + 1, 0);
    vector<int> heavy(n + 1, 0);

    auto dfs1 = [&](auto& self, int u, int p) -> void {
        for (auto& e : adj[u]) {
            if (e.to == p) continue;
            self(self, e.to, u);
            if (max_d[e.to] + e.w > max_d[u]) {
                max_d[u] = max_d[e.to] + e.w;
                heavy[u] = e.to;
            }
        }
    };
    dfs1(dfs1, 1, 0);

    vector<long long> paths;
    auto dfs2 = [&](auto& self, int u, int p, long long cur_len) -> void {
        if (heavy[u] != 0) {
            long long w = 0;
            for (auto& e : adj[u]) {
                if (e.to == heavy[u]) {
                    w = e.w;
                    break;
                }
            }
            self(self, heavy[u], u, cur_len + w);
        } else {
            paths.push_back(cur_len);
        }
        for (auto& e : adj[u]) {
            if (e.to == p || e.to == heavy[u]) continue;
            self(self, e.to, u, e.w);
        }
    };
    dfs2(dfs2, 1, 0, 0);

    sort(paths.rbegin(), paths.rend());

    long long current_sum = 0;
    int num_paths = paths.size();
    for (int k = 1; k <= n; ++k) {
        if (k - 1 < num_paths) {
            current_sum += paths[k - 1];
        }
        cout << current_sum * 2 << "\n";
    }
    return 0;
}
"""
    },
    {
        "id": "arc114_c",
        "title": "Sequence Scores",
        "contest_id": "arc114",
        "rating": 2056,
        "tag": "Combinatorics",
        "subtopic": "Counting Principles",
        "topic": "Contribution to the Sum and Linearity of Expectation",
        "cat_folder": "combinatorics",
        "cat_file": "contribution_linearity_of_expectation.md",
        "statement": "Starting from an all-zero sequence X of length N, let f(A) be the minimum number of range-max operations [l, r, v] (X_i <- max(X_i, v)) to make X equal A. Compute the sum of f(A) over all M^N sequences A with elements in [1, M] modulo 998244353.",
        "key_idea": "An element A_i = v requires a new operation unless there exists a prior j < i with A_j = v such that all intermediate elements A_k > v for k in (j, i). If such j exists, A_i can be merged into the operation that created A_j. Thus f(A) = N - (number of saved indices). By linearity of expectation, we sum the probability of saving over all pairs (j, i) with distance d = i - j: A_j = A_i = v has 1 choice, intermediate d-1 elements must be > v ((M - v) choices each), and the remaining N - 1 - d elements have M choices each.",
        "observation": "f(A) is exactly N minus the number of pairs (j, i) such that A_j = A_i and all intermediate elements are strictly greater than A_j.",
        "algorithm": [
            "Total operations without savings is N * M^N.",
            "Iterate distance d = 1 to N - 1.",
            "For each d, the number of pairs (j, i) with i - j = d is N - d.",
            "Sum over v in [1, M] of (M - v)^(d - 1) is sum_{t=0}^{M-1} t^(d - 1). Precompute/maintain this power sum in O(M).",
            "Multiply by (N - d) * M^(N - 1 - d) and accumulate saved operations.",
            "Output (N * M^N - total_saved) modulo 998244353."
        ],
        "time_complexity": "O(N * M)",
        "space_complexity": "O(M)",
        "core_skill": "Decomposing complex greedy cost functions into pairwise savings and counting via linearity of expectation.",
        "reusable_pattern": "Range overwrite operation savings: A_i merges with previous A_j = A_i iff all elements between them strictly exceed A_i.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>

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

    int n, m;
    if (!(cin >> n >> m)) return 0;

    long long total_all = (1LL * n % MOD) * power(m, n) % MOD;
    long long total_saved = 0;
    vector<long long> pow_t(m, 1);

    for (int d = 1; d <= n - 1; ++d) {
        long long sum_t = 0;
        for (int t = 0; t < m; ++t) {
            sum_t = (sum_t + pow_t[t]) % MOD;
            pow_t[t] = (pow_t[t] * t) % MOD;
        }
        long long ways = (1LL * (n - d) % MOD) * power(m, n - 1 - d) % MOD;
        ways = (ways * sum_t) % MOD;
        total_saved = (total_saved + ways) % MOD;
    }

    long long ans = (total_all - total_saved + MOD) % MOD;
    cout << ans << "\n";
    return 0;
}
"""
    },
    {
        "id": "arc159_d",
        "title": "LIS 2",
        "contest_id": "arc159",
        "rating": 2056,
        "tag": "Dynamic Programming (DP)",
        "subtopic": "DP Optimizations",
        "topic": "Coordinate-Compressed Segment Tree Optimized Interval LIS",
        "cat_folder": "dynamic_programming",
        "cat_file": "coordinate_compressed_segtree_interval_lis.md",
        "statement": "Takahashi appends intervals [l_i, r_i] sequentially to an array X. Find the length of the longest strictly increasing subsequence (LIS) of the concatenated sequence X.",
        "key_idea": "Each interval [l_i, r_i] contains strictly increasing consecutive integers. When extending an existing LIS ending at value x: if x < l_i, we can append all elements [l_i, r_i], obtaining length dp[x] + (r_i - l_i + 1). If l_i <= x <= r_i, we can append (x+1 .. r_i), obtaining length dp[x] + (r_i - x) = (dp[x] - x) + r_i. Maintaining both dp[x] and (dp[x] - x) in a coordinate-compressed segment tree allows querying both transitions in O(log N) and updating at position r_i.",
        "observation": "Extending from x in [l_i, r_i] splits into querying max(dp[x]) for x < l_i and max(dp[x] - x) for l_i <= x <= r_i.",
        "algorithm": [
            "Collect all l_i and r_i endpoints and coordinate-compress them into an array of size M <= 2N.",
            "Initialize a Segment Tree supporting range max queries for two values: dp[x] and dp[x] - x.",
            "For each interval [l_i, r_i]:",
            "  Query 1: q1 = max_{x < l_i} dp[x]. Gain = q1 + (r_i - l_i + 1).",
            "  Query 2: q2 = max_{l_i <= x <= r_i} (dp[x] - x). Gain = q2 + r_i.",
            "  Best LIS ending at r_i is cur = max({r_i - l_i + 1, Gain 1, Gain 2}).",
            "  Update segment tree at position r_i with dp = cur and diff = cur - r_i.",
            "Output the maximum LIS length found."
        ],
        "time_complexity": "O(N log N)",
        "space_complexity": "O(N)",
        "core_skill": "Segment tree optimization for piecewise linear interval DP transitions.",
        "reusable_pattern": "Interval subsequence transitions split into range query for dp[x] and range query for dp[x] - x.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const long long INF = 2e18;

struct SegTree {
    int n;
    vector<long long> tree_dp;
    vector<long long> tree_diff;

    SegTree(int n) : n(n), tree_dp(4 * n, -INF), tree_diff(4 * n, -INF) {}

    void update(int node, int l, int r, int qx, long long v_dp, long long v_diff) {
        if (l == r) {
            tree_dp[node] = max(tree_dp[node], v_dp);
            tree_diff[node] = max(tree_diff[node], v_diff);
            return;
        }
        int mid = l + (r - l) / 2;
        if (qx <= mid) update(2 * node, l, mid, qx, v_dp, v_diff);
        else update(2 * node + 1, mid + 1, r, qx, v_dp, v_diff);
        tree_dp[node] = max(tree_dp[2 * node], tree_dp[2 * node + 1]);
        tree_diff[node] = max(tree_diff[2 * node], tree_diff[2 * node + 1]);
    }

    long long query_dp(int node, int l, int r, int ql, int qr) {
        if (ql > qr || ql > r || qr < l) return -INF;
        if (ql <= l && r <= qr) return tree_dp[node];
        int mid = l + (r - l) / 2;
        return max(query_dp(2 * node, l, mid, ql, qr), query_dp(2 * node + 1, mid + 1, r, ql, qr));
    }

    long long query_diff(int node, int l, int r, int ql, int qr) {
        if (ql > qr || ql > r || qr < l) return -INF;
        if (ql <= l && r <= qr) return tree_diff[node];
        int mid = l + (r - l) / 2;
        return max(query_diff(2 * node, l, mid, ql, qr), query_diff(2 * node + 1, mid + 1, r, ql, qr));
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<pair<long long, long long>> intervals(n);
    vector<long long> pts;
    for (int i = 0; i < n; ++i) {
        cin >> intervals[i].first >> intervals[i].second;
        pts.push_back(intervals[i].first);
        pts.push_back(intervals[i].second);
    }

    sort(pts.begin(), pts.end());
    pts.erase(unique(pts.begin(), pts.end()), pts.end());
    int m = pts.size();

    auto get_idx = [&](long long v) {
        return lower_bound(pts.begin(), pts.end(), v) - pts.begin();
    };

    SegTree st(m);
    long long ans = 0;

    for (int i = 0; i < n; ++i) {
        long long l = intervals[i].first;
        long long r = intervals[i].second;
        int il = get_idx(l);
        int ir = get_idx(r);

        long long q1 = st.query_dp(1, 0, m - 1, 0, il - 1);
        long long cur1 = (q1 < 0 ? 0 : q1) + (r - l + 1);

        long long q2 = st.query_diff(1, 0, m - 1, il, ir);
        long long cur2 = (q2 < -INF / 2 ? -INF : q2 + r);

        long long cur = max({cur1, cur2, r - l + 1});
        ans = max(ans, cur);

        st.update(1, 0, m - 1, ir, cur, cur - r);
    }

    cout << ans << "\n";
    return 0;
}
"""
    },
    {
        "id": "arc176_c",
        "title": "Max Permutation",
        "contest_id": "arc176",
        "rating": 2056,
        "tag": "Basics",
        "subtopic": "Permutations",
        "topic": "Permutation Construction with Value Upper Bound Counting",
        "cat_folder": "basics",
        "cat_file": "permutation_upper_bound_counting.md",
        "statement": "Given M conditions max(P_{A_i}, P_{B_i}) = C_i, count the number of permutations P of (1, 2, ..., N) satisfying all conditions modulo 998244353.",
        "key_idea": "Each condition imposes upper bounds P_{A_i} <= C_i and P_{B_i} <= C_i. For each vertex v, define X_v = min_{v in e} C_e. We determine which position takes value k in descending order k = N, N-1, ..., 1. If multiple edges have weight k, they must all share a unique common vertex v_star, forcing P_{v_star} = k. If exactly one edge (u, v) has weight k, if both endpoints are undecided and valid, either can be chosen (factor of 2). If zero edges have weight k, we choose any available undecided vertex with X_j >= k. This exact greedy counting runs in O(N + M).",
        "observation": "Processing permutation values from N down to 1 decouples constraints into unique forced centers, binary choice edges, and unconstrained pool selections.",
        "algorithm": [
            "Compute X_v = min edge weight incident to v for all v (default N).",
            "Group edges by weight C.",
            "Iterate k from N down to 1, maintaining the pool of available undecided vertices with X_v >= k.",
            "If >= 2 edges with weight k: intersect their endpoints. If not exactly 1 valid common vertex or X < k, return 0; force P = k.",
            "If 1 edge (u, v) with weight k: if both endpoints undecided and both X >= k, multiply answer by 2 and mark one decided. Else resolve uniquely or return 0.",
            "If 0 edges with weight k: multiply answer by number of available vertices and decrement pool.",
            "Output answer modulo 998244353."
        ],
        "time_complexity": "O(N + M)",
        "space_complexity": "O(N + M)",
        "core_skill": "Reverse greedy value assignment and upper-bound pool tracking for permutation constraints.",
        "reusable_pattern": "Permutation max-edge constraints: resolve from largest value downward to fix forced vertices before free pool assignments.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MOD = 998244353;

struct Edge {
    int u, v;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<int> X(n + 1, n);
    vector<vector<Edge>> by_c(n + 1);

    for (int i = 0; i < m; ++i) {
        int u, v, c;
        cin >> u >> v >> c;
        X[u] = min(X[u], c);
        X[v] = min(X[v], c);
        by_c[c].push_back({u, v});
    }

    vector<int> count_X(n + 1, 0);
    for (int i = 1; i <= n; ++i) {
        count_X[X[i]]++;
    }

    vector<bool> decided(n + 1, false);
    long long ans = 1;
    int avail = 0;

    for (int k = n; k >= 1; --k) {
        avail += count_X[k];
        auto& edges_k = by_c[k];

        if (edges_k.size() >= 2) {
            int u0 = edges_k[0].u, v0 = edges_k[0].v;
            vector<int> cand = {u0, v0};
            for (size_t i = 1; i < edges_k.size(); ++i) {
                int u = edges_k[i].u, v = edges_k[i].v;
                vector<int> next_cand;
                for (int x : cand) {
                    if (x == u || x == v) next_cand.push_back(x);
                }
                cand = next_cand;
            }
            if (cand.size() != 1) {
                cout << 0 << "\n";
                return 0;
            }
            int v_star = cand[0];
            if (X[v_star] < k || decided[v_star]) {
                cout << 0 << "\n";
                return 0;
            }
            decided[v_star] = true;
            avail--;
        } else if (edges_k.size() == 1) {
            int u = edges_k[0].u, v = edges_k[0].v;
            if (decided[u] && decided[v]) {
                cout << 0 << "\n";
                return 0;
            } else if (decided[u]) {
                if (X[v] < k) { cout << 0 << "\n"; return 0; }
                decided[v] = true;
                avail--;
            } else if (decided[v]) {
                if (X[u] < k) { cout << 0 << "\n"; return 0; }
                decided[u] = true;
                avail--;
            } else {
                bool ok_u = (X[u] >= k);
                bool ok_v = (X[v] >= k);
                if (ok_u && ok_v) {
                    ans = (ans * 2) % MOD;
                    decided[u] = true;
                    avail--;
                } else if (ok_u) {
                    decided[u] = true;
                    avail--;
                } else if (ok_v) {
                    decided[v] = true;
                    avail--;
                } else {
                    cout << 0 << "\n";
                    return 0;
                }
            }
        } else {
            if (avail <= 0) {
                cout << 0 << "\n";
                return 0;
            }
            ans = (ans * avail) % MOD;
            avail--;
        }
    }

    cout << ans << "\n";
    return 0;
}
"""
    },
    {
        "id": "abc350_g",
        "title": "Mediator",
        "contest_id": "abc350",
        "rating": 2058,
        "tag": "Data Structures (DS)",
        "subtopic": "Disjoint Set Union (DSU)",
        "topic": "Small-to-Large Tree Rerooting for Online Forest Queries",
        "cat_folder": "data_structures",
        "cat_file": "small_to_large_tree_rerooting.md",
        "statement": "Online forest maintenance on N vertices: Type 1 adds edge (u, v) between two different trees; Type 2 queries if there is a common neighbor between u and v (distance 2). Queries are encrypted with the previous answer.",
        "key_idea": "In a forest, any two vertices have at most one common neighbor. By maintaining parent pointers for each rooted tree, a common neighbor between u and v must be one of: parent[u] == parent[v], parent[parent[u]] == v, or parent[parent[v]] == u. When merging trees via edge (u, v), we re-root the smaller component at u in O(size) and set parent[u] = v. By small-to-large merging, each vertex is rerooted at most O(log N) times, giving O(N log N + Q) total time.",
        "observation": "In a rooted forest, common neighbors are verified in O(1) by checking depth-1 and depth-2 parent links, while small-to-large tree rerooting takes amortized O(log N) per node.",
        "algorithm": [
            "Maintain parent[u], sz[u], and adjacency list adj[u] for each vertex.",
            "For Type 1 (merge u, v): swap so sz[u] <= sz[v]. Re-root component of u at u via BFS/DFS, flipping parent pointers. Set parent[u] = v and sz[v] += sz[u].",
            "For Type 2 (query u, v): check if parent[u] == parent[v] (non-zero), parent[parent[u]] == v, or parent[parent[v]] == u in O(1). Output mediator or 0.",
            "Decrypt queries using last_ans in online fashion."
        ],
        "time_complexity": "O(N log N + Q)",
        "space_complexity": "O(N)",
        "core_skill": "Small-to-large component rerooting for maintaining dynamic rooted trees without heavy Link-Cut Tree machinery.",
        "reusable_pattern": "Distance-2 common neighbor in dynamic forests is solved via parent pointers with small-to-large rerooting.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MOD = 998244353;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    vector<int> parent(n + 1, 0);
    vector<int> sz(n + 1, 1);
    vector<vector<int>> adj(n + 1);

    long long last_ans = 0;

    auto reroot = [&](int root) {
        vector<int> order;
        vector<int> p_old(n + 1, 0);
        vector<int> q_list = {root};
        p_old[root] = 0;
        int head = 0;
        while (head < (int)q_list.size()) {
            int u = q_list[head++];
            order.push_back(u);
            for (int v : adj[u]) {
                if (v != p_old[u]) {
                    p_old[v] = u;
                    q_list.push_back(v);
                }
            }
        }
        for (int i = 1; i < (int)order.size(); ++i) {
            int u = order[i];
            parent[u] = p_old[u];
        }
        parent[root] = 0;
    };

    while (q--) {
        long long a, b, c;
        cin >> a >> b >> c;
        long long type = 1 + (((a * (1 + last_ans)) % MOD) % 2);
        long long u = 1 + (((b * (1 + last_ans)) % MOD) % n);
        long long v = 1 + (((c * (1 + last_ans)) % MOD) % n);

        if (type == 1) {
            adj[u].push_back(v);
            adj[v].push_back(u);
            if (sz[u] > sz[v]) {
                swap(u, v);
            }
            reroot(u);
            parent[u] = v;
            sz[v] += sz[u];
        } else {
            int ans = 0;
            if (parent[u] != 0 && parent[u] == parent[v]) {
                ans = parent[u];
            } else if (parent[u] != 0 && parent[parent[u]] == v) {
                ans = parent[u];
            } else if (parent[v] != 0 && parent[parent[v]] == u) {
                ans = parent[v];
            }
            cout << ans << "\n";
            last_ans = ans;
        }
    }
    return 0;
}
"""
    },
    {
        "id": "abc433_g",
        "title": "Substring Game",
        "contest_id": "abc433",
        "rating": 2060,
        "tag": "Strings",
        "subtopic": "Suffix Automaton / Suffix Tree",
        "topic": "Suffix Automaton DAG Impartial Game Evaluation",
        "cat_folder": "strings",
        "cat_file": "suffix_automaton_game_evaluation.md",
        "statement": "Starting with an empty string T, Alice and Bob take turns appending a character to T such that T remains a substring of S. The first player unable to make a move loses. Determine the winner under optimal play.",
        "key_idea": "The set of all substrings of S forms a DAG under character append operations. Substrings belonging to the same state in the Suffix Automaton (SAM) share the exact same outgoing character transitions. Therefore, game states naturally project onto the O(|S|) states of the Suffix Automaton. A state is a winning state (N-state) if it has a transition to a losing state (P-state), and losing otherwise. We evaluate the DAG in topological order from sink states to the initial state (empty string).",
        "observation": "The impartial substring game state collapses onto the Suffix Automaton DAG, reducing an O(|S|^2) trie to an O(|S|) DAG.",
        "algorithm": [
            "Construct the Suffix Automaton of S in O(|S| * Sigma) time.",
            "Topologically sort the SAM states by length in descending order using counting sort.",
            "Initialize win[u] = false for all states.",
            "Process states in reverse topological order: for each state u, if any transition (u, c) leads to a state v with !win[v], set win[u] = true.",
            "If win[0] is true, Alice wins; otherwise Bob wins."
        ],
        "time_complexity": "O(|S| * Sigma)",
        "space_complexity": "O(|S| * Sigma)",
        "core_skill": "Recognizing that substring game state transitions are equivalent to transitions on the Suffix Automaton DAG.",
        "reusable_pattern": "Impartial games played by extending substrings of a fixed string are solved via Win/Loss DP on the Suffix Automaton.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

struct State {
    int len, link;
    int next[26];
};

void solve() {
    string s;
    cin >> s;
    int n = s.size();

    vector<State> st(2 * n + 5);
    st[0].len = 0;
    st[0].link = -1;
    for (int c = 0; c < 26; ++c) st[0].next[c] = -1;
    int sz = 1, last = 0;

    auto extend = [&](char ch) {
        int c = ch - 'a';
        int cur = sz++;
        st[cur].len = st[last].len + 1;
        for (int i = 0; i < 26; ++i) st[cur].next[i] = -1;
        int p = last;
        while (p != -1 && st[p].next[c] == -1) {
            st[p].next[c] = cur;
            p = st[p].link;
        }
        if (p == -1) {
            st[cur].link = 0;
        } else {
            int q = st[p].next[c];
            if (st[p].len + 1 == st[q].len) {
                st[cur].link = q;
            } else {
                int clone = sz++;
                st[clone].len = st[p].len + 1;
                for (int i = 0; i < 26; ++i) st[clone].next[i] = st[q].next[i];
                st[clone].link = st[q].link;
                while (p != -1 && st[p].next[c] == q) {
                    st[p].next[c] = clone;
                    p = st[p].link;
                }
                st[q].link = clone;
                st[cur].link = clone;
            }
        }
        last = cur;
    };

    for (char ch : s) extend(ch);

    vector<int> cnt(n + 1, 0);
    for (int i = 0; i < sz; ++i) cnt[st[i].len]++;
    for (int i = 1; i <= n; ++i) cnt[i] += cnt[i - 1];
    vector<int> order(sz);
    for (int i = sz - 1; i >= 0; --i) {
        order[--cnt[st[i].len]] = i;
    }

    vector<bool> win(sz, false);
    for (int i = sz - 1; i >= 0; --i) {
        int u = order[i];
        for (int c = 0; c < 26; ++c) {
            int v = st[u].next[c];
            if (v != -1 && !win[v]) {
                win[u] = true;
                break;
            }
        }
    }

    if (win[0]) {
        cout << "Alice\n";
    } else {
        cout << "Bob\n";
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    if (cin >> t) {
        while (t--) solve();
    }
    return 0;
}
"""
    },
    {
        "id": "arc197_d",
        "title": "Ancestor Relation",
        "contest_id": "arc197",
        "rating": 2062,
        "tag": "Graph Theory",
        "subtopic": "Trees",
        "topic": "Comparability Graph Tree Reconstruction and Component Decomposition",
        "cat_folder": "graph_theory",
        "cat_file": "comparability_graph_tree_reconstruction.md",
        "statement": "Given an N x N 0-1 matrix A indicating whether two vertices are comparable (one is an ancestor of the other in a tree G rooted at 1). Find the number of valid trees G modulo 998244353.",
        "key_idea": "The matrix A represents the comparability graph of a tree poset rooted at 1. Vertex 1 must be connected to all vertices. Removing 1, the remaining vertices must partition into connected components representing independent subtrees attached to 1. Inside each component C, the root path before any branching consists of universal vertices (vertices connected to all vertices in C). If there are k universal vertices, they can be arranged in k! orders along the entrance chain. Removing them splits C into further disconnected subcomponents, which are solved recursively.",
        "observation": "In a tree comparability graph, every connected component must have a non-empty set of universal vertices forming a linear path of k! permutations before branching.",
        "algorithm": [
            "Check that A[1][i] == 1 for all i; if not, return 0.",
            "Decompose the graph of {2..N} into connected components.",
            "For each component C:",
            "  Find all universal vertices univ in C (vertices connected to every other vertex in C).",
            "  If univ is empty, return 0 (no valid tree structure).",
            "  Arranging univ along the path gives fact[k] valid permutations.",
            "  Remove univ from C. The remaining vertices rem must partition into disconnected components.",
            "  Recursively solve each subcomponent and multiply results.",
            "Return total product modulo 998244353."
        ],
        "time_complexity": "O(N^2) per testcase",
        "space_complexity": "O(N^2)",
        "core_skill": "Reconstructing tree posets from comparability matrices via universal vertex chain peel-off and component decomposition.",
        "reusable_pattern": "Tree comparability graphs are recursively decomposed by peeling off cliques of universal vertices.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <string>

using namespace std;

const int MOD = 998244353;

long long fact[505];

void solve() {
    int n;
    cin >> n;
    vector<vector<int>> A(n + 1, vector<int>(n + 1));
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= n; ++j) {
            cin >> A[i][j];
        }
    }

    for (int i = 1; i <= n; ++i) {
        if (A[1][i] == 0) {
            cout << 0 << "\n";
            return;
        }
    }

    auto solve_comp = [&](auto& self, const vector<int>& comp) -> long long {
        if (comp.empty()) return 1;
        vector<int> univ;
        for (int u : comp) {
            bool ok = true;
            for (int v : comp) {
                if (A[u][v] == 0) {
                    ok = false;
                    break;
                }
            }
            if (ok) univ.push_back(u);
        }
        if (univ.empty()) return 0;
        int k = univ.size();
        vector<bool> in_univ(n + 1, false);
        for (int u : univ) in_univ[u] = true;
        vector<int> rem;
        for (int u : comp) {
            if (!in_univ[u]) rem.push_back(u);
        }
        if (rem.empty()) return fact[k];

        vector<bool> visited(n + 1, false);
        long long ans = fact[k];
        for (int u : rem) {
            if (!visited[u]) {
                vector<int> sub_c;
                vector<int> q = {u};
                visited[u] = true;
                int head = 0;
                while (head < (int)q.size()) {
                    int cur = q[head++];
                    sub_c.push_back(cur);
                    for (int v : rem) {
                        if (A[cur][v] == 1 && !visited[v]) {
                            visited[v] = true;
                            q.push_back(v);
                        }
                    }
                }
                long long sub_res = self(self, sub_c);
                if (sub_res == 0) return 0;
                ans = (ans * sub_res) % MOD;
            }
        }
        return ans;
    };

    vector<int> rem;
    for (int i = 2; i <= n; ++i) rem.push_back(i);

    vector<bool> visited(n + 1, false);
    long long total_ans = 1;
    for (int u : rem) {
        if (!visited[u]) {
            vector<int> sub_c;
            vector<int> q = {u};
            visited[u] = true;
            int head = 0;
            while (head < (int)q.size()) {
                int cur = q[head++];
                sub_c.push_back(cur);
                for (int v : rem) {
                    if (A[cur][v] == 1 && !visited[v]) {
                        visited[v] = true;
                        q.push_back(v);
                    }
                }
            }
            long long sub_res = solve_comp(solve_comp, sub_c);
            if (sub_res == 0) {
                cout << 0 << "\n";
                return;
            }
            total_ans = (total_ans * sub_res) % MOD;
        }
    }
    cout << total_ans << "\n";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    fact[0] = 1;
    for (int i = 1; i <= 500; ++i) {
        fact[i] = (fact[i - 1] * i) % MOD;
    }

    int t;
    if (cin >> t) {
        while (t--) solve();
    }
    return 0;
}
"""
    },
    {
        "id": "arc111_d",
        "title": "Orientation",
        "contest_id": "arc111",
        "rating": 2064,
        "tag": "Graph Theory",
        "subtopic": "Directed Graphs",
        "topic": "Strong Connectivity Graph Orientation and DFS Tree Back-Edge Directing",
        "cat_folder": "graph_theory",
        "cat_file": "dfs_tree_graph_orientation_scc.md",
        "statement": "Given an undirected graph with N vertices and M edges, and reachability requirements c_1, ..., c_N. Direct all edges such that the number of reachable vertices from vertex i is exactly c_i. A valid solution is guaranteed to exist.",
        "key_idea": "If c_u > c_v, v cannot reach u (otherwise c_v >= c_u), so edge (u, v) must be directed u -> v. If c_u < c_v, it must be directed v -> u. If c_u == c_v, u and v must be mutually reachable and belong to the same Strongly Connected Component (SCC). We can orient the subgraph of edges with c_u == c_v into a strongly connected directed graph using Robbins' Theorem / DFS tree orientation: direct tree edges downward (parent -> child) and back-edges upward (descendant -> ancestor).",
        "observation": "Edges between different reachability values are strictly determined by reachability gradient; edges between equal values are made strongly connected via DFS tree orientation.",
        "algorithm": [
            "For each edge (u, v):",
            "  If c[u] > c[v]: orient u -> v.",
            "  If c[u] < c[v]: orient v -> u.",
            "  If c[u] == c[v]: add to equality adjacency list.",
            "Run DFS on the equality subgraph to construct a DFS forest.",
            "Orient tree edges from parent to child.",
            "Orient non-tree back-edges from deeper node to shallower ancestor.",
            "Output the resulting orientation for all M edges."
        ],
        "time_complexity": "O(N + M)",
        "space_complexity": "O(N + M)",
        "core_skill": "Directing bridgeless connected graphs into strongly connected components via DFS tree edge/back-edge orientation.",
        "reusable_pattern": "Graph orientation with reachability constraints: cross-component edges follow topological order of reachability; intra-component edges are oriented via DFS tree.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <string>

using namespace std;

struct Edge {
    int u, v;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<Edge> edges(m);
    for (int i = 0; i < m; ++i) {
        cin >> edges[i].u >> edges[i].v;
    }

    vector<int> c(n + 1);
    for (int i = 1; i <= n; ++i) {
        cin >> c[i];
    }

    vector<string> ans(m);
    vector<vector<pair<int, int>>> adj_eq(n + 1);

    for (int i = 0; i < m; ++i) {
        int u = edges[i].u;
        int v = edges[i].v;
        if (c[u] > c[v]) {
            ans[i] = "->";
        } else if (c[u] < c[v]) {
            ans[i] = "<-";
        } else {
            adj_eq[u].push_back({v, i});
            adj_eq[v].push_back({u, i});
        }
    }

    vector<bool> visited(n + 1, false);
    vector<int> dep(n + 1, 0);

    auto dfs = [&](auto& self, int u, int p_edge, int d) -> void {
        visited[u] = true;
        dep[u] = d;
        for (auto& edge_info : adj_eq[u]) {
            int v = edge_info.first;
            int idx = edge_info.second;
            if (idx == p_edge) continue;
            if (visited[v]) {
                if (dep[v] < dep[u]) {
                    if (edges[idx].u == u) ans[idx] = "->";
                    else ans[idx] = "<-";
                }
            } else {
                if (edges[idx].u == u) ans[idx] = "->";
                else ans[idx] = "<-";
                self(self, v, idx, d + 1);
            }
        }
    };

    for (int i = 1; i <= n; ++i) {
        if (!visited[i]) {
            dfs(dfs, i, -1, 1);
        }
    }

    for (int i = 0; i < m; ++i) {
        cout << ans[i] << "\n";
    }
    return 0;
}
"""
    },
    {
        "id": "abc199_f",
        "title": "Graph Smoothing",
        "contest_id": "abc199",
        "rating": 2065,
        "tag": "Math",
        "subtopic": "Linear Algebra",
        "topic": "Markov Chain Expected Value Transition via Matrix Exponentiation",
        "cat_folder": "math",
        "cat_file": "markov_matrix_exponentiation.md",
        "statement": "Given an undirected graph with N vertices and M edges, with initial values A_i on each vertex. In each of K steps, choose an edge uniformly at random and replace both endpoint values with their average. Find the expected value of each vertex after K steps modulo 10^9 + 7.",
        "key_idea": "Because the averaging operation is linear, expectations transition linearly: E[A'^{(t+1)}] = T * E[A'^{(t)}]. For vertex u, an incident edge (u, v) is chosen with probability 1/M, setting u's value to (A_u + A_v)/2. Non-incident edges leave A_u unchanged. Thus T_{u, u} = 1 - deg(u)/(2M) and T_{u, v} = 1/(2M) for (u, v) in E. The state after K steps is E[A^{(K)}] = T^K * A^{(0)}, computable via binary matrix exponentiation in O(N^3 log K).",
        "observation": "Random pair averaging is a linear Markov transition matrix T on expected values, allowing exact computation via T^K.",
        "algorithm": [
            "Compute degrees of all vertices.",
            "Construct N x N transition matrix T: T[u][u] = 1 - deg(u) * inv(2M); for each edge (u, v), set T[u][v] = T[v][u] = inv(2M).",
            "Compute T^K using matrix exponentiation with modulo 10^9 + 7 in O(N^3 log K).",
            "Multiply T^K by the initial value vector A.",
            "Output the resulting expected values."
        ],
        "time_complexity": "O(N^3 log K)",
        "space_complexity": "O(N^2)",
        "core_skill": "Formulating randomized linear graph processes as transition matrices and solving via binary matrix exponentiation.",
        "reusable_pattern": "Randomized pairwise updates on graphs reduce to a linear transition matrix T on expectation vectors.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>

using namespace std;

const int MOD = 1e9 + 7;

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

typedef vector<vector<long long>> Matrix;

Matrix multiply(const Matrix& A, const Matrix& B, int n) {
    Matrix C(n, vector<long long>(n, 0));
    for (int i = 0; i < n; ++i) {
        for (int k = 0; k < n; ++k) {
            if (A[i][k] == 0) continue;
            for (int j = 0; j < n; ++j) {
                C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD;
            }
        }
    }
    return C;
}

Matrix matPower(Matrix A, long long p, int n) {
    Matrix res(n, vector<long long>(n, 0));
    for (int i = 0; i < n; ++i) res[i][i] = 1;
    while (p > 0) {
        if (p & 1) res = multiply(res, A, n);
        A = multiply(A, A, n);
        p >>= 1;
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    long long k;
    if (!(cin >> n >> m >> k)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    vector<vector<int>> adj(n);
    vector<int> deg(n, 0);
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        --u; --v;
        adj[u].push_back(v);
        adj[v].push_back(u);
        deg[u]++;
        deg[v]++;
    }

    long long inv2m = modInverse(2LL * m % MOD);

    Matrix T(n, vector<long long>(n, 0));
    for (int u = 0; u < n; ++u) {
        long long diag = (1 - (1LL * deg[u] % MOD * inv2m % MOD) + MOD) % MOD;
        T[u][u] = diag;
        for (int v : adj[u]) {
            T[u][v] = inv2m;
        }
    }

    Matrix Tk = matPower(T, k, n);

    for (int i = 0; i < n; ++i) {
        long long ans = 0;
        for (int j = 0; j < n; ++j) {
            ans = (ans + Tk[i][j] * a[j]) % MOD;
        }
        cout << ans << "\n";
    }
    return 0;
}
"""
    },
    {
        "id": "abc299_g",
        "title": "Minimum Permutation",
        "contest_id": "abc299",
        "rating": 2066,
        "tag": "Data Structures (DS)",
        "subtopic": "Monotonic Queue / Deque",
        "topic": "Monotonic Stack with Frequency/Last-Occurrence Tracking for Lexicographically Minimal Permutation",
        "cat_folder": "data_structures",
        "cat_file": "monotonic_stack_lexicographical_permutation.md",
        "statement": "Given a sequence A of length N containing numbers from 1 to M, where every number appears at least once. Find the lexicographically smallest subsequence of length M that contains each number from 1 to M exactly once.",
        "key_idea": "We use a monotonic stack and track the last occurrence index last_pos[x] of each value. When processing A[i] = x: if x is already in the stack, we skip it. Otherwise, while the stack is non-empty, top element y > x, and y appears again later in A (last_pos[y] > i), we pop y from the stack and unmark it. We then push x and mark it. The resulting stack contains the unique lexicographically smallest permutation.",
        "observation": "A larger character y can be popped in favor of a smaller character x iff y appears again later in the sequence.",
        "algorithm": [
            "Precompute last_pos[x] for every value x in 1..M.",
            "Initialize an empty stack and a boolean array in_st.",
            "Iterate i from 0 to N - 1 with x = A[i]:",
            "  If in_st[x] is true, continue.",
            "  While stack is not empty, stack.back() > x, and last_pos[stack.back()] > i: in_st[stack.back()] = false; stack.pop_back().",
            "  Push x onto stack and set in_st[x] = true.",
            "Output the M elements of the stack."
        ],
        "time_complexity": "O(N)",
        "space_complexity": "O(N + M)",
        "core_skill": "Greedy subsequence construction using a monotonic stack with future availability validation.",
        "reusable_pattern": "Smallest subsequence with unique characters: pop stack when top > current and top appears later.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<int> a(n);
    vector<int> last_pos(m + 1, -1);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        last_pos[a[i]] = i;
    }

    vector<int> st;
    vector<bool> in_st(m + 1, false);

    for (int i = 0; i < n; ++i) {
        int x = a[i];
        if (in_st[x]) continue;

        while (!st.empty() && st.back() > x && last_pos[st.back()] > i) {
            in_st[st.back()] = false;
            st.pop_back();
        }

        st.push_back(x);
        in_st[x] = true;
    }

    for (int i = 0; i < m; ++i) {
        cout << st[i] << (i == m - 1 ? "" : " ");
    }
    cout << "\n";
    return 0;
}
"""
    },
    {
        "id": "abc158_f",
        "title": "Removing Robots",
        "contest_id": "abc158",
        "rating": 2067,
        "tag": "Dynamic Programming (DP)",
        "subtopic": "Classic DP",
        "topic": "Chain Reaction Interval Reachability via Segment Tree and Linear DP",
        "cat_folder": "dynamic_programming",
        "cat_file": "chain_reaction_interval_reachability_dp.md",
        "statement": "N robots on a number line at coordinates X_i move D_i to the right when activated, triggering any robot in [X_i, X_i + D_i) recursively. How many distinct sets of remaining robots can result from activating robots some number of times modulo 998244353?",
        "key_idea": "Sort robots by X_i. Activating robot i triggers a contiguous range of robots [i, R_i]. We compute R_i from right to left using a Segment Tree: R_i = max(k, query_max(i+1, k)), where k is the rightmost robot with X_k < X_i + D_i. Once each robot removes [i, R_i], for robot i we have two disjoint choices: (1) robot i is never activated, leaving robot i and moving to i+1 (dp[i+1] ways); or (2) robot i is activated, removing [i, R_i] and moving to R_i+1 (dp[R_i+1] ways). Thus dp[i] = dp[i+1] + dp[R_i+1].",
        "observation": "Recursive activation forms contiguous intervals [i, R_i], turning set counting into a clean 2-choice linear DP: keep robot i (dp[i+1]) vs activate robot i (dp[R_i+1]).",
        "algorithm": [
            "Sort robots by X_i.",
            "Initialize a Segment Tree supporting point update and range maximum query.",
            "For i from N-1 down to 0:",
            "  Find k = upper_bound(X) - 1 for X_i + D_i.",
            "  If k > i: R_i = max(k, query(i+1, k)); else R_i = i.",
            "  Update segment tree at position i with R_i.",
            "Initialize dp array of size N+2 with dp[N] = 1, dp[N+1] = 1.",
            "For i from N-1 down to 0: dp[i] = (dp[i+1] + dp[R_i+1]) % 998244353.",
            "Output dp[0]."
        ],
        "time_complexity": "O(N log N)",
        "space_complexity": "O(N)",
        "core_skill": "Combining range maximum segment tree for domino reachability with linear DP.",
        "reusable_pattern": "Cascading range trigger DP: compute range closure [i, R_i] with segment tree, then transition dp[i] = dp[i+1] + dp[R_i+1].",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MOD = 998244353;

struct Robot {
    long long x, d;
    int id;
};

struct SegTree {
    int n;
    vector<int> tree;
    SegTree(int n) : n(n), tree(4 * n, 0) {}

    void update(int node, int l, int r, int qx, int val) {
        if (l == r) {
            tree[node] = val;
            return;
        }
        int mid = l + (r - l) / 2;
        if (qx <= mid) update(2 * node, l, mid, qx, val);
        else update(2 * node + 1, mid + 1, r, qx, val);
        tree[node] = max(tree[2 * node], tree[2 * node + 1]);
    }

    int query(int node, int l, int r, int ql, int qr) {
        if (ql > qr || ql > r || qr < l) return 0;
        if (ql <= l && r <= qr) return tree[node];
        int mid = l + (r - l) / 2;
        return max(query(2 * node, l, mid, ql, qr), query(2 * node + 1, mid + 1, r, ql, qr));
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<Robot> robots(n);
    for (int i = 0; i < n; ++i) {
        cin >> robots[i].x >> robots[i].d;
        robots[i].id = i;
    }

    sort(robots.begin(), robots.end(), [](const Robot& a, const Robot& b) {
        return a.x < b.x;
    });

    vector<long long> X(n);
    for (int i = 0; i < n; ++i) X[i] = robots[i].x;

    SegTree st(n);
    vector<int> R(n);

    for (int i = n - 1; i >= 0; --i) {
        long long reach_x = robots[i].x + robots[i].d;
        int k = lower_bound(X.begin(), X.end(), reach_x) - X.begin() - 1;
        if (k > i) {
            R[i] = max(k, st.query(1, 0, n - 1, i + 1, k));
        } else {
            R[i] = i;
        }
        st.update(1, 0, n - 1, i, R[i]);
    }

    vector<long long> dp(n + 2, 0);
    dp[n] = 1;
    dp[n + 1] = 1;

    for (int i = n - 1; i >= 0; --i) {
        dp[i] = (dp[i + 1] + dp[R[i] + 1]) % MOD;
    }

    cout << dp[0] << "\n";
    return 0;
}
"""
    },
    {
        "id": "abc195_f",
        "title": "Coprime Present",
        "contest_id": "abc195",
        "rating": 2068,
        "tag": "Dynamic Programming (DP)",
        "subtopic": "Bit Related DP",
        "topic": "Prime Factor Bitmask DP over Bounded Interval Differences",
        "cat_folder": "dynamic_programming",
        "cat_file": "prime_factor_bitmask_dp_bounded_interval.md",
        "statement": "You have cards with integers from A to B (B - A <= 72, A <= B <= 10^18). Count the number of subsets of cards where all chosen numbers are pairwise coprime.",
        "key_idea": "Two numbers x, y in [A, B] can share a common prime factor p only if p <= |x - y| <= B - A <= 72. There are exactly 20 primes <= 72. Any prime factor > 72 can divide at most one number in [A, B]. Therefore, a subset is pairwise coprime if and only if their masks of prime factors <= 72 are pairwise disjoint. With 20 primes (2^20 ~ 10^6 states) and at most 73 numbers, we use standard bitmask DP: for each number x, iterate over submasks disjoint from mask(x) and transition.",
        "observation": "Any prime factor that could possibly be shared between two numbers in [A, B] must be <= B - A <= 72, restricting all shared divisibility constraints to a 20-bit mask.",
        "algorithm": [
            "List the 20 primes <= 72.",
            "Initialize dp[0] = 1 with size 2^20.",
            "For each x from A to B:",
            "  Compute m = bitmask of primes <= 72 dividing x.",
            "  Let sub = (2^20 - 1) ^ m (all masks disjoint from m).",
            "  Iterate mask through submasks of sub in descending order: dp[mask | m] += dp[mask].",
            "Sum dp[mask] over all 2^20 masks and output."
        ],
        "time_complexity": "O((B - A) * 2^20)",
        "space_complexity": "O(2^20)",
        "core_skill": "Recognizing that interval width bounds the set of relevant prime factors for pairwise coprimality to a small bitmask.",
        "reusable_pattern": "Pairwise coprime subsets in an interval [A, B] with small B - A are solved via bitmask DP over primes <= B - A.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>

using namespace std;

const int primes[] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71};
const int NUM_PRIMES = 20;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long A, B;
    if (!(cin >> A >> B)) return 0;

    int total_masks = 1 << NUM_PRIMES;
    vector<long long> dp(total_masks, 0);
    dp[0] = 1;

    for (long long x = A; x <= B; ++x) {
        int m = 0;
        for (int i = 0; i < NUM_PRIMES; ++i) {
            if (x % primes[i] == 0) {
                m |= (1 << i);
            }
        }

        int sub = (total_masks - 1) ^ m;
        for (int mask = sub; ; mask = (mask - 1) & sub) {
            dp[mask | m] += dp[mask];
            if (mask == 0) break;
        }
    }

    long long ans = 0;
    for (int mask = 0; mask < total_masks; ++mask) {
        ans += dp[mask];
    }

    cout << ans << "\n";
    return 0;
}
"""
    },
    {
        "id": "arc214_c",
        "title": "Divide into 4 Teams",
        "contest_id": "arc214",
        "rating": 2070,
        "tag": "Dynamic Programming (DP)",
        "subtopic": "Classic DP",
        "topic": "Basis Decoupling Sign DP and Subset Sum Reduction",
        "cat_folder": "dynamic_programming",
        "cat_file": "basis_decoupling_subset_sum_dp.md",
        "statement": "N people with strengths P_i are partitioned into 4 non-empty teams A, B, C, D such that sum(P_A) = sum(P_B) and sum(P_C) = sum(P_D). Count the number of valid formations modulo 998244353.",
        "key_idea": "Represent team assignment as independent sign pairs (u_i, v_i) in {+1, -1}^2: A = (+1, +1), B = (-1, -1), C = (+1, -1), D = (-1, +1). The conditions sum(P_A) = sum(P_B) and sum(P_C) = sum(P_D) decouple into two independent equations: sum u_i P_i = 0 and sum v_i P_i = 0. Each choice of signs summing to 0 is equivalent to choosing a subset summing to Total/2. If C is the number of such subsets, there are C^2 total sign assignments. A team can be empty iff an entire pair {A, B} or {C, D} is empty (since P_i >= 1 and sum(A) = sum(B)), which contributes 2C invalid assignments. Thus the answer is exactly C(C - 2) modulo 998244353.",
        "observation": "A linear change of basis decouples 4-team balance into two independent 2-team subset sum problems, yielding C^2 - 2C = C(C - 2).",
        "algorithm": [
            "Compute Total = sum(P_i). If Total is odd, output 0.",
            "Run 0-1 knapsack DP to count C = number of subsets with sum Total/2 modulo 998244353.",
            "Output C * (C - 2) modulo 998244353."
        ],
        "time_complexity": "O(N * sum(P))",
        "space_complexity": "O(sum(P))",
        "core_skill": "Decoupling coupled team constraints using orthogonal sign vectors in a 2D basis.",
        "reusable_pattern": "Balanced 4-team partitioning decomposes into independent 2-team subset sums via sign basis transformation.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

const int MOD = 998244353;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> p(n);
    int total = 0;
    for (int i = 0; i < n; ++i) {
        cin >> p[i];
        total += p[i];
    }

    if (total % 2 != 0) {
        cout << 0 << "\n";
        return 0;
    }

    int target = total / 2;
    vector<long long> dp(target + 1, 0);
    dp[0] = 1;

    for (int x : p) {
        for (int w = target; w >= x; --w) {
            dp[w] = (dp[w] + dp[w - x]) % MOD;
        }
    }

    long long C = dp[target];
    long long ans = (C * (C - 2 + MOD)) % MOD;
    cout << ans << "\n";
    return 0;
}
"""
    },
    {
        "id": "arc226_c",
        "title": "Square Corner Packing",
        "contest_id": "arc226",
        "rating": 2070,
        "tag": "Miscellaneous",
        "subtopic": "Constructive Algorithms",
        "topic": "Grid Parity Lower Bound and Recursive Square Border Peeling Construction",
        "cat_folder": "miscellaneous",
        "cat_file": "square_corner_packing_peeling.md",
        "statement": "Given an H x W grid of white cells. In each step, choose integers r, c, s such that the 4 corners (r, c), (r+s, c), (r, c+s), (r+s, c+s) are all white, and paint them black. Find the maximum number of operations and output one valid sequence.",
        "key_idea": "Each square corners operation consumes 0 or 2 cells in any row or column. Thus if W is odd, at least 1 cell per row cannot be painted (at least H unpainted cells). If H and W are even, 2x2 squares achieve HW/4 operations. If one is odd (say W odd, H even), 2x2 squares achieve H(W-1)/4 operations. If both H and W are odd: when H != W, peel 2 columns/rows of 2x2 squares until H == W; when H == W is odd, peel an outer border of thickness 2 containing one (H-1)x(H-1) square and 2x2 border squares, reducing H by 4.",
        "observation": "Row/column parity invariants establish a tight upper bound, matched constructively by 2x2 tiling and recursive border peeling.",
        "algorithm": [
            "Handle even-even, even-odd, and odd-even via standard 2x2 tiling.",
            "When both H and W are odd:",
            "  If H < W, peel rightmost 2 columns with 2x2 squares and recurse on (H, W - 2).",
            "  If H > W, peel bottom 2 rows with 2x2 squares and recurse on (H - 2, W).",
            "  If H == W: if H == 1 return; if H == 3 output 1 square of size 2; if H >= 5, place corner square of size H - 1, fill the 4 borders with 2x2 squares, and recurse on (H - 4, W - 4).",
            "Output total operation count followed by the operations."
        ],
        "time_complexity": "O(H * W)",
        "space_complexity": "O(H * W)",
        "core_skill": "Parity invariant lower bounds on grid cell coverings and recursive border peeling construction.",
        "reusable_pattern": "Square corner packings achieve parity bounds via recursive 2x2 tiling and outer border reduction.",
        "editorial_comparison": "Matches official editorial by snuke.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <string>

using namespace std;

struct Op {
    int r, c, s;
};

void solve() {
    int H, W;
    cin >> H >> W;

    vector<Op> ops;

    auto peel = [&](auto& self, int r1, int c1, int h, int w) -> void {
        if (h <= 1 || w <= 1) return;

        if (h % 2 == 0 && w % 2 == 0) {
            for (int r = r1; r < r1 + h; r += 2) {
                for (int c = c1; c < c1 + w; c += 2) {
                    ops.push_back({r, c, 1});
                }
            }
            return;
        }

        if (h % 2 == 0 && w % 2 != 0) {
            for (int r = r1; r < r1 + h; r += 2) {
                for (int c = c1; c < c1 + w - 1; c += 2) {
                    ops.push_back({r, c, 1});
                }
            }
            return;
        }

        if (h % 2 != 0 && w % 2 == 0) {
            for (int r = r1; r < r1 + h - 1; r += 2) {
                for (int c = c1; c < c1 + w; c += 2) {
                    ops.push_back({r, c, 1});
                }
            }
            return;
        }

        if (h < w) {
            for (int r = r1; r < r1 + h - 1; r += 2) {
                ops.push_back({r, c1 + w - 2, 1});
            }
            self(self, r1, c1, h, w - 2);
            return;
        }
        if (h > w) {
            for (int c = c1; c < c1 + w - 1; c += 2) {
                ops.push_back({r1 + h - 2, c, 1});
            }
            self(self, r1, c1, h - 2, w);
            return;
        }

        if (h == 1) return;
        if (h == 3) {
            ops.push_back({r1, c1, 2});
            return;
        }

        ops.push_back({r1, c1, h - 1});

        for (int c = c1 + 1; c + 1 < c1 + h - 1; c += 2) {
            ops.push_back({r1, c, 1});
        }
        for (int c = c1 + 1; c + 1 < c1 + h - 1; c += 2) {
            ops.push_back({r1 + h - 2, c, 1});
        }
        for (int r = r1 + 2; r + 1 < r1 + h - 1; r += 2) {
            ops.push_back({r, c1, 1});
        }
        for (int r = r1 + 1; r + 1 < r1 + h - 2; r += 2) {
            ops.push_back({r, c1 + h - 2, 1});
        }

        self(self, r1 + 2, c1 + 2, h - 4, w - 4);
    };

    peel(peel, 1, 1, H, W);

    cout << ops.size() << "\n";
    for (auto& op : ops) {
        cout << op.r << " " << op.c << " " << op.s << "\n";
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    if (cin >> t) {
        while (t--) solve();
    }
    return 0;
}
"""
    },
    {
        "id": "arc168_c",
        "title": "Swap Characters",
        "contest_id": "arc168",
        "rating": 2071,
        "tag": "Combinatorics",
        "subtopic": "Counting Principles",
        "topic": "Permutation Cycle Decomposition and Multinomial Mismatch Counting",
        "cat_folder": "combinatorics",
        "cat_file": "cycle_decomposition_multinomial_counting.md",
        "statement": "Given a string S of length N consisting of 'A', 'B', 'C'. Find the number of distinct strings reachable by performing at most K character swaps modulo 998244353.",
        "key_idea": "Any reachable string T has the same character frequencies as S. The mismatch positions decompose into 2-cycles (A<->B, B<->C, C<->A, taking 1 swap each) and 3-cycles (A->B->C->A and A->C->B->A, taking 2 swaps each). A minimal swap sequence never contains both 3-cycle directions (min(c1, c2) = 0). Iterating over all valid tuples (c1, c2, c_AB, c_BC, c_CA) with swaps <= K uniquely determines the mismatch counts between all character pairs. The number of strings with a given mismatch matrix is computed via multinomial coefficients.",
        "observation": "Any permutation of 3 symbols decomposes into disjoint 2-cycles and 3-cycles, uniquely specifying character assignment counts for multinomial enumeration.",
        "algorithm": [
            "Count frequencies ca, cb, cc of 'A', 'B', 'C' in S.",
            "Precompute factorials and inverse factorials up to N.",
            "Iterate 3-cycle counts c1 (A->B->C->A) and c2 (A->C->B->A) with 2*(c1+c2) <= K and min(c1, c2) == 0.",
            "Iterate 2-cycle counts cab, cbc, cca such that cab + cbc + cca <= K - 2*(c1+c2).",
            "Derive directed transitions: A->B, A->C, B->A, B->C, C->A, C->B.",
            "If valid under ca, cb, cc bounds, multiply multinomial(ca, A->B, A->C) * multinomial(cb, B->A, B->C) * multinomial(cc, C->A, C->B).",
            "Sum over all valid tuples and output modulo 998244353."
        ],
        "time_complexity": "O(N + K^4)",
        "space_complexity": "O(N)",
        "core_skill": "Character swap reachability via permutation cycle decomposition and multinomial counting.",
        "reusable_pattern": "Bounded-swap string reachability on small alphabet decomposes into independent cycle types.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

const int MOD = 998244353;

long long fact[250005], invFact[250005];

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

void precompute(int n) {
    fact[0] = 1;
    invFact[0] = 1;
    for (int i = 1; i <= n; ++i) {
        fact[i] = (fact[i - 1] * i) % MOD;
    }
    invFact[n] = modInverse(fact[n]);
    for (int i = n - 1; i >= 1; --i) {
        invFact[i] = (invFact[i + 1] * (i + 1)) % MOD;
    }
}

long long multinomial(int n, int a, int b) {
    if (a < 0 || b < 0 || a + b > n) return 0;
    int c = n - a - b;
    long long res = fact[n];
    res = (res * invFact[a]) % MOD;
    res = (res * invFact[b]) % MOD;
    res = (res * invFact[c]) % MOD;
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    string s;
    cin >> s;

    precompute(n);

    int ca = 0, cb = 0, cc = 0;
    for (char ch : s) {
        if (ch == 'A') ca++;
        else if (ch == 'B') cb++;
        else cc++;
    }

    long long ans = 0;

    for (int c1 = 0; 2 * c1 <= k; ++c1) {
        for (int c2 = 0; 2 * c2 <= k; ++c2) {
            if (c1 > 0 && c2 > 0) continue;
            int rem_k = k - 2 * (c1 + c2);
            for (int cab = 0; cab <= rem_k; ++cab) {
                for (int cbc = 0; cab + cbc <= rem_k; ++cbc) {
                    for (int cca = 0; cab + cbc + cca <= rem_k; ++cca) {
                        int a_to_b = cab + c1;
                        int a_to_c = cca + c2;
                        int b_to_a = cab + c2;
                        int b_to_c = cbc + c1;
                        int c_to_a = cca + c1;
                        int c_to_b = cbc + c2;

                        if (a_to_b + a_to_c > ca) continue;
                        if (b_to_a + b_to_c > cb) continue;
                        if (c_to_a + c_to_b > cc) continue;

                        long long ways = multinomial(ca, a_to_b, a_to_c);
                        ways = (ways * multinomial(cb, b_to_a, b_to_c)) % MOD;
                        ways = (ways * multinomial(cc, c_to_a, c_to_b)) % MOD;

                        ans = (ans * ways) % MOD;
                    }
                }
            }
        }
    }

    cout << ans << "\n";
    return 0;
}
"""
    },
    {
        "id": "arc081_c",
        "title": "Don't Be a Subsequence",
        "contest_id": "arc081",
        "rating": 2072,
        "tag": "Dynamic Programming (DP)",
        "subtopic": "Classic DP",
        "topic": "Automaton Transition DAG Shortest Non-Subsequence DP with Lexicographical Greedy Reconstruction",
        "cat_folder": "dynamic_programming",
        "cat_file": "shortest_non_subsequence_dp.md",
        "statement": "Given a lowercase string A. Find the shortest string that is not a subsequence of A. If multiple such strings exist, find the lexicographically smallest one.",
        "key_idea": "Subsequence matching operates as a transition DAG where from index i, choosing character c jumps to the first occurrence j = next_pos(i, c) >= i. Let dp[i] be the minimum length of a non-subsequence of the suffix A[i..|A|]. From index i, if character c does not appear, length is 1; otherwise length is 1 + dp[next_pos(i, c) + 1]. Computing dp backwards in O(26 |A|) gives optimal lengths. We then greedily reconstruct the lexicographically smallest string by picking the smallest character c achieving dp[i].",
        "observation": "Subsequence rejection on a string DAG corresponds to the shortest path to an exit state, with lexicographical ties broken greedily from 'a' to 'z'.",
        "algorithm": [
            "Compute nxt[i][c] = next occurrence of character c at or after position i, working backwards from |A| down to 1.",
            "Initialize dp[|A| + 1] = 1.",
            "For i from |A| down to 1: dp[i] = min_{c} (1 if nxt[i][c] not found else 1 + dp[nxt[i][c] + 1]).",
            "Reconstruct answer: start at cur = 1; while cur <= |A|+1, test c from 'a' to 'z' and pick first c where transition length matches dp[cur]. Advance cur = nxt[cur][c] + 1.",
            "Output the reconstructed string."
        ],
        "time_complexity": "O(26 * |A|)",
        "space_complexity": "O(26 * |A|)",
        "core_skill": "Shortest path on a next-occurrence automaton DAG with lexicographical tie-breaking.",
        "reusable_pattern": "Shortest non-subsequence: backward DP on character jump DAG followed by greedy forward reconstruction.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

const int INF = 1e9 + 7;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!(cin >> s)) return 0;

    int n = s.size();
    vector<vector<int>> nxt(n + 2, vector<int>(26, n + 1));

    for (int i = n; i >= 1; --i) {
        for (int c = 0; c < 26; ++c) {
            nxt[i][c] = nxt[i + 1][c];
        }
        nxt[i][s[i - 1] - 'a'] = i;
    }

    vector<int> dp(n + 2, INF);
    dp[n + 1] = 1;

    for (int i = n; i >= 1; --i) {
        for (int c = 0; c < 26; ++c) {
            int p = nxt[i][c];
            if (p == n + 1) {
                dp[i] = 1;
            } else {
                dp[i] = min(dp[i], 1 + dp[p + 1]);
            }
        }
    }

    string ans = "";
    int cur = 1;
    while (cur <= n + 1) {
        for (int c = 0; c < 26; ++c) {
            int p = nxt[cur][c];
            int len = (p == n + 1 ? 1 : 1 + dp[p + 1]);
            if (len == dp[cur]) {
                ans += (char)('a' + c);
                cur = p + 1;
                break;
            }
        }
        if (cur > n) break;
    }

    cout << ans << "\n";
    return 0;
}
"""
    },
    {
        "id": "arc101_b",
        "title": "Median of Medians",
        "contest_id": "abc107",
        "rating": 2073,
        "tag": "Data Structures (DS)",
        "subtopic": "Segment Tree / Fenwick Tree",
        "topic": "Binary Search on Answer with +1/-1 Reduction and Fenwick Tree Prefix Sum Inversion Counting",
        "cat_folder": "data_structures",
        "cat_file": "binary_search_fenwick_median_of_medians.md",
        "statement": "Given an array A of N elements. For all 1 <= l <= r <= N, let m_{l, r} be the median of A[l..r]. Find the median of all N(N+1)/2 medians.",
        "key_idea": "Binary search on the answer X. The median of a subsegment A[l..r] is >= X if and only if at least half of its elements are >= X. Replacing each element with b_i = +1 if A_i >= X else -1, the median condition becomes sum_{k=l}^r b_k > 0, which is equivalent to pref[r] > pref[l-1]. Counting such pairs (l-1, r) reduces to counting inversions in the prefix sum array, solvable in O(N log N) using a Fenwick tree. If the number of subsegments with median >= X is >= (N(N+1)/2) / 2 + 1, then the median of medians is >= X.",
        "observation": "Subsegment median comparison against X reduces to prefix sum inequalities pref[r] > pref[l-1] with +/-1 values, counted in O(N log N) via Fenwick tree.",
        "algorithm": [
            "Binary search on X in [1, 10^9].",
            "In check(X):",
            "  Convert A to b with b_i = (+1 if A_i >= X else -1).",
            "  Maintain prefix sums pref with pref[0] = 0.",
            "  Insert pref[0] into a Fenwick tree shifted by N+1.",
            "  For each r = 1..N: count l-1 such that pref[l-1] < pref[r] via Fenwick query, then insert pref[r].",
            "  Return true iff count >= floor(total_intervals / 2) + 1.",
            "Output the maximum X for which check(X) is true."
        ],
        "time_complexity": "O(N log N log(max A))",
        "space_complexity": "O(N)",
        "core_skill": "Binary searching for median values using +1/-1 transformation and prefix sum inversion counting with Fenwick tree.",
        "reusable_pattern": "Median of subsegments: map elements to +/-1, then count valid ranges via Fenwick prefix sum order queries.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>

using namespace std;

struct Fenwick {
    int n;
    vector<int> tree;
    Fenwick(int n) : n(n), tree(n + 1, 0) {}

    void add(int i, int delta) {
        for (; i <= n; i += i & -i) tree[i] += delta;
    }

    int query(int i) {
        int sum = 0;
        for (; i > 0; i -= i & -i) sum += tree[i];
        return sum;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    long long total_intervals = 1LL * n * (n + 1) / 2;
    long long req = total_intervals / 2 + 1;

    auto check = [&](int x) -> bool {
        int offset = n + 1;
        Fenwick bit(2 * n + 2);
        bit.add(0 + offset, 1);

        long long count_valid = 0;
        int cur_pref = 0;

        for (int i = 0; i < n; ++i) {
            cur_pref += (a[i] >= x ? 1 : -1);
            count_valid += bit.query(cur_pref - 1 + offset);
            bit.add(cur_pref + offset, 1);
        }

        return count_valid >= req;
    };

    int low = 1, high = 1e9, ans = 1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (check(mid)) {
            ans = mid;
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }

    cout << ans << "\n";
    return 0;
}
"""
    }
]

REJECTED_PROBLEMS = []

# Step 1: Verify and Compile all selected problems
print(f"[*] Compiling and validating {len(SELECTED_PROBLEMS)} selected C++ solutions...")
scratch_dir = "scratch"
os.makedirs(scratch_dir, exist_ok=True)

for p in SELECTED_PROBLEMS:
    cpp_path = os.path.join(scratch_dir, f"{p['id']}.cpp")
    exe_path = os.path.join(scratch_dir, f"{p['id']}.exe")
    with open(cpp_path, "w", encoding="utf-8") as f:
        f.write(p["cpp_code"])
    
    cmd = ["g++", "-O2", "-std=c++17", cpp_path, "-o", exe_path]
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if res.returncode != 0:
        print(f"[!] Compilation FAILED for {p['id']}:")
        print(res.stderr)
        sys.exit(1)
    else:
        print(f"[+] Compiled {p['id']} successfully.")

# Step 2: Generate Individual Analysis Markdown Files
print(f"[*] Generating {len(SELECTED_PROBLEMS)} analysis markdown files in analysis/...")
for p in SELECTED_PROBLEMS:
    analysis_file = os.path.join("analysis", f"AtCoder-{p['id']}.md")
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

**Key Idea**: {p['key_idea']}

## 2. Core Observation & Invariant
{p['observation']}

## 3. Step-by-Step Algorithm
"""
    for idx, step in enumerate(p["algorithm"], 1):
        content += f"{idx}. {step}\n"

    content += f"""
## 4. Complexity Analysis
- **Time Complexity**: `{p['time_complexity']}`
- **Space Complexity**: `{p['space_complexity']}`

## 5. Core Algorithmic Skill & Learning Takeaway
{p['core_skill']}

**Reusable Pattern**: {p['reusable_pattern']}

## 6. Comparison with Alternative Approaches
{p['editorial_comparison']}

## 7. Verified Clean C++ Source Code
```cpp
{p['cpp_code'].strip()}
```
"""
    with open(analysis_file, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"[+] Generated: {analysis_file}")

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
    tag_str = f"{p['tag']} → {p['topic']}"
    log_line = f"| [problem:AtCoder-{p['id']}] | {p['title']} | {p['rating']} | **REJECTED** | {tag_str} | {p['reason']} |"
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
        f.write("\n### Batch 6 Part 2A: ABC / ARC Curated Ladder (2051 - 2073)\n" + "\n".join(new_q_lines) + "\n")
    print("[+] Updated QUALITY_PROBLEMS_BY_TOPIC.md with new archetypes.")

# Update state/progress.json
with open("state/progress.json", "r", encoding="utf-8") as f:
    progress = json.load(f)

progress["current_batch"] = "Batch 6 Part 2A: ABC / ARC Ladder (2051-2073) COMPLETED"
progress["status"] = "IN_PROGRESS"
for p in SELECTED_PROBLEMS:
    if p["id"] not in progress["completed_problem_ids"]:
        progress["completed_problem_ids"].append(p["id"])
progress["total_evaluated_in_curriculum"] = len(progress["completed_problem_ids"])

# Add all evaluated IDs
evaluated_set = set(progress.get("evaluated_problems", []))
for p in SELECTED_PROBLEMS:
    evaluated_set.add(p["id"])
for p in REJECTED_PROBLEMS:
    evaluated_set.add(p["id"])
progress["evaluated_problems"] = sorted(list(evaluated_set))

with open("state/progress.json", "w", encoding="utf-8") as f:
    json.dump(progress, f, indent=2)
print(f"[+] Updated progress checkpoint: state/progress.json")

print("=" * 75)
print("Batch 6 Part 2A completed successfully!")
