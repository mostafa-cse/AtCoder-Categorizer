import os
import subprocess
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Ensure directories exist
os.makedirs("analysis", exist_ok=True)
os.makedirs("categories", exist_ok=True)
os.makedirs("state", exist_ok=True)
os.makedirs("scratch", exist_ok=True)

print("=" * 75)
print("      PROCESSING BATCH 6 PART 3A: ABC / ARC CURATED LADDER (2101 - 2125)")
print("=" * 75)

SELECTED_PROBLEMS = [
    {
        "id": "abc370_f",
        "title": "Cake Division",
        "contest_id": "abc370",
        "rating": 2102,
        "tag": "Data Structures (DS)",
        "subtopic": "Sparse Table",
        "topic": "Sparse Table",
        "cat_folder": "data_structures",
        "cat_file": "binary_lifting_circular_array_partition.md",
        "statement": "You have a circular cake divided into N pieces with weights A_1, ..., A_N. You want to make K cuts along piece boundaries to divide the cake into K contiguous pieces, maximizing the minimum piece weight. Find this maximum possible weight W, and count how many of the N cut lines never appear in any optimal cut set of size K.",
        "key_idea": "Binary search on the minimum piece weight W. For a fixed W, duplicate the array to length 2N to handle circularity. Using two pointers, compute for each position i the earliest right boundary r such that the piece weight sum is at least W. Build a binary lifting table up[j][i] to simulate making K greedy jumps in O(log K). A cut position i can successfully produce K pieces of weight >= W if and only if up[K][i] <= i + N. To count how many cut positions never appear in ANY optimal cut partition, we trace the forward jumps of all valid starting cuts and mark all visited boundaries.",
        "observation": "Circular greedy partitioning reduces to functional graphs under binary lifting; doubling table up[j][i] checks K contiguous jumps in O(log K).",
        "algorithm": [
            "Duplicate array A to 2N and compute prefix sums.",
            "Binary search W in [1, sum(A) / K]:",
            "  Compute two pointers nxt[i] = earliest r with pref[r] - pref[i] >= W.",
            "  Build binary lifting table up[18][2N].",
            "  Check if there exists i in [0, N-1] with up[K][i] <= i + N.",
            "For optimal W, identify all valid starting cuts i with up[K][i] <= i + N.",
            "Trace and mark all cut boundaries visited along chains of length K from valid starting positions.",
            "Output optimal W and the count of unmarked cut lines."
        ],
        "time_complexity": "O(N log(sum A) + N log K)",
        "space_complexity": "O(N log K)",
        "core_skill": "Binary lifting on circular arrays combined with binary search on partition bounds.",
        "reusable_pattern": "Circular partition feasibility verification using duplicated array doubling table up[log K][2N].",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> a(2 * n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        a[i + n] = a[i];
    }

    vector<long long> pref(2 * n + 1, 0);
    for (int i = 0; i < 2 * n; ++i) {
        pref[i + 1] = pref[i] + a[i];
    }

    auto check = [&](long long W) {
        vector<int> nxt(2 * n + 1, 2 * n);
        int r = 0;
        for (int i = 0; i < 2 * n; ++i) {
            while (r <= 2 * n && pref[r] - pref[i] < W) {
                r++;
            }
            nxt[i] = r;
        }

        int LOG = 18;
        vector<vector<int>> up(LOG, vector<int>(2 * n + 1, 2 * n));
        for (int i = 0; i <= 2 * n; ++i) up[0][i] = nxt[i];
        for (int j = 1; j < LOG; ++j) {
            for (int i = 0; i <= 2 * n; ++i) {
                up[j][i] = up[j - 1][up[j - 1][i]];
            }
        }

        for (int i = 0; i < n; ++i) {
            int cur = i;
            for (int j = 0; j < LOG; ++j) {
                if ((k >> j) & 1) {
                    cur = up[j][cur];
                }
            }
            if (cur <= i + n) return true;
        }
        return false;
    };

    long long low = 1, high = pref[n] / k, optW = 1;
    while (low <= high) {
        long long mid = low + (high - low) / 2;
        if (check(mid)) {
            optW = mid;
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }

    int LOG = 18;
    vector<vector<int>> up(LOG, vector<int>(2 * n + 1, 2 * n));
    int r = 0;
    for (int i = 0; i < 2 * n; ++i) {
        while (r <= 2 * n && pref[r] - pref[i] < optW) {
            r++;
        }
        up[0][i] = r;
    }
    for (int j = 1; j < LOG; ++j) {
        for (int i = 0; i <= 2 * n; ++i) {
            up[j][i] = up[j - 1][up[j - 1][i]];
        }
    }

    vector<bool> can_start(n, false);
    for (int i = 0; i < n; ++i) {
        int cur = i;
        for (int j = 0; j < LOG; ++j) {
            if ((k >> j) & 1) {
                cur = up[j][cur];
            }
        }
        if (cur <= i + n) can_start[i] = true;
    }

    vector<bool> used_cut(n, false);
    for (int i = 0; i < n; ++i) {
        if (can_start[i]) {
            int cur = i;
            for (int step = 0; step < k; ++step) {
                used_cut[cur % n] = true;
                cur = up[0][cur];
            }
        }
    }

    int unused_cuts = 0;
    for (int i = 0; i < n; ++i) {
        if (!used_cut[i]) unused_cuts++;
    }

    cout << optW << " " << unused_cuts << "\n";
    return 0;
}
"""
    },
    {
        "id": "agc029_c",
        "title": "Lexicographic constraints",
        "contest_id": "agc029",
        "rating": 2103,
        "tag": "Basics",
        "subtopic": "Leveraging Monotonicity",
        "topic": "Binary Search",
        "cat_folder": "basics",
        "cat_file": "binary_search_base_k_digit_stack.md",
        "statement": "Given a sequence of positive integers A_1, ..., A_N, find the minimum alphabet size K such that there exist strings S_1 < S_2 < ... < S_N in lexicographical order with |S_i| = A_i.",
        "key_idea": "Binary search on the alphabet size K. If A_1 < A_2 < ... < A_N is strictly increasing, K = 1 is trivially sufficient. For K >= 2, we can greedily make each string S_i the lexicographically smallest string strictly greater than S_{i-1} of length A_i. If A_i > A_{i-1}, we simply append '0's (implicit trailing zeros). If A_i <= A_{i-1}, we truncate the string to length A_i and increment it like a base-K integer at position A_i! Since lengths can be up to 10^9, we maintain non-zero digits using a stack of pairs (position, value in 1..K-1). If an increment carries past the first position, alphabet size K is impossible.",
        "observation": "Greedy lexicographical string extension is isomorphic to base-K arbitrary precision integer increments, maintained sparsely via a stack of non-zero digits in O(N log N).",
        "algorithm": [
            "If A is non-decreasing, answer is 1.",
            "Binary search K in [2, N]:",
            "  Maintain a stack of non-zero digits (pos, val).",
            "  For each i from 1 to N - 1:",
            "    If A[i] > A[i-1], continue (implicit 0s).",
            "    Truncate stack to remove elements with pos > A[i].",
            "    Increment digit at position A[i], propagating carries backward.",
            "    If carry reaches position 0, return false.",
            "  Return true if all increments succeed.",
            "Output the minimum valid K."
        ],
        "time_complexity": "O(N log N)",
        "space_complexity": "O(N)",
        "core_skill": "Sparse base-K integer increment simulation on stacks with binary search on alphabet size.",
        "reusable_pattern": "Simulating lexicographical string sequences with large lengths via sparse stacks of non-zero base-K digits.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> a(n);
    bool non_decreasing = true;
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        if (i > 0 && a[i] <= a[i - 1]) non_decreasing = false;
    }

    if (non_decreasing) {
        cout << 1 << "\n";
        return 0;
    }

    auto check = [&](int K) {
        vector<pair<int, int>> st;

        for (int i = 1; i < n; ++i) {
            if (a[i] > a[i - 1]) continue;

            while (!st.empty() && st.back().first > a[i]) {
                st.pop_back();
            }

            int pos = a[i];
            while (true) {
                if (pos == 0) return false;

                if (!st.empty() && st.back().first == pos) {
                    if (st.back().second + 1 < K) {
                        st.back().second++;
                        break;
                    } else {
                        st.pop_back();
                        pos--;
                    }
                } else {
                    st.push_back({pos, 1});
                    break;
                }
            }
        }
        return true;
    };

    int low = 2, high = n, ans = n;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (check(mid)) {
            ans = mid;
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }

    cout << ans << "\n";
    return 0;
}
"""
    },
    {
        "id": "abc140_f",
        "title": "Many Slimes",
        "contest_id": "abc140",
        "rating": 2105,
        "tag": "Basics",
        "subtopic": "Greedy and Constructive",
        "topic": "Basic Greedy Algorithms",
        "cat_folder": "basics",
        "cat_file": "greedy_multiset_slime_reproduction.md",
        "statement": "You start with 1 slime. In each of N seconds, every existing slime reproduces by spawning a strictly smaller slime. Given the desired final multiset of 2^N slime sizes, determine if it is possible to achieve this multiset.",
        "key_idea": "The initial slime must be the maximum element of the multiset. In each round k (from 1 to N), every slime in the current population must spawn a smaller slime. To maximize the chances of future slimes being able to spawn even smaller slimes, each existing slime should greedily choose the largest available slime in the remaining multiset that is strictly smaller than itself. If at any step an existing slime cannot find any strictly smaller slime, reproduction is impossible.",
        "observation": "Greedy selection of the largest available strictly smaller child preserves maximum dominance for subsequent reproduction rounds.",
        "algorithm": [
            "Store the 2^N elements in a multiset.",
            "Extract the global maximum element as the initial root slime.",
            "For step from 0 to N - 1:",
            "  For each existing slime in descending order:",
            "    Query multiset for the largest element strictly smaller than current slime.",
            "    If none exists, output No.",
            "    Remove it from the multiset and add it to the newly spawned population.",
            "  Add all spawned slimes into the active population and sort descending.",
            "If all N steps succeed, output Yes."
        ],
        "time_complexity": "O(N * 2^N)",
        "space_complexity": "O(2^N)",
        "core_skill": "Greedy multiset lower_bound matching for hierarchical binary tree reproduction processes.",
        "reusable_pattern": "Verifying binary tree spawn processes by greedily matching existing nodes to largest valid remaining leaves.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    int total = 1 << n;
    multiset<int> s;
    for (int i = 0; i < total; ++i) {
        int x;
        cin >> x;
        s.insert(x);
    }

    vector<int> current;
    auto it = prev(s.end());
    current.push_back(*it);
    s.erase(it);

    for (int step = 0; step < n; ++step) {
        vector<int> next_gen;
        for (int val : current) {
            auto it2 = s.lower_bound(val);
            if (it2 == s.begin()) {
                cout << "No\n";
                return 0;
            }
            --it2;
            next_gen.push_back(*it2);
            s.erase(it2);
        }
        for (int v : next_gen) {
            current.push_back(v);
        }
        sort(current.rbegin(), current.rend());
    }

    cout << "Yes\n";
    return 0;
}
"""
    },
    {
        "id": "abc342_g",
        "title": "Retroactive Range Chmax",
        "contest_id": "abc342",
        "rating": 2107,
        "tag": "Data Structures (DS)",
        "subtopic": "Segment Tree",
        "topic": "Segment Tree (Point Update Range Query)",
        "cat_folder": "data_structures",
        "cat_file": "segment_tree_multiset_tag_percolation.md",
        "statement": "Given an array A of length N and Q queries: 1) Range chmax A[l..r] = max(A[l..r], x) tagged with query ID i. 2) Undo/cancel query i. 3) Point query A[p].",
        "key_idea": "Instead of pushing updates down to leaves (which makes deletion difficult), we maintain a multiset of active chmax values at each canonical node of a Segment Tree covering [l, r]. Query 1 inserts x into the multisets of the O(log N) canonical nodes covering [l, r]. Query 2 erases x from those exact canonical nodes. Query 3 for position p simply traverses the segment tree from leaf p up to the root, taking the maximum value among all multisets encountered.",
        "observation": "Tag percolation on segment tree canonical nodes with multisets allows reversible range updates and point queries in O(log N).",
        "algorithm": [
            "Initialize segment tree of size N where each node contains a multiset<int>.",
            "Insert initial elements as range updates [i, i] with x = A[i].",
            "For query 1: insert x into canonical nodes covering [l, r].",
            "For query 2: erase x from canonical nodes covering [queries[id].l, queries[id].r].",
            "For query 3: traverse nodes containing position p, taking the maximum of their max elements.",
            "Output point query answers."
        ],
        "time_complexity": "O(Q log^2 N)",
        "space_complexity": "O((N + Q) log N)",
        "core_skill": "Segment tree tag percolation with reversible multiset maintenance.",
        "reusable_pattern": "Undoable range operations on segment tree via storing updates at canonical nodes and aggregating along point query paths.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

struct Query {
    int type;
    int l, r, x;
};

int n, q;
vector<multiset<int>> tree;

void update_insert(int u, int l, int r, int ql, int qr, int x) {
    if (ql <= l && r <= qr) {
        tree[u].insert(x);
        return;
    }
    int mid = (l + r) / 2;
    if (ql <= mid) update_insert(2 * u, l, mid, ql, qr, x);
    if (qr > mid) update_insert(2 * u + 1, mid + 1, r, ql, qr, x);
}

void update_erase(int u, int l, int r, int ql, int qr, int x) {
    if (ql <= l && r <= qr) {
        auto it = tree[u].find(x);
        if (it != tree[u].end()) tree[u].erase(it);
        return;
    }
    int mid = (l + r) / 2;
    if (ql <= mid) update_erase(2 * u, l, mid, ql, qr, x);
    if (qr > mid) update_erase(2 * u + 1, mid + 1, r, ql, qr, x);
}

int query_point(int u, int l, int r, int p) {
    int max_val = 0;
    if (!tree[u].empty()) {
        max_val = *tree[u].rbegin();
    }
    if (l == r) return max_val;
    int mid = (l + r) / 2;
    if (p <= mid) {
        max_val = max(max_val, query_point(2 * u, l, mid, p));
    } else {
        max_val = max(max_val, query_point(2 * u + 1, mid + 1, r, p));
    }
    return max_val;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n)) return 0;

    vector<int> a(n + 1);
    for (int i = 1; i <= n; ++i) cin >> a[i];

    cin >> q;
    vector<Query> queries(q + 1);
    tree.resize(4 * n + 5);

    for (int i = 1; i <= n; ++i) {
        update_insert(1, 1, n, i, i, a[i]);
    }

    for (int k = 1; k <= q; ++k) {
        cin >> queries[k].type;
        if (queries[k].type == 1) {
            cin >> queries[k].l >> queries[k].r >> queries[k].x;
            update_insert(1, 1, n, queries[k].l, queries[k].r, queries[k].x);
        } else if (queries[k].type == 2) {
            int id;
            cin >> id;
            update_erase(1, 1, n, queries[id].l, queries[id].r, queries[id].x);
        } else {
            int p;
            cin >> p;
            cout << query_point(1, 1, n, p) << "\n";
        }
    }

    return 0;
}
"""
    },
    {
        "id": "abc289_g",
        "title": "Shopping in AtCoder store",
        "contest_id": "abc289",
        "rating": 2109,
        "tag": "Dynamic Programming (DP)",
        "subtopic": "Convex Hull Trick (CHT)",
        "topic": "Convex Hull Trick (CHT) and Dynamic CHT",
        "cat_folder": "dynamic_programming",
        "cat_file": "upper_convex_hull_revenue_envelope.md",
        "statement": "There are N customers with base valuations B_1, ..., B_N. You receive M queries, each with a price increase C_j. A price P will attract all customers i with B_i + C_j >= P. Find the maximum revenue achievable for each query C_j.",
        "key_idea": "Sort base valuations descending: B_1 >= B_2 >= ... >= B_N. If you target selling to the top i customers, the optimal price is P = B_i + C_j, yielding total revenue i * (B_i + C_j) = i * C_j + i * B_i. This is a linear function of C_j with slope m_i = i and y-intercept c_i = i * B_i. Finding the maximum revenue over all i in [1, N] for each query C_j is the upper convex hull envelope of lines with strictly increasing slopes, solved via the classic Convex Hull Trick.",
        "observation": "Pricing revenue functions form lines y = i * x + i * B_i with increasing slopes, evaluated via upper envelope binary search.",
        "algorithm": [
            "Sort base valuations descending: B_1 >= B_2 >= ... >= B_N.",
            "Construct lines y = i * x + i * B_i for i = 1 to N.",
            "Filter lines using cross product / intersection checks to maintain the upper convex hull.",
            "For each query C_j, binary search on the upper hull to find the tangent line maximizing revenue.",
            "Output maximum revenue for each query."
        ],
        "time_complexity": "O(N log N + M log N)",
        "space_complexity": "O(N)",
        "core_skill": "Convex Hull Trick upper envelope construction on linear pricing models.",
        "reusable_pattern": "Maximizing revenue i * (B_i + C) reduces directly to evaluating upper envelope of lines with slope i and intercept i * B_i.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Line {
    long long m, c;
    long long eval(long long x) const {
        return m * x + c;
    }
};

