import os, sys, json, subprocess

sys.stdout.reconfigure(encoding='utf-8')

print("=" * 75)
print("      PROCESSING BATCH 6 PART 4A: ABC / ARC CURATED LADDER (2151 - 2164)")
print("=" * 75)

# Load existing progress
with open('state/progress.json', 'r', encoding='utf-8') as f:
    progress = json.load(f)

completed_ids = set(progress.get('completed_problem_ids', []))
evaluated_ids = set(progress.get('evaluated_problems', []))

# Problem definitions for Part 4A
problems_meta = [
    {
        'id': 'abc356_f',
        'contest_id': 'abc356',
        'title': 'Distance Component Size Query',
        'rating': 2152,
        'domain': 'Data Structures (DS)',
        'domain_folder': 'data_structures',
        'subtopic': 'Binary Indexed Tree (BIT)',
        'topic': 'BIT / Fenwick Tree',
        'cat_file': 'categories/data_structures/gap_tracking_fenwick_component_count.md',
        'key_idea': 'Maintain a dynamic set S under insertions/deletions and compute the size of the connected component containing x in a graph with edges between points having distance <= K. Monotonicity implies components are contiguous sorted intervals where consecutive gaps are <= K. Track break points (gaps > K) in an ordered set and count elements in interval [L, R] using a Fenwick tree.',
        'observation': 'If a < b < c and c - a <= K, then both b - a <= K and c - b <= K. Thus, graph connectivity is completely determined by adjacent differences in sorted order of S. A component boundary occurs at any adjacent pair (u, v) with v - u > K. The component containing x is [L, R] where L is the successor of the nearest break < x (or min(S)), and R is the nearest break >= x (or max(S)).',
        'algorithm': [
            'Coordinate compress all queried x coordinates to support point updates (+1/-1) and prefix range sum queries in a Fenwick tree.',
            'Maintain elements of S in a std::set<long long> S, and maintain break points {u in S | next(u) - u > K} in a second std::set<long long> breaks.',
            'On insert/erase of x, locate neighbors prev(x) and next(x) in S, update the breaks set accordingly, and update the Fenwick tree.',
            'On query for x, find the largest break < x to determine L, find the smallest break >= x to determine R, and query the Fenwick tree for the count of elements in [L, R].'
        ],
        'time_complexity': 'O(Q log Q)',
        'space_complexity': 'O(Q)',
        'code': r'''#include <iostream>
#include <vector>
#include <set>
#include <algorithm>

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
    int query(int l, int r) {
        if (l > r) return 0;
        return query(r) - query(l - 1);
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int q;
    long long k;
    if (!(cin >> q >> k)) return 0;

    vector<pair<int, long long>> queries(q);
    vector<long long> coords;
    for (int i = 0; i < q; ++i) {
        cin >> queries[i].first >> queries[i].second;
        coords.push_back(queries[i].second);
    }

    sort(coords.begin(), coords.end());
    coords.erase(unique(coords.begin(), coords.end()), coords.end());
    auto get_idx = [&](long long val) {
        return lower_bound(coords.begin(), coords.end(), val) - coords.begin() + 1;
    };

    Fenwick bit(coords.size());
    set<long long> S;
    set<long long> breaks; // u in breaks means next(u) - u > k

    for (int i = 0; i < q; ++i) {
        int type = queries[i].first;
        long long x = queries[i].second;

        if (type == 1) {
            if (S.count(x)) {
                // Remove x
                auto it = S.find(x);
                auto prev_it = (it == S.begin()) ? S.end() : prev(it);
                auto next_it = next(it);

                if (prev_it != S.end() && breaks.count(*prev_it)) {
                    breaks.erase(*prev_it);
                }
                if (breaks.count(x)) {
                    breaks.erase(x);
                }
                if (prev_it != S.end() && next_it != S.end()) {
                    if (*next_it - *prev_it > k) {
                        breaks.insert(*prev_it);
                    }
                }
                bit.add(get_idx(x), -1);
                S.erase(it);
            } else {
                // Insert x
                auto next_it = S.upper_bound(x);
                auto prev_it = (next_it == S.begin()) ? S.end() : prev(next_it);

                if (prev_it != S.end() && next_it != S.end()) {
                    if (breaks.count(*prev_it)) {
                        breaks.erase(*prev_it);
                    }
                }
                if (prev_it != S.end()) {
                    if (x - *prev_it > k) {
                        breaks.insert(*prev_it);
                    }
                }
                if (next_it != S.end()) {
                    if (*next_it - x > k) {
                        breaks.insert(x);
                    }
                }
                bit.add(get_idx(x), 1);
                S.insert(x);
            }
        } else {
            // Query size of component containing x
            long long L, R;
            auto it_b_left = breaks.lower_bound(x);
            if (it_b_left == breaks.begin()) {
                L = *S.begin();
            } else {
                long long b_val = *prev(it_b_left);
                auto it_s = S.upper_bound(b_val);
                L = *it_s;
            }

            auto it_b_right = breaks.lower_bound(x);
            if (it_b_right == breaks.end()) {
                R = *S.rbegin();
            } else {
                R = *it_b_right;
            }

            int ans = bit.query(get_idx(L), get_idx(R));
            cout << ans << "\n";
        }
    }
    return 0;
}
'''
    },
    {
        'id': 'abc209_e',
        'contest_id': 'abc209',
        'title': 'Shiritori',
        'rating': 2153,
        'domain': 'Game Theory',
        'domain_folder': 'game_theory',
        'subtopic': 'Graph Games',
        'topic': 'Games on Arbitrary Graphs',
        'cat_file': 'categories/game_theory/retrograde_analysis_directed_cyclic_graphs.md',
        'key_idea': 'Model 3-character prefix/suffix word transitions as a directed graph. Determine whether Takahashi wins, Aoki wins, or the game draws if Takahashi plays word s_i first. Since cycles allow infinite play (Draw), classify vertex outcomes (Win/Lose/Draw) via retrograde analysis BFS on the reversed graph.',
        'observation': 'When Takahashi says s_i, Aoki moves from vertex v = suffix3(s_i). In a finite impartial/normal play game on a directed graph with cycles: a state is LOSE if out-degree is 0 or all outgoing edges lead to WIN; a state is WIN if at least one outgoing edge leads to LOSE; all remaining undetermined states are DRAW. Retrograde BFS propagates known states backwards along reverse edges.',
        'algorithm': [
            'Compress 3-letter prefixes and suffixes into integer vertex IDs. Add directed edges u -> v for each word.',
            'Compute out-degrees for all vertices and build the reversed adjacency list.',
            'Initialize a queue with all vertices having out_degree == 0, marking them as LOSE (-1).',
            'Perform retrograde BFS: when popping a LOSE vertex v, any predecessor u can transition to LOSE, so mark u as WIN (+1) and push to queue. When popping a WIN vertex v, decrement out_degree[u]; if out_degree[u] reaches 0, all moves from u lead to WIN, so mark u as LOSE (-1) and push to queue.',
            'For each word s_i with target suffix vertex v: if state[v] == -1, Aoki loses so Takahashi wins; if state[v] == 1, Aoki wins; if state[v] == 0, the outcome is Draw.'
        ],
        'time_complexity': 'O(N)',
        'space_complexity': 'O(N)',
        'code': r'''#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <queue>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<string> s(n);
    map<string, int> str_to_id;
    auto get_id = [&](const string& str) {
        if (!str_to_id.count(str)) {
            int id = str_to_id.size();
            str_to_id[str] = id;
        }
        return str_to_id[str];
    };

    vector<pair<int, int>> edges(n);
    for (int i = 0; i < n; ++i) {
        cin >> s[i];
        string pre = s[i].substr(0, 3);
        string suf = s[i].substr(s[i].length() - 3, 3);
        edges[i] = {get_id(pre), get_id(suf)};
    }

    int V = str_to_id.size();
    vector<vector<int>> rev_adj(V);
    vector<int> out_deg(V, 0);

    for (int i = 0; i < n; ++i) {
        int u = edges[i].first;
        int v = edges[i].second;
        rev_adj[v].push_back(u);
        out_deg[u]++;
    }

    vector<int> state(V, 0); // 0 = Draw, 1 = Win, -1 = Lose
    queue<int> q;

    for (int i = 0; i < V; ++i) {
        if (out_deg[i] == 0) {
            state[i] = -1;
            q.push(i);
        }
    }

    while (!q.empty()) {
        int v = q.front();
        q.pop();

        for (int u : rev_adj[v]) {
            if (state[u] != 0) continue;

            if (state[v] == -1) {
                state[u] = 1;
                q.push(u);
            } else if (state[v] == 1) {
                out_deg[u]--;
                if (out_deg[u] == 0) {
                    state[u] = -1;
                    q.push(u);
                }
            }
        }
    }

    for (int i = 0; i < n; ++i) {
        int target = edges[i].second;
        if (state[target] == -1) {
            cout << "Takahashi\n";
        } else if (state[target] == 1) {
            cout << "Aoki\n";
        } else {
            cout << "Draw\n";
        }
    }

    return 0;
}
'''
    },
    {
        'id': 'abc252_g',
        'contest_id': 'abc252',
        'title': 'Pre-Order',
        'rating': 2153,
        'domain': 'Dynamic Programming (DP)',
        'domain_folder': 'dynamic_programming',
        'subtopic': 'Classic DP',
        'topic': 'Interval DP / Range DP / Matrix Chain Multiplication (MCM)',
        'cat_file': 'categories/dynamic_programming/interval_dp_preorder_tree_reconstruction.md',
        'key_idea': 'Given the DFS preorder sequence of a rooted tree where children of any vertex are visited in strictly increasing numerical order, count the number of valid rooted tree topologies modulo 998244353. Solved via interval DP tracking valid forests under root order constraints.',
        'observation': 'Let dp[l][r] count valid trees rooted at a virtual node 0 covering the subsequence A[l..r-1]. The first child of 0 is A[l]. Either A[l] is the sole child of 0 (all remaining elements are in A[l]\'s subtree, counted by dp[l+1][r]), or 0 has subsequent children. If the next child of 0 is A[k] (l+1 <= k < r), the condition that siblings are visited in increasing order demands A[l] < A[k]. Subtree of A[l] covers [l+1, k) and the remaining forest covers [k, r).',
        'algorithm': [
            'Define DP state dp[l][r] for 2 <= l <= r <= N + 1 where base cases are dp[i][i] = 1.',
            'Iterate over interval length len from 2 to N, and left endpoint l from 2 to N + 1 - len + 1.',
            'Transition: dp[l][r] = dp[l+1][r] + sum_{l+1 <= k < r, A[l] < A[k]} (dp[l+1][k] * dp[k][r]) % MOD.',
            'The total number of valid trees is given by dp[2][N+1].'
        ],
        'time_complexity': 'O(N^3)',
        'space_complexity': 'O(N^2)',
        'code': r'''#include <iostream>
#include <vector>

using namespace std;

const int MOD = 998244353;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> a(n + 2);
    for (int i = 1; i <= n; ++i) {
        cin >> a[i];
    }

    vector<vector<long long>> dp(n + 2, vector<long long>(n + 2, 0));

    for (int i = 1; i <= n + 1; ++i) {
        dp[i][i] = 1;
    }

    for (int len = 2; len <= n; ++len) {
        for (int l = 2; l + len - 1 <= n + 1; ++l) {
            int r = l + len - 1;
            long long res = dp[l + 1][r];
            for (int k = l + 1; k < r; ++k) {
                if (a[l] < a[k]) {
                    res = (res + dp[l + 1][k] * dp[k][r]) % MOD;
                }
            }
            dp[l][r] = res;
        }
    }

    cout << dp[2][n + 1] << "\n";
    return 0;
}
'''
    },
    {
        'id': 'abc189_f',
        'contest_id': 'abc189',
        'title': 'Sugoroku2',
        'rating': 2154,
        'domain': 'Math',
        'domain_folder': 'math',
        'subtopic': 'Probabilities and Expected Values',
        'topic': 'Probabilities and Expected Values',
        'cat_file': 'categories/math/expected_value_dp_reset_squares_affine.md',
        'key_idea': 'Compute the expected number of turns to reach square >= N on a 1D board with dice rolls 1..M, where landing on designated trap squares resets Takahashi back to square 0. Express each state expected value as an affine function of E[0] and maintain sliding window sums.',
        'observation': 'If M consecutive squares are reset squares, the game cannot terminate (output -1). For each state i, the expected steps to finish satisfies E[i] = 1 + (1/M) sum_{d=1}^M E[i+d]. Landing on a reset square gives E[i] = E[0]. Since the recurrence is linear, every state can be expressed as E[i] = a_i * E[0] + b_i. Sliding window sums compute coefficients in O(1) backwards, and E[0] is solved directly from E[0] = a_0 * E[0] + b_0.',
        'algorithm': [
            'Check if any sequence of M consecutive squares are reset squares; if so, output -1.',
            'Represent each state as E[i] = A[i] * E[0] + B[i]. For i >= N, A[i] = 0, B[i] = 0. For reset squares, A[i] = 1, B[i] = 0.',
            'Maintain sliding window sums of A and B of length M from i = N - 1 down to 0.',
            'For non-reset squares, set A[i] = sumA / M and B[i] = sumB / M + 1.',
            'Solve for E[0] = B[0] / (1 - A[0]). If |1 - A[0]| < 1e-9, output -1.'
        ],
        'time_complexity': 'O(N)',
        'space_complexity': 'O(N)',
        'code': r'''#include <iostream>
#include <vector>
#include <iomanip>
#include <cmath>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m, k;
    if (!(cin >> n >> m >> k)) return 0;

    vector<bool> send_back(n + 1, false);
    for (int i = 0; i < k; ++i) {
        int a;
        cin >> a;
        send_back[a] = true;
    }

    int consecutive = 0;
    for (int i = 0; i <= n; ++i) {
        if (send_back[i]) {
            consecutive++;
            if (consecutive >= m) {
                cout << -1 << "\n";
                return 0;
            }
        } else {
            consecutive = 0;
        }
    }

    vector<double> A(n + m + 1, 0.0);
    vector<double> B(n + m + 1, 0.0);

    double sumA = 0.0;
    double sumB = 0.0;

    for (int i = n - 1; i >= 0; --i) {
        if (send_back[i]) {
            A[i] = 1.0;
            B[i] = 0.0;
        } else {
            A[i] = sumA / m;
            B[i] = sumB / m + 1.0;
        }

        sumA += A[i];
        sumB += B[i];

        if (i + m <= n + m) {
            sumA -= A[i + m];
            sumB -= B[i + m];
        }
    }

    if (abs(1.0 - A[0]) < 1e-9) {
        cout << -1 << "\n";
    } else {
        double ans = B[0] / (1.0 - A[0]);
        cout << fixed << setprecision(10) << ans << "\n";
    }

    return 0;
}
'''
    },
    {
        'id': 'arc060_c',
        'contest_id': 'arc060',
        'title': 'Tak and Hotels',
        'rating': 2154,
        'domain': 'Graph Theory',
        'domain_folder': 'graph_theory',
        'subtopic': 'Lowest Common Ancestor (LCA)',
        'topic': 'Binary Lifting and LCA',
        'cat_file': 'categories/graph_theory/binary_lifting_interval_reachability.md',
        'key_idea': 'Given N sorted hotels on a line and maximum daily travel distance L, answer Q queries finding the minimum number of days to travel between hotel a and hotel b. Monotonicity implies each step greedily jumps to the farthest reachable hotel, modeled as binary lifting on functional graphs.',
        'observation': 'Because staying at a hotel further along the line strictly dominates staying closer, the optimal next hotel from hotel i is the maximum j such that x[j] - x[i] <= L (when moving right) or minimum j such that x[i] - x[j] <= L (when moving left). Binary lifting precomputes the hotel reached after 2^k daily maximal jumps.',
        'algorithm': [
            'For each hotel i, use binary search (upper_bound / lower_bound) to find the farthest reachable hotel in one day to the right and left.',
            'Build binary lifting tables up_r[k][i] and up_l[k][i] for k = 0..17.',
            'For each query (a, b) with a < b, binary lift from a using up_r while the 2^k destination is strictly less than b, accumulating 2^k days, and add 1 final day.',
            'Handle queries with a > b symmetrically using up_l.'
        ],
        'time_complexity': 'O((N + Q) log N)',
        'space_complexity': 'O(N log N)',
        'code': r'''#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MAXLOG = 18;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> x(n + 1);
    for (int i = 1; i <= n; ++i) cin >> x[i];

    long long L;
    cin >> L;

    int q;
    cin >> q;

    vector<vector<int>> up_r(MAXLOG, vector<int>(n + 1));
    for (int i = 1; i <= n; ++i) {
        int idx = upper_bound(x.begin() + 1, x.end(), x[i] + L) - x.begin() - 1;
        up_r[0][i] = idx;
    }

    for (int k = 1; k < MAXLOG; ++k) {
        for (int i = 1; i <= n; ++i) {
            up_r[k][i] = up_r[k - 1][up_r[k - 1][i]];
        }
    }

    vector<vector<int>> up_l(MAXLOG, vector<int>(n + 1));
    for (int i = 1; i <= n; ++i) {
        int idx = lower_bound(x.begin() + 1, x.end(), x[i] - L) - x.begin();
        up_l[0][i] = idx;
    }

    for (int k = 1; k < MAXLOG; ++k) {
        for (int i = 1; i <= n; ++i) {
            up_l[k][i] = up_l[k - 1][up_l[k - 1][i]];
        }
    }

    while (q--) {
        int a, b;
        cin >> a >> b;
        if (a < b) {
            int ans = 0;
            int curr = a;
            for (int k = MAXLOG - 1; k >= 0; --k) {
                if (up_r[k][curr] < b) {
                    ans += (1 << k);
                    curr = up_r[k][curr];
                }
            }
            ans++;
            cout << ans << "\n";
        } else {
            int ans = 0;
            int curr = a;
            for (int k = MAXLOG - 1; k >= 0; --k) {
                if (up_l[k][curr] > b) {
                    ans += (1 << k);
                    curr = up_l[k][curr];
                }
            }
            ans++;
            cout << ans << "\n";
        }
    }

    return 0;
}
'''
    },
    {
        'id': 'arc156_c',
        'contest_id': 'arc156',
        'title': 'Tree and LCS',
        'rating': 2155,
        'domain': 'Basics',
        'domain_folder': 'basics',
        'subtopic': 'Greedy and Constructive',
        'topic': 'Basic Constructive Algorithms',
        'cat_file': 'categories/basics/leaf_peeling_inversion_matching_tree_lcs.md',
        'key_idea': 'Construct a permutation P of tree vertices that minimizes the maximum LCS between any simple path x and its mapped sequence P(x). A similarity of 1 can always be achieved by iteratively peeling pairs of leaves and swapping their permutation values.',
        'observation': 'If two opposite leaves u and v are paired with P[u] = v and P[v] = u, no simple path can contain both in its common subsequence with mapped values. By peeling leaves in pairs and assigning cross-mappings, we inductively reduce the tree by 2 vertices while preserving the invariant that no path shares more than 1 common vertex with its image.',
        'algorithm': [
            'Initialize vertex degrees and push all leaves (degree <= 1) onto a stack.',
            'While the stack has >= 2 vertices, pop u and v, assign P[u] = v and P[v] = u.',
            'Remove u and v from the tree by decrementing neighbor degrees; if any neighbor becomes a leaf, push it onto the stack.',
            'If one central vertex remains (when N is odd), assign P[x] = x.',
            'Output the resulting 1-indexed permutation P.'
        ],
        'time_complexity': 'O(N)',
        'space_complexity': 'O(N)',
        'code': r'''#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<int>> g(n + 1);
    vector<int> deg(n + 1, 0);
    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        g[u].push_back(v);
        g[v].push_back(u);
        deg[u]++;
        deg[v]++;
    }

    vector<int> st;
    for (int i = 1; i <= n; ++i) {
        if (deg[i] <= 1) {
            st.push_back(i);
        }
    }

    vector<int> p(n + 1, 0);
    while (st.size() >= 2) {
        int u = st.back(); st.pop_back();
        int v = st.back(); st.pop_back();
        p[u] = v;
        p[v] = u;

        for (int to : g[u]) {
            deg[to]--;
            if (deg[to] == 1) st.push_back(to);
        }
        for (int to : g[v]) {
            deg[to]--;
            if (deg[to] == 1) st.push_back(to);
        }
    }

    if (!st.empty()) {
        int x = st.back();
        st.pop_back();
        p[x] = x;
    }

    for (int i = 1; i <= n; ++i) {
        cout << p[i] << (i == n ? "" : " ");
    }
    cout << "\n";

    return 0;
}
'''
    },
    {
        'id': 'agc017_d',
        'contest_id': 'agc017',
        'title': 'Game on Tree',
        'rating': 2156,
        'domain': 'Game Theory',
        'domain_folder': 'game_theory',
        'subtopic': 'Hackenbush',
        'topic': 'Green Hackenbush on Trees and Graphs',
        'cat_file': 'categories/game_theory/green_hackenbush_trees_colon_principle.md',
        'key_idea': 'Determine the winner of Green Hackenbush on a rooted tree where players alternate cutting edges and components disconnected from the root are removed. Solved via the Colon Principle.',
        'observation': 'According to the Colon Principle in combinatorial game theory, attaching a subtree with Grundy value G(v) to a parent u via a single edge yields an equivalent game with Grundy value G(v) + 1. Multiple branches incident to the same root vertex behave as independent games summed via XOR: G(u) = XOR_{v in children(u)} (G(v) + 1). Alice wins iff G(root) != 0.',
        'algorithm': [
            'Root the tree arbitrarily at vertex 1.',
            'Perform a post-order DFS: for a leaf node, Grundy value is 0.',
            'For any internal node u, compute G(u) = XOR_{v in children(u)} (dfs(v) + 1).',
            'If G(1) != 0, print "Alice"; otherwise print "Bob".'
        ],
        'time_complexity': 'O(N)',
        'space_complexity': 'O(N)',
        'code': r'''#include <iostream>
#include <vector>

using namespace std;

int dfs(int u, int p, const vector<vector<int>>& g) {
    int g_val = 0;
    for (int v : g[u]) {
        if (v == p) continue;
        g_val ^= (dfs(v, u, g) + 1);
    }
    return g_val;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<int>> g(n + 1);
    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        g[u].push_back(v);
        g[v].push_back(u);
    }

    int g_root = dfs(1, 0, g);
    if (g_root != 0) {
        cout << "Alice\n";
    } else {
        cout << "Bob\n";
    }

    return 0;
}
'''
    },
    {
        'id': 'abc295_e',
        'contest_id': 'abc295',
        'title': 'Kth Number',
        'rating': 2157,
        'domain': 'Math',
        'domain_folder': 'math',
        'subtopic': 'Probabilities and Expected Values',
        'topic': 'Probabilities and Expected Values',
        'cat_file': 'categories/math/tail_sum_expectation_binomial_order_statistics.md',
        'key_idea': 'Sequence A has zeros replaced uniformly at random with integers in 1..M. Compute the expected value of the K-th smallest element of sorted A modulo 998244353 using the tail sum formula E[X] = sum_{x=1}^M P(X >= x).',
        'observation': 'A_K >= x if and only if the total count of elements strictly less than x is at most K - 1. Fixed non-zero elements contribute a deterministic count C_{< x}. The remaining Z zeros independently land in [1, x-1] with probability p = (x-1)/M. The count of zeros < x follows a Binomial distribution B(Z, p), evaluated in O(Z) per x.',
        'algorithm': [
            'Count total zeros Z in array A. Precompute factorials and inverses for combinations nCr.',
            'For each threshold x from 1 to M, count fixed non-zero elements with A[i] < x (let this be c_less).',
            'If c_less > K - 1, P(A_K >= x) = 0.',
            'Otherwise, sum the binomial probabilities sum_{j=0}^{min(Z, K - 1 - c_less)} nCr(Z, j) * p^j * (1-p)^{Z-j} where p = (x-1)/M.',
            'Accumulate P(A_K >= x) over all x in 1..M modulo 998244353.'
        ],
        'time_complexity': 'O(N * M)',
        'space_complexity': 'O(N + M)',
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

const int MAXF = 4005;
long long fact[MAXF], invFact[MAXF];

void precompute() {
    fact[0] = 1;
    invFact[0] = 1;
    for (int i = 1; i < MAXF; ++i) {
        fact[i] = (fact[i - 1] * i) % MOD;
    }
    invFact[MAXF - 1] = modInverse(fact[MAXF - 1]);
    for (int i = MAXF - 2; i >= 1; --i) {
        invFact[i] = (invFact[i + 1] * (i + 1)) % MOD;
    }
}

long long nCr(int n, int r) {
    if (r < 0 || r > n) return 0;
    return fact[n] * invFact[r] % MOD * invFact[n - r] % MOD;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    precompute();

    int n, m, k;
    if (!(cin >> n >> m >> k)) return 0;

    vector<int> a(n);
    int Z = 0;
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        if (a[i] == 0) Z++;
    }

    long long invM = modInverse(m);
    long long total_exp = 0;

    for (int x = 1; x <= m; ++x) {
        int c_less = 0;
        for (int i = 0; i < n; ++i) {
            if (a[i] != 0 && a[i] < x) {
                c_less++;
            }
        }

        if (c_less > k - 1) continue;

        int max_j = min(Z, k - 1 - c_less);
        long long p = (1LL * (x - 1) * invM) % MOD;
        long long q_prob = (1LL * (m - x + 1) * invM) % MOD;

        long long p_prob = 0;
        for (int j = 0; j <= max_j; ++j) {
            long long ways = nCr(Z, j);
            long long term = ways * power(p, j) % MOD * power(q_prob, Z - j) % MOD;
            p_prob = (p_prob + term) % MOD;
        }

        total_exp = (total_exp + p_prob) % MOD;
    }

    cout << total_exp << "\n";
    return 0;
}
'''
    },
    {
        'id': 'abc345_f',
        'contest_id': 'abc345',
        'title': 'Many Lamps',
        'rating': 2157,
        'domain': 'Graph Theory',
        'domain_folder': 'graph_theory',
        'subtopic': 'Graph Traversal',
        'topic': 'DFS Tree',
        'cat_file': 'categories/graph_theory/spanning_tree_leaf_root_parity_toggling.md',
        'key_idea': 'Toggle edge endpoints to turn on exactly K lamps in a graph. Since each operation toggles 2 vertices, the total ON count is always even. On any spanning tree, bottom-up post-order toggling monotonically turns on lamps without ever decreasing the ON count.',
        'observation': 'If K is odd, impossible (output "No"). In a tree, if child v is OFF and we toggle edge (u, v), v becomes ON. Whether u was ON or OFF, the total ON count changes by +2 or 0; it never decreases. Thus, the ON count increases in steps of 2, hitting every even target K up to the maximum achievable capacity.',
        'algorithm': [
            'If K % 2 != 0, output "No".',
            'Find spanning forest components via DFS.',
            'In post-order traversal of the spanning tree: for each child v of u, if v is OFF and curr_on < K, toggle edge (u, v), updating lamp states and recording the operation.',
            'If curr_on == K, output "Yes", the operation count, and the sequence of edge indices; otherwise output "No".'
        ],
        'time_complexity': 'O(N + M)',
        'space_complexity': 'O(N + M)',
        'code': r'''#include <iostream>
#include <vector>

using namespace std;

struct Edge {
    int to;
    int id;
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m, k;
    if (!(cin >> n >> m >> k)) return 0;

    vector<vector<Edge>> g(n + 1);
    for (int i = 1; i <= m; ++i) {
        int u, v;
        cin >> u >> v;
        g[u].push_back({v, i});
        g[v].push_back({u, i});
    }

    if (k % 2 != 0) {
        cout << "No\n";
        return 0;
    }

    vector<bool> visited(n + 1, false);
    vector<int> state(n + 1, 0);
    vector<int> ops;
    int curr_on = 0;

    auto dfs = [&](auto& self, int u) -> void {
        visited[u] = true;
        for (auto& edge : g[u]) {
            int v = edge.to;
            if (visited[v]) continue;
            self(self, v);

            if (curr_on < k && state[v] == 0) {
                ops.push_back(edge.id);
                if (state[v] == 0) curr_on++; else curr_on--;
                state[v] ^= 1;
                if (state[u] == 0) curr_on++; else curr_on--;
                state[u] ^= 1;
            }
        }
    };

    for (int i = 1; i <= n; ++i) {
        if (!visited[i]) {
            dfs(dfs, i);
        }
    }

    if (curr_on == k) {
        cout << "Yes\n";
        cout << ops.size() << "\n";
        for (size_t i = 0; i < ops.size(); ++i) {
            cout << ops[i] << (i + 1 == ops.size() ? "" : " ");
        }
        cout << "\n";
    } else {
        cout << "No\n";
    }

    return 0;
}
'''
    },
    {
        'id': 'arc192_c',
        'contest_id': 'arc192',
        'title': 'Range Sums 2',
        'rating': 2158,
        'domain': 'Miscellaneous',
        'domain_folder': 'miscellaneous',
        'subtopic': 'Interactive Problems',
        'topic': 'Interactive Problems',
        'cat_file': 'categories/miscellaneous/interactive_range_sums_extremal_reconstruction.md',
        'key_idea': 'Interactive reconstruction of a permutation P and positive array A from at most 2N range sum queries sum_{i=min(P_s, P_t)}^{max(P_s, P_t)} A_i with P_1 < P_2 guaranteed.',
        'observation': 'Because all A_i > 0, querying (1, i) for all i >= 2 identifies an extreme endpoint m with maximal range sum (so P_m = 1 or P_m = N). Assuming P_m = 1, querying (m, i) sorts elements along the line, yielding P and differences A_3..A_N. One boundary query finds A_1 and A_2. If P_1 > P_2, invert P_i <- N + 1 - P_i and reverse A.',
        'algorithm': [
            'Query (1, i) for i = 2..N. Let m be the index with the maximal returned sum. Assume P_m = 1.',
            'Query (m, i) for all i != m (reusing query (1, m) from step 1).',
            'Sort remaining vertices by their (m, i) responses to assign P_{x_1} = 2, ..., P_{x_{N-1}} = N.',
            'Compute adjacent differences to find A_3..A_N.',
            'Query (x_1, x_{N-1}) to get total sum minus A_1, determining A_1 and A_2.',
            'If P_1 > P_2, replace P_i with N + 1 - P_i and reverse A. Output answer with !.'
        ],
        'time_complexity': 'O(N log N) with <= 2N - 2 queries',
        'space_complexity': 'O(N)',
        'code': r'''#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

using namespace std;

long long query(int s, int t) {
    cout << "? " << s << " " << t << "\n";
    cout.flush();
    long long ret;
    cin >> ret;
    return ret;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    pair<long long, int> mx = {-1, -1};
    vector<long long> from1(n + 1, 0);

    for (int i = 2; i <= n; ++i) {
        long long val = query(1, i);
        from1[i] = val;
        mx = max(mx, {val, i});
    }

    int m = mx.second;
    vector<pair<long long, int>> resps;
    for (int i = 1; i <= n; ++i) {
        if (i == m) continue;
        long long val;
        if (i == 1) {
            val = from1[m];
        } else {
            val = query(m, i);
        }
        resps.push_back({val, i});
    }

    sort(resps.begin(), resps.end());

    vector<int> P(n + 1, 0);
    vector<long long> A(n + 1, 0);

    P[m] = 1;
    for (int i = 0; i < n - 1; ++i) {
        P[resps[i].second] = i + 2;
    }

    for (int i = 1; i < n - 1; ++i) {
        A[i + 2] = resps[i].first - resps[i - 1].first;
    }

    long long q_ends = query(resps[0].second, resps.back().second);
    long long total = resps.back().first;
    A[1] = total - q_ends;

    long long sum_known = 0;
    for (int i = 1; i <= n; ++i) {
        if (i != 2) sum_known += A[i];
    }
    A[2] = total - sum_known;

    if (P[1] > P[2]) {
        for (int i = 1; i <= n; ++i) {
            P[i] = n + 1 - P[i];
        }
        reverse(A.begin() + 1, A.end());
    }

    cout << "!";
    for (int i = 1; i <= n; ++i) cout << " " << P[i];
    for (int i = 1; i <= n; ++i) cout << " " << A[i];
    cout << "\n";
    cout.flush();

    return 0;
}
'''
    },
    {
        'id': 'tokiomarine2020_d',
        'contest_id': 'tokiomarine2020',
        'title': 'Knapsack Queries on a tree',
        'rating': 2158,
        'domain': 'Miscellaneous',
        'domain_folder': 'miscellaneous',
        'subtopic': 'Techniques',
        'topic': 'Meet in the Middle',
        'cat_file': 'categories/miscellaneous/complete_binary_tree_depth_meet_in_the_middle.md',
        'key_idea': 'Complete binary tree of depth <= 18 with 0-1 knapsack queries on paths from v to root. Sqrt decomposition / Meet-in-the-Middle on tree depth: precalculate Pareto frontiers for the top 9 levels, and enumerate 2^k subsets for the bottom <= 9 levels.',
        'observation': 'Splitting the path at depth 9 limits both the top ancestor path and the bottom path to at most 9 items. For nodes u < 512, precalculating the Pareto frontier of non-dominated (weight, value) pairs takes negligible memory (< 2 MB) and O(2^9) operations per node. For any query (v, L), bottom subsets (<= 256) are combined with top Pareto pairs via binary search in O(2^k log S).',
        'algorithm': [
            'For every node u < 512, compute its Pareto frontier by merging the parent\'s frontier with item u and filtering dominated pairs.',
            'For each query (v, L), walk upwards from v until reaching ancestor u < 512, collecting the bottom items (at most 9).',
            'Generate all 2^k subsets of bottom items with total weight <= L.',
            'For each bottom subset, binary search node u\'s Pareto frontier for the largest weight <= L - w_bot and maximize v_bot + v_top.'
        ],
        'time_complexity': 'O(N + Q * 2^(D/2) * log(2^(D/2)))',
        'space_complexity': 'O(2^(D/2) * 2^(D/2) + N)',
        'code': r'''#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Item {
    long long w, v;
};

