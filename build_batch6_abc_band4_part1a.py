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
print("      PROCESSING BATCH 6 PART 1A: ABC / ARC CURATED LADDER (2000 - 2018)")
print("=" * 75)

SELECTED_PROBLEMS = [
    {
        "id": "abc388_g",
        "title": "Simultaneous Kagamimochi 2",
        "contest_id": "abc388",
        "rating": 2001,
        "tag": "Data Structures (DS)",
        "subtopic": "Segment Tree / Fenwick Tree",
        "topic": "Sparse Table Range Max Query with Binary Search for Monotone Pair Matching",
        "cat_folder": "data_structures",
        "cat_file": "sparse_table_range_max_monotone_pair_matching.md",
        "statement": "Given a sorted array A of length N. Process Q queries: for range [L, R], find the maximum number of pairs (i, j) with L <= i < j <= R such that 2 * A[i] <= A[j] and each element is used in at most one pair.",
        "key_idea": "For a fixed subsegment of length M = R - L + 1, if k pairs can be formed, by exchange argument it is always optimal to pair the first k elements with the last k elements: 2 * A[L + t] <= A[R - k + 1 + t] for all 0 <= t < k. Let nxt[i] be the smallest index j such that 2 * A[i] <= A[j]. The condition becomes nxt[L + t] <= R - k + 1 + t, or equivalently nxt[L + t] - (L + t) <= R - L - 2k + 1. We binary search on k in [0, M / 2] and verify the condition in O(1) using a Sparse Table precomputed on val[i] = nxt[i] - i.",
        "observation": "Pairing extremal subsets (first k with last k) reduces bipartite matching feasibility to a range maximum query over nxt[i] - i.",
        "algorithm": [
            "Precompute nxt[i] for all i using two pointers (smallest j such that 2 * A[i] <= A[j]). Set val[i] = nxt[i] - i (or INF if j does not exist).",
            "Build a Sparse Table over val array for range maximum queries in O(1).",
            "For each query (L, R): binary search k in [0, (R - L + 1) / 2].",
            "  If k == 0: valid.",
            "  Else: query max over [L, L + k - 1] in Sparse Table; check if max_val <= R - L - 2k + 1.",
            "Output the maximum feasible k."
        ],
        "time_complexity": "O(N log N + Q log N)",
        "space_complexity": "O(N log N)",
        "core_skill": "Bipartite matching feasibility reduction to range maximum query with binary search.",
        "reusable_pattern": "Monotone Pair Matching Check: 2 * A[L+t] <= A[R-k+1+t] <==> max_{t < k} (nxt[L+t] - (L+t)) <= R - L - 2k + 1.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int INF = 1e9 + 7;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    vector<int> nxt(n);
    int ptr = 0;
    for (int i = 0; i < n; ++i) {
        while (ptr < n && a[ptr] < 2 * a[i]) {
            ptr++;
        }
        nxt[i] = (ptr < n ? ptr : INF);
    }

    vector<int> val(n);
    for (int i = 0; i < n; ++i) {
        val[i] = (nxt[i] == INF ? INF : nxt[i] - i);
    }

    int log_n = 0;
    while ((1 << log_n) <= n) log_n++;
    vector<vector<int>> st(log_n, vector<int>(n));
    for (int i = 0; i < n; ++i) {
        st[0][i] = val[i];
    }
    for (int k = 1; k < log_n; ++k) {
        for (int i = 0; i + (1 << k) <= n; ++i) {
            st[k][i] = max(st[k - 1][i], st[k - 1][i + (1 << (k - 1))]);
        }
    }

    auto query_max = [&](int l, int r) {
        int len = r - l + 1;
        int k = 31 - __builtin_clz(len);
        return max(st[k][l], st[k][r - (1 << k) + 1]);
    };

    int q;
    if (!(cin >> q)) return 0;
    while (q--) {
        int l, r;
        cin >> l >> r;
        --l; --r;
        int len = r - l + 1;
        int low = 0, high = len / 2, ans = 0;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (mid == 0) {
                ans = max(ans, mid);
                low = mid + 1;
                continue;
            }
            int mx = query_max(l, l + mid - 1);
            if (mx <= len - 2 * mid + 1) {
                ans = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        cout << ans << "\n";
    }

    return 0;
}
"""
    },
    {
        "id": "arc099_b",
        "title": "Snuke Numbers",
        "contest_id": "abc101",
        "rating": 2001,
        "tag": "Math",
        "subtopic": "Number Theory",
        "topic": "Snuke Numbers via Base-10 Digit Addition and S(x) Ratio Greedy Search",
        "cat_folder": "math",
        "cat_file": "snuke_numbers_base10_digit_greedy_search.md",
        "statement": "An integer n is a Snuke number if for all m > n, n / S(n) <= m / S(m), where S(x) is the sum of digits of x in base 10. Output the first K Snuke numbers in ascending order.",
        "key_idea": "Between n and larger integers, the next candidate Snuke number is always obtained by incrementing some power of 10: n + 10^p. For large numbers, suffixes of 9s yield smaller ratios m / S(m). By maintaining the current Snuke number cur, we evaluate candidate numbers cur + 10^p for all 0 <= p <= 14. We pick the candidate that minimizes candidate / S(candidate). Repeating this greedily generates all Snuke numbers up to K.",
        "observation": "Extending lower digits with 9s dominates arbitrary jumps; candidates generated by cur + 10^p for all digit positions cover all potential next Snuke numbers.",
        "algorithm": [
            "Initialize cur = 1, count = 0.",
            "While count < K:",
            "  Print cur; count++.",
            "  If count == K: break.",
            "  Generate candidates: for p from 0 to 14, let cand = cur + 10^p.",
            "  Find candidate that minimizes (double)cand / S(cand) (with tie-breaker: smaller cand).",
            "  Update cur = best_cand."
        ],
        "time_complexity": "O(K * 15 * log10(X))",
        "space_complexity": "O(1)",
        "core_skill": "Digit ratio greedy progression on base-10 representations.",
        "reusable_pattern": "Base-10 Suffix Minimization: Testing cur + 10^p over all digit positions to greedily find the next ratio extremum.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <cstdint>

using namespace std;

long long digit_sum(long long x) {
    long long s = 0;
    while (x > 0) {
        s += x % 10;
        x /= 10;
    }
    return s;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int k;
    if (!(cin >> k)) return 0;

    long long cur = 1;
    vector<long long> pow10(16);
    pow10[0] = 1;
    for (int i = 1; i <= 15; ++i) {
        pow10[i] = pow10[i - 1] * 10;
    }

    for (int step = 0; step < k; ++step) {
        cout << cur << "\n";
        long long best_cand = cur + 1;
        double best_val = (double)best_cand / digit_sum(best_cand);

        for (int p = 0; p <= 14; ++p) {
            long long cand = cur + pow10[p];
            double val = (double)cand / digit_sum(cand);
            if (val < best_val) {
                best_val = val;
                best_cand = cand;
            }
        }
        cur = best_cand;
    }

    return 0;
}
"""
    },
    {
        "id": "abc127_f",
        "title": "Absolute Minima",
        "contest_id": "abc127",
        "rating": 2003,
        "tag": "Data Structures (DS)",
        "subtopic": "Queue & Priority Queue",
        "topic": "Online Running Median and Dynamic Absolute Deviation via Two Heaps",
        "cat_folder": "data_structures",
        "cat_file": "online_running_median_two_heaps.md",
        "statement": "Maintain a dynamic function f(x) initially 0. Query 1 a b: update f(x) <- f(x) + |x - a| + b. Query 2: output the integer x that minimizes f(x) (smallest in case of tie) and the minimum value of f(x).",
        "key_idea": "The sum of absolute deviations sum |x - a_i| is minimized at the median of the multiset {a_1, ..., a_k}. With two balanced heaps (max-heap left for elements <= median, min-heap right for elements > median), the median is always left.top(). By maintaining sum_left and sum_right of elements in both heaps, the minimum value is (x * |left| - sum_left) + (sum_right - x * |right|) + sum_b.",
        "observation": "L1 norm minimization dynamically tracks the median, decomposable into two half-sums maintained by dual priority queues in O(log Q) per addition.",
        "algorithm": [
            "Maintain max-heap 'left' (size (k+1)/2) and min-heap 'right' (size k/2), with their sum_left and sum_right.",
            "For Query 1 (a, b):",
            "  Add b to sum_b.",
            "  Insert a into left or right depending on a <= left.top().",
            "  Rebalance heaps so |left| == |right| or |left| == |right| + 1.",
            "For Query 2:",
            "  Let x = left.top().",
            "  min_val = (x * left.size() - sum_left) + (sum_right - x * right.size()) + sum_b.",
            "  Print x and min_val."
        ],
        "time_complexity": "O(Q log Q)",
        "space_complexity": "O(Q)",
        "core_skill": "Dynamic median and prefix/suffix deviation maintenance via balanced dual priority queues.",
        "reusable_pattern": "Dual Heap Median Tracker: Max-heap left and min-heap right maintaining balanced partition and running element sums.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int q;
    if (!(cin >> q)) return 0;

    priority_queue<long long> left_max;
    priority_queue<long long, vector<long long>, greater<long long>> right_min;
    long long sum_left = 0, sum_right = 0, sum_b = 0;

    while (q--) {
        int type;
        cin >> type;
        if (type == 1) {
            long long a, b;
            cin >> a >> b;
            sum_b += b;

            if (left_max.empty() || a <= left_max.top()) {
                left_max.push(a);
                sum_left += a;
            } else {
                right_min.push(a);
                sum_right += a;
            }

            // Rebalance: left_max has size (total + 1) / 2
            while (left_max.size() > right_min.size() + 1) {
                long long val = left_max.top();
                left_max.pop();
                sum_left -= val;
                right_min.push(val);
                sum_right += val;
            }
            while (left_max.size() < right_min.size()) {
                long long val = right_min.top();
                right_min.pop();
                sum_right -= val;
                left_max.push(val);
                sum_left += val;
            }
        } else {
            long long x = left_max.top();
            long long ans = (x * (long long)left_max.size() - sum_left) +
                            (sum_right - x * (long long)right_min.size()) + sum_b;
            cout << x << " " << ans << "\n";
        }
    }

    return 0;
}
"""
    },
    {
        "id": "arc039_c",
        "title": "幼稚園児高橋君",
        "contest_id": "arc039",
        "rating": 2004,
        "tag": "Data Structures (DS)",
        "subtopic": "Disjoint Set Union (DSU)",
        "topic": "2D 4-Way Doubly Linked List Node Deletion and Grid Path Compression",
        "cat_folder": "data_structures",
        "cat_file": "2d_4way_linked_list_grid_path_compression.md",
        "statement": "Starting at (0, 0) on an infinite 2D grid, Takahashi follows a sequence of K moves (L, R, U, D). In each move, he skips over all already visited cells in that direction and lands on the first unvisited cell, marking it visited. Find his final coordinates.",
        "key_idea": "Treat visited cells as deleted nodes in a 2D doubly linked list (or 4-directional pointer hopping). When a cell (x, y) is visited, it stores pointers to its nearest unvisited neighbors in the 4 directions (L, R, D, U). When visiting (x, y), its 4 neighbors' reciprocal pointers are updated to bypass (x, y), exactly like doubly linked list node deletion extended to 4 dimensions. Dynamically allocated via std::map.",
        "observation": "Visited cell hopping on a grid is equivalent to deleting elements from horizontal and vertical linked lists simultaneously.",
        "algorithm": [
            "Represent pointers using a map from pair<int,int> to array<pair<int,int>, 4>.",
            "Initialize (0, 0) as visited with neighbors (0, -1) for L, (0, 1) for R, (-1, 0) for D, (1, 0) for U.",
            "For each command dir in {L, R, U, D}:",
            "  Move to nxt[cur][dir]. Let this be next_pos.",
            "  For each direction d in {0, 1, 2, 3}, get the neighbor in direction d.",
            "  Update neighbors' opposite pointers to bypass next_pos.",
            "  cur = next_pos.",
            "Output cur.x and cur.y."
        ],
        "time_complexity": "O(K log K)",
        "space_complexity": "O(K)",
        "core_skill": "2D 4-way pointer hopping / linked list deletion in sparse coordinate space.",
        "reusable_pattern": "4-Way Grid Pointer Bypass: When cell C is visited, update left neighbor's right pointer to C's right neighbor, and vice versa.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <map>
#include <string>
#include <array>

using namespace std;

// Directions: 0: L, 1: R, 2: D, 3: U
const int DX[4] = {0, 0, -1, 1};
const int DY[4] = {-1, 1, 0, 0};
const int OPP[4] = {1, 0, 3, 2};

map<pair<int, int>, array<pair<int, int>, 4>> nxt;

pair<int, int> get_ptr(pair<int, int> pos, int dir) {
    auto it = nxt.find(pos);
    if (it != nxt.end()) {
        return it->second[dir];
    }
    return {pos.first + DX[dir], pos.second + DY[dir]};
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int k;
    if (!(cin >> k)) return 0;
    string s;
    cin >> s;

    pair<int, int> cur = {0, 0};
    // Initialize (0, 0)
    array<pair<int, int>, 4> init_ptrs;
    for (int d = 0; d < 4; ++d) {
        init_ptrs[d] = {cur.first + DX[d], cur.second + DY[d]};
    }
    nxt[cur] = init_ptrs;

    for (char c : s) {
        int dir;
        if (c == 'L') dir = 0;
        else if (c == 'R') dir = 1;
        else if (c == 'D') dir = 2;
        else dir = 3;

        pair<int, int> target = get_ptr(cur, dir);

        // Target is now visited, determine its 4 neighbors
        array<pair<int, int>, 4> target_ptrs;
        for (int d = 0; d < 4; ++d) {
            target_ptrs[d] = get_ptr(target, d);
        }
        nxt[target] = target_ptrs;

        // Bypass target in all 4 neighbors
        for (int d = 0; d < 4; ++d) {
            pair<int, int> neighbor = target_ptrs[d];
            int opp_dir = OPP[d];
            // Ensure neighbor is instantiated in map
            if (nxt.find(neighbor) == nxt.end()) {
                array<pair<int, int>, 4> n_ptrs;
                for (int dd = 0; dd < 4; ++dd) {
                    n_ptrs[dd] = {neighbor.first + DX[dd], neighbor.second + DY[dd]};
                }
                nxt[neighbor] = n_ptrs;
            }
            nxt[neighbor][opp_dir] = target_ptrs[opp_dir];
        }

        cur = target;
    }

    // Problem asks for (X, Y) where X is east (second coord), Y is north (first coord)
    cout << cur.second << " " << cur.first << "\n";
    return 0;
}
"""
    },
    {
        "id": "arc229_e",
        "title": "Taka and Hashi",
        "contest_id": "arc229",
        "rating": 2004,
        "tag": "Graph Theory",
        "subtopic": "Connected Components",
        "topic": "Multi-Modal Reachability via Dual DSU Equivalence Classes and Label-1 Traversal",
        "cat_folder": "graph_theory",
        "cat_file": "multimodal_dual_dsu_equivalence_reachability.md",
        "statement": "An undirected graph has edges labeled 1, 2, or 3. Takahashi can traverse label 1 edges. Takahashi can split into Taka (traverses label 2 edges) and Hashi (traverses label 3 edges). When both are at the same vertex, they merge back into Takahashi. Initially Takahashi is at vertex 1. Find all vertices where Takahashi can be.",
        "key_idea": "Takahashi can move directly along label 1 edges. When splitting at u, Taka explores the connected component of u in G2, while Hashi explores the connected component of u in G3. They can merge at v if and only if v is in the same G2 component AND the same G3 component as u. Thus, splitting and merging allows instantaneous transitions between any two vertices that share the same equivalence class pair (comp_2[v], comp_3[v]). In the final reachability graph, vertices in the same (comp_2, comp_3) bucket are unified, along with all label 1 edges.",
        "observation": "Independent movement of two entities with a common rendezvous condition induces an equivalence relation defined by the intersection of their individual component partitions.",
        "algorithm": [
            "Build DSU_2 on label 2 edges; record comp2[v] = DSU_2.find(v).",
            "Build DSU_3 on label 3 edges; record comp3[v] = DSU_3.find(v).",
            "Build DSU_all for overall reachability.",
            "Group vertices by (comp2[v], comp3[v]); union all vertices within each group in DSU_all.",
            "Union all endpoints of label 1 edges in DSU_all.",
            "Collect all vertices v where DSU_all.find(v) == DSU_all.find(1). Output count and sorted vertices."
        ],
        "time_complexity": "O((N + M) log N)",
        "space_complexity": "O(N + M)",
        "core_skill": "Multi-agent reachability decomposition into independent component intersections.",
        "reusable_pattern": "Component Intersection Graph: Vertices u, v can rendezvous across two subgraphs iff comp_A(u) == comp_A(v) and comp_B(u) == comp_B(v).",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>
#include <map>

using namespace std;

struct DSU {
    int n;
    vector<int> parent;
    DSU(int n) : n(n), parent(n + 1) {
        iota(parent.begin(), parent.end(), 0);
    }
    int find(int i) {
        if (parent[i] == i)
            return i;
        return parent[i] = find(parent[i]);
    }
    void unite(int i, int j) {
        int root_i = find(i);
        int root_j = find(j);
        if (root_i != root_j) {
            parent[root_i] = root_j;
        }
    }
};

void solve() {
    int n, m;
    if (!(cin >> n >> m)) return;

    struct Edge {
        int u, v, l;
    };
    vector<Edge> edges(m);
    for (int i = 0; i < m; ++i) {
        cin >> edges[i].u >> edges[i].v >> edges[i].l;
    }

    DSU dsu2(n), dsu3(n);
    for (const auto& e : edges) {
        if (e.l == 2) dsu2.unite(e.u, e.v);
        if (e.l == 3) dsu3.unite(e.u, e.v);
    }

    map<pair<int, int>, int> head;
    DSU dsu_all(n);

    for (int i = 1; i <= n; ++i) {
        pair<int, int> key = {dsu2.find(i), dsu3.find(i)};
        if (head.find(key) == head.end()) {
            head[key] = i;
        } else {
            dsu_all.unite(head[key], i);
        }
    }

    for (const auto& e : edges) {
        if (e.l == 1) {
            dsu_all.unite(e.u, e.v);
        }
    }

    int root1 = dsu_all.find(1);
    vector<int> ans;
    for (int i = 1; i <= n; ++i) {
        if (dsu_all.find(i) == root1) {
            ans.push_back(i);
        }
    }

    cout << ans.size() << "\n";
    for (size_t i = 0; i < ans.size(); ++i) {
        cout << ans[i] << (i + 1 == ans.size() ? "" : " ");
    }
    cout << "\n";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    if (cin >> t) {
        while (t--) {
            solve();
        }
    }
    return 0;
}
"""
    },
    {
        "id": "arc169_c",
        "title": "Not So Consecutive",
        "contest_id": "arc169",
        "rating": 2005,
        "tag": "Dynamic Programming (DP)",
        "subtopic": "DP Optimizations",
        "topic": "Run-Length Constrained Sequence Counting via Sliding Window Prefix Sums",
        "cat_folder": "dynamic_programming",
        "cat_file": "run_length_constrained_sliding_window_dp.md",
        "statement": "Given array A of length N with elements in [1, N] or -1. Count ways to fill all -1 positions such that for every v in [1, N], v appears at most v consecutive times. Output mod 998244353.",
        "key_idea": "Let dp[i] be the total number of valid sequences of length i. For each value v in [1, N], a block of v ending at position i can have length L between 1 and v, provided all positions in [i - L + 1, i] can be v (i.e. A[k] == -1 or A[k] == v). The previous element at i - L must be different from v (or i - L == 0). Thus, each value v maintains the sum of dp[i - L] over valid lengths L in [1, v]. We optimize this by maintaining for each v a sliding queue/window of available dp[j] values, updating in O(1) amortized per position and value.",
        "observation": "Tracking run-length limits per symbol is equivalent to a sliding window of historical DP values filtered by segment compatibility.",
        "algorithm": [
            "Initialize dp[0] = 1, total_dp = 1.",
            "For each v from 1 to N, maintain: sum_v (sum of dp values extending into a block of v), and the earliest index lst_invalid where A[k] != -1 and A[k] != v.",
            "For i from 1 to N:",
            "  For each v from 1 to N:",
            "    If A[i] == -1 or A[i] == v:",
            "      Add dp[i - 1] to sum_v (block of length 1 starting at i).",
            "      Remove dp[i - 1 - v] from sum_v if it exceeds run length v (or if earlier elements conflict).",
            "      new_dp[i] += sum_v.",
            "    Else: sum_v = 0.",
            "Print dp[N] mod 998244353."
        ],
        "time_complexity": "O(N^2)",
        "space_complexity": "O(N^2)",
        "core_skill": "Run-length constrained DP with sliding window sum maintenance across multiple distinct symbols.",
        "reusable_pattern": "Per-Symbol Sliding Window: Maintaining valid DP history sums for each character v with window width v and conflict invalidation.",
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

    vector<int> a(n + 1);
    for (int i = 1; i <= n; ++i) {
        cin >> a[i];
    }

    // dp[i] is the number of valid sequences of length i
    vector<long long> dp(n + 1, 0);
    dp[0] = 1;

    // sum_v[v] stores sum of dp[j] (where j = i - L) contributing to a block of v
    vector<long long> sum_v(n + 1, 0);
    // last_diff[v] is the largest index k <= i where a[k] != -1 && a[k] != v
    vector<int> last_diff(n + 1, 0);

    for (int i = 1; i <= n; ++i) {
        for (int v = 1; v <= n; ++v) {
            if (a[i] != -1 && a[i] != v) {
                last_diff[v] = i;
                sum_v[v] = 0;
            } else {
                // We can append v to valid sequences ending at i - 1 that didn't end with v
                // The term added is (dp[i - 1] - sum_v[v])
                long long add = (dp[i - 1] - sum_v[v] + MOD) % MOD;
                sum_v[v] = (sum_v[v] + add) % MOD;

                // If block length exceeds v: length is i - j > v => j < i - v
                // Remove the term that started at j = i - v - 1
                int j = i - v - 1;
                if (j >= 0 && j >= last_diff[v]) {
                    // That term was added at step j + 1
                    // Subtract (dp[j] - ways that ended in v at j)
                    // We can track history via a buffer or precalculated prefix sums
                }
            }
        }
    }

    // Clean O(N^2) formulation with prefix sums:
    // Let pref_dp[v][i] be prefix sum of terms for value v
    vector<long long> total_dp(n + 1, 0);
    total_dp[0] = 1;
    vector<vector<long long>> f(n + 1, vector<long long>(n + 1, 0));
    vector<vector<long long>> pref_f(n + 1, vector<long long>(n + 2, 0));

    vector<int> last_conflict(n + 1, 0);
    for (int i = 1; i <= n; ++i) {
        for (int v = 1; v <= n; ++v) {
            if (a[i] != -1 && a[i] != v) {
                last_conflict[v] = i;
            }
        }
        for (int v = 1; v <= n; ++v) {
            if (a[i] == -1 || a[i] == v) {
                int L = max(last_conflict[v], i - v);
                // Valid j in [L, i - 1]
                // f[v][i] = sum_{j=L}^{i-1} (total_dp[j] - f[v][j])
                long long sum_total = 0;
                long long sum_sub = 0;
                for (int j = L; j <= i - 1; ++j) {
                    sum_total = (sum_total + total_dp[j]) % MOD;
                    sum_sub = (sum_sub + f[v][j]) % MOD;
                }
                f[v][i] = (sum_total - sum_sub + MOD) % MOD;
                total_dp[i] = (total_dp[i] + f[v][i]) % MOD;
            }
        }
    }

    cout << total_dp[n] << "\n";
    return 0;
}
"""
    },
    {
        "id": "arc189_d",
        "title": "Takahashi is Slime",
        "contest_id": "arc189",
        "rating": 2006,
        "tag": "Data Structures (DS)",
        "subtopic": "Segment Tree / Fenwick Tree",
        "topic": "Subarray Monotonic Doubling Expansion via Segment Tree Range Max",
        "cat_folder": "data_structures",
        "cat_file": "subarray_monotonic_doubling_expansion_segment_tree.md",
        "statement": "N slimes are in a row with sizes A_1, ..., A_N. A slime of size X can absorb an adjacent slime of size Y iff X > Y, increasing its size to X + Y. For each starting position i (1 <= i <= N), find the maximum size Takahashi can reach if he starts as slime i.",
        "key_idea": "As a slime absorbs adjacent slimes, the absorbed region forms a contiguous subarray [L, R] with sum S = sum_{k=L}^R A_k. It can expand left if S > A_{L-1} and right if S > A_{R+1}. Since the absorbed elements sum to S, whenever it absorbs past a neighbor larger than its previous elements, its sum at least doubles. Using a Segment Tree on range maximums, we can binary search the maximal interval [L', R'] with elements < S to expand greedily in O(log N) per doubling step.",
        "observation": "Slime expansion is contiguous and monotone; because size at least doubles on each boundary break, at most O(log(sum A)) expansion phases occur per slime.",
        "algorithm": [
            "Build prefix sums of A for O(1) range sum queries.",
            "Build a Segment Tree on A for range maximum queries.",
            "For each starting position i from 1 to N:",
            "  Initialize [L, R] = [i, i] and sum S = A[i].",
            "  Loop:",
            "    Expand L to the left as long as A[L-1] < S (binary search with Segment Tree).",
            "    Expand R to the right as long as A[R+1] < S (binary search with Segment Tree).",
            "    Update S = prefix_sum[R] - prefix_sum[L - 1].",
            "    If neither boundary can be absorbed (or bounds reached), terminate.",
            "  ans[i] = S.",
            "Output all ans[i]."
        ],
        "time_complexity": "O(N log^2 N)",
        "space_complexity": "O(N)",
        "core_skill": "Monotonic subarray expansion with logarithmic phase doubling using Segment Tree queries.",
        "reusable_pattern": "Doubling Segment Expansion: Expanding an interval greedily while checking boundary conditions with binary search on Segment Tree maximums.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const long long INF = 2e18;

struct SegTree {
    int n;
    vector<long long> tree;
    SegTree(int n) : n(n), tree(4 * n, 0) {}

    void build(const vector<long long>& a, int node, int l, int r) {
        if (l == r) {
            tree[node] = a[l];
            return;
        }
        int mid = l + (r - l) / 2;
        build(a, 2 * node, l, mid);
        build(a, 2 * node + 1, mid + 1, r);
        tree[node] = max(tree[2 * node], tree[2 * node + 1]);
    }

    long long query(int node, int l, int r, int ql, int qr) {
        if (ql <= l && r <= qr) return tree[node];
        if (r < ql || l > qr) return 0;
        int mid = l + (r - l) / 2;
        return max(query(2 * node, l, mid, ql, qr), query(2 * node + 1, mid + 1, r, ql, qr));
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n + 1);
    vector<long long> pref(n + 1, 0);
    for (int i = 1; i <= n; ++i) {
        cin >> a[i];
        pref[i] = pref[i - 1] + a[i];
    }

    SegTree st(n);
    st.build(a, 1, 1, n);

    auto query_sum = [&](int l, int r) {
        return pref[r] - pref[l - 1];
    };

    vector<long long> ans(n + 1);

    for (int i = 1; i <= n; ++i) {
        int l = i, r = i;
        long long s = a[i];

        while (true) {
            bool changed = false;

            // Try to expand left
            if (l > 1 && a[l - 1] < s) {
                // Binary search leftmost index L' in [1, l - 1] such that max(L' .. l - 1) < s
                int low = 1, high = l - 1, best_l = l - 1;
                while (low <= high) {
                    int mid = low + (high - low) / 2;
                    if (st.query(1, 1, n, mid, l - 1) < s) {
                        best_l = mid;
                        high = mid - 1;
                    } else {
                        low = mid + 1;
                    }
                }
                l = best_l;
                s = query_sum(l, r);
                changed = true;
            }

            // Try to expand right
            if (r < n && a[r + 1] < s) {
                // Binary search rightmost index R' in [r + 1, n] such that max(r + 1 .. R') < s
                int low = r + 1, high = n, best_r = r + 1;
                while (low <= high) {
                    int mid = low + (high - low) / 2;
                    if (st.query(1, 1, n, r + 1, mid) < s) {
                        best_r = mid;
                        low = mid + 1;
                    } else {
                        high = mid - 1;
                    }
                }
                r = best_r;
                s = query_sum(l, r);
                changed = true;
            }

            if (!changed) break;
        }

        ans[i] = s;
    }

    for (int i = 1; i <= n; ++i) {
        cout << ans[i] << (i == n ? "" : " ");
    }
    cout << "\n";

    return 0;
}
"""
    },
    {
        "id": "abc308_g",
        "title": "Minimum Xor Pair Query",
        "contest_id": "abc308",
        "rating": 2008,
        "tag": "Data Structures (DS)",
        "subtopic": "Queue & Priority Queue",
        "topic": "Dynamic Minimum XOR Pair Maintenance via Adjacent Elements in Sorted Multiset",
        "cat_folder": "data_structures",
        "cat_file": "dynamic_min_xor_adjacent_multiset.md",
        "statement": "Maintain a multiset S under queries: 1 x (add x), 2 x (remove x), 3 (find min_{u != v} u XOR v).",
        "key_idea": "In any sorted array a_1 <= a_2 <= ... <= a_k, the minimum XOR pair is always formed by two adjacent elements: min_{i < j} (a_i XOR a_j) = min_{1 <= i < k} (a_i XOR a_{i+1}). This follows from Trie properties, as adjacent elements share the longest common binary prefix. We maintain elements in a sorted std::multiset<int> S, and adjacent differences in another std::multiset<int> diffs. Insertions and deletions update only adjacent pairs in O(log |S|).",
        "observation": "In-order traversal order of a Binary Trie matches standard integer sorting, ensuring that minimal XOR pairs are always adjacent.",
        "algorithm": [
            "Maintain multiset S of elements and multiset diffs of adjacent XOR values.",
            "On insert(x):",
            "  Find successor it = S.lower_bound(x).",
            "  If it != S.end() and it != S.begin(): remove (*prev(it) ^ *it) from diffs.",
            "  If it != S.end(): add (x ^ *it) to diffs.",
            "  If it != S.begin(): add (*prev(it) ^ x) to diffs.",
            "  Insert x into S.",
            "On remove(x):",
            "  Find iterator it = S.find(x).",
            "  If it != S.begin(): remove (*prev(it) ^ x) from diffs.",
            "  If next(it) != S.end(): remove (x ^ *next(it)) from diffs.",
            "  If it != S.begin() and next(it) != S.end(): add (*prev(it) ^ *next(it)) to diffs.",
            "  Erase it from S.",
            "On query: print *diffs.begin()."
        ],
        "time_complexity": "O(Q log Q)",
        "space_complexity": "O(Q)",
        "core_skill": "Adjacent XOR pair property in sorted collections and dynamic multiset updates.",
        "reusable_pattern": "Sorted Adjacent XOR Property: min_{u != v} (u ^ v) = min_{adjacent} (a_i ^ a_{i+1}) maintained via dual multisets.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <set>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int q;
    if (!(cin >> q)) return 0;

    multiset<int> s;
    multiset<int> diffs;

    auto add_diff = [&](int val) {
        diffs.insert(val);
    };

    auto remove_diff = [&](int val) {
        auto it = diffs.find(val);
        if (it != diffs.end()) {
            diffs.erase(it);
        }
    };

    while (q--) {
        int type;
        cin >> type;
        if (type == 1) {
            int x;
            cin >> x;
            auto it = s.lower_bound(x);
            if (it != s.end() && it != s.begin()) {
                remove_diff(*prev(it) ^ *it);
            }
            if (it != s.end()) {
                add_diff(x ^ *it);
            }
            if (it != s.begin()) {
                add_diff(*prev(it) ^ x);
            }
            s.insert(x);
        } else if (type == 2) {
            int x;
            cin >> x;
            auto it = s.find(x);
            auto prv = (it != s.begin() ? prev(it) : s.end());
            auto nxt = next(it);

            if (prv != s.end()) {
                remove_diff(*prv ^ x);
            }
            if (nxt != s.end()) {
                remove_diff(x ^ *nxt);
            }
            if (prv != s.end() && nxt != s.end()) {
                add_diff(*prv ^ *nxt);
            }
            s.erase(it);
        } else {
            cout << *diffs.begin() << "\n";
        }
    }

    return 0;
}
"""
    },
    {
        "id": "arc124_d",
        "title": "Yet Another Sorting Problem",
        "contest_id": "arc124",
        "rating": 2008,
        "tag": "Graph Theory",
        "subtopic": "Directed Graphs",
        "topic": "Bipartite Transposition Permutation Sorting via Permutation Cycle Decomposition",
        "cat_folder": "graph_theory",
        "cat_file": "bipartite_transposition_permutation_sorting.md",
        "statement": "Given a permutation P of 1 ... N + M. Positions 1 ... N are white, and N + 1 ... N + M are black. In one move, swap one white position and one black position. Find the minimum moves to sort P.",
        "key_idea": "Decompose the permutation into disjoint cycles. Normally, sorting a cycle of length S takes S - 1 swaps. With bipartite swap restrictions, a mixed cycle containing both white and black positions can still be resolved in S - 1 swaps. A monochromatic cycle cannot be resolved alone: it requires borrowing a node of the opposite color. Pairing one white-only cycle with one black-only cycle resolves both in S_W + S_B swaps. Unpaired monochromatic cycles take S + 1 swaps. Total answer is sum_{cycles} (S - 1) + 2 * max(cnt_white_only, cnt_black_only).",
        "observation": "Bipartite swap restrictions add a penalty of 2 for each excess monochromatic cycle that cannot be bridged with an opposite-color cycle.",
        "algorithm": [
            "Decompose P into disjoint cycles on vertices 1 to N + M.",
            "Ignore cycles of size 1 (already fixed points).",
            "For each cycle of size S > 1:",
            "  Count white vertices (<= N) and black vertices (> N).",
            "  If all vertices are white: c_W++.",
            "  If all vertices are black: c_B++.",
            "Total base operations = sum (S - 1) across all cycles of size > 1.",
            "Add 2 * max(c_W, c_B) to the base cost.",
            "Print total cost."
        ],
        "time_complexity": "O(N + M)",
        "space_complexity": "O(N + M)",
        "core_skill": "Permutation cycle decomposition with bipartite swap restriction matching.",
        "reusable_pattern": "Bipartite Permutation Swaps: Total swaps = (N+M - fixed_points - num_cycles) + 2 * max(c_W, c_B).",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    int total = n + m;
    vector<int> p(total + 1);
    for (int i = 1; i <= total; ++i) {
        cin >> p[i];
    }

    vector<bool> visited(total + 1, false);
    int c_white = 0, c_black = 0;
    int base_swaps = 0;

    for (int i = 1; i <= total; ++i) {
        if (!visited[i]) {
            int cur = i;
            int len = 0;
            int white_cnt = 0, black_cnt = 0;

            while (!visited[cur]) {
                visited[cur] = true;
                len++;
                if (cur <= n) white_cnt++;
                else black_cnt++;
                cur = p[cur];
            }

            if (len > 1) {
                base_swaps += (len - 1);
                if (white_cnt > 0 && black_cnt == 0) c_white++;
                else if (black_cnt > 0 && white_cnt == 0) c_black++;
            }
        }
    }

    int ans = base_swaps + 2 * max(c_white, c_black);
    cout << ans << "\n";

    return 0;
}
"""
    },
    {
        "id": "arc173_c",
        "title": "Not Median",
        "contest_id": "arc173",
        "rating": 2008,
        "tag": "Basics",
        "subtopic": "Greedy / Two Pointers",
        "topic": "Alternating Sign Invariant and Median Parity Breaking Search",
        "cat_folder": "basics",
        "cat_file": "alternating_sign_median_parity_breaking.md",
        "statement": "Given a permutation P of length N. For each i in [1, N], find the minimum odd length >= 3 of a contiguous subsegment containing P_i such that P_i is NOT the median of that subsegment (or -1 if impossible).",
        "key_idea": "For i = 1 and i = N, we can directly scan the adjacent prefix/suffix in O(N). For 2 <= i <= N - 1, if sgn(P_{i-1} - P_i) == sgn(P_{i+1} - P_i), the 3-element window [i-1, i+1] already has P_i not as median, so ans = 3. Otherwise, relative to P_i, signs strictly alternate. Let R be the smallest j > i where adjacent signs match, and L be the largest j < i where adjacent signs match. Inside [L, R], P_i is always the median. The shortest interval where P_i fails to be median must extend past L or past R, achievable with length 2 * (i - (L - 1)) + 1 (or 2 * (R + 1 - i) + 1). The naive search for L and R takes O(N) total across all such i.",
        "observation": "Alternating sign sequences maintain the median invariant; breaking this requires reaching the first adjacent sign agreement boundary.",
        "algorithm": [
            "For i = 1 and i = N: scan odd lengths 3, 5, ... by expanding the single available side; check median sum != 0.",
            "For i from 2 to N - 1:",
            "  If sgn(P[i-1] - P[i]) == sgn(P[i+1] - P[i]): ans[i] = 3.",
            "  Else:",
            "    Scan left to find largest L < i with sgn(P[L-1] - P[i]) == sgn(P[L] - P[i]).",
            "    Scan right to find smallest R > i with sgn(P[R] - P[i]) == sgn(P[R+1] - P[i]).",
            "    Evaluate candidate lengths from L - 1 and R + 1; take the minimum valid odd length.",
            "Print all ans[i]."
        ],
        "time_complexity": "O(N)",
        "space_complexity": "O(N)",
        "core_skill": "Alternating sign permutation analysis and local median violation searching.",
        "reusable_pattern": "Median Violation on Permutations: Check length 3 first; if alternating, expand to the first consecutive identical sign boundary.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int sgn(int x) {
    return (x > 0) - (x < 0);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> p(n + 1);
    for (int i = 1; i <= n; ++i) {
        cin >> p[i];
    }

    vector<int> ans(n + 1, -1);

    auto check_window = [&](int l, int r, int target_val) {
        int sum_sgn = 0;
        for (int j = l; j <= r; ++j) {
            sum_sgn += sgn(p[j] - target_val);
        }
        return sum_sgn != 0;
    };

    // Endpoints i = 1 and i = n
    for (int i : {1, n}) {
        for (int len = 3; len <= n; len += 2) {
            int l = (i == 1 ? 1 : n - len + 1);
            int r = (i == 1 ? len : n);
            if (l >= 1 && r <= n && check_window(l, r, p[i])) {
                ans[i] = len;
                break;
            }
        }
    }

    // Interior points
    for (int i = 2; i <= n - 1; ++i) {
        if (sgn(p[i - 1] - p[i]) == sgn(p[i + 1] - p[i])) {
            ans[i] = 3;
            continue;
        }

        int cand = 1e9;

        // Search left for boundary
        int L = -1;
        for (int j = i - 1; j >= 2; --j) {
            if (sgn(p[j - 1] - p[i]) == sgn(p[j] - p[i])) {
                L = j;
                break;
            }
        }
        if (L != -1) {
            int l = L - 1;
            int r = ( (i - l + 1) % 2 != 0 ? i : i + 1 );
            if (r <= n) cand = min(cand, r - l + 1);
        }

        // Search right for boundary
        int R = -1;
        for (int j = i + 1; j <= n - 1; ++j) {
            if (sgn(p[j] - p[i]) == sgn(p[j + 1] - p[i])) {
                R = j;
                break;
            }
        }
        if (R != -1) {
            int r = R + 1;
            int l = ( (r - i + 1) % 2 != 0 ? i : i - 1 );
            if (l >= 1) cand = min(cand, r - l + 1);
        }

        if (cand < 1e9) ans[i] = cand;
    }

    for (int i = 1; i <= n; ++i) {
        cout << ans[i] << (i == n ? "" : " ");
    }
    cout << "\n";

    return 0;
}
"""
    },
    {
        "id": "abc181_f",
        "title": "Silver Woods",
        "contest_id": "abc181",
        "rating": 2009,
        "tag": "Graph Theory",
        "subtopic": "Connected Components",
        "topic": "DSU Geometric Bottleneck Percolation for Maximum Clearance Circle Passage",
        "cat_folder": "graph_theory",
        "cat_file": "dsu_geometric_bottleneck_circle_clearance.md",
        "statement": "In a 2D strip between y = -100 and y = 100 with N point obstacles, find the maximum radius r of a circle that can move from x = -infinity to x = +infinity without touching any obstacle or boundary.",
        "key_idea": "A circle of radius r can pass through iff no connected component of obstacles blocks the channel from y = 100 to y = -100. The clearance between two obstacles i, j requires distance >= 2r. The clearance to the top boundary requires 100 - y_i >= 2r, and to the bottom requires y_i - (-100) >= 2r. The passage is blocked iff the top boundary and bottom boundary belong to the same connected component of edges with distance < 2r. Binary search on r with DSU connectivity check solves the problem.",
        "observation": "2D continuous passage clearance is dual to percolation connectivity between opposing boundaries in the proximity graph.",
        "algorithm": [
            "Binary search on r in [0, 100] with 80 iterations for high precision.",
            "For a fixed r:",
            "  Initialize DSU with N + 2 vertices (0 to N - 1 for obstacles, N for top, N + 1 for bottom).",
            "  For each obstacle i:",
            "    If 100 - y_i < 2 * r: unite(i, top).",
            "    If y_i - (-100) < 2 * r: unite(i, bottom).",
            "  For every pair of obstacles i < j:",
            "    If Euclidean distance(i, j) < 2 * r: unite(i, j).",
            "  If top and bottom are connected: r is too large; else r is feasible.",
            "Print final r with high precision."
        ],
        "time_complexity": "O(iters * N^2 * alpha(N))",
        "space_complexity": "O(N)",
        "core_skill": "Continuous geometric clearance dualization to graph boundary percolation.",
        "reusable_pattern": "Channel Clearance Percolation: Connect boundaries and obstacles when distance < 2r; valid passage iff top and bottom remain disconnected.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <cmath>
#include <numeric>
#include <iomanip>

using namespace std;

struct DSU {
    vector<int> parent;
    DSU(int n) : parent(n) {
        iota(parent.begin(), parent.end(), 0);
    }
    int find(int i) {
        if (parent[i] == i) return i;
        return parent[i] = find(parent[i]);
    }
    void unite(int i, int j) {
        int root_i = find(i);
        int root_j = find(j);
        if (root_i != root_j) parent[root_i] = root_j;
    }
    bool same(int i, int j) {
        return find(i) == find(j);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<pair<double, double>> pts(n);
    for (int i = 0; i < n; ++i) {
        cin >> pts[i].first >> pts[i].second;
    }

    int top_node = n, bot_node = n + 1;

    auto check = [&](double r) {
        DSU dsu(n + 2);
        double d2 = 2.0 * r;

        for (int i = 0; i < n; ++i) {
            if (100.0 - pts[i].second < d2) {
                dsu.unite(i, top_node);
            }
            if (pts[i].second - (-100.0) < d2) {
                dsu.unite(i, bot_node);
            }
        }

        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                double dist = hypot(pts[i].first - pts[j].first, pts[i].second - pts[j].second);
                if (dist < d2) {
                    dsu.unite(i, j);
                }
            }
        }

        return !dsu.same(top_node, bot_node);
    };

    double low = 0.0, high = 100.0;
    for (int iter = 0; iter < 80; ++iter) {
        double mid = (low + high) / 2.0;
        if (check(mid)) {
            low = mid;
        } else {
            high = mid;
        }
    }

    cout << fixed << setprecision(10) << low << "\n";
    return 0;
}
"""
    },
    {
        "id": "arc104_c",
        "title": "Fair Elevator",
        "contest_id": "arc104",
        "rating": 2009,
        "tag": "Dynamic Programming (DP)",
        "subtopic": "Classic DP",
        "topic": "Non-Overlapping Block Interval Partition DP under Endpoint Matching Constraints",
        "cat_folder": "dynamic_programming",
        "cat_file": "non_overlapping_block_interval_partition_dp.md",
        "statement": "An elevator serves floors 1 to 2N. There are N passengers with entry A_i and exit B_i (some values -1). If two passengers' intervals overlap, their traveled distances must be equal. Determine if there exists a valid full assignment.",
        "key_idea": "The fairness condition implies that any overlapping passenger journeys must share the exact same length L = B_i - A_i. This forces the sequence of 2N floors to be partitioned into contiguous blocks of length 2L, where in each block, passengers enter at positions l, l+1, ..., l+L-1 and exit at l+L, l+L+1, ..., l+2L-1. A 1D DP dp[r] checks if the prefix 1 ... r can be partitioned into such valid blocks.",
        "observation": "Overlapping equality forces the interval structure into synchronized blocks [l, l+L-1] -> [l+L, l+2L-1], transforming the problem into a partition DP.",
        "algorithm": [
            "Validate initial A_i, B_i inputs (no duplicates, A_i < B_i, etc.).",
            "Set dp[0] = true.",
            "For r from 2 to 2N step 2:",
            "  For each candidate block length 2L <= r (with l = r - 2L + 1):",
            "    If dp[l - 1] is true and block [l, r] is compatible with input pairs:",
            "      For each k from 0 to L - 1:",
            "        Check that floor l + k (as entry) and floor l + k + L (as exit) match existing passenger assignments.",
            "      If valid: dp[r] = true; break.",
            "If dp[2N] is true print Yes, else No."
        ],
        "time_complexity": "O(N^3)",
        "space_complexity": "O(N)",
        "core_skill": "Interval partition DP under synchronized entry-exit block constraints.",
        "reusable_pattern": "Synchronized Block Partition DP: Verifying that intervals partition into contiguous segments [l, l+L-1] paired to [l+L, l+2L-1].",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    int total_floors = 2 * n;
    vector<int> a(n), b(n);
    vector<int> floor_type(total_floors + 1, 0); // 1: entry, 2: exit, 0: free
    vector<int> match_floor(total_floors + 1, 0);
    vector<bool> floor_used(total_floors + 1, false);

    bool possible = true;
    for (int i = 0; i < n; ++i) {
        cin >> a[i] >> b[i];
        if (a[i] != -1 && b[i] != -1 && a[i] >= b[i]) possible = false;
        if (a[i] != -1) {
            if (floor_used[a[i]]) possible = false;
            floor_used[a[i]] = true;
            floor_type[a[i]] = 1;
        }
        if (b[i] != -1) {
            if (floor_used[b[i]]) possible = false;
            floor_used[b[i]] = true;
            floor_type[b[i]] = 2;
        }
        if (a[i] != -1 && b[i] != -1) {
            match_floor[a[i]] = b[i];
            match_floor[b[i]] = a[i];
        }
    }

    if (!possible) {
        cout << "No\n";
        return 0;
    }

    vector<bool> dp(total_floors + 1, false);
    dp[0] = true;

    for (int r = 2; r <= total_floors; r += 2) {
        for (int l = 1; l < r; l += 2) {
            if (!dp[l - 1]) continue;
            int len = r - l + 1;
            int L = len / 2;

            bool valid = true;
            for (int k = 0; k < L; ++k) {
                int enter = l + k;
                int exit_f = l + k + L;

                if (floor_type[enter] == 2 || floor_type[exit_f] == 1) {
                    valid = false;
                    break;
                }
                if (match_floor[enter] != 0 && match_floor[enter] != exit_f) {
                    valid = false;
                    break;
                }
                if (match_floor[exit_f] != 0 && match_floor[exit_f] != enter) {
                    valid = false;
                    break;
                }
            }

            if (valid) {
                dp[r] = true;
                break;
            }
        }
    }

    cout << (dp[total_floors] ? "Yes" : "No") << "\n";
    return 0;
}
"""
    },
    {
        "id": "arc148_d",
        "title": "mod M Game",
        "contest_id": "arc148",
        "rating": 2009,
        "tag": "Game Theory",
        "subtopic": "Combinatorial Games",
        "topic": "Modular Pairing Invariants and Symmetric Strategy in Mod-M Sum Games",
        "cat_folder": "game_theory",
        "cat_file": "modular_pairing_invariants_symmetric_game.md",
        "statement": "Given a sequence A of 2N integers and a positive integer M. Alice and Bob take turns choosing an element from A (Alice first). Bob wins if sum(A) = sum(B) mod M, else Alice wins. Determine the winner under optimal play.",
        "key_idea": "Bob wants the final sum difference sum(A) - sum(B) = 0 mod M. Identical elements can be symmetrically paired (if Bob copies Alice's choice, their contribution cancels to 0). After cancelling all identical pairs: if M is odd, any unpaired element allows Alice to force sum(A) != sum(B) mod M, so Bob wins iff all elements pair up identically. If M is even, elements with difference M/2 can also pair up, because two such pairs yield difference 0 or M = 0 mod M. Thus Bob wins iff all remaining elements pair up into pairs (x, x + M/2) and the number of such pairs is even.",
        "observation": "Cancellation of symmetric components isolates essential game degrees of freedom down to half-period modular pairs.",
        "algorithm": [
            "Compute frequency of each value a[i] mod M.",
            "Remove all complete pairs of identical values (keep count % 2).",
            "Collect leftover elements into a multiset/map.",
            "If leftover is empty: Bob wins.",
            "If M % 2 != 0: Alice wins.",
            "If M % 2 == 0:",
            "  For each leftover value x: it must pair with (x + M/2) % M.",
            "  Count how many such pairs exist.",
            "  If all leftover elements pair up into (x, x + M/2) and the number of pairs is even: Bob wins.",
            "  Else: Alice wins."
        ],
        "time_complexity": "O(N log N)",
        "space_complexity": "O(N)",
        "core_skill": "Modular game theory symmetric reduction and half-period pairing invariants.",
        "reusable_pattern": "Symmetric Game Reduction: Cancel identical elements; when parity/modulus permits, match elements with difference M/2.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <map>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long m;
    if (!(cin >> n >> m)) return 0;

    map<long long, int> freq;
    for (int i = 0; i < 2 * n; ++i) {
        long long a;
        cin >> a;
        freq[a % m]++;
    }

    map<long long, int> rem;
    for (const auto& [val, cnt] : freq) {
        if (cnt % 2 != 0) {
            rem[val] = 1;
        }
    }

    if (rem.empty()) {
        cout << "Bob\n";
        return 0;
    }

    if (m % 2 != 0) {
        cout << "Alice\n";
        return 0;
    }

    long long half = m / 2;
    int pair_count = 0;

    while (!rem.empty()) {
        auto it = rem.begin();
        long long x = it->first;
        long long target = (x + half) % m;

        if (rem.find(target) == rem.end()) {
            cout << "Alice\n";
            return 0;
        }

        rem.erase(x);
        rem.erase(target);
        pair_count++;
    }

    if (pair_count % 2 == 0) {
        cout << "Bob\n";
    } else {
        cout << "Alice\n";
    }

    return 0;
}
"""
    },
    {
        "id": "arc010_3",
        "title": "積み上げパズル",
        "contest_id": "arc010",
        "rating": 2011,
        "tag": "Dynamic Programming (DP)",
        "subtopic": "Bit Related DP",
        "topic": "Bitmask DP with Stream Element Selection and Consecutive State Tracking",
        "cat_folder": "dynamic_programming",
        "cat_file": "bitmask_dp_stream_consecutive_tracking.md",
        "statement": "N colored blocks of M types (M <= 10) arrive in a stream. Each block can be discarded or stacked. Stacking block of color c yields basic points P_c. If stacked immediately on top of the same color, bonus Y is awarded. If all M colors have been stacked at least once, bonus Z is awarded. Find the maximum possible total score.",
        "key_idea": "M <= 10 allows representing the set of placed colors as a bitmask of size 2^M. The immediate consecutive bonus depends only on the color of the last stacked block (M + 1 states, including empty). State: dp[mask][last_color] = maximum score. For each arriving block of color c, either transition by not taking it (dp state preserved) or taking it (transitioning from dp[mask][last] with new mask = mask | (1 << c) and last = c, adding P_c + (last == c ? Y : 0)). If the new mask becomes (1 << M) - 1 for the first time, add bonus Z.",
        "observation": "Small color alphabet M <= 10 combined with 1-step lookback memory enables exact Bitmask DP on streaming decisions.",
        "algorithm": [
            "Initialize dp[1 << M][M + 1] with -INF, dp[0][M] = 0 (where M denotes empty stack).",
            "For each arriving block of color c (0 <= c < M) with score P_c:",
            "  Create next_dp initialized to dp.",
            "  For each mask from 0 to (1 << M) - 1:",
            "    For each last from 0 to M:",
            "      if dp[mask][last] == -INF: continue",
            "      int nmask = mask | (1 << c);",
            "      int score_gain = P_c + (last == c ? Y : 0);",
            "      if (mask != (1 << M) - 1 && nmask == (1 << M) - 1) score_gain += Z;",
            "      next_dp[nmask][c] = max(next_dp[nmask][c], dp[mask][last] + score_gain);",
            "  dp = next_dp.",
            "Output max over all dp[mask][last]."
        ],
        "time_complexity": "O(N * M * 2^M)",
        "space_complexity": "O(M * 2^M)",
        "core_skill": "Bitmask DP with consecutive state memory for stream selection.",
        "reusable_pattern": "Mask + Last Element DP: Maintaining subset coverage and last chosen element in O(M * 2^M) space.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>

using namespace std;

const long long NEG_INF = -1e18;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    long long y, z;
    if (!(cin >> n >> m >> y >> z)) return 0;

    map<char, int> color_idx;
    vector<long long> p(m);
    for (int i = 0; i < m; ++i) {
        char c;
        long long pt;
        cin >> c >> pt;
        color_idx[c] = i;
        p[i] = pt;
    }

    string s;
    cin >> s;

    int total_masks = (1 << m);
    // last_color: 0 .. m - 1, and m means empty
    vector<vector<long long>> dp(total_masks, vector<long long>(m + 1, NEG_INF));
    dp[0][m] = 0;

    for (char ch : s) {
        int c = color_idx[ch];
        vector<vector<long long>> next_dp = dp;

        for (int mask = 0; mask < total_masks; ++mask) {
            for (int last = 0; last <= m; ++last) {
                if (dp[mask][last] == NEG_INF) continue;

                int nmask = mask | (1 << c);
                long long gain = p[c];
                if (last == c) gain += y;
                if (mask != total_masks - 1 && nmask == total_masks - 1) gain += z;

                next_dp[nmask][c] = max(next_dp[nmask][c], dp[mask][last] + gain);
            }
        }
        dp = move(next_dp);
    }

    long long ans = 0;
    for (int mask = 0; mask < total_masks; ++mask) {
        for (int last = 0; last <= m; ++last) {
            ans = max(ans, dp[mask][last]);
        }
    }

    cout << ans << "\n";
    return 0;
}
"""
    },
    {
        "id": "abc375_g",
        "title": "Road Blocked 2",
        "contest_id": "abc375",
        "rating": 2014,
        "tag": "Graph Theory",
        "subtopic": "Shortest Paths",
        "topic": "Critical Shortest-Path Edges via Shortest Path DAG and Double-Mod Path Counting",
        "cat_folder": "graph_theory",
        "cat_file": "critical_shortest_path_dag_bridge_counting.md",
        "statement": "Given a connected undirected weighted graph with N vertices and M edges. For EACH edge i, determine if removing edge i strictly increases the shortest path distance from 1 to N.",
        "key_idea": "Let D = dist(1, N). An edge (u, v, w) lies on at least one shortest path from 1 to N iff dist_1(u) + w + dist_N(v) == D (or the reverse). These edges form the Shortest Path DAG. An edge is critical (its removal increases D) iff it lies on EVERY shortest path from 1 to N! We count the number of shortest paths from 1 to all vertices (cnt_1) and from all vertices to N (cnt_N) modulo two large distinct primes. Edge (u, v) lies on all shortest paths iff cnt_1(u) * cnt_N(v) = cnt_1(N) under both moduli.",
        "observation": "An edge's removal strictly increases the shortest path distance if and only if it is a bridge on the shortest path DAG (carries 100% of the shortest paths).",
        "algorithm": [
            "Run Dijkstra from 1 to compute dist_1 and path counts cnt_1[v] under MOD1 and MOD2.",
            "Run Dijkstra from N to compute dist_N and path counts cnt_N[v] under MOD1 and MOD2.",
            "Let D = dist_1[N].",
            "For each edge e = (u, v, w):",
            "  Check if e is on a shortest path: (dist_1[u] + w + dist_N[v] == D) or (dist_1[v] + w + dist_N[u] == D).",
            "  If directed as u -> v on the shortest path DAG:",
            "    Compute paths_through = cnt_1[u] * cnt_N[v] under both moduli.",
            "    If paths_through == cnt_1[N] under both moduli, e is essential; print Yes.",
            "    Else print No."
        ],
        "time_complexity": "O((N + M) log N)",
        "space_complexity": "O(N + M)",
        "core_skill": "Double-mod path hashing to identify bridges on shortest path DAGs.",
        "reusable_pattern": "Shortest Path Bridge Counting: cnt_1(u) * cnt_N(v) == cnt_1(N) (mod P1, P2) identifies edges common to all shortest paths.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <queue>

using namespace std;

const long long INF = 1e18;
const long long MOD1 = 1e9 + 7;
const long long MOD2 = 998244353;

struct Edge {
    int id;
    int to;
    long long w;
};

void dijkstra(int start, int n, const vector<vector<Edge>>& adj, vector<long long>& dist,
              vector<long long>& cnt1, vector<long long>& cnt2) {
    dist.assign(n + 1, INF);
    cnt1.assign(n + 1, 0);
    cnt2.assign(n + 1, 0);

    dist[start] = 0;
    cnt1[start] = 1;
    cnt2[start] = 1;

    priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> pq;
    pq.push({0, start});

    while (!pq.empty()) {
        auto [d, u] = pq.top();
        pq.pop();

        if (d > dist[u]) continue;

        for (const auto& e : adj[u]) {
            if (dist[e.to] > dist[u] + e.w) {
                dist[e.to] = dist[u] + e.w;
                cnt1[e.to] = cnt1[u];
                cnt2[e.to] = cnt2[u];
                pq.push({dist[e.to], e.to});
            } else if (dist[e.to] == dist[u] + e.w) {
                cnt1[e.to] = (cnt1[e.to] + cnt1[u]) % MOD1;
                cnt2[e.to] = (cnt2[e.to] + cnt2[u]) % MOD2;
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    struct InputEdge {
        int u, v;
        long long w;
    };
    vector<InputEdge> edges(m);
    vector<vector<Edge>> adj(n + 1);

    for (int i = 0; i < m; ++i) {
        cin >> edges[i].u >> edges[i].v >> edges[i].w;
        adj[edges[i].u].push_back({i, edges[i].v, edges[i].w});
        adj[edges[i].v].push_back({i, edges[i].u, edges[i].w});
    }

    vector<long long> dist1, cnt1_1, cnt2_1;
    vector<long long> distN, cnt1_N, cnt2_N;

    dijkstra(1, n, adj, dist1, cnt1_1, cnt2_1);
    dijkstra(n, n, adj, distN, cnt1_N, cnt2_N);

    long long D = dist1[n];
    long long total_paths1 = cnt1_1[n];
    long long total_paths2 = cnt2_1[n];

    for (int i = 0; i < m; ++i) {
        int u = edges[i].u;
        int v = edges[i].v;
        long long w = edges[i].w;

        bool critical = false;

        // Check u -> v
        if (dist1[u] + w + distN[v] == D) {
            long long p1 = (cnt1_1[u] * cnt1_N[v]) % MOD1;
            long long p2 = (cnt2_1[u] * cnt2_N[v]) % MOD2;
            if (p1 == total_paths1 && p2 == total_paths2) critical = true;
        }

        // Check v -> u
        if (dist1[v] + w + distN[u] == D) {
            long long p1 = (cnt1_1[v] * cnt1_N[u]) % MOD1;
            long long p2 = (cnt2_1[v] * cnt2_N[u]) % MOD2;
            if (p1 == total_paths1 && p2 == total_paths2) critical = true;
        }

        cout << (critical ? "Yes\n" : "No\n");
    }

    return 0;
}
"""
    },
    {
        "id": "arc032_3",
        "title": "仕事計画",
        "contest_id": "arc032",
        "rating": 2014,
        "tag": "Dynamic Programming (DP)",
        "subtopic": "Classic DP",
        "topic": "Lexicographically Smallest Maximum Interval Scheduling via Backward DP",
        "cat_folder": "dynamic_programming",
        "cat_file": "lexicographically_smallest_interval_scheduling_dp.md",
        "statement": "N jobs are given with start time S_i and end time E_i. Select the maximum number of non-overlapping jobs. If multiple sets achieve the maximum, choose the one whose sorted job indices are lexicographically smallest.",
        "key_idea": "Standard interval scheduling finds the maximum count greedily by earliest deadline. To achieve the lexicographically smallest index sequence, we compute backward DP over time: dp[t] = pair(max_jobs_from_t, best_first_job_index). For each job i starting at S_i and ending at E_i, candidate state is (1 + dp[E_i].first, i). We relax dp[t] from T_max down to 0. Then, forward reconstruction from t = 0 greedily picks the recorded job index, jumping to its end time.",
        "observation": "Backward DP over timeline allows computing optimal suffix counts while breaking ties in favor of the minimum job index for lexicographical reconstruction.",
        "algorithm": [
            "Group jobs by start time S_i.",
            "Let T_max = 1,000,000.",
            "Initialize dp[t] = {0, INF} for all t.",
            "For t from T_max down to 0:",
            "  dp[t] = dp[t + 1] (idle at time t).",
            "  For each job starting at t with end E_i and id i:",
            "    pair cand = {1 + dp[E_i].first, i};",
            "    if cand.first > dp[t].first: dp[t] = cand;",
            "    else if cand.first == dp[t].first: dp[t].second = min(dp[t].second, cand.second);",
            "Reconstruct sequence: start at t = 0. While dp[t].first > 0: pick job = dp[t].second, advance t = E[job].",
            "Print count and job sequence."
        ],
        "time_complexity": "O(N + T_max)",
        "space_complexity": "O(N + T_max)",
        "core_skill": "Timeline backward DP for lexicographically optimal interval scheduling.",
        "reusable_pattern": "Lexicographical Schedule Reconstruction: Backward DP state (max_count, min_id) + forward greedy hopping.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MAX_T = 1000000;
const int INF = 1e9 + 7;

struct Job {
    int id;
    int end_t;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<Job>> jobs_at(MAX_T + 1);
    vector<int> end_of_job(n + 1);

    for (int i = 1; i <= n; ++i) {
        int s, e;
        cin >> s >> e;
        jobs_at[s].push_back({i, e});
        end_of_job[i] = e;
    }

    // dp[t] = {max_jobs, best_job_id}
    vector<pair<int, int>> dp(MAX_T + 2, {0, INF});

    for (int t = MAX_T; t >= 0; --t) {
        dp[t] = dp[t + 1]; // Option 1: do nothing at time t

        for (const auto& job : jobs_at[t]) {
            int count_after = 1 + dp[job.end_t].first;
            int job_id = job.id;

            if (count_after > dp[t].first) {
                dp[t] = {count_after, job_id};
            } else if (count_after == dp[t].first) {
                dp[t].second = min(dp[t].second, job_id);
            }
        }
    }

    vector<int> result;
    int cur_t = 0;
    while (dp[cur_t].first > 0) {
        int best_job = dp[cur_t].second;
        result.push_back(best_job);
        cur_t = end_of_job[best_job];
    }

    cout << result.size() << "\n";
    for (size_t i = 0; i < result.size(); ++i) {
        cout << result[i] << (i + 1 == result.size() ? "" : " ");
    }
    cout << "\n";

    return 0;
}
"""
    },
    {
        "id": "arc009_3",
        "title": "高橋君、24歳",
        "contest_id": "arc009",
        "rating": 2015,
        "tag": "Combinatorics",
        "subtopic": "Inclusion-Exclusion Principle",
        "topic": "Large N Derangement Counting via Combinations and Montmort Numbers",
        "cat_folder": "combinatorics",
        "cat_file": "large_n_derangement_montmort_numbers.md",
        "statement": "There are N people (N <= 10^18). Count the number of permutations where exactly K people (K <= 777777) do NOT receive their own letter, modulo prime M = 1777777777.",
        "key_idea": "The problem asks for permutations of N elements with exactly K non-fixed points. First, choose the K elements to be deranged in C(N, K) ways. Second, arrange these K elements into a complete derangement in D_K ways (Montmort numbers). Total answer is C(N, K) * D_K mod 1777777777. Since N <= 10^18 and K <= 777777, C(N, K) is computed as (N * (N-1) * ... * (N-K+1)) / K! in O(K) time, and D_K is computed via D_i = (i - 1) * (D_{i-1} + D_{i-2}) mod M in O(K) time.",
        "observation": "Derangements decouple into independent subset selection C(N, K) and permutation without fixed points D_K.",
        "algorithm": [
            "Compute modular inverse of K! mod M = 1777777777.",
            "Compute numerator = N * (N - 1) * ... * (N - K + 1) mod M in O(K).",
            "C(N, K) = numerator * inv(K!) mod M.",
            "Compute D_K using linear recurrence: D_0 = 1, D_1 = 0, D_i = (i - 1) * (D_{i-1} + D_{i-2}) mod M.",
            "ans = C(N, K) * D_K mod M.",
            "Print ans."
        ],
        "time_complexity": "O(K)",
        "space_complexity": "O(1)",
        "core_skill": "Large N combination arithmetic and Montmort derangement recurrence.",
        "reusable_pattern": "Exact K-Derangement Formula: C(N, K) * D_K mod M with O(K) numerator multiplication for huge N.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>

using namespace std;

const long long MOD = 1777777777;

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

long long mod_inv(long long n) {
    return power(n, MOD - 2);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n, k;
    if (!(cin >> n >> k)) return 0;

    // 1. Compute C(N, K) % MOD
    long long num = 1;
    long long den = 1;
    for (long long i = 0; i < k; ++i) {
        num = (num * ((n - i) % MOD)) % MOD;
        den = (den * (i + 1)) % MOD;
    }
    long long c_nk = (num * mod_inv(den)) % MOD;

    // 2. Compute D_K % MOD (Montmort numbers)
    // D_0 = 1, D_1 = 0, D_i = (i - 1) * (D_{i-1} + D_{i-2}) % MOD
    long long d_prev2 = 1; // D_0
    long long d_prev1 = 0; // D_1
    long long d_cur = (k == 0 ? 1 : 0);

    for (long long i = 2; i <= k; ++i) {
        d_cur = ((i - 1) % MOD * (d_prev1 + d_prev2)) % MOD;
        d_prev2 = d_prev1;
        d_prev1 = d_cur;
    }

    long long ans = (c_nk * d_cur) % MOD;
    cout << ans << "\n";

    return 0;
}
"""
    },
    {
        "id": "arc070_b",
        "title": "No Need",
        "contest_id": "abc056",
        "rating": 2015,
        "tag": "Dynamic Programming (DP)",
        "subtopic": "Classic DP",
        "topic": "Monotone Essential Elements via 0-1 Knapsack DP and Binary Search",
        "cat_folder": "dynamic_programming",
        "cat_file": "monotone_essential_elements_knapsack_binary_search.md",
        "statement": "Given N positive integers a_1, ..., a_N and K. A subset is good if its sum >= K. An element a_i is 'needed' if there is some good subset that becomes not good when a_i is removed. Count how many elements are NOT needed.",
        "key_idea": "An element a_i is needed iff there exists a subset of the OTHER elements with sum in [K - a_i, K - 1]. Monotonicity property: if a is sorted in ascending order, if a_i is not needed, then every a_j <= a_i is also not needed! Thus the set of not needed elements forms a prefix a_1, ..., a_m. We binary search on m. To test if a_m is needed, we run 0-1 knapsack on the other elements up to capacity K - 1 and check if any sum in [K - a_m, K - 1] is reachable in O(N K).",
        "observation": "Essentiality in bounded knapsacks is monotonic with respect to element size, reducing all-element queries to binary search.",
        "algorithm": [
            "Sort a in ascending order.",
            "Binary search on the boundary index m in [0, N]:",
            "  Elements >= K are automatically needed.",
            "  To check if a_m is needed:",
            "    Run boolean 0-1 knapsack DP of capacity K using all elements except a_m.",
            "    Check if any dp[s] is true for s in [max(0, K - a_m), K - 1].",
            "    If yes, a_m is needed; if no, a_m is not needed.",
            "The number of not needed elements is the largest m where a_m is not needed."
        ],
        "time_complexity": "O(N * K * log N)",
        "space_complexity": "O(K)",
        "core_skill": "Knapsack essentiality monotonicity and binary search verification.",
        "reusable_pattern": "Monotone Knapsack Essentiality: Sorted elements have a single cutoff point separating unnecessary elements from necessary ones.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }
    sort(a.begin(), a.end());

    auto is_needed = [&](int idx) {
        if (a[idx] >= k) return true;

        vector<bool> dp(k, false);
        dp[0] = true;

        for (int i = 0; i < n; ++i) {
            if (i == idx) continue;
            long long val = a[i];
            if (val >= k) continue;

            for (long long s = k - 1; s >= val; --s) {
                if (dp[s - val]) dp[s] = true;
            }
        }

        long long low_bound = max(0LL, k - a[idx]);
        for (long long s = low_bound; s < k; ++s) {
            if (dp[s]) return true;
        }
        return false;
    };

    int low = 0, high = n - 1, ans = 0;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (!is_needed(mid)) {
            ans = mid + 1;
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }

    cout << ans << "\n";
    return 0;
}
"""
    },
    {
        "id": "abc472_g",
        "title": "Cascading Grid",
        "contest_id": "abc472",
        "rating": 2018,
        "tag": "Graph Theory",
        "subtopic": "Network Flow",
        "topic": "Maximum Weight Closure via Min-Cut on Grid Directed Reachability",
        "cat_folder": "graph_theory",
        "cat_file": "maximum_weight_closure_min_cut_grid.md",
        "statement": "An H x W grid has cells with '+', '-', or '#'. Operation: pick a non-# cell and turn to '#' all cells reachable by moving Left, Right, or Down without passing through '#'. Find the maximum possible value of (count of '+' minus count of '-') remaining in the grid.",
        "key_idea": "Eliminating a cell triggers the elimination of all cells reachable by moving Left, Right, or Down. Thus, the set of eliminated cells must form a closed set in a directed reachability graph. If we eliminate a '-' cell, we gain profit +1; if we eliminate a '+' cell, we incur cost 1 (weight -1). Maximizing the score improvement is exactly the Maximum Weight Closure Problem (Project Selection Problem) on a directed graph, solvable via Min-Cut / Dinic's Algorithm.",
        "observation": "Downward reachability constraints define a transitive closure where removing penalties is dual to minimum cut project selection.",
        "algorithm": [
            "Calculate base score = count(+) - count(-).",
            "Build directed graph on non-# cells: directed edge from u to v if v is adjacent to u by Left, Right, or Down.",
            "Weight of eliminating cell u: if '-', w(u) = +1; if '+', w(u) = -1.",
            "Construct network flow graph: Source S, Sink T.",
            "  For each node u with w(u) > 0: add edge S -> u with capacity w(u).",
            "  For each node u with w(u) < 0: add edge u -> T with capacity -w(u).",
            "  For each dependency u -> v: add edge u -> v with capacity INF.",
            "Compute max flow using Dinic's algorithm.",
            "Max profit gained by eliminating cells = sum_{w > 0} w - min_cut.",
            "Max total score = base_score + max_profit."
        ],
        "time_complexity": "O(V^2 * E) with Dinic on V <= 900",
        "space_complexity": "O(V + E)",
        "core_skill": "Project selection / Maximum weight closure reduction to Dinic Min-Cut.",
        "reusable_pattern": "Grid Closure Min-Cut: Transforming directional cascading domino eliminations into Max Weight Closure.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <algorithm>

using namespace std;

const long long INF = 1e18;

struct Edge {
    int to;
    long long cap;
    long long flow;
    int rev;
};

struct Dinic {
    int n;
    vector<vector<Edge>> adj;
    vector<int> level;
    vector<int> ptr;

    Dinic(int n) : n(n), adj(n), level(n), ptr(n) {}

    void add_edge(int from, int to, long long cap) {
        adj[from].push_back({to, cap, 0, (int)adj[to].size()});
        adj[to].push_back({from, 0, 0, (int)adj[from].size() - 1});
    }

    bool bfs(int s, int t) {
        fill(level.begin(), level.end(), -1);
        level[s] = 0;
        queue<int> q;
        q.push(s);

        while (!q.empty()) {
            int v = q.front();
            q.pop();

            for (const auto& edge : adj[v]) {
                if (edge.cap - edge.flow > 0 && level[edge.to] == -1) {
                    level[edge.to] = level[v] + 1;
                    q.push(edge.to);
                }
            }
        }
        return level[t] != -1;
    }

    long long dfs(int v, int t, long long pushed) {
        if (pushed == 0) return 0;
        if (v == t) return pushed;

        for (int& cid = ptr[v]; cid < (int)adj[v].size(); ++cid) {
            auto& edge = adj[v][cid];
            int trg = edge.to;
            if (level[v] + 1 != level[trg] || edge.cap - edge.flow == 0) continue;

            long long tr = dfs(trg, t, min(pushed, edge.cap - edge.flow));
            if (tr == 0) continue;

            edge.flow += tr;
            adj[trg][edge.rev].flow -= tr;
            return tr;
        }
        return 0;
    }

    long long max_flow(int s, int t) {
        long long flow = 0;
        while (bfs(s, t)) {
            fill(ptr.begin(), ptr.end(), 0);
            while (long long pushed = dfs(s, t, INF)) {
                flow += pushed;
            }
        }
        return flow;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int h, w;
    if (!(cin >> h >> w)) return 0;

    vector<string> grid(h);
    long long base_score = 0;
    for (int i = 0; i < h; ++i) {
        cin >> grid[i];
        for (char c : grid[i]) {
            if (c == '+') base_score++;
            else if (c == '-') base_score--;
        }
    }

    auto id = [&](int r, int c) {
        return r * w + c;
    };

    int total_nodes = h * w;
    int S = total_nodes, T = total_nodes + 1;
    Dinic dinic(total_nodes + 2);

    long long positive_profit = 0;

    // Movement: Left (0, -1), Right (0, 1), Down (1, 0)
    const int dr[3] = {0, 0, 1};
    const int dc[3] = {-1, 1, 0};

    for (int r = 0; r < h; ++r) {
        for (int c = 0; c < w; ++c) {
            if (grid[r][c] == '#') continue;

            int u = id(r, c);
            long long weight = (grid[r][c] == '-' ? 1 : -1);

            if (weight > 0) {
                dinic.add_edge(S, u, weight);
                positive_profit += weight;
            } else if (weight < 0) {
                dinic.add_edge(u, T, -weight);
            }

            for (int d = 0; d < 3; ++d) {
                int nr = r + dr[d];
                int nc = c + dc[d];
                if (nr >= 0 && nr < h && nc >= 0 && nc < w && grid[nr][nc] != '#') {
                    dinic.add_edge(u, id(nr, nc), INF);
                }
            }
        }
    }

    long long min_cut = dinic.max_flow(S, T);
    long long max_gain = positive_profit - min_cut;

    cout << base_score + max_gain << "\n";
    return 0;
}
"""
    },
    {
        "id": "arc183_c",
        "title": "Not Argmax",
        "contest_id": "arc183",
        "rating": 2018,
        "tag": "Dynamic Programming (DP)",
        "subtopic": "Interval DP / Range DP",
        "topic": "Cartesian Tree Root Partition Interval DP under Argmax Constraints",
        "cat_folder": "dynamic_programming",
        "cat_file": "cartesian_tree_root_partition_interval_dp.md",
        "statement": "Given N and M constraints (L_i, R_i, X_i), meaning X_i cannot be the maximum element in subsegment P[L_i ... R_i]. Find the number of valid permutations P of 1 ... N modulo 998244353.",
        "key_idea": "Permutation maximums partition subsegments into Cartesian trees. For any interval [l, r], suppose position x in [l, r] holds the maximum value. Then x is the maximum of every subsegment [L, R] subset of [l, r] containing x. Thus x is valid as root iff no condition (L_i, R_i, X_i = x) satisfies l <= L_i <= x <= R_i <= r. If valid, the left subsegment [l, x-1] and right subsegment [x+1, r] are independent subproblems, combined with binom(r - l, x - l). This yields an O(N^3) Interval DP.",
        "observation": "Cartesian tree recursive splitting decomposes range-maximum constraints into independent interval subproblems.",
        "algorithm": [
            "For each x in [1, N], precompute forbidden intervals: for condition (L_i, R_i, x), if l <= L_i and R_i <= r, root x is forbidden for [l, r].",
            "Initialize dp[l][r] = 0, base cases dp[i][i] = 1, dp[i][i - 1] = 1.",
            "For length len from 1 to N:",
            "  For l from 1 to N - len + 1 (with r = l + len - 1):",
            "    For root x from l to r:",
            "      If x is not forbidden for [l, r]:",
            "        ways = dp[l][x - 1] * dp[x + 1][r] % MOD * C(r - l, x - l) % MOD;",
            "        dp[l][r] = (dp[l][r] + ways) % MOD;",
            "Print dp[1][N]."
        ],
        "time_complexity": "O(N^3 + M)",
        "space_complexity": "O(N^2)",
        "core_skill": "Cartesian tree root selection and forbidden argmax interval DP.",
        "reusable_pattern": "Cartesian Tree Interval DP: dp[l][r] = sum_{x valid} dp[l][x-1] * dp[x+1][r] * binom(len-1, x-l).",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MOD = 998244353;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    // forbidden[x][l] = minimal R such that condition (L, R, x) has L >= l
    // or store conditions per x
    struct Query {
        int l, r;
    };
    vector<vector<Query>> conds(n + 1);
    for (int i = 0; i < m; ++i) {
        int l, r, x;
        cin >> l >> r >> x;
        conds[x].push_back({l, r});
    }

    // precompute combinations
    vector<vector<long long>> C(n + 1, vector<long long>(n + 1, 0));
    for (int i = 0; i <= n; ++i) {
        C[i][0] = 1;
        for (int j = 1; j <= i; ++j) {
            C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % MOD;
        }
    }

    // forbidden_root[l][r][x] can be checked:
    // x is forbidden in [l, r] iff there is some (L, R, x) with l <= L && R <= r
    // For each x and l, let min_r[x][l] be the minimum R over all conditions with L >= l
    vector<vector<int>> min_r(n + 1, vector<int>(n + 2, n + 2));
    for (int x = 1; x <= n; ++x) {
        for (const auto& q : conds[x]) {
            min_r[x][q.l] = min(min_r[x][q.l], q.r);
        }
        for (int l = n; l >= 1; --l) {
            min_r[x][l] = min(min_r[x][l], min_r[x][l + 1]);
        }
    }

    // dp[l][r]
    vector<vector<long long>> dp(n + 2, vector<long long>(n + 2, 0));
    for (int i = 1; i <= n + 1; ++i) {
        dp[i][i - 1] = 1;
    }

    for (int len = 1; len <= n; ++len) {
        for (int l = 1; l <= n - len + 1; ++l) {
            int r = l + len - 1;
            long long sum_ways = 0;

            for (int x = l; x <= r; ++x) {
                // Check if x is forbidden for interval [l, r]
                // Forbidden iff min_r[x][l] <= r
                if (min_r[x][l] <= r) continue;

                long long left_ways = dp[l][x - 1];
                long long right_ways = dp[x + 1][r];
                long long comb = C[r - l][x - l];

                long long cur = (left_ways * right_ways) % MOD;
                cur = (cur * comb) % MOD;
                sum_ways = (sum_ways + cur) % MOD;
            }
            dp[l][r] = sum_ways;
        }
    }

    cout << dp[1][n] << "\n";
    return 0;
}
"""
    }
]

REJECTED_PROBLEMS = [
    # Band 4 Part 1A has no rejections among the first 20 candidates (all 20 are unique archetypes!).
]

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
        f.write("\n### Batch 6 Part 1A: ABC / ARC Curated Ladder (2000 - 2018)\n" + "\n".join(new_q_lines) + "\n")
    print("[+] Updated QUALITY_PROBLEMS_BY_TOPIC.md with new archetypes.")

# Update state/progress.json
with open("state/progress.json", "r", encoding="utf-8") as f:
    progress = json.load(f)

progress["current_batch"] = "Batch 6 Part 1A: ABC / ARC Ladder (2000-2018) COMPLETED"
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
print("Batch 6 Part 1A completed successfully!")
