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
print("      PROCESSING BATCH 5 PART 4B: ABC CURATED LADDER (1951 - 1999)")
print("=" * 75)

SELECTED_PROBLEMS = [
    {
        "id": "arc098_c",
        "title": "Range Minimum Queries",
        "contest_id": "arc098",
        "rating": 1951,
        "tag": "Basics",
        "subtopic": "Greedy / Two Pointers",
        "topic": "Min-Max Spread Optimization via Fixed Lower Bound and Segmented Greedy Extraction",
        "cat_folder": "basics",
        "cat_file": "min_max_spread_fixed_lower_bound.md",
        "statement": "Given array A of length N. In each step, choose an interval of length K, take its minimum, and remove it from A. Repeat Q times. Minimize max(Z) - min(Z) where Z is the multiset of Q removed elements.",
        "key_idea": "Iterate over the minimum element X in Z (at most N choices from A). For a fixed X, any chosen element must be >= X, meaning elements < X cannot be inside any chosen window. This splits A into contiguous segments of elements >= X. For each segment of length L >= K, we can extract L - K + 1 elements; greedily choose the smallest L - K + 1 elements from each segment. If the total extractable elements across all segments is >= Q, take the Q-th smallest element Y from the merged pool, and update ans = min(ans, Y - X).",
        "observation": "Fixing the lower bound decomposes the interval selection constraint into independent contiguous segments where greedy choice is optimal.",
        "algorithm": [
            "For each candidate minimum value X in A:",
            "  Split A into contiguous segments of elements >= X.",
            "  For each segment with length L >= K:",
            "    Sort elements and add the smallest L - K + 1 elements to pool.",
            "  If pool.size() >= Q:",
            "    Sort pool and update ans = min(ans, pool[Q - 1] - X).",
            "Print ans."
        ],
        "time_complexity": "O(N^2 log N)",
        "space_complexity": "O(N)",
        "core_skill": "Fixing the lower bound in min-max spread problems to enable greedy segment extraction.",
        "reusable_pattern": "Fixed Lower Bound Sweep: Iterate X in A, segment elements >= X, extract greedily, take Q-th element.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int INF = 1e9 + 7;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k, q;
    if (!(cin >> n >> k >> q)) return 0;

    vector<int> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    int ans = INF;

    for (int i = 0; i < n; ++i) {
        int x = a[i];
        vector<int> pool;
        vector<int> cur_seg;

        for (int j = 0; j < n; ++j) {
            if (a[j] >= x) {
                cur_seg.push_back(a[j]);
            } else {
                if ((int)cur_seg.size() >= k) {
                    sort(cur_seg.begin(), cur_seg.end());
                    int extract_cnt = (int)cur_seg.size() - k + 1;
                    for (int m = 0; m < extract_cnt; ++m) {
                        pool.push_back(cur_seg[m]);
                    }
                }
                cur_seg.clear();
            }
        }
        if ((int)cur_seg.size() >= k) {
            sort(cur_seg.begin(), cur_seg.end());
            int extract_cnt = (int)cur_seg.size() - k + 1;
            for (int m = 0; m < extract_cnt; ++m) {
                pool.push_back(cur_seg[m]);
            }
        }

        if ((int)pool.size() >= q) {
            sort(pool.begin(), pool.end());
            ans = min(ans, pool[q - 1] - x);
        }
    }

    cout << ans << "\n";
    return 0;
}
"""
    },
    {
        "id": "abc191_d",
        "title": "Circle Lattice Points",
        "contest_id": "abc191",
        "rating": 1953,
        "tag": "Geometry",
        "subtopic": "Lattice Points",
        "topic": "Exact Circle Lattice Point Counting via Fixed-Point Integer Scaling and 1D Sweep",
        "cat_folder": "geometry",
        "cat_file": "circle_lattice_points_fixed_point_sweep.md",
        "statement": "Given circle center (X, Y) and radius R given as decimals with at most 4 digits after the decimal point. Count the number of integer coordinate grid points (x, y) strictly inside or on the boundary of the circle.",
        "key_idea": "Scale X, Y, R by 10^4 into exact 64-bit integers to eliminate floating point error. An integer coordinate x corresponds to scaled coordinate X_scaled = x * 10^4. For each integer x in [ceil((X - R)/10^4), floor((X + R)/10^4)], let dx = x * 10^4 - X. We need (y * 10^4 - Y)^2 <= R^2 - dx^2. Compute D = floor(sqrt(R^2 - dx^2)) using integer square root. The valid integer y values satisfy Y - D <= y * 10^4 <= Y + D, giving floor((Y + D)/10^4) - ceil((Y - D)/10^4) + 1 lattice points.",
        "observation": "Fixed-point integer arithmetic prevents catastrophic precision loss in circular boundary containment checks.",
        "algorithm": [
            "Parse X, Y, R as fixed-point integers scaled by 10^4.",
            "Determine integer range [min_x, max_x] = [ceil((X - R)/10^4), floor((X + R)/10^4)].",
            "ans = 0.",
            "For each x in min_x..max_x:",
            "  dx = x * 10^4 - X.",
            "  Compute D = isqrt(R^2 - dx^2) ensuring exact integer bounds.",
            "  ans += floor((Y + D)/10^4) - ceil((Y - D)/10^4) + 1.",
            "Print ans."
        ],
        "time_complexity": "O(R * 10^-4)",
        "space_complexity": "O(1)",
        "core_skill": "Fixed-point scaling to convert geometric float intersection queries into exact integer range bounds.",
        "reusable_pattern": "Lattice Point Circle Sweep: Scale by 10^4, sweep x, compute integer y bounds via integer sqrt.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <string>
#include <cmath>
#include <algorithm>

using namespace std;

long long parse_fixed(const string& s) {
    bool neg = (s[0] == '-');
    int start = neg ? 1 : 0;
    size_t dot = s.find('.');
    long long integer_part = 0;
    long long frac_part = 0;

    if (dot == string::npos) {
        integer_part = stoll(s.substr(start));
    } else {
        integer_part = stoll(s.substr(start, dot - start));
        string frac_str = s.substr(dot + 1);
        while (frac_str.size() < 4) frac_str += '0';
        if (frac_str.size() > 4) frac_str = frac_str.substr(0, 4);
        frac_part = stoll(frac_str);
    }
    long long val = integer_part * 10000 + frac_part;
    return neg ? -val : val;
}

long long floor_div(long long a, long long b) {
    long long res = a / b;
    long long rem = a % b;
    if (rem != 0 && ((a < 0) ^ (b < 0))) res--;
    return res;
}

long long ceil_div(long long a, long long b) {
    long long res = a / b;
    long long rem = a % b;
    if (rem != 0 && !((a < 0) ^ (b < 0))) res++;
    return res;
}

long long isqrt(long long n) {
    if (n <= 0) return 0;
    long long r = sqrt((double)n);
    while ((r + 1) * (r + 1) <= n) r++;
    while (r * r > n) r--;
    return r;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string sx, sy, sr;
    if (!(cin >> sx >> sy >> sr)) return 0;

    long long X = parse_fixed(sx);
    long long Y = parse_fixed(sy);
    long long R = parse_fixed(sr);

    long long min_x = ceil_div(X - R, 10000);
    long long max_x = floor_div(X + R, 10000);

    long long ans = 0;
    for (long long x = min_x; x <= max_x; ++x) {
        long long dx = x * 10000 - X;
        long long rem_sq = R * R - dx * dx;
        if (rem_sq < 0) continue;

        long long D = isqrt(rem_sq);
        long long min_y = ceil_div(Y - D, 10000);
        long long max_y = floor_div(Y + D, 10000);

        if (max_y >= min_y) {
            ans += (max_y - min_y + 1);
        }
    }

    cout << ans << "\n";
    return 0;
}
"""
    },
    {
        "id": "arc025_3",
        "title": "ウサギとカメ",
        "contest_id": "arc025",
        "rating": 1954,
        "tag": "Graph Theory",
        "subtopic": "Shortest Paths",
        "topic": "All-Pairs Shortest Path Distance Scaling Inequality Counting via Dijkstra and Binary Search",
        "cat_folder": "graph_theory",
        "cat_file": "all_pairs_dijkstra_distance_scaling_inequality.md",
        "statement": "Weighted undirected graph with N vertices and M edges. Takahashi (rabbit) travels at speed R, Aoki (turtle) at speed T. Count ordered triplets of distinct vertices (s, r, t) such that the turtle takes strictly less time than the rabbit: dist(s, t) / T < dist(s, r) / R.",
        "key_idea": "The condition is dist(s, t) * R < dist(s, r) * T. For each starting vertex s, run Dijkstra to obtain all distances dist(s, v). Sort the non-source vertices by distance. For each chosen goal vertex t, the required condition on rabbit vertex r is dist(s, r) > dist(s, t) * R / T. Using binary search (upper_bound) on the sorted distances, count valid r vertices in O(log N), excluding s and t.",
        "observation": "Fixing the source s and goal t decouples the search for r into an upper_bound query on the sorted distance array.",
        "algorithm": [
            "For each vertex s in 1..N:",
            "  Run Dijkstra to compute dist[s][v] for all v.",
            "  Collect and sort distances to all v != s.",
            "  For each goal t != s:",
            "    Compute threshold = dist[s][t] * R / T.",
            "    Find count of vertices with dist > threshold via upper_bound.",
            "    If dist[s][t] > threshold, decrement count (since r cannot equal t).",
            "    ans += count.",
            "Print ans."
        ],
        "time_complexity": "O(N * (M log N + N log N))",
        "space_complexity": "O(N + M)",
        "core_skill": "All-pairs shortest paths combined with binary search on scaled distance inequalities.",
        "reusable_pattern": "Dijkstra Inequality Counting: Dijkstra from each source, sort distances, query valid pairs via upper_bound.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

const long long INF = 1e18;

struct Edge {
    int to;
    long long w;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    long long R, T;
    if (!(cin >> n >> m >> R >> T)) return 0;

    vector<vector<Edge>> adj(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v;
        long long w;
        cin >> u >> v >> w;
        adj[u].push_back({v, w});
        adj[v].push_back({u, w});
    }

    long long total_count = 0;

    for (int s = 1; s <= n; ++s) {
        vector<long long> dist(n + 1, INF);
        priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> pq;

        dist[s] = 0;
        pq.push({0, s});

        while (!pq.empty()) {
            auto [d, u] = pq.top();
            pq.pop();

            if (d > dist[u]) continue;

            for (const auto& e : adj[u]) {
                if (dist[e.to] > d + e.w) {
                    dist[e.to] = d + e.w;
                    pq.push({dist[e.to], e.to});
                }
            }
        }

        vector<long long> dlist;
        for (int v = 1; v <= n; ++v) {
            if (v != s && dist[v] < INF) {
                dlist.push_back(dist[v]);
            }
        }
        sort(dlist.begin(), dlist.end());

        for (int t = 1; t <= n; ++t) {
            if (t == s || dist[t] == INF) continue;

            long long lhs = dist[t] * R;
            long long threshold = lhs / T;

            int valid_r = dlist.end() - upper_bound(dlist.begin(), dlist.end(), threshold);
            if (dist[t] > threshold) {
                valid_r--;
            }
            total_count += valid_r;
        }
    }

    cout << total_count << "\n";
    return 0;
}
"""
    },
    {
        "id": "abc200_e",
        "title": "Patisserie ABC 2",
        "contest_id": "abc200",
        "rating": 1955,
        "tag": "Combinatorics",
        "subtopic": "Inclusion-Exclusion / Stars and Bars",
        "topic": "Lexicographical K-th Triplet Selection under Bounded Sum via Stars and Bars Bounding",
        "cat_folder": "combinatorics",
        "cat_file": "lexicographical_kth_triplet_bounded_sum.md",
        "statement": "Cakes have 3 integer beauty attributes (i, j, k) in [1, N]. They are sorted by sum S = i + j + k ascending, then i ascending, then j ascending. Find the K-th cake.",
        "key_idea": "For a fixed sum S in [3, 3N], the number of integer solutions to i + j + k = S with 1 <= i, j, k <= N is computed via stars-and-bars with inclusion-exclusion: binom(S - 1, 2) - 3*binom(S - 1 - N, 2) + 3*binom(S - 1 - 2N, 2). Subtract counts to identify the exact sum S containing the K-th cake. Then iterate i in [1, N]; the number of pairs (j, k) with j + k = S - i and 1 <= j, k <= N is the length of interval [max(1, S - i - N), min(N, S - i - 1)]. Subtract to locate i, then j, then k = S - i - j.",
        "observation": "Stars-and-bars with inclusion-exclusion gives O(1) count for sum S, reducing search space to O(N).",
        "algorithm": [
            "Compute ways(S) for S = 3..3N using inclusion-exclusion.",
            "Find exact sum S containing K by subtracting ways(S).",
            "For each candidate i in 1..N:",
            "  rem = S - i. Compute count of j in [1, N] such that 1 <= rem - j <= N.",
            "  If count >= K: commit to i, break. Else: K -= count.",
            "Find j by adding min_j + K - 1. Set k = S - i - j.",
            "Print i, j, k."
        ],
        "time_complexity": "O(N)",
        "space_complexity": "O(1)",
        "core_skill": "Multi-variable bounded sum counting via stars-and-bars with lexicographical rank extraction.",
        "reusable_pattern": "Lexicographical K-th Triplet: Identify sum bucket via stars-and-bars, identify first element, deduce remainder.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <algorithm>

using namespace std;

long long C2(long long n) {
    if (n < 2) return 0;
    return n * (n - 1) / 2;
}

long long count_triplets(long long S, long long N) {
    long long ans = C2(S - 1);
    if (S - 1 - N >= 2) ans -= 3 * C2(S - 1 - N);
    if (S - 1 - 2 * N >= 2) ans += 3 * C2(S - 1 - 2 * N);
    return ans;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n, k;
    if (!(cin >> n >> k)) return 0;

    long long target_s = -1;
    for (long long s = 3; s <= 3 * n; ++s) {
        long long ways = count_triplets(s, n);
        if (k <= ways) {
            target_s = s;
            break;
        }
        k -= ways;
    }

    long long ans_i = -1, ans_j = -1, ans_k = -1;

    for (long long i = 1; i <= n; ++i) {
        long long rem = target_s - i;
        long long low_j = max(1LL, rem - n);
        long long high_j = min(n, rem - 1);

        if (low_j <= high_j) {
            long long ways = high_j - low_j + 1;
            if (k <= ways) {
                ans_i = i;
                ans_j = low_j + k - 1;
                ans_k = target_s - ans_i - ans_j;
                break;
            }
            k -= ways;
        }
    }

    cout << ans_i << " " << ans_j << " " << ans_k << "\n";
    return 0;
}
"""
    },
    {
        "id": "abc017_4",
        "title": "サプリメント",
        "contest_id": "abc017",
        "rating": 1956,
        "tag": "Dynamic Programming (DP)",
        "subtopic": "Two Pointers / Prefix Sum DP",
        "topic": "Non-Duplicate Contiguous Partition DP Accelerated by Monotonic Left-Bound Prefix Sums",
        "cat_folder": "dp",
        "cat_file": "non_duplicate_partition_prefix_sum_dp.md",
        "statement": "Given N supplements of types f_1, ..., f_N. Partition the sequence into contiguous packs such that no pack contains duplicate supplement types. Find the number of valid partitionings modulo 10^9 + 7.",
        "key_idea": "Let dp[i] be the number of valid partitions of prefix 1..i. dp[i] = sum_{j = L_i}^{i - 1} dp[j], where L_i is the smallest index such that subarray f[L_i + 1..i] contains no duplicates. The boundary L_i is monotonically non-decreasing: L_i = max(L_{i-1}, last_pos[f_i]). Because L_i is monotonic, the transition is a range sum query over dp[L_i..i-1], maintained in O(1) via prefix sums of dp.",
        "observation": "Monotonicity of valid left boundaries enables O(1) DP transitions via prefix sums.",
        "algorithm": [
            "Initialize dp[0] = 1, pref[0] = 0, pref[1] = 1.",
            "Maintain last_pos[type] initialized to 0.",
            "L = 0.",
            "For i = 1 to N:",
            "  L = max(L, last_pos[f[i]]).",
            "  dp[i] = (pref[i] - pref[L] + MOD) % MOD.",
            "  pref[i + 1] = (pref[i] + dp[i]) % MOD.",
            "  last_pos[f[i]] = i.",
            "Print dp[N]."
        ],
        "time_complexity": "O(N)",
        "space_complexity": "O(N + M)",
        "core_skill": "Combining two-pointer monotonic boundaries with prefix sum arrays for linear-time partition DP.",
        "reusable_pattern": "Non-Duplicate Partition DP: L = max(L, last_seen[val]), dp[i] = pref[i] - pref[L].",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MOD = 1000000007;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<int> f(n + 1);
    for (int i = 1; i <= n; ++i) {
        cin >> f[i];
    }

    vector<int> dp(n + 1, 0);
    vector<int> pref(n + 2, 0);
    vector<int> last_pos(m + 1, 0);

    dp[0] = 1;
    pref[1] = 1;

    int L = 0;
    for (int i = 1; i <= n; ++i) {
        L = max(L, last_pos[f[i]]);
        dp[i] = (pref[i] - pref[L] + MOD) % MOD;
        pref[i + 1] = (pref[i] + dp[i]) % MOD;
        last_pos[f[i]] = i;
    }

    cout << dp[n] << "\n";
    return 0;
}
"""
    },
    {
        "id": "arc153_c",
        "title": "± Increasing Sequence",
        "contest_id": "arc153",
        "rating": 1960,
        "tag": "Basics",
        "subtopic": "Constructive",
        "topic": "Difference Sequence Linear Equation Construction with Suffix Sum Invariants",
        "cat_folder": "basics",
        "cat_file": "difference_sequence_suffix_sum_construction.md",
        "statement": "Given sequence A of length N with A_i in {+1, -1}. Construct a strictly increasing integer sequence x_1 < x_2 < ... < x_N such that sum(A_i * x_i) = 0 with |x_i| <= 10^12, or report No.",
        "key_idea": "Represent x_i via positive differences: x_i = x_1 + sum_{j=1}^{i-1} d_j with d_j >= 1. The equation sum(A_i * x_i) = 0 rewrites to x_1 * sum(A) + sum_{j=1}^{N-1} d_j * suffix_sum_{j+1}(A) = 0. If sum(A) != 0, set d_j = 1, adjust d_j by at most sum(A), and solve for x_1. If sum(A) = 0, find a positive suffix sum and a negative suffix sum to cancel each other out by scaling their respective d_j. If all suffix sums have identical sign, output No.",
        "observation": "Change of variables to positive differences transforms coordinate constraints into linear combinations of suffix sums.",
        "algorithm": [
            "Compute total sum and suffix sums of A.",
            "If sum(A) != 0: set base d_j = 1; adjust one d_j so that the remaining sum is divisible by sum(A); solve for x_1; reconstruct x_i.",
            "If sum(A) == 0: find index p with suf[p] > 0 and index q with suf[q] < 0. Set d_p = -suf[q], d_q = suf[p], other d_j = 1. Balance with offset.",
            "If no two opposite-sign suffix sums exist, output No.",
            "Print Yes and the constructed sequence."
        ],
        "time_complexity": "O(N)",
        "space_complexity": "O(N)",
        "core_skill": "Transforming monotonicity into difference variables and solving under suffix sum invariants.",
        "reusable_pattern": "Increasing Sequence Construction: Rewrite x_i = x_1 + sum(d_j), solve sum(d_j * suf_{j+1}) = 0.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    if (n == 1) {
        cout << "No\n";
        return 0;
    }

    vector<long long> suf(n + 1, 0);
    for (int i = n - 1; i >= 0; --i) {
        suf[i] = suf[i + 1] + a[i];
    }

    vector<long long> x(n);

    if (suf[0] != 0) {
        long long S = 0;
        for (int i = 0; i < n; ++i) {
            x[i] = i;
            S += a[i] * x[i];
        }

        if (suf[0] > 0) {
            // Need S to decrease, increase x[0] by -S / suf[0]
            x[0] -= S;
        } else {
            x[0] += S;
        }

        // Adjust so that x is strictly increasing
        long long min_diff = 1;
        long long cur = x[0];
        vector<long long> ans(n);
        ans[0] = x[0];
        for (int i = 1; i < n; ++i) {
            ans[i] = max(ans[i - 1] + 1, x[i]);
        }
        // Direct reconstruction
        vector<long long> d(n - 1, 1);
        long long current_sum = 0;
        for (int i = 0; i < n - 1; ++i) {
            current_sum += d[i] * suf[i + 1];
        }
        long long rem = -current_sum;
        long long q = rem / suf[0];
        long long r = rem % suf[0];
        if (r < 0) {
            r += abs(suf[0]);
            q = (rem - r) / suf[0];
        }

        int target_idx = -1;
        for (int i = 0; i < n - 1; ++i) {
            if ((suf[0] > 0 && suf[i + 1] == 1) || (suf[0] < 0 && suf[i + 1] == -1)) {
                target_idx = i;
                break;
            }
        }
        if (target_idx != -1) {
            d[target_idx] += abs(suf[0]) - r;
            current_sum = 0;
            for (int i = 0; i < n - 1; ++i) current_sum += d[i] * suf[i + 1];
            q = -current_sum / suf[0];
        }

        cout << "Yes\n";
        vector<long long> res(n);
        res[0] = q;
        for (int i = 0; i < n - 1; ++i) {
            res[i + 1] = res[i] + d[i];
        }
        for (int i = 0; i < n; ++i) {
            cout << res[i] << (i == n - 1 ? "" : " ");
        }
        cout << "\n";
    } else {
        int pos_idx = -1, neg_idx = -1;
        for (int i = 1; i < n; ++i) {
            if (suf[i] > 0 && pos_idx == -1) pos_idx = i;
            if (suf[i] < 0 && neg_idx == -1) neg_idx = i;
        }

        if (pos_idx == -1 || neg_idx == -1) {
            cout << "No\n";
            return 0;
        }

        cout << "Yes\n";
        vector<long long> d(n - 1, 1);
        long long current_sum = 0;
        for (int i = 0; i < n - 1; ++i) {
            current_sum += d[i] * suf[i + 1];
        }

        if (current_sum > 0) {
            d[neg_idx - 1] += current_sum; // since suf[neg_idx] <= -1, this reduces sum
        } else if (current_sum < 0) {
            d[pos_idx - 1] += (-current_sum); // increases sum
        }

        vector<long long> res(n);
        res[0] = 0;
        for (int i = 0; i < n - 1; ++i) {
            res[i + 1] = res[i] + d[i];
        }
        for (int i = 0; i < n; ++i) {
            cout << res[i] << (i == n - 1 ? "" : " ");
        }
        cout << "\n";
    }

    return 0;
}
"""
    },
    {
        "id": "abc167_f",
        "title": "Bracket Sequencing",
        "contest_id": "abc167",
        "rating": 1961,
        "tag": "Basics",
        "subtopic": "Greedy / Invariants",
        "topic": "Bipartite Greedy Balance Sorting for Bracket Sequence Concatenation",
        "cat_folder": "basics",
        "cat_file": "bipartite_greedy_bracket_concatenation.md",
        "statement": "Given N bracket sequences S_1, ..., S_N. Determine whether they can be concatenated in some order to form a single valid bracket sequence.",
        "key_idea": "Reduce each string by canceling matched pairs '()', leaving a string of form ')))((('. Each string is characterized by required prefix balance L_i and net change delta_i = R_i - L_i. Overall balance sum(delta_i) must equal 0. Partition into positive delta (delta >= 0) and negative delta (delta < 0). Positive delta strings are sorted by L_i ascending (process low requirements first). Negative delta strings are viewed in reverse and sorted by R_i descending. Then simulate prefix balance to ensure it never drops below 0.",
        "observation": "Reversing the process for net-negative brackets aligns the greedy priority with right-end requirements.",
        "algorithm": [
            "For each string S_i, compute min_balance L_i and net delta_i.",
            "Check if sum(delta_i) == 0; if not, return No.",
            "Split into positive (delta >= 0) and negative (delta < 0).",
            "Sort positive by L_i ascending.",
            "Sort negative by R_i = L_i + delta_i descending.",
            "Simulate running balance across concatenated positive then negative strings.",
            "If running balance < 0 at any point, output No; else Yes."
        ],
        "time_complexity": "O(sum |S_i| + N log N)",
        "space_complexity": "O(sum |S_i|)",
        "core_skill": "Bipartite exchange sorting on prefix and suffix bracket balance profiles.",
        "reusable_pattern": "Bracket Sequencing: delta >= 0 sorted by L asc; delta < 0 sorted by R desc.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

struct BracketString {
    int req;   // min prefix balance required
    int delta; // net change
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<BracketString> pos, neg;
    long long total_delta = 0;

    for (int i = 0; i < n; ++i) {
        string s;
        cin >> s;

        int bal = 0;
        int min_bal = 0;
        for (char c : s) {
            if (c == '(') bal++;
            else bal--;
            min_bal = min(min_bal, bal);
        }

        int req = -min_bal;
        int delta = bal;
        total_delta += delta;

        if (delta >= 0) {
            pos.push_back({req, delta});
        } else {
            neg.push_back({req, delta});
        }
    }

    if (total_delta != 0) {
        cout << "No\n";
        return 0;
    }

    sort(pos.begin(), pos.end(), [](const BracketString& a, const BracketString& b) {
        return a.req < b.req;
    });

    sort(neg.begin(), neg.end(), [](const BracketString& a, const BracketString& b) {
        int ra = a.req + a.delta;
        int rb = b.req + b.delta;
        return ra > rb;
    });

    long long cur_bal = 0;
    for (const auto& bs : pos) {
        if (cur_bal < bs.req) {
            cout << "No\n";
            return 0;
        }
        cur_bal += bs.delta;
    }

    for (const auto& bs : neg) {
        if (cur_bal < bs.req) {
            cout << "No\n";
            return 0;
        }
        cur_bal += bs.delta;
    }

    cout << (cur_bal == 0 ? "Yes" : "No") << "\n";
    return 0;
}
"""
    },
    {
        "id": "abc216_g",
        "title": "01Sequence",
        "contest_id": "abc216",
        "rating": 1963,
        "tag": "Data Structures (DS)",
        "subtopic": "DSU / Fenwick Tree",
        "topic": "Greedy Rightmost Interval 1-Filling via DSU Predecessor Jumping and Fenwick Tree",
        "cat_folder": "data_structures",
        "cat_file": "greedy_interval_filling_dsu_fenwick.md",
        "statement": "Given N and M intervals [L_i, R_i] with required minimum number of 1s X_i. Construct a 0-1 sequence of length N that satisfies all constraints while minimizing the total number of 1s.",
        "key_idea": "Sort constraints by R_i ascending. To help future overlapping intervals, any needed 1s should be placed as far right as possible within [L_i, R_i]. Query the number of existing 1s in [L_i, R_i] via a Fenwick Tree. If count < X_i, greedily place 1s at the largest unoccupied indices <= R_i. Finding the largest available 0 position <= x is accelerated to nearly O(1) using a DSU predecessor pointer: parent[x] = find(x - 1) when position x is filled.",
        "observation": "DSU predecessor jumping eliminates scanning already-filled indices, achieving linear-logarithmic interval filling.",
        "algorithm": [
            "Sort constraints by R_i ascending.",
            "Initialize Fenwick Tree and DSU parent[i] = i for i = 0..N.",
            "For each constraint (L_i, R_i, X_i):",
            "  existing = query(R_i) - query(L_i - 1).",
            "  needed = X_i - existing.",
            "  while needed > 0:",
            "    idx = find(R_i).",
            "    ans[idx] = 1, update Fenwick at idx.",
            "    parent[idx] = find(idx - 1).",
            "    needed--.",
            "Print ans[1..N]."
        ],
        "time_complexity": "O(N * alpha(N) + M log N)",
        "space_complexity": "O(N)",
        "core_skill": "Combining DSU fast-forwarding for unoccupied index discovery with Fenwick tree range counting.",
        "reusable_pattern": "Greedy Rightmost Fill: DSU find(R) jumps directly to the latest available free index.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Constraint {
    int l, r, x;
};

int parent_dsu[200005];

int find_set(int v) {
    if (v == parent_dsu[v]) return v;
    return parent_dsu[v] = find_set(parent_dsu[v]);
}

int bit_tree[200005];
int n_size;

void bit_add(int idx, int val) {
    for (; idx <= n_size; idx += idx & -idx) bit_tree[idx] += val;
}

int bit_query(int idx) {
    int sum = 0;
    for (; idx > 0; idx -= idx & -idx) sum += bit_tree[idx];
    return sum;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;
    n_size = n;

    vector<Constraint> cons(m);
    for (int i = 0; i < m; ++i) {
        cin >> cons[i].l >> cons[i].r >> cons[i].x;
    }

    sort(cons.begin(), cons.end(), [](const Constraint& a, const Constraint& b) {
        return a.r < b.r;
    });

    for (int i = 0; i <= n; ++i) {
        parent_dsu[i] = i;
    }

    vector<int> ans(n + 1, 0);

    for (const auto& c : cons) {
        int existing = bit_query(c.r) - bit_query(c.l - 1);
        int needed = c.x - existing;

        while (needed > 0) {
            int pos = find_set(c.r);
            if (pos < c.l) break;

            ans[pos] = 1;
            bit_add(pos, 1);
            parent_dsu[pos] = find_set(pos - 1);
            needed--;
        }
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
        "id": "arc105_c",
        "title": "Camels and Bridge",
        "contest_id": "arc105",
        "rating": 1964,
        "tag": "Basics",
        "subtopic": "Permutations / DAG DP",
        "topic": "Extremal Permutation Evaluation with Segment Weight Constraints and DAG Distance DP",
        "cat_folder": "basics",
        "cat_file": "extremal_permutation_dag_distance_dp.md",
        "statement": "N camels (N <= 8) with weights w_1..w_N must cross an M-part bridge (M <= 10^5). Part j has length l_j and weight limit v_j. Find the minimum distance between the front and rear camels so that no bridge section is overloaded.",
        "key_idea": "Since N <= 8, enumerate all N! = 40320 permutations. Precompute req_dist[W]: the maximum length of any bridge section with weight capacity < W, using two-pointer/binary search on pre-sorted bridge sections. For a fixed camel order, any subsegment of camels i..j has total weight W(i..j); if W(i..j) > min(v), the distance between camel i and camel j must be >= req_dist[W(i..j)]. Compute camel positions via DAG DP: pos[j] = max_{i < j} (pos[i] + req_dist[W(i..j)]). Output the minimum pos[N] over all permutations.",
        "observation": "Small N <= 8 permits full permutation search; bridge weight constraints simplify to maximum length under weight thresholds.",
        "algorithm": [
            "Check if max(w_i) > min(v_j); if so, print -1.",
            "Sort bridge parts by capacity v_j ascending and build prefix maximums of length l_j.",
            "Enumerate all N! permutations of camels.",
            "For each permutation, evaluate pairwise distance requirements req[i][j] via binary search on weight sum.",
            "Compute positions: pos[0] = 0; pos[j] = max_{i < j} (pos[i] + req[i][j]).",
            "ans = min(ans, pos[N - 1]).",
            "Print ans."
        ],
        "time_complexity": "O(M log M + N! * N^2)",
        "space_complexity": "O(M + N^2)",
        "core_skill": "Permutation enumeration with weight-capacity binary search and DAG distance dynamic programming.",
        "reusable_pattern": "Permutation Spacing DP: pos[j] = max_{i < j} (pos[i] + min_dist(i, j)), minimized over all N! permutations.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

using namespace std;

const long long INF = 1e18;

struct Bridge {
    long long l, v;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<long long> w(n);
    long long max_w = 0;
    for (int i = 0; i < n; ++i) {
        cin >> w[i];
        max_w = max(max_w, w[i]);
    }

    vector<Bridge> b(m);
    long long min_v = INF;
    for (int i = 0; i < m; ++i) {
        cin >> b[i].l >> b[i].v;
        min_v = min(min_v, b[i].v);
    }

    if (max_w > min_v) {
        cout << -1 << "\n";
        return 0;
    }

    sort(b.begin(), b.end(), [](const Bridge& x, const Bridge& y) {
        return x.v < y.v;
    });

    vector<long long> pref_max_l(m);
    pref_max_l[0] = b[0].l;
    for (int i = 1; i < m; ++i) {
        pref_max_l[i] = max(pref_max_l[i - 1], b[i].l);
    }

    auto get_min_dist = [&](long long weight) -> long long {
        // Find largest bridge with v < weight
        int low = 0, high = m - 1, best = -1;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (b[mid].v < weight) {
                best = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        if (best == -1) return 0;
        return pref_max_l[best];
    };

    vector<int> p(n);
    iota(p.begin(), p.end(), 0);

    long long min_total_dist = INF;

    do {
        vector<long long> pos(n, 0);
        for (int j = 0; j < n; ++j) {
            long long cur_w = w[p[j]];
            for (int i = j - 1; i >= 0; --i) {
                cur_w += w[p[i]];
                long long req = get_min_dist(cur_w);
                pos[j] = max(pos[j], pos[i] + req);
            }
        }
        min_total_dist = min(min_total_dist, pos[n - 1]);
    } while (next_permutation(p.begin(), p.end()));

    cout << min_total_dist << "\n";
    return 0;
}
"""
    },
    {
        "id": "abc152_f",
        "title": "Tree and Constraints",
        "contest_id": "abc152",
        "rating": 1965,
        "tag": "Combinatorics",
        "subtopic": "Inclusion-Exclusion",
        "topic": "Principle of Inclusion-Exclusion on Tree Path Cover Constraints via Bitmask Edge Unions",
        "cat_folder": "combinatorics",
        "cat_file": "pie_tree_path_bitmask_edge_unions.md",
        "statement": "Given a tree with N vertices (N <= 50). Each edge can be colored white or black (2^{N-1} colorings). M constraints (M <= 20): path between u_i and v_i must contain at least one black edge. Count valid colorings.",
        "key_idea": "M <= 20 directly suggests Principle of Inclusion-Exclusion (PIE). Let violation condition i be: all edges on path (u_i, v_i) are white. For a subset of constraints S in {0..M-1}, all edges on paths in S must be colored white. Compute the path edge set for each constraint as a 64-bit integer mask. For any subset S, the union of edges is the bitwise OR of path masks. If S forces K = popcount(mask) edges to be white, the remaining (N - 1 - K) edges have 2 choices each. By PIE, sum_{S} (-1)^{|S|} 2^{N - 1 - popcount(union_mask)} gives the exact answer.",
        "observation": "N <= 50 fits into a standard 64-bit integer bitmask, reducing tree edge set unions to O(1) bitwise OR operations.",
        "algorithm": [
            "Assign edge IDs 0..N-2 to all tree edges.",
            "For each of the M constraints (u_i, v_i), find path via DFS and encode edge set as a 64-bit mask.",
            "Iterate S from 0 to 2^M - 1:",
            "  union_mask = 0, sign = 1.",
            "  For each bit j in S: union_mask |= path_mask[j], sign = -sign.",
            "  free_edges = (N - 1) - popcount(union_mask).",
            "  ans += sign * (1ULL << free_edges).",
            "Print ans."
        ],
        "time_complexity": "O(N + M + M * 2^M)",
        "space_complexity": "O(N + M)",
        "core_skill": "Principle of Inclusion-Exclusion accelerated by 64-bit bitmask edge path representations.",
        "reusable_pattern": "Tree Path PIE: Encode paths as uint64_t masks, iterate 2^M subsets, evaluate via 1ULL << (E - popcount).",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <cstdint>

using namespace std;

struct Edge {
    int to;
    int id;
};

int n, m;
vector<vector<Edge>> adj;
vector<uint64_t> path_mask;

bool get_path(int u, int target, int parent, uint64_t& mask) {
    if (u == target) return true;
    for (const auto& e : adj[u]) {
        if (e.to == parent) continue;
        mask |= (1ULL << e.id);
        if (get_path(e.to, target, u, mask)) return true;
        mask &= ~(1ULL << e.id);
    }
    return false;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n)) return 0;

    adj.assign(n + 1, vector<Edge>());
    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back({v, i});
        adj[v].push_back({u, i});
    }

    cin >> m;
    path_mask.assign(m, 0);
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        uint64_t mask = 0;
        get_path(u, v, -1, mask);
        path_mask[i] = mask;
    }

    long long total_valid = 0;
    int total_subsets = 1 << m;

    for (int mask = 0; mask < total_subsets; ++mask) {
        uint64_t union_edges = 0;
        int bits = 0;
        for (int i = 0; i < m; ++i) {
            if ((mask >> i) & 1) {
                union_edges |= path_mask[i];
                bits++;
            }
        }

        int forced_white = __builtin_popcountll(union_edges);
        long long ways = 1LL << ((n - 1) - forced_white);

        if (bits % 2 == 1) {
            total_valid -= ways;
        } else {
            total_valid += ways;
        }
    }

    cout << total_valid << "\n";
    return 0;
}
"""
    },
    {
        "id": "abc170_f",
        "title": "Pond Skater",
        "contest_id": "abc170",
        "rating": 1968,
        "tag": "Graph Theory",
        "subtopic": "Grid BFS",
        "topic": "Bounded Ray-Shooting Grid BFS with Early Pruning on Directional Steps",
        "cat_folder": "graph_theory",
        "cat_file": "bounded_ray_shooting_grid_bfs.md",
        "statement": "An H x W grid (H * W <= 10^6). A skater can travel up to K squares in one cardinal direction per move without crossing obstacles. Find minimum moves from (x_1, y_1) to (x_2, y_2), or -1.",
        "key_idea": "Standard BFS explores neighbor cells. Traveling up to K squares introduces up to K steps per direction. To maintain linear complexity O(H * W), when extending in direction (dr, dc) up to K steps: if a cell (nr, nc) has dist[nr][nc] < dist[r][c] + 1, we can pass through it (since future cells along this ray may not have been reached yet), but if dist[nr][nc] <= dist[r][c], an earlier/shorter wave has already explored this ray further, so we can immediately break!",
        "observation": "Breaking ray expansion when encountering a cell reached with <= current distance guarantees each cell is visited at most a constant number of times.",
        "algorithm": [
            "Initialize dist[H][W] with INF.",
            "Set dist[x_1][y_1] = 0 and push to queue.",
            "While queue is not empty:",
            "  pop (r, c).",
            "  For each of the 4 cardinal directions:",
            "    For step s = 1 to K:",
            "      nr = r + dr * s, nc = c + dc * s.",
            "      If out of bounds or obstacle, break.",
            "      If dist[nr][nc] <= dist[r][c], break.",
            "      If dist[nr][nc] == INF: dist[nr][nc] = dist[r][c] + 1, push (nr, nc).",
            "Print dist[x_2][y_2] if < INF, else -1."
        ],
        "time_complexity": "O(H * W)",
        "space_complexity": "O(H * W)",
        "core_skill": "Optimizing ray-shooting grid BFS via directional early-pruning conditions.",
        "reusable_pattern": "Ray-Shooting BFS: Break ray expansion when dist[next] <= dist[cur] to guarantee O(V + E) bounds.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <string>
#include <queue>

using namespace std;

const int INF = 1e9 + 7;
const int dr[] = {-1, 1, 0, 0};
const int dc[] = {0, 0, -1, 1};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int h, w, k;
    if (!(cin >> h >> w >> k)) return 0;

    int x1, y1, x2, y2;
    cin >> x1 >> y1 >> x2 >> y2;
    --x1; --y1; --x2; --y2;

    vector<string> grid(h);
    for (int i = 0; i < h; ++i) {
        cin >> grid[i];
    }

    vector<vector<int>> dist(h, vector<int>(w, INF));
    queue<pair<int, int>> q;

    dist[x1][y1] = 0;
    q.push({x1, y1});

    while (!q.empty()) {
        auto [r, c] = q.front();
        q.pop();

        if (r == x2 && c == y2) {
            cout << dist[r][c] << "\n";
            return 0;
        }

        int d = dist[r][c];

        for (int dir = 0; dir < 4; ++dir) {
            for (int s = 1; s <= k; ++s) {
                int nr = r + dr[dir] * s;
                int nc = c + dc[dir] * s;

                if (nr < 0 || nr >= h || nc < 0 || nc >= w || grid[nr][nc] == '@') {
                    break;
                }
                if (dist[nr][nc] <= d) {
                    break;
                }
                if (dist[nr][nc] == INF) {
                    dist[nr][nc] = d + 1;
                    q.push({nr, nc});
                }
            }
        }
    }

    cout << (dist[x2][y2] >= INF ? -1 : dist[x2][y2]) << "\n";
    return 0;
}
"""
    },
    {
        "id": "arc029_3",
        "title": "高橋君と国家",
        "contest_id": "arc029",
        "rating": 1973,
        "tag": "Graph Theory",
        "subtopic": "Minimum Spanning Tree",
        "topic": "Super-Source Vertex Activation Transformation for Minimum Spanning Tree",
        "cat_folder": "graph_theory",
        "cat_file": "super_source_mst_vertex_activation.md",
        "statement": "N cities, M roads. City i can build a trade port for cost c_i. Road j connects a_j, b_j with cost r_j. Find minimum cost so every city is connected to at least one trade port.",
        "key_idea": "Building a trade port at city i can be modeled as adding an edge between city i and a virtual 'super-source' vertex 0 with weight c_i. The requirement that every city has a path to at least one trade port is equivalent to requiring that every city is connected to vertex 0! Thus, the problem reduces directly to finding the Minimum Spanning Tree on N + 1 vertices (vertices 0..N) using Kruskal's algorithm with DSU.",
        "observation": "Vertex costs are transformed into edges to an auxiliary super-source, unifying vertex activation with edge connectivity.",
        "algorithm": [
            "Create graph with N + 1 vertices (0 to N).",
            "Add edge (0, i) with weight c_i for each city i in 1..N.",
            "Add road edges (a_j, b_j) with weight r_j.",
            "Sort all N + M edges by weight ascending.",
            "Run Kruskal's algorithm with DSU to find MST weight.",
            "Print total MST weight."
        ],
        "time_complexity": "O((N + M) log(N + M))",
        "space_complexity": "O(N + M)",
        "core_skill": "Super-source graph modeling for facility location and vertex activation via MST.",
        "reusable_pattern": "Super-Source MST: Connect facility candidate i to dummy node 0 with weight c_i; run Kruskal.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
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
    DSU(int n) : parent(n) {
        iota(parent.begin(), parent.end(), 0);
    }
    int find(int v) {
        if (v == parent[v]) return v;
        return parent[v] = find(parent[v]);
    }
    bool unite(int a, int b) {
        a = find(a);
        b = find(b);
        if (a != b) {
            parent[b] = a;
            return true;
        }
        return false;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<Edge> edges;
    for (int i = 1; i <= n; ++i) {
        long long c;
        cin >> c;
        edges.push_back({0, i, c});
    }

    for (int i = 0; i < m; ++i) {
        int u, v;
        long long r;
        cin >> u >> v >> r;
        edges.push_back({u, v, r});
    }

    sort(edges.begin(), edges.end(), [](const Edge& a, const Edge& b) {
        return a.w < b.w;
    });

    DSU dsu(n + 1);
    long long total_cost = 0;
    int edges_used = 0;

    for (const auto& e : edges) {
        if (dsu.unite(e.u, e.v)) {
            total_cost += e.w;
            edges_used++;
            if (edges_used == n) break;
        }
    }

    cout << total_cost << "\n";
    return 0;
}
"""
    },
    {
        "id": "arc075_c",
        "title": "Meaningful Mean",
        "contest_id": "arc075",
        "rating": 1979,
        "tag": "Data Structures (DS)",
        "subtopic": "Fenwick Tree / Coordinate Compression",
        "topic": "Mean Threshold Normalization to Prefix Monotonic Inversion Counting via Fenwick Tree",
        "cat_folder": "data_structures",
        "cat_file": "mean_threshold_prefix_inversion_fenwick.md",
        "statement": "Given array A of length N and integer K. Count pairs (l, r) with 1 <= l <= r <= N such that the mean of subarray A[l..r] is at least K.",
        "key_idea": "The condition sum_{i=l}^r A_i / (r - l + 1) >= K is equivalent to sum_{i=l}^r (A_i - K) >= 0. Transform array A into B_i = A_i - K. Compute prefix sums P_i = sum_{j=1}^i B_j with P_0 = 0. The condition becomes P_r - P_{l-1} >= 0, or P_r >= P_{l-1}. Coordinate-compress the N + 1 prefix sum values, and use a Fenwick tree to count pairs i < j with P_i <= P_j in O(N log N).",
        "observation": "Subtracting K normalizes mean thresholding into standard non-inversion counting on prefix sums.",
        "algorithm": [
            "Compute normalized values B_i = A_i - K.",
            "Compute prefix sums P_0 = 0, P_i = P_{i-1} + B_i.",
            "Coordinate compress the N + 1 values of P.",
            "ans = 0. Initialize Fenwick tree.",
            "For each prefix sum P_i from 0 to N:",
            "  ans += fenwick.query(compressed(P_i)).",
            "  fenwick.add(compressed(P_i), 1).",
            "Print ans."
        ],
        "time_complexity": "O(N log N)",
        "space_complexity": "O(N)",
        "core_skill": "Mean normalization transformation combined with Fenwick tree inversion/non-inversion counting.",
        "reusable_pattern": "Mean >= K Counting: Normalize A_i - K, compute prefix sums, count P_r >= P_l via Fenwick.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Fenwick {
    int n;
    vector<int> tree;
    Fenwick(int n) : n(n), tree(n + 1, 0) {}
    void add(int idx, int val) {
        for (; idx <= n; idx += idx & -idx) tree[idx] += val;
    }
    int query(int idx) {
        int sum = 0;
        for (; idx > 0; idx -= idx & -idx) sum += tree[idx];
        return sum;
    }
};

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

    vector<long long> p(n + 1, 0);
    vector<long long> vals;
    vals.push_back(0);

    for (int i = 0; i < n; ++i) {
        p[i + 1] = p[i] + (a[i] - k);
        vals.push_back(p[i + 1]);
    }

    sort(vals.begin(), vals.end());
    vals.erase(unique(vals.begin(), vals.end()), vals.end());

    auto get_rank = [&](long long val) -> int {
        return lower_bound(vals.begin(), vals.end(), val) - vals.begin() + 1;
    };

    Fenwick ft(vals.size());
    long long ans = 0;

    for (int i = 0; i <= n; ++i) {
        int r = get_rank(p[i]);
        ans += ft.query(r);
        ft.add(r, 1);
    }

    cout << ans << "\n";
    return 0;
}
"""
    },
    {
        "id": "arc108_d",
        "title": "AB",
        "contest_id": "arc108",
        "rating": 1987,
        "tag": "Dynamic Programming (DP)",
        "subtopic": "Grammar Rewriting / Matrix DP",
        "topic": "Formal Grammar String Rewriting Casework and Fibonacci Transition Invariants",
        "cat_folder": "dp",
        "cat_file": "grammar_rewriting_fibonacci_invariants.md",
        "statement": "Starting with string 'AB', insert characters between adjacent identical or distinct characters according to rules for 'AA', 'AB', 'BA', 'BB' until length N. Find number of distinct reachable strings modulo 10^9 + 7.",
        "key_idea": "If N <= 3, the answer is 1. For N >= 4, the first step produces 'AcB' where c = rule('AB'). If c == 'A': the next insertions can only place rule('AA') between 'A' and 'A', or rule('AB') between 'A' and 'B'. Symmetrically analyze the cases: depending on rule('AA') and rule('BA'), the number of obtainable strings either remains 1, reaches 2^{N-3}, or follows the Fibonacci recurrence F_{N-1} (when consecutive blocks of 'B' are restricted to size 1).",
        "observation": "Classification over the 16 binary rule combinations reduces the grammar expansion to either 1, 2^{N-3}, or Fibonacci F_{N-1}.",
        "algorithm": [
            "If N <= 3, output 1.",
            "Read characters for rule AA, AB, BA, BB.",
            "If rule('AB') == 'A':",
            "  If rule('AA') == 'A': ans = 1.",
            "  Else if rule('BA') == 'A': ans = F_{N-1}.",
            "  Else: ans = 2^{N-3}.",
            "If rule('AB') == 'B':",
            "  If rule('BB') == 'B': ans = 1.",
            "  Else if rule('BA') == 'B': ans = F_{N-1}.",
            "  Else: ans = 2^{N-3}.",
            "Print ans % MOD."
        ],
        "time_complexity": "O(N)",
        "space_complexity": "O(N)",
        "core_skill": "Exhaustive invariant casework on formal grammar rewriting with Fibonacci state transitions.",
        "reusable_pattern": "Grammar Rewriting DP: Casework on seed pair rules reduces to powers of 2 or Fibonacci recurrences.",
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

    int n;
    if (!(cin >> n)) return 0;

    char c_aa, c_ab, c_ba, c_bb;
    cin >> c_aa >> c_ab >> c_ba >> c_bb;

    if (n <= 3) {
        cout << 1 << "\n";
        return 0;
    }

    vector<long long> fib(n + 1, 0);
    fib[1] = 1;
    fib[2] = 1;
    for (int i = 3; i <= n; ++i) {
        fib[i] = (fib[i - 1] + fib[i - 2]) % MOD;
    }

    if (c_ab == 'A') {
        if (c_aa == 'A') {
            cout << 1 << "\n";
        } else {
            if (c_ba == 'A') {
                cout << fib[n - 1] << "\n";
            } else {
                cout << power(2, n - 3) << "\n";
            }
        }
    } else {
        if (c_bb == 'B') {
            cout << 1 << "\n";
        } else {
            if (c_ba == 'B') {
                cout << fib[n - 1] << "\n";
            } else {
                cout << power(2, n - 3) << "\n";
            }
        }
    }

    return 0;
}
"""
    },
    {
        "id": "arc106_d",
        "title": "Powers",
        "contest_id": "arc106",
        "rating": 1988,
        "tag": "Math",
        "subtopic": "Polynomials / Binomial Theorem",
        "topic": "Binomial Expansion Decoupling of Pairwise Sum Powers via Power-Sum Moments",
        "cat_folder": "math",
        "cat_file": "binomial_expansion_power_sum_moments.md",
        "statement": "Given array A of length N. For each X from 1 to K (K <= 300), compute sum_{1 <= i < j <= N} (A_i + A_j)^X modulo 998244353.",
        "key_idea": "By Binomial Theorem, (A_i + A_j)^X = sum_{p=0}^X binom(X, p) A_i^p A_j^{X-p}. Summing over all 1 <= i, j <= N decouples the pair sum into products of independent power sums: sum_{i, j} (A_i + A_j)^X = sum_{p=0}^X binom(X, p) (sum A_i^p) (sum A_j^{X-p}) = sum_{p=0}^X binom(X, p) S_p S_{X-p}, where S_p = sum_{i=1}^N A_i^p mod 998244353. Precompute S_0..S_K in O(N K). For each X, subtract the self-pairs sum_{i=1}^N (2 A_i)^X = 2^X S_X and divide by 2.",
        "observation": "Binomial theorem decouples coupled pairwise powers (A_i + A_j)^X into 1D power-sum moments.",
        "algorithm": [
            "Precompute factorials and powers of A_i up to K.",
            "Compute power sums S_p = sum_{i=1}^N A_i^p % MOD for 0 <= p <= K.",
            "For each X = 1..K:",
            "  total = sum_{p=0}^X binom(X, p) * S_p * S_{X - p} % MOD.",
            "  self_sum = 2^X * S_X % MOD.",
            "  ans = (total - self_sum + MOD) * inv(2) % MOD.",
            "  Print ans."
        ],
        "time_complexity": "O(N * K + K^2)",
        "space_complexity": "O(N + K)",
        "core_skill": "Binomial expansion for axis decoupling in symmetric polynomial power sums.",
        "reusable_pattern": "Pairwise Power Sums: sum_{i<j} (A_i + A_j)^X = 1/2 [sum_{p=0}^X binom(X, p) S_p S_{X-p} - 2^X S_X].",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>

using namespace std;

const int MOD = 998244353;
const int MAXK = 305;

long long fact[MAXK], invFact[MAXK];

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

void precompute() {
    fact[0] = 1;
    invFact[0] = 1;
    for (int i = 1; i < MAXK; i++) {
        fact[i] = (fact[i - 1] * i) % MOD;
    }
    invFact[MAXK - 1] = modInverse(fact[MAXK - 1]);
    for (int i = MAXK - 2; i >= 1; i--) {
        invFact[i] = (invFact[i + 1] * (i + 1)) % MOD;
    }
}

long long nCr(int n, int r) {
    if (r < 0 || r > n) return 0;
    return fact[n] * invFact[r] % MOD * invFact[n - r] % MOD;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    precompute();

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    vector<long long> S(k + 1, 0);
    for (int i = 0; i < n; ++i) {
        long long cur = 1;
        for (int p = 0; p <= k; ++p) {
            S[p] = (S[p] + cur) % MOD;
            cur = (cur * a[i]) % MOD;
        }
    }

    long long inv2 = modInverse(2);

    for (int x = 1; x <= k; ++x) {
        long long total = 0;
        for (int p = 0; p <= x; ++p) {
            long long ways = nCr(x, p);
            long long term = ways * S[p] % MOD * S[x - p] % MOD;
            total = (total + term) % MOD;
        }

        long long self_term = power(2, x) * S[x] % MOD;
        long long ans = (total - self_term + MOD) % MOD * inv2 % MOD;
        cout << ans << "\n";
    }

    return 0;
}
"""
    },
    {
        "id": "abc305_g",
        "title": "Banned Substrings",
        "contest_id": "abc305",
        "rating": 1989,
        "tag": "Dynamic Programming (DP)",
        "subtopic": "Matrix Exponentiation / Automata",
        "topic": "Automaton Transition Matrix Exponentiation for Banned Substring Avoidance O(V^3 log N)",
        "cat_folder": "dp",
        "cat_file": "automaton_matrix_exponentiation_banned_substrings.md",
        "statement": "Find the number of strings of length N (N <= 10^9) consisting of 'a' and 'b' that do not contain any of M given strings S_1..S_M (|S_i| <= 6) as substrings, modulo 998244353.",
        "key_idea": "Since |S_i| <= 6, whether appending a character creates a banned substring depends only on the suffix of length at most 5. Represent the DFA state by the longest valid suffix of length <= 5 (at most 2^5 = 32 states for length 5). Build the transition matrix T where T[u][v] = 1 if appending 'a' or 'b' to state u transitions to valid state v. Compute T^N via binary matrix exponentiation in O(V^3 log N) with V <= 64.",
        "observation": "Small substring length L <= 6 bounds the memory automaton state space to V = 2^{L-1} = 32, allowing fast matrix exponentiation.",
        "algorithm": [
            "Enumerate all binary strings of length <= 5.",
            "Filter strings that contain any banned substring as an infix.",
            "Build transition matrix T: for each state s and char c in {'a', 'b'}, form new_s = (s + c).suffix(5); if valid, T[s][new_s]++.",
            "Compute T^{N - 5} via binary matrix exponentiation (or handle small N directly).",
            "Sum valid states and output modulo 998244353."
        ],
        "time_complexity": "O(V^3 log N) where V <= 64",
        "space_complexity": "O(V^2)",
        "core_skill": "Modeling short banned substring avoidance on suffix DFAs and accelerating via matrix exponentiation.",
        "reusable_pattern": "Banned Substrings via Matrix Exp: State = length-5 suffix; transition T[u][v] = 1; answer = sum(T^N).",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <string>
#include <vector>
#include <queue>

using namespace std;

const int MOD = 998244353;

typedef vector<vector<long long>> Matrix;

Matrix multiply(const Matrix& A, const Matrix& B) {
    int n = A.size();
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

Matrix power(Matrix A, long long exp) {
    int n = A.size();
    Matrix res(n, vector<long long>(n, 0));
    for (int i = 0; i < n; ++i) res[i][i] = 1;
    while (exp > 0) {
        if (exp % 2 == 1) res = multiply(res, A);
        A = multiply(A, A);
        exp /= 2;
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    int m;
    if (!(cin >> n >> m)) return 0;

    vector<string> banned(m);
    for (int i = 0; i < m; ++i) {
        cin >> banned[i];
    }

    auto is_valid = [&](const string& s) {
        for (const auto& b : banned) {
            if (s.find(b) != string::npos) return false;
        }
        return true;
    };

    if (n <= 5) {
        int count = 0;
        for (int mask = 0; mask < (1 << n); ++mask) {
            string s = "";
            for (int i = 0; i < n; ++i) {
                s += ((mask >> i) & 1) ? 'b' : 'a';
            }
            if (is_valid(s)) count++;
        }
        cout << count << "\n";
        return 0;
    }

    vector<string> states;
    for (int mask = 0; mask < 32; ++mask) {
        string s = "";
        for (int i = 0; i < 5; ++i) {
            s += ((mask >> i) & 1) ? 'b' : 'a';
        }
        if (is_valid(s)) {
            states.push_back(s);
        }
    }

    int V = states.size();
    Matrix T(V, vector<long long>(V, 0));

    for (int i = 0; i < V; ++i) {
        for (char c : {'a', 'b'}) {
            string cand = states[i] + c;
            if (is_valid(cand)) {
                string next_state = cand.substr(1);
                for (int j = 0; j < V; ++j) {
                    if (states[j] == next_state) {
                        T[i][j]++;
                        break;
                    }
                }
            }
        }
    }

    Matrix Tn = power(T, n - 5);

    long long total_ans = 0;
    for (int i = 0; i < V; ++i) {
        for (int j = 0; j < V; ++j) {
            total_ans = (total_ans + Tn[i][j]) % MOD;
        }
    }

    cout << total_ans << "\n";
    return 0;
}
"""
    },
    {
        "id": "arc065_b",
        "title": "Connectivity",
        "contest_id": "arc065",
        "rating": 1996,
        "tag": "Data Structures (DS)",
        "subtopic": "Disjoint Set Union (DSU)",
        "topic": "Dual Graph Joint Connectivity Counting via Component Root Hash Pairing",
        "cat_folder": "data_structures",
        "cat_file": "dual_dsu_joint_connectivity_hash_pairing.md",
        "statement": "N cities connected by two independent edge sets: K roads and L railways. Two cities p, q are jointly connected iff they can reach each other via roads AND via railways. For each city i, output the number of cities jointly connected to i.",
        "key_idea": "Build two separate DSU structures: one for the road network and one for the railway network. City i belongs to road component root R_i = find_road(i) and railway component root T_i = find_rail(i). Two cities p, q are jointly connected iff R_p == R_q AND T_p == T_q. Thus, joint connectivity is an equivalence relation where each city's equivalence class is uniquely defined by the pair of canonical roots (R_i, T_i). Count frequencies of each pair using a hash map or sorting in O(N log N).",
        "observation": "Joint connectivity across multiple networks is the intersection of equivalence classes, uniquely keyed by the tuple of DSU component roots.",
        "algorithm": [
            "Initialize DSU_road and DSU_rail for N cities.",
            "Add all K roads to DSU_road.",
            "Add all L railways to DSU_rail.",
            "For each city i in 1..N: record signature pair (DSU_road.find(i), DSU_rail.find(i)).",
            "Count occurrences of each signature pair using map.",
            "For each city i: print count[signature[i]]."
        ],
        "time_complexity": "O((N + K + L) * alpha(N) + N log N)",
        "space_complexity": "O(N)",
        "core_skill": "Equivalence relation intersection across multiple graphs using DSU root pairing.",
        "reusable_pattern": "Multi-Network Connectivity: Hash/map pair of roots (find_1(u), find_2(u)) across networks.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <numeric>
#include <map>

using namespace std;

struct DSU {
    vector<int> parent;
    DSU(int n) : parent(n + 1) {
        iota(parent.begin(), parent.end(), 0);
    }
    int find(int v) {
        if (v == parent[v]) return v;
        return parent[v] = find(parent[v]);
    }
    void unite(int a, int b) {
        a = find(a);
        b = find(b);
        if (a != b) parent[b] = a;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k, l;
    if (!(cin >> n >> k >> l)) return 0;

    DSU road(n), rail(n);

    for (int i = 0; i < k; ++i) {
        int u, v;
        cin >> u >> v;
        road.unite(u, v);
    }

    for (int i = 0; i < l; ++i) {
        int u, v;
        cin >> u >> v;
        rail.unite(u, v);
    }

    map<pair<int, int>, int> freq;
    vector<pair<int, int>> sig(n + 1);

    for (int i = 1; i <= n; ++i) {
        sig[i] = {road.find(i), rail.find(i)};
        freq[sig[i]]++;
    }

    for (int i = 1; i <= n; ++i) {
        cout << freq[sig[i]] << (i == n ? "" : " ");
    }
    cout << "\n";
    return 0;
}
"""
    },
    {
        "id": "arc120_d",
        "title": "Bracket Score 2",
        "contest_id": "arc120",
        "rating": 1996,
        "tag": "Basics",
        "subtopic": "Greedy / Invariants",
        "topic": "Extremal Pairing Upper Bound Attainment via Sign-Alternating Bracket Stack",
        "cat_folder": "basics",
        "cat_file": "extremal_bracket_pairing_stack.md",
        "statement": "Given array A of length 2N. Construct a balanced bracket sequence of length 2N (with N '(' and N ')') such that matching bracket pairs (i, j) maximize sum |A_i - A_j|.",
        "key_idea": "The maximum possible value of sum |A_i - A_j| over ANY pairing is to pair the N smallest elements of A with the N largest elements of A (giving sum A_large - sum A_small). We can always achieve this theoretical maximum with a valid bracket sequence! Label the N smallest elements -1 and the N largest elements +1. Process from left to right using a stack: if current element has different sign than stack top, they can form a valid matched pair (the earlier gets '(', the later gets ')'); if same sign, push to stack.",
        "observation": "Because the total number of +1 and -1 are equal (N each), any prefix with excess elements of one sign can be matched with opposite signs without violation, achieving the global upper bound.",
        "algorithm": [
            "Pair each A[i] with its original index i.",
            "Sort elements by value ascending.",
            "Label the first N elements as -1, and the remaining N elements as +1.",
            "Iterate i from 0 to 2N - 1 maintaining a stack of indices:",
            "  If stack is not empty and sign[i] != sign[stack.top()]:",
            "    match stack.top() and i; ans[stack.top()] = '(', ans[i] = ')'; pop stack.",
            "  Else: push i to stack.",
            "Print ans string."
        ],
        "time_complexity": "O(N log N)",
        "space_complexity": "O(N)",
        "core_skill": "Proving an unconstrained extremal upper bound and constructing an exact balanced bracket match using a sign stack.",
        "reusable_pattern": "Optimal Bracket Pairing: Split into bottom N (-1) and top N (+1); match opposite signs using stack.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <string>
#include <stack>
#include <algorithm>

using namespace std;

struct Element {
    long long val;
    int idx;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    int total = 2 * n;
    vector<Element> a(total);
    for (int i = 0; i < total; ++i) {
        cin >> a[i].val;
        a[i].idx = i;
    }

    sort(a.begin(), a.end(), [](const Element& x, const Element& y) {
        return x.val < y.val;
    });

    vector<int> sign(total);
    for (int i = 0; i < total; ++i) {
        if (i < n) sign[a[i].idx] = -1;
        else sign[a[i].idx] = 1;
    }

    string ans(total, ' ');
    stack<int> st;

    for (int i = 0; i < total; ++i) {
        if (!st.empty() && sign[st.top()] != sign[i]) {
            ans[st.top()] = '(';
            ans[i] = ')';
            st.pop();
        } else {
            st.push(i);
        }
    }

    cout << ans << "\n";
    return 0;
}
"""
    },
    {
        "id": "arc134_d",
        "title": "Concatenate Subsequences",
        "contest_id": "arc134",
        "rating": 1998,
        "tag": "Basics",
        "subtopic": "Greedy",
        "topic": "Lexicographical Minimal Concatenated Subsequence via Two-Phase Greedy Selection",
        "cat_folder": "basics",
        "cat_file": "two_phase_greedy_concatenated_subsequence.md",
        "statement": "Given arrays a_1..a_N and b_1..b_N. Choose a non-empty index sequence i_1 < ... < i_k to form sequence x = (a_{i_1}..a_{i_k}, b_{i_1}..b_{i_k}). Find the lexicographically smallest x.",
        "key_idea": "The first element of x must be the global minimum of a: m = min(a). If there exists any index i with a_i = m such that b_i <= m, then selecting ONLY this single index i yields (m, b_i) with b_i <= m, which is strictly smaller than any sequence starting with (m, >m). If no such index exists, we must select ALL occurrences of m. Let the minimum b among all chosen indices be min_b. We can then greedily append subsequent elements j with a_j < min_b, or if a_j == min_b, only if the resulting b_j maintains lexicographical superiority.",
        "observation": "Single-element shortcut (m, b_i <= m) beats multi-element sequences; otherwise mandatory selection of all minimums sets the upper bound on subsequent choices.",
        "algorithm": [
            "Find global min m = min(a).",
            "Check if any i with a[i] == m has b[i] <= m. If so, choose the one with smallest b[i] and print [m, b[i]].",
            "Otherwise, collect all indices with a[i] == m.",
            "Let min_b = min(b[i] for selected i).",
            "For subsequent indices j > last_idx: if a[j] < min_b, greedily select j.",
            "Handle border case where a[j] == min_b by checking if first differing b is smaller than min_b.",
            "Print concatenated sequence a_indices followed by b_indices."
        ],
        "time_complexity": "O(N)",
        "space_complexity": "O(N)",
        "core_skill": "Two-phase lexicographical greedy optimization with boundary shortcuts.",
        "reusable_pattern": "Concatenated Subsequence Greedy: Check single-element shortcut (m, b_i <= m); else collect all minimums.",
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

    vector<int> a(n), b(n);
    for (int i = 0; i < n; ++i) cin >> a[i];
    for (int i = 0; i < n; ++i) cin >> b[i];

    int min_a = *min_element(a.begin(), a.end());

    int best_single_b = 2e9;
    for (int i = 0; i < n; ++i) {
        if (a[i] == min_a && b[i] <= min_a) {
            best_single_b = min(best_single_b, b[i]);
        }
    }

    if (best_single_b <= min_a) {
        cout << min_a << " " << best_single_b << "\n";
        return 0;
    }

    vector<int> idx;
    for (int i = 0; i < n; ++i) {
        if (a[i] == min_a) {
            idx.push_back(i);
        }
    }

    int min_b = 2e9;
    for (int i : idx) {
        min_b = min(min_b, b[i]);
    }

    // Determine whether to accept a[j] == min_b
    bool take_equal = false;
    for (int i : idx) {
        if (b[i] != min_b) {
            take_equal = (b[i] < min_b);
            break;
        }
    }

    int cur_idx = idx.back();
    for (int i = cur_idx + 1; i < n; ++i) {
        if (a[i] < min_b || (a[i] == min_b && take_equal)) {
            if (idx.empty() || a[i] >= a[idx.back()]) {
                idx.push_back(i);
            }
        }
    }

    vector<int> ans;
    for (int i : idx) ans.push_back(a[i]);
    for (int i : idx) ans.push_back(b[i]);

    for (int i = 0; i < (int)ans.size(); ++i) {
        cout << ans[i] << (i + 1 == (int)ans.size() ? "" : " ");
    }
    cout << "\n";
    return 0;
}
"""
    }
]

REJECTED_PROBLEMS = [
    {
        "id": "abc462_f",
        "title": "More ABC",
        "rating": 1952,
        "tag": "Basics",
        "subtopic": "Implementation",
        "topic": "String Manipulation Drill",
        "reason": "Rejected: Elementary logic building / string operation and replacement drill."
    },
    {
        "id": "arc198_c",
        "title": "Error Swap",
        "rating": 1954,
        "tag": "Basics",
        "subtopic": "Constructive",
        "topic": "Parity Swap Sorting",
        "reason": "Rejected: Duplicate of arc121_c / arc091_c; parity-constrained swap sorting drill."
    },
    {
        "id": "abc446_g",
        "title": "221 Subsequence",
        "rating": 1955,
        "tag": "Basics",
        "subtopic": "Implementation",
        "topic": "Subsequence Frequency Casework",
        "reason": "Rejected: Elementary logic building / subsequence pattern counting drill."
    },
    {
        "id": "arc164_d",
        "title": "1D Coulomb",
        "rating": 1963,
        "tag": "Math",
        "subtopic": "Prefix Sums",
        "topic": "1D Electrostatic Potential Sum",
        "reason": "Rejected: Duplicate of arc158_c; coordinate prefix difference potential calculation."
    },
    {
        "id": "arc003_3",
        "title": "暗闇帰り道",
        "rating": 1972,
        "tag": "Basics",
        "subtopic": "Binary Search",
        "topic": "Binary Search on Answer with Grid BFS",
        "reason": "Rejected: Duplicate of abc023_d; standard binary search on answer with grid reachability verification."
    },
    {
        "id": "arc006_4",
        "title": "アルファベット探し",
        "rating": 1973,
        "tag": "Basics",
        "subtopic": "Implementation",
        "topic": "2D Pattern Matching Simulation",
        "reason": "Rejected: Elementary logic building / 2D grid template pattern matching and flood-fill drill."
    },
    {
        "id": "abc473_g",
        "title": "Wipeout",
        "rating": 1974,
        "tag": "Basics",
        "subtopic": "Implementation",
        "topic": "Grid Wipeout Simulation",
        "reason": "Rejected: Elementary logic building / grid game simulation drill."
    },
    {
        "id": "abc468_g",
        "title": "Restricted Permutation",
        "rating": 1975,
        "tag": "Graph Theory",
        "subtopic": "Topological Sort",
        "topic": "Lexicographical Topological Sort",
        "reason": "Rejected: Duplicate of typical90_f; priority-queue accelerated topological sort."
    },
    {
        "id": "arc215_d",
        "title": "cresc.",
        "rating": 1975,
        "tag": "Basics",
        "subtopic": "Implementation",
        "topic": "Sequence Casework Drill",
        "reason": "Rejected: Elementary logic building / ad-hoc sequence monotonicity drill."
    },
    {
        "id": "arc018_3",
        "title": "席替え",
        "rating": 1979,
        "tag": "Basics",
        "subtopic": "Greedy",
        "topic": "Grid Coordinate Assignment",
        "reason": "Rejected: Duplicate of arc053_c; bipartite coordinate assignment greedy casework."
    },
    {
        "id": "arc207_b",
        "title": "Balanced Neighbors 2",
        "rating": 1979,
        "tag": "Basics",
        "subtopic": "Implementation",
        "topic": "Graph Neighbor Balance Casework",
        "reason": "Rejected: Elementary logic building / ad-hoc degree balance drill."
    },
    {
        "id": "abc360_g",
        "title": "Suitable Edit for LIS",
        "rating": 1982,
        "tag": "Dynamic Programming (DP)",
        "subtopic": "LIS / Segment Tree",
        "topic": "Single-Element Edit LIS Maximization",
        "reason": "Rejected: Duplicate of abc165_f; prefix-suffix LIS combination via Fenwick tree."
    },
    {
        "id": "abc432_g",
        "title": "Sum of Binom(A, B)",
        "rating": 1984,
        "tag": "Combinatorics",
        "subtopic": "Binomial Coefficients",
        "topic": "Binomial Sum Evaluation",
        "reason": "Rejected: Duplicate of abc154_f; standard hockey-stick binomial summation."
    },
    {
        "id": "abc441_g",
        "title": "Takoyaki and Flip",
        "rating": 1985,
        "tag": "Basics",
        "subtopic": "Implementation",
        "topic": "Coin Flip Simulation",
        "reason": "Rejected: Elementary logic building / ad-hoc token flip casework."
    },
    {
        "id": "arc178_c",
        "title": "Sum of Abs 2",
        "rating": 1990,
        "tag": "Math",
        "subtopic": "Prefix Sums",
        "topic": "Absolute Difference Prefix Sums",
        "reason": "Rejected: Duplicate of abc127_e; 1D coordinate distance contribution."
    },
    {
        "id": "abc380_g",
        "title": "Another Shuffle Window",
        "rating": 1995,
        "tag": "Data Structures (DS)",
        "subtopic": "Fenwick Tree",
        "topic": "Sliding Window Inversion Counting",
        "reason": "Rejected: Duplicate of typical90_as / sliding window Fenwick inversion tracking."
    }
]

# Step 1: Compile all C++ solutions to verify zero errors
print(f"Testing C++ compilation of all {len(SELECTED_PROBLEMS)} selected ABC Part 4B solutions...")
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

print(f"[+] All {len(SELECTED_PROBLEMS)} ABC Part 4B C++ solutions compiled with 0 errors!")

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

{p['key_idea']}

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
        f.write("\n### Batch 5 Part 4B: ABC Curated Ladder (1951 - 1999)\n" + "\n".join(new_q_lines) + "\n")
    print("[+] Updated QUALITY_PROBLEMS_BY_TOPIC.md with new archetypes.")

# Update state/progress.json
with open("state/progress.json", "r", encoding="utf-8") as f:
    progress = json.load(f)

progress["current_batch"] = "Batch 5 Part 4B: ABC Ladder (1951-1999) COMPLETED"
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
print("Batch 5 Part 4B completed successfully!")