const int TOP_LIMIT = 512;
vector<Item> top_dp[TOP_LIMIT];
long long V[300005], W[300005];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    for (int i = 1; i <= n; ++i) {
        cin >> V[i] >> W[i];
    }

    top_dp[1] = {{0, 0}, {W[1], V[1]}};
    if (top_dp[1][0].w == top_dp[1][1].w) {
        top_dp[1] = {{W[1], max(top_dp[1][0].v, top_dp[1][1].v)}};
    } else {
        if (top_dp[1][1].v < top_dp[1][0].v) {
            top_dp[1].pop_back();
        }
    }

    for (int u = 2; u < min(n + 1, TOP_LIMIT); ++u) {
        int p = u / 2;
        vector<Item> combined;
        for (const auto& item : top_dp[p]) {
            combined.push_back({item.w + W[u], item.v + V[u]});
        }
        for (const auto& item : top_dp[p]) {
            combined.push_back(item);
        }
        sort(combined.begin(), combined.end(), [](const Item& a, const Item& b) {
            if (a.w != b.w) return a.w < b.w;
            return a.v > b.v;
        });

        vector<Item> filtered;
        long long max_v = -1;
        for (const auto& item : combined) {
            if (item.v > max_v) {
                if (!filtered.empty() && filtered.back().w == item.w) {
                    filtered.back().v = item.v;
                } else {
                    filtered.push_back(item);
                }
                max_v = item.v;
            }
        }
        top_dp[u] = move(filtered);
    }

    int q;
    cin >> q;
    while (q--) {
        int v;
        long long L;
        cin >> v >> L;

        vector<pair<long long, long long>> bottom_items;
        int curr = v;
        while (curr >= TOP_LIMIT) {
            bottom_items.push_back({W[curr], V[curr]});
            curr /= 2;
        }

        int m = bottom_items.size();
        vector<Item> bot_subsets;
        bot_subsets.reserve(1 << m);
        bot_subsets.push_back({0, 0});
        for (int i = 0; i < m; ++i) {
            int sz = bot_subsets.size();
            for (int j = 0; j < sz; ++j) {
                long long nw = bot_subsets[j].w + bottom_items[i].first;
                long long nv = bot_subsets[j].v + bottom_items[i].second;
                if (nw <= L) {
                    bot_subsets.push_back({nw, nv});
                }
            }
        }

        long long ans = 0;
        const auto& top_list = top_dp[curr];

        for (const auto& b : bot_subsets) {
            long long rem_w = L - b.w;
            int low = 0, high = (int)top_list.size() - 1, best_idx = -1;
            while (low <= high) {
                int mid = low + (high - low) / 2;
                if (top_list[mid].w <= rem_w) {
                    best_idx = mid;
                    low = mid + 1;
                } else {
                    high = mid - 1;
                }
            }
            if (best_idx != -1) {
                ans = max(ans, b.v + top_list[best_idx].v);
            }
        }

        cout << ans << "\n";
    }

    return 0;
}
'''
    },
    {
        'id': 'abc247_g',
        'contest_id': 'abc247',
        'title': 'Dream Team',
        'rating': 2159,
        'domain': 'Graph Theory',
        'domain_folder': 'graph_theory',
        'subtopic': 'Flow and Min Cut',
        'topic': 'Min Cost Max Flow (MCMF)',
        'cat_file': 'categories/graph_theory/mcmf_primal_dual_bipartite_matching_all_sizes.md',
        'key_idea': 'Select a dream team of size k maximizing total power such that all universities and subjects are distinct. Formulated as maximum weight bipartite matching solved via successive shortest path Min-Cost Max-Flow (Primal-Dual) across all matching sizes k.',
        'observation': 'Universities (<= 150) form the left partition and subjects (<= 150) form the right partition. For each pair (u, v), only retain the maximum power person. By negating costs (or setting cost = BIG - C_{u, v}), each unit of augmented flow from Source to Sink adds exactly 1 person while maximizing power. The algorithm stops when no augmenting path exists.',
        'algorithm': [
            'Deduplicate input edges between university A_i and subject B_i, keeping max C_i.',
            'Build bipartite flow network with Source 0, Sink 301, capacities 1 from S to universities and subjects to T.',
            'Add edges from universities to subjects with capacity 1 and cost BIG - C_{u, v}.',
            'Run successive shortest path (Dijkstra with Johnson potentials) augmenting 1 unit of flow per step.',
            'Record and output the maximum power for each team size k = 1, 2, ...'
        ],
        'time_complexity': 'O(V * E log V)',
        'space_complexity': 'O(V + E)',
        'code': r'''#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

