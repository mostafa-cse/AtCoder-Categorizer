import os, sys, json, subprocess

sys.stdout.reconfigure(encoding='utf-8')

print("=" * 75)
print("      PROCESSING BATCH 6 PART 4B: ABC / ARC CURATED LADDER (2164 - 2177)")
print("=" * 75)

# Load existing progress
with open('state/progress.json', 'r', encoding='utf-8') as f:
    progress = json.load(f)

completed_ids = set(progress.get('completed_problem_ids', []))
evaluated_ids = set(progress.get('evaluated_problems', []))

# Problem definitions for Part 4B
problems_meta = [
    {
        'id': 'arc021_3',
        'contest_id': 'arc021',
        'title': 'C. 増築王高橋君',
        'rating': 2164,
        'domain': 'Basics',
        'domain_folder': 'basics',
        'subtopic': 'Leveraging Monotonicity',
        'topic': 'Binary Search',
        'cat_file': 'categories/basics/binary_search_marginal_cost_threshold.md',
        'key_idea': 'Find the minimum cost to perform K building upgrades where building i starts at price A_i and increases by D_i per upgrade. The upgrade costs for building i form an arithmetic progression A_i + m*D_i. Binary search on the marginal upgrade cost threshold X. Upgrades with cost strictly below X are unconditionally taken, and the remaining upgrades needed to reach K are purchased at price exactly X.',
        'observation': 'As marginal cost X increases, the number of available upgrades costing <= X is monotonically non-decreasing: sum_i max(0, (X - A_i)/D_i + 1). Binary searching for the smallest integer X where the total count is >= K isolates the K-th cheapest upgrade. Summing the closed-form arithmetic progressions c_i*A_i + c_i*(c_i-1)/2*D_i for all c_i upgrades with cost < X takes O(N) time.',
        'algorithm': [
            'Binary search on the marginal cost threshold X in the range [1, 2*10^14].',
            'In the predicate, count total upgrades costing <= X: count(X) = sum_i max(0LL, (X - A_i) / D_i + 1). If count >= K, set best_X = X and search lower.',
            'After finding best_X, count and sum costs of all upgrades strictly less than best_X using the arithmetic progression sum for each building.',
            'Add (K - taken_upgrades) * best_X to account for the remaining upgrades at cost exactly best_X.'
        ],
        'time_complexity': 'O(N log(max_cost))',
        'space_complexity': 'O(N)',
        'code': r'''#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long K;
    int N;
    if (!(cin >> K >> N)) return 0;

    vector<long long> A(N), D(N);
    for (int i = 0; i < N; ++i) {
        cin >> A[i] >> D[i];
    }

    long long low = 1, high = 2e14, best_X = high;
    while (low <= high) {
        long long mid = low + (high - low) / 2;
        long long cnt = 0;
        for (int i = 0; i < N; ++i) {
            if (mid >= A[i]) {
                cnt += (mid - A[i]) / D[i] + 1;
                if (cnt >= K) break;
            }
        }
        if (cnt >= K) {
            best_X = mid;
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }

    long long total_cost = 0;
    long long total_upgrades = 0;
    for (int i = 0; i < N; ++i) {
        if (best_X - 1 >= A[i]) {
            long long c = (best_X - 1 - A[i]) / D[i] + 1;
            total_upgrades += c;
            total_cost += c * A[i] + (c * (c - 1) / 2) * D[i];
        }
    }

    total_cost += (K - total_upgrades) * best_X;
    cout << total_cost << "\n";
    return 0;
}'''
    },
    {
        'id': 'arc194_d',
        'contest_id': 'arc194',
        'title': 'D. Reverse Brackets',
        'rating': 2164,
        'domain': 'Miscellaneous',
        'domain_folder': 'miscellaneous',
        'subtopic': 'General',
        'topic': 'Tree Isomorphism',
        'cat_file': 'categories/miscellaneous/tree_isomorphism_bracket_multinomial_counting.md',
        'key_idea': 'Given a valid parenthesis sequence S, reversing balanced subsegments bijects to rooted ordered trees where contiguous reversals generate the full symmetric group of sibling subtrees. Distinct reachable strings correspond to all valid permutations of sibling subtrees, counted via tree isomorphism hashing and multinomial coefficients.',
        'observation': 'Enclosing S as ( + S + ) forms a single rooted tree where each matched pair () is a node and nested pairs are children. Consecutive reversals of child subsegments allow arbitrary reordering of a node\'s children. If node u has k children with isomorphism counts c_1, ..., c_m, the number of distinct ordered sequences is k! / (c_1! * ... * c_m!). The total count is the product of these multinomial coefficients across all vertices.',
        'algorithm': [
            'Parse the bracket sequence into an explicit rooted tree with parent-child adjacency.',
            'Traverse bottom-up (post-order DFS) to compute a canonical isomorphism hash/ID for each subtree by sorting the IDs of its children and memoizing in a map<vector<int>, int>.',
            'At each node with k children, count multiplicities of isomorphic child subtree IDs, multiplying the answer by k! / prod(c_i!).',
            'Compute all factorials and modular inverses under modulo 998244353.'
        ],
        'time_complexity': 'O(N log N)',
        'space_complexity': 'O(N)',
        'code': r'''#include <iostream>
#include <string>
#include <vector>
#include <map>
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

    int N;
    if (!(cin >> N)) return 0;
    string S;
    cin >> S;

    string s = "(" + S + ")";
    int total_chars = (int)s.size();

    vector<long long> fact(total_chars + 1, 1), inv(total_chars + 1, 1);
    for (int i = 1; i <= total_chars; ++i) fact[i] = (fact[i - 1] * i) % MOD;
    inv[total_chars] = modInverse(fact[total_chars]);
    for (int i = total_chars - 1; i >= 0; --i) inv[i] = (inv[i + 1] * (i + 1)) % MOD;

    vector<vector<int>> adj;
    adj.push_back({});
    vector<int> stack = {0};

    for (int i = 1; i < total_chars; ++i) {
        if (s[i] == '(') {
            int new_id = (int)adj.size();
            adj.push_back({});
            adj[stack.back()].push_back(new_id);
            stack.push_back(new_id);
        } else {
            stack.pop_back();
        }
    }

    map<vector<int>, int> memo;
    long long ans = 1;

    auto dfs = [&](auto& self, int u) -> int {
        vector<int> child_labels;
        for (int v : adj[u]) {
            child_labels.push_back(self(self, v));
        }
        int k = (int)child_labels.size();
        sort(child_labels.begin(), child_labels.end());

        long long term = fact[k];
        int count = 0;
        for (int i = 0; i < k; ++i) {
            count++;
            if (i + 1 == k || child_labels[i] != child_labels[i + 1]) {
                term = (term * inv[count]) % MOD;
                count = 0;
            }
        }
        ans = (ans * term) % MOD;

        if (memo.find(child_labels) == memo.end()) {
            int new_label = (int)memo.size() + 1;
            memo[child_labels] = new_label;
        }
        return memo[child_labels];
    };

    dfs(dfs, 0);
    cout << ans << "\n";
    return 0;
}'''
    },
    {
        'id': 'arc219_e',
        'contest_id': 'arc219',
        'title': 'E. Equal Distribution',
        'rating': 2164,
        'domain': 'Graph Theory',
        'domain_folder': 'graph_theory',
        'subtopic': 'Hamiltonian Path',
        'topic': 'Hamiltonian Path and Cycle',
        'cat_file': 'categories/graph_theory/hamiltonian_snake_cycle_circular_discrete_ivt.md',
        'key_idea': 'Partition a 2H x 2W grid containing 2HW strawberries into two connected regions A and B of size 2HW each containing exactly HW strawberries. Construct a Hamiltonian cycle on the 2H x 2W grid; any contiguous subsegment of length 2HW forms a connected path whose complement is also connected. By the discrete intermediate value theorem, a circular arc of length 2HW with exactly HW strawberries always exists.',
        'observation': 'A standard snake Hamiltonian cycle visits columns in alternating up/down directions on rows 1..2H-1, then returns along row 0. On this cycle of length 4HW, let f(i) be the number of strawberries in the arc of length 2HW starting at cell i. Since f(i + 2HW) = 2HW - f(i) and f changes by at most 1 between adjacent starting points, by the discrete IVT there must be an index where f(i) = HW.',
        'algorithm': [
            'Construct a Hamiltonian cycle of length 4HW on the 2H x 2W grid: snake down columns 2j and up columns 2j+1 on rows 1..2H-1, then return right-to-left along row 0.',
            'Represent the strawberry presence along the cycle as a binary circular array of length 4HW.',
            'Compute the sliding window sum of length 2HW. Find a starting index start where the strawberry sum is exactly HW.',
            'Color the 2HW cells along the cycle starting at start with A, and color the remaining 2HW cells with B.'
        ],
        'time_complexity': 'O(H * W) per testcase',
        'space_complexity': 'O(H * W)',
        'code': r'''#include <iostream>
#include <vector>
#include <string>

using namespace std;

void solve_case() {
    int H, W;
    if (!(cin >> H >> W)) return;
    int R = 2 * H, C = 2 * W;
    vector<string> S(R);
    for (int i = 0; i < R; ++i) cin >> S[i];

    vector<pair<int, int>> cycle;
    cycle.reserve(R * C);
    for (int j = 0; j < W; ++j) {
        int col1 = 2 * j;
        int col2 = 2 * j + 1;
        for (int r = 1; r < R; ++r) cycle.push_back({r, col1});
        for (int r = R - 1; r >= 1; --r) cycle.push_back({r, col2});
    }
    for (int c = C - 1; c >= 0; --c) {
        cycle.push_back({0, c});
    }

    int N = R * C;
    int L = 2 * H * W;
    vector<int> val(2 * N);
    for (int i = 0; i < N; ++i) {
        val[i] = (S[cycle[i].first][cycle[i].second] == 'o' ? 1 : 0);
        val[i + N] = val[i];
    }

    int cur = 0;
    for (int i = 0; i < L; ++i) cur += val[i];

    int target = H * W;
    int start = -1;
    if (cur == target) {
        start = 0;
    } else {
        for (int i = 1; i < N; ++i) {
            cur += val[i + L - 1] - val[i - 1];
            if (cur == target) {
                start = i;
                break;
            }
        }
    }

    vector<string> res(R, string(C, 'B'));
    for (int j = 0; j < L; ++j) {
        auto [r, c] = cycle[(start + j) % N];
        res[r][c] = 'A';
    }

    for (int i = 0; i < R; ++i) {
        cout << res[i] << "\n";
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    if (cin >> T) {
        while (T--) solve_case();
    }
    return 0;
}'''
    },
    {
        'id': 'soundhound2018_summer_qual_e',
        'contest_id': 'soundhound2018_summer_qual',
        'title': 'E. + Graph',
        'rating': 2164,
        'domain': 'Graph Theory',
        'domain_folder': 'graph_theory',
        'subtopic': 'Graph Traversal',
        'topic': 'Depth First Search (DFS)',
        'cat_file': 'categories/graph_theory/edge_sum_linear_system_bipartite_odd_cycle.md',
        'key_idea': 'Determine the number of positive integer vertex labelings on a connected graph such that for every edge (u, v), x_u + x_v = s_e. Fix x_1 = t. Every vertex value x_v is parameterized as sgn[v] * t + C[v]. An odd cycle produces an equation fixing t to a unique integer; a bipartite graph yields a continuous bounding interval [t_min, t_max] of valid positive integers.',
        'observation': 'Traversing a spanning tree from root 1, edge x_u + x_v = s implies x_v = -sgn[u]*t + (s - C[u]), forcing sgn[v] = -sgn[u]. Non-tree edges between same-sign vertices form an odd cycle: sgn[u]*t + C[u] + sgn[v]*t + C[v] = s, uniquely solving for t. Non-tree edges between opposite-sign vertices must satisfy C[u] + C[v] = s. For bipartite graphs, x_v >= 1 imposes lower bounds t >= 1 - C[v] (when sgn = +1) and upper bounds t <= C[v] - 1 (when sgn = -1).',
        'algorithm': [
            'Run BFS/DFS from vertex 1 with sgn[1] = 1, C[1] = 0.',
            'For every traversed edge (u, v, s): if v unvisited, assign sgn[v] = -sgn[u], C[v] = s - C[u].',
            'If v already visited with sgn[v] == sgn[u]: solve 2*sgn[u]*t = s - C[u] - C[v]. Check divisibility and consistency with any previously fixed t.',
            'If v already visited with sgn[v] != sgn[u]: check consistency C[u] + C[v] == s. If violated, output 0.',
            'If t is uniquely fixed: verify t > 0 and sgn[v]*t + C[v] > 0 for all v; output 1 if valid, 0 otherwise.',
            'If no odd cycle: compute L = max_{sgn=1}(1 - C[v]) and R = min_{sgn=-1}(C[v] - 1). Output max(0LL, R - L + 1).'
        ],
        'time_complexity': 'O(N + M)',
        'space_complexity': 'O(N + M)',
        'code': r'''#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    struct Edge {
        int to;
        long long s;
    };
    vector<vector<Edge>> adj(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v;
        long long s;
        cin >> u >> v >> s;
        adj[u].push_back({v, s});
        adj[v].push_back({u, s});
    }

    vector<int> sgn(n + 1, 0);
    vector<long long> C(n + 1, 0);
    vector<bool> visited(n + 1, false);

    sgn[1] = 1;
    C[1] = 0;
    visited[1] = true;

    queue<int> q;
    q.push(1);
    long long fixed_t = -1;
    bool has_fixed = false;

    while (!q.empty()) {
        int u = q.front();
        q.pop();

        for (auto& e : adj[u]) {
            int v = e.to;
            long long s = e.s;
            if (!visited[v]) {
                visited[v] = true;
                sgn[v] = -sgn[u];
                C[v] = s - C[u];
                q.push(v);
            } else {
                if (sgn[v] != -sgn[u]) {
                    long long diff = s - C[u] - C[v];
                    long long denom = 2LL * sgn[u];
                    if (diff % denom != 0) {
                        cout << 0 << "\n";
                        return 0;
                    }
                    long long t_cand = diff / denom;
                    if (has_fixed && fixed_t != t_cand) {
                        cout << 0 << "\n";
                        return 0;
                    }
                    has_fixed = true;
                    fixed_t = t_cand;
                } else {
                    if (C[v] != s - C[u]) {
                        cout << 0 << "\n";
                        return 0;
                    }
                }
            }
        }
    }

    if (has_fixed) {
        if (fixed_t <= 0) {
            cout << 0 << "\n";
            return 0;
        }
        for (int i = 1; i <= n; ++i) {
            long long val = (long long)sgn[i] * fixed_t + C[i];
            if (val <= 0) {
                cout << 0 << "\n";
                return 0;
            }
        }
        cout << 1 << "\n";
    } else {
        long long L = 1, R = 1e18;
        for (int i = 1; i <= n; ++i) {
            if (sgn[i] == 1) {
                L = max(L, 1LL - C[i]);
            } else {
                R = min(R, C[i] - 1LL);
            }
        }
        cout << max(0LL, R - L + 1) << "\n";
    }

    return 0;
}'''
    },
    {
        'id': 'abc346_g',
        'contest_id': 'abc346',
        'title': 'G. Alone',
        'rating': 2166,
        'domain': 'Data Structures (DS)',
        'domain_folder': 'data_structures',
        'subtopic': 'Segment Tree',
        'topic': 'Segment Tree (Point Update Range Query)',
        'cat_file': 'categories/data_structures/rectangle_union_sweep_line_segment_tree.md',
        'key_idea': 'Find the number of pairs (L, R) such that at least one value appears uniquely in A[L..R]. For each occurrence p_k of value x, it is unique in A[L..R] iff p_{k-1} < L <= p_k and p_k <= R < p_{k+1}. The problem reduces to finding the area of the union of axis-aligned rectangles [p_{k-1}+1, p_k] x [p_k, p_{k+1}-1] via sweep-line and segment tree.',
        'observation': 'Each occurrence generates an independent rectangle of valid (L, R) coordinates. The union of these rectangles covers all valid pairs. Sweeping L from 1 to N, we activate and deactivate intervals [R1, R2] on a segment tree tracking min coverage and zero-count. The number of covered R values at each step L is N - (zero_count if min == 0 else 0).',
        'algorithm': [
            'For each distinct value x, collect occurrence indices p_0=0, p_1, ..., p_m, p_{m+1}=N+1.',
            'For each occurrence p_k, create interval addition +1 at L = p_{k-1} + 1 on [p_k, p_{k+1} - 1] and removal -1 at L = p_k + 1.',
            'Maintain coverage on [1, N] using a lazy segment tree storing minimum value and count of minimums.',
            'Iterate L from 1 to N: apply all segment updates for L, then add the count of covered positions (N - zero_count) to the answer.'
        ],
        'time_complexity': 'O(N log N)',
        'space_complexity': 'O(N)',
        'code': r'''#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct SegTree {
    int n;
    vector<int> mn, cnt, lazy;
    SegTree(int n) : n(n), mn(4 * (n + 1)), cnt(4 * (n + 1)), lazy(4 * (n + 1)) {
        build(1, 1, n);
    }
    void build(int node, int l, int r) {
        mn[node] = 0;
        cnt[node] = r - l + 1;
        lazy[node] = 0;
        if (l == r) return;
        int mid = (l + r) / 2;
        build(2 * node, l, mid);
        build(2 * node + 1, mid + 1, r);
    }
    void apply(int node, int val) {
        mn[node] += val;
        lazy[node] += val;
    }
    void push(int node) {
        if (lazy[node] != 0) {
            apply(2 * node, lazy[node]);
            apply(2 * node + 1, lazy[node]);
            lazy[node] = 0;
        }
    }
    void pull(int node) {
        mn[node] = min(mn[2 * node], mn[2 * node + 1]);
        cnt[node] = 0;
        if (mn[2 * node] == mn[node]) cnt[node] += cnt[2 * node];
        if (mn[2 * node + 1] == mn[node]) cnt[node] += cnt[2 * node + 1];
    }
    void update(int node, int l, int r, int ql, int qr, int val) {
        if (ql <= l && r <= qr) {
            apply(node, val);
            return;
        }
        push(node);
        int mid = (l + r) / 2;
        if (ql <= mid) update(2 * node, l, mid, ql, qr, val);
        if (qr > mid) update(2 * node + 1, mid + 1, r, ql, qr, val);
        pull(node);
    }
    int get_covered() {
        return n - (mn[1] == 0 ? cnt[1] : 0);
    }
};

struct Event {
    int r1, r2, val;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    if (!(cin >> N)) return 0;
    vector<int> A(N + 1);
    vector<vector<int>> pos(N + 1);
    for (int i = 1; i <= N; ++i) {
        cin >> A[i];
        pos[A[i]].push_back(i);
    }

    vector<vector<Event>> events(N + 2);
    for (int x = 1; x <= N; ++x) {
        int m = (int)pos[x].size();
        for (int k = 0; k < m; ++k) {
            int p_prev = (k > 0 ? pos[x][k - 1] : 0);
            int p_curr = pos[x][k];
            int p_next = (k + 1 < m ? pos[x][k + 1] : N + 1);
            int l1 = p_prev + 1, l2 = p_curr;
            int r1 = p_curr, r2 = p_next - 1;
            if (l1 <= l2 && r1 <= r2) {
                events[l1].push_back({r1, r2, 1});
                events[l2 + 1].push_back({r1, r2, -1});
            }
        }
    }

    SegTree st(N);
    long long ans = 0;
    for (int l = 1; l <= N; ++l) {
        for (auto& e : events[l]) {
            st.update(1, 1, N, e.r1, e.r2, e.val);
        }
        ans += st.get_covered();
    }

    cout << ans << "\n";
    return 0;
}'''
    },
    {
        'id': 'abc408_g',
        'contest_id': 'abc408',
        'title': 'G. A/B < p/q < C/D',
        'rating': 2167,
        'domain': 'Miscellaneous',
        'domain_folder': 'miscellaneous',
        'subtopic': 'General',
        'topic': 'Stern-Brocot Tree and Rational Approximation',
        'cat_file': 'categories/miscellaneous/stern_brocot_simplest_fraction_euclidean_reduction.md',
        'key_idea': 'Given positive integers A, B, C, D with A/B < C/D, find the smallest denominator q such that there exists an integer p with A/B < p/q < C/D. Solved in O(log(min(B, D))) using the Stern-Brocot Euclidean mediant reduction / continued fractions.',
        'observation': 'If floor(A/B) + 1 < C/D, an integer exists strictly between the fractions, so q = 1. Otherwise, floor(A/B) = k. Subtracting k gives 0 <= (A - kB)/B < p\'/q < (C - kD)/D <= 1. Inverting the inequality yields D/(C - kD) < q/p\' < B/(A - kB), which recursively asks for the simplest fraction (minimal numerator q) strictly between the inverted bounds.',
        'algorithm': [
            'Define recursive function find_pq(A, B, C, D) returning (p, q).',
            'Let k = A / B. If (k + 1) * D < C, return (k + 1, 1).',
            'If A == k * B, return (k * q + 1, q) where q = D / (C - k*D) + 1.',
            'Otherwise, recursively compute (q, p\') = find_pq(D, C - k*D, B, A - k*B). Return (k * q + p\', q).',
            'Use __int128 to prevent overflow during intermediate operations.'
        ],
        'time_complexity': 'O(log(min(B, D))) per testcase',
        'space_complexity': 'O(log(min(B, D)))',
        'code': r'''#include <iostream>

using namespace std;

pair<__int128, __int128> find_pq(__int128 A, __int128 B, __int128 C, __int128 D) {
    __int128 k = A / B;
    if ((k + 1) * D < C) {
        return {k + 1, 1};
    }
    if (A == k * B) {
        __int128 rem_C = C - k * D;
        __int128 q = D / rem_C + 1;
        return {k * q + 1, q};
    }
    __int128 rem_A = A - k * B;
    __int128 rem_C = C - k * D;
    auto [q, p_prime] = find_pq(D, rem_C, B, rem_A);
    return {k * q + p_prime, q};
}

void solve_case() {
    long long a, b, c, d;
    cin >> a >> b >> c >> d;
    auto [p, q] = find_pq(a, b, c, d);
    cout << (long long)q << "\n";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    if (cin >> T) {
        while (T--) solve_case();
    }
    return 0;
}'''
    },
    {
        'id': 'abc457_f',
        'contest_id': 'abc457',
        'title': 'F. Second Gap',
        'rating': 2167,
        'domain': 'Dynamic Programming (DP)',
        'domain_folder': 'dp',
        'subtopic': 'Intro to DP',
        'topic': 'Knapsack and Basic Dynamic Programming',
        'cat_file': 'categories/dp/permutation_insertion_dp_suffix_second_gap.md',
        'key_idea': 'Count permutations P of 1..N such that in every suffix P[i..N], the distance between the largest and 2nd largest element is D_i. Process elements from right to left (suffix i from N-2 down to 0) tracking only the index a of the maximum element. Multiplications by N - i - 2 and point updates are efficiently handled via a Lazy Segment Tree.',
        'observation': 'When prepending P_i to suffix i+1..N, P_i can be: (1) largest (previous max was at i + D_i); (2) 2nd largest (max was at i + D_i); or (3) smaller than both. The 3rd case preserves the relative max and 2nd-max positions, valid iff D_i == D_{i+1}, which multiplies all existing states by N - i - 2. If D_i != D_{i+1}, all other states become 0.',
        'algorithm': [
            'Base condition: for suffix of length 2, D[N-2] must equal 1 (otherwise return 0). Initialize dp[N-1] = dp[N-2] = 1.',
            'Use a Lazy Segment Tree supporting point set, range multiplication, and range sum queries.',
            'Iterate i from N-3 down to 0: let j = i + D_i and v = dp[j].',
            'If D_i == D_{i+1}, multiply all states by N - i - 2; else set all states to 0.',
            'Add v to dp[j] and dp[i] in the segment tree.',
            'Final answer is the total sum in the segment tree modulo 998244353.'
        ],
        'time_complexity': 'O(N log N)',
        'space_complexity': 'O(N)',
        'code': r'''#include <iostream>
#include <vector>

using namespace std;

const int MOD = 998244353;

struct LazySegTree {
    int n;
    vector<long long> tree, lazy;
    LazySegTree(int n) : n(n), tree(4 * n, 0), lazy(4 * n, 1) {}

    void apply(int node, long long mul) {
        tree[node] = (tree[node] * mul) % MOD;
        lazy[node] = (lazy[node] * mul) % MOD;
    }

    void push(int node) {
        if (lazy[node] != 1) {
            apply(2 * node, lazy[node]);
            apply(2 * node + 1, lazy[node]);
            lazy[node] = 1;
        }
    }

    void pull(int node) {
        tree[node] = (tree[2 * node] + tree[2 * node + 1]) % MOD;
    }

    void set_val(int node, int l, int r, int idx, long long val) {
        if (l == r) {
            tree[node] = val % MOD;
            lazy[node] = 1;
            return;
        }
        push(node);
        int mid = (l + r) / 2;
        if (idx <= mid) set_val(2 * node, l, mid, idx, val);
        else set_val(2 * node + 1, mid + 1, r, idx, val);
        pull(node);
    }

    void multiply_all(int node, int l, int r, long long mul) {
        apply(node, mul);
    }

    long long get_val(int node, int l, int r, int idx) {
        if (l == r) return tree[node];
        push(node);
        int mid = (l + r) / 2;
        if (idx <= mid) return get_val(2 * node, l, mid, idx);
        else return get_val(2 * node + 1, mid + 1, r, idx);
    }

    long long query_total() {
        return tree[1];
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    if (!(cin >> N)) return 0;

    vector<int> D(N - 1);
    for (int i = 0; i < N - 1; ++i) cin >> D[i];

    if (D.back() != 1) {
        cout << 0 << "\n";
        return 0;
    }

    LazySegTree st(N);
    st.set_val(1, 0, N - 1, N - 1, 1);
    st.set_val(1, 0, N - 1, N - 2, 1);

    for (int i = N - 3; i >= 0; --i) {
        int j = i + D[i];
        long long v = st.get_val(1, 0, N - 1, j);
        if (D[i] == D[i + 1]) {
            st.multiply_all(1, 0, N - 1, N - i - 2);
        } else {
            st.multiply_all(1, 0, N - 1, 0);
        }
        long long cur_j = st.get_val(1, 0, N - 1, j);
        long long cur_i = st.get_val(1, 0, N - 1, i);
        st.set_val(1, 0, N - 1, j, (cur_j + v) % MOD);
        st.set_val(1, 0, N - 1, i, (cur_i + v) % MOD);
    }

    cout << st.query_total() << "\n";
    return 0;
}'''
    },
    {
        'id': 'apc001_e',
        'contest_id': 'apc001',
        'title': 'E. Antennas on Tree',
        'rating': 2167,
        'domain': 'Dynamic Programming (DP)',
        'domain_folder': 'dp',
        'subtopic': 'Dp on Different Structures',
        'topic': 'DP on Trees and DAGs',
        'cat_file': 'categories/dp/metric_dimension_tree_dp_high_degree_root.md',
        'key_idea': 'Determine the minimum number of antennas required to uniquely identify any invaded vertex on a tree. Removing any vertex v with degree k must leave at least k - 1 connected components containing at least one antenna. If max degree <= 2, the tree is a path (answer 1). Otherwise, root the tree at any vertex of degree >= 3 and solve via simple bottom-up Tree DP.',
        'observation': 'Rooting at a vertex r of degree >= 3 guarantees that for every vertex u != r, the parent component already contains an antenna. Thus, for every node u, at most one child subtree can have 0 antennas. For leaf u, f(u) = 0. For internal node u with z children having f(v) = 0, f(u) = sum(f(v)) + max(0, z - 1). The answer is f(r).',
        'algorithm': [
            'If N <= 2 or max degree <= 2, output 1.',
            'Locate any vertex root with degree >= 3.',
            'Perform DFS from root: for each child v of u, compute res = dfs(v). Accumulate sum s += res and count zeros z += (res == 0).',
            'For a leaf (no children), return 0. For internal node, return s + max(0, z - 1).',
            'Return and print dfs(root, -1).'
        ],
        'time_complexity': 'O(N)',
        'space_complexity': 'O(N)',
        'code': r'''#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    if (!(cin >> N)) return 0;

    if (N <= 2) {
        cout << 1 << "\n";
        return 0;
    }

    vector<vector<int>> adj(N);
    for (int i = 0; i < N - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    int root = -1;
    for (int i = 0; i < N; ++i) {
        if ((int)adj[i].size() >= 3) {
            root = i;
            break;
        }
    }

    if (root == -1) {
        cout << 1 << "\n";
        return 0;
    }

    auto dfs = [&](auto& self, int u, int p) -> int {
        int s = 0, z = 0;
        bool is_leaf = true;
        for (int v : adj[u]) {
            if (v != p) {
                is_leaf = false;
                int res = self(self, v, u);
                s += res;
                if (res == 0) z++;
            }
        }
        if (is_leaf) return 0;
        return s + max(0, z - 1);
    };

    cout << dfs(dfs, root, -1) << "\n";
    return 0;
}'''
    },
    {
        'id': 'abc349_f',
        'contest_id': 'abc349',
        'title': 'I. Subsequence LCM',
        'rating': 2169,
        'domain': 'Dynamic Programming (DP)',
        'domain_folder': 'dp',
        'subtopic': 'Bit Related DP',
        'topic': 'Sum Over Subsets DP (SOS DP)',
        'cat_file': 'categories/dp/subsequence_lcm_sos_dp_inclusion_exclusion.md',
        'key_idea': 'Find the number of non-empty subsequences with LCM equal to M. Factor M into distinct prime powers p_j^{e_j} (at most k <= 15 prime powers). Filter elements to those dividing M, mapping each to a k-bit mask indicating which prime power exponents match e_j. Count subsequences whose bitwise OR is full mask (1<<k)-1 using SOS DP and Principle of Inclusion-Exclusion.',
        'observation': 'An element A_i can only be used if A_i | M. For each prime factor p_j, the LCM reaches the exact power p_j^{e_j} iff at least one chosen element has exponent e_j. With k <= 15 distinct prime powers, submask counts F(S) = sum_{T subseteq S} cnt[T] are computed in O(k * 2^k) via SOS DP. By inclusion-exclusion, the number of full-OR subsets is sum_{S} (-1)^{k - |S|} 2^{F(S)}.',
        'algorithm': [
            'If M = 1, count elements equal to 1 (say c) and output 2^c - 1.',
            'Factorize M into prime powers (p_0, pw_0), ..., (p_{k-1}, pw_{k-1}).',
            'For each A_i dividing M, compute its bitmask sum_{j} [A_i % pw_j == 0] * 2^j, and record counts in array cnt[mask].',
            'Compute SOS DP f[mask] = sum_{sub subseteq mask} cnt[sub] in O(k * 2^k).',
            'Calculate answer via inclusion-exclusion: ans = sum_{mask} (-1)^{k - popcount(mask)} * 2^{f[mask]} mod 998244353.'
        ],
        'time_complexity': 'O(N + sqrt(M) + k * 2^k)',
        'space_complexity': 'O(2^k)',
        'code': r'''#include <iostream>
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

    int N;
    long long M;
    if (!(cin >> N >> M)) return 0;

    vector<long long> A(N);
    for (int i = 0; i < N; ++i) cin >> A[i];

    if (M == 1) {
        int c = 0;
        for (long long x : A) {
            if (x == 1) c++;
        }
        cout << (power(2, c) - 1 + MOD) % MOD << "\n";
        return 0;
    }

    long long temp = M;
    vector<pair<long long, long long>> primes;
    for (long long p = 2; p * p <= temp; ++p) {
        if (temp % p == 0) {
            long long pw = 1;
            while (temp % p == 0) {
                pw *= p;
                temp /= p;
            }
            primes.push_back({p, pw});
        }
    }
    if (temp > 1) {
        primes.push_back({temp, temp});
    }

    int k = (int)primes.size();
    vector<int> cnt(1 << k, 0);

    for (long long x : A) {
        if (M % x != 0) continue;
        int mask = 0;
        for (int i = 0; i < k; ++i) {
            if (x % primes[i].second == 0) {
                mask |= (1 << i);
            }
        }
        cnt[mask]++;
    }

    vector<int> f = cnt;
    for (int i = 0; i < k; ++i) {
        for (int mask = 0; mask < (1 << k); ++mask) {
            if (mask & (1 << i)) {
                f[mask] += f[mask ^ (1 << i)];
            }
        }
    }

    long long ans = 0;
    for (int mask = 0; mask < (1 << k); ++mask) {
        int set_bits = __builtin_popcount(mask);
        int sign = ((k - set_bits) % 2 == 1 ? -1 : 1);
        long long term = power(2, f[mask]);
        ans = (ans + sign * term) % MOD;
        if (ans < 0) ans += MOD;
    }

    cout << ans << "\n";
    return 0;
}'''
    },
    {
        'id': 'abc454_f',
        'contest_id': 'abc454',
        'title': 'I. Make it Palindrome 2',
        'rating': 2169,
        'domain': 'Basics',
        'domain_folder': 'basics',
        'subtopic': 'More Techniques',
        'topic': 'Difference Array',
        'cat_file': 'categories/basics/palindrome_modulo_difference_array_matching.md',
        'key_idea': 'Minimum range increment/decrement operations modulo M to make sequence A palindromic. Folding differences B_i = (A_i - A_{N+1-i}) mod M reduces the problem to zeroing B. Transforming to difference array C_i = (B_i - B_{i-1}) mod M turns range operations into pairs of increment/decrement on single elements, solvable greedily by sorting.',
        'observation': 'Cross-center range operations decompose into symmetric left/right operations without penalty. On difference sequence C (where sum(C) is a multiple of M), each operation increments one element and decrements another modulo M. Choosing a subset of elements X to only decrease and the rest to only increase yields minimum operations sum of the k smallest elements of C, where k = |C| - sum(C)/M.',
        'algorithm': [
            'Compute difference array B of length floor(N/2) with B_i = (A_i - A_{N-1-i}) mod M, padded with zeros at both ends.',
            'Compute adjacent differences C_i = (B_{i+1} - B_i) mod M.',
            'Sort C in ascending order.',
            'The minimum operations is the sum of the first len(C) - sum(C)/M elements of C.'
        ],
        'time_complexity': 'O(N log N) per testcase',
        'space_complexity': 'O(N)',
        'code': r'''#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

using namespace std;

void solve_case() {
    int N;
    long long M;
    cin >> N >> M;
    vector<long long> A(N);
    for (int i = 0; i < N; ++i) cin >> A[i];

    int half = N / 2;
    vector<long long> B;
    B.reserve(half + 2);
    B.push_back(0);
    for (int i = 0; i < half; ++i) {
        long long diff = (A[i] - A[N - 1 - i]) % M;
        if (diff < 0) diff += M;
        B.push_back(diff);
    }
    B.push_back(0);

    vector<long long> C;
    C.reserve(B.size() - 1);
    long long sum_c = 0;
    for (size_t i = 0; i + 1 < B.size(); ++i) {
        long long diff = (B[i + 1] - B[i]) % M;
        if (diff < 0) diff += M;
        C.push_back(diff);
        sum_c += diff;
    }

    sort(C.begin(), C.end());
    size_t k = C.size() - (sum_c / M);
    long long ans = 0;
    for (size_t i = 0; i < k; ++i) {
        ans += C[i];
    }
    cout << ans << "\n";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    if (cin >> T) {
        while (T--) solve_case();
    }
    return 0;
}'''
    },
    {
        'id': 'agc028_b',
        'contest_id': 'agc028',
        'title': 'B. Removing Blocks',
        'rating': 2172,
        'domain': 'Math',
        'domain_folder': 'math',
        'subtopic': 'Probabilities and Expected Values',
        'topic': 'Probabilities and Expected Values',
        'cat_file': 'categories/math/linearity_of_expectation_harmonic_prefix_sums.md',
        'key_idea': 'Compute the total cost of removing N blocks in all N! random orders. By Linearity of Expectation, block j is connected to block i at the moment i is removed iff block i is removed before all blocks strictly between i and j. The probability is 1 / (|j - i| + 1). Summing over all pairs yields a closed-form expression using Harmonic numbers H_m = sum_{k=1}^m 1/k.',
        'observation': 'The set of blocks between i and j inclusive has size |j - i| + 1. The first block among them to be removed is uniformly distributed over the |j - i| + 1 candidates. Block j contributes to the cost of removing i iff i is chosen first among these blocks, with probability 1 / (|j - i| + 1). Summing over all i for a fixed j gives H_j + H_{N - j + 1} - 1. Multiplying by N! gives the exact answer.',
        'algorithm': [
            'Precompute modular inverses and harmonic prefix sums H_m = sum_{k=1}^m k^{-1} mod (10^9 + 7) in O(N).',
            'Compute N! mod (10^9 + 7).',
            'For each block j from 1 to N, its total expected contribution factor is H_j + H_{N - j + 1} - 1.',
            'Multiply each A_j by its factor, sum over all j, and multiply the total by N! mod (10^9 + 7).'
        ],
        'time_complexity': 'O(N)',
        'space_complexity': 'O(N)',
        'code': r'''#include <iostream>
#include <vector>

using namespace std;

const int MOD = 1000000007;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    if (!(cin >> N)) return 0;

    vector<long long> A(N + 1);
    for (int i = 1; i <= N; ++i) cin >> A[i];

    vector<long long> inv(N + 1, 1);
    for (int i = 2; i <= N; ++i) {
        inv[i] = (MOD - MOD / i) * inv[MOD % i] % MOD;
    }

    vector<long long> H(N + 1, 0);
    for (int i = 1; i <= N; ++i) {
        H[i] = (H[i - 1] + inv[i]) % MOD;
    }

    long long fact = 1;
    for (int i = 1; i <= N; ++i) {
        fact = (fact * i) % MOD;
    }

    long long total = 0;
    for (int j = 1; j <= N; ++j) {
        long long coeff = (H[j] + H[N - j + 1] - 1 + MOD) % MOD;
        long long term = (A[j] % MOD) * coeff % MOD;
        total = (total + term) % MOD;
    }

    long long ans = (total * fact) % MOD;
    cout << ans << "\n";
    return 0;
}'''
    },
    {
        'id': 'abc283_g',
        'contest_id': 'abc283',
        'title': 'G. Partial Xor Enumeration',
        'rating': 2173,
        'domain': 'Math',
        'domain_folder': 'math',
        'subtopic': 'Linear Algebra',
        'topic': '[Technique] XOR Basis ft Reduced Row Echelon Form',
        'cat_file': 'categories/math/xor_basis_reduced_row_echelon_kth_query.md',
        'key_idea': 'Find the k-th smallest subset XOR value for each k in [L, R]. Construct a linear basis of the given integers over F_2 and diagonalize it into Reduced Row Echelon Form (RREF). The sorted distinct subset XOR values correspond 1-to-1 with the binary representations of integers 0 <= idx < 2^d expanded over the basis.',
        'observation': 'Once the basis B_0 < B_1 < ... < B_{d-1} is in canonical RREF (each basis vector has a unique pivot bit that is 0 in all other basis vectors), lexicographical order of subset XORs matches the standard integer binary order. Thus, the k-th smallest subset XOR is obtained directly by taking linear combinations matching the binary representation of k - 1.',
        'algorithm': [
            'Insert each integer A_i into a linear basis using standard Gaussian elimination.',
            'Diagonalize the basis into Reduced Row Echelon Form (RREF) so that the leading pivot of each basis vector is cleared from all other basis vectors.',
            'Sort the basis vectors in ascending order of their pivot bits.',
            'For each k in [L, R], evaluate the XOR sum of basis[b] for each bit b set in (k - 1).'
        ],
        'time_complexity': 'O(N * 60 + (R - L + 1) * 60)',
        'space_complexity': 'O(N + 60)',
        'code': r'''#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    long long L, R;
    if (!(cin >> N >> L >> R)) return 0;

    vector<unsigned long long> A(N);
    vector<unsigned long long> basis;
    for (int i = 0; i < N; ++i) {
        cin >> A[i];
        unsigned long long x = A[i];
        for (unsigned long long b : basis) {
            x = min(x, x ^ b);
        }
        if (x > 0) {
            basis.push_back(x);
            sort(basis.rbegin(), basis.rend());
        }
    }

    int d = (int)basis.size();
    for (int i = d - 1; i >= 0; --i) {
        for (int j = i - 1; j >= 0; --j) {
            basis[j] = min(basis[j], basis[j] ^ basis[i]);
        }
    }

    reverse(basis.begin(), basis.end());

    for (long long k = L; k <= R; ++k) {
        long long idx = k - 1;
        unsigned long long val = 0;
        for (int b = 0; b < d; ++b) {
            if ((idx >> b) & 1) {
                val ^= basis[b];
            }
        }
        cout << val << (k == R ? "" : " ");
    }
    cout << "\n";
    return 0;
}'''
    },
    {
        'id': 'arc035_d',
        'contest_id': 'arc035',
        'title': 'D. 高橋くんとマラソンコース',
        'rating': 2173,
        'domain': 'Data Structures (DS)',
        'domain_folder': 'data_structures',
        'subtopic': 'Segment Tree',
        'topic': 'Segment Tree (Point Update Range Query)',
        'cat_file': 'categories/data_structures/grid_paths_log_binomial_fenwick_tree.md',
        'key_idea': 'Given N checkpoints on a grid, moving only North or East, the number of paths between checkpoint i and i+1 is binom(dx + dy, dx). Compare total path products across query subsegments under point checkpoint modifications. Maintain logarithms of binomial coefficients in a Fenwick tree; compare range sums of log-probabilities.',
        'observation': 'The problem guarantees that the larger path count is at least twice the smaller path count. Taking logarithms transforms product queries into range sum queries: sum_{i=l}^{r-1} log binom(dx_i + dy_i, dx_i). Precomputing log-factorials log(m!) allows O(1) evaluation of log binom, and a Fenwick tree supports O(log N) updates and range comparisons with double precision.',
        'algorithm': [
            'Precompute logfact[m] = sum_{j=1}^m log(j) for m <= 2*10^6.',
            'Initialize Fenwick tree with values log binom(dx_i + dy_i, dx_i) for segment i to i+1.',
            'Type 1 query: update checkpoint k position; recalculate and apply point differences to segments k-1 and k in the Fenwick tree.',
            'Type 2 query: query range sums s1 on [l1, r1-1] and s2 on [l2, r2-1]. Output FIRST if s1 > s2, else SECOND.'
        ],
        'time_complexity': 'O((N + Q) log N)',
        'space_complexity': 'O(N + max_coord)',
        'code': r'''#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

const int MAX = 2000005;
double logfact[MAX];

struct Fenwick {
    int n;
    vector<double> tree;
    Fenwick(int n) : n(n), tree(n + 1, 0.0) {}
    void add(int i, double delta) {
        for (; i <= n; i += i & -i) tree[i] += delta;
    }
    double query(int i) {
        double sum = 0;
        for (; i > 0; i -= i & -i) sum += tree[i];
        return sum;
    }
    double query(int l, int r) {
        if (l > r) return 0.0;
        return query(r) - query(l - 1);
    }
};

double logcomb(int dx, int dy) {
    if (dx < 0 || dy < 0) return -1e18;
    return logfact[dx + dy] - logfact[dx] - logfact[dy];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    logfact[0] = 0.0;
    for (int i = 1; i < MAX; ++i) logfact[i] = logfact[i - 1] + log((double)i);

    int N;
    if (!(cin >> N)) return 0;

    vector<pair<int, int>> P(N + 1);
    for (int i = 1; i <= N; ++i) {
        cin >> P[i].first >> P[i].second;
    }

    Fenwick ft(N);
    auto seg_val = [&](int i) -> double {
        int dx = P[i + 1].first - P[i].first;
        int dy = P[i + 1].second - P[i].second;
        return logcomb(dx, dy);
    };

    for (int i = 1; i < N; ++i) {
        ft.add(i, seg_val(i));
    }

    int Q;
    cin >> Q;
    while (Q--) {
        int type;
        cin >> type;
        if (type == 1) {
            int k, a, b;
            cin >> k >> a >> b;
            double old_prev = (k > 1 ? seg_val(k - 1) : 0.0);
            double old_curr = (k < N ? seg_val(k) : 0.0);
            P[k] = {a, b};
            if (k > 1) {
                double new_prev = seg_val(k - 1);
                ft.add(k - 1, new_prev - old_prev);
            }
            if (k < N) {
                double new_curr = seg_val(k);
                ft.add(k, new_curr - old_curr);
            }
        } else {
            int l1, r1, l2, r2;
            cin >> l1 >> r1 >> l2 >> r2;
            double s1 = ft.query(l1, r1 - 1);
            double s2 = ft.query(l2, r2 - 1);
            if (s1 > s2) cout << "FIRST\n";
            else cout << "SECOND\n";
        }
    }

    return 0;
}'''
    },
    {
        'id': 'arc217_c',
        'contest_id': 'arc217',
        'title': 'C. Greedy Customers 2',
        'rating': 2173,
        'domain': 'Math',
        'domain_folder': 'math',
        'subtopic': 'Probabilities and Expected Values',
        'topic': 'Probabilities and Expected Values',
        'cat_file': 'categories/math/greedy_customers_hall_multinomial_prefix_dp.md',
        'key_idea': 'N customers with random budgets in 1..C greedily purchase the most expensive available item they can afford. By Hall\'s condition, at least k items are sold iff for each i in 1..k, at least k - i + 1 customers have budget >= A_i. Compute tail probabilities P(>= k) via suffix DP and multinomial transitions, then recover exact probabilities P(k) = P(>= k) - P(>= k + 1).',
        'observation': 'Sorting items A_1 <= A_2 <= ... <= A_k <= C, customers with budget in [A_i, A_{i+1}-1] are grouped into buckets. DP state dp[j] counts ways to assign budgets to j customers with budget >= A_i satisfying all suffix conditions up to item k. Transitioning from i+1 down to i with multinomial weights (diff)^t / t! solves each k in O(k * N^2) time, totaling O(N^4).',
        'algorithm': [
            'For each k from 1 to N, calculate the probability P(>= k) that at least k items are purchased.',
            'Run DP from i = k down to 1: dp[j] represents ways to distribute budgets such that j people have budget >= A_i, subject to j >= k - i + 1.',
            'Transition by adding t people to bucket [A_i, A_{i+1} - 1] weighted by (A_{i+1} - A_i)^t / t!.',
            'After bucket 1, multiply by remaining people choosing budgets < A_1, normalize by N! / C^N.',
            'Output P(k) = P(>= k) - P(>= k + 1) for all k = 0, ..., N modulo 998244353.'
        ],
        'time_complexity': 'O(N^4)',
        'space_complexity': 'O(N)',
        'code': r'''#include <iostream>
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

void solve_case() {
    int N;
    long long C;
    cin >> N >> C;
    vector<long long> A(N);
    for (int i = 0; i < N; ++i) cin >> A[i];
    sort(A.begin(), A.end());

    vector<long long> fact(N + 1, 1), inv(N + 1, 1);
    for (int i = 1; i <= N; ++i) fact[i] = (fact[i - 1] * i) % MOD;
    inv[N] = modInverse(fact[N]);
    for (int i = N - 1; i >= 0; --i) inv[i] = (inv[i + 1] * (i + 1)) % MOD;

    long long inv_c_n = power(power(C % MOD, N), MOD - 2);

    vector<long long> P_ge(N + 1, 0);
    P_ge[0] = 1;

    for (int k = 1; k <= N; ++k) {
        vector<long long> dp(N + 1, 0);
        dp[0] = 1;

        for (int i = k; i >= 1; --i) {
            long long p_curr = A[i - 1];
            long long p_next = (i == k ? C + 1 : A[i]);
            long long diff = (p_next - p_curr) % MOD;
            if (diff < 0) diff += MOD;

            vector<long long> term(N + 1, 1);
            for (int t = 1; t <= N; ++t) {
                term[t] = term[t - 1] * diff % MOD * inv[t] % MOD * fact[t - 1] % MOD;
            }

            vector<long long> new_dp(N + 1, 0);
            for (int j = k - i + 1; j <= N; ++j) {
                long long s = 0;
                for (int j_prev = 0; j_prev <= j; ++j_prev) {
                    if (dp[j_prev]) {
                        s = (s + dp[j_prev] * term[j - j_prev]) % MOD;
                    }
                }
                new_dp[j] = s;
            }
            dp = move(new_dp);
        }

        long long diff0 = (A[0] - 1) % MOD;
        if (diff0 < 0) diff0 += MOD;

        vector<long long> term0(N + 1, 1);
        for (int t = 1; t <= N; ++t) {
            term0[t] = term0[t - 1] * diff0 % MOD * inv[t] % MOD * fact[t - 1] % MOD;
        }

        long long total_ways = 0;
        for (int j = k; j <= N; ++j) {
            total_ways = (total_ways + dp[j] * term0[N - j]) % MOD;
        }
        total_ways = total_ways * fact[N] % MOD * inv_c_n % MOD;
        P_ge[k] = total_ways;
    }

    vector<long long> P_eq(N + 1, 0);
    for (int k = 0; k < N; ++k) {
        P_eq[k] = (P_ge[k] - P_ge[k + 1] + MOD) % MOD;
    }
    P_eq[N] = P_ge[N];

    for (int k = 0; k <= N; ++k) {
        cout << P_eq[k] << (k == N ? "" : " ");
    }
    cout << "\n";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    if (cin >> T) {
        while (T--) solve_case();
    }
    return 0;
}'''
    },
    {
        'id': 'abc291_g',
        'contest_id': 'abc291',
        'title': 'G. OR Sum',
        'rating': 2176,
        'domain': 'Math',
        'domain_folder': 'math',
        'subtopic': 'Convolution',
        'topic': 'Fast Fourier Transform (FFT)',
        'cat_file': 'categories/math/cyclic_or_convolution_bitwise_ntt.md',
        'key_idea': 'Maximize sum_{i=0}^{N-1} (A_i | B_{(i+k)%N}) over all cyclic shifts k in [0, N-1]. Decompose numbers into 5 bits. For each bit b, x | y = 1 - (1 - x)(1 - y). Compute cyclic cross-correlations of (1 - A) and (1 - B) across all shifts using Number Theoretic Transform (NTT) under modulo 998244353.',
        'observation': 'The bitwise OR sum decomposes linearly across the 5 independent bit positions 0 <= bit < 5. For each bit, x_i | y_j = 1 - u_i * v_j where u_i = 1 - x_i and v_j = 1 - y_j. The sum sum_i u_i * v_{(i+k)%N} is a cyclic cross-correlation, computed by reversing u and convolving with duplicated v (length 2N) via NTT in O(N log N) time.',
        'algorithm': [
            'For each bit b in 0..4:',
            '  Construct array u of length N with u[N - 1 - i] = 1 - ((A[i] >> b) & 1).',
            '  Construct array v of length 2N with v[i] = v[i + N] = 1 - ((B[i] >> b) & 1).',
            '  Convolve u and v using NTT modulo 998244353.',
            '  For each shift k in 0..N-1, the number of (1, 1) zero-pairs is conv[N - 1 + k], meaning N - conv[N - 1 + k] positions have bit b set in OR.',
            '  Add (N - conv[N - 1 + k]) * 2^b to total_score[k].',
            'Output max_{k} total_score[k].'
        ],
        'time_complexity': 'O(5 * N log N)',
        'space_complexity': 'O(N)',
        'code': r'''#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MOD = 998244353;
const int G = 3;

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

void ntt(vector<long long>& a, bool invert) {
    int n = a.size();
    for (int i = 1, j = 0; i < n; i++) {
        int bit = n >> 1;
        for (; j & bit; bit >>= 1) j ^= bit;
        j ^= bit;
        if (i < j) swap(a[i], a[j]);
    }
    for (int len = 2; len <= n; len <<= 1) {
        long long wlen = power(G, (MOD - 1) / len);
        if (invert) wlen = modInverse(wlen);
        for (int i = 0; i < n; i += len) {
            long long w = 1;
            for (int j = 0; j < len / 2; j++) {
                long long u = a[i + j];
                long long v = (a[i + j + len / 2] * w) % MOD;
                a[i + j] = (u + v < MOD ? u + v : u + v - MOD);
                a[i + j + len / 2] = (u - v >= 0 ? u - v : u - v + MOD);
                w = (w * wlen) % MOD;
            }
        }
    }
    if (invert) {
        long long n_inv = modInverse(n);
        for (long long& x : a) x = (x * n_inv) % MOD;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    if (!(cin >> N)) return 0;

    vector<int> A(N), B(N);
    for (int i = 0; i < N; ++i) cin >> A[i];
    for (int i = 0; i < N; ++i) cin >> B[i];

    int sz = 1;
    while (sz < 3 * N) sz <<= 1;

    vector<long long> score(N, 0);

    for (int bit = 0; bit < 5; ++bit) {
        vector<long long> u(sz, 0), v(sz, 0);
        for (int i = 0; i < N; ++i) {
            u[N - 1 - i] = 1 - ((A[i] >> bit) & 1);
            v[i] = 1 - ((B[i] >> bit) & 1);
            v[i + N] = v[i];
        }

        ntt(u, false);
        ntt(v, false);
        for (int i = 0; i < sz; ++i) {
            u[i] = (u[i] * v[i]) % MOD;
        }
        ntt(u, true);

        long long bit_val = 1LL << bit;
        for (int k = 0; k < N; ++k) {
            long long zero_pairs = u[N - 1 + k];
            long long one_pairs = N - zero_pairs;
            score[k] += one_pairs * bit_val;
        }
    }

    long long ans = 0;
    for (int k = 0; k < N; ++k) {
        ans = max(ans, score[k]);
    }
    cout << ans << "\n";
    return 0;
}'''
    },
    {
        'id': 'agc022_c',
        'contest_id': 'agc022',
        'title': 'C. Remainder Game',
        'rating': 2176,
        'domain': 'Miscellaneous',
        'domain_folder': 'miscellaneous',
        'subtopic': 'Greedy Algorithms',
        'topic': 'Exchange Arguments',
        'cat_file': 'categories/miscellaneous/remainder_game_greedy_power_of_two_reachability.md',
        'key_idea': 'Transform array a into b using operations v <- v mod k at cost 2^k. Since costs are powers of 2, minimizing the sum corresponds to lexicographically minimizing the set of chosen moduli from largest to smallest. Greedily attempt to drop k from 50 down to 1, retaining k iff removing it destroys reachability from a_i to b_i.',
        'observation': 'Moduli k > 50 are useless since all values are <= 50. Because cost is sum of 2^k, choosing 2^k is more expensive than any combination of smaller powers sum_{j < k} 2^j < 2^k. Thus, a greedy high-to-low elimination strategy is optimal. Reachability on the 51-node directed graph (u -> u mod m for allowed m) is checked in O(50 * V^2).',
        'algorithm': [
            'Initialize allowed set of moduli S = {1, 2, ..., 50}.',
            'Verify that b_i is reachable from a_i for all i using all moduli in S. If not, output -1.',
            'For k = 50 down to 1: temporarily remove k from S. Check if reachability still holds for all pairs (a_i, b_i). If reachability breaks, k must be retained in S.',
            'Output sum_{k in S} 2^k.'
        ],
        'time_complexity': 'O(50 * (50 * V^2 + N))',
        'space_complexity': 'O(V^2)',
        'code': r'''#include <iostream>
#include <vector>
#include <set>

using namespace std;

bool check(const set<int>& allowed, const vector<int>& a, const vector<int>& b, int n) {
    vector<vector<int>> adj(51);
    for (int u = 0; u <= 50; ++u) {
        for (int k : allowed) {
            adj[u].push_back(u % k);
        }
    }

    vector<vector<bool>> reach(51, vector<bool>(51, false));
    for (int u = 0; u <= 50; ++u) {
        reach[u][u] = true;
        vector<int> q = {u};
        for (size_t idx = 0; idx < q.size(); ++idx) {
            int v = q[idx];
            for (int w : adj[v]) {
                if (!reach[u][w]) {
                    reach[u][w] = true;
                    q.push_back(w);
                }
            }
        }
    }

    for (int i = 0; i < n; ++i) {
        if (!reach[a[i]][b[i]]) return false;
    }
    return true;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    if (!(cin >> N)) return 0;

    vector<int> A(N), B(N);
    for (int i = 0; i < N; ++i) cin >> A[i];
    for (int i = 0; i < N; ++i) cin >> B[i];

    set<int> allowed;
    for (int k = 1; k <= 50; ++k) allowed.insert(k);

    if (!check(allowed, A, B, N)) {
        cout << -1 << "\n";
        return 0;
    }

    for (int k = 50; k >= 1; --k) {
        allowed.erase(k);
        if (!check(allowed, A, B, N)) {
            allowed.insert(k);
        }
    }

    long long ans = 0;
    for (int k : allowed) {
        ans += (1LL << k);
    }
    cout << ans << "\n";
    return 0;
}'''
    },
    {
        'id': 'agc049_c',
        'contest_id': 'agc049',
        'title': 'C. Robots',
        'rating': 2177,
        'domain': 'Basics',
        'domain_folder': 'basics',
        'subtopic': 'Greedy and Constructive',
        'topic': 'Basic Greedy Algorithms',
        'cat_file': 'categories/basics/robots_line_intervals_suffix_min_greedy.md',
        'key_idea': 'Robots start at coordinates A_i and move B_i steps left, destroying encountered robots. Avoid destroying Robot 0 with minimum ball modifications. Robots with B_j < A_j can safely destroy other robots without reaching 0. Dangerous robots (B_i >= A_i) must either be destroyed by a safe robot to their right, or modified by deleting B_i - A_i + 1 balls (which sweeps and destroys all robots to its left).',
        'observation': 'A safe robot j (B_j < A_j) covers coordinate range [A_j - B_j, A_j - 1]. Precomputing suffix minimums min_{j > k, B_j < A_j} (A_j - B_j) identifies which dangerous robots are automatically covered. If we delete B_i - A_i + 1 balls from the rightmost modified dangerous robot i, it safely destroys all robots < A_i. The optimal answer is min over all dangerous i of max(B_i - A_i + 1, suffix_uncovered_dangerous[i + 1]).',
        'algorithm': [
            'Precompute suff_min[j] = min_{idx >= j, B < A} (A - B) from right to left.',
            'Identify uncovered dangerous robots: bad[k] = 1 iff B_k >= A_k and suff_min[k + 1] > A_k.',
            'Compute suffix sums suff_bad[k] of uncovered dangerous robots.',
            'Initialize answer to suff_bad[0] (case with 0 deletions, purely fixing balls).',
            'For each dangerous robot i (B_i >= A_i), evaluate cost max(B_i - A_i + 1, suff_bad[i + 1]) and take the minimum.'
        ],
        'time_complexity': 'O(N)',
        'space_complexity': 'O(N)',
        'code': r'''#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    if (!(cin >> N)) return 0;

    vector<long long> A(N), B(N);
    for (int i = 0; i < N; ++i) cin >> A[i];
    for (int i = 0; i < N; ++i) cin >> B[i];

    long long INF = 2e18;
    vector<long long> suff_min(N + 1, INF);
    for (int j = N - 1; j >= 0; --j) {
        suff_min[j] = suff_min[j + 1];
        if (B[j] < A[j]) {
            suff_min[j] = min(suff_min[j], A[j] - B[j]);
        }
    }

    vector<int> bad(N, 0);
    for (int k = 0; k < N; ++k) {
        if (B[k] >= A[k]) {
            if (suff_min[k + 1] > A[k]) {
                bad[k] = 1;
            }
        }
    }

    vector<int> suff_bad(N + 1, 0);
    for (int k = N - 1; k >= 0; --k) {
        suff_bad[k] = suff_bad[k + 1] + bad[k];
    }

    long long ans = suff_bad[0];
    for (int i = 0; i < N; ++i) {
        if (B[i] >= A[i]) {
            long long cost = max(B[i] - A[i] + 1LL, (long long)suff_bad[i + 1]);
            ans = min(ans, cost);
        }
    }

    cout << ans << "\n";
    return 0;
}'''
    },
    {
        'id': 'mujin_pc_2017_b',
        'contest_id': 'mujin_pc_2017',
        'title': 'B. Row to Column',
        'rating': 2177,
        'domain': 'Basics',
        'domain_folder': 'basics',
        'subtopic': 'Greedy and Constructive',
        'topic': 'Basic Constructive Algorithms',
        'cat_file': 'categories/basics/row_to_column_grid_operations_state_reduction.md',
        'key_idea': 'On an N x N grid of white/black cells, an operation copies row i into column j. Minimize operations to make all cells black. The strategy is to construct a single completely black row r, and then copy row r into every column that is not already fully black. Solved by iterating over all possible target rows r.',
        'observation': 'If no cell is black initially, it is impossible (output -1). If all cells are black, 0 operations. Every column not initially full black must eventually be painted by an all-black row. To make row r all black, for each white cell (r, c) we copy a row whose r-th cell is black into column c (Z_r operations). If column r has no black cell initially, 1 extra operation seeds column r with a black cell.',
        'algorithm': [
            'If no \'#\' exists in the grid, output -1. If every cell is \'#\', output 0.',
            'Count the number of columns not completely black: c_nonfull.',
            'For each row r from 0 to N-1, count white cells Z_r in row r.',
            'Check if column r contains at least one \'#\'. If not, add 1 extra operation.',
            'Minimum operations is c_nonfull + min_r (Z_r + (1 if column r has no black cell else 0)).'
        ],
        'time_complexity': 'O(N^2)',
        'space_complexity': 'O(N^2)',
        'code': r'''#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    if (!(cin >> N)) return 0;

    vector<string> grid(N);
    bool has_any_black = false;
    bool all_black = true;
    for (int i = 0; i < N; ++i) {
        cin >> grid[i];
        for (char c : grid[i]) {
            if (c == '#') has_any_black = true;
            else all_black = false;
        }
    }

    if (!has_any_black) {
        cout << -1 << "\n";
        return 0;
    }
    if (all_black) {
        cout << 0 << "\n";
        return 0;
    }

    vector<bool> col_full(N, true);
    vector<bool> col_has_black(N, false);
    int c_nonfull = 0;

    for (int c = 0; c < N; ++c) {
        for (int r = 0; r < N; ++r) {
            if (grid[r][c] == '#') {
                col_has_black[c] = true;
            } else {
                col_full[c] = false;
            }
        }
        if (!col_full[c]) c_nonfull++;
    }

    int ans = 1e9;
    for (int r = 0; r < N; ++r) {
        int z_r = 0;
        for (int c = 0; c < N; ++c) {
            if (grid[r][c] == '.') z_r++;
        }
        int add = (!col_has_black[r] ? 1 : 0);
        ans = min(ans, c_nonfull + z_r + add);
    }

    cout << ans << "\n";
    return 0;
}'''
    }
]