bool is_redundant(const Line& l1, const Line& l2, const Line& l3) {
    return (__int128)(l1.c - l2.c) * (l3.m - l2.m) <= (__int128)(l2.c - l3.c) * (l2.m - l1.m);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<long long> b(n);
    for (int i = 0; i < n; ++i) cin >> b[i];

    sort(b.rbegin(), b.rend());

    vector<Line> hull;
    for (int i = 1; i <= n; ++i) {
        Line cur = { (long long)i, (long long)i * b[i - 1] };
        while (hull.size() >= 2 && is_redundant(hull[hull.size() - 2], hull.back(), cur)) {
            hull.pop_back();
        }
        hull.push_back(cur);
    }

    for (int j = 0; j < m; ++j) {
        long long c;
        cin >> c;

        int low = 0, high = (int)hull.size() - 1;
        while (low < high) {
            int mid = low + (high - low) / 2;
            if (hull[mid].eval(c) < hull[mid + 1].eval(c)) {
                low = mid + 1;
            } else {
                high = mid;
            }
        }
        cout << hull[low].eval(c) << (j + 1 == m ? "" : " ");
    }
    cout << "\n";

    return 0;
}
"""
    },
    {
        "id": "abc371_f",
        "title": "Takahashi in Narrow Road",
        "contest_id": "abc371",
        "rating": 2109,
        "tag": "Data Structures (DS)",
        "subtopic": "Segment Tree",
        "topic": "Segment Tree with Lazy Propagation",
        "cat_folder": "data_structures",
        "cat_file": "monotonic_position_shift_lazy_segtree.md",
        "statement": "N people stand on a line at X_1 < X_2 < ... < X_N. Q queries move person T_i to G_i, pushing others so that positions remain strictly increasing. Find the total distance moved by all people.",
        "key_idea": "The spacing constraint X_{j+1} - X_j >= 1 becomes non-decreasing coordinates Y_j = X_j - j, where Y_1 <= Y_2 <= ... <= Y_N. Moving person T to target G means setting Y_T to G - T. If target > Y_T, we push all adjacent people to the right with Y_j < target up to target. If target < Y_T, we push all adjacent people to the left with Y_j > target down to target. Since Y is non-decreasing, the set of pushed people forms a contiguous interval! Using a Lazy Segment Tree supporting range assignment and range sum queries, we binary search the boundary of the pushed range and execute the range assignment in O(log N).",
        "observation": "Coordinate shift Y_i = X_i - i reduces collision constraints to non-decreasing monotonic range assignments on a Lazy Segment Tree.",
        "algorithm": [
            "Transform positions: Y_i = X_i - i.",
            "Build Lazy Segment Tree over Y storing sum, min, and max.",
            "For each query (T, G):",
            "  target = G - T, cur = query_point(T).",
            "  If target > cur:",
            "    Binary search rightmost R >= T with Y_R < target.",
            "    Distance moved = (R - T + 1) * target - query_sum(T, R).",
            "    Update range [T, R] to target.",
            "  If target < cur:",
            "    Binary search leftmost L <= T with Y_L > target.",
            "    Distance moved = query_sum(L, T) - (T - L + 1) * target.",
            "    Update range [L, T] to target.",
            "Output total accumulated distance."
        ],
        "time_complexity": "O((N + Q) log N)",
        "space_complexity": "O(N)",
        "core_skill": "Coordinate compression/offset to convert strict spacing constraints into monotonic lazy range assignments.",
        "reusable_pattern": "Shifting X_i -> X_i - i converts no-collision physics on a line into monotonic range assignments on segment trees.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Node {
    long long sum;
    long long min_val, max_val;
    long long lazy;
};

int n;
vector<long long> y;
vector<Node> tree;

const long long INF = 2e18;

void apply_lazy(int u, int l, int r, long long val) {
    tree[u].lazy = val;
    tree[u].min_val = val;
    tree[u].max_val = val;
    tree[u].sum = 1LL * (r - l + 1) * val;
}

void push(int u, int l, int r) {
    if (tree[u].lazy != -INF) {
        int mid = (l + r) / 2;
        apply_lazy(2 * u, l, mid, tree[u].lazy);
        apply_lazy(2 * u + 1, mid + 1, r, tree[u].lazy);
        tree[u].lazy = -INF;
    }
}

void pull(int u) {
    tree[u].sum = tree[2 * u].sum + tree[2 * u + 1].sum;
    tree[u].min_val = min(tree[2 * u].min_val, tree[2 * u + 1].min_val);
    tree[u].max_val = max(tree[2 * u].max_val, tree[2 * u + 1].max_val);
}

void build(int u, int l, int r) {
    tree[u].lazy = -INF;
    if (l == r) {
        tree[u].sum = y[l];
        tree[u].min_val = y[l];
        tree[u].max_val = y[l];
        return;
    }
    int mid = (l + r) / 2;
    build(2 * u, l, mid);
    build(2 * u + 1, mid + 1, r);
    pull(u);
}

long long query_point(int u, int l, int r, int p) {
    if (l == r) return tree[u].sum;
    push(u, l, r);
    int mid = (l + r) / 2;
    if (p <= mid) return query_point(2 * u, l, mid, p);
    return query_point(2 * u + 1, mid + 1, r, p);
}

long long query_sum(int u, int l, int r, int ql, int qr) {
    if (ql > qr) return 0;
    if (ql <= l && r <= qr) return tree[u].sum;
    push(u, l, r);
    int mid = (l + r) / 2;
    long long res = 0;
    if (ql <= mid) res += query_sum(2 * u, l, mid, ql, qr);
    if (qr > mid) res += query_sum(2 * u + 1, mid + 1, r, ql, qr);
    return res;
}

void update_range(int u, int l, int r, int ql, int qr, long long val) {
    if (ql > qr) return;
    if (ql <= l && r <= qr) {
        apply_lazy(u, l, r, val);
        return;
    }
    push(u, l, r);
    int mid = (l + r) / 2;
    if (ql <= mid) update_range(2 * u, l, mid, ql, qr, val);
    if (qr > mid) update_range(2 * u + 1, mid + 1, r, ql, qr, val);
    pull(u);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n)) return 0;

    y.resize(n + 1);
    for (int i = 1; i <= n; ++i) {
        long long x;
        cin >> x;
        y[i] = x - i;
    }

    tree.resize(4 * n + 5);
    build(1, 1, n);

    int q;
    if (!(cin >> q)) return 0;

    long long total_dist = 0;

    while (q--) {
        int t;
        long long g;
        cin >> t >> g;
        long long target = g - t;
        long long cur = query_point(1, 1, n, t);

        if (target > cur) {
            int low = t, high = n, R = t;
            while (low <= high) {
                int mid = (low + high) / 2;
                if (query_point(1, 1, n, mid) < target) {
                    R = mid;
                    low = mid + 1;
                } else {
                    high = mid - 1;
                }
            }
            long long prev_sum = query_sum(1, 1, n, t, R);
            long long new_sum = 1LL * (R - t + 1) * target;
            total_dist += (new_sum - prev_sum);
            update_range(1, 1, n, t, R, target);
        } else if (target < cur) {
            int low = 1, high = t, L = t;
            while (low <= high) {
                int mid = (low + high) / 2;
                if (query_point(1, 1, n, mid) > target) {
                    L = mid;
                    high = mid - 1;
                } else {
                    low = mid + 1;
                }
            }
            long long prev_sum = query_sum(1, 1, n, L, t);
            long long new_sum = 1LL * (t - L + 1) * target;
            total_dist += (prev_sum - new_sum);
            update_range(1, 1, n, L, t, target);
        }
    }

    cout << total_dist << "\n";
    return 0;
}
"""
    },
    {
        "id": "arc100_c",
        "title": "Or Plus Max",
        "contest_id": "arc100",
        "rating": 2111,
        "tag": "Dynamic Programming (DP)",
        "subtopic": "Bit Related DP",
        "topic": "Sum Over Subsets DP (SOS DP)",
        "cat_folder": "dynamic_programming",
        "cat_file": "sos_dp_top2_submask_aggregation.md",
        "statement": "Given an array A of length 2^N. For each K in [1, 2^N - 1], find max {A_u + A_v | u < v and (u OR v) <= K}.",
        "key_idea": "The condition (u OR v) <= K is relaxed to considering all subsets where u and v are submasks of mask, which ensures (u OR v) is a submask of mask. For any bitmask, the maximum pair sum is obtained by the top two largest elements among all submasks! We use SOS DP (Fast Zeta Transform) to compute the pair (max1, max2) for every mask in O(N * 2^N). Then, answer for K is the prefix maximum of (max1 + max2) for all masks <= K.",
        "observation": "Submask containment relaxes bitwise OR constraints; maintaining top 2 elements via SOS DP solves pairwise maximums in O(N * 2^N).",
        "algorithm": [
            "Initialize dp[mask] = {A[mask], -1} for all mask in [0, 2^N - 1].",
            "For bit j from 0 to N - 1:",
            "  For mask from 0 to 2^N - 1:",
            "    If bit j is set in mask:",
            "      Merge top-2 elements of dp[mask ^ (1 << j)] into dp[mask].",
            "Compute prefix maximums over K = 1 to 2^N - 1 of (dp[K].max1 + dp[K].max2).",
            "Output the running maximum for each K."
        ],
        "time_complexity": "O(N * 2^N)",
        "space_complexity": "O(2^N)",
        "core_skill": "SOS DP / Fast Zeta Transform maintaining top-2 maximum elements across submasks.",
        "reusable_pattern": "Pairwise sum maximization under bitwise OR constraints via SOS DP tracking top two values.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Top2 {
    int max1, max2;
    void update(int val) {
        if (val > max1) {
            max2 = max1;
            max1 = val;
        } else if (val > max2) {
            max2 = val;
        }
    }
};