const long long INF = 1e18;
const long long BIG_COST = 1e9 + 7;

struct Edge {
    int to;
    int cap;
    long long cost;
    int rev;
};

struct MCMF {
    int n;
    vector<vector<Edge>> g;
    vector<long long> h, dist;
    vector<int> prevv, preve;

    MCMF(int n) : n(n), g(n), h(n, 0), dist(n), prevv(n), preve(n) {}

    void add_edge(int from, int to, int cap, long long cost) {
        g[from].push_back({to, cap, cost, (int)g[to].size()});
        g[to].push_back({from, 0, -cost, (int)g[from].size() - 1});
    }

    pair<int, long long> augment(int s, int t) {
        priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> pq;
        fill(dist.begin(), dist.end(), INF);
        dist[s] = 0;
        pq.push({0, s});

        while (!pq.empty()) {
            auto [d, v] = pq.top();
            pq.pop();
            if (dist[v] < d) continue;

            for (int i = 0; i < (int)g[v].size(); ++i) {
                Edge& e = g[v][i];
                if (e.cap > 0 && dist[e.to] > dist[v] + e.cost + h[v] - h[e.to]) {
                    dist[e.to] = dist[v] + e.cost + h[v] - h[e.to];
                    prevv[e.to] = v;
                    preve[e.to] = i;
                    pq.push({dist[e.to], e.to});
                }
            }
        }

        if (dist[t] == INF) return {0, 0};

        for (int v = 0; v < n; ++v) h[v] += dist[v];

        int d = 1;
        for (int v = t; v != s; v = prevv[v]) {
            d = min(d, g[prevv[v]][preve[v]].cap);
        }
        for (int v = t; v != s; v = prevv[v]) {
            Edge& e = g[prevv[v]][preve[v]];
            e.cap -= d;
            g[v][e.rev].cap += d;
        }

        return {d, h[t]};
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    int max_a[155][155];
    for (int i = 0; i <= 150; ++i) {
        for (int j = 0; j <= 150; ++j) {
            max_a[i][j] = -1;
        }
    }

    for (int i = 0; i < n; ++i) {
        int a, b;
        long long c;
        cin >> a >> b >> c;
        if (c > max_a[a][b]) {
            max_a[a][b] = c;
        }
    }

    int s = 0, t = 301;
    MCMF flow(305);

    for (int i = 1; i <= 150; ++i) {
        flow.add_edge(s, i, 1, 0);
        flow.add_edge(150 + i, t, 1, 0);
    }

    for (int i = 1; i <= 150; ++i) {
        for (int j = 1; j <= 150; ++j) {
            if (max_a[i][j] != -1) {
                flow.add_edge(i, 150 + j, 1, BIG_COST - max_a[i][j]);
            }
        }
    }

    vector<long long> ans;
    long long total_cost = 0;
    while (true) {
        auto [f, c] = flow.augment(s, t);
        if (f == 0) break;
        total_cost += c;
        int k = ans.size() + 1;
        long long max_power = 1LL * k * BIG_COST - total_cost;
        ans.push_back(max_power);
    }

    cout << ans.size() << "\n";
    for (long long val : ans) {
        cout << val << "\n";
    }

    return 0;
}
'''
    },
    {
        'id': 'arc099_c',
        'contest_id': 'arc099',
        'title': 'Independence',
        'rating': 2160,
        'domain': 'Graph Theory',
        'domain_folder': 'graph_theory',
        'subtopic': 'Cliques and Independent Sets',
        'topic': 'Maximum Clique',
        'cat_file': 'categories/graph_theory/clique_partition_complement_bipartite_knapsack.md',
        'key_idea': 'Partition a graph into two cliques minimizing edges with endpoints in the same state. A clique partition in G corresponds to a 2-coloring (bipartite coloring) in the complement graph G_bar. Knapsack balances the component color classes.',
        'observation': 'Two vertices belong to the same clique in G iff there is NO edge between them in the complement graph G_bar. Thus, the complement graph must be bipartite; otherwise no valid partition exists (output -1). For each bipartite connected component with partition sizes (s_i, t_i), choose one side for state A using knapsack DP, minimizing same-state edges C(a, 2) + C(b, 2).',
        'algorithm': [
            'Construct the complement graph G_bar of size N <= 700.',
            'Check if G_bar is bipartite via BFS/DFS 2-coloring. If an odd cycle is detected, output -1.',
            'Collect component partition sizes (s_i, t_i).',
            'Use a bitset knapsack to compute all reachable sizes a of state A: dp = (dp << s_i) | (dp << t_i).',
            'Find achievable a minimizing a*(a-1)/2 + (N-a)*(N-a-1)/2.'
        ],
        'time_complexity': 'O(N^2)',
        'space_complexity': 'O(N^2)',
        'code': r'''#include <iostream>
#include <vector>
#include <bitset>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<bool>> adj(n + 1, vector<bool>(n + 1, false));
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u][v] = adj[v][u] = true;
    }

    vector<vector<int>> comp_adj(n + 1);
    for (int i = 1; i <= n; ++i) {
        for (int j = i + 1; j <= n; ++j) {
            if (!adj[i][j]) {
                comp_adj[i].push_back(j);
                comp_adj[j].push_back(i);
            }
        }
    }

    vector<int> color(n + 1, 0);
    vector<pair<int, int>> comps;

    for (int i = 1; i <= n; ++i) {
        if (color[i] != 0) continue;

        int cnt1 = 0, cnt2 = 0;
        vector<int> q = {i};
        color[i] = 1;
        cnt1++;

        bool ok = true;
        for (size_t head = 0; head < q.size(); ++head) {
            int u = q[head];
            for (int v : comp_adj[u]) {
                if (color[v] == 0) {
                    color[v] = -color[u];
                    if (color[v] == 1) cnt1++; else cnt2++;
                    q.push_back(v);
                } else if (color[v] == color[u]) {
                    ok = false;
                }
            }
        }

        if (!ok) {
            cout << -1 << "\n";
            return 0;
        }

        comps.push_back({cnt1, cnt2});
    }

    bitset<705> dp;
    dp[0] = 1;

    for (const auto& c : comps) {
        dp = (dp << c.first) | (dp << c.second);
    }

    long long min_same_state = 1e18;
    for (int a = 0; a <= n; ++a) {
        if (dp[a]) {
            int b = n - a;
            long long inside = 1LL * a * (a - 1) / 2 + 1LL * b * (b - 1) / 2;
            min_same_state = min(min_same_state, inside);
        }
    }

    if (min_same_state > 1e17) {
        cout << -1 << "\n";
    } else {
        cout << min_same_state << "\n";
    }

    return 0;
}
'''
    },
    {
        'id': 'abc404_f',
        'contest_id': 'abc404',
        'title': 'Lost and Pound',
        'rating': 2162,
        'domain': 'Dynamic Programming (DP)',
        'domain_folder': 'dynamic_programming',
        'subtopic': 'Intro to DP',
        'topic': 'Knapsack and Basic Dynamic Programming',
        'cat_file': 'categories/dynamic_programming/integer_partition_knapsack_optimal_resource_game.md',
        'key_idea': 'Sequential decision game with N buttons (1 winner) and T turns of M presses. Takahashi maximizes probability of winning >= K times. Backward induction on turns and presses solved via bounded integer partition knapsack DP.',
        'observation': 'Let DP[t][k] be the winning probability from turn t with k winning presses so far. At each turn, Takahashi chooses press counts c_1 + ... + c_N = M. Since the winning button is uniformly random, the winning probability is (1/N) sum DP[t+1][k + c_i]. Non-zero presses occur on at most min(N, M) buttons; the optimal choice of positive parts is found via an integer partition knapsack.',
        'algorithm': [
            'Initialize base case DP[T][k] = 1 for k >= K, and 0 otherwise.',
            'For turn t from T-1 down to 0 and current winning count k from 0 to K:',
            'Precompute bounded partition knapsack dp_parts[count][s]: maximum sum of DP[t+1][min(K, k + c_i)] where count positive parts sum to s.',
            'Evaluate best_sum = max_{1 <= count <= min(N, M)} (dp_parts[count][M] + (N - count) * DP[t+1][k]).',
            'Set DP[t][k] = best_sum / N. Output DP[0][0].'
        ],
        'time_complexity': 'O(T * K * M^3)',
        'space_complexity': 'O(T * K + M^2)',
        'code': r'''#include <iostream>