# 1. Compile and verify every problem
print("\n--- Compiling all 18 Solutions ---")
os.makedirs('scratch/test_p4b_bins', exist_ok=True)
for p in problems_meta:
    pid = p['id']
    cpp_file = f"scratch/test_p4b_bins/{pid}.cpp"
    exe_file = f"scratch/test_p4b_bins/{pid}.exe"
    with open(cpp_file, 'w', encoding='utf-8') as f:
        f.write(p['code'])
    
    cmd = ['g++', '-std=c++17', '-O2', cpp_file, '-o', exe_file]
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if res.returncode != 0:
        print(f"[!] Compilation FAILED for {pid}:")
        print(res.stderr)
        sys.exit(1)
    else:
        print(f"[+] Compiled {pid} successfully.")

# 2. Generate Analysis Markdown Files
print("\n--- Generating Analysis Files ---")
os.makedirs('analysis', exist_ok=True)
for p in problems_meta:
    analysis_path = f"analysis/AtCoder-{p['id']}.md"
    steps_md = "\n".join([f"{i+1}. {step}" for i, step in enumerate(p['algorithm'])])
    
    # Category file link relative to analysis/
    rel_cat_path = f"../{p['cat_file']}"
    
    content = f"""# Problem Analysis: AtCoder-{p['id']} — {p['title']}

**Problem ID**: `AtCoder-{p['id']}`  
**Contest**: `{p['contest_id']}`  
**Rating / Difficulty**: {p['rating']}  
**URL**: https://atcoder.jp/contests/{p['contest_id']}/tasks/{p['id']}  
**VJudge Tag**: `[problem:AtCoder-{p['id']}]`  
**Category File**: [`{rel_cat_path}`]({rel_cat_path})  

- **Tag (Domain)**: `{p['domain']}`  
- **Subtopic**: `{p['subtopic']}`  
- **Topic (Skill)**: `{p['topic']}`  

---

## 1. Problem Statement & Key Idea
{p['key_idea']}

## 2. Core Observation & Invariant
{p['observation']}

## 3. Step-by-Step Algorithm
{steps_md}

## 4. Complexity Analysis
- **Time Complexity**: `{p['time_complexity']}`
- **Space Complexity**: `{p['space_complexity']}`

## 5. C++ Source Code
```cpp
{p['code']}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
"""
    with open(analysis_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"[+] Generated: {analysis_path}")