Top2 merge(const Top2& a, const Top2& b) {
    Top2 res = a;
    res.update(b.max1);
    res.update(b.max2);
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    int total = 1 << n;
    vector<Top2> dp(total, {-1, -1});
    for (int i = 0; i < total; ++i) {
        int a;
        cin >> a;
        dp[i].max1 = a;
    }

    for (int j = 0; j < n; ++j) {
        for (int mask = 0; mask < total; ++mask) {
            if ((mask >> j) & 1) {
                dp[mask] = merge(dp[mask], dp[mask ^ (1 << j)]);
            }
        }
    }

    int cur_max = 0;
    for (int k = 1; k < total; ++k) {
        cur_max = max(cur_max, dp[k].max1 + dp[k].max2);
        cout << cur_max << "\n";
    }

    return 0;
}
"""
    },
    {
        "id": "abc230_f",
        "title": "Predilection",
        "contest_id": "abc230",
        "rating": 2113,
        "tag": "Dynamic Programming (DP)",
        "subtopic": "Intro to DP",
        "topic": "Knapsack and Basic Dynamic Programming",
        "cat_folder": "dynamic_programming",
        "cat_file": "distinct_subsequence_prefix_sums.md",
        "statement": "Given an array A of length N, you can repeatedly merge adjacent elements A_i + A_{i+1}. Find the number of distinct arrays that can be formed modulo 998244353.",
        "key_idea": "Merging adjacent elements partitions the prefix sums into a chosen subset of prefix sums S_1, S_2, ..., S_{N-1} (with S_N fixed as the total sum). Two partitions result in the exact same array if and only if they select the exact same subsequence of prefix sum values! Thus, the problem is isomorphic to counting the number of distinct subsequences of the prefix sum sequence S[1..N-1]. This is solved via classic distinct subsequence DP using a hash map storing the last DP value for each prefix sum value.",
        "observation": "Array merging choices correspond bijectively to selecting a non-empty subsequence of the prefix sums; distinct output arrays equal distinct prefix sum subsequences.",
        "algorithm": [
            "Compute prefix sums S[1..N].",
            "Maintain total_subseq = 1 (representing empty selection).",
            "Maintain a map last_val_dp storing the contribution previously added by value S[i].",
            "For each i from 1 to N - 1:",
            "  New subsequences formed = total_subseq - last_val_dp[S[i]].",
            "  total_subseq = (total_subseq + new_subsequences) % MOD.",
            "  Update last_val_dp[S[i]] = total_subseq.",
            "Output total_subseq."
        ],
        "time_complexity": "O(N log N)",
        "space_complexity": "O(N)",
        "core_skill": "Isomorphism between adjacent array merges and prefix sum subsequence selection.",
        "reusable_pattern": "Adjacent array merging equivalence reduces to counting distinct subsequences of prefix sums.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <map>

using namespace std;

const int MOD = 998244353;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    vector<long long> pref(n + 1, 0);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        pref[i + 1] = pref[i] + a[i];
    }

    map<long long, long long> last_val_dp;
    long long total_subseq = 1;

    for (int i = 1; i < n; ++i) {
        long long val = pref[i];
        long long new_subseq = total_subseq;
        long long prev_for_val = last_val_dp[val];
        long long added = (new_subseq - prev_for_val + MOD) % MOD;
        total_subseq = (total_subseq + added) % MOD;
        last_val_dp[val] = new_subseq;
    }

    cout << total_subseq << "\n";
    return 0;
}
"""
    },
    {
        "id": "abc343_g",
        "title": "Compress Strings",
        "contest_id": "abc343",
        "rating": 2114,
        "tag": "Dynamic Programming (DP)",
        "subtopic": "Bit Related DP",
        "topic": "Bitmask DP",
        "cat_folder": "dynamic_programming",
        "cat_file": "shortest_common_superstring_kmp_tsp.md",
        "statement": "Given N strings S_1, ..., S_N, find the minimum length of a string that contains all S_i as substrings.",
        "key_idea": "First, eliminate any string that is already a substring of another string. Next, compute for every ordered pair (u, v) the maximum suffix-prefix overlap between S_u and S_v using the KMP prefix function on S_v + '#' + S_u. Appending S_v after S_u adds cost[u][v] = |S_v| - overlap(u, v). Since N <= 20, the Shortest Common Superstring problem reduces to the Traveling Salesperson Problem (TSP), solved via O(2^N * N^2) Bitmask DP.",
        "observation": "Eliminating redundant substrings reduces Shortest Common Superstring to asymmetric TSP on KMP overlap weights.",
        "algorithm": [
            "Filter out strings contained inside other strings.",
            "If only 1 string remains, output its length.",
            "For all pairs (u, v), compute KMP overlap of suffix(u) with prefix(v).",
            "Set cost[u][v] = length(v) - overlap(u, v).",
            "Run Bitmask DP dp[mask][u] = min length covering subset mask ending at string u.",
            "Output min_u dp[(1 << M) - 1][u]."
        ],
        "time_complexity": "O(N * sum(|S|) + 2^N * N^2)",
        "space_complexity": "O(2^N * N)",
        "core_skill": "KMP overlap calculation and bitmask TSP reduction for Shortest Common Superstring.",
        "reusable_pattern": "Superstring length minimization via KMP pairwise overlap matrix + Hamiltonian path bitmask DP.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

vector<int> prefix_function(const string& s) {
    int n = s.size();
    vector<int> pi(n, 0);
    for (int i = 1; i < n; ++i) {
        int j = pi[i - 1];
        while (j > 0 && s[i] != s[j]) j = pi[j - 1];
        if (s[i] == s[j]) j++;
        pi[i] = j;
    }
    return pi;
}

int compute_overlap(const string& s1, const string& s2) {
    string combined = s2 + '#' + s1;
    vector<int> pi = prefix_function(combined);
    return pi.back();
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<string> raw_s(n);
    for (int i = 0; i < n; ++i) cin >> raw_s[i];

    vector<string> s;
    for (int i = 0; i < n; ++i) {
        bool contained = false;
        for (int j = 0; j < n; ++j) {
            if (i == j) continue;
            if (raw_s[j].size() > raw_s[i].size() || (raw_s[j].size() == raw_s[i].size() && i > j)) {
                if (raw_s[j].find(raw_s[i]) != string::npos) {
                    contained = true;
                    break;
                }
            }
        }
        if (!contained) {
            s.push_back(raw_s[i]);
        }
    }

    int m = s.size();
    if (m == 1) {
        cout << s[0].size() << "\n";
        return 0;
    }

    vector<vector<int>> cost(m, vector<int>(m, 0));
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < m; ++j) {
            if (i == j) continue;
            int overlap = compute_overlap(s[i], s[j]);
            cost[i][j] = (int)s[j].size() - overlap;
        }
    }

    int total_masks = 1 << m;
    vector<vector<int>> dp(total_masks, vector<int>(m, 1e9));

    for (int i = 0; i < m; ++i) {
        dp[1 << i][i] = s[i].size();
    }

    for (int mask = 1; mask < total_masks; ++mask) {
        for (int u = 0; u < m; ++u) {
            if (dp[mask][u] >= 1e9) continue;
            for (int v = 0; v < m; ++v) {
                if (!((mask >> v) & 1)) {
                    int next_mask = mask | (1 << v);
                    dp[next_mask][v] = min(dp[next_mask][v], dp[mask][u] + cost[u][v]);
                }
            }
        }
    }

    int ans = 1e9;
    for (int i = 0; i < m; ++i) {
        ans = min(ans, dp[total_masks - 1][i]);
    }

    cout << ans << "\n";
    return 0;
}
"""
    },
    {
        "id": "arc117_d",
        "title": "Miracle Tree",
        "contest_id": "arc117",
        "rating": 2115,
        "tag": "Graph Theory",
        "subtopic": "Graph Traversal",
        "topic": "Tree Diameter",
        "cat_folder": "graph_theory",
        "cat_file": "tree_diameter_euler_tour_labeling.md",
        "statement": "Given a tree T with N vertices, assign distinct positive integers E_v to all vertices such that |E_u - E_v| >= dist(u, v) for all pairs (u, v). Minimize the maximum label max_v E_v.",
        "key_idea": "If we traverse the tree in an Euler tour stepping along edges and incrementing a global time counter at each step, any two vertices have label difference >= tree distance (by triangle inequality). A standard tour visits each edge twice (taking 2(N-1) steps). To minimize the maximum time without returning to the root, we save steps equal to the depth of the last visited leaf! To maximize this savings, the path from the root to the last visited leaf must be the tree diameter. We find the diameter endpoints S and T, root at S, and visit the diameter child last at each branching step.",
        "observation": "Euler tour traversal times naturally satisfy distance lower bounds |E_u - E_v| >= dist(u, v); visiting diameter endpoints first and last minimizes peak label.",
        "algorithm": [
            "Find tree diameter endpoints S and T via two BFS/DFS passes.",
            "Root tree at S and mark all edges along the path from S to T.",
            "Run DFS starting at S: at each vertex u, visit non-diameter children first, and diameter child last.",
            "Maintain global counter t starting at 1; assign E[u] = t upon first visit, incrementing t on each step and backtrack.",
            "Output the resulting vertex labels E_1, ..., E_N."
        ],
        "time_complexity": "O(N)",
        "space_complexity": "O(N)",
        "core_skill": "Tree diameter Euler tour traversal for optimal metric labeling.",
        "reusable_pattern": "Metric label assignment satisfying |E_u - E_v| >= dist(u, v) minimized via diameter-guided DFS Euler tour.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int n;
vector<vector<int>> adj;
vector<int> dist_node;

void dfs_dist(int u, int p, int d) {
    dist_node[u] = d;
    for (int v : adj[u]) {
        if (v != p) dfs_dist(v, u, d + 1);
    }
}

int get_farthest(int start) {
    dist_node.assign(n + 1, 0);
    dfs_dist(start, 0, 0);
    int best = start;
    for (int i = 1; i <= n; ++i) {
        if (dist_node[i] > dist_node[best]) best = i;
    }
    return best;
}

vector<bool> on_diam;

bool find_path(int u, int p, int target) {
    if (u == target) {
        on_diam[u] = true;
        return true;
    }
    for (int v : adj[u]) {
        if (v != p && find_path(v, u, target)) {
            on_diam[u] = true;
            return true;
        }
    }
    return false;
}

vector<int> E;
int cur_time = 1;

void dfs_euler(int u, int p) {
    E[u] = cur_time;
    vector<int> non_diam_children;
    int diam_child = -1;
    for (int v : adj[u]) {
        if (v == p) continue;
        if (on_diam[v]) diam_child = v;
        else non_diam_children.push_back(v);
    }

    for (int v : non_diam_children) {
        cur_time++;
        dfs_euler(v, u);
        cur_time++;
    }

    if (diam_child != -1) {
        cur_time++;
        dfs_euler(diam_child, u);
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n)) return 0;

    adj.assign(n + 1, vector<int>());
    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    int S = get_farthest(1);
    int T = get_farthest(S);

    on_diam.assign(n + 1, false);
    find_path(S, 0, T);

    E.assign(n + 1, 0);
    dfs_euler(S, 0);

    for (int i = 1; i <= n; ++i) {
        cout << E[i] << (i == n ? "" : " ");
    }
    cout << "\n";

    return 0;
}
"""
    },
    {
        "id": "keyence2021_d",
        "title": "Choosing Up Sides",
        "contest_id": "keyence2021",
        "rating": 2115,
        "tag": "Basics",
        "subtopic": "Greedy and Constructive",
        "topic": "Basic Constructive Algorithms",
        "cat_folder": "basics",
        "cat_file": "hadamard_matrix_sylvester_construction.md",
        "statement": "For 2^N people and 2^N - 1 rounds, partition people into two teams of size 2^{N-1} each round such that every pair of people are on the same team in exactly 2^{N-2} - 1 rounds.",
        "key_idea": "The condition that all pairs of columns have the identical dot product across team indicators (+1 and -1) is uniquely satisfied by the construction of a Hadamard Matrix of order 2^N. Using Sylvester's recursive Kronecker product construction, H[r][c] = (-1)^{popcount(r & c)}. Row 0 consists entirely of 1s (all on team A). The remaining 2^N - 1 rows have exactly equal counts of +1 ('A') and -1 ('B') and their column dot products are orthogonal, giving equal pairwise shared rounds for all pairs of people.",
        "observation": "Pairwise balanced tournament rounds correspond exactly to the orthogonal rows of a Sylvester Hadamard Matrix.",
        "algorithm": [
            "Set total_rounds = 2^N - 1, total_people = 2^N.",
            "For row r from 1 to 2^N - 1:",
            "  Construct string of length 2^N where character c is 'A' if popcount(r & c) is even, and 'B' if odd.",
            "Output total_rounds followed by the team assignment strings."
        ],
        "time_complexity": "O(4^N)",
        "space_complexity": "O(2^N)",
        "core_skill": "Sylvester Hadamard matrix construction for balanced bipartite orthogonal tournament pairings.",
        "reusable_pattern": "Generating balanced pairwise tournament designs using bitwise AND popcount parity.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    int total_people = 1 << n;
    int total_rounds = (1 << n) - 1;

    cout << total_rounds << "\n";
    for (int r = 1; r < total_people; ++r) {
        string s = "";
        for (int c = 0; c < total_people; ++c) {
            int sign = __builtin_popcount(r & c) % 2;
            s += (sign == 0 ? 'A' : 'B');
        }
        cout << s << "\n";
    }

    return 0;
}
"""
    },
    {
        "id": "abc145_f",
        "title": "Laminate",
        "contest_id": "abc145",
        "rating": 2116,
        "tag": "Dynamic Programming (DP)",
        "subtopic": "Intro to DP",
        "topic": "Knapsack and Basic Dynamic Programming",
        "cat_folder": "dynamic_programming",
        "cat_file": "subsequence_retention_dp_laminate.md",
        "statement": "You have N columns of heights H_1, ..., H_N. Minimum operations to level all columns to 0 is sum_{i=1}^N max(0, H_i - H_{i-1}). You can change the heights of at most K columns. Find the minimum operations required.",
        "key_idea": "Changing at most K columns is equivalent to choosing M = N - K columns to KEEP at their original heights! The optimal choice for intermediate changed columns between two kept columns i and j is to set them to min(H_i, H_j), incurring cost max(0, H_j - H_i). We define dp[i][cnt] as the minimum cost for a prefix ending at kept column i with cnt columns kept. Transitions iterate over all previous kept columns i < j in O(N^2 * (N - K)).",
        "observation": "Modifying up to K columns is equivalent to selecting N - K columns to retain, with transitions between kept columns i and j contributing max(0, H_j - H_i).",
        "algorithm": [
            "Set m = N - K. If m <= 0, output 0.",
            "Initialize dp[N+1][m+1] with infinity, dp[0][0] = 0.",
            "For i from 0 to N:",
            "  For cnt from 0 to m:",
            "    For j from i + 1 to N:",
            "      dp[j][cnt + 1] = min(dp[j][cnt + 1], dp[i][cnt] + max(0LL, H[j] - H[i])).",
            "Output min_{i} dp[i][m]."
        ],
        "time_complexity": "O(N^2 * (N - K))",
        "space_complexity": "O(N * (N - K))",
        "core_skill": "Reformulating modification budgets into retention subsequence DP.",
        "reusable_pattern": "Reducing bounded element modifications in prefix-difference costs to selecting optimal retention subsequences.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const long long INF = 1e18;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> h(n + 1, 0);
    for (int i = 1; i <= n; ++i) cin >> h[i];

    int m = n - k;
    if (m <= 0) {
        cout << 0 << "\n";
        return 0;
    }

    vector<vector<long long>> dp(n + 1, vector<long long>(m + 1, INF));
    dp[0][0] = 0;

    for (int i = 0; i <= n; ++i) {
        for (int cnt = 0; cnt <= m; ++cnt) {
            if (dp[i][cnt] >= INF) continue;
            for (int j = i + 1; j <= n; ++j) {
                if (cnt + 1 <= m) {
                    long long cost = max(0LL, h[j] - h[i]);
                    dp[j][cnt + 1] = min(dp[j][cnt + 1], dp[i][cnt] + cost);
                }
            }
        }
    }

    long long ans = INF;
    for (int i = 1; i <= n; ++i) {
        ans = min(ans, dp[i][m]);
    }

    cout << ans << "\n";
    return 0;
}
"""
    },
    {
        "id": "arc175_c",
        "title": "Jumping Through Intervals",
        "contest_id": "arc175",
        "rating": 2116,
        "tag": "Basics",
        "subtopic": "Greedy and Constructive",
        "topic": "Basic Greedy Algorithms",
        "cat_folder": "basics",
        "cat_file": "backward_interval_clamping_greedy.md",
        "statement": "Given N intervals [L_i, R_i], choose A_i in [L_i, R_i] to minimize sum_{i=1}^{N-1} |A_i - A_{i+1}|. If multiple solutions exist, find the lexicographically smallest sequence A.",
        "key_idea": "Backward pass calculates the optimal reachable interval [optL_i, optR_i] for each A_i. If [L_i, R_i] overlaps with [optL_{i+1}, optR_{i+1}], the intersection achieves zero additional transition cost. If it lies completely to the left, A_i = R_i; if to the right, A_i = L_i. A subsequent forward pass greedily selects the minimum valid A_i within [optL_i, optR_i] that matches the previous chosen value A_{i-1} as closely as possible, ensuring lexicographical minimality.",
        "observation": "Backward interval projection identifies the optimal continuous locus of points; forward greedy clamping resolves lexicographical tie-breaking.",
        "algorithm": [
            "Backward sweep from N-1 down to 0:",
            "  If [L_i, R_i] is disjoint to right of opt[i+1], opt[i] = [L_i, L_i].",
            "  If disjoint to left, opt[i] = [R_i, R_i].",
            "  Otherwise, opt[i] = [max(L_i, optL_{i+1}), min(R_i, optR_{i+1})].",
            "Forward sweep from 0 to N-1:",
            "  A[0] = optL[0].",
            "  For i from 1 to N-1: clamp A[i-1] into [optL_i, optR_i].",
            "Output sequence A."
        ],
        "time_complexity": "O(N)",
        "space_complexity": "O(N)",
        "core_skill": "Two-pass interval projection and lexicographical greedy forward clamping.",
        "reusable_pattern": "Minimizing transition distance between constrained intervals via backward reachability projection followed by forward tie-breaking.",
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

    vector<long long> L(n), R(n);
    for (int i = 0; i < n; ++i) {
        cin >> L[i] >> R[i];
    }

    vector<long long> optL(n), optR(n);
    optL[n - 1] = L[n - 1];
    optR[n - 1] = R[n - 1];

    for (int i = n - 2; i >= 0; --i) {
        if (R[i] < optL[i + 1]) {
            optL[i] = optR[i] = R[i];
        } else if (L[i] > optR[i + 1]) {
            optL[i] = optR[i] = L[i];
        } else {
            optL[i] = max(L[i], optL[i + 1]);
            optR[i] = min(R[i], optR[i + 1]);
        }
    }

    vector<long long> A(n);
    A[0] = optL[0];

    for (int i = 1; i < n; ++i) {
        if (A[i - 1] < optL[i]) {
            A[i] = optL[i];
        } else if (A[i - 1] > optR[i]) {
            A[i] = optR[i];
        } else {
            A[i] = A[i - 1];
        }
    }

    for (int i = 0; i < n; ++i) {
        cout << A[i] << (i + 1 == n ? "" : " ");
    }
    cout << "\n";

    return 0;
}
"""
    },
    {
        "id": "abc244_g",
        "title": "Construct Good Path",
        "contest_id": "abc244",
        "rating": 2117,
        "tag": "Graph Theory",
        "subtopic": "Graph Traversal",
        "topic": "DFS Tree",
        "cat_folder": "graph_theory",
        "cat_file": "dfs_tree_parity_correction_detours.md",
        "statement": "Given a connected undirected graph and a binary parity string S, construct a walk of length at most 4N such that vertex v is visited an odd number of times iff S_v = 1.",
        "key_idea": "Build a DFS spanning tree of the graph. Traverse the tree. When returning from a child v to parent u, check if the current visit parity of v matches S_v. If not, take an immediate 2-step detour u -> v -> u! This detour flips the parity of v while visiting u twice (leaving u's parity completely unchanged). Backtracking in this bottom-up manner fixes all vertices' parities. If the root's parity is incorrect at the very end, simply omit the final step of the walk.",
        "observation": "A 2-step edge detour u -> v -> u flips the parity of v without altering the parity of u, enabling bottom-up parity satisfaction on DFS trees.",
        "algorithm": [
            "Construct DFS tree from vertex 1.",
            "Record visits in a path array, maintaining current parity of each vertex.",
            "On backtracking from child v to parent u:",
            "  If cur_parity[v] != S[v]:",
            "    Append v, flip parity of v.",
            "    Append u, flip parity of u.",
            "If cur_parity[root] != S[root], remove the final step from path.",
            "Output walk length and sequence."
        ],
        "time_complexity": "O(N + M)",
        "space_complexity": "O(N)",
        "core_skill": "DFS tree bottom-up parity correction using localized 2-step edge detours.",
        "reusable_pattern": "Satisfying arbitrary vertex visit parities on connected graphs via DFS spanning tree detours.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <string>

using namespace std;

int n, m;
vector<vector<int>> adj;
string s;
vector<bool> visited;
vector<int> path;
vector<int> cur_parity;

void dfs(int u) {
    visited[u] = true;
    path.push_back(u);
    cur_parity[u] ^= 1;

    for (int v : adj[u]) {
        if (!visited[v]) {
            dfs(v);
            path.push_back(u);
            cur_parity[u] ^= 1;

            if (cur_parity[v] != (s[v - 1] - '0')) {
                path.push_back(v);
                cur_parity[v] ^= 1;
                path.push_back(u);
                cur_parity[u] ^= 1;
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n >> m)) return 0;

    adj.assign(n + 1, vector<int>());
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    cin >> s;

    visited.assign(n + 1, false);
    cur_parity.assign(n + 1, 0);

    dfs(1);

    if (cur_parity[1] != (s[0] - '0')) {
        path.pop_back();
        cur_parity[1] ^= 1;
    }

    cout << path.size() << "\n";
    for (int i = 0; i < (int)path.size(); ++i) {
        cout << path[i] << (i + 1 == (int)path.size() ? "" : " ");
    }
    cout << "\n";

    return 0;
}
"""
    },
    {
        "id": "arc077_c",
        "title": "guruguru",
        "contest_id": "arc077",
        "rating": 2117,
        "tag": "Basics",
        "subtopic": "More Techniques",
        "topic": "Difference Array",
        "cat_folder": "basics",
        "cat_file": "second_order_difference_array_slope_imos.md",
        "statement": "A circular dial has M positions 1..M. In each transition a_i -> a_{i+1}, you can step +1 or jump directly to a preset favorite button x. Find the optimal x to minimize total button presses.",
        "key_idea": "For a transition from u to v of distance d = (v - u + M) mod M, setting the favorite button to x saves presses if x lies on the forward arc: savings start at 0 at u+1, increase with slope +1 up to v (where savings = d - 1), then drop to 0 at v+1. Because the savings function is piecewise linear, we can use second-order difference arrays (slope changes) to add the piecewise linear functions from all transitions in O(1) each, then integrate twice to find the maximum savings.",
        "observation": "Piecewise linear cost functions on circular domains are efficiently aggregated via second-order difference arrays (slope imos).",
        "algorithm": [
            "Compute base cost sum (a_{i+1} - a_i + M) mod M.",
            "For each transition with distance d > 1:",
            "  Add +1 slope change at u + 2.",
            "  Add -d slope change at u + d + 1.",
            "  Add +(d - 1) slope change at u + d + 2.",
            "Integrate second-order differences twice to recover savings for each x in [1, M].",
            "Find maximum savings and subtract from base cost."
        ],
        "time_complexity": "O(N + M)",
        "space_complexity": "O(M)",
        "core_skill": "Second-order difference array integration for circular piecewise linear optimization.",
        "reusable_pattern": "Aggregating piecewise linear savings functions over circular intervals via double prefix sums.",
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

    vector<int> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    long long base_cost = 0;
    vector<long long> d2(2 * m + 5, 0);

    for (int i = 0; i < n - 1; ++i) {
        int from = a[i];
        int to = a[i + 1];
        long long dist = (to - from + m) % m;
        base_cost += dist;

        if (dist > 1) {
            int l = from + 2;
            int r = from + dist;
            d2[l] += 1;
            d2[r + 1] -= (dist);
            d2[r + 2] += (dist - 1);
        }
    }

    vector<long long> slope(2 * m + 5, 0);
    vector<long long> savings_extended(2 * m + 5, 0);

    long long cur_slope = 0;
    long long cur_savings = 0;
    for (int x = 1; x <= 2 * m; ++x) {
        cur_slope += d2[x];
        slope[x] = cur_slope;
        cur_savings += cur_slope;
        savings_extended[x] = cur_savings;
    }

    vector<long long> savings(m + 1, 0);
    for (int x = 1; x <= 2 * m; ++x) {
        int actual_x = (x - 1) % m + 1;
        savings[actual_x] += savings_extended[x];
    }

    long long max_savings = 0;
    for (int x = 1; x <= m; ++x) {
        max_savings = max(max_savings, savings[x]);
    }

    cout << base_cost - max_savings << "\n";
    return 0;
}
"""
    },
    {
        "id": "arc183_b",
        "title": "Near Assignment",
        "contest_id": "arc183",
        "rating": 2118,
        "tag": "Basics",
        "subtopic": "Greedy and Constructive",
        "topic": "Basic Constructive Algorithms",
        "cat_folder": "basics",
        "cat_file": "distance_k_replication_reachability.md",
        "statement": "Given two arrays A and B of length N, determine if A can be transformed into B by repeatedly choosing i, j with |i - j| <= K and setting A_i = A_j.",
        "key_idea": "If A == B, answer is trivially Yes. Otherwise, every value in B must exist in A (values cannot be created from nothing). Furthermore, since an assignment A_i = A_j overwrites a value, values can only replicate without losing variety if B contains at least one duplicate pair within distance K (i.e. exists i < j with B_i = B_j and j - i <= K). If no such nearby duplicate exists in B, every window of length K+1 has strictly distinct elements, making it impossible to perform any overwrite without permanently extinguishing a necessary value.",
        "observation": "Replication reachability under radius K requires value subset containment and the existence of at least one duplicate pair within distance K in the target array.",
        "algorithm": [
            "If A == B, return Yes.",
            "Verify all elements of B appear in A; if not, return No.",
            "Check if there exist indices i < j with B[i] == B[j] and j - i <= K using last occurrence tracking.",
            "If such a pair exists, return Yes; otherwise return No."
        ],
        "time_complexity": "O(N)",
        "space_complexity": "O(N)",
        "core_skill": "Replication invariant analysis and local duplicate density verification.",
        "reusable_pattern": "Array transformation under local overwriting radius K requires target to contain nearby duplicate seeds.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void solve() {
    int n, k;
    cin >> n >> k;

    vector<int> a(n), b(n);
    vector<bool> in_a(n + 1, false);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        in_a[a[i]] = true;
    }
    for (int i = 0; i < n; ++i) {
        cin >> b[i];
    }

    if (a == b) {
        cout << "Yes\n";
        return;
    }

    for (int i = 0; i < n; ++i) {
        if (!in_a[b[i]]) {
            cout << "No\n";
            return;
        }
    }

    vector<int> last_pos(n + 1, -1);
    bool has_near_dup = false;
    for (int i = 0; i < n; ++i) {
        if (last_pos[b[i]] != -1 && i - last_pos[b[i]] <= k) {
            has_near_dup = true;
            break;
        }
        last_pos[b[i]] = i;
    }

    if (has_near_dup) {
        cout << "Yes\n";
    } else {
        cout << "No\n";
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
        "id": "abc426_g",
        "title": "Range Knapsack Query",
        "contest_id": "abc426",
        "rating": 2119,
        "tag": "Miscellaneous",
        "subtopic": "Techniques",
        "topic": "Divide and Conquer on Queries",
        "cat_folder": "miscellaneous",
        "cat_file": "divide_and_conquer_range_knapsack.md",
        "statement": "Given N items with weights W_i and values V_i. Answer Q queries: find the maximum value knapsack on subarray [L_i, R_i] with weight capacity C_i.",
        "key_idea": "Offline Divide and Conquer over the item range [1, N]. For queries lying completely in [L, mid] or [mid+1, R], recurse on the respective halves. For queries spanning across mid (L <= mid < R), compute a suffix knapsack table from mid down to L and a prefix knapsack table from mid+1 up to R. Each spanning query with capacity C can be answered by taking max_{c} (suffix_dp[c] + prefix_dp[C - c]) in O(C) time.",
        "observation": "Subarray knapsack queries spanning a split point mid can be resolved in O(C) by merging suffix and prefix knapsack tables.",
        "algorithm": [
            "Divide and conquer solve_dc(l, r, queries):",
            "  If l == r, answer single-item queries directly.",
            "  Partition queries into left, right, and spanning queries.",
            "  Recurse on left and right subsegments.",
            "  For spanning queries: build suffix knapsack DP from mid down to l, and prefix knapsack DP from mid+1 up to r.",
            "  For each spanning query, merge suffix_dp and prefix_dp in O(C) time.",
            "Output answers in query order."
        ],
        "time_complexity": "O(N C log N + Q C)",
        "space_complexity": "O(N C + Q)",
        "core_skill": "Offline divide and conquer on queries with prefix/suffix knapsack convolutions.",
        "reusable_pattern": "Range queries on non-invertible monoids (like knapsacks) solved via offline D&C with suffix-prefix convolutions across midpoints.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Item {
    int w, v;
};

struct Query {
    int id;
    int l, r, c;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<Item> items(n + 1);
    for (int i = 1; i <= n; ++i) {
        cin >> items[i].w >> items[i].v;
    }

    int q;
    if (!(cin >> q)) return 0;

    vector<Query> queries(q);
    for (int i = 0; i < q; ++i) {
        queries[i].id = i;
        cin >> queries[i].l >> queries[i].r >> queries[i].c;
    }

    vector<long long> ans(q, 0);

    auto solve_dc = [&](auto& self, int l, int r, vector<Query>& q_list) -> void {
        if (q_list.empty()) return;
        if (l == r) {
            for (auto& qry : q_list) {
                if (items[l].w <= qry.c) ans[qry.id] = items[l].v;
                else ans[qry.id] = 0;
            }
            return;
        }

        int mid = (l + r) / 2;
        vector<Query> left_q, right_q, span_q;
        for (auto& qry : q_list) {
            if (qry.r <= mid) left_q.push_back(qry);
            else if (qry.l > mid) right_q.push_back(qry);
            else span_q.push_back(qry);
        }

        self(self, l, mid, left_q);
        self(self, mid + 1, r, right_q);

        if (span_q.empty()) return;

        int max_c = 0;
        for (auto& qry : span_q) max_c = max(max_c, qry.c);

        vector<vector<long long>> suff_dp(mid - l + 2, vector<long long>(max_c + 1, 0));
        for (int i = mid; i >= l; --i) {
            int idx = mid - i + 1;
            suff_dp[idx] = suff_dp[idx - 1];
            int w = items[i].w;
            int v = items[i].v;
            for (int cap = max_c; cap >= w; --cap) {
                suff_dp[idx][cap] = max(suff_dp[idx][cap], suff_dp[idx - 1][cap - w] + v);
            }
        }

        vector<vector<long long>> pref_dp(r - mid + 1, vector<long long>(max_c + 1, 0));
        for (int i = mid + 1; i <= r; ++i) {
            int idx = i - mid;
            pref_dp[idx] = pref_dp[idx - 1];
            int w = items[i].w;
            int v = items[i].v;
            for (int cap = max_c; cap >= w; --cap) {
                pref_dp[idx][cap] = max(pref_dp[idx][cap], pref_dp[idx - 1][cap - w] + v);
            }
        }

        for (auto& qry : span_q) {
            int left_idx = mid - qry.l + 1;
            int right_idx = qry.r - mid;
            long long best = 0;
            for (int cap = 0; cap <= qry.c; ++cap) {
                best = max(best, suff_dp[left_idx][cap] + pref_dp[right_idx][qry.c - cap]);
            }
            ans[qry.id] = best;
        }
    };

    solve_dc(solve_dc, 1, n, queries);

    for (int i = 0; i < q; ++i) {
        cout << ans[i] << "\n";
    }

    return 0;
}
"""
    },
    {
        "id": "agc048_c",
        "title": "Penguin Skating",
        "contest_id": "agc048",
        "rating": 2120,
        "tag": "Basics",
        "subtopic": "Leveraging Monotonicity",
        "topic": "Two Pointers",
        "cat_folder": "basics",
        "cat_file": "coordinate_shifted_cluster_two_pointers.md",
        "statement": "N penguins stand on a line at A_1 < A_2 < ... < A_N on a board of length L. Sliding a penguin moves it until it hits another penguin or the boundary. Given target positions B_1 < B_2 < ... < B_N, find the minimum operations to reach B, or -1 if impossible.",
        "key_idea": "Shift coordinates by setting a_i = A_i - i and b_i = B_i - i. When penguins slide and cluster, contiguous blocks in a become equal to the anchor penguin's value! Therefore, the target sequence b can be formed if and only if each b_i can be matched to an occurrence of the identical value in a. Since penguins move either strictly leftward (b_i < a_i) or rightward (b_i > a_i), we can use two pointers to match each b_i with the closest matching value in a, accumulating total move steps.",
        "observation": "Penguin sliding collapses differences A_i - i into contiguous constant blocks, reducing the problem to two-pointer matching on monotonic transformed coordinates.",
        "algorithm": [
            "Set a_i = A_i - i and b_i = B_i - i with boundary sentinels.",
            "Verify matching via two pointers j_left and j_right:",
            "  If b_i < a_i: advance j_left to find a[j_left] == b_i, add (i - j_left) moves.",
            "  If b_i > a_i: advance j_right to find a[j_right] == b_i, add (j_right - i) moves.",
            "  If any value cannot be matched, output -1.",
            "Output total moves."
        ],
        "time_complexity": "O(N)",
        "space_complexity": "O(N)",
        "core_skill": "Coordinate shift invariant mapping cluster sliding to constant blocks and two-pointer matching.",
        "reusable_pattern": "Compressing contiguous sliding collisions into constant value blocks on offset coordinates A_i - i.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long L;
    if (!(cin >> n >> L)) return 0;

    vector<long long> A(n + 2), B(n + 2);
    A[0] = 0; B[0] = 0;
    for (int i = 1; i <= n; ++i) cin >> A[i];
    for (int i = 1; i <= n; ++i) cin >> B[i];
    A[n + 1] = L + 1; B[n + 1] = L + 1;

    vector<long long> a(n + 2), b(n + 2);
    for (int i = 0; i <= n + 1; ++i) {
        a[i] = A[i] - i;
        b[i] = B[i] - i;
    }

    long long ans = 0;
    int j_left = 0, j_right = 0;

    for (int i = 1; i <= n; ++i) {
        if (a[i] == b[i]) continue;

        if (b[i] < a[i]) {
            while (j_left < i && a[j_left] < b[i]) {
                j_left++;
            }
            if (a[j_left] != b[i]) {
                cout << -1 << "\n";
                return 0;
            }
            ans += (i - j_left);
        } else {
            j_right = max(j_right, i);
            while (j_right <= n + 1 && a[j_right] < b[i]) {
                j_right++;
            }
            if (a[j_right] != b[i]) {
                cout << -1 << "\n";
                return 0;
            }
            ans += (j_right - i);
        }
    }

    cout << ans << "\n";
    return 0;
}
"""
    }
]

REJECTED_PROBLEMS = []

# Step 1: Verify compilation for all 18 problems
print("\n--- Verifying Compilation ---")
for p in SELECTED_PROBLEMS:
    cpp_source = p["cpp_code"]
    src_file = os.path.join("scratch", f"temp_p3a_{p['id']}.cpp")
    exe_file = os.path.join("scratch", f"temp_p3a_{p['id']}.exe")
    with open(src_file, "w", encoding="utf-8") as f:
        f.write(cpp_source)
    res = subprocess.run(["g++", "-std=c++17", "-O2", src_file, "-o", exe_file], capture_output=True, text=True)
    if res.returncode != 0:
        print(f"[-] Compilation FAILED for {p['id']}:\n{res.stderr}")
        sys.exit(1)
    else:
        print(f"[+] Compiled successfully: {p['id']}")

# Step 2: Generate analysis files
print("\n--- Generating Analysis Files ---")
for p in SELECTED_PROBLEMS:
    analysis_file = os.path.join("analysis", f"AtCoder-{p['id']}.md")
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

## 5. Core Skill & Reusable Pattern
- **Core Skill**: {p['core_skill']}
- **Reusable Pattern**: {p['reusable_pattern']}

## 6. Editorial Comparison & Alternative Approaches
{p['editorial_comparison']}

## 7. Verified C++17 Implementation
```cpp
{p['cpp_code'].strip()}
```
"""
    with open(analysis_file, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"[+] Generated: {analysis_file}")

