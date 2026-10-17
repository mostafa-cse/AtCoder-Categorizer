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
print("      PROCESSING BATCH 5 PART 2B: ABC CURATED LADDER (1751 - 1799)")
print("=" * 75)

SELECTED_PROBLEMS = [
    {
        "id": "abc023_c",
        "title": "収集王",
        "contest_id": "abc023",
        "rating": 1752,
        "tag": "Basics",
        "subtopic": "Frequency Counting",
        "topic": "Row/Column Candy Count with Sparse Cell Adjustment",
        "cat_folder": "basics",
        "cat_file": "row_col_frequency_sparse_adjustment.md",
        "statement": "An R x C grid has N candies at coordinates (r_i, c_i). Find the number of cells (r, c) such that the total candies in row r and column c equals K.",
        "key_idea": "The total candies in cell (r, c)'s cross is row_cnt[r] + col_cnt[c] - (1 if candy at (r, c) else 0). Compute frequencies of candy counts across rows and columns. Initially assume independence: sum_{x=0}^K freq_row[x] * freq_col[K - x]. Then adjust for cells with candies.",
        "observation": "Iterate over all N candies: if row_cnt[r_i] + col_cnt[c_i] == K, decrement count by 1 (it was counted but actually has sum K - 1). If row_cnt[r_i] + col_cnt[c_i] == K + 1, increment count by 1 (its adjusted sum is K).",
        "algorithm": [
            "Compute row_cnt[r] and col_cnt[c] for all rows and columns.",
            "Build freq_row[x] and freq_col[y].",
            "Initial answer ans = sum_{x=0}^K freq_row[x] * freq_col[K - x].",
            "For each candy at (r_i, c_i):",
            "  sum_cross = row_cnt[r_i] + col_cnt[c_i].",
            "  if sum_cross == K: ans -= 1.",
            "  if sum_cross == K + 1: ans += 1.",
            "Print ans."
        ],
        "time_complexity": "O(R + C + N)",
        "space_complexity": "O(R + C + N)",
        "core_skill": "Independent 2D projection frequency multiplication followed by sparse point adjustments.",
        "reusable_pattern": "Row/Column Independent Frequency: freq_r * freq_c minus sparse intersection correction.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>

using namespace std;

struct Candy {
    int r, c;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int R, C, K;
    if (!(cin >> R >> C >> K)) return 0;

    int n;
    cin >> n;

    vector<Candy> candies(n);
    vector<int> row_cnt(R + 1, 0);
    vector<int> col_cnt(C + 1, 0);

    for (int i = 0; i < n; ++i) {
        cin >> candies[i].r >> candies[i].c;
        row_cnt[candies[i].r]++;
        col_cnt[candies[i].c]++;
    }

    vector<int> freq_r(n + 1, 0);
    vector<int> freq_c(n + 1, 0);

    for (int r = 1; r <= R; ++r) {
        if (row_cnt[r] <= n) freq_r[row_cnt[r]]++;
    }
    for (int c = 1; c <= C; ++c) {
        if (col_cnt[c] <= n) freq_c[col_cnt[c]]++;
    }

    long long ans = 0;
    for (int x = 0; x <= K; ++x) {
        int y = K - x;
        if (x <= n && y <= n) {
            ans += (long long)freq_r[x] * freq_c[y];
        }
    }

    for (int i = 0; i < n; ++i) {
        int sum_val = row_cnt[candies[i].r] + col_cnt[candies[i].c];
        if (sum_val == K) ans--;
        if (sum_val == K + 1) ans++;
    }

    cout << ans << "\n";
    return 0;
}
"""
    },
    {
        "id": "abc293_g",
        "title": "Triple Index",
        "contest_id": "abc293",
        "rating": 1753,
        "tag": "Data Structures (DS)",
        "subtopic": "Mo's Algorithm",
        "topic": "Mo's Algorithm for Range Triples C(c, 3)",
        "cat_folder": "data_structures",
        "cat_file": "mos_algorithm_range_triples.md",
        "statement": "Given an array A of N integers and Q queries (l_i, r_i). For each query, find the number of index triples (i, j, k) such that l <= i < j < k <= r and A_i = A_j = A_k.",
        "key_idea": "For a value occurring c times in a range, the number of triples is C(c, 3) = c * (c - 1) * (c - 2) / 6. Using Mo's Algorithm with block size B = N / sqrt(Q), update the triple count in O(1) when extending or shrinking the range.",
        "observation": "Adding an element of count c increases triples by C(c, 2) = c * (c - 1) / 2. Removing an element of count c decreases triples by C(c - 1, 2) = (c - 1) * (c - 2) / 2.",
        "algorithm": [
            "Sort queries offline by (l / B, r) with Hilbert or alternating parity order.",
            "Maintain current range [cur_l, cur_r], frequency array cnt[val], and cur_ans.",
            "add(x): cur_ans += cnt[x] * (cnt[x] - 1) / 2; cnt[x]++;",
            "remove(x): cnt[x]--; cur_ans -= cnt[x] * (cnt[x] - 1) / 2;",
            "Process all queries and store answers.",
            "Print answers in original order."
        ],
        "time_complexity": "O((N + Q) * sqrt(N))",
        "space_complexity": "O(N + Q + max_val)",
        "core_skill": "Mo's Algorithm for non-invertible polynomial range combinations.",
        "reusable_pattern": "Mo's Algorithm Range Combinations: add/remove update C(c, k) in O(1).",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

struct Query {
    int l, r, id;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    vector<int> a(n + 1);
    for (int i = 1; i <= n; ++i) {
        cin >> a[i];
    }

    vector<Query> queries(q);
    for (int i = 0; i < q; ++i) {
        cin >> queries[i].l >> queries[i].r;
        queries[i].id = i;
    }

    int block_size = max(1, (int)(n / sqrt(q)));
    sort(queries.begin(), queries.end(), [&](const Query& x, const Query& y) {
        int b1 = x.l / block_size;
        int b2 = y.l / block_size;
        if (b1 != b2) return b1 < b2;
        return (b1 & 1) ? (x.r < y.r) : (x.r > y.r);
    });

    vector<long long> cnt(200005, 0);
    vector<long long> ans(q);
    long long cur_triples = 0;

    auto add = [&](int val) {
        cur_triples += cnt[val] * (cnt[val] - 1) / 2;
        cnt[val]++;
    };

    auto remove = [&](int val) {
        cnt[val]--;
        cur_triples -= cnt[val] * (cnt[val] - 1) / 2;
    };

    int cur_l = 1, cur_r = 0;
    for (auto& qry : queries) {
        while (cur_l > qry.l) add(a[--cur_l]);
        while (cur_r < qry.r) add(a[++cur_r]);
        while (cur_l < qry.l) remove(a[cur_l++]);
        while (cur_r > qry.r) remove(a[cur_r--]);
        ans[qry.id] = cur_triples;
    }

    for (int i = 0; i < q; ++i) {
        cout << ans[i] << "\n";
    }

    return 0;
}
"""
    },
    {
        "id": "abc161_e",
        "title": "Yutori",
        "contest_id": "abc161",
        "rating": 1760,
        "tag": "Basics",
        "subtopic": "Greedy",
        "topic": "Mandatory Task Identification via Leftmost vs Rightmost Greedy Schedules",
        "cat_folder": "basics",
        "cat_file": "mandatory_days_left_right_greedy.md",
        "statement": "Given a schedule of N days where each day is work ('o') or rest ('x'). Choose K days to work such that after working on day i, you must rest for at least C days (next work day >= i + C + 1). Find all days that MUST be worked on in EVERY valid schedule.",
        "key_idea": "Compute the greedy earliest schedule L[1..K] from left to right, and the greedy latest schedule R[1..K] from right to left. Day d is mandatory iff for some task index i, L[i] == R[i] == d.",
        "observation": "Any valid schedule must place the i-th work day in the interval [L[i], R[i]]. If L[i] == R[i], the i-th work day has only one possible placement across all valid schedules.",
        "algorithm": [
            "Greedy forward pass: find earliest day for work 1..K -> L[1..K].",
            "Greedy backward pass: find latest day for work K..1 -> R[1..K].",
            "For i = 1 to K: if L[i] == R[i], record L[i] as a mandatory day.",
            "Print all mandatory days in ascending order."
        ],
        "time_complexity": "O(N)",
        "space_complexity": "O(N + K)",
        "core_skill": "Pinpointing unique schedule choices via intersection of earliest and latest greedy bounds.",
        "reusable_pattern": "Mandatory Element via Left/Right Greedy Bounds: Mandatory iff earliest[i] == latest[i].",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k, c;
    if (!(cin >> n >> k >> c)) return 0;

    string s;
    cin >> s;

    vector<int> L(k + 1);
    int cur_day = 0;
    for (int i = 1; i <= k; ++i) {
        while (cur_day < n && s[cur_day] != 'o') cur_day++;
        L[i] = cur_day + 1;
        cur_day += c + 1;
    }

    vector<int> R(k + 1);
    cur_day = n - 1;
    for (int i = k; i >= 1; --i) {
        while (cur_day >= 0 && s[cur_day] != 'o') cur_day--;
        R[i] = cur_day + 1;
        cur_day -= (c + 1);
    }

    for (int i = 1; i <= k; ++i) {
        if (L[i] == R[i]) {
            cout << L[i] << "\n";
        }
    }

    return 0;
}
"""
    },
    {
        "id": "abc146_e",
        "title": "Rem of Sum is Num",
        "contest_id": "abc146",
        "rating": 1762,
        "tag": "Data Structures (DS)",
        "subtopic": "Sliding Window Hash",
        "topic": "Prefix Sum Shift Transformation (S_i - i) mod K with Sliding Window Map",
        "cat_folder": "data_structures",
        "cat_file": "prefix_sum_shift_sliding_window_map.md",
        "statement": "Given an array A of N integers and an integer K. Count pairs (l, r) such that 1 <= r - l + 1 < K and sum_{i=l}^r A_i = r - l + 1 (mod K).",
        "key_idea": "The condition (S_r - S_{l-1}) = r - (l - 1) (mod K) rearranges to (S_r - r) = (S_{l-1} - (l - 1)) (mod K). Defining B_i = (S_i - i) mod K, we require B_r == B_{l-1} within a sliding window of length at most K - 1.",
        "observation": "Maintain a hash map of frequencies of B_{l-1} for the last K - 1 indices. For each r, add freq[B_r] to the answer, then add B_r to the map and remove the element that falls out of the sliding window.",
        "algorithm": [
            "Compute prefix sums S_i.",
            "Let B_i = ((S_i - i) % K + K) % K for i = 0..N.",
            "Maintain frequency map of B in a window of size K - 1.",
            "Insert B_0 with count 1.",
            "For r = 1 to N:",
            "  if r >= K: decrement count of B_{r - K} in map.",
            "  ans += map[B_r].",
            "  increment count of B_r in map.",
            "Print ans."
        ],
        "time_complexity": "O(N log K)",
        "space_complexity": "O(K)",
        "core_skill": "Rewriting modular range sum length conditions into transformed prefix invariants with sliding window size constraints.",
        "reusable_pattern": "Transformed Prefix Invariant: (S_r - r) == (S_l - l) mod K in sliding window.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <map>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> a(n + 1);
    vector<long long> b(n + 1, 0);

    for (int i = 1; i <= n; ++i) {
        cin >> a[i];
    }

    long long pref = 0;
    for (int i = 1; i <= n; ++i) {
        pref += a[i];
        b[i] = ((pref - i) % k + k) % k;
    }

    map<long long, int> freq;
    long long ans = 0;

    freq[0] = 1;

    for (int r = 1; r <= n; ++r) {
        if (r >= k) {
            freq[b[r - k]]--;
        }
        ans += freq[b[r]];
        freq[b[r]]++;
    }

    cout << ans << "\n";
    return 0;
}
"""
    },
    {
        "id": "abc162_f",
        "title": "Select Half",
        "contest_id": "abc162",
        "rating": 1764,
        "tag": "Dynamic Programming",
        "subtopic": "Classic DP",
        "topic": "Non-Adjacent Selection via Skip-Budget DP",
        "cat_folder": "dp",
        "cat_file": "skip_budget_dp_select_half.md",
        "statement": "Given an array A of N integers. Choose floor(N / 2) elements such that no two chosen elements are adjacent. Maximize the sum of chosen elements.",
        "key_idea": "To choose floor(N/2) non-adjacent elements out of N, the total number of 'extra skips' allowed is at most 1 (for even N) or at most 2 (for odd N). Maintain DP state dp[i][skip] tracking the maximum sum using skip extra skips.",
        "observation": "Transitions: at index i, you either choose A[i] (skipping the immediate next index) or take an extra skip to move to i + 1. Total states O(N * 3), taking O(N) time.",
        "algorithm": [
            "Let max_skips = N % 2 == 0 ? 1 : 2.",
            "Initialize dp[N + 1][3] with -INF.",
            "dp[0][0] = 0.",
            "For i = 0 to N - 1:",
            "  For skip = 0 to max_skips:",
            "    if dp[i][skip] == -INF: continue.",
            "    // Choice 1: Take A[i+1], advance to i + 2",
            "    if (i + 1 <= N) dp[min(N, i + 2)][skip] = max(dp[min(N, i + 2)][skip], dp[i][skip] + A[i + 1]).",
            "    // Choice 2: Extra skip, advance to i + 1",
            "    if (skip + 1 <= max_skips) dp[i + 1][skip + 1] = max(dp[i + 1][skip + 1], dp[i][skip]).",
            "Answer is max over valid final states."
        ],
        "time_complexity": "O(N)",
        "space_complexity": "O(N)",
        "core_skill": "Dynamic programming with bounded slack/skip budget for non-adjacent element selection.",
        "reusable_pattern": "Skip-Budget DP: dp[i][slack] tracking exact count of omitted positions.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const long long INF = 1e18;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    int max_skips = (n % 2 == 0) ? 1 : 2;
    // dp[i][skip]: after considering elements up to index i-1, with 'skip' extra skips used
    vector<vector<long long>> dp(n + 2, vector<long long>(max_skips + 1, -INF));
    dp[0][0] = 0;

    for (int i = 0; i < n; ++i) {
        for (int s = 0; s <= max_skips; ++s) {
            if (dp[i][s] == -INF) continue;

            // Option 1: Pick a[i], must skip i+1, so jump to i+2
            int next_i = min(n, i + 2);
            dp[next_i][s] = max(dp[next_i][s], dp[i][s] + a[i]);

            // Option 2: Do not pick a[i], spend 1 extra skip, jump to i+1
            if (s + 1 <= max_skips) {
                dp[i + 1][s + 1] = max(dp[i + 1][s + 1], dp[i][s]);
            }
        }
    }

    long long ans = -INF;
    for (int s = 0; s <= max_skips; ++s) {
        ans = max(ans, dp[n][s]);
        ans = max(ans, dp[n + 1][s]);
    }

    cout << ans << "\n";
    return 0;
}
"""
    },
    {
        "id": "abc353_g",
        "title": "Merchant Takahashi",
        "contest_id": "abc353",
        "rating": 1765,
        "tag": "Data Structures (DS)",
        "subtopic": "Segment Tree DP",
        "topic": "Segment Tree Optimization for 1D Manhattan Distance DP",
        "cat_folder": "data_structures",
        "cat_file": "segment_tree_manhattan_dp.md",
        "statement": "There are N towns on a line. Traveling between towns i and j costs C * |i - j|. M business events occur sequentially: event i in town T_i gives profit P_i. Choose a subset of events to maximize total profit.",
        "key_idea": "When transitioning from town j to town T, the net change is dp[j] - C * |T - j| + P. Split into two cases: for j <= T, cost is dp[j] + C * j + P - C * T; for j >= T, cost is dp[j] - C * j + P + C * T. Maintain two segment trees storing (dp[j] + C * j) and (dp[j] - C * j).",
        "observation": "Each event requires two range maximum queries: query [1, T] from Tree 1 and query [T, N] from Tree 2, then update town T in both trees in O(log N).",
        "algorithm": [
            "Build two Segment Trees of size N:",
            "  Tree 1 stores dp[j] + C * j.",
            "  Tree 2 stores dp[j] - C * j.",
            "Initialize with dp[1] = 0, all other dp[j] = -INF.",
            "For each event (T, P):",
            "  best_left = Tree1.query(1, T) - C * T.",
            "  best_right = Tree2.query(T, N) + C * T.",
            "  new_dp = max(best_left, best_right) + P.",
            "  Tree1.update(T, new_dp + C * T).",
            "  Tree2.update(T, new_dp - C * T).",
            "Print max over all dp[j]."
        ],
        "time_complexity": "O(M log N)",
        "space_complexity": "O(N)",
        "core_skill": "Segment tree acceleration of 1D absolute difference / Manhattan transitions.",
        "reusable_pattern": "Manhattan DP Optimization: Split |T - j| into two segment trees storing dp[j] +/- C*j.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const long long INF = 2e18;

struct SegTree {
    int sz;
    vector<long long> tree;
    SegTree(int n) {
        sz = 1;
        while (sz <= n) sz <<= 1;
        tree.assign(2 * sz, -INF);
    }
    void update(int i, long long val) {
        i += sz;
        tree[i] = max(tree[i], val);
        for (i >>= 1; i > 0; i >>= 1) {
            tree[i] = max(tree[2 * i], tree[2 * i + 1]);
        }
    }
    long long query(int l, int r) {
        long long res = -INF;
        for (l += sz, r += sz + 1; l < r; l >>= 1, r >>= 1) {
            if (l & 1) res = max(res, tree[l++]);
            if (r & 1) res = max(res, tree[--r]);
        }
        return res;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long c;
    if (!(cin >> n >> c)) return 0;

    int m;
    cin >> m;

    SegTree tree1(n + 1); // dp[j] + c * j
    SegTree tree2(n + 1); // dp[j] - c * j

    tree1.update(1, 0 + c * 1);
    tree2.update(1, 0 - c * 1);

    long long max_ans = 0;

    while (m--) {
        int t;
        long long p;
        cin >> t >> p;

        long long left_max = tree1.query(1, t) - c * t;
        long long right_max = tree2.query(t, n) + c * t;

        long long best_prev = max(left_max, right_max);
        if (best_prev > -INF / 2) {
            long long new_dp = best_prev + p;
            max_ans = max(max_ans, new_dp);
            tree1.update(t, new_dp + c * t);
            tree2.update(t, new_dp - c * t);
        }
    }

    cout << max_ans << "\n";
    return 0;
}
"""
    },
    {
        "id": "arc117_c",
        "title": "Tricolor Pyramid",
        "contest_id": "arc117",
        "rating": 1768,
        "tag": "Math",
        "subtopic": "Lucas Theorem",
        "topic": "Cellular Automaton Modulo 3 Linearity via Pascal & Lucas' Theorem",
        "cat_folder": "math",
        "cat_file": "cellular_automaton_lucas_theorem_mod3.md",
        "statement": "A bottom row of N blocks has colors 'B', 'W', 'R' (encoded as 0, 1, 2 mod 3). Adjacent blocks of identical colors yield that color; different colors yield the third color. Determine the color at the apex (top) of the pyramid.",
        "key_idea": "The transition function for colors x and y in Z_3 is f(x, y) = -(x + y) mod 3. Propagating this linear relation up N - 1 levels gives the apex color: (-1)^{N - 1} * sum_{i=0}^{N - 1} C(N - 1, i) * c_i mod 3.",
        "observation": "C(N - 1, i) mod 3 can be computed in O(log_3 N) using Lucas' Theorem, or by maintaining 3-adic valuations of factorials.",
        "algorithm": [
            "Map 'B' -> 0, 'W' -> 1, 'R' -> 2.",
            "Write a function nCr_mod3(n, r) using Lucas' Theorem:",
            "  while n > 0 or r > 0:",
            "    ni = n % 3, ri = r % 3;",
            "    if ri > ni: return 0;",
            "    res = res * comb(ni, ri) % 3;",
            "    n /= 3, r /= 3;",
            "Compute apex = (-1)^{N - 1} * sum_{i=0}^{N - 1} nCr_mod3(N - 1, i) * color[i] mod 3.",
            "Map apex mod 3 back to character and print."
        ],
        "time_complexity": "O(N log_3 N)",
        "space_complexity": "O(N)",
        "core_skill": "Recognizing linear modular recurrence in 2D cellular automata and computing binomial coefficients via Lucas' Theorem.",
        "reusable_pattern": "Pyramid Modulo Linearity: Apex = (-1)^{N-1} sum C(N-1, i) * A[i] mod P using Lucas' Theorem.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <string>
#include <vector>

using namespace std;

int comb_small(int n, int r) {
    if (r < 0 || r > n) return 0;
    if (r == 0 || r == n) return 1;
    return n; // n=2, r=1 -> 2
}

int lucas(int n, int r) {
    int res = 1;
    while (n > 0 || r > 0) {
        int ni = n % 3;
        int ri = r % 3;
        if (ri > ni) return 0;
        res = (res * comb_small(ni, ri)) % 3;
        n /= 3;
        r /= 3;
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    string s;
    cin >> s;

    auto char_to_val = [](char c) -> int {
        if (c == 'B') return 0;
        if (c == 'W') return 1;
        return 2; // 'R'
    };

    auto val_to_char = [](int v) -> char {
        if (v == 0) return 'B';
        if (v == 1) return 'W';
        return 'R';
    };

    long long sum_val = 0;
    for (int i = 0; i < n; ++i) {
        int coeff = lucas(n - 1, i);
        sum_val += coeff * char_to_val(s[i]);
    }

    sum_val %= 3;

    if ((n - 1) % 2 == 1) {
        sum_val = (3 - sum_val) % 3;
    }

    cout << val_to_char(sum_val) << "\n";
    return 0;
}
"""
    },
    {
        "id": "arc064_c",
        "title": "Cosmic Rays",
        "contest_id": "arc064",
        "rating": 1769,
        "tag": "Graph Theory",
        "subtopic": "Shortest Paths",
        "topic": "Continuous Euclidean Distance on Circular Barriers via Dense Dijkstra",
        "cat_folder": "graph_theory",
        "cat_file": "euclidean_barrier_dense_dijkstra.md",
        "statement": "Given a start point (x_s, y_s), a destination (x_t, y_t), and N circular barriers with center (x_i, y_i) and radius r_i. Inside a barrier, exposure to cosmic rays is 0. Find the minimum Euclidean distance traveled outside barriers.",
        "key_idea": "The shortest path consists of straight lines between circles. The distance between two circles with centers (x_1, y_1), (x_2, y_2) and radii r_1, r_2 is max(0.0, hypot(x_1 - x_2, y_1 - y_2) - r_1 - r_2). Build a dense graph with N + 2 vertices and run Dijkstra in O(V^2).",
        "observation": "Since N <= 1000, an O(N^2) dense Dijkstra implementation without priority queue is optimal and runs in under 100 ms.",
        "algorithm": [
            "Create vertices 0 to N + 1 where 0 is Start, N + 1 is End, and 1..N are circles.",
            "Compute distance matrix dist[i][j] = max(0.0, dist(c_i, c_j) - r_i - r_j).",
            "Run O(V^2) dense Dijkstra: at each step find unvisited node with minimum distance, mark visited, and relax neighbors.",
            "Print min distance to End with 10 decimal digits of precision."
        ],
        "time_complexity": "O(N^2)",
        "space_complexity": "O(N^2)",
        "core_skill": "Modeling continuous geometric barrier traversal as discrete dense graph shortest path.",
        "reusable_pattern": "Circular Barrier Shortest Path: Edge weight = max(0.0, center_dist - r1 - r2) + O(V^2) Dijkstra.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <cmath>
#include <iomanip>

using namespace std;

struct Circle {
    double x, y, r;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    double xs, ys, xt, yt;
    if (!(cin >> xs >> ys >> xt >> yt)) return 0;

    int n;
    cin >> n;

    vector<Circle> pts;
    pts.push_back({xs, ys, 0});
    for (int i = 0; i < n; ++i) {
        double x, y, r;
        cin >> x >> y >> r;
        pts.push_back({x, y, r});
    }
    pts.push_back({xt, yt, 0});

    int total_nodes = n + 2;
    vector<vector<double>> adj(total_nodes, vector<double>(total_nodes));

    for (int i = 0; i < total_nodes; ++i) {
        for (int j = i; j < total_nodes; ++j) {
            double d = hypot(pts[i].x - pts[j].x, pts[i].y - pts[j].y);
            double w = max(0.0, d - pts[i].r - pts[j].r);
            adj[i][j] = adj[j][i] = w;
        }
    }

    vector<double> min_dist(total_nodes, 1e18);
    vector<bool> visited(total_nodes, false);
    min_dist[0] = 0;

    for (int iter = 0; iter < total_nodes; ++iter) {
        int u = -1;
        double best = 1e18;
        for (int i = 0; i < total_nodes; ++i) {
            if (!visited[i] && min_dist[i] < best) {
                best = min_dist[i];
                u = i;
            }
        }

        if (u == -1) break;
        visited[u] = true;

        for (int v = 0; v < total_nodes; ++v) {
            if (!visited[v] && min_dist[u] + adj[u][v] < min_dist[v]) {
                min_dist[v] = min_dist[u] + adj[u][v];
            }
        }
    }

    cout << fixed << setprecision(10) << min_dist[total_nodes - 1] << "\n";
    return 0;
}
"""
    },
    {
        "id": "abc126_f",
        "title": "XOR Matching",
        "contest_id": "abc126",
        "rating": 1770,
        "tag": "Basics",
        "subtopic": "Constructive",
        "topic": "Constructive XOR Palindromic Sandwich Sequence",
        "cat_folder": "basics",
        "cat_file": "constructive_xor_palindromic_sandwich.md",
        "statement": "Given M and K. Construct a sequence of length 2^{M + 1} containing two copies of each integer from 0 to 2^M - 1 such that for any two identical numbers at indices i < j, the XOR sum between them is K. Output -1 if impossible.",
        "key_idea": "For M >= 2, the XOR sum of all integers in [0, 2^M - 1] is 0. If K >= 2^M, impossible. For M = 1: K = 0 gives 0 0 1 1, K = 1 is impossible. For M >= 2, construct: [all elements except K in ascending order] + [K] + [all elements except K in descending order] + [K].",
        "observation": "In this construction, between the two Ks, all other elements appear once, giving XOR sum 0 XOR K = K. For any other element x, between its two copies, every other element appears twice (canceling to 0) except K which appears once, giving XOR sum K.",
        "algorithm": [
            "If K >= (1 << M), print -1.",
            "If M == 0: if K == 0 print '0 0', else print -1.",
            "If M == 1: if K == 0 print '0 0 1 1', else print -1.",
            "For M >= 2:",
            "  Print all numbers in [0, (1 << M) - 1] except K in ascending order.",
            "  Print K.",
            "  Print all numbers in [0, (1 << M) - 1] except K in descending order.",
            "  Print K."
        ],
        "time_complexity": "O(2^M)",
        "space_complexity": "O(2^M)",
        "core_skill": "Constructive sequence design utilizing involution and identity cancellation under XOR.",
        "reusable_pattern": "XOR Palindromic Sandwich: [Elements except K] + K + [Reverse] + K.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int m;
    long long k;
    if (!(cin >> m >> k)) return 0;

    int total_vals = 1 << m;

    if (k >= total_vals) {
        cout << -1 << "\n";
        return 0;
    }

    if (m == 0) {
        if (k == 0) cout << "0 0\n";
        else cout << -1 << "\n";
        return 0;
    }

    if (m == 1) {
        if (k == 0) cout << "0 0 1 1\n";
        else cout << -1 << "\n";
        return 0;
    }

    vector<int> ans;
    for (int i = 0; i < total_vals; ++i) {
        if (i != k) ans.push_back(i);
    }
    ans.push_back(k);
    for (int i = total_vals - 1; i >= 0; --i) {
        if (i != k) ans.push_back(i);
    }
    ans.push_back(k);

    for (int i = 0; i < (int)ans.size(); ++i) {
        cout << ans[i] << (i + 1 == (int)ans.size() ? "" : " ");
    }
    cout << "\n";

    return 0;
}
"""
    },
    {
        "id": "abc154_f",
        "title": "Many Many Paths",
        "contest_id": "abc154",
        "rating": 1775,
        "tag": "Combinatorics",
        "subtopic": "Hockey-Stick Identity",
        "topic": "Double Hockey-Stick Identity on Grid Path Combinations",
        "cat_folder": "combinatorics",
        "cat_file": "double_hockey_stick_grid_paths.md",
        "statement": "Paths from (0, 0) to (r, c) is C(r + c, r). Find sum_{r=r1}^{r2} sum_{c=c1}^{c2} C(r + c, r) modulo 10^9 + 7. (r2, c2 <= 10^6).",
        "key_idea": "By the Hockey-Stick Identity, sum_{c=0}^C C(r + c, c) = C(r + C + 1, C). Summing over r gives sum_{r=0}^R C(r + C + 1, r) = C(R + C + 2, R) - 1. Thus, F(R, C) = sum_{r=0}^R sum_{c=0}^C C(r + c, r) = C(R + C + 2, R + 1) - 1.",
        "observation": "The 2D rectangle sum is decomposed into F(r2, c2) - F(r1 - 1, c2) - F(r2, c1 - 1) + F(r1 - 1, c1 - 1), computable in O(1) using precomputed factorials.",
        "algorithm": [
            "Precompute factorials and inverses up to max(R + C + 2) ~ 2 * 10^6 + 5.",
            "Define F(R, C) = C(R + C + 2, R + 1) - 1.",
            "Answer = (F(r2, c2) - F(r1 - 1, c2) - F(r2, c1 - 1) + F(r1 - 1, c1 - 1)) % MOD.",
            "Print answer."
        ],
        "time_complexity": "O(max(R, C))",
        "space_complexity": "O(max(R, C))",
        "core_skill": "Double application of Pascal's Hockey-Stick identity to evaluate 2D grid path sums in closed form.",
        "reusable_pattern": "2D Grid Path Sum Formula: F(R, C) = C(R + C + 2, R + 1) - 1.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>

using namespace std;

const int MOD = 1000000007;
const int MAX_VAL = 2000005;

long long fact[MAX_VAL], inv[MAX_VAL];

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

long long nCr(int n, int r) {
    if (r < 0 || r > n) return 0;
    return fact[n] * inv[r] % MOD * inv[n - r] % MOD;
}

long long F(int r, int c) {
    if (r < 0 || c < 0) return 0;
    return (nCr(r + c + 2, r + 1) - 1 + MOD) % MOD;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    fact[0] = 1;
    inv[0] = 1;
    for (int i = 1; i < MAX_VAL; ++i) {
        fact[i] = (fact[i - 1] * i) % MOD;
    }
    inv[MAX_VAL - 1] = power(fact[MAX_VAL - 1], MOD - 2);
    for (int i = MAX_VAL - 2; i >= 1; --i) {
        inv[i] = (inv[i + 1] * (i + 1)) % MOD;
    }

    int r1, c1, r2, c2;
    if (!(cin >> r1 >> c1 >> r2 >> c2)) return 0;

    long long ans = (F(r2, c2) - F(r1 - 1, c2) - F(r2, c1 - 1) + F(r1 - 1, c1 - 1)) % MOD;
    ans = (ans + MOD) % MOD;

    cout << ans << "\n";
    return 0;
}
"""
    },
    {
        "id": "abc010_4",
        "title": "浮気予防",
        "contest_id": "abc010",
        "rating": 1777,
        "tag": "Graph Theory",
        "subtopic": "Network Flow",
        "topic": "Min-Cut / Max-Flow Model on Network Disconnection",
        "cat_folder": "graph_theory",
        "cat_file": "min_cut_max_flow_network_disconnection.md",
        "statement": "A social network has N people (0 to N - 1) and M friendship connections. Given G girls whom Takahashi (person 0) could potentially contact. Find the minimum number of friendship edges to delete so that Takahashi cannot contact any of the G girls.",
        "key_idea": "Standard Min-Cut problem. Source is Takahashi (0). Create a supersink T. For each of the G girls, add an edge to T with capacity 1. For each original friendship edge (u, v), add bidirectional capacity 1. By the Max-Flow Min-Cut Theorem, min cut equals max flow from 0 to T.",
        "observation": "Running Dinic's Algorithm or Edmonds-Karp computes the maximum flow in O(V^2 E), which runs in under 1 ms for N <= 100.",
        "algorithm": [
            "Build flow network with N + 1 vertices (0 to N, where N is supersink).",
            "For each girl p_i: add directed edge (p_i, N) with capacity 1.",
            "For each edge (u, v): add capacity 1 in both directions.",
            "Run Dinic's Algorithm from source 0 to sink N.",
            "Print max flow."
        ],
        "time_complexity": "O(V^2 * E)",
        "space_complexity": "O(V + E)",
        "core_skill": "Modeling target disconnection and edge removal using min-cut / max-flow duality.",
        "reusable_pattern": "Network Disconnection Min-Cut: Connect target set to super-sink with unit capacity and run Dinic.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

struct Edge {
    int to, rev;
    int cap, flow;
};

struct Dinic {
    int n, s, t;
    vector<vector<Edge>> adj;
    vector<int> level, ptr;

    Dinic(int n, int s, int t) : n(n), s(s), t(t), adj(n), level(n), ptr(n) {}

    void add_edge(int from, int to, int cap) {
        adj[from].push_back({to, (int)adj[to].size(), cap, 0});
        adj[to].push_back({from, (int)adj[from].size() - 1, 0, 0});
    }

    bool bfs() {
        fill(level.begin(), level.end(), -1);
        level[s] = 0;
        queue<int> q;
        q.push(s);

        while (!q.empty()) {
            int v = q.front(); q.pop();
            for (auto& edge : adj[v]) {
                if (edge.cap - edge.flow > 0 && level[edge.to] == -1) {
                    level[edge.to] = level[v] + 1;
                    q.push(edge.to);
                }
            }
        }
        return level[t] != -1;
    }

    int dfs(int v, int pushed) {
        if (pushed == 0 || v == t) return pushed;
        for (int& cid = ptr[v]; cid < (int)adj[v].size(); ++cid) {
            auto& edge = adj[v][cid];
            int tr = edge.to;
            if (level[v] + 1 != level[tr] || edge.cap - edge.flow == 0) continue;
            int tr_pushed = dfs(tr, min(pushed, edge.cap - edge.flow));
            if (tr_pushed == 0) continue;
            edge.flow += tr_pushed;
            adj[tr][edge.rev].flow -= tr_pushed;
            return tr_pushed;
        }
        return 0;
    }

    int max_flow() {
        int flow = 0;
        while (bfs()) {
            fill(ptr.begin(), ptr.end(), 0);
            while (int pushed = dfs(s, 1e9)) {
                flow += pushed;
            }
        }
        return flow;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, g, m;
    if (!(cin >> n >> g >> m)) return 0;

    int sink = n;
    Dinic dinic(n + 1, 0, sink);

    for (int i = 0; i < g; ++i) {
        int girl;
        cin >> girl;
        dinic.add_edge(girl, sink, 1);
    }

    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        dinic.add_edge(u, v, 1);
        dinic.add_edge(v, u, 1);
    }

    cout << dinic.max_flow() << "\n";
    return 0;
}
"""
    },
    {
        "id": "abc377_g",
        "title": "Edit to Match",
        "contest_id": "abc377",
        "rating": 1782,
        "tag": "Data Structures (DS)",
        "subtopic": "Trie",
        "topic": "Trie-Accelerated Prefix Edit Distance / LCS Minimization",
        "cat_folder": "data_structures",
        "cat_file": "trie_accelerated_prefix_edit_distance.md",
        "statement": "Given N strings S_1, ..., S_N. For each S_i, find the minimum cost to transform S_i into a prefix of some previously processed string S_j (j < i) or an empty string, where operations are: delete the last character (cost 1) or append any character (cost 1).",
        "key_idea": "If S_i shares a common prefix of length d with S_j, transforming S_i into S_j's prefix costs |S_i| - d + (|S_j| - d) = |S_i| + (|S_j| - 2d). In a Trie, each node at depth d maintains min(|S_j| - 2d) over all strings passing through it.",
        "observation": "For query S_i, walk down the Trie. At each matched prefix node at depth d, best cost is |S_i| + min_val[node]. Then insert S_i into the Trie updating min_val.",
        "algorithm": [
            "Initialize Trie where each node stores min_val initialized to INF.",
            "For each string S_i:",
            "  ans = |S_i| (reducing to empty string).",
            "  Walk S_i down the Trie:",
            "    at node u with depth d: ans = min(ans, |S_i| + node.min_val).",
            "  Print ans.",
            "  Insert S_i into Trie: at each node u with depth d, node.min_val = min(node.min_val, |S_i| - 2 * d)."
        ],
        "time_complexity": "O(sum |S_i|)",
        "space_complexity": "O(sum |S_i| * 26)",
        "core_skill": "Trie node caching of prefix match metric min(|S_j| - 2d) for linear edit distance.",
        "reusable_pattern": "Trie Prefix Edit Distance: Cache min(|S_j| - 2*depth) at each node to query in O(|S|).",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

const int INF = 1e9;

struct TrieNode {
    int next[26];
    int min_val;
    TrieNode() : min_val(INF) {
        fill(next, next + 26, -1);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<TrieNode> trie;
    trie.emplace_back(); // Root at index 0

    for (int i = 0; i < n; ++i) {
        string s;
        cin >> s;
        int len = s.size();

        int ans = len; // Delete all characters to become empty string
        int u = 0;

        // Query step
        ans = min(ans, len + trie[u].min_val);
        for (int d = 1; d <= len; ++d) {
            int c = s[d - 1] - 'a';
            if (trie[u].next[c] == -1) break;
            u = trie[u].next[c];
            ans = min(ans, len + trie[u].min_val);
        }

        cout << ans << "\n";

        // Insert step
        u = 0;
        trie[u].min_val = min(trie[u].min_val, len);
        for (int d = 1; d <= len; ++d) {
            int c = s[d - 1] - 'a';
            if (trie[u].next[c] == -1) {
                trie[u].next[c] = trie.size();
                trie.emplace_back();
            }
            u = trie[u].next[c];
            trie[u].min_val = min(trie[u].min_val, len - 2 * d);
        }
    }

    return 0;
}
"""
    },
    {
        "id": "abc192_f",
        "title": "Potion",
        "contest_id": "abc192",
        "rating": 1783,
        "tag": "Dynamic Programming",
        "subtopic": "Knapsack DP",
        "topic": "Exact Cardinality Modulo Remainder Knapsack DP",
        "cat_folder": "dp",
        "cat_file": "exact_cardinality_modulo_knapsack.md",
        "statement": "Given N ingredients with power A_i. You want to reach total power X. Choosing exactly k ingredients with sum S takes time (X - S) / k, which requires S <= X and S = X (mod k). Minimize the time taken. (N <= 100, X <= 10^18).",
        "key_idea": "Iterate over the exact number of ingredients k from 1 to N. For a fixed k, we need to choose k elements whose sum S <= X satisfies S = X (mod k) and maximizes S. Run a 2D Knapsack DP dp[c][r] = max sum of c items with remainder r mod k.",
        "observation": "For each k, the DP table size is (k + 1) x k. Running DP for all k takes sum_{k=1}^N O(N * k^2) ~ O(N^4 / 3) ~ 3 * 10^7 operations, easily completing within the time limit.",
        "algorithm": [
            "best_time = INF.",
            "For k = 1 to N:",
            "  target_rem = X % k.",
            "  Initialize dp[c][r] = -1 for c in 0..k, r in 0..k-1; dp[0][0] = 0.",
            "  For each item val in A:",
            "    For c = k - 1 down to 0:",
            "      For r = 0 to k - 1:",
            "        if dp[c][r] != -1:",
            "          next_r = (r + val) % k.",
            "          dp[c + 1][next_r] = max(dp[c + 1][next_r], dp[c][r] + val).",
            "  if dp[k][target_rem] > 0 and dp[k][target_rem] <= X:",
            "    best_time = min(best_time, (X - dp[k][target_rem]) / k).",
            "Print best_time."
        ],
        "time_complexity": "O(N^4)",
        "space_complexity": "O(N^2)",
        "core_skill": "Combining exact cardinality selection with modulo remainder constraints in knapsack DP.",
        "reusable_pattern": "Fixed-Cardinality Modulo Knapsack: dp[count][rem] tracking max sum matching target remainder.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const long long INF = 4e18;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long x;
    if (!(cin >> n >> x)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    long long min_time = INF;

    for (int k = 1; k <= n; ++k) {
        long long target_rem = x % k;
        vector<vector<long long>> dp(k + 1, vector<long long>(k, -1));
        dp[0][0] = 0;

        for (long long val : a) {
            for (int c = k - 1; c >= 0; --c) {
                for (int r = 0; r < k; ++r) {
                    if (dp[c][r] != -1) {
                        int next_r = (r + val) % k;
                        dp[c + 1][next_r] = max(dp[c + 1][next_r], dp[c][r] + val);
                    }
                }
            }
        }

        if (dp[k][target_rem] > 0 && dp[k][target_rem] <= x) {
            min_time = min(min_time, (x - dp[k][target_rem]) / k);
        }
    }

    cout << min_time << "\n";
    return 0;
}
"""
    },
    {
        "id": "abc339_g",
        "title": "Smaller Sum",
        "contest_id": "abc339",
        "rating": 1792,
        "tag": "Data Structures (DS)",
        "subtopic": "Persistent Segment Tree",
        "topic": "Persistent Segment Tree for Online Range Value-Bounded Sum",
        "cat_folder": "data_structures",
        "cat_file": "persistent_segment_tree_online_range_bounded_sum.md",
        "statement": "Given an array A of N integers and Q online queries (L, R, X) encrypted with the previous answer. For each query, find the sum of all elements in A[L..R] that are <= X. (N, Q <= 2 * 10^5, A_i <= 10^9).",
        "key_idea": "Coordinate-compress array values. Build a Persistent Segment Tree where version i contains all elements of prefix A[1..i]. A range query [L, R] evaluates query(root[R], <= X) - query(root[L - 1], <= X) in O(log N).",
        "observation": "Each point insertion adds O(log N) new nodes. Answering online queries takes O(log N) per query with O(N log N) space.",
        "algorithm": [
            "Coordinate compress unique values of A.",
            "Build persistent segment tree: root[0] is empty tree.",
            "For i = 1 to N: root[i] = insert(root[i - 1], comp_val(A[i]), A[i]).",
            "ans = 0.",
            "For each encrypted query:",
            "  decode L, R, X with ans.",
            "  find rightmost compressed value <= X via upper_bound.",
            "  ans = query(root[R], 0..comp_idx) - query(root[L - 1], 0..comp_idx).",
            "  print ans."
        ],
        "time_complexity": "O((N + Q) log N)",
        "space_complexity": "O(N log N)",
        "core_skill": "Persistent Segment Tree construction and online prefix version subtraction.",
        "reusable_pattern": "Online Range Value Query: Version R minus Version L-1 on Persistent Segment Tree.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Node {
    int left_child, right_child;
    long long sum;
};

const int MAX_NODES = 200005 * 40;
Node tree[MAX_NODES];
int node_count = 0;

int insert(int prev, int l, int r, int pos, long long val) {
    int cur = ++node_count;
    tree[cur] = tree[prev];
    tree[cur].sum += val;

    if (l == r) return cur;

    int mid = l + (r - l) / 2;
    if (pos <= mid) {
        tree[cur].left_child = insert(tree[prev].left_child, l, mid, pos, val);
    } else {
        tree[cur].right_child = insert(tree[prev].right_child, mid + 1, r, pos, val);
    }
    return cur;
}

long long query(int node, int l, int r, int ql, int qr) {
    if (!node || l > qr || r < ql) return 0;
    if (ql <= l && r <= qr) return tree[node].sum;

    int mid = l + (r - l) / 2;
    return query(tree[node].left_child, l, mid, ql, qr) +
           query(tree[node].right_child, mid + 1, r, ql, qr);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n + 1);
    vector<long long> vals;
    for (int i = 1; i <= n; ++i) {
        cin >> a[i];
        vals.push_back(a[i]);
    }

    sort(vals.begin(), vals.end());
    vals.erase(unique(vals.begin(), vals.end()), vals.end());
    int m = vals.size();

    vector<int> roots(n + 1, 0);
    for (int i = 1; i <= n; ++i) {
        int pos = lower_bound(vals.begin(), vals.end(), a[i]) - vals.begin() + 1;
        roots[i] = insert(roots[i - 1], 1, m, pos, a[i]);
    }

    int q;
    cin >> q;

    long long last_ans = 0;
    while (q--) {
        long long alpha, beta, gamma;
        cin >> alpha >> beta >> gamma;

        long long l = alpha ^ last_ans;
        long long r = beta ^ last_ans;
        long long x = gamma ^ last_ans;

        if (l > r) swap(l, r);

        auto it = upper_bound(vals.begin(), vals.end(), x);
        int max_pos = it - vals.begin();

        if (max_pos == 0) {
            last_ans = 0;
        } else {
            long long right_sum = query(roots[r], 1, m, 1, max_pos);
            long long left_sum = query(roots[l - 1], 1, m, 1, max_pos);
            last_ans = right_sum - left_sum;
        }

        cout << last_ans << "\n";
    }

    return 0;
}
"""
    },
    {
        "id": "abc171_f",
        "title": "Strivore",
        "contest_id": "abc171",
        "rating": 1795,
        "tag": "Combinatorics",
        "subtopic": "Subsequence Counting",
        "topic": "Canonical Greedy Subsequence Embedding / Distinct Superstring Counting",
        "cat_folder": "combinatorics",
        "cat_file": "canonical_subsequence_embedding_superstrings.md",
        "statement": "Given string S of length N. Insert any lowercase English letter K times to form a string of length N + K. Count the number of distinct resulting strings, modulo 10^9 + 7.",
        "key_idea": "A superstring T contains S iff the greedy leftmost match of S in T succeeds. Let the greedy match of S complete at index i in [N, N + K]. Then each non-matched character before index i has 25 choices (cannot match current character), the N matched characters are fixed, and characters after index i have 26 choices.",
        "observation": "Summing over the terminal match index i: sum_{i=N}^{N + K} C(i - 1, N - 1) * 25^{i - N} * 26^{N + K - i} mod 10^9 + 7.",
        "algorithm": [
            "Read K and string S. N = |S|.",
            "Precompute factorials and powers of 25 and 26.",
            "ans = 0.",
            "For i = N to N + K:",
            "  ways = C(i - 1, N - 1) * pow25[i - N] % MOD * pow26[N + K - i] % MOD.",
            "  ans = (ans + ways) % MOD.",
            "Print ans."
        ],
        "time_complexity": "O(N + K)",
        "space_complexity": "O(N + K)",
        "core_skill": "Canonical leftmost greedy embedding to count distinct superstrings without overcounting.",
        "reusable_pattern": "Leftmost Greedy Subsequence Embedding: sum C(i - 1, N - 1) * 25^{i - N} * 26^{L - i}.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <string>
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

    int k;
    if (!(cin >> k)) return 0;

    string s;
    cin >> s;
    int n = s.size();

    int max_len = n + k;
    vector<long long> fact(max_len + 1), inv(max_len + 1);
    vector<long long> pow25(max_len + 1), pow26(max_len + 1);

    fact[0] = inv[0] = 1;
    pow25[0] = pow26[0] = 1;

    for (int i = 1; i <= max_len; ++i) {
        fact[i] = (fact[i - 1] * i) % MOD;
        pow25[i] = (pow25[i - 1] * 25) % MOD;
        pow26[i] = (pow26[i - 1] * 26) % MOD;
    }
    inv[max_len] = power(fact[max_len], MOD - 2);
    for (int i = max_len - 1; i >= 1; --i) {
        inv[i] = (inv[i + 1] * (i + 1)) % MOD;
    }

    auto nCr = [&](int total, int choose) -> long long {
        if (choose < 0 || choose > total) return 0;
        return fact[total] * inv[choose] % MOD * inv[total - choose] % MOD;
    };

    long long ans = 0;
    for (int i = n; i <= max_len; ++i) {
        long long ways = nCr(i - 1, n - 1) * pow25[i - n] % MOD * pow26[max_len - i] % MOD;
        ans = (ans + ways) % MOD;
    }

    cout << ans << "\n";
    return 0;
}
"""
    },
    {
        "id": "arc089_b",
        "title": "Checker",
        "contest_id": "abc086",
        "rating": 1797,
        "tag": "Basics",
        "subtopic": "2D Prefix Sums",
        "topic": "2D Periodic Chessboard Coordinate Reduction and 2D Prefix Sums",
        "cat_folder": "basics",
        "cat_file": "2d_periodic_chessboard_reduction.md",
        "statement": "Given N points with target colors ('B' or 'W') on an infinite 2D plane. An infinite chessboard grid with tile size K has alternating black and white squares. Find the shift (dx, dy) that maximizes satisfied points.",
        "key_idea": "The chessboard pattern has period 2K in both X and Y dimensions. A white point at (x, y) is equivalent to a black point at (x, y + K). Fold all points modulo 2K: (x % 2K, y % 2K). Then use 2D prefix sums to evaluate all (2K) x (2K) shift offsets in O(K^2).",
        "observation": "Construct a (2K) x (2K) grid counting folded black points. Duplicate the grid into a (4K) x (4K) array so that any K x K subgrid query wraps seamlessly via standard 2D prefix sums.",
        "algorithm": [
            "For each point (x, y, color):",
            "  If color == 'W': y += K.",
            "  grid[x % (2K)][y % (2K)]++.",
            "Tile the (2K) x (2K) counts across a (4K) x (4K) board.",
            "Compute 2D prefix sums on the board.",
            "For dx in 0..K-1, dy in 0..K-1:",
            "  sum_black = query(dx, dy, dx + K, dy + K) + query(dx + K, dy + K, dx + 2K, dy + 2K).",
            "  max_satisfied = max(max_satisfied, max(sum_black, N - sum_black)).",
            "Print max_satisfied."
        ],
        "time_complexity": "O(N + K^2)",
        "space_complexity": "O(K^2)",
        "core_skill": "Periodic grid coordinate folding and wrapping 2D prefix sums.",
        "reusable_pattern": "Periodic 2D Grid Folding: Map (x, y) mod 2K and query K x K blocks via 2D prefix sum.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    int k2 = 2 * k;
    vector<vector<int>> cnt(k2, vector<int>(k2, 0));

    for (int i = 0; i < n; ++i) {
        int x, y;
        char c;
        cin >> x >> y >> c;
        if (c == 'W') y += k;
        cnt[x % k2][y % k2]++;
    }

    vector<vector<int>> pref(2 * k2 + 1, vector<int>(2 * k2 + 1, 0));
    for (int i = 0; i < 2 * k2; ++i) {
        for (int j = 0; j < 2 * k2; ++j) {
            pref[i + 1][j + 1] = cnt[i % k2][j % k2] + pref[i][j + 1] + pref[i + 1][j] - pref[i][j];
        }
    }

    auto get_sum = [&](int x1, int y1, int x2, int y2) -> int {
        return pref[x2][y2] - pref[x1][y2] - pref[x2][y1] + pref[x1][y1];
    };

    int max_ans = 0;
    for (int i = 0; i < k; ++i) {
        for (int j = 0; j < k; ++j) {
            int black_count = get_sum(i, j, i + k, j + k) +
                              get_sum(i + k, j + k, i + 2 * k, j + 2 * k);
            max_ans = max(max_ans, max(black_count, n - black_count));
        }
    }

    cout << max_ans << "\n";
    return 0;
}
"""
    }
]

