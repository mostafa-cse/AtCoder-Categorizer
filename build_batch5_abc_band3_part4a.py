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
print("      PROCESSING BATCH 5 PART 4A: ABC CURATED LADDER (1900 - 1950)")
print("=" * 75)

SELECTED_PROBLEMS = [
    {
        "id": "arc053_c",
        "title": "魔法使い高橋君",
        "contest_id": "arc053",
        "rating": 1901,
        "tag": "Basics",
        "subtopic": "Greedy",
        "topic": "Greedy Exchange Argument on Bipartite Temperature Deltas (a < b ascending, a >= b descending)",
        "cat_folder": "basics",
        "cat_file": "greedy_exchange_bipartite_deltas.md",
        "statement": "Takahashi casts N spells. Spell i first raises temperature by a_i, then lowers it by b_i. Initial temperature is 0. Find an ordering of all N spells that minimizes the maximum temperature reached at any point.",
        "key_idea": "Partition spells into net-decrease (a_i < b_i) and net-increase (a_i >= b_i). For net-decrease spells, doing them first reduces the baseline for subsequent spells; exchange argument shows sorting them by a_i ascending minimizes peak. For net-increase spells, doing them last after all temperature reductions, reverse view shows sorting by b_i descending minimizes peak.",
        "observation": "For any two spells in the decrease group, max(a_1, a_1 - b_1 + a_2) <= max(a_2, a_2 - b_2 + a_1) holds iff a_1 <= a_2. Hence sorting gives optimal order in O(N log N).",
        "algorithm": [
            "Partition spells into decr (a_i < b_i) and incr (a_i >= b_i).",
            "Sort decr by a_i ascending.",
            "Sort incr by b_i descending.",
            "Simulate the process through decr then incr, maintaining max_temp and current_temp.",
            "Print max_temp."
        ],
        "time_complexity": "O(N log N)",
        "space_complexity": "O(N)",
        "core_skill": "Greedy exchange argument partitioning on asymmetric delta transitions.",
        "reusable_pattern": "Bipartite Delta Ordering: Sort positive gain by a_i asc, negative gain by b_i desc.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Spell {
    long long a, b;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<Spell> decr, incr;
    for (int i = 0; i < n; ++i) {
        long long a, b;
        cin >> a >> b;
        if (a < b) {
            decr.push_back({a, b});
        } else {
            incr.push_back({a, b});
        }
    }

    sort(decr.begin(), decr.end(), [](const Spell& x, const Spell& y) {
        return x.a < y.a;
    });

    sort(incr.begin(), incr.end(), [](const Spell& x, const Spell& y) {
        return x.b > y.b;
    });

    long long current = 0;
    long long max_temp = 0;

    for (const auto& s : decr) {
        max_temp = max(max_temp, current + s.a);
        current += (s.a - s.b);
    }

    for (const auto& s : incr) {
        max_temp = max(max_temp, current + s.a);
        current += (s.a - s.b);
    }

    cout << max_temp << "\n";
    return 0;
}
"""
    },
    {
        "id": "arc004_3",
        "title": "平均値太郎の憂鬱",
        "contest_id": "arc004",
        "rating": 1904,
        "tag": "Math",
        "subtopic": "Analytical Bounds",
        "topic": "Average Remainder Bounding and Modular Divisibility on Truncated Arithmetic Progression",
        "cat_folder": "math",
        "cat_file": "truncated_arithmetic_progression_average_bounds.md",
        "statement": "From 1, 2, ..., N, one element M (1 <= M <= N) is removed. The average of the remaining N - 1 numbers is X / Y in irreducible fraction form. Find all valid pairs (N, M), or report Impossible.",
        "key_idea": "Total sum is N(N+1)/2. Removing M gives sum S = N(N+1)/2 - M = X(N - 1) / Y. Since 1 <= M <= N, the average S / (N - 1) must lie strictly in [N/2, (N+2)/2]. This restricts N to at most two integer candidates near 2X/Y. Furthermore, Y must divide X(N - 1), so N = 1 mod Y.",
        "observation": "N is tightly bounded within |N - 2X/Y| <= 1. Testing these candidates takes O(1) time.",
        "algorithm": [
            "Reduce X / Y by gcd.",
            "Bound candidate N values in [2X/Y - 1, 2X/Y + 1].",
            "For each N >= 2, check if (N - 1) % Y == 0.",
            "If so, compute S = (N - 1) / Y * X, and M = N(N + 1) / 2 - S.",
            "If 1 <= M <= N, output (N, M). If no pair is valid, print Impossible."
        ],
        "time_complexity": "O(1)",
        "space_complexity": "O(1)",
        "core_skill": "Deriving tight analytical bounds on arithmetic sequences combined with modular divisibility.",
        "reusable_pattern": "Truncated AP Bounding: Average restricts N to 2X/Y +/- 1 with N = 1 mod Y.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <numeric>
#include <vector>

using namespace std;

long long gcd_val(long long a, long long b) {
    while (b) {
        a %= b;
        swap(a, b);
    }
    return a;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long X, Y;
    char slash;
    if (!(cin >> X >> slash >> Y)) return 0;

    long long g = gcd_val(X, Y);
    X /= g;
    Y /= g;

    long long low_N = 2 * X / Y - 1;
    long long high_N = 2 * X / Y + 1;
    if (low_N < 2) low_N = 2;

    bool found = false;
    for (long long N = low_N; N <= high_N; ++N) {
        if ((N - 1) % Y == 0) {
            long long k = (N - 1) / Y;
            long long S = k * X;
            long long total = N * (N + 1) / 2;
            long long M = total - S;
            if (M >= 1 && M <= N) {
                cout << N << " " << M << "\n";
                found = true;
            }
        }
    }

    if (!found) {
        cout << "Impossible\n";
    }

    return 0;
}
"""
    },
    {
        "id": "arc014_4",
        "title": "grepマスター",
        "contest_id": "arc014",
        "rating": 1904,
        "tag": "Data Structures (DS)",
        "subtopic": "Binary Search / Prefix Sums",
        "topic": "Interval Union under Bounded Expansion via Sorted Gap Prefix Sums",
        "cat_folder": "data_structures",
        "cat_file": "interval_union_sorted_gap_prefix_sums.md",
        "statement": "Given N matched line positions L_1 < L_2 < ... < L_N in an all-line file. Answer M queries (X, Y): each match displays [L_i - X, L_i + Y] clamped to [1, all]. Output the number of uniquely displayed lines.",
        "key_idea": "Match intervals expand by X to the left and Y to the right (total expansion S = X + Y between adjacent matches). The gap between L_i and L_{i+1} is d_i = L_{i+1} - L_i - 1. The number of covered lines between them is min(d_i, S). Sort all gaps d_i; for each query S, binary search splits gaps into those <= S (sum from prefix sums) and those > S ((count) * S). Boundary matches expand by min(X, L_1 - 1) and min(Y, all - L_N).",
        "observation": "Sorting gaps once in O(N log N) allows answering each query in O(log N).",
        "algorithm": [
            "Compute gaps d_i = L_{i+1} - L_i - 1 for i = 1..N-1.",
            "Sort gaps and compute prefix sums.",
            "For each query (X, Y): S = X + Y.",
            "idx = upper_bound(d.begin(), d.end(), S) - d.begin().",
            "ans = N + min(X, L_1 - 1) + min(Y, all - L_N) + pref[idx] + (N - 1 - idx) * S.",
            "Print ans."
        ],
        "time_complexity": "O(N log N + M log N)",
        "space_complexity": "O(N)",
        "core_skill": "Binary search on sorted gap differences to evaluate bounded interval unions in logarithmic time.",
        "reusable_pattern": "Interval Union on Points: sum(min(gap_i, S)) answered via binary search on sorted gaps.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long all;
    int n, m;
    if (!(cin >> all >> n >> m)) return 0;

    vector<long long> l(n);
    for (int i = 0; i < n; ++i) {
        cin >> l[i];
    }

    vector<long long> d(n - 1);
    for (int i = 0; i < n - 1; ++i) {
        d[i] = l[i + 1] - l[i] - 1;
    }
    sort(d.begin(), d.end());

    vector<long long> pref(n, 0);
    for (int i = 0; i < n - 1; ++i) {
        pref[i + 1] = pref[i] + d[i];
    }

    for (int q = 0; q < m; ++q) {
        long long x, y;
        cin >> x >> y;

        long long left_ext = min(x, l[0] - 1);
        long long right_ext = min(y, all - l[n - 1]);
        long long s = x + y;

        int idx = upper_bound(d.begin(), d.end(), s) - d.begin();
        long long gap_sum = pref[idx] + (long long)(n - 1 - idx) * s;

        long long ans = n + left_ext + right_ext + gap_sum;
        cout << ans << "\n";
    }

    return 0;
}
"""
    },
    {
        "id": "abc149_e",
        "title": "Handshake",
        "contest_id": "abc149",
        "rating": 1905,
        "tag": "Basics",
        "subtopic": "Binary Search",
        "topic": "Top-M Pairwise Sums via Threshold Binary Search and Prefix Accumulation",
        "cat_folder": "basics",
        "cat_file": "top_m_pairwise_sums_binary_search.md",
        "statement": "Given N power values A_1, ..., A_N. Choose M ordered pairs (i, j) (1 <= i, j <= N) to maximize the sum of (A_i + A_j). Output the maximum sum.",
        "key_idea": "Binary search on the minimum pair sum threshold S such that at least M pairs have A_i + A_j >= S. For sorted array A, counting pairs with A_i + A_j >= S takes O(N) using two pointers/lower_bound. After finding the maximal S, sum all pairs with sum > S using prefix sums of A, and fill the remaining M - count(S + 1) pairs with exact value S.",
        "observation": "Monotonicity in pair sum allows determining both the cut-off value and exact sum in O(N log(max A)).",
        "algorithm": [
            "Sort A ascending and build prefix sums.",
            "Binary search S in [0, 2 * max(A)]: count pairs with A_i + A_j >= S.",
            "Find largest S with count(S) >= M.",
            "Sum all pairs with A_i + A_j > S via prefix sums: A_i * count + sum_{j}(A_j).",
            "Add (M - total_pairs_added) * S.",
            "Print total sum."
        ],
        "time_complexity": "O(N log(max A))",
        "space_complexity": "O(N)",
        "core_skill": "Dual binary search on pairwise value threshold combined with prefix sum contribution accumulation.",
        "reusable_pattern": "Top-M Pair Sums: Binary search threshold S, sum all pairs > S, pad remainder with S.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long m;
    if (!(cin >> n >> m)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }
    sort(a.begin(), a.end());

    vector<long long> pref(n + 1, 0);
    for (int i = 0; i < n; ++i) {
        pref[i + 1] = pref[i] + a[i];
    }

    auto count_pairs = [&](long long mid) -> long long {
        long long cnt = 0;
        for (int i = 0; i < n; ++i) {
            long long req = mid - a[i];
            int idx = lower_bound(a.begin(), a.end(), req) - a.begin();
            cnt += (n - idx);
        }
        return cnt;
    };

    long long low = 0, high = 2000000;
    long long best_mid = 0;
    while (low <= high) {
        long long mid = low + (high - low) / 2;
        if (count_pairs(mid) >= m) {
            best_mid = mid;
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }

    long long total_sum = 0;
    long long total_pairs = 0;
    for (int i = 0; i < n; ++i) {
        long long req = best_mid + 1 - a[i];
        int idx = lower_bound(a.begin(), a.end(), req) - a.begin();
        long long count = n - idx;
        if (count > 0) {
            total_sum += a[i] * count + (pref[n] - pref[idx]);
            total_pairs += count;
        }
    }

    total_sum += (m - total_pairs) * best_mid;
    cout << total_sum << "\n";
    return 0;
}
"""
    },
    {
        "id": "arc058_b",
        "title": "Iroha and a Grid",
        "contest_id": "arc058",
        "rating": 1905,
        "tag": "Combinatorics",
        "subtopic": "Grid Paths",
        "topic": "Grid Path Combinations with Rectangular Cutout via Bottleneck Diagonal Partition",
        "cat_folder": "combinatorics",
        "cat_file": "grid_paths_cutout_bottleneck_partition.md",
        "statement": "In an H x W grid, the bottom-left A x B subgrid (rows H-A+1..H, cols 1..B) cannot be entered. Find the number of paths from (1, 1) to (H, W) moving only right and down, modulo 10^9 + 7.",
        "key_idea": "Every valid path must cross column B to column B + 1 at some row i in [1, H - A]. Since the step from (i, B) to (i, B + 1) is horizontal, each crossing row i defines a disjoint set of paths. The number of paths through row i is binom((i - 1) + (B - 1), i - 1) * binom((H - i) + (W - B - 1), H - i). Summing over all 1 <= i <= H - A gives the answer.",
        "observation": "Partitioning paths by the unique step across the vertical cut-line boundary decomposes the restricted grid into independent binomial products.",
        "algorithm": [
            "Precompute factorials and inverse factorials up to H + W.",
            "Iterate row i from 1 to H - A.",
            "ways = binom(i - 1 + B - 1, i - 1) * binom(H - i + W - B - 1, H - i) % MOD.",
            "ans = (ans + ways) % MOD.",
            "Print ans."
        ],
        "time_complexity": "O(H + W)",
        "space_complexity": "O(H + W)",
        "core_skill": "Partitioning constrained grid walks by a minimal cut line of disjoint boundary transitions.",
        "reusable_pattern": "Cutout Grid Walk: Sum over boundary crossing cells binom(start -> (i, B)) * binom((i, B+1) -> target).",
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

long long modInverse(long long n) {
    return power(n, MOD - 2);
}

void precompute() {
    fact[0] = 1;
    invFact[0] = 1;
    for (int i = 1; i < MAX; i++) {
        fact[i] = (fact[i - 1] * i) % MOD;
    }
    invFact[MAX - 1] = modInverse(fact[MAX - 1]);
    for (int i = MAX - 2; i >= 1; i--) {
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

    int h, w, a, b;
    if (!(cin >> h >> w >> a >> b)) return 0;

    long long ans = 0;
    for (int i = 1; i <= h - a; ++i) {
        long long ways1 = nCr((i - 1) + (b - 1), i - 1);
        long long ways2 = nCr((h - i) + (w - b - 1), h - i);
        long long term = (ways1 * ways2) % MOD;
        ans = (ans + term) % MOD;
    }

    cout << ans << "\n";
    return 0;
}
"""
    },
    {
        "id": "arc136_d",
        "title": "Without Carry",
        "contest_id": "arc136",
        "rating": 1908,
        "tag": "Dynamic Programming (DP)",
        "subtopic": "SOS DP / Fast Zeta Transform",
        "topic": "Base-10 Multi-Dimensional Fast Zeta Transform / SOS DP for Carry-Free Pairs",
        "cat_folder": "dp",
        "cat_file": "base10_fast_zeta_transform_carry_free.md",
        "statement": "Given N integers A_1, ..., A_N (A_i < 10^6). Find the number of pairs (i, j) with i < j such that A_i + A_j does not produce any carry in base 10.",
        "key_idea": "A_i + A_j has no carry iff for all 6 digits d, digit_d(A_i) + digit_d(A_j) <= 9, or digit_d(A_j) <= 9 - digit_d(A_i). Let comp(A_i) be the number with digits 9 - digit_d(A_i). We need the count of A_j whose digits are sub-digits of comp(A_i). This is a 6-dimensional submask sum query over base 10, solved in 6 * 10^6 operations via Fast Zeta Transform (SOS DP in base 10).",
        "observation": "Base-10 SOS DP computes multidimensional prefix sums over Cartesian product of 6 dimensions [0..9].",
        "algorithm": [
            "Store frequency of each A_i in dp array of size 10^6.",
            "For each dimension d in 0..5 (place value 10^d): for i = 0 to 999999: if digit < 9, dp[i + 10^d] += dp[i].",
            "For each A_i, query dp[comp(A_i)]. Subtract 1 if A_i + A_i has no carry.",
            "Divide the sum by 2 and print."
        ],
        "time_complexity": "O(6 * 10^6 + N)",
        "space_complexity": "O(10^6)",
        "core_skill": "Multi-dimensional Fast Zeta Transform / SOS DP generalized to base 10.",
        "reusable_pattern": "Base-10 SOS DP: Iterate digit positions d, add dp[i] to dp[i + 10^d] for digit < 9.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>

using namespace std;

const int MAX = 1000000;
int dp[MAX];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> arr(n);
    for (int i = 0; i < n; ++i) {
        cin >> arr[i];
        dp[arr[i]]++;
    }

    // Fast Zeta Transform (SOS DP) in base 10 across 6 digits
    int p10 = 1;
    for (int d = 0; d < 6; ++d) {
        for (int i = 0; i < MAX; ++i) {
            if ((i / p10) % 10 < 9) {
                dp[i + p10] += dp[i];
            }
        }
        p10 *= 10;
    }

    auto get_comp = [](int x) {
        int comp = 0;
        int p = 1;
        for (int d = 0; d < 6; ++d) {
            int digit = (x / p) % 10;
            comp += (9 - digit) * p;
            p *= 10;
        }
        return comp;
    };

    long long total_pairs = 0;
    for (int i = 0; i < n; ++i) {
        int comp = get_comp(arr[i]);
        int count = dp[comp];
        bool self_ok = true;
        int temp = arr[i];
        while (temp > 0) {
            if ((temp % 10) * 2 >= 10) {
                self_ok = false;
                break;
            }
            temp /= 10;
        }
        if (self_ok) {
            count--;
        }
        total_pairs += count;
    }

    cout << total_pairs / 2 << "\n";
    return 0;
}
"""
    },
    {
        "id": "arc112_c",
        "title": "DFS Game",
        "contest_id": "arc112",
        "rating": 1913,
        "tag": "Game Theory",
        "subtopic": "Tree Games / Minimax",
        "topic": "Tree DFS Minimax Game with Subtree Size Parity Inversion and Greedy Child Ordering",
        "cat_folder": "game_theory",
        "cat_file": "tree_dfs_minimax_parity_inversion.md",
        "statement": "Rooted tree with N vertices, 1 coin per vertex. Two players explore tree via DFS. When entering a node, player collects its coin. Player chooses which unvisited child to visit next. When DFS returns from a child, player who moves next depends on whether subtree size is odd or even. Minimax coins for Takahashi.",
        "key_idea": "Let f[u] be the net difference (mover - other) from subtree u. Node u gives +1 coin. If child v has even size sz[v], the same player gets the turn upon return. Thus first player greedily takes all even subtrees with f[v] > 0 first. Odd subtrees change the turn upon return; first player sorts odd subtrees to alternate picks greedily. Finally, even subtrees with negative values are consumed by whoever is left with the turn.",
        "observation": "Subtree parity dictates control flow: even size preserves initiative, odd size flips initiative.",
        "algorithm": [
            "Post-order DFS computing sz[u] and f[u].",
            "Categorize children into even_pos (sz even, f > 0), even_neg (sz even, f <= 0), and odd (sz odd).",
            "base_val = 1 + sum(even_pos).",
            "Sort odd ascending; alternate signs: base_val += sign * odd[i], sign = -sign.",
            "Add remaining even_neg with current sign: base_val += sign * sum(even_neg).",
            "f[u] = base_val.",
            "Takahashi's total coins = (N + f[1]) / 2."
        ],
        "time_complexity": "O(N log N)",
        "space_complexity": "O(N)",
        "core_skill": "Minimax game theory on trees with parity-driven initiative transfer and optimal child sorting.",
        "reusable_pattern": "Tree DFS Minimax: Even sz subtrees retain turn; odd sz subtrees flip turn, sorted greedily.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

using namespace std;

int n;
vector<vector<int>> adj;
vector<int> sz;
vector<int> f;

void dfs(int u) {
    sz[u] = 1;
    vector<int> even_pos;
    vector<int> even_neg;
    vector<int> odd;

    int base_val = 1;

    for (int v : adj[u]) {
        dfs(v);
        sz[u] += sz[v];
        if (sz[v] % 2 == 0) {
            if (f[v] > 0) {
                even_pos.push_back(f[v]);
            } else {
                even_neg.push_back(f[v]);
            }
        } else {
            odd.push_back(f[v]);
        }
    }

    for (int x : even_pos) {
        base_val += x;
    }

    sort(odd.begin(), odd.end());
    int sign = -1;
    for (int x : odd) {
        base_val += sign * x;
        sign = -sign;
    }

    for (int x : even_neg) {
        base_val += sign * x;
    }

    f[u] = base_val;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n)) return 0;

    adj.assign(n + 1, vector<int>());
    sz.assign(n + 1, 0);
    f.assign(n + 1, 0);

    for (int i = 2; i <= n; ++i) {
        int p;
        cin >> p;
        adj[p].push_back(i);
    }

    dfs(1);

    int takahashi = (n + f[1]) / 2;
    cout << takahashi << "\n";
    return 0;
}
"""
    },
    {
        "id": "abc009_3",
        "title": "辞書式順序ふたたび",
        "contest_id": "abc009",
        "rating": 1915,
        "tag": "Basics",
        "subtopic": "Greedy",
        "topic": "Greedy Lexicographical String Construction with Feasibility Verification under Edit Budget",
        "cat_folder": "basics",
        "cat_file": "greedy_lexicographical_edit_budget_feasibility.md",
        "statement": "Given string S of length N (N <= 100) and integer K. Find the lexicographically smallest anagram T of S such that T differs from S in at most K positions.",
        "key_idea": "Construct T character by character from position 0 to N - 1. At index i, try characters c in ['a'..'z'] in alphabetical order. If character c is placed at position i, verify whether the remaining characters can be assigned to satisfy the edit budget K. The minimum extra mismatches for suffix i + 1..N - 1 is (length - sum_{ch} min(count_T(ch), count_S(ch))). If (current_diff + extra_diff <= K), greedily commit to c.",
        "observation": "Checking feasibility for each character takes O(|Sigma|) using multiset intersection, allowing exact lexicographical greedy choice.",
        "algorithm": [
            "Count initial character frequencies of S.",
            "For position i = 0 to N - 1:",
            "  For character c = 0 to 25:",
            "    If count[c] == 0 continue.",
            "    Temporarily place c at T[i].",
            "    Compute cur_diff = diff_so_far + (c != S[i]).",
            "    Calculate max possible matches on remaining suffix: sum min(count[ch], s_rem[ch]).",
            "    If cur_diff + extra_diff <= K, commit to c and break.",
            "Print T."
        ],
        "time_complexity": "O(N^2 * 26)",
        "space_complexity": "O(N)",
        "core_skill": "Greedy lexicographical construction with forward-looking multiset matchability verification.",
        "reusable_pattern": "Greedy Anagram Prefix: Test 'a'..'z', verify if remaining character multiset can match suffix within budget K.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;
    string s;
    cin >> s;

    vector<int> count(26, 0);
    for (char c : s) count[c - 'a']++;

    string t = "";
    int diff_so_far = 0;

    for (int i = 0; i < n; ++i) {
        for (int c = 0; c < 26; ++c) {
            if (count[c] == 0) continue;

            count[c]--;
            int cur_diff = diff_so_far + (c != (s[i] - 'a'));

            vector<int> s_rem(26, 0);
            for (int j = i + 1; j < n; ++j) {
                s_rem[s[j] - 'a']++;
            }

            int matches = 0;
            for (int ch = 0; ch < 26; ++ch) {
                matches += min(count[ch], s_rem[ch]);
            }
            int extra_diff = (n - 1 - i) - matches;

            if (cur_diff + extra_diff <= k) {
                t += (char)('a' + c);
                diff_so_far = cur_diff;
                break;
            }

            count[c]++;
        }
    }

    cout << t << "\n";
    return 0;
}
"""
    },
    {
        "id": "abc142_f",
        "title": "Pure",
        "contest_id": "abc142",
        "rating": 1919,
        "tag": "Graph Theory",
        "subtopic": "Cycles / BFS",
        "topic": "Induced Directed Cycle Extraction via Shortest Cycle BFS Search",
        "cat_folder": "graph_theory",
        "cat_file": "induced_directed_cycle_shortest_bfs.md",
        "statement": "Given a directed graph with N vertices and M edges. Find an induced subgraph where every vertex has in-degree 1 and out-degree 1 (an induced simple directed cycle with zero chord edges), or report -1.",
        "key_idea": "Any chord in a directed cycle splits it into strictly shorter directed cycles. Therefore, a directed cycle of MINIMUM LENGTH in the graph cannot have any chord edges, making it guaranteed to be an induced cycle! Finding the shortest directed cycle is achieved by running BFS from every vertex s in O(N * (N + M)).",
        "observation": "Min-length cycle has no chords => Every vertex in the cycle has indegree 1 and outdegree 1 in the induced subgraph.",
        "algorithm": [
            "For each vertex s = 1..N:",
            "  Run BFS from s.",
            "  If an edge u -> s is encountered, cycle length is dist[u] + 1.",
            "  Track the global minimum cycle length and reconstruct the cycle path.",
            "If no cycle found, output -1.",
            "Otherwise print cycle size and vertices in cyclic order."
        ],
        "time_complexity": "O(N * (N + M))",
        "space_complexity": "O(N + M)",
        "core_skill": "Proving that minimal cycles are chordless, reducing induced cycle extraction to All-Pairs BFS.",
        "reusable_pattern": "Chordless Cycle Extraction: The shortest directed cycle in G is always an induced cycle.",
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

    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
    }

    int min_len = n + 1;
    vector<int> best_cycle;

    for (int s = 1; s <= n; ++s) {
        vector<int> dist(n + 1, -1);
        vector<int> parent(n + 1, -1);
        queue<int> q;

        dist[s] = 0;
        q.push(s);

        int cycle_end = -1;

        while (!q.empty()) {
            int u = q.front();
            q.pop();

            bool found = false;
            for (int v : adj[u]) {
                if (v == s && dist[u] + 1 < min_len) {
                    min_len = dist[u] + 1;
                    cycle_end = u;
                    found = true;
                    break;
                }
                if (dist[v] == -1) {
                    dist[v] = dist[u] + 1;
                    parent[v] = u;
                    q.push(v);
                }
            }
            if (found) break;
        }

        if (cycle_end != -1) {
            vector<int> path;
            int curr = cycle_end;
            while (curr != s) {
                path.push_back(curr);
                curr = parent[curr];
            }
            path.push_back(s);
            reverse(path.begin(), path.end());
            best_cycle = path;
        }
    }

    if (best_cycle.empty()) {
        cout << -1 << "\n";
    } else {
        cout << best_cycle.size() << "\n";
        for (int node : best_cycle) {
            cout << node << "\n";
        }
    }

    return 0;
}
"""
    },
    {
        "id": "arc026_3",
        "title": "蛍光灯",
        "contest_id": "arc026",
        "rating": 1930,
        "tag": "Dynamic Programming (DP)",
        "subtopic": "DP Optimization using Data Structures",
        "topic": "Interval Cover Minimum Cost DP Accelerated by Range Minimum Segment Tree",
        "cat_folder": "dp",
        "cat_file": "interval_cover_segment_tree_min_dp.md",
        "statement": "A street of length L must be illuminated. N lights are available; light i covers [l_i, r_i] with cost c_i. Find the minimum cost to completely illuminate [0, L].",
        "key_idea": "Sort lights by r_i ascending. Let dp[x] be the minimum cost to illuminate [0, x]. For light covering [l_i, r_i] with cost c_i, the new covered prefix can reach r_i if some point in [l_i, r_i] was already illuminated: dp[r_i] = min(dp[r_i], min_{x in [l_i, r_i]} dp[x] + c_i). Range minimum query on [l_i, r_i] is handled by a Segment Tree in O(log L).",
        "observation": "Maintaining prefix coverage DP via Segment Tree range minimum queries reduces interval coverage to O(N log L).",
        "algorithm": [
            "Sort lights by right endpoint r_i.",
            "Initialize Segment Tree over [0, L] with INF, and dp[0] = 0.",
            "For each light (l_i, r_i, c_i):",
            "  best_prev = query_min(l_i, r_i).",
            "  if best_prev < INF: update(r_i, best_prev + c_i).",
            "Print query_min(L, L)."
        ],
        "time_complexity": "O(N log N + N log L)",
        "space_complexity": "O(L)",
        "core_skill": "Accelerating 1D contiguous coverage dynamic programming using Segment Tree range minimum queries.",
        "reusable_pattern": "Interval Cover DP: dp[r] = min_{k in [l, r]} dp[k] + cost, maintained via Segment Tree.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const long long INF = 1e18;

struct Light {
    int l, r;
    long long c;
};

int n, L;
vector<long long> tree;

void update(int node, int start, int end, int idx, long long val) {
    if (start == end) {
        tree[node] = min(tree[node], val);
        return;
    }
    int mid = start + (end - start) / 2;
    if (idx <= mid) {
        update(2 * node, start, mid, idx, val);
    } else {
        update(2 * node + 1, mid + 1, end, idx, val);
    }
    tree[node] = min(tree[2 * node], tree[2 * node + 1]);
}

long long query(int node, int start, int end, int l, int r) {
    if (r < start || end < l) return INF;
    if (l <= start && end <= r) return tree[node];
    int mid = start + (end - start) / 2;
    return min(query(2 * node, start, mid, l, r), query(2 * node + 1, mid + 1, end, l, r));
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n >> L)) return 0;

    vector<Light> lights(n);
    for (int i = 0; i < n; ++i) {
        cin >> lights[i].l >> lights[i].r >> lights[i].c;
    }

    sort(lights.begin(), lights.end(), [](const Light& a, const Light& b) {
        if (a.r != b.r) return a.r < b.r;
        return a.l < b.l;
    });

    tree.assign(4 * (L + 1), INF);
    update(1, 0, L, 0, 0);

    for (const auto& lt : lights) {
        long long best_prev = query(1, 0, L, lt.l, lt.r);
        if (best_prev < INF) {
            update(1, 0, L, lt.r, best_prev + lt.c);
        }
    }

    long long ans = query(1, 0, L, L, L);
    cout << ans << "\n";
    return 0;
}
"""
    },
    {
        "id": "abc131_f",
        "title": "Must Be Rectangular!",
        "contest_id": "abc131",
        "rating": 1937,
        "tag": "Graph Theory",
        "subtopic": "Connected Components / Bipartite Graphs",
        "topic": "Bipartite Component Product Transformation for 2D Grid Point Rectangulation",
        "cat_folder": "graph_theory",
        "cat_file": "bipartite_component_grid_rectangulation.md",
        "statement": "Given N points (x_i, y_i) in 2D plane. If points exist at (x_1, y_1), (x_1, y_2), (x_2, y_1), you can add (x_2, y_2). Find maximum number of added points.",
        "key_idea": "Model 2D points as edges in a bipartite graph between X coordinates and Y coordinates. The operation states: if edges (x_1, y_1), (x_1, y_2), (x_2, y_1) exist, add (x_2, y_2). This means any X and Y in the same connected component can eventually be connected! Each connected component becomes a complete bipartite graph K_{|X_c|, |Y_c|}. The maximum total points is sum_{c} (|X_c| * |Y_c|), and the number of added points is this sum minus N.",
        "observation": "Transitive closure on grid coordinates creates complete bipartite graphs on each connected component.",
        "algorithm": [
            "Use Disjoint Set Union (DSU) with 2 * MAX vertices (X in 1..MAX, Y in MAX+1..2*MAX).",
            "For each point (x, y), union x and y + MAX.",
            "Track the count of X vertices and Y vertices in each DSU root.",
            "Total possible points = sum_{roots} (size_x[r] * size_y[r]).",
            "Output total_possible - N."
        ],
        "time_complexity": "O(N * alpha(MAX))",
        "space_complexity": "O(MAX)",
        "core_skill": "Bipartite graph modeling of 2D coordinates with complete component product evaluation.",
        "reusable_pattern": "Grid Point Rectangulation: Model (x, y) as bipartite edge; max edges = sum(X_c * Y_c).",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>

using namespace std;

const int MAX = 100001;

int parent_arr[2 * MAX];
long long size_x[2 * MAX];
long long size_y[2 * MAX];

int find_set(int v) {
    if (v == parent_arr[v]) return v;
    return parent_arr[v] = find_set(parent_arr[v]);
}

void union_sets(int a, int b) {
    a = find_set(a);
    b = find_set(b);
    if (a != b) {
        parent_arr[b] = a;
        size_x[a] += size_x[b];
        size_y[a] += size_y[b];
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    for (int i = 0; i < 2 * MAX; ++i) {
        parent_arr[i] = i;
        if (i < MAX) size_x[i] = 1;
        else size_y[i] = 1;
    }

    for (int i = 0; i < n; ++i) {
        int x, y;
        cin >> x >> y;
        union_sets(x, y + MAX);
    }

    long long max_points = 0;
    for (int i = 0; i < 2 * MAX; ++i) {
        if (parent_arr[i] == i) {
            max_points += size_x[i] * size_y[i];
        }
    }

    long long added = max_points - n;
    cout << added << "\n";
    return 0;
}
"""
    },
    {
        "id": "abc127_e",
        "title": "Cell Distance",
        "contest_id": "abc127",
        "rating": 1938,
        "tag": "Combinatorics",
        "subtopic": "Linearity of Expectation",
        "topic": "Manhattan Pairwise Distance Contribution over Subsets via Dimension Decoupling",
        "cat_folder": "combinatorics",
        "cat_file": "manhattan_distance_subset_contribution.md",
        "statement": "In an N x M grid, choose K cells. Over all binom(NM, K) subsets, compute the sum of pairwise Manhattan distances between chosen cells. Output modulo 10^9 + 7.",
        "key_idea": "By Linearity of Expectation / Contribution to Sum, any fixed pair of cells (A, B) appears in exactly binom(NM - 2, K - 2) choices of K cells. Manhattan distance |r_1 - r_2| + |c_1 - c_2| decouples into row differences and column differences. For rows, each pair of rows (r_1, r_2) has M cells each, contributing |r_1 - r_2| * M^2. Symmetrically for columns, each pair contributes |c_1 - c_2| * N^2. Sum both and multiply by binom(NM - 2, K - 2).",
        "observation": "Independence of coordinate axes reduces the sum over all cell pairs to 1D arithmetic progressions in O(N + M).",
        "algorithm": [
            "Precompute factorials up to NM.",
            "Sum row distances: sum_{d=1}^{N-1} d * (N - d) * M^2.",
            "Sum col distances: sum_{d=1}^{M-1} d * (M - d) * N^2.",
            "ans = (total_dist * binom(NM - 2, K - 2)) % MOD.",
            "Print ans."
        ],
        "time_complexity": "O(N + M)",
        "space_complexity": "O(N * M)",
        "core_skill": "Linearity of expectation on subset selections with Cartesian dimension decoupling.",
        "reusable_pattern": "Pairwise Manhattan on Subsets: binom(NM-2, K-2) * [M^2 sum(d*(N-d)) + N^2 sum(d*(M-d))].",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>

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

long long modInverse(long long n) {
    return power(n, MOD - 2);
}

void precompute() {
    fact[0] = 1;
    invFact[0] = 1;
    for (int i = 1; i < MAX; i++) {
        fact[i] = (fact[i - 1] * i) % MOD;
    }
    invFact[MAX - 1] = modInverse(fact[MAX - 1]);
    for (int i = MAX - 2; i >= 1; i--) {
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

    long long n, m, k;
    if (!(cin >> n >> m >> k)) return 0;

    long long total_dist = 0;

    long long m2 = (m * m) % MOD;
    for (long long d = 1; d < n; ++d) {
        long long count = (n - d) * m2 % MOD;
        total_dist = (total_dist + d * count) % MOD;
    }

    long long n2 = (n * n) % MOD;
    for (long long d = 1; d < m; ++d) {
        long long count = (m - d) * n2 % MOD;
        total_dist = (total_dist + d * count) % MOD;
    }

    long long ways = nCr(n * m - 2, k - 2);
    long long ans = (total_dist * ways) % MOD;

    cout << ans << "\n";
    return 0;
}
"""
    },
    {
        "id": "arc151_c",
        "title": "01 Game",
        "contest_id": "arc151",
        "rating": 1940,
        "tag": "Game Theory",
        "subtopic": "Sprague-Grundy Theorem",
        "topic": "Interval Grundy Decomposition under Alternating Parity Boundary Constraints",
        "cat_folder": "game_theory",
        "cat_file": "interval_grundy_alternating_boundary.md",
        "statement": "N squares in a row. M squares initially have 0 or 1. Players alternate placing 0 or 1 into an empty square such that no adjacent squares share the same number. Last player to move wins. Determine winner.",
        "key_idea": "The board decomposes into independent intervals of empty cells. By Sprague-Grundy theorem, the total game is the XOR sum of segment Grundy values. For an open end of length L, G(L) = L. For an internal segment of length L between matching values (0...0 or 1...1), G(L) = 1 if L is odd, 0 if L is even (i.e. 1 for odd, 0 for even). Between opposite values (0...1 or 1...0), G(L) = 0 for all L! If M = 0, G = N mod 2.",
        "observation": "Opposite boundary values neutralize the entire interval (G = 0); matching values give parity 1; open ends give length L.",
        "algorithm": [
            "If M == 0: Takahashi wins iff N % 2 == 1.",
            "Sort clues by position.",
            "xor_sum = (pos[0] - 1) ^ (N - pos[M - 1]).",
            "For each adjacent clue pair: if val[i] == val[i + 1], xor_sum ^= 1.",
            "If xor_sum != 0, print Takahashi; else print Aoki."
        ],
        "time_complexity": "O(M log M)",
        "space_complexity": "O(M)",
        "core_skill": "Sprague-Grundy game decomposition with local boundary-constrained state transitions.",
        "reusable_pattern": "Boundary-Constrained Grundy: Open ends give G = L; identical boundaries give G = 1; opposite give G = 0.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Clue {
    long long pos;
    int val;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    int m;
    if (!(cin >> n >> m)) return 0;

    if (m == 0) {
        cout << (n % 2 == 1 ? "Takahashi" : "Aoki") << "\n";
        return 0;
    }

    vector<Clue> clues(m);
    for (int i = 0; i < m; ++i) {
        cin >> clues[i].pos >> clues[i].val;
    }

    sort(clues.begin(), clues.end(), [](const Clue& a, const Clue& b) {
        return a.pos < b.pos;
    });

    long long xor_sum = 0;

    xor_sum ^= (clues[0].pos - 1);

    for (int i = 0; i < m - 1; ++i) {
        if (clues[i].val == clues[i + 1].val) {
            xor_sum ^= 1;
        } else {
            xor_sum ^= 0;
        }
    }

    xor_sum ^= (n - clues[m - 1].pos);

    cout << (xor_sum != 0 ? "Takahashi" : "Aoki") << "\n";
    return 0;
}
"""
    },
    {
        "id": "abc258_g",
        "title": "Triangle",
        "contest_id": "abc258",
        "rating": 1944,
        "tag": "Data Structures (DS)",
        "subtopic": "Bitset Optimizations",
        "topic": "Bitset-Accelerated Triangle Counting via Neighbor Set Intersections O(N^3 / 64)",
        "cat_folder": "data_structures",
        "cat_file": "bitset_triangle_counting_n3_64.md",
        "statement": "Given an undirected simple graph with N vertices (N <= 3000) as an adjacency matrix. Count the number of triangles (i, j, k) with i < j < k.",
        "key_idea": "For each pair of adjacent vertices (i, j) with i < j, the number of common neighbors k > j is the size of the set intersection of neighbors of i and neighbors of j restricted to indices > j. Using std::bitset<3000>, storing only neighbors with index > i, the count is simply (adj[i] & adj[j]).count(). Running bitwise AND over 64-bit machine words reduces operations by a factor of 64 to N^3 / 64 ~ 4.2 * 10^8 ops, executing in ~0.3s.",
        "observation": "std::bitset bitwise AND + popcount achieves word-level parallelism for dense graph triangle enumeration.",
        "algorithm": [
            "Initialize adj[i] as bitset<3000> for each vertex i.",
            "Read adjacency matrix; if edge (i, j) exists and j > i, set bit j in adj[i].",
            "ans = 0.",
            "For each i from 0 to N - 1:",
            "  For each j > i where adj[i].test(j):",
            "    ans += (adj[i] & adj[j]).count().",
            "Print ans."
        ],
        "time_complexity": "O(N^3 / 64)",
        "space_complexity": "O(N^2 / 64)",
        "core_skill": "Bitset acceleration for word-level parallelism in cubic dense graph operations.",
        "reusable_pattern": "Bitset Triangle Count: For edge (i, j) with i < j, count += (adj[i] & adj[j]).count().",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <string>
#include <bitset>

using namespace std;

const int MAXN = 3000;
bitset<MAXN> adj[MAXN];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    for (int i = 0; i < n; ++i) {
        string s;
        cin >> s;
        for (int j = i + 1; j < n; ++j) {
            if (s[j] == '1') {
                adj[i].set(j);
            }
        }
    }

    long long count = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            if (adj[i].test(j)) {
                count += (adj[i] & adj[j]).count();
            }
        }
    }

    cout << count << "\n";
    return 0;
}
"""
    },
    {
        "id": "abc197_f",
        "title": "Construct a Palindrome",
        "contest_id": "abc197",
        "rating": 1945,
        "tag": "Graph Theory",
        "subtopic": "BFS / State Graphs",
        "topic": "Bidirectional Symmetric Pair BFS for Shortest Palindromic Graph Walk",
        "cat_folder": "graph_theory",
        "cat_file": "bidirectional_pair_bfs_palindromic_walk.md",
        "statement": "Given an undirected graph with N vertices and M edges labeled with lowercase English letters. Find the minimum length of a walk from 1 to N whose edge labels form a palindrome, or report -1.",
        "key_idea": "A palindrome is symmetric: start from both endpoints (1, N) simultaneously. Define BFS state as (u, v) where u starts at 1 and v starts at N. From state (u, v), step to (u', v') if u has edge u -> u' labeled c and v has edge v -> v' with the same label c, increasing step distance by 2. When u == v, walk length is 2 * dist. When u and v share an edge, walk length is 2 * dist + 1.",
        "observation": "State graph of pairs (u, v) has N^2 states. BFS finds the global minimum distance efficiently.",
        "algorithm": [
            "Build adjacency list with characters.",
            "Initialize dist[u][v] = INF for all 1 <= u, v <= N.",
            "Set dist[1][N] = 0 and push (1, N) to queue.",
            "Run BFS: pop (u, v). If u == v, ans = min(ans, 2 * d). If edge (u, v) exists, ans = min(ans, 2 * d + 1).",
            "Transition to (u', v') for matching edge characters c.",
            "Print ans if < INF, else -1."
        ],
        "time_complexity": "O(N^2 + M^2)",
        "space_complexity": "O(N^2)",
        "core_skill": "Bidirectional simultaneous search on pair states for palindromic graph walks.",
        "reusable_pattern": "Palindromic Walk BFS: Pair state (u, v) moves to (u', v') iff edge labels match.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <queue>
#include <string>

using namespace std;

const int INF = 1e9;

struct Edge {
    int to;
    char c;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<Edge>> adj(n + 1);
    vector<vector<int>> is_edge(n + 1, vector<int>(n + 1, 0));

    for (int i = 0; i < m; ++i) {
        int u, v;
        char c;
        cin >> u >> v >> c;
        adj[u].push_back({v, c});
        adj[v].push_back({u, c});
        is_edge[u][v] = 1;
        is_edge[v][u] = 1;
    }

    vector<vector<int>> dist(n + 1, vector<int>(n + 1, INF));
    queue<pair<int, int>> q;

    dist[1][n] = 0;
    q.push({1, n});

    int ans = INF;

    while (!q.empty()) {
        auto [u, v] = q.front();
        q.pop();

        int d = dist[u][v];

        if (u == v) {
            ans = min(ans, 2 * d);
        }
        if (is_edge[u][v]) {
            ans = min(ans, 2 * d + 1);
        }

        for (const auto& eu : adj[u]) {
            for (const auto& ev : adj[v]) {
                if (eu.c == ev.c) {
                    if (dist[eu.to][ev.to] > d + 1) {
                        dist[eu.to][ev.to] = d + 1;
                        q.push({eu.to, ev.to});
                    }
                }
            }
        }
    }

    if (ans >= INF) {
        cout << -1 << "\n";
    } else {
        cout << ans << "\n";
    }

    return 0;
}
"""
    },
    {
        "id": "abc193_e",
        "title": "Oversleeping",
        "contest_id": "abc193",
        "rating": 1948,
        "tag": "Number Theory",
        "subtopic": "Chinese Remainder Theorem",
        "topic": "Dual Periodic Cycle Synchronization via Chinese Remainder Theorem on Interval Windows",
        "cat_folder": "number_theory",
        "cat_file": "crt_dual_periodic_cycle_synchronization.md",
        "statement": "A train cycle has period M_1 = 2X + 2Y, visiting station at times t = t1 mod M_1 for t1 in [X, X + Y - 1]. Sleep cycle has period M_2 = P + Q, waking at t = t2 mod M_2 for t2 in [P, P + Q - 1]. Find the earliest time Takahashi can get off the train, or report infinity.",
        "key_idea": "For any pair of offsets t1 in [X, X + Y) and t2 in [P, P + Q), we have a system of two modular equations: t = t1 mod M_1 and t = t2 mod M_2. Since Y, Q <= 500, we can solve this using the Chinese Remainder Theorem (via Extended Euclidean Algorithm) across candidate pairs, finding the minimal non-negative solution.",
        "observation": "Small window widths Y, Q <= 500 allow directly checking pairwise CRT solutions in O(Y * Q * log(M)).",
        "algorithm": [
            "For each query, set M1 = 2X + 2Y and M2 = P + Q.",
            "Iterate t1 from X to X + Y - 1 and t2 from P to P + Q - 1.",
            "Solve CRT(t1, M1, t2, M2) using extgcd.",
            "If valid solution r >= 0 exists, update ans = min(ans, r).",
            "Output ans if found, else infinity."
        ],
        "time_complexity": "O(Y * Q * log(min(M1, M2)))",
        "space_complexity": "O(1)",
        "core_skill": "Synchronizing dual periodic events over interval windows using Chinese Remainder Theorem.",
        "reusable_pattern": "Periodic Cycle Sync: CRT(t1 mod M1, t2 mod M2) finds earliest alignment over window pairs.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <numeric>
#include <algorithm>

using namespace std;

long long extgcd(long long a, long long b, long long &x, long long &y) {
    if (b == 0) {
        x = 1;
        y = 0;
        return a;
    }
    long long x1, y1;
    long long d = extgcd(b, a % b, x1, y1);
    x = y1;
    y = x1 - y1 * (a / b);
    return d;
}

pair<long long, long long> crt(long long r1, long long m1, long long r2, long long m2) {
    long long p, q;
    long long d = extgcd(m1, m2, p, q);
    if ((r2 - r1) % d != 0) return {0, -1};
    long long m = m1 / d * m2;
    long long tmp = (r2 - r1) / d % (m2 / d) * p % (m2 / d);
    long long r = (r1 + m1 * tmp) % m;
    if (r < 0) r += m;
    return {r, m};
}

void solve() {
    long long X, Y, P, Q;
    cin >> X >> Y >> P >> Q;

    long long M1 = 2 * X + 2 * Y;
    long long M2 = P + Q;

    long long ans = -1;

    for (long long t1 = X; t1 < X + Y; ++t1) {
        for (long long t2 = P; t2 < P + Q; ++t2) {
            auto [r, m] = crt(t1, M1, t2, M2);
            if (m != -1) {
                if (ans == -1 || r < ans) {
                    ans = r;
                }
            }
        }
    }

    if (ans == -1) {
        cout << "infinity\n";
    } else {
        cout << ans << "\n";
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
    }
]

REJECTED_PROBLEMS = [
    {
        "id": "arc194_c",
        "title": "Cost to Flip",
        "rating": 1913,
        "tag": "Basics",
        "subtopic": "Bitwise Operations",
        "topic": "Bit-Flip Cost Optimization",
        "reason": "Rejected: Duplicate of abc150_e; redundant bitwise flip order and contribution casework."
    },
    {
        "id": "arc188_a",
        "title": "ABC Symmetry",
        "rating": 1914,
        "tag": "Basics",
        "subtopic": "Implementation",
        "topic": "String Ad-hoc Casework",
        "reason": "Rejected: Elementary logic building / ad-hoc string palindrome casework without generalizable CP algorithm."
    },
    {
        "id": "abc475_f",
        "title": "Rectangle Filling",
        "rating": 1916,
        "tag": "Basics",
        "subtopic": "Implementation",
        "topic": "Grid Simulation",
        "reason": "Rejected: Elementary logic building / 2D grid filling simulation drill."
    },
    {
        "id": "arc204_a",
        "title": "Use Udon Coupon",
        "rating": 1923,
        "tag": "Basics",
        "subtopic": "Implementation",
        "topic": "Coupon Greedy Casework",
        "reason": "Rejected: Elementary logic building / ad-hoc greedy coupon casework drill."
    },
    {
        "id": "arc008_3",
        "title": "THE☆たこ焼き祭り2012",
        "rating": 1927,
        "tag": "Graph Theory",
        "subtopic": "Shortest Paths",
        "topic": "Euclidean Dense Dijkstra",
        "reason": "Rejected: Duplicate of arc064_c; dense Dijkstra on complete Euclidean graph with arrival sorting."
    },
    {
        "id": "abc457_g",
        "title": "Catch All Apples",
        "rating": 1928,
        "tag": "Basics",
        "subtopic": "Implementation",
        "topic": "Coordinate Sweep Drill",
        "reason": "Rejected: Elementary logic building / coordinate collection simulation drill."
    },
    {
        "id": "arc206_d",
        "title": "LIS ∩ LDS",
        "rating": 1930,
        "tag": "Basics",
        "subtopic": "Constructive",
        "topic": "LIS / LDS Extremal Construction",
        "reason": "Rejected: Duplicate of arc091_c; constructive permutation under simultaneous LIS and LDS constraints."
    },
    {
        "id": "arc216_b",
        "title": "Range Mex Sum",
        "rating": 1935,
        "tag": "Data Structures (DS)",
        "subtopic": "Segment Tree / Mex Queries",
        "topic": "Range Mex Query",
        "reason": "Rejected: Duplicate of typical90_ah / range mex data structure archetypes."
    },
    {
        "id": "abc479_f",
        "title": "Narrow Passage",
        "rating": 1938,
        "tag": "Basics",
        "subtopic": "Implementation",
        "topic": "Narrow Passage Simulation",
        "reason": "Rejected: Elementary logic building / passage traversal simulation casework."
    },
    {
        "id": "abc461_f",
        "title": "Total Product is N",
        "rating": 1940,
        "tag": "Number Theory",
        "subtopic": "Divisors / Factorization",
        "topic": "Divisor Multiplicative Partition",
        "reason": "Rejected: Duplicate of typical90_ad / divisor factorization DP archetypes."
    },
    {
        "id": "arc222_c",
        "title": "2 Directions vs 4 Directions",
        "rating": 1945,
        "tag": "Basics",
        "subtopic": "Implementation",
        "topic": "Directional Movement Casework",
        "reason": "Rejected: Elementary logic building / directional grid move casework drill."
    }
]

# Step 1: Compile all C++ solutions to verify zero errors
print(f"Testing C++ compilation of all {len(SELECTED_PROBLEMS)} selected ABC Part 4A solutions...")
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

print(f"[+] All {len(SELECTED_PROBLEMS)} ABC Part 4A C++ solutions compiled with 0 errors!")

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
        f.write("\n### Batch 5 Part 4A: ABC Curated Ladder (1900 - 1950)\n" + "\n".join(new_q_lines) + "\n")
    print("[+] Updated QUALITY_PROBLEMS_BY_TOPIC.md with new archetypes.")

# Update state/progress.json
with open("state/progress.json", "r", encoding="utf-8") as f:
    progress = json.load(f)

progress["current_batch"] = "Batch 5 Part 4A: ABC Ladder (1900-1950) COMPLETED"
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
print("Batch 5 Part 4A completed successfully!")
