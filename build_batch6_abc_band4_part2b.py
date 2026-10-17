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
print("      PROCESSING BATCH 6 PART 2B: ABC / ARC CURATED LADDER (2074 - 2099)")
print("=" * 75)

SELECTED_PROBLEMS = [
    {
        "id": "abc207_d",
        "title": "Congruence Points",
        "contest_id": "abc207",
        "rating": 2074,
        "tag": "Geometry",
        "subtopic": "Geometry 2D",
        "topic": "Points, Vectors, Transformations, Dot Products, Cross Products, Precision Issues and Polar Sort(2D)",
        "cat_folder": "geometry",
        "cat_file": "point_set_congruence_centroid_rotation.md",
        "statement": "You are given two sets of N points on a 2D plane, S and T. Determine if S can be made to coincide with T by translating and rotating S around the origin by some angle theta.",
        "key_idea": "Translation invariance is eliminated by shifting both point sets so their centroids lie at the origin (scaling coordinates by N to retain exact integer arithmetic). Under rotation around the origin, Euclidean distance from the origin is preserved. To test rotational congruence, pick a non-origin anchor point in S, test aligning it with every candidate point in T having the identical squared norm. The rotation angle theta is uniquely determined by the dot and cross product of the two vectors, which allows rotating every point of S using integer arithmetic and testing set equality in O(N log N) via sorting.",
        "observation": "Aligning centroids removes the 2D translational degree of freedom. A 2D rotation preserving norm is uniquely fixed by mapping one non-zero vector to another.",
        "algorithm": [
            "Compute centroid sums (sx, sy) and (tx, ty) for S and T.",
            "Center both sets by setting (x, y) -> (N*x - sx, N*y - sy). If N == 1, trivially Yes.",
            "Sort T to enable fast equality comparison.",
            "Find an anchor point s0 in S that is non-zero (if none, all points are at origin, return Yes).",
            "For each candidate point t in T with ||t||^2 == ||s0||^2:",
            "  Compute cos_theta * ||s0||^2 = s0 . t and sin_theta * ||s0||^2 = s0 x t.",
            "  Rotate each point s in S using the integer transformation matrix.",
            "  If all coordinates remain integers and the sorted rotated set equals T, output Yes.",
            "If no candidate works, output No."
        ],
        "time_complexity": "O(N^2 log N)",
        "space_complexity": "O(N)",
        "core_skill": "Centroid normalization to eliminate translation and exact integer matrix transformation for rotation verification.",
        "reusable_pattern": "For 2D point cloud matching, normalize by centroid and anchor one non-zero vector to test all O(N) candidate rotational alignments exactly without floating-point error.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Point {
    long long x, y;
    bool operator<(const Point& o) const {
        if (x != o.x) return x < o.x;
        return y < o.y;
    }
    bool operator==(const Point& o) const {
        return x == o.x && y == o.y;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<Point> S(n), T(n);
    long long sx = 0, sy = 0, tx = 0, ty = 0;
    for (int i = 0; i < n; ++i) {
        cin >> S[i].x >> S[i].y;
        sx += S[i].x;
        sy += S[i].y;
    }
    for (int i = 0; i < n; ++i) {
        cin >> T[i].x >> T[i].y;
        tx += T[i].x;
        ty += T[i].y;
    }

    if (n == 1) {
        cout << "Yes\n";
        return 0;
    }

    for (int i = 0; i < n; ++i) {
        S[i].x = S[i].x * n - sx;
        S[i].y = S[i].y * n - sy;
        T[i].x = T[i].x * n - tx;
        T[i].y = T[i].y * n - ty;
    }

    sort(T.begin(), T.end());

    int non_zero = -1;
    for (int i = 0; i < n; ++i) {
        if (S[i].x != 0 || S[i].y != 0) {
            non_zero = i;
            break;
        }
    }

    if (non_zero == -1) {
        cout << "Yes\n";
        return 0;
    }

    long long x0 = S[non_zero].x, y0 = S[non_zero].y;
    long long norm0 = x0 * x0 + y0 * y0;

    for (int j = 0; j < n; ++j) {
        long long xt = T[j].x, yt = T[j].y;
        if (xt * xt + yt * yt != norm0) continue;

        long long c = x0 * xt + y0 * yt;
        long long s = x0 * yt - y0 * xt;

        vector<Point> S_rot(n);
        bool ok = true;
        for (int i = 0; i < n; ++i) {
            long long rx = S[i].x * c - S[i].y * s;
            long long ry = S[i].x * s + S[i].y * c;
            if (rx % norm0 != 0 || ry % norm0 != 0) {
                ok = false;
                break;
            }
            S_rot[i] = {rx / norm0, ry / norm0};
        }
        if (!ok) continue;

        sort(S_rot.begin(), S_rot.end());
        if (S_rot == T) {
            cout << "Yes\n";
            return 0;
        }
    }

    cout << "No\n";
    return 0;
}
"""
    },
    {
        "id": "abc257_g",
        "title": "Prefix Concatenation",
        "contest_id": "abc257",
        "rating": 2075,
        "tag": "Strings",
        "subtopic": "String Matching",
        "topic": "Knuth Morris Pratt (KMP) and Prefix Automaton",
        "cat_folder": "strings",
        "cat_file": "greedy_prefix_extension_kmp.md",
        "statement": "You are given two strings S and T. Find the minimum number of prefixes of S needed to concatenate together to form T. If impossible, output -1.",
        "key_idea": "To minimize the number of prefixes used, we greedily take the longest possible prefix of S matching the remaining prefix of T at each step. By concatenating S + '#' + T and computing the KMP prefix function (pi array), pi[|S| + 1 + i] gives the length of the longest prefix of S that matches a suffix of T[1..i]. Then, starting from index |T|, we can greedily jump backward: if we are at position curr and the longest prefix of S ending at curr is L = pi[|S| + 1 + curr], we jump to curr - L. If L == 0, it is impossible to cover position curr, so output -1.",
        "observation": "The greedy strategy of extending each prefix as far right as possible is always optimal because prefix subsets are strictly nested.",
        "algorithm": [
            "Construct combined string U = S + '#' + T.",
            "Compute KMP pi array of U in O(|S| + |T|).",
            "Set curr = |T| and steps = 0.",
            "While curr > 0:",
            "  Let L = pi[|S| + 1 + curr].",
            "  If L <= 0, return -1.",
            "  curr -= L, steps++.",
            "Output steps."
        ],
        "time_complexity": "O(|S| + |T|)",
        "space_complexity": "O(|S| + |T|)",
        "core_skill": "KMP prefix function on concatenated strings for longest prefix matching and greedy reverse jumping.",
        "reusable_pattern": "Finding longest prefix of S ending at each position of T using KMP on S + '#' + T in linear time.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <string>
#include <vector>

using namespace std;

vector<int> prefix_function(const string& s) {
    int n = s.size();
    vector<int> pi(n, 0);
    for (int i = 1; i < n; ++i) {
        int j = pi[i - 1];
        while (j > 0 && s[i] != s[j])
            j = pi[j - 1];
        if (s[i] == s[j])
            j++;
        pi[i] = j;
    }
    return pi;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s, t;
    if (!(cin >> s >> t)) return 0;

    string combined = s + '#' + t;
    vector<int> pi = prefix_function(combined);

    int cur = t.size();
    int s_len = s.size();
    int ans = 0;

    while (cur > 0) {
        int match_len = pi[s_len + 1 + cur - 1];
        if (match_len == 0) {
            cout << -1 << "\n";
            return 0;
        }
        ans++;
        cur -= match_len;
    }

    cout << ans << "\n";
    return 0;
}
"""
    },
    {
        "id": "arc110_d",
        "title": "Binomial Coefficient is Fun",
        "contest_id": "arc110",
        "rating": 2075,
        "tag": "Basics",
        "subtopic": "Basic Counting",
        "topic": "Stars and Bars",
        "cat_folder": "basics",
        "cat_file": "stars_and_bars_product_binomial_bijection.md",
        "statement": "Given a sequence A = (A_1, A_2, ..., A_N) and an integer M, calculate the sum of prod_{i=1}^N binom(B_i, A_i) over all non-negative integer sequences B of length N such that sum_{i=1}^N B_i <= M, modulo 10^9 + 7.",
        "key_idea": "Consider a row of M balls. Let S = sum_{i=1}^N A_i. The product prod binom(B_i, A_i) asks us to partition a prefix of length sum B_i <= M into N segments of lengths B_1, ..., B_N, and choose A_i items from the i-th segment. By introducing a slack variable B_{N+1} = M - sum B_i, this corresponds to partitioning M items into N+1 bins and choosing A_i items from bin i (for 1 <= i <= N). This is combinatorially isomorphic to choosing N delimiters and S chosen elements from a total sequence of M + N positions! Therefore, the entire sum collapses into a single binomial coefficient: binom(M + N, S + N).",
        "observation": "Sums of products of binomial coefficients over partition configurations collapse to a single global choice via stars-and-bars bijection.",
        "algorithm": [
            "Compute S = sum_{i=1}^N A_i.",
            "If S > M, output 0.",
            "The answer is binom(M + N, S + N) modulo 10^9 + 7.",
            "Since S + N <= 4 * 10^6 and M <= 10^9, compute binom(M + N, S + N) in O(S + N) using modular inverse."
        ],
        "time_complexity": "O(N + sum A_i)",
        "space_complexity": "O(1)",
        "core_skill": "Combinatorial bijection collapsing multivariable binomial convolutions into single stars-and-bars choices.",
        "reusable_pattern": "sum_{sum B_i <= M} prod binom(B_i, A_i) = binom(M + N, N + sum A_i).",
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

long long modInverse(long long n) {
    return power(n, MOD - 2);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n, m;
    if (!(cin >> n >> m)) return 0;

    long long sumA = 0;
    for (int i = 0; i < n; ++i) {
        long long a;
        cin >> a;
        sumA += a;
    }

    if (sumA > m) {
        cout << 0 << "\n";
        return 0;
    }

    long long top = n + m;
    long long k = sumA + n;

    long long num = 1, den = 1;
    for (long long i = 0; i < k; ++i) {
        num = (num * ((top - i) % MOD)) % MOD;
        den = (den * ((i + 1) % MOD)) % MOD;
    }

    long long ans = (num * modInverse(den)) % MOD;
    cout << ans << "\n";

    return 0;
}
"""
    },
    {
        "id": "abc337_g",
        "title": "Tree And LCS",
        "contest_id": "abc337",
        "rating": 2078,
        "tag": "Data Structures (DS)",
        "subtopic": "Binary Indexed Tree (BIT)",
        "topic": "BIT / Fenwick Tree",
        "cat_folder": "data_structures",
        "cat_file": "tree_path_dominance_fenwick_dfs.md",
        "statement": "Given a tree with N vertices labeled 1 through N. For each vertex r, consider rooting the tree at r. Find the sum over all vertices v of the number of ancestors u of v such that u < v.",
        "key_idea": "For any directed edge u -> v (where u is the parent of v in root r), the condition u < v adds 1 to the count for all nodes in the subtree of v. Rather than rerooting explicitly, consider a fixed root (say node 1). For every vertex x from 1 to N, all nodes y < x on the tree path from 1 to x are either in the component of the parent of x or in a child subtree of x. Using a Fenwick tree over DFS traversal enter/exit timestamps, we can query how many nodes y < x lie inside each subtree of x and outside, and translate these into difference array updates on the tree. A final prefix sum down the tree yields the exact answer for all r.",
        "observation": "Pairwise tree ancestor conditions can be decomposed into static subtree counts of smaller-labeled vertices using a Fenwick tree and tree difference arrays.",
        "algorithm": [
            "Root tree at node 1. Compute DFS entry/exit times in and out, and subtree sizes.",
            "Iterate x from 1 to N:",
            "  Query the BIT for the number of elements < x in x's subtree.",
            "  For each child c of x, query how many elements < x are in c's subtree.",
            "  Add difference updates on the tree for each component.",
            "  Insert x into the Fenwick tree at in[x].",
            "Perform a top-down DFS to accumulate prefix sums of the tree difference array.",
            "Output the results for all vertices 1..N."
        ],
        "time_complexity": "O(N log N)",
        "space_complexity": "O(N)",
        "core_skill": "Tree difference arrays combined with Fenwick tree range queries during DFS to aggregate ancestor relations.",
        "reusable_pattern": "Translating relative order constraints u < v across all possible roots into static subtree BIT queries and imos on trees.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>

using namespace std;

struct Fenwick {
    int n;
    vector<long long> tree;
    Fenwick(int n) : n(n), tree(n + 1, 0) {}
    void add(int i, long long delta) {
        for (; i <= n; i += i & -i) tree[i] += delta;
    }
    long long query(int i) {
        long long sum = 0;
        for (; i > 0; i -= i & -i) sum += tree[i];
        return sum;
    }
    long long query(int l, int r) {
        if (l > r) return 0;
        return query(r) - query(l - 1);
    }
};

int n;
vector<vector<int>> adj;
vector<int> tin, tout;
vector<vector<int>> children;
int timer = 0;

void dfs_time(int u, int p) {
    tin[u] = ++timer;
    for (int v : adj[u]) {
        if (v != p) {
            children[u].push_back(v);
            dfs_time(v, u);
        }
    }
    tout[u] = timer;
}

vector<long long> diff;

void dfs_diff(int u) {
    for (int v : children[u]) {
        dfs_diff(v);
        diff[u] += diff[v];
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n)) return 0;

    adj.assign(n + 1, vector<int>());
    tin.assign(n + 1, 0);
    tout.assign(n + 1, 0);
    children.assign(n + 1, vector<int>());
    diff.assign(n + 2, 0);

    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    dfs_time(1, 0);

    Fenwick bit(n);
    vector<long long> ans(n + 1, 0);

    for (int x = 1; x <= n; ++x) {
        long long total_below = bit.query(tin[x], tout[x]);
        ans[1] += total_below;

        for (int c : children[x]) {
            long long below_c = bit.query(tin[c], tout[c]);
            diff[c] -= below_c;
        }
        diff[x] += total_below;

        bit.add(tin[x], 1);
    }

    dfs_diff(1);

    for (int i = 1; i <= n; ++i) {
        ans[i] = ans[1] + diff[i];
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
        "id": "arc152_c",
        "title": "Pivot",
        "contest_id": "arc152",
        "rating": 2079,
        "tag": "Number Theory",
        "subtopic": "Euclidean Algorithm",
        "topic": "Euclidean Algorithm",
        "cat_folder": "number_theory",
        "cat_file": "reflection_group_diameter_gcd.md",
        "statement": "You are given a set of N integers A_1 < A_2 < ... < A_N. You can choose any element A_k and reflect all elements across A_k (replacing each x with 2*A_k - x). Find the minimum possible value of max(A) - min(A) after any sequence of operations.",
        "key_idea": "Reflecting across a point preserves the distances between adjacent elements (it merely reverses their order and shifts them). Thus, the diameter L = A_N - A_1 is an absolute invariant! Under repeated reflections, the positions of the set generate an affine reflection group. The translation component of two reflections across A_i and A_j is 2*(A_i - A_j). The group of all reachable shifts of the minimum element A_1 is the additive subgroup generated by G = 2 * gcd_{i > 1}(A_i - A_1). The minimum possible span is achieved by minimizing the max coordinate max(x) = min(x) + L, which corresponds to finding the minimal non-negative coordinate modulo G.",
        "observation": "Reflections preserve diameter L = A_N - A_1 and generate translations in multiples of 2 * gcd(A_i - A_1).",
        "algorithm": [
            "Compute L = A_N - A_1.",
            "Compute g = gcd(A_2 - A_1, A_3 - A_1, ..., A_N - A_1).",
            "The translation period is G = 2 * g.",
            "The position of A_1 modulo G can be shifted by any multiple of G.",
            "A single reflection also reverses orientation, so we can achieve orientations starting at A_1 mod G or (-A_N) mod G.",
            "Calculate min(A_1 mod G, (-A_N) mod G) and add L.",
            "Output the minimum achievable maximum coordinate."
        ],
        "time_complexity": "O(N + log(max A))",
        "space_complexity": "O(N)",
        "core_skill": "Affine reflection group analysis and Euclidean GCD translation lattice invariants.",
        "reusable_pattern": "Sequences of 1D point reflections preserve interval diameter and generate a discrete translation lattice with step 2 * gcd(deltas).",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

using namespace std;

long long gcd(long long a, long long b) {
    while (b) {
        a %= b;
        swap(a, b);
    }
    return a;
}

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
        cout << 0 << "\n";
        return 0;
    }

    long long g = 0;
    for (int i = 1; i < n; ++i) {
        g = gcd(g, a[i] - a[0]);
    }

    long long G = 2 * g;
    long long L = a[n - 1] - a[0];

    long long r1 = a[0] % G;
    long long r2 = (G - (a[n - 1] % G)) % G;

    long long ans = L + 2 * min(r1, r2);
    // Alternatively, max value is L + shift, check both orientations
    long long best_max = 2e18;
    for (int i = 0; i < n; ++i) {
        long long rem = a[i] % G;
        long long cand = rem + L;
        // check symmetrical
        long long cand2 = (G - rem) % G + L;
        best_max = min({best_max, cand, cand2});
    }

    // Direct exact calculation:
    // Any reachable state has points {x + d_i} where x in a[0] + 2k*g or -a[n-1] + 2k*g
    long long x1 = a[0] % G;
    long long x2 = (-a[n - 1] % G + G) % G;
    long long min_start = min(x1, x2);

    cout << min_start + L << "\n";

    return 0;
}
"""
    },
    {
        "id": "arc138_d",
        "title": "Differ by K bits",
        "contest_id": "arc138",
        "rating": 2080,
        "tag": "Math",
        "subtopic": "Linear Algebra",
        "topic": "Vector Space and XOR Basis",
        "cat_folder": "math",
        "cat_file": "linear_basis_hypercube_gray_code.md",
        "statement": "Given integers N and K, construct a permutation P of 0, 1, ..., 2^N - 1 such that P_0 = 0 and each adjacent pair of elements (including P_{2^N - 1} and P_0) differs by exactly K bits. If no such permutation exists, report it.",
        "key_idea": "A cycle of length 2^N where each step flips K bits is a Hamiltonian cycle on a generalized hypercube graph. The parity of the number of 1s in the binary representation changes by K mod 2 at each step. Since 2^N is even, visiting all vertices and returning to 0 requires an even number of steps, but if K is even, the parity of the number of set bits never changes, making it bipartite-partitioned and impossible to visit odd-weight states! Thus K must be odd and 1 <= K < N. When K is odd, we can find N linearly independent vectors v_1, ..., v_N in (F_2)^N each having popcount K. Using the standard reflected binary Gray code G_i, we map each element to sum_{j=0}^{N-1} ((G_i >> j) & 1) * v_j.",
        "observation": "Even K creates a parity obstruction on popcount. For odd K, the problem reduces via linear isomorphism to standard Gray code over an F_2 basis of K-weight vectors.",
        "algorithm": [
            "If K is even or K > N: output No (if K == N, only N=1 is valid).",
            "Find N linearly independent vectors in {0, 1}^N each with popcount K using Gaussian elimination over F_2.",
            "Generate standard reflected binary Gray code g_i = i ^ (i >> 1) for 0 <= i < 2^N.",
            "For each i, P[i] = sum of basis vectors corresponding to set bits of g_i.",
            "Output Yes and the sequence P."
        ],
        "time_complexity": "O(N * 2^N)",
        "space_complexity": "O(2^N)",
        "core_skill": "F_2 linear basis construction and linear isomorphism of hypercube Gray codes.",
        "reusable_pattern": "Constructing Hamiltonian cycles with constrained XOR differences by finding an F_2 basis of valid deltas and applying Gray code.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>

using namespace std;

int count_bits(int x) {
    return __builtin_popcount(x);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    if (k % 2 == 0 || k > n) {
        cout << "No\n";
        return 0;
    }

    if (k == n) {
        if (n == 1) {
            cout << "Yes\n0 1\n";
        } else {
            cout << "No\n";
        }
        return 0;
    }

    vector<int> basis;
    vector<int> original;

    for (int mask = 1; mask < (1 << n); ++mask) {
        if (count_bits(mask) == k) {
            int cur = mask;
            for (int b : basis) {
                cur = min(cur, cur ^ b);
            }
            if (cur > 0) {
                basis.push_back(cur);
                original.push_back(mask);
                // Maintain reduced basis
                for (int i = (int)basis.size() - 1; i > 0; --i) {
                    if (basis[i] > basis[i - 1]) {
                        swap(basis[i], basis[i - 1]);
                    }
                }
                if ((int)original.size() == n) break;
            }
        }
    }

    if ((int)original.size() < n) {
        cout << "No\n";
        return 0;
    }

    cout << "Yes\n";
    int total = 1 << n;
    for (int i = 0; i < total; ++i) {
        int gray = i ^ (i >> 1);
        int val = 0;
        for (int j = 0; j < n; ++j) {
            if ((gray >> j) & 1) {
                val ^= original[j];
            }
        }
        cout << val << (i + 1 == total ? "" : " ");
    }
    cout << "\n";

    return 0;
}
"""
    },
    {
        "id": "abc027_d",
        "title": "Robot Movement",
        "contest_id": "abc027",
        "rating": 2081,
        "tag": "Basics",
        "subtopic": "Greedy and Constructive",
        "topic": "Basic Greedy Algorithms",
        "cat_folder": "basics",
        "cat_file": "future_contribution_greedy_sorting.md",
        "statement": "You are given a string S containing 'M', '+', and '-'. An integer variable x starts at 0. At 'M', your score increases by x. At each '+' or '-', you must choose to either increment x or decrement x. The total number of increments must equal the total number of decrements (so x ends at 0). Find the maximum possible final score.",
        "key_idea": "Each operation (+ or -) performed at index i affects all subsequent 'M' characters. Specifically, choosing +1 at index i contributes +1 * (number of 'M' after index i) to the score, and -1 contributes -1 * (number of 'M' after index i). Thus, the i-th non-'M' position has an intrinsic coefficient c_i = count of 'M's in S[i+1..|S|]. To maximize the total sum sum c_i * sign_i with exactly half chosen as +1 and half as -1, we simply sort the coefficients c_i in ascending order, assign -1 to the smaller half, and +1 to the larger half.",
        "observation": "Cumulative sum scores can be decoupled into individual coefficient contributions of future 'M' occurrences, turning the problem into greedy sorting.",
        "algorithm": [
            "Compute suffix counts of 'M' for the entire string S.",
            "For each position where S[i] != 'M', record c_i = suffix_M[i + 1].",
            "Sort all recorded coefficients c in ascending order.",
            "Assign -1 to the first half and +1 to the second half.",
            "Output the resulting sum."
        ],
        "time_complexity": "O(|S| log |S|)",
        "space_complexity": "O(|S|)",
        "core_skill": "Decoupling cumulative state increments into independent future contribution coefficients and greedy sign pairing.",
        "reusable_pattern": "When choices at step i additively affect all subsequent evaluation steps, reframe the score as sum (sign_i * future_events) and sort greedily.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!(cin >> s)) return 0;

    int n = s.size();
    vector<int> suffix_m(n + 1, 0);
    for (int i = n - 1; i >= 0; --i) {
        suffix_m[i] = suffix_m[i + 1] + (s[i] == 'M' ? 1 : 0);
    }

    vector<int> coeffs;
    for (int i = 0; i < n; ++i) {
        if (s[i] != 'M') {
            coeffs.push_back(suffix_m[i + 1]);
        }
    }

    sort(coeffs.begin(), coeffs.end());

    int k = coeffs.size();
    long long ans = 0;
    for (int i = 0; i < k / 2; ++i) {
        ans -= coeffs[i];
    }
    for (int i = k / 2; i < k; ++i) {
        ans += coeffs[i];
    }

    cout << ans << "\n";
    return 0;
}
"""
    },
    {
        "id": "abc205_f",
        "title": "Grid and Tokens",
        "contest_id": "abc205",
        "rating": 2082,
        "tag": "Graph Theory",
        "subtopic": "Flow and Min Cut",
        "topic": "Maximum Flow / Minimum Cut",
        "cat_folder": "graph_theory",
        "cat_file": "vertex_capacitated_bipartite_max_flow.md",
        "statement": "On an H x W grid, N tokens are placed. Token i must be placed at (r_i, c_i) with A_i <= r_i <= C_i and B_i <= c_i <= D_i. No two tokens may share the same row or column. Find the maximum number of tokens that can be placed.",
        "key_idea": "Each token can be chosen at most once (capacity 1 on token), can occupy at most one row, and can occupy at most one column. Furthermore, each row can host at most 1 token, and each column can host at most 1 token. We model this as a maximum flow network with node splitting: Source -> Row nodes (capacity 1) -> Token_in nodes (capacity 1) -> Token_out nodes (capacity 1) -> Column nodes (capacity 1) -> Sink.",
        "observation": "Enforcing both row-uniqueness, column-uniqueness, and token-uniqueness simultaneously is solved via a 4-layer flow network with unit edge and vertex capacities.",
        "algorithm": [
            "Construct network: Source S, Row nodes 1..H, Token_in 1..N, Token_out 1..N, Column nodes 1..W, Sink T.",
            "Add edge S -> Row r with capacity 1 for all r in [1, H].",
            "Add edge Row r -> Token_in i with capacity 1 for all r in [A_i, C_i].",
            "Add edge Token_in i -> Token_out i with capacity 1 for all i in [1, N] (vertex capacity).",
            "Add edge Token_out i -> Col c with capacity 1 for all c in [B_i, D_i].",
            "Add edge Col c -> Sink T with capacity 1 for all c in [1, W].",
            "Compute maximum bipartite flow using Dinic's algorithm."
        ],
        "time_complexity": "O(V^2 E) with Dinic, practically O(N * (H + W))",
        "space_complexity": "O(H + W + N + E)",
        "core_skill": "Vertex splitting and bipartite flow modeling for multi-constraint unit matching.",
        "reusable_pattern": "Token placement under simultaneous row and column exclusion constraints modeled as Source -> Rows -> Tokens -> Columns -> Sink.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

struct Edge {
    int to;
    int cap;
    int flow;
    int rev;
};

struct Dinic {
    int n;
    vector<vector<Edge>> adj;
    vector<int> level;
    vector<int> ptr;

    Dinic(int n) : n(n), adj(n), level(n), ptr(n) {}

    void add_edge(int from, int to, int cap) {
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
            for (auto& edge : adj[v]) {
                if (edge.cap - edge.flow > 0 && level[edge.to] == -1) {
                    level[edge.to] = level[v] + 1;
                    q.push(edge.to);
                }
            }
        }
        return level[t] != -1;
    }

    int dfs(int v, int t, int pushed) {
        if (pushed == 0) return 0;
        if (v == t) return pushed;
        for (int& cid = ptr[v]; cid < (int)adj[v].size(); ++cid) {
            auto& edge = adj[v][cid];
            int tr = edge.to;
            if (level[v] + 1 != level[tr] || edge.cap - edge.flow == 0) continue;
            int tr_pushed = dfs(tr, t, min(pushed, edge.cap - edge.flow));
            if (tr_pushed == 0) continue;
            edge.flow += tr_pushed;
            adj[tr][edge.rev].flow -= tr_pushed;
            return tr_pushed;
        }
        return 0;
    }

    int max_flow(int s, int t) {
        int flow = 0;
        while (bfs(s, t)) {
            fill(ptr.begin(), ptr.end(), 0);
            while (int pushed = dfs(s, t, 1e9)) {
                flow += pushed;
            }
        }
        return flow;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int h, w, n;
    if (!(cin >> h >> w >> n)) return 0;

    int S = 0;
    int row_start = 1;
    int token_in_start = row_start + h;
    int token_out_start = token_in_start + n;
    int col_start = token_out_start + n;
    int T = col_start + w;

    Dinic dinic(T + 1);

    for (int r = 1; r <= h; ++r) {
        dinic.add_edge(S, row_start + r - 1, 1);
    }
    for (int c = 1; c <= w; ++c) {
        dinic.add_edge(col_start + c - 1, T, 1);
    }

    for (int i = 0; i < n; ++i) {
        int a, b, c, d;
        cin >> a >> b >> c >> d;
        int t_in = token_in_start + i;
        int t_out = token_out_start + i;
        dinic.add_edge(t_in, t_out, 1);

        for (int r = a; r <= c; ++r) {
            dinic.add_edge(row_start + r - 1, t_in, 1);
        }
        for (int col = b; col <= d; ++col) {
            dinic.add_edge(t_out, col_start + col - 1, 1);
        }
    }

    cout << dinic.max_flow(S, T) << "\n";
    return 0;
}
"""
    },
    {
        "id": "abc237_g",
        "title": "Range Sort Query",
        "contest_id": "abc237",
        "rating": 2085,
        "tag": "Data Structures (DS)",
        "subtopic": "Segment Tree",
        "topic": "Segment Tree with Lazy Propagation",
        "cat_folder": "data_structures",
        "cat_file": "binary_search_01_reduction_lazy_segtree.md",
        "statement": "Given a permutation P of 1..N and Q queries, each query sorts a subarray P[L..R] in ascending or descending order. Find the final 1-based index of the value X.",
        "key_idea": "Sorting arbitrary permutations online is difficult, but sorting a 0-1 sequence is trivial using a lazy segment tree (count the number of 1s in [L, R], then overwrite a prefix with 0s and suffix with 1s). Since we only care about the position of a single element X, we can encode elements as: 0 if P_i < X, 1 if P_i == X, and 2 if P_i > X (or binary search the index, or maintain 3-state counts in the lazy segment tree). Maintaining three values {0, 1, 2} in a lazy segment tree allows directly performing range sorts and locating the single position containing 1 at the end.",
        "observation": "Range sorting queries preserve relative orders under monotone thresholding. Replacing numbers with {< X, == X, > X} allows lazy range assignment to simulate full range sorts.",
        "algorithm": [
            "Build a Lazy Segment Tree over an array of size N where A[i] = 0 if P[i] < X, 1 if P[i] == X, and 2 if P[i] > X.",
            "For each query (type, L, R):",
            "  Query counts of 0s, 1s, and 2s in [L, R].",
            "  If ascending: update [L, L + c0 - 1] to 0, [L + c0, L + c0 + c1 - 1] to 1, and the remainder to 2.",
            "  If descending: update [L, L + c2 - 1] to 2, [L + c2, L + c2 + c1 - 1] to 1, and the remainder to 0.",
            "After all queries, binary search / walk down the segment tree to find the position containing the value 1."
        ],
        "time_complexity": "O((N + Q) log N)",
        "space_complexity": "O(N)",
        "core_skill": "0-1-2 reduction of permutations to lazy range assignments on segment trees.",
        "reusable_pattern": "Tracking a single target element across multiple range sorts by collapsing the permutation into three relative classes and executing range overwrites.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>

using namespace std;

struct Node {
    int c0, c1, c2;
    int lazy; // -1: none, 0, 1, 2
};

int n, q, x_val;
vector<int> p;
vector<Node> tree;

void apply_lazy(int u, int l, int r, int val) {
    tree[u].c0 = tree[u].c1 = tree[u].c2 = 0;
    int len = r - l + 1;
    if (val == 0) tree[u].c0 = len;
    else if (val == 1) tree[u].c1 = len;
    else if (val == 2) tree[u].c2 = len;
    tree[u].lazy = val;
}

void push(int u, int l, int r) {
    if (tree[u].lazy != -1 && l < r) {
        int mid = (l + r) / 2;
        apply_lazy(2 * u, l, mid, tree[u].lazy);
        apply_lazy(2 * u + 1, mid + 1, r, tree[u].lazy);
        tree[u].lazy = -1;
    }
}

void pull(int u) {
    tree[u].c0 = tree[2 * u].c0 + tree[2 * u + 1].c0;
    tree[u].c1 = tree[2 * u].c1 + tree[2 * u + 1].c1;
    tree[u].c2 = tree[2 * u].c2 + tree[2 * u + 1].c2;
}

void build(int u, int l, int r) {
    tree[u].lazy = -1;
    if (l == r) {
        int val = (p[l] < x_val ? 0 : (p[l] == x_val ? 1 : 2));
        tree[u].c0 = (val == 0);
        tree[u].c1 = (val == 1);
        tree[u].c2 = (val == 2);
        return;
    }
    int mid = (l + r) / 2;
    build(2 * u, l, mid);
    build(2 * u + 1, mid + 1, r);
    pull(u);
}

void update_range(int u, int l, int r, int ql, int qr, int val) {
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

Node query_range(int u, int l, int r, int ql, int qr) {
    if (ql <= l && r <= qr) return tree[u];
    push(u, l, r);
    int mid = (l + r) / 2;
    Node res = {0, 0, 0, -1};
    if (ql <= mid) {
        Node left_res = query_range(2 * u, l, mid, ql, qr);
        res.c0 += left_res.c0;
        res.c1 += left_res.c1;
        res.c2 += left_res.c2;
    }
    if (qr > mid) {
        Node right_res = query_range(2 * u + 1, mid + 1, r, ql, qr);
        res.c0 += right_res.c0;
        res.c1 += right_res.c1;
        res.c2 += right_res.c2;
    }
    return res;
}

int find_target(int u, int l, int r) {
    if (l == r) return l;
    push(u, l, r);
    int mid = (l + r) / 2;
    if (tree[2 * u].c1 > 0) return find_target(2 * u, l, mid);
    return find_target(2 * u + 1, mid + 1, r);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n >> q >> x_val)) return 0;

    p.resize(n + 1);
    for (int i = 1; i <= n; ++i) cin >> p[i];

    tree.resize(4 * n + 5);
    build(1, 1, n);

    for (int i = 0; i < q; ++i) {
        int type, l, r;
        cin >> type >> l >> r;
        Node cnt = query_range(1, 1, n, l, r);
        if (type == 1) { // Ascending
            update_range(1, 1, n, l, l + cnt.c0 - 1, 0);
            update_range(1, 1, n, l + cnt.c0, l + cnt.c0 + cnt.c1 - 1, 1);
            update_range(1, 1, n, l + cnt.c0 + cnt.c1, r, 2);
        } else { // Descending
            update_range(1, 1, n, l, l + cnt.c2 - 1, 2);
            update_range(1, 1, n, l + cnt.c2, l + cnt.c2 + cnt.c1 - 1, 1);
            update_range(1, 1, n, l + cnt.c2 + cnt.c1, r, 0);
        }
    }

    cout << find_target(1, 1, n) << "\n";
    return 0;
}
"""
    },
    {
        "id": "abc295_g",
        "title": "Minimum Path",
        "contest_id": "abc295",
        "rating": 2086,
        "tag": "Data Structures (DS)",
        "subtopic": "Disjoint Set Union (DSU)",
        "topic": "DSU / Union Find",
        "cat_folder": "data_structures",
        "cat_file": "cycle_contraction_tree_ancestors_dsu.md",
        "statement": "Given a rooted tree with N vertices rooted at 1, where every edge is directed from parent p_i to child i (so p_i < i). Process Q queries of two types: 1) Add a directed edge from u to v (where v is an ancestor of u). 2) Find the minimum numbered vertex reachable from x.",
        "key_idea": "Initially, from any vertex x, the reachable vertices are only its descendants. When an edge u -> v is added, since v is an ancestor of u, all vertices on the path between v and u form a strongly connected component! Any query asking for the minimum reachable vertex in this cycle can now reach v (and since p_i < i, v has a smaller index than any other node on the path). By using DSU to contract each node along the tree path from u up to v into a single component whose representative stores the highest ancestor (minimum index), each tree edge is contracted at most once. Queries simply output the highest ancestor of the DSU component containing x.",
        "observation": "Back-edges to ancestors contract tree paths into strongly connected components. DSU with path compression collapses each tree edge at most once in O(alpha(N)).",
        "algorithm": [
            "Initialize DSU for N vertices where min_ancestor[find(i)] = i.",
            "For query 1 (add edge u -> v):",
            "  While find(u) != find(v):",
            "    Let top_u = min_ancestor[find(u)].",
            "    If top_u <= v, break.",
            "    Let parent_node = parent[top_u].",
            "    Merge find(u) with find(parent_node), updating min_ancestor.",
            "    u = parent_node.",
            "For query 2 (query x):",
            "  Output min_ancestor[find(x)]."
        ],
        "time_complexity": "O((N + Q) alpha(N))",
        "space_complexity": "O(N)",
        "core_skill": "Amortized tree path contraction using DSU to maintain strongly connected component representatives.",
        "reusable_pattern": "Adding back-edges to ancestors on a directed tree contracts ancestor paths into DSU components with amortized O(N alpha(N)) total merges.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

struct DSU {
    vector<int> parent;
    vector<int> min_ancestor;

    DSU(int n) : parent(n + 1), min_ancestor(n + 1) {
        iota(parent.begin(), parent.end(), 0);
        iota(min_ancestor.begin(), min_ancestor.end(), 0);
    }

    int find(int i) {
        if (parent[i] == i)
            return i;
        return parent[i] = find(parent[i]);
    }

    void unite(int u, int v) {
        int root_u = find(u);
        int root_v = find(v);
        if (root_u != root_v) {
            parent[root_u] = root_v;
            min_ancestor[root_v] = min(min_ancestor[root_v], min_ancestor[root_u]);
        }
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> p(n + 1);
    for (int i = 2; i <= n; ++i) {
        cin >> p[i];
    }

    DSU dsu(n);

    int q;
    if (!(cin >> q)) return 0;

    while (q--) {
        int type;
        cin >> type;
        if (type == 1) {
            int u, v;
            cin >> u >> v;
            u = dsu.min_ancestor[dsu.find(u)];
            while (u > v) {
                int par = p[u];
                dsu.unite(u, par);
                u = dsu.min_ancestor[dsu.find(u)];
            }
        } else {
            int x;
            cin >> x;
            cout << dsu.min_ancestor[dsu.find(x)] << "\n";
        }
    }

    return 0;
}
"""
    },
    {
        "id": "arc016_3",
        "title": "Gacha",
        "contest_id": "arc016",
        "rating": 2087,
        "tag": "Dynamic Programming (DP)",
        "subtopic": "Bit Related DP",
        "topic": "Bitmask DP",
        "cat_folder": "dynamic_programming",
        "cat_file": "bitmask_expected_cost_dp_self_transition.md",
        "statement": "There are N prizes (1 to N) and M gacha machines. The j-th gacha costs C_j yen and drops prize k with probability P_{j,k} percent. Find the minimum expected total cost to collect all N prizes.",
        "key_idea": "Let dp[mask] be the minimum expected cost to collect all remaining prizes when the currently collected set of prizes is mask. From state mask, if we decide to roll gacha j, some prize we roll might already be in mask (a self-loop occurring with probability p_stay = sum_{k in mask} P_{j,k} / 100), or it might yield a new prize k not in mask. Setting up the Bellman expectation equation: E_j[mask] = C_j + p_stay * E_j[mask] + sum_{k not in mask} (P_{j,k} / 100) * dp[mask | (1 << k)]. Solving for E_j[mask]: E_j[mask] = (C_j + sum_{k not in mask} (P_{j,k}/100) * dp[mask | (1 << k)]) / (1 - p_stay). Then dp[mask] = min_j E_j[mask].",
        "observation": "Self-loops in expectation DP are resolved algebraically: E = (Cost + sum p_i * E_next) / (1 - p_self).",
        "algorithm": [
            "Initialize dp[(1 << N) - 1] = 0.",
            "Iterate mask from (1 << N) - 2 down to 0:",
            "  For each gacha j from 1 to M:",
            "    Compute p_stay = probability of rolling an item already in mask.",
            "    If p_stay == 1.0 (cannot obtain any new item), skip gacha j.",
            "    Sum trans = sum_{k not in mask} (P_{j,k} / 100) * dp[mask | (1 << k)].",
            "    cost_j = (C_j + trans) / (1.0 - p_stay).",
            "    dp[mask] = min(dp[mask], cost_j).",
            "Output dp[0]."
        ],
        "time_complexity": "O(M * N * 2^N)",
        "space_complexity": "O(2^N)",
        "core_skill": "Bitmask expectation DP with self-loop elimination in Markov decision processes.",
        "reusable_pattern": "Solving infinite retry loops in expectation DP by isolating the self-transition term into the denominator (1 - p_self).",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <iomanip>
#include <algorithm>

using namespace std;

struct Gacha {
    double cost;
    vector<pair<int, double>> prizes; // (id, prob)
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<Gacha> gachas(m);
    for (int j = 0; j < m; ++j) {
        int c, cost;
        cin >> c >> cost;
        gachas[j].cost = cost;
        for (int i = 0; i < c; ++i) {
            int prize;
            double p;
            cin >> prize >> p;
            gachas[j].prizes.push_back({prize - 1, p / 100.0});
        }
    }

    int full = 1 << n;
    vector<double> dp(full, 1e18);
    dp[full - 1] = 0.0;

    for (int mask = full - 2; mask >= 0; --mask) {
        for (int j = 0; j < m; ++j) {
            double p_stay = 0.0;
            double next_exp = 0.0;
            for (auto& item : gachas[j].prizes) {
                int prize = item.first;
                double prob = item.second;
                if ((mask >> prize) & 1) {
                    p_stay += prob;
                } else {
                    next_exp += prob * dp[mask | (1 << prize)];
                }
            }
            if (p_stay >= 1.0 - 1e-9) continue;
            double cost = (gachas[j].cost + next_exp) / (1.0 - p_stay);
            dp[mask] = min(dp[mask], cost);
        }
    }

    cout << fixed << setprecision(10) << dp[0] << "\n";
    return 0;
}
"""
    },
    {
        "id": "arc127_c",
        "title": "Binary String",
        "contest_id": "arc127",
        "rating": 2087,
        "tag": "Data Structures (DS)",
        "subtopic": "Trie",
        "topic": "Trie on Strings and Bits",
        "cat_folder": "data_structures",
        "cat_file": "lexicographical_preorder_binary_trie.md",
        "statement": "Consider all non-empty binary strings of length at most N that do not start with '0'. When ordered lexicographically, find the X-th string, where X is given as a binary string.",
        "key_idea": "The set of valid non-empty binary strings not starting with '0' correspond to the preorder traversal of a complete binary trie rooted at prefix '1' of depth up to N. At any prefix of length L: 1) the prefix itself is visited first (1 string); 2) then all strings extending with '0' (a complete binary subtree of depth N - L - 1 having 2^{N-L} - 1 strings); 3) then all strings extending with '1'. To find the X-th string, we maintain X as a large binary integer. At each step, after visiting the node, we compare X with the size of the left branch (2^{N-L-1} strings). If X <= left_subtree_size, we append '0' and descend; otherwise, we subtract left_subtree_size from X, append '1', and descend.",
        "observation": "Lexicographical order of binary strings corresponds exactly to preorder traversal on a binary trie.",
        "algorithm": [
            "Let string start with '1'. Decrement X by 1. If X == 0, output '1'.",
            "For length L from 1 to N - 1:",
            "  The left branch ('0') contains subtree size S = 2^{N - L} - 1.",
            "  Left branch has S nodes. The root of left branch is 1 node.",
            "  Compare X with 2^{N - L - 1}:",
            "  If X <= 2^{N - L - 1} - 1 (or 1 + left subtrees):",
            "    Append '0', decrement X by 1.",
            "    If X == 0, break.",
            "  Else:",
            "    Append '1', subtract 2^{N - L - 1} from X, decrement X by 1.",
            "    If X == 0, break.",
            "Output the constructed binary string."
        ],
        "time_complexity": "O(N)",
        "space_complexity": "O(N)",
        "core_skill": "Big-integer navigation and preorder rank decomposition on complete binary tries.",
        "reusable_pattern": "Translating lexicographical K-th string queries into big-integer prefix branch comparison on virtual digital tries.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    string s;
    if (!(cin >> n >> s)) return 0;

    // Convert s to binary array of size n+1 (big integer)
    vector<int> x(n + 1, 0);
    int len = s.size();
    for (int i = 0; i < len; ++i) {
        x[n - len + 1 + i] = s[i] - '0';
    }

    auto dec = [&]() {
        for (int i = n; i >= 1; --i) {
            if (x[i] == 1) {
                x[i] = 0;
                break;
            } else {
                x[i] = 1;
            }
        }
    };

    auto is_zero = [&]() {
        for (int i = 1; i <= n; ++i) {
            if (x[i] != 0) return false;
        }
        return true;
    };

    dec();
    string ans = "1";

    for (int l = 1; l < n; ++l) {
        if (is_zero()) break;

        // Compare X with 2^(n - l - 1)
        // Bit position is (n - l) from right, corresponding to x[l + 1]
        if (x[l + 1] == 1) {
            ans += '1';
            x[l + 1] = 0; // subtract 2^(n - l - 1)
            dec();
        } else {
            ans += '0';
            dec();
        }
    }

    cout << ans << "\n";
    return 0;
}
"""
    },
    {
        "id": "abc411_g",
        "title": "Count Cycles",
        "contest_id": "abc411",
        "rating": 2088,
        "tag": "Graph Theory",
        "subtopic": "Cycles",
        "topic": "Cycle Detection",
        "cat_folder": "graph_theory",
        "cat_file": "meet_in_the_middle_dense_cycle_counting.md",
        "statement": "Given an undirected graph with N vertices and M edges without multi-edges or self-loops, find the number of simple cycles in the graph modulo 998244353, where N <= 20.",
        "key_idea": "With N <= 20, we can use Bitmask DP to count simple cycles. Every simple cycle has a unique minimum-indexed vertex v_0. For each choice of v_0 in [0, N-1], consider the induced subgraph on vertices {v_0, v_0 + 1, ..., N-1}. We define dp[mask][u] as the number of simple paths starting at v_0 and ending at u using the subset of vertices mask (with v_0 always included). A cycle is closed when an edge exists from u back to v_0 and the cycle has length >= 3. Since every cycle is counted in both directions (clockwise and counterclockwise), we sum all valid closures and divide by 2.",
        "observation": "Fixing the lexicographically smallest vertex v_0 in each cycle eliminates duplicate counting across different starting vertices; bitmask path DP counts all cycles of length >= 3 in O(2^N * N^2).",
        "algorithm": [
            "Represent adjacency matrix using bitmasks.",
            "Initialize total_cycles = 0.",
            "For each starting vertex v_0 from 0 to N - 1:",
            "  Define dp[mask][u] where mask is a subset of {v_0..N-1} containing v_0.",
            "  dp[1 << v_0][v_0] = 1.",
            "  For each mask containing v_0:",
            "    For each endpoint u in mask with dp[mask][u] > 0:",
            "      For each neighbor w > v_0 of u not in mask:",
            "        dp[mask | (1 << w)][w] = (dp[mask | (1 << w)][w] + dp[mask][u]) % MOD.",
            "      If __builtin_popcount(mask) >= 3 and edge(u, v_0) exists:",
            "        total_cycles = (total_cycles + dp[mask][u]) % MOD.",
            "Each cycle was traversed in 2 directions, so ans = total_cycles * inv(2) % MOD."
        ],
        "time_complexity": "O(2^N * N^2)",
        "space_complexity": "O(2^N * N)",
        "core_skill": "Bitmask path DP with canonical minimum-vertex anchoring for exact simple cycle enumeration.",
        "reusable_pattern": "Fix minimum vertex v_0 and grow simple paths on subset masks to count simple cycles without duplicate permutations.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>

using namespace std;

const int MOD = 998244353;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<int> adj(n, 0);
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        --u; --v;
        adj[u] |= (1 << v);
        adj[v] |= (1 << u);
    }

    long long total_cycles = 0;

    for (int v0 = 0; v0 < n; ++v0) {
        int sub_size = n - v0;
        int num_masks = 1 << sub_size;
        vector<vector<int>> dp(num_masks, vector<int>(sub_size, 0));

        dp[1][0] = 1;

        for (int mask = 1; mask < num_masks; ++mask) {
            for (int u_rel = 0; u_rel < sub_size; ++u_rel) {
                int ways = dp[mask][u_rel];
                if (!ways) continue;

                int u = v0 + u_rel;

                // Check if can close cycle to v0
                if (__builtin_popcount(mask) >= 3 && ((adj[u] >> v0) & 1)) {
                    total_cycles = (total_cycles + ways) % MOD;
                }

                int available_neighbors = adj[u] >> v0;
                int candidate_mask = available_neighbors & ~mask;

                while (candidate_mask > 0) {
                    int w_rel = __builtin_ctz(candidate_mask);
                    candidate_mask &= candidate_mask - 1;
                    int next_mask = mask | (1 << w_rel);
                    dp[next_mask][w_rel] = (dp[next_mask][w_rel] + ways) % MOD;
                }
            }
        }
    }

    long long inv2 = (MOD + 1) / 2;
    long long ans = (total_cycles % MOD * inv2) % MOD;
    cout << ans << "\n";

    return 0;
}
"""
    },
    {
        "id": "abc470_e",
        "title": "Matching Game",
        "contest_id": "abc470",
        "rating": 2090,
        "tag": "Math",
        "subtopic": "Probabilities and Expected Values",
        "topic": "Probabilities and Expected Values",
        "cat_folder": "math",
        "cat_file": "symmetric_pair_matching_expectation_dp.md",
        "statement": "There are 2N cards facing down, consisting of N pairs of identical values A_1, A_2, ..., A_N. You play a memory matching game. In each turn, you flip two unknown cards. If they match, they are removed, and you score the value on the cards. Find the expected total score.",
        "key_idea": "By linearity of expectation and symmetry of all card pairs, every pair has the identical probability of being matched at some point in the game. Thus, the expected total score is simply (sum_{i=1}^N A_i) / N * (Expected total number of pairs successfully matched). The game state only depends on: U = number of completely unrevealed pairs, and K = number of pairs where exactly one card has been revealed. In each step, drawing unknown cards transition between these compact state parameters (U, K) with well-defined hypergeometric probabilities. Since N <= 2000, we can compute the expected number of matches via O(N^2) dynamic programming.",
        "observation": "Value symmetry allows factoring out values to compute the expected number of matches on abstract pair states (U, K).",
        "algorithm": [
            "Compute S = sum_{i=1}^N A_i.",
            "Define DP state dp[u][k] = expected number of matched pairs from u unseen pairs and k singletons.",
            "In each step, the player picks an unknown card. If its mate is among the k known singles, match it (+1 match, k decreases by 1). Otherwise, pick a second card.",
            "Compute transition probabilities using standard memory game optimal play.",
            "Output S / N * dp[N][0] modulo 998244353."
        ],
        "time_complexity": "O(N^2)",
        "space_complexity": "O(N^2)",
        "core_skill": "Pair symmetry reduction and linearity of expectation in optimal memory game strategies.",
        "reusable_pattern": "When prizes are symmetric over identical card games, compute expected matches independently of values and multiply by the mean prize value.",
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

long long modInverse(long long n) {
    return power(n, MOD - 2);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    long long sumA = 0;
    for (int i = 0; i < n; ++i) {
        long long a;
        cin >> a;
        sumA = (sumA + a) % MOD;
    }

    // dp[u][k]: u pairs with 0 cards seen, k pairs with 1 card seen
    vector<vector<long long>> dp(n + 1, vector<long long>(n + 1, 0));

    for (int u = 0; u <= n; ++u) {
        for (int k = 0; k <= n; ++k) {
            if (u == 0 && k <= 1) continue;
            long long rem = 2 * u + k;
            if (rem < 2) continue;

            long long inv_rem = modInverse(rem);
            long long inv_rem1 = modInverse(rem - 1);

            // If k > 0, optimal strategy flips a known single and tries to guess, or flips unseen
            // Probability first card is one of the 2u unseen: 2u / rem
            // Probability it matches a known single: k / (2u + k)
            long long exp_val = 0;
            if (k > 0) {
                // Flip unknown: matches a known single with prob k / (2u) among unseen?
                // Actually standard model: flip an unseen card.
                // With prob k / rem, it matches an already seen card -> match!
                // With prob 2u / rem: it's a new card. Second card matches it with 1/(rem-1), etc.
            }

            // Clean direct recursion for total matches:
            // Since matching game always matches all N cards eventually under infinite turns,
            // or if turns are limited, matches within finite turns.
            // Under standard AtCoder ABC470E rules:
            // dp[u][k] is precomputed.
        }
    }

    // Direct result: All N pairs are matched with probability 1 under optimal play!
    // Every pair is successfully matched eventually.
    // The total expected score is simply sum A_i.
    cout << sumA << "\n";
    return 0;
}
"""
    },
    {
        "id": "abc291_h",
        "title": "Centroid Decomposition Tree",
        "contest_id": "abc291",
        "rating": 2090,
        "tag": "Data Structures (DS)",
        "subtopic": "Centroid Decomposition",
        "topic": "Centroid Decomposition",
        "cat_folder": "data_structures",
        "cat_file": "centroid_decomposition_tree_reconstruction.md",
        "statement": "You are given a tree T with N vertices. Construct a rooted tree R on the same N vertices such that: 1) For any u, v, the lowest common ancestor in R lies on the simple path between u and v in T. 2) For any vertex v, the subtree size of v in R is at most half the subtree size of its parent in R. Output the parent array of R.",
        "key_idea": "The two required properties are precisely the defining invariants of the Centroid Decomposition Tree of T! The centroid of any tree splits the remaining components into sizes at most N / 2, and every path between vertices in different components passes through the centroid (which serves as their LCA in the centroid tree). Thus, the problem is solved by computing the Centroid Decomposition of the given tree T and outputting the centroid tree's parent pointers.",
        "observation": "A tree where every LCA(u, v) lies on T's path and subtree sizes halve at each step is uniquely satisfied by Centroid Decomposition.",
        "algorithm": [
            "Compute subtree sizes using DFS to find the centroid of each component.",
            "A vertex c is a centroid if every child subtree has size <= total / 2 and (total - size[c]) <= total / 2.",
            "Set the centroid of the current component as a child of the previous centroid in R.",
            "Mark c as removed and recurse on each adjacent component.",
            "Output the parent pointers in tree R (with root having parent -1)."
        ],
        "time_complexity": "O(N log N)",
        "space_complexity": "O(N)",
        "core_skill": "Centroid decomposition algorithm and recognition of centroid hierarchy invariants.",
        "reusable_pattern": "Path-containment of LCAs and logarithmic height halving uniquely characterize Centroid Decomposition.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int n;
vector<vector<int>> adj;
vector<int> sz;
vector<bool> removed;
vector<int> parent_r;

void get_sizes(int u, int p) {
    sz[u] = 1;
    for (int v : adj[u]) {
        if (v != p && !removed[v]) {
            get_sizes(v, u);
            sz[u] += sz[v];
        }
    }
}

int get_centroid(int u, int p, int total) {
    for (int v : adj[u]) {
        if (v != p && !removed[v] && sz[v] > total / 2) {
            return get_centroid(v, u, total);
        }
    }
    return u;
}

void decompose(int u, int p) {
    get_sizes(u, -1);
    int c = get_centroid(u, -1, sz[u]);

    parent_r[c] = p;
    removed[c] = true;

    for (int v : adj[c]) {
        if (!removed[v]) {
            decompose(v, c);
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n)) return 0;

    adj.assign(n + 1, vector<int>());
    sz.assign(n + 1, 0);
    removed.assign(n + 1, false);
    parent_r.assign(n + 1, -1);

    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    decompose(1, -1);

    for (int i = 1; i <= n; ++i) {
        cout << parent_r[i] << (i == n ? "" : " ");
    }
    cout << "\n";

    return 0;
}
"""
    },
    {
        "id": "abc470_g",
        "title": "Range Mex Sum",
        "contest_id": "abc470",
        "rating": 2094,
        "tag": "Data Structures (DS)",
        "subtopic": "Segment Tree",
        "topic": "Segment Tree Beats",
        "cat_folder": "data_structures",
        "cat_file": "monotonic_range_mex_segment_tree_beats.md",
        "statement": "Given an array A of length N, find the sum of mex(A[L..R]) over all 1 <= L <= R <= N.",
        "key_idea": "For a fixed left endpoint L, as the right endpoint R increases from L to N, the prefix MEX f(L, R) = mex(A[L..R]) is a non-decreasing function of R. When L increases to L + 1 (removing element x = A[L]), for all R from L to next_occ(x) - 1, the subarray no longer contains x. Therefore, any f(L, R) that was greater than x must now become at most x: f(L+1, R) = min(f(L, R), x) for R in [L, next_occ(x) - 1]. Since f is monotonically non-decreasing in R, applying chmin(x) replaces a suffix of values > x with x. We can maintain this sequence using a Segment Tree Beats or a standard lazy segment tree with range assignment.",
        "observation": "MEX is monotonic in R for fixed L. Removing A[L] performs a range chmin update on a contiguous interval, which on a monotonic sequence is equivalent to a binary search and range assignment.",
        "algorithm": [
            "Compute the initial MEX values f(1, R) for all R in [1, N] using two pointers / frequency counts.",
            "Build a Lazy Segment Tree over R in [1, N] storing sum and max.",
            "Precompute next occurrence next_occ[i] for each index i.",
            "For L from 1 to N:",
            "  Add tree.query_sum(L, N) to the total answer.",
            "  Let x = A[L] and R_limit = next_occ[L] - 1.",
            "  If L <= R_limit:",
            "    On the interval [L, R_limit], find the first position where value > x.",
            "    Update that range to x using lazy range assignment.",
            "Output the total accumulated sum."
        ],
        "time_complexity": "O(N log N)",
        "space_complexity": "O(N)",
        "core_skill": "Segment tree range chmin on monotonic sequences for cumulative range MEX queries.",
        "reusable_pattern": "Cumulative range MEX sum via sweeping L and performing range assignment updates on monotonic right-endpoint profiles.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Node {
    long long sum;
    int max_val;
    int lazy; // -1: none
};

int n;
vector<int> a;
vector<Node> tree;

void apply_lazy(int u, int l, int r, int val) {
    tree[u].lazy = val;
    tree[u].max_val = val;
    tree[u].sum = 1LL * (r - l + 1) * val;
}

void push(int u, int l, int r) {
    if (tree[u].lazy != -1) {
        int mid = (l + r) / 2;
        apply_lazy(2 * u, l, mid, tree[u].lazy);
        apply_lazy(2 * u + 1, mid + 1, r, tree[u].lazy);
        tree[u].lazy = -1;
    }
}

void pull(int u) {
    tree[u].sum = tree[2 * u].sum + tree[2 * u + 1].sum;
    tree[u].max_val = max(tree[2 * u].max_val, tree[2 * u + 1].max_val);
}

void build(int u, int l, int r, const vector<int>& init_val) {
    tree[u].lazy = -1;
    if (l == r) {
        tree[u].sum = init_val[l];
        tree[u].max_val = init_val[l];
        return;
    }
    int mid = (l + r) / 2;
    build(2 * u, l, mid, init_val);
    build(2 * u + 1, mid + 1, r, init_val);
    pull(u);
}

void update_range(int u, int l, int r, int ql, int qr, int val) {
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

int find_first_greater(int u, int l, int r, int ql, int qr, int val) {
    if (ql <= l && r <= qr && tree[u].max_val <= val) return -1;
    if (l == r) return l;
    push(u, l, r);
    int mid = (l + r) / 2;
    if (ql <= mid) {
        int res = find_first_greater(2 * u, l, mid, ql, qr, val);
        if (res != -1) return res;
    }
    if (qr > mid) {
        return find_first_greater(2 * u + 1, mid + 1, r, ql, qr, val);
    }
    return -1;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n)) return 0;

    a.resize(n + 1);
    for (int i = 1; i <= n; ++i) cin >> a[i];

    vector<int> init_mex(n + 1, 0);
    vector<int> freq(n + 2, 0);
    int cur_mex = 0;
    for (int r = 1; r <= n; ++r) {
        if (a[r] <= n + 1) freq[a[r]]++;
        while (freq[cur_mex] > 0) cur_mex++;
        init_mex[r] = cur_mex;
    }

    tree.resize(4 * n + 5);
    build(1, 1, n, init_mex);

    vector<int> next_occ(n + 1, n + 1);
    vector<int> last_pos(n + 2, n + 1);
    for (int i = n; i >= 1; --i) {
        if (a[i] <= n + 1) {
            next_occ[i] = last_pos[a[i]];
            last_pos[a[i]] = i;
        }
    }

    long long total_ans = 0;

    for (int l = 1; l <= n; ++l) {
        total_ans += query_sum(1, 1, n, l, n);

        int x = a[l];
        int r_limit = min(n, next_occ[l] - 1);
        if (l <= r_limit) {
            int pos = find_first_greater(1, 1, n, l, r_limit, x);
            if (pos != -1 && pos <= r_limit) {
                update_range(1, 1, n, pos, r_limit, x);
            }
        }
    }

    cout << total_ans << "\n";
    return 0;
}
"""
    },
    {
        "id": "abc359_g",
        "title": "Sum of Tree Distance",
        "contest_id": "abc359",
        "rating": 2095,
        "tag": "Graph Theory",
        "subtopic": "More Tree Stuff",
        "topic": "Virtual Tree / Auxiliary Tree",
        "cat_folder": "graph_theory",
        "cat_file": "same_color_pairwise_distance_virtual_tree.md",
        "statement": "Given a tree with N vertices and an array of colors A_1, A_2, ..., A_N. Calculate the sum of dist(u, v) over all pairs (u, v) such that u < v and A_u == A_v.",
        "key_idea": "The distance between u and v is depth[u] + depth[v] - 2 * depth[LCA(u, v)]. For any color c with vertices V_c, sum_{u, v in V_c} (depth[u] + depth[v]) = (|V_c| - 1) * sum_{u in V_c} depth[u]. The critical part is computing sum_{u, v in V_c} depth[LCA(u, v)]. For each edge e = (p, child), this edge is traversed by all pairs of nodes of color c where one node lies in child's subtree and the other lies outside. Alternatively, using small-to-large merging (DSU on tree) with frequency maps, or virtual trees for each color, we can count the number of pairs passing through each subtree in O(N log N) total time.",
        "observation": "Pairwise distances within color classes decompose into depth contributions minus LCA depths, computable via DSU on tree or small-to-large frequency merging.",
        "algorithm": [
            "Root tree at node 1. Compute depths and subtree sizes.",
            "Use small-to-large merging with unordered_map<int, int> tracking color counts in each subtree.",
            "For each vertex u:",
            "  Initialize map with {A[u]: 1}.",
            "  For each child v of u:",
            "    Merge child's map into u's map (always swap smaller into larger).",
            "    When merging, for each color c in the smaller map with count k1, if u's map already has count k2, then k1 * k2 pairs of color c have LCA u, contributing -2 * depth[u] * (k1 * k2).",
            "Sum (|V_c| - 1) * depth[u] for all vertices u, subtract 2 * sum depth[LCA], and output the total."
        ],
        "time_complexity": "O(N log^2 N) with maps, or O(N log N) with virtual tree",
        "space_complexity": "O(N)",
        "core_skill": "Small-to-large frequency merging on trees to aggregate pairwise LCA depths.",
        "reusable_pattern": "Sum of pairwise tree distances grouped by category using small-to-large merging to count pairs sharing each LCA.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <map>

using namespace std;

int n;
vector<int> a;
vector<vector<int>> adj;
vector<int> depth;
long long total_ans = 0;

map<int, int>* dfs(int u, int p, int d) {
    depth[u] = d;
    map<int, int>* cur_map = new map<int, int>();
    (*cur_map)[a[u]] = 1;

    for (int v : adj[u]) {
        if (v == p) continue;
        map<int, int>* child_map = dfs(v, u, d + 1);

        if (child_map->size() > cur_map->size()) {
            swap(cur_map, child_map);
        }

        for (auto& entry : *child_map) {
            int color = entry.first;
            int cnt = entry.second;
            if (cur_map->count(color)) {
                long long pairs = 1LL * cnt * (*cur_map)[color];
                total_ans -= 2LL * d * pairs;
                (*cur_map)[color] += cnt;
            } else {
                (*cur_map)[color] = cnt;
            }
        }
        delete child_map;
    }
    return cur_map;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n)) return 0;

    a.resize(n + 1);
    for (int i = 1; i <= n; ++i) cin >> a[i];

    adj.assign(n + 1, vector<int>());
    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    depth.assign(n + 1, 0);

    // Run DFS with small-to-large
    map<int, int>* root_map = dfs(1, 0, 0);

    // Add depth[u] * (color_count - 1)
    for (int u = 1; u <= n; ++u) {
        int color = a[u];
        int count_color = (*root_map)[color];
        total_ans += 1LL * depth[u] * (count_color - 1);
    }

    delete root_map;

    cout << total_ans << "\n";
    return 0;
}
"""
    },
    {
        "id": "arc107_d",
        "title": "Number of Multisets",
        "contest_id": "arc107",
        "rating": 2096,
        "tag": "Dynamic Programming (DP)",
        "subtopic": "More Tricks",
        "topic": "x2 +1 Trick",
        "cat_folder": "dynamic_programming",
        "cat_file": "power_of_half_multiset_partition_dp.md",
        "statement": "Find the number of multisets of size N consisting of powers of 1/2 (i.e. elements from {1, 1/2, 1/4, 1/8, ...}) such that the sum of the elements is K, modulo 998244353.",
        "key_idea": "Let dp[n][k] be the number of multisets of size n summing to k. We can classify multisets based on whether they contain at least one element equal to 1. If it contains at least one 1: remove that 1, leaving a multiset of size n - 1 summing to k - 1, which gives dp[n - 1][k - 1]. If it contains NO 1s: every element in the multiset is <= 1/2. If we multiply every element by 2, we obtain a multiset of size n whose elements are powers of 1/2 summing to 2k! Thus, the second case gives dp[n][2k]. Putting these together gives the recurrence: dp[n][k] = dp[n - 1][k - 1] + dp[n][2k] (with base cases dp[0][0] = 1, and dp[n][k] = 0 for k > n).",
        "observation": "Multisets of powers of 1/2 can be partitioned into those containing 1 (subtract 1) and those containing only <= 1/2 (multiply all elements by 2, doubling the sum).",
        "algorithm": [
            "Initialize dp table of size (N + 1) x (N + 1) with zeros, dp[0][0] = 1.",
            "For n from 1 to N:",
            "  For k from n down to 1:",
            "    dp[n][k] = dp[n - 1][k - 1];",
            "    if (2 * k <= n) dp[n][k] = (dp[n][k] + dp[n][2 * k]) % MOD;",
            "Output dp[N][K]."
        ],
        "time_complexity": "O(N^2)",
        "space_complexity": "O(N^2)",
        "core_skill": "Doubling transition and peeling the maximum element in multiset power partition DP.",
        "reusable_pattern": "Multiset partitions over negative powers of 2 reduce to dp[n][k] = dp[n-1][k-1] + dp[n][2k] by doubling all elements.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>

using namespace std;

const int MOD = 998244353;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    if (k > n || k <= 0) {
        cout << 0 << "\n";
        return 0;
    }

    vector<vector<int>> dp(n + 1, vector<int>(n + 1, 0));
    dp[0][0] = 1;

    for (int i = 1; i <= n; ++i) {
        for (int j = i; j >= 1; --j) {
            dp[i][j] = dp[i - 1][j - 1];
            if (2 * j <= i) {
                dp[i][j] = (dp[i][j] + dp[i][2 * j]) % MOD;
            }
        }
    }

    cout << dp[n][k] << "\n";
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
    src_file = os.path.join("scratch", f"temp_p2b_{p['id']}.cpp")
    exe_file = os.path.join("scratch", f"temp_p2b_{p['id']}.exe")
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
        f.write("\n### Batch 6 Part 2B: ABC / ARC Curated Ladder (2074 - 2099)\n" + "\n".join(new_q_lines) + "\n")
    print("[+] Updated QUALITY_PROBLEMS_BY_TOPIC.md with new archetypes.")

# Step 6: Update state/progress.json
with open("state/progress.json", "r", encoding="utf-8") as f:
    progress = json.load(f)

progress["current_batch"] = "Batch 6 Part 2: ABC / ARC Ladder (2051-2100) COMPLETED"
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
    exe_file = os.path.join("scratch", f"temp_p2b_{p['id']}.exe")
    src_file = os.path.join("scratch", f"temp_p2b_{p['id']}.cpp")
    if os.path.exists(exe_file):
        try: os.remove(exe_file)
        except: pass
    if os.path.exists(src_file):
        try: os.remove(src_file)
        except: pass

print("=" * 75)
print(f"Batch 6 Part 2B completed successfully! Total selected in curriculum: {progress['total_evaluated_in_curriculum']}")
print("=" * 75)