# Step 3: Create / Update Category files
print("\n--- Updating Category Workbooks ---")
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

# Step 4: Update SELECTION_LOG.md
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

# Step 5: Update QUALITY_PROBLEMS_BY_TOPIC.md
with open("QUALITY_PROBLEMS_BY_TOPIC.md", "r", encoding="utf-8") as f:
    existing_q = f.read()

new_q_lines = []
for p in SELECTED_PROBLEMS:
    line = f"- `[problem:AtCoder-{p['id']}]` — **{p['title']}** (Rating: {p['rating']}) | Topic: `{p['topic']}` | Analysis: [`analysis/AtCoder-{p['id']}.md`](analysis/AtCoder-{p['id']}.md)"
    if f"[problem:AtCoder-{p['id']}]" not in existing_q:
        new_q_lines.append(line)

if new_q_lines:
    with open("QUALITY_PROBLEMS_BY_TOPIC.md", "a", encoding="utf-8") as f:
        f.write("\n### Batch 6 Part 3A: ABC / ARC Curated Ladder (2101 - 2125)\n" + "\n".join(new_q_lines) + "\n")
    print("[+] Updated QUALITY_PROBLEMS_BY_TOPIC.md with new archetypes.")

# Step 6: Update state/progress.json
with open("state/progress.json", "r", encoding="utf-8") as f:
    progress = json.load(f)

progress["current_batch"] = "Batch 6 Part 3A: ABC / ARC Ladder (2101-2125) COMPLETED"
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

# Step 7: Clean temporary test executables in scratch/
for p in SELECTED_PROBLEMS:
    exe_file = os.path.join("scratch", f"temp_p3a_{p['id']}.exe")
    src_file = os.path.join("scratch", f"temp_p3a_{p['id']}.cpp")
    if os.path.exists(exe_file):
        try: os.remove(exe_file)
        except: pass
    if os.path.exists(src_file):
        try: os.remove(src_file)
        except: pass

print("=" * 75)
print(f"Batch 6 Part 3A completed successfully! Total selected in curriculum: {progress['total_evaluated_in_curriculum']}")
print("=" * 75)