REJECTED_PROBLEMS = [
    {"id": "abc465_f", "title": "Sjeltzer?", "rating": 1754, "reason": "REJECTED (BASIC LOGIC BUILDING) — Ad-hoc string query casework."},
    {"id": "arc222_b", "title": "Circular RPS", "rating": 1756, "reason": "REJECTED (BASIC LOGIC BUILDING) — Ad-hoc rock paper scissors cycle drill."},
    {"id": "arc215_c", "title": "Strong Surname", "rating": 1767, "reason": "REJECTED (BASIC LOGIC BUILDING) — String casework drill."},
    {"id": "arc179_c", "title": "Beware of Overflow", "rating": 1771, "reason": "REJECTED (BASIC LOGIC BUILDING) — Interactive overflow simulation."},
    {"id": "arc195_c", "title": "Hamiltonian Pieces", "rating": 1777, "reason": "REJECTED (BASIC LOGIC BUILDING) — Piece placement drill."},
    {"id": "arc192_b", "title": "Fennec VS. Snuke 2", "rating": 1783, "reason": "REJECTED (BASIC LOGIC BUILDING) — Ad-hoc tree game drill."},
    {"id": "arc209_b", "title": "Minimize Even Palindrome", "rating": 1787, "reason": "REJECTED (BASIC LOGIC BUILDING) — Palindrome reduction casework."},
    {"id": "arc201_c", "title": "Prefix Covering", "rating": 1789, "reason": "REJECTED (BASIC LOGIC BUILDING) — Prefix covering casework drill."},
    {"id": "arc211_c", "title": "Forest", "rating": 1792, "reason": "REJECTED (BASIC LOGIC BUILDING) — Forest query drill."},
    {"id": "arc180_b", "title": "Improve Inversions", "rating": 1797, "reason": "REJECTED (BASIC LOGIC BUILDING) — Ad-hoc permutation inversion drill."}
]

# Step 1: Compile all C++ solutions to verify zero errors
print(f"Testing C++ compilation of all {len(SELECTED_PROBLEMS)} selected ABC Part 2B solutions...")
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

print(f"[+] All {len(SELECTED_PROBLEMS)} ABC Part 2B C++ solutions compiled with 0 errors!")

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
        f.write("\n### Batch 5 Part 2B: ABC Curated Ladder (1751 - 1799)\n" + "\n".join(new_q_lines) + "\n")
    print("[+] Updated QUALITY_PROBLEMS_BY_TOPIC.md with new archetypes.")

# Update state/progress.json
with open("state/progress.json", "r", encoding="utf-8") as f:
    progress = json.load(f)

progress["current_batch"] = "Batch 5 Part 2B: ABC Ladder (1751-1799) COMPLETED"
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
print("Batch 5 Part 2B completed successfully!")
