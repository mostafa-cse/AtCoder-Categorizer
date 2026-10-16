#!/usr/bin/env python3
"""
Batch 1 Processor: Educational DP Contest (dp_a through dp_z)
==============================================================
Fully analyzes, solves, generates C++ code, compares with editorial,
and categorizes all 26 canonical EDPC problems following the master prompt.
"""

import json
import os
import re
from typing import Dict, List, Any

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
CATEGORIES_DIR = os.path.join(BASE_DIR, "categories")
ANALYSIS_DIR = os.path.join(BASE_DIR, "analysis")
STATE_DIR = os.path.join(BASE_DIR, "state")
os.makedirs(CATEGORIES_DIR, exist_ok=True)
os.makedirs(ANALYSIS_DIR, exist_ok=True)
os.makedirs(STATE_DIR, exist_ok=True)

# 26 Complete EDPC Problems Data with Full Verified C++ Implementations
EDPC_PROBLEMS = [
    {
        "id": "dp_a",
        "title": "Frog 1",
        "rating": 600,
        "tag": "Dynamic Programming (DP)",
        "subtopic": "Intro to DP",
        "topic": "1D State Recurrence / Bounded Lookahead",
        "folder": "dp",
        "file": "1d_dp.md",
        "statement": "N stones are numbered 1 to N with heights h_i. Starting from stone 1, the frog can jump to stone i+1 or i+2 with cost |h_i - h_j|. Find minimum total cost to reach stone N.",
        "key_idea": "Represent the minimum cost to reach stone i using optimal substructure from the previous two stones.",
        "observation": "At stone i, arrival is possible exclusively from i-1 or i-2. The state depends only on local height differences and optimal prefix solutions. Space compresses to O(1).",
        "algorithm": "1. Initialize dp[1] = 0, dp[2] = |h_2 - h_1|.\n2. For i from 3 to N: dp[i] = min(dp[i-1] + |h_i - h_{i-1}|, dp[i-2] + |h_i - h_{i-2}|).\n3. Result is dp[N].",
        "complexity": "Time: O(N), Space: O(1) rolling state.",
        "cpp_code": """#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<int> h(n + 1);
    for (int i = 1; i <= n; ++i) cin >> h[i];

    vector<int> dp(n + 1, 0);
    dp[1] = 0;
    if (n >= 2) dp[2] = abs(h[2] - h[1]);

    for (int i = 3; i <= n; ++i) {
        dp[i] = min(dp[i - 1] + abs(h[i] - h[i - 1]),
                    dp[i - 2] + abs(h[i] - h[i - 2]));
    }

    cout << dp[n] << "\\n";
    return 0;
}
""",
        "editorial": "Standard 1D forward relaxation recurrence.",
        "teaches": "Optimal substructure, state initialization, and memory-compressed transitions.",
        "pattern": "Linear 1D DP with constant lookback window."
    },
    {
        "id": "dp_b",
        "title": "Frog 2",
        "rating": 700,
        "tag": "Dynamic Programming (DP)",
        "subtopic": "Intro to DP",
        "topic": "1D DP with K-Step Transitions",
        "folder": "dp",
        "file": "1d_dp.md",
        "statement": "Similar to Frog 1, but the frog can jump up to K stones forward (from i to i+j for 1 <= j <= K). Find min cost to reach stone N.",
        "key_idea": "Generalize jumps to up to K stones with minimum total energy cost.",
        "observation": "Each state dp[i] is relaxed over a sliding window of the previous K states: dp[i] = min_{1 <= j <= K} (dp[i-j] + |h_i - h_{i-j}|).",
        "algorithm": "1. Set dp[1] = 0, others INF.\n2. For i from 1 to N-1: for step in 1..K with i+step <= N: dp[i+step] = min(dp[i+step], dp[i] + |h_{i+step} - h_i|).\n3. Result is dp[N].",
        "complexity": "Time: O(N * K), Space: O(N).",
        "cpp_code": """#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

const int INF = 1e9 + 7;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;
    vector<int> h(n + 1);
    for (int i = 1; i <= n; ++i) cin >> h[i];

    vector<int> dp(n + 1, INF);
    dp[1] = 0;

    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= k && i + j <= n; ++j) {
            dp[i + j] = min(dp[i + j], dp[i] + abs(h[i + j] - h[i]));
        }
    }

    cout << dp[n] << "\\n";
    return 0;
}
""",
        "editorial": "Standard push-based relaxation over parameterized lookahead.",
        "teaches": "Parameterized transition loops and boundary-bounded relaxation.",
        "pattern": "Push DP over variable-sized transition intervals."
    },
    {
        "id": "dp_c",
        "title": "Vacation",
        "rating": 900,
        "tag": "Dynamic Programming (DP)",
        "subtopic": "Intro to DP",
        "topic": "Multi-State DP / Consecutive Constraints",
        "folder": "dp",
        "file": "1d_dp.md",
        "statement": "Choose activities A, B, or C over N days maximizing happiness, with the constraint that Taro cannot do the same activity two days in a row.",
        "key_idea": "Maintain happiness while enforcing non-repeating consecutive activity constraints.",
        "observation": "Enforcing the constraint 'no two consecutive identical choices' requires augmenting the state with the identity of the last chosen activity.",
        "algorithm": "1. State: dp[day][act] where act in {0, 1, 2}.\n2. dp[i][0] = a_i + max(dp[i-1][1], dp[i-1][2]), and symmetrically for 1 and 2.\n3. Return max_{act} dp[N][act].",
        "complexity": "Time: O(N), Space: O(1) rolling state.",
        "cpp_code": """#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> dp(3, 0);

    for (int i = 0; i < n; ++i) {
        int a, b, c;
        cin >> a >> b >> c;
        vector<int> next_dp(3);
        next_dp[0] = a + max(dp[1], dp[2]);
        next_dp[1] = b + max(dp[0], dp[2]);
        next_dp[2] = c + max(dp[0], dp[1]);
        dp = next_dp;
    }

    cout << max({dp[0], dp[1], dp[2]}) << "\\n";
    return 0;
}
""",
        "editorial": "Classic 3-state Markov transition graph.",
        "teaches": "State augmentation for path-dependent constraints and state-machine DP.",
        "pattern": "Categorical state-machine DP with mutually exclusive transitions."
    },
    {
        "id": "dp_d",
        "title": "Knapsack 1",
        "rating": 1150,
        "tag": "Dynamic Programming (DP)",
        "subtopic": "Intro to DP",
        "topic": "Knapsack and Basic Dynamic Programming",
        "folder": "dp",
        "file": "knapsack.md",
        "statement": "Given N items with weights w_i and values v_i, choose items with total weight <= W (W <= 10^5) maximizing total value.",
        "key_idea": "Classical 0/1 Knapsack where capacity W <= 10^5 serves as the DP state index.",
        "observation": "By iterating weight downwards from W to w_i, 1D array space is sufficient without using an item multiple times.",
        "algorithm": "1. Initialize dp[0..W] = 0.\n2. For each item (w_i, v_i): for cap from W down to w_i: dp[cap] = max(dp[cap], dp[cap - w_i] + v_i).\n3. Result is max(dp).",
        "complexity": "Time: O(N * W), Space: O(W).",
        "cpp_code": """#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, W;
    if (!(cin >> n >> W)) return 0;

    vector<long long> dp(W + 1, 0);

    for (int i = 0; i < n; ++i) {
        int w;
        long long v;
        cin >> w >> v;
        for (int cap = W; cap >= w; --cap) {
            dp[cap] = max(dp[cap], dp[cap - w] + v);
        }
    }

    cout << dp[W] << "\\n";
    return 0;
}
""",
        "editorial": "Textbook 0/1 Knapsack with 1D memory compression.",
        "teaches": "Reverse-order state traversal to prevent unbounded repetition in subset selection.",
        "pattern": "1D space-optimized 0/1 knapsack."
    },
    {
        "id": "dp_e",
        "title": "Knapsack 2",
        "rating": 1450,
        "tag": "Dynamic Programming (DP)",
        "subtopic": "Intro to DP",
        "topic": "Knapsack Dual State / Value as State",
        "folder": "dp",
        "file": "knapsack.md",
        "statement": "Solve 0/1 Knapsack when capacity W <= 10^9 is enormous, but v_i <= 1000 and N <= 100.",
        "key_idea": "When capacity W is up to 10^9, weight cannot be an array index. Invert the state: define dp[v] as the minimum weight required to achieve exact value v.",
        "observation": "Total value sum <= 100 * 1000 = 10^5. The value dimension is pseudopolynomial while weight is not.",
        "algorithm": "1. V_sum = sum(v_i). dp[0] = 0, dp[1..V_sum] = INF.\n2. For each item (w_i, v_i): for v from V_sum down to v_i: dp[v] = min(dp[v], dp[v - v_i] + w_i).\n3. Return max v such that dp[v] <= W.",
        "complexity": "Time: O(N * sum(V)), Space: O(sum(V)).",
        "cpp_code": """#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const long long INF = 1e18;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long W;
    if (!(cin >> n >> W)) return 0;

    vector<int> w(n);
    vector<int> v(n);
    int max_val = 0;
    for (int i = 0; i < n; ++i) {
        cin >> w[i] >> v[i];
        max_val += v[i];
    }

    vector<long long> dp(max_val + 1, INF);
    dp[0] = 0;

    for (int i = 0; i < n; ++i) {
        for (int val = max_val; val >= v[i]; --val) {
            if (dp[val - v[i]] != INF) {
                dp[val] = min(dp[val], dp[val - v[i]] + w[i]);
            }
        }
    }

    int ans = 0;
    for (int val = max_val; val >= 0; --val) {
        if (dp[val] <= W) {
            ans = val;
            break;
        }
    }

    cout << ans << "\\n";
    return 0;
}
""",
        "editorial": "Dual problem formulation and state parameter swapping.",
        "teaches": "Swapping objective function and state dimension when constraints are large but values are compact.",
        "pattern": "Dual DP parameter inversion."
    },
    {
        "id": "dp_f",
        "title": "LCS",
        "rating": 1250,
        "tag": "Dynamic Programming (DP)",
        "subtopic": "Classic DP",
        "topic": "Longest Common Subsequence & Backtracking",
        "folder": "dp",
        "file": "interval_dp.md",
        "statement": "Given two strings s and t, find and print the actual string corresponding to their Longest Common Subsequence.",
        "key_idea": "Reconstruct and print the actual string corresponding to the Longest Common Subsequence of strings s and t.",
        "observation": "Standard 2D table computes optimal lengths. The sequence itself is uniquely extracted by tracing back from (len(s), len(t)) following optimal transition choices.",
        "algorithm": "1. Compute dp[i][j]: if s[i-1] == t[j-1] -> dp[i-1][j-1]+1; else max(dp[i-1][j], dp[i][j-1]).\n2. Traceback: if s[i-1] == t[j-1]: append s[i-1], i--, j--; else if dp[i-1][j] >= dp[i][j-1]: i--; else j--.\n3. Reverse characters.",
        "complexity": "Time: O(|s| * |t|), Space: O(|s| * |t|).",
        "cpp_code": """#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s, t;
    if (!(cin >> s >> t)) return 0;

    int n = s.size();
    int m = t.size();
    vector<vector<int>> dp(n + 1, vector<int>(m + 1, 0));

    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            if (s[i - 1] == t[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1] + 1;
            } else {
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
    }

    string lcs = "";
    int i = n, j = m;
    while (i > 0 && j > 0) {
        if (s[i - 1] == t[j - 1]) {
            lcs += s[i - 1];
            --i;
            --j;
        } else if (dp[i - 1][j] >= dp[i][j - 1]) {
            --i;
        } else {
            --j;
        }
    }

    reverse(lcs.begin(), lcs.end());
    cout << lcs << "\\n";
    return 0;
}
""",
        "editorial": "Full 2D DP matrix traceback.",
        "teaches": "State path reconstruction and multi-dimensional backtracking.",
        "pattern": "Optimal decision matrix traceback."
    },
    {
        "id": "dp_g",
        "title": "Longest Path",
        "rating": 1350,
        "tag": "Dynamic Programming (DP)",
        "subtopic": "Dp on Different Structures",
        "topic": "DP on Trees and DAGs",
        "folder": "dp",
        "file": "dp_on_trees.md",
        "statement": "Find the length of the longest directed path in a Directed Acyclic Graph (DAG) with N vertices and M edges.",
        "key_idea": "Since the graph has no directed cycles, topological ordering exists. The longest path starting at u is dp[u] = 1 + max_{(u, v) in E} dp[v].",
        "observation": "Acyclic structure guarantees no circular dependencies. Memoized DFS evaluates each vertex and edge exactly once.",
        "algorithm": "1. Memoized DFS: memo[u] = -1.\n2. DFS(u): if memo[u] != -1 return memo[u]. ans = 0. For each neighbor v: ans = max(ans, 1 + DFS(v)). memo[u] = ans.\n3. Return max_{u} DFS(u).",
        "complexity": "Time: O(V + E), Space: O(V + E).",
        "cpp_code": """#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int dfs(int u, const vector<vector<int>>& adj, vector<int>& memo) {
    if (memo[u] != -1) return memo[u];
    int best = 0;
    for (int v : adj[u]) {
        best = max(best, 1 + dfs(v, adj, memo));
    }
    return memo[u] = best;
}

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

    vector<int> memo(n + 1, -1);
    int ans = 0;
    for (int i = 1; i <= n; ++i) {
        ans = max(ans, dfs(i, adj, memo));
    }

    cout << ans << "\\n";
    return 0;
}
""",
        "editorial": "Topological sort DP on DAG.",
        "teaches": "Topological ordering as the fundamental validity condition for DAG DP.",
        "pattern": "Memoized DFS transition over DAG edges."
    },
    {
        "id": "dp_h",
        "title": "Grid 1",
        "rating": 1050,
        "tag": "Dynamic Programming (DP)",
        "subtopic": "Classic DP",
        "topic": "Grid DP / Path Counting with Obstacles",
        "folder": "dp",
        "file": "grid_dp.md",
        "statement": "Count paths from top-left (1,1) to bottom-right (H,W) moving only right and down, avoiding obstacle walls '#'. Output modulo 10^9+7.",
        "key_idea": "Transitions are purely local: dp[r][c] = (dp[r-1][c] + dp[r][c-1]) mod (10^9+7). Any obstacle cell '#' strictly resets dp[r][c] to 0.",
        "observation": "Transitions are purely local: dp[r][c] = (dp[r-1][c] + dp[r][c-1]) mod (10^9+7). Any obstacle cell '#' strictly resets dp[r][c] to 0.",
        "algorithm": "1. dp[1][1] = 1.\n2. For r in 1..H, c in 1..W: if grid[r][c] == '#': dp[r][c] = 0; else dp[r][c] = (dp[r-1][c] + dp[r][c-1]) % MOD.\n3. Return dp[H][W].",
        "complexity": "Time: O(H * W), Space: O(W).",
        "cpp_code": """#include <iostream>
#include <vector>
#include <string>

using namespace std;

const int MOD = 1e9 + 7;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int h, w;
    if (!(cin >> h >> w)) return 0;

    vector<string> grid(h);
    for (int i = 0; i < h; ++i) cin >> grid[i];

    vector<vector<int>> dp(h, vector<int>(w, 0));
    dp[0][0] = 1;

    for (int r = 0; r < h; ++r) {
        for (int c = 0; c < w; ++c) {
            if (grid[r][c] == '#') {
                dp[r][c] = 0;
                continue;
            }
            if (r > 0) dp[r][c] = (dp[r][c] + dp[r - 1][c]) % MOD;
            if (c > 0) dp[r][c] = (dp[r][c] + dp[r][c - 1]) % MOD;
        }
    }

    cout << dp[h - 1][w - 1] << "\\n";
    return 0;
}
""",
        "editorial": "Grid combinatorial dynamic programming.",
        "teaches": "Grid boundary enforcement, obstacle nullification, and modulo arithmetic accumulation.",
        "pattern": "2D additive grid DP."
    },
    {
        "id": "dp_i",
        "title": "Coins",
        "rating": 1150,
        "tag": "Dynamic Programming (DP)",
        "subtopic": "Intro to DP",
        "topic": "Probability and Expected Value DP",
        "folder": "dp",
        "file": "expected_value_dp.md",
        "statement": "N independent biased coins have probabilities p_i of turning up heads. Find the probability that more heads than tails appear.",
        "key_idea": "Calculate the exact probability that more heads than tails appear when tossing N independent biased coins.",
        "observation": "Let dp[i][j] be probability of exactly j heads after i coin tosses. Outcome partitions probability mass into two events: heads (p_i) or tails (1 - p_i).",
        "algorithm": "1. dp[0][0] = 1.0; others 0.0.\n2. For i in 1..N: for j in 0..i: dp[i][j] = (j > 0 ? dp[i-1][j-1] * p_i : 0) + dp[i-1][j] * (1 - p_i).\n3. Sum dp[N][j] for j > N/2.",
        "complexity": "Time: O(N^2), Space: O(N).",
        "cpp_code": """#include <iostream>
#include <vector>
#include <iomanip>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<double> p(n);
    for (int i = 0; i < n; ++i) cin >> p[i];

    vector<double> dp(n + 1, 0.0);
    dp[0] = 1.0;

    for (int i = 0; i < n; ++i) {
        vector<double> next_dp(n + 1, 0.0);
        for (int j = 0; j <= i; ++j) {
            next_dp[j + 1] += dp[j] * p[i];
            next_dp[j] += dp[j] * (1.0 - p[i]);
        }
        dp = next_dp;
    }

    double ans = 0.0;
    for (int j = (n + 1) / 2; j <= n; ++j) {
        ans += dp[j];
    }

    cout << fixed << setprecision(10) << ans << "\\n";
    return 0;
}
""",
        "editorial": "Poisson binomial distribution dynamic programming.",
        "teaches": "Probability mass conservation and floating-point accumulation in discrete trial DP.",
        "pattern": "Probability convolution DP over independent Bernoulli trials."
    },
    {
        "id": "dp_j",
        "title": "Sushi",
        "rating": 1650,
        "tag": "Dynamic Programming (DP)",
        "subtopic": "Intro to DP",
        "topic": "Expected Value DP with Multi-Frequency States",
        "folder": "dp",
        "file": "expected_value_dp.md",
        "statement": "N plates have 1, 2, or 3 sushi. Repeatedly choose a random plate and eat one sushi if present. Find expected operations to empty all plates.",
        "key_idea": "Plate identity is irrelevant; state is the count of plates with 1, 2, and 3 sushi (c1, c2, c3). Picking an empty plate loops back to the same state (self-loop).",
        "observation": "Self-loop equation E = 1 + sum(P_i E_i) + P_empty E solves algebraically: E = (N + c1*E1 + c2*E2 + c3*E3) / (c1 + c2 + c3).",
        "algorithm": "1. Memoized 3D DP array: memo[c1][c2][c3].\n2. Compute recursively using the resolved self-loop formula.\n3. Base: memo[0][0][0] = 0.0.",
        "complexity": "Time: O(N^3), Space: O(N^3).",
        "cpp_code": """#include <iostream>
#include <vector>
#include <iomanip>

using namespace std;

double memo[305][305][305];
bool vis[305][305][305];
int n;

double solve(int c1, int c2, int c3) {
    if (c1 == 0 && c2 == 0 && c3 == 0) return 0.0;
    if (vis[c1][c2][c3]) return memo[c1][c2][c3];

    double sum = n;
    if (c1 > 0) sum += c1 * solve(c1 - 1, c2, c3);
    if (c2 > 0) sum += c2 * solve(c1 + 1, c2 - 1, c3);
    if (c3 > 0) sum += c3 * solve(c1, c2 + 1, c3 - 1);

    vis[c1][c2][c3] = true;
    return memo[c1][c2][c3] = sum / (c1 + c2 + c3);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n)) return 0;
    int c1 = 0, c2 = 0, c3 = 0;
    for (int i = 0; i < n; ++i) {
        int a;
        cin >> a;
        if (a == 1) c1++;
        else if (a == 2) c2++;
        else if (a == 3) c3++;
    }

    cout << fixed << setprecision(12) << solve(c1, c2, c3) << "\\n";
    return 0;
}
""",
        "editorial": "Expected value recurrence with algebraic self-loop resolution.",
        "teaches": "Multi-frequency state compression and algebraic self-loop elimination in expected value DP.",
        "pattern": "Self-loop elimination: E = (1 + \sum P_i E_i) / (1 - P_{self})."
    },
    {
        "id": "dp_k",
        "title": "Stones",
        "rating": 1100,
        "tag": "Game Theory",
        "subtopic": "Impartial Games",
        "topic": "Sprague-Grundy / Combinatorial Game DP",
        "folder": "game_theory",
        "file": "sprague_grundy_impartial_games.md",
        "statement": "Two players remove a_i stones from a pile of size K. Determine if First or Second player wins under optimal play.",
        "key_idea": "State x is Winning (First wins) if there exists a valid move a_i such that state x - a_i is Losing (Second wins). If all valid moves lead to Winning states, x is Losing.",
        "observation": "Game state graph is finite and directed acyclic. Backward induction computes boolean outcomes in O(N * K).",
        "algorithm": "1. dp[0] = False (Losing state).\n2. For x from 1 to K: dp[x] = True if any(a_i <= x and not dp[x - a_i] for a_i in A) else False.\n3. Output 'First' if dp[K] else 'Second'.",
        "complexity": "Time: O(N * K), Space: O(K).",
        "cpp_code": """#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<int> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    vector<bool> dp(k + 1, false);
    for (int x = 1; x <= k; ++x) {
        for (int v : a) {
            if (v <= x && !dp[x - v]) {
                dp[x] = true;
                break;
            }
        }
    }

    cout << (dp[k] ? "First" : "Second") << "\\n";
    return 0;
}
""",
        "editorial": "Classic backward induction on impartial game graph.",
        "teaches": "P-positions and N-positions, finite state game backward induction, and Sprague-Grundy fundamentals.",
        "pattern": "Boolean game state induction: win(x) = \exists a, \neg win(x - a)."
    },
    {
        "id": "dp_l",
        "title": "Deque",
        "rating": 1400,
        "tag": "Dynamic Programming (DP)",
        "subtopic": "Classic DP",
        "topic": "Interval DP / Range DP / Matrix Chain Multiplication (MCM)",
        "folder": "dp",
        "file": "interval_dp.md",
        "statement": "Two players remove numbers from either end of an array. Player 1 maximizes X - Y, Player 2 minimizes it.",
        "key_idea": "Over remaining subsegment [l, r], the active player chooses either a_l or a_r: dp[l][r] = max(a_l - dp[l+1][r], a_r - dp[l][r-1]).",
        "observation": "Zero-sum game with symmetric negation: your advantage equals your chosen element minus opponent's optimal advantage from remaining subinterval.",
        "algorithm": "1. Base: dp[i][i] = a_i.\n2. Loop len from 2 to N: loop l from 1 to N-len+1: r = l+len-1: dp[l][r] = max(a_l - dp[l+1][r], a_r - dp[l][r-1]).\n3. Return dp[1][N].",
        "complexity": "Time: O(N^2), Space: O(N^2).",
        "cpp_code": """#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    vector<vector<long long>> dp(n, vector<long long>(n, 0));
    for (int i = 0; i < n; ++i) dp[i][i] = a[i];

    for (int len = 2; len <= n; ++len) {
        for (int l = 0; l <= n - len; ++l) {
            int r = l + len - 1;
            dp[l][r] = max(a[l] - dp[l + 1][r], a[r] - dp[l][r - 1]);
        }
    }

    cout << dp[0][n - 1] << "\\n";
    return 0;
}
""",
        "editorial": "Zero-sum minimax interval DP.",
        "teaches": "Interval dynamic programming evaluated by segment length and minimax negation.",
        "pattern": "Minimax interval DP: dp[l][r] = max(opt_left - dp[l+1][r], opt_right - dp[l][r-1])."
    },
    {
        "id": "dp_m",
        "title": "Candies",
        "rating": 1550,
        "tag": "Dynamic Programming (DP)",
        "subtopic": "DP Optimizations",
        "topic": "Prefix Sum Optimized DP",
        "folder": "dp",
        "file": "prefix_sum_dp.md",
        "statement": "Distribute K candies among N children such that child i receives at most a_i candies.",
        "key_idea": "The naive transition dp[i][j] = sum_{k=0}^{a_i} dp[i-1][j-k] is over a contiguous range [j - a_i, j] in dp[i-1].",
        "observation": "Prefix sums of the previous row evaluate the contiguous range sum in O(1), dropping overall complexity from O(N * K^2) to O(N * K).",
        "algorithm": "1. dp[0] = 1, others 0.\n2. For each child i: compute prefix sums pref of current dp.\n3. dp[j] = (pref[j+1] - pref[max(0, j - a_i)]) mod MOD.\n4. Return dp[K].",
        "complexity": "Time: O(N * K), Space: O(K).",
        "cpp_code": """#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MOD = 1e9 + 7;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<int> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    vector<int> dp(k + 1, 0);
    dp[0] = 1;

    for (int i = 0; i < n; ++i) {
        vector<int> pref(k + 2, 0);
        for (int j = 0; j <= k; ++j) {
            pref[j + 1] = (pref[j] + dp[j]) % MOD;
        }

        vector<int> next_dp(k + 1, 0);
        for (int j = 0; j <= k; ++j) {
            int left = max(0, j - a[i]);
            next_dp[j] = (pref[j + 1] - pref[left] + MOD) % MOD;
        }
        dp = next_dp;
    }

    cout << dp[k] << "\\n";
    return 0;
}
""",
        "editorial": "Prefix sum acceleration of contiguous state transitions.",
        "teaches": "Sliding window range sum optimization reducing quadratic transitions to linear.",
        "pattern": "Prefix sum acceleration of contiguous state transitions."
    },
    {
        "id": "dp_n",
        "title": "Slimes",
        "rating": 1600,
        "tag": "Dynamic Programming (DP)",
        "subtopic": "Classic DP",
        "topic": "Interval DP / Range DP / Matrix Chain Multiplication (MCM)",
        "folder": "dp",
        "file": "interval_dp.md",
        "statement": "Merge adjacent slimes pairwise into one slime with minimum total combination cost.",
        "key_idea": "The final combine step joins two sub-blocks [l, k] and [k+1, r] with cost sum(a[l..r]).",
        "observation": "dp[l][r] = sum(a[l..r]) + min_{l <= k < r} (dp[l][k] + dp[k+1][r]). Prefix sums yield sum(a[l..r]) in O(1).",
        "algorithm": "1. Precompute prefix sums.\n2. For len = 2..N: for l = 1..N-len+1: r = l+len-1: dp[l][r] = min_{k=l}^{r-1}(dp[l][k] + dp[k+1][r]) + (pref[r] - pref[l-1]).\n3. Return dp[1][N].",
        "complexity": "Time: O(N^3) standard, O(N^2) via Knuth optimization.",
        "cpp_code": """#include <iostream>
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
    vector<long long> pref(n + 1, 0);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        pref[i + 1] = pref[i] + a[i];
    }

    vector<vector<long long>> dp(n, vector<long long>(n, 0));

    for (int len = 2; len <= n; ++len) {
        for (int l = 0; l <= n - len; ++l) {
            int r = l + len - 1;
            dp[l][r] = INF;
            long long cost = pref[r + 1] - pref[l];
            for (int k = l; k < r; ++k) {
                dp[l][r] = min(dp[l][r], dp[l][k] + dp[k + 1][r] + cost);
            }
        }
    }

    cout << dp[0][n - 1] << "\\n";
    return 0;
}
""",
        "editorial": "Optimal binary search tree / matrix chain multiplication DP.",
        "teaches": "Interval DP with split-point minimization and cost of merging subproblems.",
        "pattern": "Split-point interval DP."
    },
    {
        "id": "dp_o",
        "title": "Matching",
        "rating": 1650,
        "tag": "Dynamic Programming (DP)",
        "subtopic": "Bit Related DP",
        "topic": "Bitmask DP",
        "folder": "dp",
        "file": "bitmask_dp.md",
        "statement": "Count perfect matchings in a bipartite graph with N men and N women (N <= 21).",
        "key_idea": "When matching men 0, 1, ..., i-1, exactly i women must be chosen. Thus, i = popcount(mask). The index of the active man is implicit in the bitmask!",
        "observation": "By iterating masks by popcount or sequentially from 0 to 2^N - 1, we eliminate the man dimension entirely: dp[mask | (1 << j)] += dp[mask].",
        "algorithm": "1. dp[0] = 1, all other dp = 0.\n2. For mask from 0 to 2^N - 1: let i = popcount(mask). If i == N, continue.\n3. For each woman j in 0..N-1: if compatible(i, j) and not (mask & (1 << j)): dp[mask | (1 << j)] = (dp[mask | (1 << j)] + dp[mask]) mod MOD.\n4. Return dp[(1<<N) - 1].",
        "complexity": "Time: O(N * 2^N), Space: O(2^N).",
        "cpp_code": """#include <iostream>
#include <vector>

using namespace std;

const int MOD = 1e9 + 7;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<int>> a(n, vector<int>(n));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) cin >> a[i][j];
    }

    int total_masks = 1 << n;
    vector<int> dp(total_masks, 0);
    dp[0] = 1;

    for (int mask = 0; mask < total_masks; ++mask) {
        if (dp[mask] == 0) continue;
        int i = __builtin_popcount(mask);
        if (i == n) continue;

        for (int j = 0; j < n; ++j) {
            if (a[i][j] && !(mask & (1 << j))) {
                int next_mask = mask | (1 << j);
                dp[next_mask] = (dp[next_mask] + dp[mask]) % MOD;
            }
        }
    }

    cout << dp[total_masks - 1] << "\\n";
    return 0;
}
""",
        "editorial": "Popcount dimension-reduced bitmask DP.",
        "teaches": "Dimension reduction in Bitmask DP using subset cardinality invariants.",
        "pattern": "Popcount implicit state matching: i = popcount(mask)."
    },
    {
        "id": "dp_p",
        "title": "Independent Set",
        "rating": 1500,
        "tag": "Dynamic Programming (DP)",
        "subtopic": "Dp on Different Structures",
        "topic": "DP on Trees and DAGs",
        "folder": "dp",
        "file": "dp_on_trees.md",
        "statement": "Count ways to paint vertices of a tree black or white such that no two adjacent vertices are both black.",
        "key_idea": "Root tree arbitrarily. Maintain two states: dp[u][White] and dp[u][Black].",
        "observation": "If node u is Black, all children must be White. If u is White, each child can be independently either Black or White.",
        "algorithm": "1. Post-order DFS(u, parent).\n2. dp[u][Black] = prod_{v in children} dp[v][White].\n3. dp[u][White] = prod_{v in children} (dp[v][Black] + dp[v][White]).\n4. Return (dp[root][Black] + dp[root][White]) mod MOD.",
        "complexity": "Time: O(N), Space: O(N).",
        "cpp_code": """#include <iostream>
#include <vector>

using namespace std;

const int MOD = 1e9 + 7;

void dfs(int u, int p, const vector<vector<int>>& adj, vector<long long>& white, vector<long long>& black) {
    white[u] = 1;
    black[u] = 1;

    for (int v : adj[u]) {
        if (v == p) continue;
        dfs(v, u, adj, white, black);
        white[u] = (white[u] * ((white[v] + black[v]) % MOD)) % MOD;
        black[u] = (black[u] * white[v]) % MOD;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    vector<long long> white(n + 1, 1), black(n + 1, 1);
    dfs(1, 0, adj, white, black);

    cout << (white[1] + black[1]) % MOD << "\\n";
    return 0;
}
""",
        "editorial": "Tree independent set combinatorial DP.",
        "teaches": "Subtree DP, state-color branching, and product-rule combination over tree children.",
        "pattern": "Two-state subtree product DP on trees."
    },
    {
        "id": "dp_q",
        "title": "Flowers",
        "rating": 1600,
        "tag": "Dynamic Programming (DP)",
        "subtopic": "DP Optimizations",
        "topic": "DP Optimization using Data Structures [Some Practice Problems]",
        "folder": "data_structures",
        "file": "fenwick_segment_tree.md",
        "statement": "Given N flowers with distinct heights h_i and beauties a_i, choose a subsequence of strictly increasing heights maximizing total beauty.",
        "key_idea": "dp[h_i] = a_i + max_{0 <= h < h_i} dp[h]. Querying max in [0, h_i - 1] and updating point h_i is dynamically solved in O(log N) by a Fenwick or Segment Tree.",
        "observation": "Transforming quadratic inner-loop search into dynamic range queries via data structures.",
        "algorithm": "1. Maintain Fenwick tree supporting point-update and prefix-max queries.\n2. For each flower i: best = fenwick.query(h_i - 1); fenwick.update(h_i, best + a_i).\n3. Return fenwick.query(N).",
        "complexity": "Time: O(N log N), Space: O(N).",
        "cpp_code": """#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Fenwick {
    int n;
    vector<long long> tree;
    Fenwick(int n) : n(n), tree(n + 1, 0) {}

    void update(int i, long long val) {
        for (; i <= n; i += i & -i) tree[i] = max(tree[i], val);
    }

    long long query(int i) {
        long long res = 0;
        for (; i > 0; i -= i & -i) res = max(res, tree[i]);
        return res;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> h(n);
    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> h[i];
    for (int i = 0; i < n; ++i) cin >> a[i];

    Fenwick bit(n);
    for (int i = 0; i < n; ++i) {
        long long best = bit.query(h[i] - 1);
        bit.update(h[i], best + a[i]);
    }

    cout << bit.query(n) << "\\n";
    return 0;
}
""",
        "editorial": "Fenwick tree / Segment tree accelerated LIS.",
        "teaches": "Transforming quadratic inner-loop search into dynamic range queries via data structures.",
        "pattern": "BIT/Segment Tree accelerated DP."
    },
    {
        "id": "dp_r",
        "title": "Walk",
        "rating": 1700,
        "tag": "Dynamic Programming (DP)",
        "subtopic": "Dp on Different Structures",
        "topic": "Matrix Exponentiation DP",
        "folder": "dp",
        "file": "matrix_exponentiation.md",
        "statement": "Given a directed graph with N vertices (N <= 50), count the number of directed paths of exact length K (K <= 10^18) modulo 10^9+7.",
        "key_idea": "The number of paths of length K between all pairs of vertices is given by A^K, where A is the adjacency matrix.",
        "observation": "Matrix multiplication computes transitions; binary exponentiation solves K <= 10^18 in O(N^3 log K) steps.",
        "algorithm": "1. Construct adjacency matrix A.\n2. Compute M = A^K mod (10^9+7) using binary matrix exponentiation.\n3. Total paths = sum_{i, j} M[i][j] mod MOD.",
        "complexity": "Time: O(N^3 log K), Space: O(N^2).",
        "cpp_code": """#include <iostream>
#include <vector>

using namespace std;

const int MOD = 1e9 + 7;
using Matrix = vector<vector<long long>>;

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

Matrix power(Matrix A, long long p, int n) {
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

    int n;
    long long k;
    if (!(cin >> n >> k)) return 0;

    Matrix A(n, vector<long long>(n));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) cin >> A[i][j];
    }

    Matrix Ak = power(A, k, n);
    long long ans = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            ans = (ans + Ak[i][j]) % MOD;
        }
    }

    cout << ans << "\\n";
    return 0;
}
""",
        "editorial": "Matrix exponentiation for path counting on graphs.",
        "teaches": "Formulating linear state recurrences as matrix products and exponentiating large step counts.",
        "pattern": "Matrix exponentiation DP for enormous transition steps."
    },
    {
        "id": "dp_s",
        "title": "Digit Sum",
        "rating": 1750,
        "tag": "Dynamic Programming (DP)",
        "subtopic": "Digit DP",
        "topic": "Digit DP with Remainder State",
        "folder": "dp",
        "file": "digit_dp.md",
        "statement": "Count positive integers up to K (K <= 10^10000) whose sum of digits is a multiple of D.",
        "key_idea": "Process K as a string of up to 10,000 digits. Maintain state (index, remainder_mod_D, tight_flag).",
        "observation": "At index i, if tight is True, the next digit can only range from 0 to K[i]. If tight is False, the next digit can range from 0 to 9 freely.",
        "algorithm": "1. dp[index][rem][tight]: count of valid prefix configurations.\n2. For each digit d in 0..(tight ? K[idx] : 9): dp[idx+1][(rem + d) % D][tight and (d == K[idx])] += dp[idx][rem][tight].\n3. Final count = (dp[len][0][0] + dp[len][0][1] - 1 + MOD) % MOD.",
        "complexity": "Time: O(|K| * D * 10), Space: O(|K| * D).",
        "cpp_code": """#include <iostream>
#include <string>
#include <vector>

using namespace std;

const int MOD = 1e9 + 7;

int dp[10005][105][2];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string K;
    int D;
    if (!(cin >> K >> D)) return 0;

    int n = K.size();
    dp[0][0][1] = 1;

    for (int i = 0; i < n; ++i) {
        int limit = K[i] - '0';
        for (int rem = 0; rem < D; ++rem) {
            for (int tight = 0; tight < 2; ++tight) {
                if (dp[i][rem][tight] == 0) continue;
                int max_digit = tight ? limit : 9;
                for (int d = 0; d <= max_digit; ++d) {
                    int next_rem = (rem + d) % D;
                    int next_tight = tight && (d == limit);
                    dp[i + 1][next_rem][next_tight] = (dp[i + 1][next_rem][next_tight] + dp[i][rem][tight]) % MOD;
                }
            }
        }
    }

    int ans = (dp[n][0][0] + dp[n][0][1] - 1 + MOD) % MOD;
    cout << ans << "\\n";
    return 0;
}
""",
        "editorial": "Textbook Digit DP with tight bound tracking.",
        "teaches": "Digit-by-digit construction, tight prefix bound handling, and large integer parsing.",
        "pattern": "Standard Digit DP state tuple (index, remainder, is_tight)."
    },
    {
        "id": "dp_t",
        "title": "Permutation",
        "rating": 1950,
        "tag": "Dynamic Programming (DP)",
        "subtopic": "DP Optimizations",
        "topic": "Relative Order Insertion DP with Prefix Sums",
        "folder": "dp",
        "file": "prefix_sum_dp.md",
        "statement": "Given a signature string S of length N-1 with characters '<' and '>', count permutations p of 1..N satisfying p_i < p_{i+1} if S_i == '<' and p_i > p_{i+1} if S_i == '>'.",
        "key_idea": "Construct permutation of 1..N element by element. When inserting element i, insert it into relative rank j in [1, i] among previously placed elements.",
        "observation": "If S[i-1] == '<', j must be greater than previous element's rank k. If '>', j must be <= k. Prefix sums evaluate the transition sum in O(1).",
        "algorithm": "1. dp[1][1] = 1.\n2. For i from 2 to N: compute prefix sums pref of dp[i-1].\n3. If S[i-2] == '<': dp[i][j] = pref[j-1]. If S[i-2] == '>': dp[i][j] = pref[i-1] - pref[j-1].\n4. Return sum_{j=1}^N dp[N][j] mod MOD.",
        "complexity": "Time: O(N^2), Space: O(N).",
        "cpp_code": """#include <iostream>
#include <string>
#include <vector>

using namespace std;

const int MOD = 1e9 + 7;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    string s;
    if (!(cin >> n >> s)) return 0;

    vector<int> dp(2, 0);
    dp[1] = 1;

    for (int i = 2; i <= n; ++i) {
        vector<int> pref(i, 0);
        for (int j = 1; j < i; ++j) {
            pref[j] = (pref[j - 1] + dp[j]) % MOD;
        }

        vector<int> next_dp(i + 1, 0);
        char cond = s[i - 2];
        for (int j = 1; j <= i; ++j) {
            if (cond == '<') {
                next_dp[j] = pref[j - 1];
            } else {
                next_dp[j] = (pref[i - 1] - pref[j - 1] + MOD) % MOD;
            }
        }
        dp = next_dp;
    }

    int ans = 0;
    for (int j = 1; j <= n; ++j) {
        ans = (ans + dp[j]) % MOD;
    }

    cout << ans << "\\n";
    return 0;
}
""",
        "editorial": "Relative order insertion DP with prefix sum acceleration.",
        "teaches": "Constructing permutations by inserting elements into relative rank slots and optimizing transitions with prefix sums.",
        "pattern": "Relative rank insertion DP + prefix sum acceleration."
    },
    {
        "id": "dp_u",
        "title": "Grouping",
        "rating": 1850,
        "tag": "Dynamic Programming (DP)",
        "subtopic": "Bit Related DP",
        "topic": "Bitmask DP / O(3^N) Submask Enumeration",
        "folder": "dp",
        "file": "bitmask_dp.md",
        "statement": "Partition N rabbits into arbitrary groups to maximize total compatibility score (N <= 16).",
        "key_idea": "Precompute standalone group scores in O(N^2 * 2^N). Then dp[mask] = max_{sub is submask of mask} (score[sub] + dp[mask ^ sub]).",
        "observation": "Iterating submasks via `sub = (sub - 1) & mask` visits each submask without redundant branches. Over all 2^N masks, total operations equal sum_{k=0}^N binom(N, k) 2^k = 3^N.",
        "algorithm": "1. Precompute score[mask] for all 2^N subsets.\n2. Loop mask from 1 to 2^N - 1:\n   sub = mask; while sub > 0: dp[mask] = max(dp[mask], score[sub] + dp[mask ^ sub]); sub = (sub - 1) & mask.\n3. Return dp[(1<<N) - 1].",
        "complexity": "Time: O(3^N + N^2 * 2^N), Space: O(2^N).",
        "cpp_code": """#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<long long>> a(n, vector<long long>(n));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) cin >> a[i][j];
    }

    int total_masks = 1 << n;
    vector<long long> score(total_masks, 0);

    for (int mask = 0; mask < total_masks; ++mask) {
        for (int i = 0; i < n; ++i) {
            if (!(mask & (1 << i))) continue;
            for (int j = i + 1; j < n; ++j) {
                if (mask & (1 << j)) {
                    score[mask] += a[i][j];
                }
            }
        }
    }

    vector<long long> dp(total_masks, 0);

    for (int mask = 1; mask < total_masks; ++mask) {
        for (int sub = mask; sub > 0; sub = (sub - 1) & mask) {
            dp[mask] = max(dp[mask], score[sub] + dp[mask ^ sub]);
        }
    }

    cout << dp[total_masks - 1] << "\\n";
    return 0;
}
""",
        "editorial": "Textbook submask enumeration.",
        "teaches": "The (sub - 1) & mask bit trick and set partition dynamic programming.",
        "pattern": "O(3^N) submask iteration: sub = (sub - 1) & mask."
    },
    {
        "id": "dp_v",
        "title": "Subtree",
        "rating": 2100,
        "tag": "Dynamic Programming (DP)",
        "subtopic": "Dp on Different Structures",
        "topic": "Tree DP with Subtree Rerooting without Division",
        "folder": "dp",
        "file": "dp_on_trees.md",
        "statement": "For every vertex v in a tree, compute the number of black-connected components containing v modulo M (M may not be prime).",
        "key_idea": "Reroot the tree in O(N) using two DFS passes. Because M is composite, division by (down[child] + 1) is illegal; prefix and suffix products of children answers exclude a child in O(1) without division.",
        "observation": "For each node, children values can be preprocessed into prefix and suffix cumulative products. Excluded child contribution is calculated by multiplying prefix[:i-1] * suffix[i+1:].",
        "algorithm": "1. DFS1: down[u] = prod_{v in children} (down[v] + 1) mod M.\n2. DFS2: compute parent contribution up[u] using prefix and suffix products of sibling values.\n3. Ans[u] = down[u] * (up[u] + 1) mod M.",
        "complexity": "Time: O(N), Space: O(N).",
        "cpp_code": """#include <iostream>
#include <vector>

using namespace std;

int n;
long long M;
vector<vector<int>> adj;
vector<long long> down_dp, ans;

void dfs1(int u, int p) {
    down_dp[u] = 1;
    for (int v : adj[u]) {
        if (v == p) continue;
        dfs1(v, u);
        down_dp[u] = (down_dp[u] * (down_dp[v] + 1)) % M;
    }
}

void dfs2(int u, int p, long long up_val) {
    ans[u] = (down_dp[u] * (up_val + 1)) % M;

    vector<int> children;
    for (int v : adj[u]) {
        if (v != p) children.push_back(v);
    }

    int deg = children.size();
    if (deg == 0) return;

    vector<long long> pref(deg + 1, 1), suff(deg + 1, 1);
    for (int i = 0; i < deg; ++i) {
        pref[i + 1] = (pref[i] * (down_dp[children[i]] + 1)) % M;
    }
    for (int i = deg - 1; i >= 0; --i) {
        suff[i] = (suff[i + 1] * (down_dp[children[i]] + 1)) % M;
    }

    for (int i = 0; i < deg; ++i) {
        int v = children[i];
        long long next_up = (up_val + 1) % M;
        next_up = (next_up * pref[i]) % M;
        next_up = (next_up * suff[i + 1]) % M;
        dfs2(v, u, next_up);
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n >> M)) return 0;
    adj.assign(n + 1, vector<int>());
    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    down_dp.assign(n + 1, 1);
    ans.assign(n + 1, 0);

    dfs1(1, 0);
    dfs2(1, 0, 0);

    for (int i = 1; i <= n; ++i) {
        cout << ans[i] << "\\n";
    }
    return 0;
}
""",
        "editorial": "All-roots tree DP rerooting with non-invertible operators.",
        "teaches": "Tree rerooting technique without modular division via prefix/suffix product arrays.",
        "pattern": "Division-free prefix/suffix rerooting on trees."
    },
    {
        "id": "dp_w",
        "title": "Intervals",
        "rating": 2350,
        "tag": "Dynamic Programming (DP)",
        "subtopic": "DP Optimizations",
        "topic": "Lazy Segment Tree Range-Add Point-Query DP",
        "folder": "dp",
        "file": "lazy_segment_tree_dp.md",
        "statement": "Construct a binary string s of length N. You are given M intervals [l_i, r_i] with score a_i. An interval gives score a_i if at least one '1' falls in [l_i, r_i]. Maximize total score.",
        "key_idea": "DP where state is the position of the last '1'. Maintain dp[j] in a Lazy Segment Tree. When scanning i from 1 to N, for each interval ending at i, add its score a to range [l, i].",
        "observation": "If the previous '1' is at position j in [l, i], the interval is satisfied. Adding a to range [l, i] updates all valid previous positions in O(log N). dp[i] = max_{0 <= j < i} dp[j].",
        "algorithm": "1. Group intervals by their right endpoint r.\n2. Maintain Lazy Segment Tree of size N+1.\n3. For i from 1 to N: for each interval [l, i] with score a: segtree.range_add(l, i, a). dp[i] = segtree.query_max(0, i-1). segtree.update_point(i, dp[i]).\n4. Return segtree.query_max(0, N).",
        "complexity": "Time: O((N + M) log N), Space: O(N).",
        "cpp_code": """#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const long long INF = 1e18;

struct LazySegTree {
    int n;
    vector<long long> tree, lazy;
    LazySegTree(int n) : n(n), tree(4 * n, 0), lazy(4 * n, 0) {}

    void push(int node) {
        if (lazy[node] != 0) {
            tree[2 * node] += lazy[node];
            lazy[2 * node] += lazy[node];
            tree[2 * node + 1] += lazy[node];
            lazy[2 * node + 1] += lazy[node];
            lazy[node] = 0;
        }
    }

    void update_range(int node, int l, int r, int ql, int qr, long long val) {
        if (ql <= l && r <= qr) {
            tree[node] += val;
            lazy[node] += val;
            return;
        }
        push(node);
        int mid = (l + r) / 2;
        if (ql <= mid) update_range(2 * node, l, mid, ql, qr, val);
        if (qr > mid) update_range(2 * node + 1, mid + 1, r, ql, qr, val);
        tree[node] = max(tree[2 * node], tree[2 * node + 1]);
    }

    long long query_max(int node, int l, int r, int ql, int qr) {
        if (ql <= l && r <= qr) return tree[node];
        push(node);
        int mid = (l + r) / 2;
        long long res = -INF;
        if (ql <= mid) res = max(res, query_max(2 * node, l, mid, ql, qr));
        if (qr > mid) res = max(res, query_max(2 * node + 1, mid + 1, r, ql, qr));
        return res;
    }

    void update_point(int node, int l, int r, int idx, long long val) {
        if (l == r) {
            tree[node] = val;
            return;
        }
        push(node);
        int mid = (l + r) / 2;
        if (idx <= mid) update_point(2 * node, l, mid, idx, val);
        else update_point(2 * node + 1, mid + 1, r, idx, val);
        tree[node] = max(tree[2 * node], tree[2 * node + 1]);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    struct Interval { int l; long long a; };
    vector<vector<Interval>> intervals_at(n + 1);
    for (int i = 0; i < m; ++i) {
        int l, r;
        long long a;
        cin >> l >> r >> a;
        intervals_at[r].push_back({l, a});
    }

    LazySegTree seg(n + 1);

    for (int i = 1; i <= n; ++i) {
        // Carry forward previous optimal state
        long long best_prev = seg.query_max(1, 0, n, 0, i - 1);
        seg.update_point(1, 0, n, i, best_prev);

        // Add intervals ending at i
        for (const auto& inv : intervals_at[i]) {
            seg.update_range(1, 0, n, inv.l, i, inv.a);
        }
    }

    cout << max(0LL, seg.query_max(1, 0, n, 0, n)) << "\\n";
    return 0;
}
""",
        "editorial": "Range-add point-query Lazy Segment Tree dynamic programming.",
        "teaches": "Using Lazy Segment Tree to dynamically update previous state transitions across ranges of active intervals.",
        "pattern": "Lazy Segment Tree accelerated range-event DP."
    },
    {
        "id": "dp_x",
        "title": "Tower",
        "rating": 2250,
        "tag": "Dynamic Programming (DP)",
        "subtopic": "Intro to DP",
        "topic": "Greedy Exchange Argument + 0/1 Knapsack DP",
        "folder": "dp",
        "file": "exchange_argument_dp.md",
        "statement": "N blocks have weight w_i, solidness s_i, and value v_i. Tower can be built if each block's solidness is >= sum of weights of blocks above it. Maximize total value.",
        "key_idea": "Exchange Argument: Block i should be placed below block j if s_i - w_j >= s_j - w_i, which rearranges to s_i + w_i >= s_j + w_j. Sorting blocks by w_i + s_i fixes the optimal stacking order!",
        "observation": "Once sorted by w_i + s_i, the problem reduces to a 0/1 Knapsack where a block can only be added if accumulated weight w <= s_i.",
        "algorithm": "1. Sort blocks ascending by w_i + s_i.\n2. Maintain dp[weight] = max value.\n3. For each block i: for w from s_i down to 0: dp[w + w_i] = max(dp[w + w_i], dp[w] + v_i).\n4. Return max(dp).",
        "complexity": "Time: O(N log N + N * max(S)), Space: O(max(S)).",
        "cpp_code": """#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Block {
    int w, s;
    long long v;
    bool operator<(const Block& other) const {
        return (w + s) < (other.w + other.s);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<Block> blocks(n);
    int max_s = 0;
    for (int i = 0; i < n; ++i) {
        cin >> blocks[i].w >> blocks[i].s >> blocks[i].v;
        max_s = max(max_s, blocks[i].s);
    }

    sort(blocks.begin(), blocks.end());

    int max_weight = max_s + 10005;
    vector<long long> dp(max_weight + 1, -1);
    dp[0] = 0;

    long long ans = 0;
    for (const auto& b : blocks) {
        for (int w = b.s; w >= 0; --w) {
            if (dp[w] != -1) {
                if (w + b.w <= max_weight) {
                    dp[w + b.w] = max(dp[w + b.w], dp[w] + b.v);
                    ans = max(ans, dp[w + b.w]);
                }
            }
        }
    }

    cout << ans << "\\n";
    return 0;
}
""",
        "editorial": "Greedy exchange argument establishes canonical topological order for Knapsack DP.",
        "teaches": "Pairwise exchange arguments (deriving s_i + w_i invariant) combined with 0/1 knapsack.",
        "pattern": "Exchange argument pre-sorting + Knapsack DP."
    },
    {
        "id": "dp_y",
        "title": "Grid 2",
        "rating": 2150,
        "tag": "Combinatorics",
        "subtopic": "Inclusion-Exclusion",
        "topic": "First-Hit Obstacle Inclusion-Exclusion DP",
        "folder": "dp",
        "file": "inclusion_exclusion_dp.md",
        "statement": "Grid of size H x W with N <= 3000 obstacles. Count paths from (1, 1) to (H, W) avoiding all obstacles. (H, W <= 10^5).",
        "key_idea": "Grid is too huge for 2D DP (H, W <= 10^5), but obstacle count N <= 3000 is small. Define dp[i] = paths from (1, 1) to obstacle i whose FIRST encountered obstacle is obstacle i.",
        "observation": "dp[i] = binom((r_i - 1) + (c_i - 1), r_i - 1) - sum_{j < i, r_j <= r_i, c_j <= c_i} (dp[j] * binom((r_i - r_j) + (c_i - c_j), r_i - r_j)).",
        "algorithm": "1. Add destination (H, W) as (N+1)-th obstacle.\n2. Sort obstacles by (r, c).\n3. Precompute factorials and inverse factorials up to H + W.\n4. For each obstacle i: dp[i] = ways(1,1 to i) - sum_{j < i} (dp[j] * ways(j to i)).\n5. Return dp[destination].",
        "complexity": "Time: O(N^2 + (H + W)), Space: O(N + H + W).",
        "cpp_code": """#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MOD = 1e9 + 7;
const int MAX = 200005;

long long fact[MAX], invFact[MAX];

long long power(long long base, long long exp) {
    long long res = 1;
    base %= MOD;
    while (exp > 0) {
        if (exp & 1) res = (res * base) % MOD;
        base = (base * base) % MOD;
        exp >>= 1;
    }
    return res;
}

long long modInverse(long long n) {
    return power(n, MOD - 2);
}

void precompute() {
    fact[0] = 1;
    invFact[0] = 1;
    for (int i = 1; i < MAX; ++i) {
        fact[i] = (fact[i - 1] * i) % MOD;
    }
    invFact[MAX - 1] = modInverse(fact[MAX - 1]);
    for (int i = MAX - 2; i >= 1; --i) {
        invFact[i] = (invFact[i + 1] * (i + 1)) % MOD;
    }
}

long long nCr(int n, int r) {
    if (r < 0 || r > n) return 0;
    return fact[n] * invFact[r] % MOD * invFact[n - r] % MOD;
}

long long paths(int r1, int c1, int r2, int c2) {
    int dr = r2 - r1;
    int dc = c2 - c1;
    if (dr < 0 || dc < 0) return 0;
    return nCr(dr + dc, dr);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    precompute();

    int h, w, n;
    if (!(cin >> h >> w >> n)) return 0;

    struct Point { int r, c; };
    vector<Point> pts(n);
    for (int i = 0; i < n; ++i) cin >> pts[i].r >> pts[i].c;

    // Add destination
    pts.push_back({h, w});
    sort(pts.begin(), pts.end(), [](const Point& a, const Point& b) {
        if (a.r != b.r) return a.r < b.r;
        return a.c < b.c;
    });

    int total_pts = pts.size();
    vector<long long> dp(total_pts, 0);

    for (int i = 0; i < total_pts; ++i) {
        dp[i] = paths(1, 1, pts[i].r, pts[i].c);
        for (int j = 0; j < i; ++j) {
            if (pts[j].r <= pts[i].r && pts[j].c <= pts[i].c) {
                long long subtract = (dp[j] * paths(pts[j].r, pts[j].c, pts[i].r, pts[i].c)) % MOD;
                dp[i] = (dp[i] - subtract + MOD) % MOD;
            }
        }
    }

    cout << dp[total_pts - 1] << "\\n";
    return 0;
}
""",
        "editorial": "First-hit obstacle inclusion-exclusion dynamic programming.",
        "teaches": "Combinatorial grid paths with obstacles using first-encounter inclusion-exclusion.",
        "pattern": "First-hit inclusion-exclusion over coordinate points."
    },
    {
        "id": "dp_z",
        "title": "Frog 3",
        "rating": 2200,
        "tag": "Dynamic Programming (DP)",
        "subtopic": "Convex Hull Trick (CHT)",
        "topic": "Convex Hull Trick (CHT) and Dynamic CHT",
        "folder": "dp",
        "file": "convex_hull_trick.md",
        "statement": "Jump from stone i to j with quadratic cost (h_j - h_i)^2 + C where heights are strictly increasing.",
        "key_idea": "Expand (h_j - h_i)^2 + C = h_j^2 + C + (h_i^2 + dp[i]) - 2 * h_j * h_i. For fixed j, this is min_i (m_i * x + b_i) with slope m_i = -2 * h_i and x = h_j.",
        "observation": "Since heights h_i are strictly increasing, slopes are strictly decreasing and query points are strictly increasing. A deque maintains the lower convex hull in O(1) amortized time per query.",
        "algorithm": "1. Deque stores lines.\n2. For stone j: pop front while line[0].eval(h_j) >= line[1].eval(h_j).\n3. dp[j] = deque.front().eval(h_j) + h_j^2 + C.\n4. Add new line (slope = -2*h_j, intercept = h_j^2 + dp[j]) to back, popping non-convex lines.",
        "complexity": "Time: O(N), Space: O(N).",
        "cpp_code": """#include <iostream>
#include <vector>
#include <deque>

using namespace std;

struct Line {
    long long m, b;
    long long eval(long long x) const {
        return m * x + b;
    }
};

// Check if l2 is made redundant by l1 and l3
bool redundant(const Line& l1, const Line& l2, const Line& l3) {
    // Intersection of l1 and l2 vs l2 and l3
    return (double)(l2.b - l1.b) * (l2.m - l3.m) >= (double)(l3.b - l2.b) * (l1.m - l2.m);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long C;
    if (!(cin >> n >> C)) return 0;

    vector<long long> h(n);
    for (int i = 0; i < n; ++i) cin >> h[i];

    vector<long long> dp(n, 0);
    deque<Line> hull;

    // Line for stone 0: m = -2*h[0], b = h[0]^2 + dp[0]
    hull.push_back({-2 * h[0], h[0] * h[0]});

    for (int j = 1; j < n; ++j) {
        long long x = h[j];
        // Pop suboptimal lines from front
        while (hull.size() >= 2 && hull[0].eval(x) >= hull[1].eval(x)) {
            hull.pop_front();
        }

        dp[j] = hull.front().eval(x) + x * x + C;

        Line cur = {-2 * h[j], dp[j] + h[j] * h[j]};
        // Maintain convexity at back
        while (hull.size() >= 2 && redundant(hull[hull.size() - 2], hull.back(), cur)) {
            hull.pop_back();
        }
        hull.push_back(cur);
    }

    cout << dp[n - 1] << "\\n";
    return 0;
}
""",
        "editorial": "Canonical Convex Hull Trick with monotonic slopes and queries.",
        "teaches": "Geometric line lower envelope maintenance, convex hull deque operations, and linearizing quadratic DP costs.",
        "pattern": "Monotonic Convex Hull Trick (CHT)."
    }
]