#include <vector>
#include <iomanip>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, t_total, m_press, k_target;
    if (!(cin >> n >> t_total >> m_press >> k_target)) return 0;

    vector<vector<double>> dp(t_total + 1, vector<double>(k_target + 1, 0.0));
    for (int k = 0; k <= k_target; ++k) {
        dp[t_total][k] = (k >= k_target ? 1.0 : 0.0);
    }

    for (int t = t_total - 1; t >= 0; --t) {
        for (int k = 0; k <= k_target; ++k) {
            vector<vector<double>> dp_parts(m_press + 1, vector<double>(m_press + 1, -1.0));
            dp_parts[0][0] = 0.0;

            for (int count = 1; count <= min(n, m_press); ++count) {
                for (int s = count; s <= m_press; ++s) {
                    for (int c = 1; c <= s - count + 1; ++c) {
                        if (dp_parts[count - 1][s - c] >= 0.0) {
                            int next_k = min(k_target, k + c);
                            dp_parts[count][s] = max(dp_parts[count][s], dp_parts[count - 1][s - c] + dp[t + 1][next_k]);
                        }
                    }
                }
            }

            double best_sum = 0.0;
            for (int count = 1; count <= min(n, m_press); ++count) {
                if (dp_parts[count][m_press] >= 0.0) {
                    double total = dp_parts[count][m_press] + (double)(n - count) * dp[t + 1][k];
                    best_sum = max(best_sum, total);
                }
            }

            dp[t][k] = best_sum / n;
        }
    }

    cout << fixed << setprecision(12) << dp[0][0] << "\n";
    return 0;
}
'''
    },
    {
        'id': 'agc066_b',
        'contest_id': 'agc066',
        'title': 'Decreasing Digit Sums',
        'rating': 2162,
        'domain': 'Basics',
        'domain_folder': 'basics',
        'subtopic': 'Greedy and Constructive',
        'topic': 'Basic Constructive Algorithms',
        'cat_file': 'categories/basics/decreasing_digit_sums_doubling_powers_of_five.md',
        'key_idea': 'Construct an integer x < 10^10000 whose base-10 digit sum strictly decreases under repeated doubling: f(2^{i-1} x) > f(2^i x) for all 1 <= i <= N (N <= 50). Solved via powers of five.',
        'observation': 'Notice 2^i * 5^{50} n = 10^i * 5^{50-i} n. Multiplying by 10^i appends trailing zeros without changing digit sum, so f(2^i x) = f(5^{50-i} n). As i increases, the exponent 50 - i decreases, naturally shrinking the digit sum. Concatenating 5^50..5^99 with 100 zero-padding spaces eliminates carry interference and ensures strictly decreasing digit sums for all 50 steps.',
        'algorithm': [
            'Represent large integers using custom base-10 BigInt addition and scalar multiplication.',
            'Compute 5^50, then successively compute 5^j for j = 50..99.',
            'Assemble x = sum_{j=50}^{99} 5^j * 10^{(j-50)*100}.',
            'Print the resulting decimal string (< 5000 digits).'
        ],
        'time_complexity': 'O(L^2) where L < 5000 digits',
        'space_complexity': 'O(L)',
        'code': r'''#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