# 3. Update Category Workbooks
print("\n--- Updating Category Workbooks ---")
for p in problems_meta:
    cat_path = p['cat_file']
    os.makedirs(os.path.dirname(cat_path), exist_ok=True)
    
    table_row = f"| [`AtCoder-{p['id']}`](../../analysis/AtCoder-{p['id']}.md) | {p['title']} | {p['rating']} | {p['key_idea'][:120]}... |\n"
    
    if not os.path.exists(cat_path):
        header = f"""# {p['topic']}

**Taxonomy Path**: `{p['domain']}` > `{p['subtopic']}` > `{p['topic']}`

## Description
This topic focuses on {p['topic'].lower()} techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: {p['observation']}
- Common Reductions: {p['key_idea']}

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
"""
        with open(cat_path, 'w', encoding='utf-8') as f:
            f.write(header + table_row)
        print(f"[+] Created Category File: {cat_path}")
    else:
        with open(cat_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # Check if already present
        if not any(p['id'] in line for line in lines):
            with open(cat_path, 'a', encoding='utf-8') as f:
                f.write(table_row)
            print(f"[+] Updated Category File: {cat_path}")
        else:
            print(f"[~] Already in Category File: {cat_path}")

# 4. Update SELECTION_LOG.md
with open('SELECTION_LOG.md', 'r', encoding='utf-8') as f:
    sel_log = f.read()

new_log_entries = []
for p in problems_meta:
    pid = p['id']
    tag_str = f"`[problem:AtCoder-{pid}]`"
    if pid not in sel_log:
        entry = f"| {tag_str} | `{p['contest_id']}` | {p['rating']} | `{p['domain']}` | `{p['subtopic']}` | `{p['topic']}` | **SELECTED** | Premier archetype: {p['key_idea'][:90]}... |\n"
        new_log_entries.append(entry)

if new_log_entries:
    with open('SELECTION_LOG.md', 'a', encoding='utf-8') as f:
        f.writelines(new_log_entries)
    print(f"[+] Added {len(new_log_entries)} new entries to SELECTION_LOG.md")

# 5. Update QUALITY_PROBLEMS_BY_TOPIC.md
with open('QUALITY_PROBLEMS_BY_TOPIC.md', 'r', encoding='utf-8') as f:
    q_content = f.read()

new_quality_entries = []
for p in problems_meta:
    pid = p['id']
    if pid not in q_content:
        entry = f"| [`[problem:AtCoder-{pid}]`](analysis/AtCoder-{pid}.md) | {p['title']} | {p['rating']} | `{p['domain']}` | `{p['topic']}` | [`{p['cat_file']}`]({p['cat_file']}) |\n"
        new_quality_entries.append(entry)

if new_quality_entries:
    with open('QUALITY_PROBLEMS_BY_TOPIC.md', 'a', encoding='utf-8') as f:
        f.writelines(new_quality_entries)
    print(f"[+] Updated QUALITY_PROBLEMS_BY_TOPIC.md with new archetypes.")

# 6. Update progress.json
for p in problems_meta:
    pid = p['id']
    if pid not in completed_ids:
        completed_ids.add(pid)
    if pid not in evaluated_ids:
        evaluated_ids.add(pid)

progress['completed_problem_ids'] = sorted(list(completed_ids))
progress['evaluated_problems'] = sorted(list(evaluated_ids))

with open('state/progress.json', 'w', encoding='utf-8') as f:
    json.dump(progress, f, indent=2, ensure_ascii=False)
print("[+] Updated progress checkpoint: state/progress.json")

print("=" * 75)
print(f"Batch 6 Part 4B completed successfully! Total selected in curriculum: {len(completed_ids)}")
print("=" * 75)