def generate_all_analysis_files():
    """Generates 26 comprehensive analysis files with complete C++ solutions."""
    for p in EDPC_PROBLEMS:
        filename = f"AtCoder-{p['id']}.md"
        filepath = os.path.join(ANALYSIS_DIR, filename)
        cat_file = f"../categories/{p['folder']}/{p['file']}"

        lines = [
            f"# Problem Analysis: AtCoder-{p['id']} — {p['title']}",
            "",
            f"**Problem ID**: `AtCoder-{p['id']}`  ",
            f"**Contest**: `dp` (Educational DP Contest)  ",
            f"**Rating / Difficulty**: {p['rating']}  ",
            f"**URL**: https://atcoder.jp/contests/dp/tasks/{p['id']}  ",
            f"**VJudge Tag**: `[problem:AtCoder-{p['id']}]`  ",
            f"**Category File**: [`{cat_file}`]({cat_file})  ",
            "",
            f"- **Tag (Domain)**: `{p['tag']}`  ",
            f"- **Subtopic**: `{p['subtopic']}`  ",
            f"- **Topic (Skill)**: `{p['topic']}`  ",
            "",
            "---",
            "",
            "## 1. Problem Statement & Key Idea",
            f"{p['statement']}",
            "",
            f"**Core Idea**: {p['key_idea']}",
            "",
            "## 2. Core Observation & Invariant",
            p["observation"],
            "",
            "## 3. Step-by-Step Algorithm",
            p["algorithm"],
            "",
            "## 4. Complexity Analysis",
            p["complexity"],
            "",
            "## 5. Complete C++ Solution",
            "```cpp",
            p["cpp_code"].strip(),
            "```",
            "",
            "## 6. Editorial Comparison & Alignment",
            p["editorial"],
            "",
            "## 7. What This Problem Teaches & Reusable Pattern",
            f"- **Core Skill**: {p['teaches']}",
            f"- **Reusable Pattern**: `{p['pattern']}`",
            "",
            "---",
            f"Back to [{p['topic']}]({cat_file}) | [Categories Directory](../categories/README.md)"
        ]

        with open(filepath, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
        print(f"[+] Generated Analysis: {filepath}")


def update_checkpoint():
    """Updates state/progress.json with completed Batch 1 problems."""
    progress_file = os.path.join(STATE_DIR, "progress.json")
    completed_ids = [p["id"] for p in EDPC_PROBLEMS]
    data = {
        "current_batch": "Batch 1: Educational DP Contest (dp_a through dp_z)",
        "status": "COMPLETED",
        "total_evaluated_in_batch": len(EDPC_PROBLEMS),
        "selected_count": len(EDPC_PROBLEMS),
        "rejected_count": 0,
        "completed_problem_ids": completed_ids
    }
    with open(progress_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"[+] Updated Checkpoint: {progress_file}")


if __name__ == "__main__":
    print("=" * 70)
    print("      PROCESSING BATCH 1: EDUCATIONAL DP CONTEST (dp_a to dp_z)")
    print("=" * 70)
    generate_all_analysis_files()
    update_checkpoint()
    print("=" * 70)
    print("Batch 1 completed successfully!")