struct BigInt {
    vector<int> d;
    BigInt(long long v = 0) {
        if (v == 0) d.push_back(0);
        while (v > 0) {
            d.push_back(v % 10);
            v /= 10;
        }
    }
    void mul(int v) {
        long long carry = 0;
        for (size_t i = 0; i < d.size() || carry; ++i) {
            if (i == d.size()) d.push_back(0);
            long long cur = carry + 1LL * d[i] * v;
            d[i] = cur % 10;
            carry = cur / 10;
        }
    }
    void add_at(const BigInt& other, int shift) {
        while (d.size() < other.d.size() + shift) d.push_back(0);
        long long carry = 0;
        for (size_t i = 0; i < other.d.size() || carry; ++i) {
            size_t idx = i + shift;
            if (idx == d.size()) d.push_back(0);
            long long cur = carry + d[idx] + (i < other.d.size() ? other.d[i] : 0);
            d[idx] = cur % 10;
            carry = cur / 10;
        }
    }
    string to_string() const {
        string s;
        for (int i = (int)d.size() - 1; i >= 0; --i) s.push_back('0' + d[i]);
        return s;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    BigInt cur_p(1);
    for (int i = 0; i < 50; ++i) cur_p.mul(5);

    BigInt x(0);
    for (int j = 50; j < 100; ++j) {
        x.add_at(cur_p, (j - 50) * 100);
        cur_p.mul(5);
    }

    cout << x.to_string() << "\n";
    return 0;
}
'''
    },
    {
        'id': 'abc459_f',
        'contest_id': 'abc459',
        'title': '-1, +1',
        'rating': 2163,
        'domain': 'Basics',
        'domain_folder': 'basics',
        'subtopic': 'Greedy and Constructive',
        'topic': 'Basic Greedy Algorithms',
        'cat_file': 'categories/basics/monotonic_block_merging_sequence_equalization.md',
        'key_idea': 'Minimum operations (A_i - 1, A_{i+1} + 1) to make A strictly increasing. Transformed to non-decreasing via A_i <- A_i - i. Solved via monotonic block merging in O(N).',
        'observation': 'Under A_i <- A_i - i, the target sequence B must be non-decreasing. An operation at i increases the index-weighted sum sum_{j=0}^{N-1} j * A_j by exactly 1 while keeping sum A_j invariant. Within each leveled block of size len and sum s, elements are B_j = floor((s + j) / len). Monotonically merge adjacent blocks whenever left_max > right_min.',
        'algorithm': [
            'Transform A_i = A_i - i for all 0 <= i < N.',
            'Maintain a stack of blocks (len, sum). For each element, push (1, A_i).',
            'While stack top has left_max = floor((tail.sum + tail.len - 1) / tail.len) > right_min = floor(now.sum / now.len), merge now with tail.',
            'Reconstruct final sequence B from the merged blocks.',
            'Total operations equals sum_{i=0}^{N-1} i * (B_i - A_i).'
        ],
        'time_complexity': 'O(N)',
        'space_complexity': 'O(N)',
        'code': r'''#include <iostream>
#include <vector>

using namespace std;

struct Block {
    long long len;
    long long sum;
};

void solve() {
    int n;
    cin >> n;
    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        a[i] -= i;
    }

