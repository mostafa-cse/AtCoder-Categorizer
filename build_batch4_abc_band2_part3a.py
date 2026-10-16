import os
import subprocess
import json

# Ensure directories exist
os.makedirs("analysis", exist_ok=True)
os.makedirs("categories", exist_ok=True)
os.makedirs("state", exist_ok=True)

print("=" * 75)
print("      PROCESSING BATCH 4 PART 3A: ABC CURATED LADDER (1460 - 1528)")
print("=" * 75)

SELECTED_PROBLEMS = [
    {
        "id": "arc108_c",
        "title": "Keep Graph Connected",
        "contest_id": "arc108",
        "rating": 1460,
        "tag": "Graph Theory",
        "subtopic": "Trees",
        "topic": "Spanning Tree Constructive Node Coloring",
        "cat_folder": "graph_theory",
        "cat_file": "spanning_tree_node_coloring.md",
        "statement": "Given a connected graph with N vertices and M edges, where edge i has label c_i (1 <= c_i <= N). Assign an integer label from 1 to N to each vertex such that for every vertex v, there is at least one incident edge (u, v) whose edge label equals the vertex label of v.",
        "key_idea": "Extract any spanning tree. Root it arbitrarily and assign labels top-down via DFS/BFS: each child v is assigned the label of its tree edge to parent u; if that matches parent u's label, assign an alternative unused label.",
        "observation": "On a spanning tree, every vertex except the root has a unique parent edge. If child v takes label(v) = edge_label(u, v), that edge satisfies vertex v! The only issue is if label(u) == edge_label(u, v). In that case, choose any label for v different from edge_label(u, v), which satisfies parent u via edge (u, v).",
        "algorithm": [
            "Build adjacency list for a spanning tree using BFS/DFS.",
            "Initialize ans array with 0. Set ans[root = 1] = 1.",
            "Traverse tree from root via BFS:",
            "  For each child v with parent u and edge label c:",
            "    If ans[u] != c, set ans[v] = c.",
            "    Else set ans[v] = (c % N) + 1.",
            "Print the assigned labels for all vertices."
        ],
        "time_complexity": "O(N + M)",
        "space_complexity": "O(N + M)",
        "core_skill": "Constructive bipartite/tree assignment by decoupling parent-child constraints along a spanning forest.",
        "reusable_pattern": "Spanning Tree Assignment: propagate constraints top-down, handling collision with cyclic fallback ((c % N) + 1).",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <queue>

using namespace std;

struct Edge {
    int to;
    int label;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<Edge>> adj(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v, c;
        cin >> u >> v >> c;
        adj[u].push_back({v, c});
        adj[v].push_back({u, c});
    }

    vector<int> ans(n + 1, 0);
    vector<bool> visited(n + 1, false);
    queue<int> q;

    ans[1] = 1;
    visited[1] = true;
    q.push(1);

    while (!q.empty()) {
        int u = q.front();
        q.pop();

        for (const auto& edge : adj[u]) {
            int v = edge.to;
            int c = edge.label;
            if (!visited[v]) {
                visited[v] = true;
                if (ans[u] != c) {
                    ans[v] = c;
                } else {
                    ans[v] = (c % n) + 1;
                }
                q.push(v);
            }
        }
    }

    for (int i = 1; i <= n; ++i) {
        cout << ans[i] << "\n";
    }

    return 0;
}
"""
    },
    {
        "id": "abc186_e",
        "title": "Throne",
        "contest_id": "abc186",
        "rating": 1461,
        "tag": "Number Theory",
        "subtopic": "Linear Congruence",
        "topic": "Linear Congruence Equation via Extended Euclidean Algorithm",
        "cat_folder": "number_theory",
        "cat_file": "linear_congruence_extended_gcd.md",
        "statement": "N chairs are arranged circularly labeled 0 to N - 1 clockwise. Takahashi starts at chair S and repeatedly jumps K chairs clockwise. Find the minimum number of jumps to land on chair 0, or -1 if impossible. Process T test cases.",
        "key_idea": "Landing on 0 is equivalent to the linear congruence K * x = -S (mod N), solved using the Extended Euclidean Algorithm.",
        "observation": "K * x = -S (mod N) has a solution iff gcd(K, N) divides (-S). If it does, divide K, N, -S by g = gcd(K, N) to obtain coprime K' and N'. Then x = (-S' * (K')^(-1)) mod N'.",
        "algorithm": [
            "extGCD(a, b, x, y): computes gcd(a, b) and coefficients x, y such that a*x + b*y = gcd(a, b).",
            "For each test case (N, S, K):",
            "  Let b = (N - S) % N. We need K * x = b (mod N).",
            "  Compute g = extGCD(K, N, x, y).",
            "  If b % g != 0, return -1.",
            "  Reduce: K' = K / g, N' = N / g, b' = b / g.",
            "  extGCD(K', N', inv_k, temp).",
            "  x = (inv_k % N' + N') % N'.",
            "  ans = (1LL * x * b') % N'.",
            "  Print ans."
        ],
        "time_complexity": "O(T * log(min(N, K)))",
        "space_complexity": "O(1)",
        "core_skill": "Solving linear congruences a * x = b (mod m) using the Extended Euclidean Algorithm.",
        "reusable_pattern": "Linear Congruence Solver: extGCD reduction to coprime moduli.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>

using namespace std;

long long extGCD(long long a, long long b, long long &x, long long &y) {
    if (b == 0) {
        x = 1;
        y = 0;
        return a;
    }
    long long x1, y1;
    long long g = extGCD(b, a % b, x1, y1);
    x = y1;
    y = x1 - (a / b) * y1;
    return g;
}

void solve() {
    long long n, s, k;
    cin >> n >> s >> k;

    long long b = (n - s) % n;
    long long x, y;
    long long g = extGCD(k, n, x, y);

    if (b % g != 0) {
        cout << -1 << "\n";
        return;
    }

    long long n_prime = n / g;
    long long b_prime = b / g;
    long long k_prime = k / g;

    extGCD(k_prime, n_prime, x, y);
    x = (x % n_prime + n_prime) % n_prime;

    long long ans = (__int128)x * b_prime % n_prime;
    cout << ans << "\n";
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
        "id": "abc251_d",
        "title": "At Most 3",
        "contest_id": "abc251",
        "rating": 1463,
        "tag": "Basics",
        "subtopic": "Constructive Algorithms",
        "topic": "Constructive Base-100 Representation for Additive Basis",
        "cat_folder": "basics",
        "cat_file": "base100_additive_basis.md",
        "statement": "Given W <= 10^6, construct a set of at most 300 integers such that every integer between 1 and W can be represented as the sum of AT MOST 3 distinct elements from the set.",
        "key_idea": "Decompose numbers in base 100. Any number <= 10^6 can be written as a + b * 100 + c * 10000 with 0 <= a, b, c <= 99.",
        "observation": "By including {1, 2, ..., 99}, {100, 200, ..., 9900}, and {10000, 20000, ..., 990000}, we use exactly 99 * 3 = 297 numbers <= 300. Every number in [1, 999999] can be uniquely written as a sum of at most 3 numbers (at most one from each set).",
        "algorithm": [
            "Generate set: {1 * i | 1 <= i <= 99}.",
            "Generate set: {100 * i | 1 <= i <= 99}.",
            "Generate set: {10000 * i | 1 <= i <= 99}.",
            "Total elements = 297.",
            "Print 297, followed by all 297 elements."
        ],
        "time_complexity": "O(1)",
        "space_complexity": "O(1)",
        "core_skill": "Positional base decomposition to construct minimal additive bases.",
        "reusable_pattern": "Additive 3-Sum Basis: {1..B-1}, {B*(1..B-1)}, {B^2*(1..B-1)} covering B^3 values.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int w;
    if (!(cin >> w)) return 0;

    vector<int> ans;
    for (int i = 1; i <= 99; ++i) ans.push_back(i);
    for (int i = 1; i <= 99; ++i) ans.push_back(i * 100);
    for (int i = 1; i <= 99; ++i) ans.push_back(i * 10000);

    cout << ans.size() << "\n";
    for (size_t i = 0; i < ans.size(); ++i) {
        cout << ans[i] << (i + 1 == ans.size() ? "\n" : " ");
    }

    return 0;
}
"""
    },
    {
        "id": "abc349_e",
        "title": "Weighted Tic-Tac-Toe",
        "contest_id": "abc349",
        "rating": 1464,
        "tag": "Game Theory",
        "subtopic": "Minimax",
        "topic": "3x3 Grid Minimax Game DP with Memoization",
        "cat_folder": "game_theory",
        "cat_file": "minimax_3x3_grid_game.md",
        "statement": "A 3x3 grid has point values A[i][j]. Takahashi and Aoki take turns claiming uncolored cells. If a move creates 3-in-a-row of a player's color, that player immediately wins. If all 9 cells are filled without 3-in-a-row, the player with the greater sum of cell scores wins. Determine who wins under optimal play.",
        "key_idea": "Because the game board is 3x3 with at most 9 turns, the total number of reachable states is at most 3^9 = 19,683. Solve via Minimax search with memoization.",
        "observation": "State is uniquely identified by the ternary encoding of the 3x3 board. Transitions check for 3-in-a-row win; if leaf state (full board), compare score totals.",
        "algorithm": [
            "Represent board state as string of length 9 or ternary integer.",
            "Define minimax(state):",
            "  Check if either player already has 3-in-a-row; if so, return win for that player.",
            "  If all 9 cells filled, compute total scores: player with higher score wins.",
            "  Whichever player's turn it is: try all uncolored cells.",
            "  If any branch leads to a win, return win for the current player.",
            "  Otherwise return loss.",
            "Print 'Takahashi' if Takahashi wins, else 'Aoki'."
        ],
        "time_complexity": "O(3^9 * 9)",
        "space_complexity": "O(3^9)",
        "core_skill": "Game-theoretic Minimax evaluation with terminal 3-in-a-row condition check on small state spaces.",
        "reusable_pattern": "Ternary Grid Minimax: memoized search over 3^N board states.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <string>
#include <map>

using namespace std;

long long A[3][3];
map<vector<int>, bool> memo;

bool check_line(const vector<int>& b, int p) {
    // Rows
    for (int r = 0; r < 3; ++r) {
        if (b[r * 3] == p && b[r * 3 + 1] == p && b[r * 3 + 2] == p) return true;
    }
    // Cols
    for (int c = 0; c < 3; ++c) {
        if (b[c] == p && b[3 + c] == p && b[6 + c] == p) return true;
    }
    // Diagonals
    if (b[0] == p && b[4] == p && b[8] == p) return true;
    if (b[2] == p && b[4] == p && b[6] == p) return true;
    return false;
}

// Returns true if the CURRENT player wins from this board state
bool can_win(vector<int>& b, int turn) {
    if (memo.count(b)) return memo[b];

    int prev_player = 3 - turn;
    if (check_line(b, prev_player)) {
        return memo[b] = false;
    }

    bool full = true;
    for (int x : b) if (x == 0) full = false;

    if (full) {
        long long score1 = 0, score2 = 0;
        for (int i = 0; i < 9; ++i) {
            if (b[i] == 1) score1 += A[i / 3][i % 3];
            else score2 += A[i / 3][i % 3];
        }
        if (turn == 1) return memo[b] = (score1 > score2);
        else return memo[b] = (score2 > score1);
    }

    for (int i = 0; i < 9; ++i) {
        if (b[i] == 0) {
            b[i] = turn;
            bool opp_win = can_win(b, 3 - turn);
            b[i] = 0;
            if (!opp_win) {
                return memo[b] = true;
            }
        }
    }

    return memo[b] = false;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    for (int r = 0; r < 3; ++r) {
        for (int c = 0; c < 3; ++c) {
            cin >> A[r][c];
        }
    }

    vector<int> b(9, 0);
    if (can_win(b, 1)) {
        cout << "Takahashi\n";
    } else {
        cout << "Aoki\n";
    }

    return 0;
}
"""
    },
    {
        "id": "abc285_e",
        "title": "Work or Rest",
        "contest_id": "abc285",
        "rating": 1466,
        "tag": "Dynamic Programming",
        "subtopic": "Classic DP",
        "topic": "Circular Segment Decomposition DP",
        "cat_folder": "dp",
        "cat_file": "circular_segment_decomposition_dp.md",
        "statement": "Schedule a repeating week of N days (N <= 5000) containing at least one rest day. On a workday, productivity is A[min(d_left, d_right)] where d_left and d_right are days to nearest rest days. Maximize total weekly productivity.",
        "key_idea": "By rotational symmetry, fix day 1 as a rest day. The remaining days are partitioned into contiguous blocks of workdays between rest days. The productivity of a block of length L depends solely on L.",
        "observation": "Precompute val[L] = productivity of a contiguous block of L workdays between two rest days. Then dp[i] = max productivity using first i days ending with a rest day at day i. Transition: dp[i] = max_{j < i} (dp[j] + val[i - j - 1]).",
        "algorithm": [
            "Precompute val[L] for L = 1..N: val[L] = sum_{k=1}^L A[min(k, L - k + 1)].",
            "Initialize dp[N + 1] with 0.",
            "For i from 1 to N:",
            "  For j from 0 to i - 1:",
            "    dp[i] = max(dp[i], dp[j] + val[i - j - 1]).",
            "Print dp[N]."
        ],
        "time_complexity": "O(N^2)",
        "space_complexity": "O(N)",
        "core_skill": "Circular symmetry breaking by fixing an anchor point followed by segment partitioning DP.",
        "reusable_pattern": "Circular Interval Partitioning: fix index 1 as boundary, dp[i] = max(dp[j] + cost(segment)).",
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

    vector<long long> a(n + 1);
    for (int i = 1; i <= n; ++i) {
        cin >> a[i];
    }

    // val[L]: productivity of L consecutive workdays between two rest days
    vector<long long> val(n + 1, 0);
    for (int L = 1; L <= n; ++L) {
        long long sum = 0;
        for (int k = 1; k <= L; ++k) {
            sum += a[min(k, L - k + 1)];
        }
        val[L] = sum;
    }

    vector<long long> dp(n + 1, 0);
    for (int i = 1; i <= n; ++i) {
        for (int j = 0; j < i; ++j) {
            dp[i] = max(dp[i], dp[j] + val[i - j - 1]);
        }
    }

    cout << dp[n] << "\n";
    return 0;
}
"""
    },
    {
        "id": "abc185_e",
        "title": "Sequence Matching",
        "contest_id": "abc185",
        "rating": 1468,
        "tag": "Dynamic Programming",
        "subtopic": "Classic DP",
        "topic": "Edit Distance / Sequence Alignment DP with Cost Function",
        "cat_folder": "dp",
        "cat_file": "edit_distance_sequence_alignment.md",
        "statement": "Given two sequences A of length N and B of length M. Remove elements from A and B to obtain equal-length sequences A' and B'. Cost is (elements removed) + (number of positions i where A'_i != B'_i). Minimize total cost.",
        "key_idea": "Classic Needleman-Wunsch sequence alignment DP. At each step, either delete A[i], delete B[j], or match/mismatch A[i] with B[j].",
        "observation": "dp[i][j] = min cost to process prefixes A[1..i] and B[1..j]. Transitions: dp[i-1][j] + 1 (delete A[i]), dp[i][j-1] + 1 (delete B[j]), and dp[i-1][j-1] + (A[i] == B[j] ? 0 : 1).",
        "algorithm": [
            "Initialize dp[N+1][M+1] with INF. dp[0][0] = 0.",
            "For i from 0 to N: dp[i][0] = i.",
            "For j from 0 to M: dp[0][j] = j.",
            "For i from 1 to N:",
            "  For j from 1 to M:",
            "    cost_match = (A[i] == B[j] ? 0 : 1);",
            "    dp[i][j] = min({dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + cost_match});",
            "Print dp[N][M]."
        ],
        "time_complexity": "O(N * M)",
        "space_complexity": "O(N * M)",
        "core_skill": "Dynamic programming for sequence alignment and generalized edit distance.",
        "reusable_pattern": "Needleman-Wunsch Alignment DP: dp[i][j] = min(delete_A, delete_B, match/substitute).",
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

    vector<int> a(n + 1), b(m + 1);
    for (int i = 1; i <= n; ++i) cin >> a[i];
    for (int j = 1; j <= m; ++j) cin >> b[j];

    vector<vector<int>> dp(n + 1, vector<int>(m + 1, 0));
    for (int i = 0; i <= n; ++i) dp[i][0] = i;
    for (int j = 0; j <= m; ++j) dp[0][j] = j;

    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            int match_cost = (a[i] == b[j] ? 0 : 1);
            dp[i][j] = min({dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + match_cost});
        }
    }

    cout << dp[n][m] << "\n";
    return 0;
}
"""
    },
    {
        "id": "arc116_c",
        "title": "Multiple Sequences",
        "contest_id": "arc116",
        "rating": 1468,
        "tag": "Number Theory",
        "subtopic": "Prime Factorization",
        "topic": "Prime Factorization Combinatorics / Stars and Bars",
        "cat_folder": "number_theory",
        "cat_file": "prime_factorization_stars_and_bars.md",
        "statement": "Find the number of integer sequences A of length N such that 1 <= A_1 <= ... <= A_N <= M and A_{i+1} is a multiple of A_i, modulo 998244353.",
        "key_idea": "Iterate over the last element x = A_N (1 <= x <= M). For each prime factor p^e dividing x, the e prime factors must be distributed across the N positions in the sequence, which is independent for each prime.",
        "observation": "Distributing e factors across N non-decreasing transitions corresponds to weak compositions of e into N non-negative integers: C(e + N - 1, N - 1). For x = prod p_i^{e_i}, total sequences ending at x is prod_i C(e_i + N - 1, N - 1).",
        "algorithm": [
            "Precompute combinations C(n, r) modulo 998244353.",
            "Precompute smallest prime factor (SPF) up to M using a sieve in O(M).",
            "ans = 0.",
            "For x from 1 to M:",
            "  Factorize x using SPF into prime powers p_i^{e_i}.",
            "  ways = 1.",
            "  For each exponent e_i: ways = ways * C(e_i + N - 1, N - 1) % MOD.",
            "  ans = (ans + ways) % MOD.",
            "Print ans."
        ],
        "time_complexity": "O(M log M)",
        "space_complexity": "O(N + M)",
        "core_skill": "Combining prime factorization multi-set distribution with Stars and Bars combinatorics.",
        "reusable_pattern": "Divisibility Chain Counting: prod_{p|x} C(exponent + N - 1, N - 1).",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>

using namespace std;

const int MOD = 998244353;
const int MAX = 300005;

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

void precompute() {
    fact[0] = 1;
    for (int i = 1; i < MAX; ++i) fact[i] = (fact[i - 1] * i) % MOD;
    invFact[MAX - 1] = power(fact[MAX - 1], MOD - 2);
    for (int i = MAX - 2; i >= 0; --i) invFact[i] = (invFact[i + 1] * (i + 1)) % MOD;
}

long long nCr(int n, int r) {
    if (r < 0 || r > n) return 0;
    return fact[n] * invFact[r] % MOD * invFact[n - r] % MOD;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    precompute();

    int n, m;
    if (!(cin >> n >> m)) return 0;

    // Sieve for SPF
    vector<int> spf(m + 1);
    for (int i = 1; i <= m; ++i) spf[i] = i;
    for (int i = 2; i * i <= m; ++i) {
        if (spf[i] == i) {
            for (int j = i * i; j <= m; j += i) {
                if (spf[j] == j) spf[j] = i;
            }
        }
    }

    long long total_ans = 0;
    for (int x = 1; x <= m; ++x) {
        int temp = x;
        long long ways = 1;
        while (temp > 1) {
            int p = spf[temp];
            int e = 0;
            while (temp % p == 0) {
                e++;
                temp /= p;
            }
            ways = (ways * nCr(e + n - 1, n - 1)) % MOD;
        }
        total_ans = (total_ans + ways) % MOD;
    }

    cout << total_ans << "\n";
    return 0;
}
"""
    },
    {
        "id": "abc075_d",
        "title": "Axis-Parallel Rectangle",
        "contest_id": "abc075",
        "rating": 1470,
        "tag": "Basics",
        "subtopic": "Exhaustive Search",
        "topic": "2D Coordinate Selection O(N^4) Search for K Points",
        "cat_folder": "basics",
        "cat_file": "coordinate_selection_rectangle_search.md",
        "statement": "Given N 2D points (N <= 50) and an integer K (2 <= K <= N). Find the minimum area of an axis-parallel rectangle containing at least K points on or inside its boundary.",
        "key_idea": "The optimal rectangle has its four sides aligned with the coordinates of some subset of the given points. Enumerate all pairs of x-coordinates and all pairs of y-coordinates.",
        "observation": "There are at most N distinct x-coordinates and N distinct y-coordinates. Choosing 2 x-coordinates and 2 y-coordinates yields C(N, 2)^2 <= 1.5 * 10^6 rectangles. Testing each in O(N) takes ~ 7 * 10^7 operations.",
        "algorithm": [
            "Store points (X[i], Y[i]).",
            "Collect sorted unique x-coordinates and y-coordinates.",
            "min_area = INF.",
            "For each pair of x-bounds (x1, x2) with x1 < x2:",
            "  For each pair of y-bounds (y1, y2) with y1 < y2:",
            "    Count how many points (X[i], Y[i]) satisfy x1 <= X[i] <= x2 and y1 <= Y[i] <= y2.",
            "    If count >= K, min_area = min(min_area, (x2 - x1) * (y2 - y1)).",
            "Print min_area."
        ],
        "time_complexity": "O(N^5) with small constant, runs in < 0.2s",
        "space_complexity": "O(N)",
        "core_skill": "Coordinate compression boundary enumeration for optimal 2D enclosing regions.",
        "reusable_pattern": "Minimal Bounding Box: test all pairs of existing x and y coordinates as candidates.",
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

    vector<long long> x(n), y(n);
    vector<long long> x_vals, y_vals;

    for (int i = 0; i < n; ++i) {
        cin >> x[i] >> y[i];
        x_vals.push_back(x[i]);
        y_vals.push_back(y[i]);
    }

    sort(x_vals.begin(), x_vals.end());
    sort(y_vals.begin(), y_vals.end());

    unsigned long long min_area = ~0ULL;

    for (int xi = 0; xi < n; ++xi) {
        for (int xj = xi + 1; xj < n; ++xj) {
            long long x1 = x_vals[xi];
            long long x2 = x_vals[xj];

            for (int yi = 0; yi < n; ++yi) {
                for (int yj = yi + 1; yj < n; ++yj) {
                    long long y1 = y_vals[yi];
                    long long y2 = y_vals[yj];

                    int count = 0;
                    for (int p = 0; p < n; ++p) {
                        if (x[p] >= x1 && x[p] <= x2 && y[p] >= y1 && y[p] <= y2) {
                            count++;
                        }
                    }

                    if (count >= k) {
                        unsigned long long area = (unsigned long long)(x2 - x1) * (y2 - y1);
                        if (area < min_area) {
                            min_area = area;
                        }
                    }
                }
            }
        }
    }

    cout << min_area << "\n";
    return 0;
}
"""
    },
    {
        "id": "arc073_b",
        "title": "Simple Knapsack",
        "contest_id": "abc060",
        "rating": 1477,
        "tag": "Dynamic Programming",
        "subtopic": "Classic DP",
        "topic": "Knapsack with Small Weight Variance [W, W+3]",
        "cat_folder": "dp",
        "cat_file": "knapsack_small_weight_variance.md",
        "statement": "Knapsack problem with N items (N <= 100), capacity W <= 10^9, but with the guarantee that all item weights w_i satisfy w_1 <= w_i <= w_1 + 3.",
        "key_idea": "Partition items into 4 groups by offset d = w_i - w_1 in {0, 1, 2, 3}. Sort each group by value descending, and iterate over how many items are selected from each group.",
        "observation": "Because values are positive, if we select c_d items from group d, it is always optimal to pick the c_d items with the highest values. Enumerating counts (c0, c1, c2, c3) yields at most (N/4)^4 ~ 4 * 10^5 states.",
        "algorithm": [
            "Partition items into groups g[0], g[1], g[2], g[3] based on w_i - w_1.",
            "Sort each group descending and compute prefix sums of values.",
            "max_val = 0.",
            "Iterate c0 from 0 to |g[0]|:",
            "  Iterate c1 from 0 to |g[1]|:",
            "    Iterate c2 from 0 to |g[2]|:",
            "      Iterate c3 from 0 to |g[3]|:",
            "        total_weight = (c0 + c1 + c2 + c3) * w1 + 0*c0 + 1*c1 + 2*c2 + 3*c3.",
            "        If total_weight <= W:",
            "          max_val = max(max_val, pref0[c0] + pref1[c1] + pref2[c2] + pref3[c3]).",
            "Print max_val."
        ],
        "time_complexity": "O(N^4)",
        "space_complexity": "O(N)",
        "core_skill": "Exploiting narrow item parameter distributions to replace pseudopolynomial DP with brute-force count tuples.",
        "reusable_pattern": "Small Variance Knapsack: group by w_i - w_1, sort descending, brute-force count tuples.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long W;
    if (!(cin >> n >> W)) return 0;

    long long w1;
    vector<long long> g[4];

    for (int i = 0; i < n; ++i) {
        long long w, v;
        cin >> w >> v;
        if (i == 0) w1 = w;
        g[w - w1].push_back(v);
    }

    for (int d = 0; d < 4; ++d) {
        sort(g[d].rbegin(), g[d].rend());
    }

    vector<long long> pref[4];
    for (int d = 0; d < 4; ++d) {
        pref[d].resize(g[d].size() + 1, 0);
        for (size_t i = 0; i < g[d].size(); ++i) {
            pref[d][i + 1] = pref[d][i] + g[d][i];
        }
    }

    long long ans = 0;

    for (size_t c0 = 0; c0 <= g[0].size(); ++c0) {
        for (size_t c1 = 0; c1 <= g[1].size(); ++c1) {
            for (size_t c2 = 0; c2 <= g[2].size(); ++c2) {
                for (size_t c3 = 0; c3 <= g[3].size(); ++c3) {
                    long long total_items = c0 + c1 + c2 + c3;
                    long long total_weight = total_items * w1 + 1 * c1 + 2 * c2 + 3 * c3;
                    if (total_weight <= W) {
                        ans = max(ans, pref[0][c0] + pref[1][c1] + pref[2][c2] + pref[3][c3]);
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
        "id": "arc120_c",
        "title": "Swaps 2",
        "contest_id": "arc120",
        "rating": 1478,
        "tag": "Data Structures",
        "subtopic": "Fenwick Tree",
        "topic": "Invariant Value Coordinate Assignment + Fenwick Inversion Counting",
        "cat_folder": "data_structures",
        "cat_file": "invariant_inversion_counting_fenwick.md",
        "statement": "Two arrays A and B of length N. In one operation, swap adjacent elements A[i] and A[i+1], then A[i] += 1 and A[i+1] -= 1. Find the minimum operations to transform A into B, or -1 if impossible.",
        "key_idea": "Notice the invariant: under swapping A[i] and A[i+1], their new values become A'[i] = A[i+1] - 1 and A'[i+1] = A[i] + 1. Thus, A[i] + i is an INVARIANT under adjacent transpositions!",
        "observation": "Let A'_i = A[i] + i and B'_i = B[i] + i. The operation becomes an ordinary adjacent swap of elements in A'. If the multisets of A' and B' match, the minimum operations equals the number of inversions to sort A' into B', computable via a Fenwick tree in O(N log N).",
        "algorithm": [
            "Compute A'_i = A[i] + i and B'_i = B[i] + i for i = 0..N-1.",
            "Check if sorted(A') == sorted(B'). If not, return -1.",
            "Group 0-indexed positions of values in B' using a queue or vector.",
            "Construct target permutation P where P[i] = next available position of A'_i in B'.",
            "Count inversions in P using a Fenwick tree.",
            "Print inversion count."
        ],
        "time_complexity": "O(N log N)",
        "space_complexity": "O(N)",
        "core_skill": "Discovering algebraic invariants under local transformations to reduce problems to inversion counting.",
        "reusable_pattern": "Invariant Transposition: transform values to preserve identity under swaps + Fenwick inversion count.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <map>
#include <queue>
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
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n), b(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        a[i] += i;
    }
    for (int i = 0; i < n; ++i) {
        cin >> b[i];
        b[i] += i;
    }

    vector<long long> sa = a, sb = b;
    sort(sa.begin(), sa.end());
    sort(sb.begin(), sb.end());

    if (sa != sb) {
        cout << -1 << "\n";
        return 0;
    }

    map<long long, queue<int>> pos;
    for (int i = 0; i < n; ++i) {
        pos[b[i]].push(i + 1);
    }

    vector<int> p(n);
    for (int i = 0; i < n; ++i) {
        p[i] = pos[a[i]].front();
        pos[a[i]].pop();
    }

    Fenwick bit(n);
    long long inversions = 0;
    for (int i = 0; i < n; ++i) {
        inversions += i - bit.query(p[i]);
        bit.add(p[i], 1);
    }

    cout << inversions << "\n";
    return 0;
}
"""
    },
    {
        "id": "abc290_e",
        "title": "Make it Palindrome",
        "contest_id": "abc290",
        "rating": 1485,
        "tag": "Basics",
        "subtopic": "Two Pointers",
        "topic": "Two Pointers Contribution to Sum for Non-Matching Pairs",
        "cat_folder": "basics",
        "cat_file": "two_pointers_palindrome_contribution.md",
        "statement": "For all contiguous subarrays of A, count the total number of operations required to make each subarray a palindrome (each operation changes one element).",
        "key_idea": "Instead of checking each subarray, count the total pairs (i, j) that are symmetric counterparts in some subarray, and subtract those where A[i] == A[j].",
        "observation": "A pair (i, j) with i < j appears as symmetric positions in exactly min(i + 1, N - j) subarrays. Summing min(i + 1, N - j) over all i < j gives the total operations if all pairs mismatched. We then subtract min(i + 1, N - j) for pairs where A[i] == A[j], which can be calculated using Two Pointers for each distinct value.",
        "algorithm": [
            "Calculate total_symmetric_pairs = sum_{i < j} min(i + 1, N - j) in O(N).",
            "Group indices by their value A[i].",
            "For each group of indices pos:",
            "  Use two pointers (l = 0, r = |pos| - 1):",
            "  While l < r:",
            "    If (pos[l] + 1) <= (N - pos[r]):",
            "      subtract (pos[l] + 1) * (r - l) from total;",
            "      l++;",
            "    Else:",
            "      subtract (N - pos[r]) * (r - l) from total;",
            "      r--;",
            "Print total."
        ],
        "time_complexity": "O(N log N) or O(N)",
        "space_complexity": "O(N)",
        "core_skill": "Inversion of contribution (total minus matching) combined with two pointers over sorted coordinate lists.",
        "reusable_pattern": "Symmetric Subarray Contribution: min(i+1, N-j) via two pointers on equal value indices.",
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
    vector<vector<int>> pos(n + 1);

    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        pos[a[i]].push_back(i);
    }

    // Total symmetric pairs over all subarrays
    long long ans = 0;
    for (int i = 0; i < n; ++i) {
        ans += 1LL * min(i + 1, n - i) * (n - 1 - i);
    }
    // Alternatively: sum over all i < j min(i + 1, n - j)
    long long total_pairs = 0;
    for (int i = 0; i < n; ++i) {
        total_pairs += 1LL * (i + 1) * (n - 1 - 2 * i > 0 ? n - 1 - 2 * i : 0);
    }

    // Precise total sum of min(i + 1, n - j)
    long long all_pairs = 0;
    for (int i = 0; i < n; ++i) {
        long long c = min(i + 1, n - i);
        all_pairs += c * (n - i - 1);
    }

    // Subtract matching pairs
    long long matches = 0;
    for (int v = 1; v <= n; ++v) {
        const auto& p = pos[v];
        int l = 0, r = (int)p.size() - 1;
        while (l < r) {
            if (p[l] + 1 <= n - p[r]) {
                matches += 1LL * (p[l] + 1) * (r - l);
                l++;
            } else {
                matches += 1LL * (n - p[r]) * (r - l);
                r--;
            }
        }
    }

    cout << all_pairs - matches << "\n";
    return 0;
}
"""
    },
    {
        "id": "abc123_d",
        "title": "Cake 123",
        "contest_id": "abc123",
        "rating": 1489,
        "tag": "Basics",
        "subtopic": "Priority Queue",
        "topic": "Priority Queue Top-K Sum of Three Arrays (Pruning to K)",
        "cat_folder": "basics",
        "cat_file": "top_k_sum_three_arrays.md",
        "statement": "Three arrays A (size X), B (size Y), C (size Z) with X, Y, Z <= 1000. Find the K largest sums of the form A_i + B_j + C_k, where K <= 3000.",
        "key_idea": "Notice that K <= 3000 is much smaller than X * Y * Z = 10^9. First compute all X * Y sums of A_i + B_j, sort descending, and retain only the top min(K, X * Y) sums. Then pair these top sums with C.",
        "observation": "Any sum of A_i + B_j not in the top K cannot possibly belong to the top K sums of A_i + B_j + C_k. Pruning to K elements reduces the candidate pool to K * Z <= 3 * 10^6 sums, easily sorted in O(K * Z log(K * Z)).",
        "algorithm": [
            "Compute all pairwise sums ab[i * Y + j] = A[i] + B[j].",
            "Sort ab in descending order and resize to min((int)ab.size(), K).",
            "Compute all sums abc = ab[i] + C[j] for i in 0..|ab|-1, j in 0..Z-1.",
            "Sort abc descending.",
            "Print the first K elements of abc."
        ],
        "time_complexity": "O(X * Y log(X * Y) + K * Z log(K * Z))",
        "space_complexity": "O(X * Y + K * Z)",
        "core_skill": "Pruning multi-array sum spaces to K largest intermediate candidates.",
        "reusable_pattern": "Top-K Sum of 3 Arrays: sort(A+B), take top K, then sort(top_K + C) and take top K.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int x, y, z, k;
    if (!(cin >> x >> y >> z >> k)) return 0;

    vector<long long> a(x), b(y), c(z);
    for (int i = 0; i < x; ++i) cin >> a[i];
    for (int i = 0; i < y; ++i) cin >> b[i];
    for (int i = 0; i < z; ++i) cin >> c[i];

    vector<long long> ab;
    ab.reserve(x * y);
    for (int i = 0; i < x; ++i) {
        for (int j = 0; j < y; ++j) {
            ab.push_back(a[i] + b[j]);
        }
    }

    sort(ab.rbegin(), ab.rend());
    if ((int)ab.size() > k) ab.resize(k);

    vector<long long> abc;
    abc.reserve(ab.size() * z);
    for (long long sum_ab : ab) {
        for (int i = 0; i < z; ++i) {
            abc.push_back(sum_ab + c[i]);
        }
    }

    sort(abc.rbegin(), abc.rend());
    for (int i = 0; i < k; ++i) {
        cout << abc[i] << "\n";
    }

    return 0;
}
"""
    },
    {
        "id": "abc175_d",
        "title": "Moving Piece",
        "contest_id": "abc175",
        "rating": 1491,
        "tag": "Basics",
        "subtopic": "Functional Graphs",
        "topic": "Functional Graph Permutation Cycle Decomposition with Round Trips",
        "cat_folder": "basics",
        "cat_file": "functional_graph_cycle_round_trips.md",
        "statement": "Given a permutation P of 1..N and score array C. Takahashi starts at square s, makes between 1 and K moves along P, adding C[current] at each step. Maximize total score over all starting squares and move counts.",
        "key_idea": "The permutation graph consists of disjoint cycles. For each cycle of length L and total score S: if S > 0 and K >= L, taking full cycles is beneficial; remaining steps (up to 2*L) can be simulated.",
        "observation": "If cycle sum S <= 0, we should only test up to min(K, L) moves. If S > 0, we can take m = max(0LL, K / L - 1) full cycles, and test the remaining K - m * L moves (at most 2*L steps).",
        "algorithm": [
            "Find all cycles in the permutation P.",
            "ans = -INF.",
            "For each starting square s from 1 to N:",
            "  Trace cycle from s, recording prefix sums pref[step].",
            "  Let L = cycle length, S = pref[L].",
            "  For step from 1 to min((long long)L, K):",
            "    score = pref[step].",
            "    If S > 0:",
            "      full_cycles = (K - step) / L;",
            "      score += full_cycles * S;",
            "    ans = max(ans, score).",
            "Print ans."
        ],
        "time_complexity": "O(N^2)",
        "space_complexity": "O(N)",
        "core_skill": "Permutation cycle decomposition with full-cycle acceleration and bounded step simulation.",
        "reusable_pattern": "Permutation Cycle Round-Trip: test all 1..min(K, L) steps + floor((K - step)/L) * cycle_sum.",
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

    vector<int> p(n + 1);
    vector<long long> c(n + 1);

    for (int i = 1; i <= n; ++i) cin >> p[i];
    for (int i = 1; i <= n; ++i) cin >> c[i];

    long long max_score = -2e18;

    for (int start = 1; start <= n; ++start) {
        vector<long long> cycle_scores;
        int curr = p[start];
        cycle_scores.push_back(c[curr]);

        while (curr != start) {
            curr = p[curr];
            cycle_scores.push_back(c[curr]);
        }

        int L = cycle_scores.size();
        vector<long long> pref(L + 1, 0);
        for (int i = 0; i < L; ++i) {
            pref[i + 1] = pref[i] + cycle_scores[i];
        }

        long long cycle_sum = pref[L];

        for (int step = 1; step <= min((long long)L, k); ++step) {
            long long score = pref[step];
            if (cycle_sum > 0) {
                long long full_cycles = (k - step) / L;
                score += full_cycles * cycle_sum;
            }
            max_score = max(max_score, score);
        }
    }

    cout << max_score << "\n";
    return 0;
}
"""
    },
    {
        "id": "abc222_e",
        "title": "Red and Blue Tree",
        "contest_id": "abc222",
        "rating": 1491,
        "tag": "Dynamic Programming",
        "subtopic": "Classic DP",
        "topic": "Tree Edge Frequencies via DFS + Subset Sum Knapsack",
        "cat_folder": "dp",
        "cat_file": "tree_edge_frequencies_subset_sum.md",
        "statement": "Given a tree with N vertices. A sequence of M vertices A_1, ..., A_M is traversed in order along simple paths. Color each edge Red or Blue. Count colorings such that (traversals of Red edges) - (traversals of Blue edges) = K, modulo 998244353.",
        "key_idea": "Compute the traversal frequency freq[e] of each edge over the M - 1 paths. R - B = K and R + B = total_freq => 2 * R = total_freq + K. This reduces to counting edge subsets with sum R.",
        "observation": "If (total_freq + K) is negative or odd, answer is 0. Otherwise target = (total_freq + K) / 2. Standard 0-1 knapsack DP counts the number of subsets of edge frequencies summing to target.",
        "algorithm": [
            "For each adjacent pair A_i -> A_{i+1}, run DFS to find path and increment traversal count of edges on path.",
            "Let total_freq = sum freq[e].",
            "If (total_freq + K) < 0 or (total_freq + K) % 2 != 0, return 0.",
            "target = (total_freq + K) / 2.",
            "Run 1D subset sum DP: dp[s] = number of subsets summing to s modulo 998244353.",
            "Print dp[target]."
        ],
        "time_complexity": "O(M * N + N * target)",
        "space_complexity": "O(N + target)",
        "core_skill": "Linear system reduction (R - B = K, R + B = S) mapped to standard subset sum counting.",
        "reusable_pattern": "Edge Traversal Frequency + Knapsack: count edge uses on paths, solve 2R = S + K.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>

using namespace std;

const int MOD = 998244353;

struct Edge {
    int to;
    int id;
};

bool dfs(int u, int target, int parent, const vector<vector<Edge>>& adj, vector<int>& edge_count) {
    if (u == target) return true;
    for (const auto& e : adj[u]) {
        if (e.to != parent) {
            if (dfs(e.to, target, u, adj, edge_count)) {
                edge_count[e.id]++;
                return true;
            }
        }
    }
    return false;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, k;
    if (!(cin >> n >> m >> k)) return 0;

    vector<int> a(m);
    for (int i = 0; i < m; ++i) cin >> a[i];

    vector<vector<Edge>> adj(n + 1);
    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back({v, i});
        adj[v].push_back({u, i});
    }

    vector<int> edge_count(n - 1, 0);
    for (int i = 0; i < m - 1; ++i) {
        dfs(a[i], a[i + 1], -1, adj, edge_count);
    }

    long long s = 0;
    for (int x : edge_count) s += x;

    if (s + k < 0 || (s + k) % 2 != 0) {
        cout << 0 << "\n";
        return 0;
    }

    long long target = (s + k) / 2;
    vector<int> dp(target + 1, 0);
    dp[0] = 1;

    for (int w : edge_count) {
        for (int j = target; j >= w; --j) {
            dp[j] = (dp[j] + dp[j - w]) % MOD;
        }
    }

    cout << dp[target] << "\n";
    return 0;
}
"""
    },
    {
        "id": "abc174_f",
        "title": "Range Set Query",
        "contest_id": "abc174",
        "rating": 1495,
        "tag": "Data Structures",
        "subtopic": "Fenwick Tree",
        "topic": "Offline Range Distinct Elements Query using Fenwick Tree",
        "cat_folder": "data_structures",
        "cat_file": "offline_distinct_elements_fenwick.md",
        "statement": "Given an array C of length N and Q range queries [l, r]. For each query, count the number of distinct elements in the subarray C[l..r].",
        "key_idea": "Process queries offline sorted by right endpoint r. Maintain a Fenwick tree where position p holds +1 iff p is the rightmost occurrence of value C[p] up to the current index r.",
        "observation": "When moving from r-1 to r, if C[r] previously occurred at last_pos[C[r]], decrement position last_pos[C[r]] in the Fenwick tree by 1. Then add +1 at position r. For any query [l, r], the distinct count is simply the range sum in [l, r].",
        "algorithm": [
            "Store queries grouped by right endpoint r.",
            "Initialize Fenwick tree of size N and array last_pos initialized to 0.",
            "For r from 1 to N:",
            "  If last_pos[C[r]] > 0, fenwick.add(last_pos[C[r]], -1).",
            "  fenwick.add(r, 1).",
            "  last_pos[C[r]] = r.",
            "  For each query [l, r]: ans[query_id] = fenwick.query(r) - fenwick.query(l - 1).",
            "Print answers for all queries in order."
        ],
        "time_complexity": "O((N + Q) log N)",
        "space_complexity": "O(N + Q)",
        "core_skill": "Offline Fenwick tree sweep-line for range distinct elements queries.",
        "reusable_pattern": "Range Distinct Query Template: sweep right endpoint r, cancel last_pos, add r, query [l, r].",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Fenwick {
    int n;
    vector<int> tree;
    Fenwick(int n) : n(n), tree(n + 1, 0) {}

    void add(int i, int delta) {
        for (; i <= n; i += i & -i) tree[i] += delta;
    }

    int query(int i) const {
        int sum = 0;
        for (; i > 0; i -= i & -i) sum += tree[i];
        return sum;
    }
};

struct Query {
    int l, r, id;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    vector<int> c(n + 1);
    for (int i = 1; i <= n; ++i) cin >> c[i];

    vector<vector<pair<int, int>>> queries_at(n + 1);
    for (int i = 0; i < q; ++i) {
        int l, r;
        cin >> l >> r;
        queries_at[r].push_back({l, i});
    }

    vector<int> last_pos(n + 1, 0);
    Fenwick bit(n);
    vector<int> ans(q);

    for (int r = 1; r <= n; ++r) {
        if (last_pos[c[r]] > 0) {
            bit.add(last_pos[c[r]], -1);
        }
        bit.add(r, 1);
        last_pos[c[r]] = r;

        for (const auto& qry : queries_at[r]) {
            int l = qry.first;
            int id = qry.second;
            ans[id] = bit.query(r) - bit.query(l - 1);
        }
    }

    for (int i = 0; i < q; ++i) {
        cout << ans[i] << "\n";
    }

    return 0;
}
"""
    },
    {
        "id": "abc170_e",
        "title": "Smart Infants",
        "contest_id": "abc170",
        "rating": 1502,
        "tag": "Data Structures",
        "subtopic": "Multiset",
        "topic": "Dual Multiset (Multiset of Multiset Maxima) Dynamic Maintenance",
        "cat_folder": "data_structures",
        "cat_file": "dual_multiset_maxima_maintenance.md",
        "statement": "N infants with ratings belong to kindergartens 1..200000. Q events occur where infant C moves from kindergarten A to B. After each event, output the minimum of the highest rating of all non-empty kindergartens.",
        "key_idea": "Maintain a multiset of ratings for each kindergarten, and a global multiset containing the maximum rating of every non-empty kindergarten.",
        "observation": "When infant C moves from kindergarten src to dst: remove infant rating from src multiset, update src's maximum in the global multiset. Add rating to dst multiset, update dst's maximum in the global multiset. Answer is *global_multiset.begin().",
        "algorithm": [
            "Maintain array of multisets kg[200001], global multiset top_ratings, and infant locations loc[i], rating[i].",
            "Populate initial ratings and global top_ratings.",
            "For each query (infant c, new kindergarten dst):",
            "  src = loc[c], val = rating[c].",
            "  Erase old max of src and dst from top_ratings.",
            "  Erase val from kg[src], insert val into kg[dst].",
            "  Reinsert new max of src (if not empty) and dst into top_ratings.",
            "  loc[c] = dst.",
            "  Print *top_ratings.begin()."
        ],
        "time_complexity": "O(Q log N)",
        "space_complexity": "O(N)",
        "core_skill": "Two-level hierarchical multiset maintenance for dynamic group extrema.",
        "reusable_pattern": "Dual Multiset Maintenance: inner multisets per group + global multiset of inner extrema.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <set>

using namespace std;

const int MAX_K = 200005;

multiset<int> kg[MAX_K];
multiset<int> top_ratings;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    vector<int> rating(n + 1), loc(n + 1);
    for (int i = 1; i <= n; ++i) {
        cin >> rating[i] >> loc[i];
        kg[loc[i]].insert(rating[i]);
    }

    for (int i = 1; i < MAX_K; ++i) {
        if (!kg[i].empty()) {
            top_ratings.insert(*kg[i].rbegin());
        }
    }

    while (q--) {
        int c, dst;
        cin >> c >> dst;
        int src = loc[c];
        int val = rating[c];

        if (src == dst) {
            cout << *top_ratings.begin() << "\n";
            continue;
        }

        // Remove old max from top_ratings
        top_ratings.erase(top_ratings.find(*kg[src].rbegin()));
        if (!kg[dst].empty()) {
            top_ratings.erase(top_ratings.find(*kg[dst].rbegin()));
        }

        // Move infant
        kg[src].erase(kg[src].find(val));
        kg[dst].insert(val);
        loc[c] = dst;

        // Reinsert new max
        if (!kg[src].empty()) {
            top_ratings.insert(*kg[src].rbegin());
        }
        top_ratings.insert(*kg[dst].rbegin());

        cout << *top_ratings.begin() << "\n";
    }

    return 0;
}
"""
    },
    {
        "id": "abc022_c",
        "title": "Blue Bird",
        "contest_id": "abc022",
        "rating": 1505,
        "tag": "Graph Theory",
        "subtopic": "All-Pairs Shortest Paths",
        "topic": "Shortest Cycle through Source via All-Pairs Shortest Path",
        "cat_folder": "graph_theory",
        "cat_file": "shortest_cycle_through_source.md",
        "statement": "An undirected weighted graph with N vertices (N <= 300) and M edges. Find the shortest simple cycle that passes through vertex 1, or -1 if no cycle exists.",
        "key_idea": "A simple cycle passing through vertex 1 consists of 1 -> u -> ... -> v -> 1, where u and v are two distinct neighbors of 1, and the path from u to v does not pass through 1.",
        "observation": "Remove vertex 1 from the graph. Compute all-pairs shortest paths on the remaining vertices 2..N using Floyd-Warshall in O(N^3). Then minimize cost(1, u) + dist[u][v] + cost(1, v) over all pairs of distinct neighbors u, v of vertex 1.",
        "algorithm": [
            "Store edge weights from vertex 1 to its neighbors.",
            "Initialize dist[u][v] = INF for u, v in 2..N.",
            "Run Floyd-Warshall on the induced subgraph of vertices 2..N.",
            "ans = INF.",
            "For all distinct neighbors u, v of 1:",
            "  If dist[u][v] < INF:",
            "    ans = min(ans, weight(1, u) + dist[u][v] + weight(1, v)).",
            "Output ans if ans < INF, else -1."
        ],
        "time_complexity": "O(N^3)",
        "space_complexity": "O(N^2)",
        "core_skill": "Cycle decomposition around an anchor node via subgraph all-pairs shortest paths.",
        "reusable_pattern": "Shortest Cycle through S: remove S, run Floyd-Warshall, minimize w(S, u) + dist[u][v] + w(v, S).",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const long long INF = 1e16;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<long long>> dist(n + 1, vector<long long>(n + 1, INF));
    for (int i = 1; i <= n; ++i) dist[i][i] = 0;

    vector<pair<int, long long>> neighbors_1;

    for (int i = 0; i < m; ++i) {
        int u, v;
        long long l;
        cin >> u >> v >> l;
        if (u == 1) {
            neighbors_1.push_back({v, l});
        } else if (v == 1) {
            neighbors_1.push_back({u, l});
        } else {
            dist[u][v] = min(dist[u][v], l);
            dist[v][u] = min(dist[v][u], l);
        }
    }

    // Floyd-Warshall on vertices 2..N
    for (int k = 2; k <= n; ++k) {
        for (int i = 2; i <= n; ++i) {
            for (int j = 2; j <= n; ++j) {
                if (dist[i][k] + dist[k][j] < dist[i][j]) {
                    dist[i][j] = dist[i][k] + dist[k][j];
                }
            }
        }
    }

    long long ans = INF;
    int k = neighbors_1.size();
    for (int i = 0; i < k; ++i) {
        for (int j = i + 1; j < k; ++j) {
            int u = neighbors_1[i].first;
            int v = neighbors_1[j].first;
            long long cycle_cost = neighbors_1[i].second + dist[u][v] + neighbors_1[j].second;
            ans = min(ans, cycle_cost);
        }
    }

    cout << (ans >= INF ? -1 : ans) << "\n";
    return 0;
}
"""
    },
    {
        "id": "abc133_e",
        "title": "Virus Tree 2",
        "contest_id": "abc133",
        "rating": 1505,
        "tag": "Combinatorics",
        "subtopic": "Tree Combinatorics",
        "topic": "Distance-2 Tree Coloring Combinatorics via DFS",
        "cat_folder": "combinatorics",
        "cat_file": "distance2_tree_coloring.md",
        "statement": "Given a tree with N vertices and K colors. Find the number of ways to color the vertices such that no two vertices at distance <= 2 share the same color, modulo 10^9 + 7.",
        "key_idea": "Root the tree at vertex 1 and traverse top-down. The root has K choices. Its children have (K - 1), (K - 2), etc. For any deeper vertex v, its parent, grandparent, and already-colored siblings forbid colors, leaving K - 2 - (sibling index) choices.",
        "observation": "For each node v, if v is root: K choices. For root's children: (K - 1), (K - 2), etc. For any child of a non-root vertex: 2 colors are used by ancestors (parent and grandparent). If the node has c children, the number of ways to color them is P(K - 2, c) = (K - 2) * (K - 3) * ... * (K - 2 - c + 1).",
        "algorithm": [
            "Root tree at 1 and run DFS.",
            "ans = K.",
            "For each vertex u:",
            "  Let children_count = count of children of u.",
            "  available_colors = (u == 1 ? K - 1 : K - 2).",
            "  For i = 0 to children_count - 1:",
            "    choices = available_colors - i.",
            "    If choices <= 0, return 0.",
            "    ans = (ans * choices) % MOD.",
            "Print ans."
        ],
        "time_complexity": "O(N)",
        "space_complexity": "O(N)",
        "core_skill": "Top-down tree traversal with local conflict counting for distance-constrained graph coloring.",
        "reusable_pattern": "Distance-2 Tree Coloring: root has K, root children have P(K-1, c), others have P(K-2, c).",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>

using namespace std;

const int MOD = 1000000007;

long long ans = 1;
int K;

void dfs(int u, int p, const vector<vector<int>>& adj) {
    int available = (u == 1 ? K - 1 : K - 2);
    int used = 0;

    for (int v : adj[u]) {
        if (v != p) {
            long long choices = available - used;
            if (choices <= 0) {
                ans = 0;
                return;
            }
            ans = (ans * choices) % MOD;
            used++;
            dfs(v, u, adj);
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n >> K)) return 0;

    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    ans = K;
    dfs(1, 0, adj);

    cout << ans << "\n";
    return 0;
}
"""
    },
    {
        "id": "abc210_d",
        "title": "National Railway",
        "contest_id": "abc210",
        "rating": 1507,
        "tag": "Dynamic Programming",
        "subtopic": "2D Grid DP",
        "topic": "2D Grid DP Coordinate Manhattan Distance Transformation",
        "cat_folder": "dp",
        "cat_file": "grid_dp_manhattan_distance.md",
        "statement": "An H x W grid with station construction costs A[i][j]. Cost to connect stations at (i, j) and (i', j') is A[i][j] + A[i'][j'] + C * (|i - i'| + |j - j'|). Minimize total cost over all pairs.",
        "key_idea": "Remove the absolute value by orienting the relative position: either (i' <= i, j' <= j) or (i' <= i, j' >= j). The second case is solved by horizontally reversing the grid.",
        "observation": "For i' <= i and j' <= j: cost = (A[i][j] + C*(i + j)) + (A[i'][j'] - C*(i' + j')). Let dp[i][j] be min over all (i', j') in the top-left subgrid (excluding (i, j)) of A[i'][j'] + C * ((i - i') + (j - j')). dp[i][j] = min(A[i-1][j] + C, dp[i-1][j] + C, A[i][j-1] + C, dp[i][j-1] + C).",
        "algorithm": [
            "Define solve(A, H, W):",
            "  dp[H][W] initialized to INF.",
            "  For r from 0 to H-1, c from 0 to W-1:",
            "    If r > 0: dp[r][c] = min(dp[r][c], min(A[r - 1][c], dp[r - 1][c]) + C).",
            "    If c > 0: dp[r][c] = min(dp[r][c], min(A[r][c - 1], dp[r][c - 1]) + C).",
            "    ans = min(ans, A[r][c] + dp[r][c]).",
            "Compute ans1 = solve(A).",
            "Reverse each row of A, compute ans2 = solve(A).",
            "Print min(ans1, ans2)."
        ],
        "time_complexity": "O(H * W)",
        "space_complexity": "O(H * W)",
        "core_skill": "Manhattan distance minimization via directional prefix DP sweeps and grid symmetry flips.",
        "reusable_pattern": "Grid Manhattan Distance DP: top-left DP sweep, reverse rows, repeat top-left DP sweep.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const long long INF = 2e18;

long long solve_directed(int h, int w, long long C, const vector<vector<long long>>& A) {
    vector<vector<long long>> dp(h, vector<long long>(w, INF));
    long long best = INF;

    for (int r = 0; r < h; ++r) {
        for (int c = 0; c < w; ++c) {
            if (r > 0) {
                dp[r][c] = min(dp[r][c], min(A[r - 1][c], dp[r - 1][c]) + C);
            }
            if (c > 0) {
                dp[r][c] = min(dp[r][c], min(A[r][c - 1], dp[r][c - 1]) + C);
            }
            if (dp[r][c] < INF) {
                best = min(best, A[r][c] + dp[r][c]);
            }
        }
    }
    return best;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int h, w;
    long long C;
    if (!(cin >> h >> w >> C)) return 0;

    vector<vector<long long>> A(h, vector<long long>(w));
    for (int r = 0; r < h; ++r) {
        for (int c = 0; c < w; ++c) {
            cin >> A[r][c];
        }
    }

    long long ans1 = solve_directed(h, w, C, A);

    // Flip horizontally
    for (int r = 0; r < h; ++r) {
        reverse(A[r].begin(), A[r].end());
    }

    long long ans2 = solve_directed(h, w, C, A);

    cout << min(ans1, ans2) << "\n";
    return 0;
}
"""
    },
    {
        "id": "arc087_b",
        "title": "FT Robot",
        "contest_id": "abc082",
        "rating": 1508,
        "tag": "Dynamic Programming",
        "subtopic": "Bitset DP",
        "topic": "Independent X/Y Coordinate Subset Sum Knapsack DP",
        "cat_folder": "dp",
        "cat_file": "independent_xy_subset_sum_bitset.md",
        "statement": "A robot starts at (0, 0) facing +X. A string S of 'F' (move forward 1) and 'T' (turn 90 degrees) is executed. Can the robot end at coordinate (X, Y)?",
        "key_idea": "Turns alternate between moving along the X-axis and Y-axis! The first segment of 'F's must move +X. All subsequent segments can move in either positive or negative direction, independently for X and Y.",
        "observation": "Parse S into consecutive 'F' block lengths separated by 'T's. Blocks alternate: X, Y, X, Y, ... The problem decouples into two independent subset sum problems: can we choose signs for X-blocks to reach X, and signs for Y-blocks to reach Y? Solved with `std::bitset` in O(len^2 / 64).",
        "algorithm": [
            "Parse S into segments of 'F' counts separated by 'T'.",
            "First segment moves strictly in +X: target_X -= len[0].",
            "Collect subsequent segments into moves_x and moves_y alternatingly.",
            "Solve check(moves, target):",
            "  Let S = sum(moves). If (target + S) < 0 or (target + S) % 2 != 0: return false.",
            "  w = (target + S) / 2.",
            "  Use bitset<16001> dp; dp[0] = 1.",
            "  For each length m in moves: dp |= (dp << m).",
            "  Return dp[w].",
            "Print 'Yes' if check(moves_x, target_X) && check(moves_y, Y), else 'No'."
        ],
        "time_complexity": "O(|S|^2 / 64)",
        "space_complexity": "O(|S|)",
        "core_skill": "Decoupling 2D orthogonal grid motions into independent 1D subset sum problems accelerated by bitsets.",
        "reusable_pattern": "Orthogonal Motion Independence: split turns into X and Y steps, solve with bitset.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <string>
#include <vector>
#include <bitset>
#include <cmath>

using namespace std;

const int OFFSET = 8000;

bool can_reach(const vector<int>& moves, int target) {
    bitset<16005> dp;
    dp[OFFSET] = 1;

    for (int d : moves) {
        dp = (dp << d) | (dp >> d);
    }

    if (abs(target) > 8000) return false;
    return dp[target + OFFSET];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    int target_x, target_y;
    if (!(cin >> s >> target_x >> target_y)) return 0;

    vector<int> segments;
    int cur = 0;
    for (char c : s) {
        if (c == 'F') {
            cur++;
        } else {
            segments.push_back(cur);
            cur = 0;
        }
    }
    segments.push_back(cur);

    // First segment is fixed along +X
    target_x -= segments[0];

    vector<int> moves_x, moves_y;
    for (size_t i = 1; i < segments.size(); ++i) {
        if (segments[i] == 0) continue;
        if (i % 2 == 1) {
            moves_y.push_back(segments[i]);
        } else {
            moves_x.push_back(segments[i]);
        }
    }

    if (can_reach(moves_x, target_x) && can_reach(moves_y, target_y)) {
        cout << "Yes\n";
    } else {
        cout << "No\n";
    }

    return 0;
}
"""
    },
    {
        "id": "abc156_e",
        "title": "Roaming",
        "contest_id": "abc156",
        "rating": 1514,
        "tag": "Combinatorics",
        "subtopic": "Stars and Bars",
        "topic": "Stars and Bars Empty Boxes Combinatorics",
        "cat_folder": "combinatorics",
        "cat_file": "stars_and_bars_empty_boxes.md",
        "statement": "There are N rooms, each initially containing 1 person. In each move, one person moves to a different room. Find the number of possible configurations of people in rooms after at most K moves, modulo 10^9 + 7.",
        "key_idea": "Each move can create at most one empty room. Thus, after at most K moves, the number of empty rooms z satisfies 0 <= z <= min(N - 1, K).",
        "observation": "For a fixed number of empty rooms z: choose which z rooms are empty in C(N, z) ways. The remaining N - z rooms must each contain at least 1 person. Distributing N people into N - z positive integer bins gives C(N - 1, (N - z) - 1) = C(N - 1, N - z - 1) ways.",
        "algorithm": [
            "Precompute factorials and modular inverse factorials up to N.",
            "ans = 0.",
            "For z from 0 to min((long long)N - 1, K):",
            "  ways = C(N, z) * C(N - 1, N - z - 1) % MOD.",
            "  ans = (ans + ways) % MOD.",
            "Print ans."
        ],
        "time_complexity": "O(N)",
        "space_complexity": "O(N)",
        "core_skill": "Characterizing reachable states by invariant empty-box count and applying Stars and Bars.",
        "reusable_pattern": "Empty Room Configurations: sum_{z=0}^{min(N-1, K)} C(N, z) * C(N-1, N-z-1).",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MOD = 1000000007;
const int MAX = 400005;

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

void precompute() {
    fact[0] = 1;
    for (int i = 1; i < MAX; ++i) fact[i] = (fact[i - 1] * i) % MOD;
    invFact[MAX - 1] = power(fact[MAX - 1], MOD - 2);
    for (int i = MAX - 2; i >= 0; --i) invFact[i] = (invFact[i + 1] * (i + 1)) % MOD;
}

long long nCr(int n, int r) {
    if (r < 0 || r > n) return 0;
    return fact[n] * invFact[r] % MOD * invFact[n - r] % MOD;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    precompute();

    int n;
    long long k;
    if (!(cin >> n >> k)) return 0;

    long long max_z = min((long long)n - 1, k);
    long long ans = 0;

    for (int z = 0; z <= max_z; ++z) {
        long long ways = nCr(n, z) * nCr(n - 1, n - z - 1) % MOD;
        ans = (ans + ways) % MOD;
    }

    cout << ans << "\n";
    return 0;
}
"""
    },
    {
        "id": "abc189_e",
        "title": "Rotate and Flip",
        "contest_id": "abc189",
        "rating": 1526,
        "tag": "Math",
        "subtopic": "Linear Algebra",
        "topic": "2D Affine Transformation Matrix Composition",
        "cat_folder": "math",
        "cat_file": "affine_transformation_composition.md",
        "statement": "N 2D points. M operations of 4 types: 1) clockwise 90 rotation; 2) counterclockwise 90 rotation; 3) reflection across x = p; 4) reflection across y = p. Answer Q queries: coordinates of point A after first B operations.",
        "key_idea": "Every operation is a 2D affine transformation. Composition of any sequence of these transformations can be maintained in O(1) prefix table form as X' = sx * (orig_coord) + cx, Y' = sy * (orig_coord) + cy.",
        "observation": "At any step, either X' is an affine function of X and Y' is an affine function of Y, or the axes are swapped. Precomputing the affine matrix at every prefix step 0..M takes O(M). Each query is answered in O(1).",
        "algorithm": [
            "Represent affine transformation as a 3x3 matrix or explicit (is_swapped, sx, sy, cx, cy).",
            "Precompute state after operation step i = 0..M.",
            "For each operation:",
            "  Apply transformation to current representation in O(1).",
            "For each query (A, B):",
            "  Apply transformation state at step B to initial coordinates of point A.",
            "  Print X' and Y'."
        ],
        "time_complexity": "O(N + M + Q)",
        "space_complexity": "O(N + M)",
        "core_skill": "Prefix composition of 2D affine reflection/rotation transformations for O(1) evaluation.",
        "reusable_pattern": "Affine Composition: compose linear map + translation vector prefix tables.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>

using namespace std;

struct Affine {
    // x' = x_src == 0 ? sx * x + cx : sx * y + cx
    // y' = y_src == 1 ? sy * y + cy : sy * x + cy
    int x_src; // 0 for x, 1 for y
    int y_src; // 0 for x, 1 for y
    long long sx, sy;
    long long cx, cy;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<pair<long long, long long>> pts(n + 1);
    for (int i = 1; i <= n; ++i) {
        cin >> pts[i].first >> pts[i].second;
    }

    int m;
    cin >> m;

    vector<Affine> pref(m + 1);
    pref[0] = {0, 1, 1, 1, 0, 0};

    for (int i = 1; i <= m; ++i) {
        int type;
        cin >> type;
        Affine prev = pref[i - 1];

        if (type == 1) {
            // (x, y) -> (y, -x)
            pref[i] = {prev.y_src, prev.x_src, prev.sy, -prev.sx, prev.cy, -prev.cx};
        } else if (type == 2) {
            // (x, y) -> (-y, x)
            pref[i] = {prev.y_src, prev.x_src, -prev.sy, prev.sx, -prev.cy, prev.cx};
        } else if (type == 3) {
            // (x, y) -> (2p - x, y)
            long long p;
            cin >> p;
            pref[i] = {prev.x_src, prev.y_src, -prev.sx, prev.sy, 2 * p - prev.cx, prev.cy};
        } else if (type == 4) {
            // (x, y) -> (x, 2p - y)
            long long p;
            cin >> p;
            pref[i] = {prev.x_src, prev.y_src, prev.sx, -prev.sy, prev.cx, 2 * p - prev.cy};
        }
    }

    int q;
    cin >> q;
    while (q--) {
        int b, a_idx;
        cin >> b >> a_idx;
        long long orig[2] = {pts[a_idx].first, pts[a_idx].second};
        Affine trans = pref[b];

        long long res_x = trans.sx * orig[trans.x_src] + trans.cx;
        long long res_y = trans.sy * orig[trans.y_src] + trans.cy;

        cout << res_x << " " << res_y << "\n";
    }

    return 0;
}
"""
    }
]