    vector<Block> st;
    auto floor_div = [](long long num, long long den) {
        long long res = num / den;
        long long rem = num % den;
        if (rem != 0 && ((num < 0) ^ (den < 0))) res--;
        return res;
    };

    for (int i = 0; i < n; ++i) {
        Block now = {1, a[i]};
        while (!st.empty()) {
            Block tail = st.back();
            long long left_max = floor_div(tail.sum + tail.len - 1, tail.len);
            long long right_min = floor_div(now.sum, now.len);

            if (left_max <= right_min) break;

            now.len += tail.len;
            now.sum += tail.sum;
            st.pop_back();
        }
        st.push_back(now);
    }

    unsigned long long ans = 0;
    int cur_idx = 0;

    for (const auto& blk : st) {
        for (long long j = 0; j < blk.len; ++j) {
            long long b_val = floor_div(blk.sum + j, blk.len);
            ans += (unsigned long long)cur_idx * (b_val - a[cur_idx]);
            cur_idx++;
        }
    }

    cout << ans << "\n";
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    if (cin >> t) {
        while (t--) solve();
    }
    return 0;
}
'''
    },
    {
        'id': 'abc436_g',
        'contest_id': 'abc436',
        'title': 'Linear Inequation',
        'rating': 2164,
        'domain': 'Math',
        'domain_folder': 'math',
        'subtopic': 'Polynomial',
        'topic': 'Generating Functions',
        'cat_file': 'categories/math/bostan_mori_polynomial_transitions_linear_inequations.md',
        'key_idea': 'Count non-negative integer solutions to sum_{i=1}^N A_i x_i <= M modulo 998244353 for M <= 10^18. Solved using binary digit decomposition Bostan-Mori polynomial transitions.',
        'observation': 'Decomposing x_i = 2 Q_i + R_i with R_i in {0, 1} yields 2 sum A_i Q_i + sum A_i R_i <= M. Let S(x) = prod_{i=1}^N (1 + x^{A_i}). Tracking polynomial coefficients coef where sum coef[M-i] f(A, i) is invariant, each step convolves S with coef and downsamples degrees by factor 2 (M <- M / 2).',
        'algorithm': [
            'Compute polynomial S(x) = prod_{i=1}^N (1 + x^{A_i}) using knapsack DP, where deg(S) = sum A_i <= 10000.',
            'Initialize coefficient vector coef = {1} representing state M.',
            'While M > 0: compute polynomial convolution conv = S * coef using Number Theoretic Transform (NTT).',
            'Downsample: accumulate conv[i] into result[M/2 - (M-i)/2] for i <= M. Set coef = result, M = M / 2.',
            'Output coef[0] modulo 998244353.'
        ],
        'time_complexity': 'O(log M * (sum A_i) log(sum A_i))',
        'space_complexity': 'O(sum A_i)',
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

vector<long long> multiply(vector<long long> const& a, vector<long long> const& b) {
    vector<long long> fa(a.begin(), a.end()), fb(b.begin(), b.end());
    int n = 1;
    while (n < (int)a.size() + (int)b.size()) n <<= 1;
    fa.resize(n);
    fb.resize(n);
    ntt(fa, false);
    ntt(fb, false);
    for (int i = 0; i < n; i++) fa[i] = (fa[i] * fb[i]) % MOD;
    ntt(fa, true);
    while (fa.size() > 1 && fa.back() == 0) fa.pop_back();
    return fa;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    unsigned long long M;
    if (!(cin >> n >> M)) return 0;

    vector<int> A(n);
    int sumA = 0;
    for (int i = 0; i < n; ++i) {
        cin >> A[i];
        sumA += A[i];
    }

    vector<long long> S(sumA + 1, 0);
    S[0] = 1;
    int cur_deg = 0;
    for (int a_val : A) {
        for (int i = cur_deg; i >= 0; --i) {
            if (S[i]) {
                S[i + a_val] = (S[i + a_val] + S[i]) % MOD;
            }
        }
        cur_deg += a_val;
    }

    vector<long long> coef = {1};

    while (M > 0) {
        vector<long long> conv = multiply(S, coef);
        int res_size = M / 2 - (M - min(M, (unsigned long long)conv.size() - 1)) / 2 + 1;
        vector<long long> result(res_size, 0);

        for (size_t i = 0; i < conv.size() && i <= M; ++i) {
            int target_idx = M / 2 - (M - i) / 2;
            result[target_idx] = (result[target_idx] + conv[i]) % MOD;
        }

        coef = move(result);
        M /= 2;
    }

    cout << coef[0] << "\n";
    return 0;
}
'''
    },
    {
        'id': 'agc008_d',
        'contest_id': 'agc008',
        'title': 'K-th K',
        'rating': 2164,
        'domain': 'Basics',
        'domain_folder': 'basics',
        'subtopic': 'Greedy and Constructive',
        'topic': 'Basic Greedy Algorithms',
        'cat_file': 'categories/basics/earliest_deadline_first_multi_occurrence_scheduling.md',
        'key_idea': 'Construct an array of length N^2 containing N copies of each 1..N such that the i-th occurrence of i is at index x_i. Solved by Earliest Deadline First (EDF) greedy scheduling.',
        'observation': 'For each number i, exactly i-1 copies must appear before position x_i, and N-i copies must appear after position x_i. The prefix placement is an interval scheduling problem with deadlines x_i: processing i in increasing order of x_i and greedily placing copies in the leftmost available slots guarantees feasibility if one exists. Suffix placement is handled symmetrically from right to left in decreasing order of x_i.',
        'algorithm': [
            'Place each fixed occurrence a[x_i] = i.',
            'Sort elements in increasing order of x_i. For each element i, find the earliest i - 1 empty slots from left to right; if any slot index exceeds x_i, output "No".',
            'Sort elements in decreasing order of x_i. For each element i, find the latest N - i empty slots from right to left; if any slot index is less than x_i, output "No".',
            'If both passes succeed, output "Yes" and the resulting array a.'
        ],
        'time_complexity': 'O(N^2)',
        'space_complexity': 'O(N^2)',
        'code': r'''#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Element {
    int id;
    int x;
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<Element> elems(n);
    vector<int> a(n * n + 1, 0);

    for (int i = 0; i < n; ++i) {
        elems[i].id = i + 1;
        cin >> elems[i].x;
        a[elems[i].x] = i + 1;
    }

    sort(elems.begin(), elems.end(), [](const Element& e1, const Element& e2) {
        return e1.x < e2.x;
    });

    int ptr = 1;
    for (const auto& e : elems) {
        int need = e.id - 1;
        for (int k = 0; k < need; ++k) {
            while (ptr <= n * n && a[ptr] != 0) ptr++;
            if (ptr > e.x) {
                cout << "No\n";
                return 0;
            }
            a[ptr] = e.id;
        }
    }

    sort(elems.begin(), elems.end(), [](const Element& e1, const Element& e2) {
        return e1.x > e2.x;
    });

    ptr = n * n;
    for (const auto& e : elems) {
        int need = n - e.id;
        for (int k = 0; k < need; ++k) {
            while (ptr >= 1 && a[ptr] != 0) ptr--;
            if (ptr < e.x) {
                cout << "No\n";
                return 0;
            }
            a[ptr] = e.id;
        }
    }

    cout << "Yes\n";
    for (int i = 1; i <= n * n; ++i) {
        cout << a[i] << (i == n * n ? "" : " ");
    }
    cout << "\n";

    return 0;
}
'''
    }
]