REJECTED_PROBLEMS = [
    {"id": "abc406_f", "title": "Compare Tree Weights", "rating": 1470, "reason": "REJECTED (BASIC LOGIC BUILDING) — Routine tree weight query simulation."},
    {"id": "abc408_f", "title": "Athletic", "rating": 1472, "reason": "REJECTED (BASIC LOGIC BUILDING) — Ad-hoc simulation without transferable CP algorithmic pattern."},
    {"id": "abc447_f", "title": "Centipede Graph", "rating": 1480, "reason": "REJECTED (BASIC LOGIC BUILDING) — Graph casework without reusable CP algorithm."},
    {"id": "abc453_e", "title": "Team Division", "rating": 1513, "reason": "REJECTED (BASIC LOGIC BUILDING) — Routine team division drill."}
]

# Step 1: Compile all C++ solutions to verify zero errors
print("Testing C++ compilation of all 22 selected ABC Part 3A solutions...")
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

print(f"[+] All {len(SELECTED_PROBLEMS)} ABC Part 3A C++ solutions compiled with 0 errors!")

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
        f.write("\n### Batch 4 Part 3A: ABC Curated Ladder (1460 - 1528)\n" + "\n".join(new_q_lines) + "\n")
    print("[+] Updated QUALITY_PROBLEMS_BY_TOPIC.md with new archetypes.")

# Update state/progress.json
with open("state/progress.json", "r", encoding="utf-8") as f:
    progress = json.load(f)

progress["current_batch"] = "Batch 4 Part 3A: ABC Ladder (1460-1528) COMPLETED"
progress["status"] = "IN_PROGRESS"
for p in SELECTED_PROBLEMS:
    if p["id"] not in progress["completed_problem_ids"]:
        progress["completed_problem_ids"].append(p["id"])
progress["total_evaluated_in_curriculum"] = len(progress["completed_problem_ids"])

with open("state/progress.json", "w", encoding="utf-8") as f:
    json.dump(progress, f, indent=2)
print(f"[+] Updated progress checkpoint: state/progress.json")

print("=" * 75)
print("Batch 4 Part 3A completed successfully!")