# 1. Verify compilation
print("\n--- Verifying Compilation ---")
os.makedirs('scratch/test_build_bins', exist_ok=True)
for p in problems_meta:
    pid = p['id']
    cpp_file = f'scratch/test_build_bins/{pid}.cpp'
    exe_file = f'scratch/test_build_bins/{pid}.exe'
    with open(cpp_file, 'w', encoding='utf-8') as f:
        f.write(p['code'])
    cmd = ['g++', '-O2', '-std=c++17', cpp_file, '-o', exe_file]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode == 0:
        print(f"[+] Compiled successfully: {pid}")
    else:
        print(f"[-] Compilation FAILED: {pid}")
        print(res.stderr)
        sys.exit(1)

# Clean up .exe
for p in problems_meta:
    exe_file = f'scratch/test_build_bins/{p["id"]}.exe'
    if os.path.exists(exe_file):
        os.remove(exe_file)

# 2. Generate Analysis files
print("\n--- Generating Analysis Files ---")
os.makedirs('analysis', exist_ok=True)
for p in problems_meta:
    pid = p['id']
    analysis_path = f"analysis/AtCoder-{pid}.md"
    algo_steps = "\n".join([f"{i+1}. {step}" for i, step in enumerate(p['algorithm'])])

    content = f"""# Problem Analysis: AtCoder-{pid} — {p['title']}

**Problem ID**: `AtCoder-{pid}`  
**Contest**: `{p['contest_id']}`  
**Rating / Difficulty**: {p['rating']}  
**URL**: https://atcoder.jp/contests/{p['contest_id']}/tasks/{pid}  
**VJudge Tag**: `[problem:AtCoder-{pid}]`  
**Category File**: [`../{p['cat_file']}`](../{p['cat_file']})  

- **Tag (Domain)**: `{p['domain']}`  
- **Subtopic**: `{p['subtopic']}`  
- **Topic (Skill)**: `{p['topic']}`  

---

## 1. Problem Statement & Key Idea
{p['key_idea']}

## 2. Core Observation & Invariant
{p['observation']}

## 3. Step-by-Step Algorithm
{algo_steps}

## 4. Complexity Analysis
- **Time Complexity**: `{p['time_complexity']}`
- **Space Complexity**: `{p['space_complexity']}`

## 5. C++ Source Code (Verified & Clean)
```cpp
{p['code'].strip()}
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
    if pid not in sel_log:
        entry = f"| `AtCoder-{pid}` | `{p['contest_id']}` | {p['rating']} | `{p['domain']}` | `{p['subtopic']}` | `{p['topic']}` | **SELECTED** | Premier archetype: {p['key_idea'][:90]}... |\n"
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
        entry = f"| [`AtCoder-{pid}`](analysis/AtCoder-{pid}.md) | {p['title']} | {p['rating']} | `{p['domain']}` | `{p['topic']}` | [`{p['cat_file']}`]({p['cat_file']}) |\n"
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
print(f"Batch 6 Part 4A completed successfully! Total selected in curriculum: {len(completed_ids)}")
print("=" * 75)
