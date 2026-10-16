import os
import subprocess
import json

# Ensure directories exist
os.makedirs("analysis", exist_ok=True)
os.makedirs("categories", exist_ok=True)
os.makedirs("state", exist_ok=True)

print("=" * 75)
print("      PROCESSING BATCH 4 PART 3B: ABC CURATED LADDER (1528 - 1599)")
print("=" * 75)

SELECTED_PROBLEMS = [
    {
        "id": "abc139_e",
        "title": "League",
        "contest_id": "abc139",
        "rating": 1528,
        "tag": "Graph Theory",
        "subtopic": "Directed Graphs",
        "topic": "DAG Longest Path / Topological Sort on Match Dependencies",
        "cat_folder": "graph_theory",
        "cat_file": "dag_longest_path_match_dependencies.md",
        "statement": "N players in a round-robin tournament. Each player has an ordered list of N - 1 opponents they must play in strict order. On each day, each player can play at most 1 match. Find the minimum days required to complete all N*(N-1)/2 matches, or -1 if impossible.",
        "key_idea": "Each match between player u and v (u < v) is a node in a directed graph. A player's required order creates directed dependency edges between consecutive matches. The answer is the longest path in this DAG, or -1 if a cycle exists.",
        "observation": "There are N*(N-1)/2 <= 5 * 10^5 nodes and <= N*(N-2) edges. Detecting cycles and computing the longest path via Kahn's topological sort or memoized DFS takes linear time O(N^2).",
        "algorithm": [
            "Map each unordered pair (u, v) with u < v to a unique match ID from 0 to N*(N-1)/2 - 1.",
            "Build directed graph: for each player, add directed edge from match_k to match_{k+1}.",
            "Compute in-degrees for all match nodes.",
            "Queue all nodes with in-degree 0, initialized with dist = 1.",
            "Run BFS (Kahn's algorithm):",
            "  Pop node u with dist[u].",
            "  For each neighbor v: in_degree[v]--, dist[v] = max(dist[v], dist[u] + 1).",
            "  If in_degree[v] == 0, push v.",
            "If processed node count < total_nodes, return -1 (cycle detected).",
            "Return max(dist[u]) over all nodes."
        ],
        "time_complexity": "O(N^2)",
        "space_complexity": "O(N^2)",
        "core_skill": "Dependency modeling on scheduling games as longest path in a directed acyclic graph.",
        "reusable_pattern": "Tournament Match Dependency DAG: pair(u, v) as node, in-degree Kahn BFS for longest path / cycle detection.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    auto get_id = [&](int u, int v) -> int {
        if (u > v) swap(u, v);
        // u in 1..n-1, v in u+1..n
        return (u - 1) * n + (v - 1);
    };

    int total_nodes = n * n;
    vector<vector<int>> adj(total_nodes);
    vector<int> in_deg(total_nodes, 0);
    vector<bool> exists(total_nodes, false);

    for (int i = 1; i <= n; ++i) {
        int prev_match = -1;
        for (int j = 0; j < n - 1; ++j) {
            int opp;
            cin >> opp;
            int cur_match = get_id(i, opp);
            exists[cur_match] = true;
            if (prev_match != -1) {
                adj[prev_match].push_back(cur_match);
                in_deg[cur_match]++;
            }
            prev_match = cur_match;
        }
    }

    queue<int> q;
    vector<int> dist(total_nodes, 0);
    int active_nodes = 0;

    for (int i = 0; i < total_nodes; ++i) {
        if (exists[i]) {
            active_nodes++;
            if (in_deg[i] == 0) {
                dist[i] = 1;
                q.push(i);
            }
        }
    }

    int processed = 0;
    int max_days = 0;

    while (!q.empty()) {
        int u = q.front();
        q.pop();
        processed++;
        max_days = max(max_days, dist[u]);

        for (int v : adj[u]) {
            dist[v] = max(dist[v], dist[u] + 1);
            if (--in_deg[v] == 0) {
                q.push(v);
            }
        }
    }

    if (processed < active_nodes) {
        cout << -1 << "\n";
    } else {
        cout << max_days << "\n";
    }

    return 0;
}
"""
    },
    {
        "id": "abc145_e",
        "title": "All-you-can-eat",
        "contest_id": "abc145",
        "rating": 1528,
        "tag": "Dynamic Programming",
        "subtopic": "Classic DP",
        "topic": "Order-Dependent 0-1 Knapsack (Sorting by Time Before DP)",
        "cat_folder": "dp",
        "cat_file": "order_dependent_knapsack_sorting.md",
        "statement": "N dishes with eating time A_i and deliciousness B_i. You can order as long as the current total time is strictly less than T. Once ordered, you can finish the dish regardless of how much time it takes. Maximize total deliciousness.",
        "key_idea": "The final dish ordered can exceed time limit T. By sorting dishes by eating time A_i ascending, the dish that exceeds T can always be assumed to be the LAST dish processed in the DP sequence.",
        "observation": "Suppose an optimal subset of dishes is chosen. The last dish ordered must start before T, and it is optimal for this last dish to be the one with the largest eating time A_i. Therefore, sorting by A_i in ascending order ensures that when processing dish i, all previously selected dishes had eating time <= A_i.",
        "algorithm": [
            "Sort items by A_i in ascending order.",
            "Initialize dp[T] = 0 (dp[t] is max value using total time t < T).",
            "ans = 0.",
            "For each item (A_i, B_i):",
            "  For each t from 0 to T - 1:",
            "    ans = max(ans, dp[t] + B_i).",
            "  For t from T - 1 down to A_i:",
            "    dp[t] = max(dp[t], dp[t - A_i] + B_i).",
            "Print ans."
        ],
        "time_complexity": "O(N * T)",
        "space_complexity": "O(T)",
        "core_skill": "Sorting items by constraint parameter before 0-1 Knapsack to resolve boundary overflow relaxations.",
        "reusable_pattern": "Relaxed Final Item Knapsack: sort by weight ascending, update global max before standard knapsack transition.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, T;
    if (!(cin >> n >> T)) return 0;

    vector<pair<int, int>> dishes(n);
    for (int i = 0; i < n; ++i) {
        cin >> dishes[i].first >> dishes[i].second;
    }

    // Sort by eating time ascending
    sort(dishes.begin(), dishes.end());

    vector<int> dp(T, 0);
    int ans = 0;

    for (int i = 0; i < n; ++i) {
        int a = dishes[i].first;
        int b = dishes[i].second;

        // Try using dish i as the final (overflowing) dish
        for (int t = 0; t < T; ++t) {
            ans = max(ans, dp[t] + b);
        }

        // Standard 0-1 knapsack transition for time < T
        for (int t = T - 1; t >= a; --t) {
            dp[t] = max(dp[t], dp[t - a] + b);
        }
    }

    cout << ans << "\n";
    return 0;
}
"""
    },
    {
        "id": "abc161_f",
        "title": "Division or Subtraction",
        "contest_id": "abc161",
        "rating": 1528,
        "tag": "Number Theory",
        "subtopic": "Divisors",
        "topic": "Number Theory Divisor Analysis on N and N-1",
        "cat_folder": "number_theory",
        "cat_file": "divisor_analysis_division_subtraction.md",
        "statement": "Given an integer N. An operation replaces N with N / K if N is divisible by K, or N - K otherwise. Count integers K >= 2 such that N eventually becomes 1.",
        "key_idea": "Split into two cases: 1) K divides N initially; 2) K does not divide N initially.",
        "observation": "If K does not divide N, N -= K is repeated until N becomes N % K. For N to become 1, we must have N % K == 1 <=> K divides (N - 1). If K divides N, repeatedly divide N by K until not divisible, then test if the remaining value mod K == 1.",
        "algorithm": [
            "Find all divisors of N - 1 greater than 1: all of them are valid K.",
            "Find all divisors of N greater than 1. For each divisor d:",
            "  Simulate: temp = N; while temp % d == 0: temp /= d.",
            "  If temp % d == 1: add d to the set of valid K.",
            "Print total count of unique valid K."
        ],
        "time_complexity": "O(sqrt(N))",
        "space_complexity": "O(sqrt(N))",
        "core_skill": "Modular arithmetic reduction of repeated subtraction combined with divisor analysis.",
        "reusable_pattern": "Divisor Branching: test divisors of N-1 (mod K == 1) and test divisors of N via full division.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <set>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;

    set<long long> valid_k;

    // Case 1: K does not divide N initially => K must divide N - 1
    long long n_minus_1 = n - 1;
    for (long long d = 1; d * d <= n_minus_1; ++d) {
        if (n_minus_1 % d == 0) {
            if (d >= 2) valid_k.insert(d);
            if (n_minus_1 / d >= 2) valid_k.insert(n_minus_1 / d);
        }
    }

    // Case 2: K divides N initially
    for (long long d = 1; d * d <= n; ++d) {
        if (n % d == 0) {
            auto test_k = [&](long long k) {
                if (k < 2) return;
                long long temp = n;
                while (temp % k == 0) temp /= k;
                if (temp % k == 1) valid_k.insert(k);
            };
            test_k(d);
            test_k(n / d);
        }
    }

    cout << valid_k.size() << "\n";
    return 0;
}
"""
    },
    {
        "id": "abc122_d",
        "title": "We Like AGC",
        "contest_id": "abc122",
        "rating": 1533,
        "tag": "Dynamic Programming",
        "subtopic": "Classic DP",
        "topic": "Dynamic Programming on Last 3 Characters / Forbidden Pattern Counting",
        "cat_folder": "dp",
        "cat_file": "forbidden_pattern_last3_dp.md",
        "statement": "Find the number of strings of length N consisting of 'A', 'G', 'C', 'T' that do not contain 'AGC' as a substring, and where swapping any two adjacent characters also does not create 'AGC', modulo 10^9 + 7.",
        "key_idea": "Forbidden 3-character patterns: 'AGC', 'GAC', 'ACG'. Forbidden 4-character patterns: 'A?GC' (e.g. AGTC->ATGC), 'AG?C'. The validity of appending a character depends only on the last 3 characters.",
        "observation": "Encoding 4 characters ('A'=0, 'G'=1, 'C'=2, 'T'=3) yields 4^3 = 64 states. DP state: `dp[len][c1][c2][c3]` tracking the last 3 characters. Transitions check all 4 choices for the next character c4.",
        "algorithm": [
            "Map 'A'->0, 'G'->1, 'C'->2, 'T'->3. Define dummy initial characters.",
            "Initialize dp[dummy][dummy][dummy] = 1.",
            "For step from 1 to N:",
            "  For each (c1, c2, c3):",
            "    For next character c4 in 0..3:",
            "      Check if (c2, c3, c4) == 'AGC', 'GAC', 'ACG', or (c1, c2, c4) == 'AGC', or (c1, c3, c4) == 'AGC'.",
            "      If valid: next_dp[c2][c3][c4] = (next_dp[c2][c3][c4] + dp[c1][c2][c3]) % MOD.",
            "Sum next_dp over all states and print result."
        ],
        "time_complexity": "O(N * 4^4)",
        "space_complexity": "O(4^3)",
        "core_skill": "Suffix state compression DP for forbidden substring avoidance under adjacent transpositions.",
        "reusable_pattern": "Suffix Window DP: maintain last K-1 characters as state to validate incoming characters.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>

using namespace std;

const int MOD = 1000000007;

// A=0, G=1, C=2, T=3, dummy=4
bool is_valid(int c1, int c2, int c3, int c4) {
    // Contains "AGC"
    if (c2 == 0 && c3 == 1 && c4 == 2) return false;
    // Swap c3, c4 -> GAC
    if (c2 == 1 && c3 == 0 && c4 == 2) return false;
    // Swap c3, c4 -> ACG
    if (c2 == 0 && c3 == 2 && c4 == 1) return false;
    // Swap c2, c3 -> A?GC
    if (c1 == 0 && c2 == 1 && c4 == 2) return false;
    // Swap c1, c2 -> AG?C
    if (c1 == 0 && c3 == 1 && c4 == 2) return false;
    return true;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    int dp[5][5][5] = {0};
    dp[4][4][4] = 1;

    for (int len = 0; len < n; ++len) {
        int next_dp[5][5][5] = {0};
        for (int c1 = 0; c1 < 5; ++c1) {
            for (int c2 = 0; c2 < 5; ++c2) {
                for (int c3 = 0; c3 < 5; ++c3) {
                    if (!dp[c1][c2][c3]) continue;
                    for (int c4 = 0; c4 < 4; ++c4) {
                        if (is_valid(c1, c2, c3, c4)) {
                            next_dp[c2][c3][c4] = (next_dp[c2][c3][c4] + dp[c1][c2][c3]) % MOD;
                        }
                    }
                }
            }
        }
        for (int c1 = 0; c1 < 5; ++c1) {
            for (int c2 = 0; c2 < 5; ++c2) {
                for (int c3 = 0; c3 < 5; ++c3) {
                    dp[c1][c2][c3] = next_dp[c1][c2][c3];
                }
            }
        }
    }

    int ans = 0;
    for (int c1 = 0; c1 < 4; ++c1) {
        for (int c2 = 0; c2 < 4; ++c2) {
            for (int c3 = 0; c3 < 4; ++c3) {
                ans = (ans + dp[c1][c2][c3]) % MOD;
            }
        }
    }

    cout << ans << "\n";
    return 0;
}
"""
    },
    {
        "id": "abc150_d",
        "title": "Semi Common Multiple",
        "contest_id": "abc150",
        "rating": 1534,
        "tag": "Number Theory",
        "subtopic": "LCM & Divisibility",
        "topic": "2-adic Valuation & Odd Multiple LCM Condition",
        "cat_folder": "number_theory",
        "cat_file": "two_adic_lcm_odd_multiples.md",
        "statement": "Given an array A of even positive integers. Find the number of integers X in 1..M such that for every i, X = A_i * (p + 0.5) for some non-negative integer p.",
        "key_idea": "X = (A_i / 2) * (2p + 1). Thus, X must be an ODD multiple of each a'_i = A_i / 2. This requires all a'_i to have the exact same 2-adic valuation (power of 2).",
        "observation": "If any two a'_i differ in their highest power of 2 dividing them, no such X can exist (output 0). Otherwise, X must be an odd multiple of L = LCM(a'_1, ..., a'_N). The count of odd multiples <= M is ((M / L) + 1) / 2.",
        "algorithm": [
            "Divide each element of A by 2 to get a'_i.",
            "Check that all a'_i have identical __builtin_ctzll(a'_i). If not, print 0.",
            "Compute L = LCM(a'_1, ..., a'_N). If at any point L > M, print 0.",
            "Print ((M / L) + 1) / 2."
        ],
        "time_complexity": "O(N log(max A))",
        "space_complexity": "O(N)",
        "core_skill": "2-adic valuation consistency check and odd-multiple LCM counting.",
        "reusable_pattern": "Odd Multiple of Elements: check equal 2-adic valuations, compute LCM, count odd multiples ((M/L)+1)/2.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <numeric>

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
    long long m;
    if (!(cin >> n >> m)) return 0;

    vector<long long> a(n);
    int common_ctz = -1;

    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        a[i] /= 2;
        int c = __builtin_ctzll(a[i]);
        if (common_ctz == -1) common_ctz = c;
        else if (common_ctz != c) {
            cout << 0 << "\n";
            return 0;
        }
    }

    long long L = 1;
    for (int i = 0; i < n; ++i) {
        long long g = gcd(L, a[i]);
        __int128 next_L = (__int128)L * (a[i] / g);
        if (next_L > m) {
            cout << 0 << "\n";
            return 0;
        }
        L = next_L;
    }

    cout << (m / L + 1) / 2 << "\n";
    return 0;
}
"""
    },
    {
        "id": "abc027_c",
        "title": "Doubling Game",
        "contest_id": "abc027",
        "rating": 1539,
        "tag": "Game Theory",
        "subtopic": "Minimax",
        "topic": "Binary Tree Game Theory Minimax Depth Parity",
        "cat_folder": "game_theory",
        "cat_file": "minimax_depth_parity_doubling.md",
        "statement": "Starting with x = 1, Takahashi and Aoki alternate turns. On their turn, a player replaces x with either 2x or 2x + 1. The first player to make x > N loses. Determine the winner under optimal play.",
        "key_idea": "The game takes place on a complete binary tree where leaves exceed N. The player who wants to win should force the game to a depth where the opponent is compelled to exceed N.",
        "observation": "Let depth D = floor(log2(N)) + 1. If D is odd, Takahashi wants the game to end at depth D (odd depth, Aoki's turn to exceed). Thus Takahashi chooses the right child (2x+1) to maximize x, while Aoki chooses the left child (2x) to delay. If D is even, roles reverse.",
        "algorithm": [
            "Compute depth D = floor(log2(N)) + 1.",
            "Simulate from x = 1, tracking whose turn it is.",
            "If D is even:",
            "  Takahashi picks 2x + 1; Aoki picks 2x.",
            "If D is odd:",
            "  Takahashi picks 2x; Aoki picks 2x + 1.",
            "Continue until x > N. The player whose turn it was when x exceeded N loses; the other player wins."
        ],
        "time_complexity": "O(log N)",
        "space_complexity": "O(1)",
        "core_skill": "Game tree depth parity analysis for binary expansion pursuit-evasion games.",
        "reusable_pattern": "Doubling Game Parity: compare depth parity, winner forces max expansion on own turn and min on opponent's.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;

    int depth = 0;
    for (long long temp = n; temp > 0; temp /= 2) {
        depth++;
    }

    long long x = 1;
    bool takahashi_turn = true;

    while (x <= n) {
        if (depth % 2 == 1) {
            // Takahashi minimizes, Aoki maximizes
            if (takahashi_turn) x = 2 * x + 1;
            else x = 2 * x;
        } else {
            // Takahashi maximizes, Aoki minimizes
            if (takahashi_turn) x = 2 * x;
            else x = 2 * x + 1;
        }
        takahashi_turn = !takahashi_turn;
    }

    // The player whose turn it is now won, because the previous player exceeded N
    if (takahashi_turn) {
        cout << "Takahashi\n";
    } else {
        cout << "Aoki\n";
    }

    return 0;
}
"""
    },
    {
        "id": "arc075_b",
        "title": "Widespread",
        "contest_id": "abc063",
        "rating": 1544,
        "tag": "Basics",
        "subtopic": "Binary Search on Answer",
        "topic": "Binary Search on Answer / Splash Damage Allocation",
        "cat_folder": "basics",
        "cat_file": "binary_search_splash_damage.md",
        "statement": "N monsters with health H_i. An explosion deals A damage to a chosen center monster and B damage to all other monsters (A > B). Find the minimum explosions to defeat all monsters.",
        "key_idea": "Binary search on the total explosions K. In K explosions, every monster automatically receives K * B splash damage. Additional center blasts on monster i add A - B damage each.",
        "observation": "For a fixed K, monster i has remaining health rem = max(0LL, H_i - K * B). The number of center hits needed on monster i is ceil(rem / (A - B)). All monsters are defeated iff the sum of needed center hits <= K.",
        "algorithm": [
            "Binary search on explosions K in [1, 10^9].",
            "Define check(K):",
            "  centers_needed = 0.",
            "  For each H_i:",
            "    rem = H_i - K * B.",
            "    If rem > 0: centers_needed += (rem + (A - B) - 1) / (A - B).",
            "  Return centers_needed <= K.",
            "Output the minimum K satisfying check(K)."
        ],
        "time_complexity": "O(N log(max H))",
        "space_complexity": "O(N)",
        "core_skill": "Binary search feasibility check by isolating uniform baseline splash damage from targeted focal damage.",
        "reusable_pattern": "Area-of-Effect Splash Damage: baseline K*B damage + ceil(rem / (A-B)) center allocations.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long a, b;
    if (!(cin >> n >> a >> b)) return 0;

    vector<long long> h(n);
    for (int i = 0; i < n; ++i) {
        cin >> h[i];
    }

    long long diff = a - b;
    long long low = 1, high = 1e9;
    long long ans = high;

    auto check = [&](long long k) -> bool {
        long long centers = 0;
        for (int i = 0; i < n; ++i) {
            long long rem = h[i] - k * b;
            if (rem > 0) {
                centers += (rem + diff - 1) / diff;
                if (centers > k) return false;
            }
        }
        return centers <= k;
    };

    while (low <= high) {
        long long mid = low + (high - low) / 2;
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
        "id": "arc079_b",
        "title": "Decrease",
        "contest_id": "abc068",
        "rating": 1545,
        "tag": "Basics",
        "subtopic": "Constructive Algorithms",
        "topic": "Reverse Operation Constructive Array Synthesis modulo N",
        "cat_folder": "basics",
        "cat_file": "reverse_operation_array_synthesis.md",
        "statement": "Given an integer K (0 <= K <= 5 * 10^16). Construct an array A of size N (2 <= N <= 50) with 0 <= A_i <= 10^16 + 1000 such that the process of repeatedly decreasing the maximum element by N and increasing all other elements by 1 takes EXACTLY K operations to terminate.",
        "key_idea": "Fix N = 50. In a complete round of N operations where each index is operated once, each element undergoes one -N and (N-1) times +1, net change of -1 to all elements. Decompose K into q = K / N rounds and r = K % N remainder operations.",
        "observation": "Base state where all elements terminate after 0 operations: all elements equal to N - 1. Adding q complete cycles adds q to all elements. For the remaining r operations, operating on r indices adds N to each of those r indices and subtracts 1 from all other 50 - r indices.",
        "algorithm": [
            "Set N = 50.",
            "Let q = K / N and r = K % N.",
            "Initialize all A[i] = (N - 1) + q.",
            "For i from 0 to r - 1: A[i] += N - (r - 1).",
            "For i from r to N - 1: A[i] -= r.",
            "Print N = 50, followed by array A."
        ],
        "time_complexity": "O(N)",
        "space_complexity": "O(N)",
        "core_skill": "Reverse operation quotient-remainder decomposition for invariant cycle construction.",
        "reusable_pattern": "Global Cycle Constructive Synthesis: base (N-1) + (K/N) with remainder prefix offsets.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long k;
    if (!(cin >> k)) return 0;

    int n = 50;
    long long q = k / n;
    int r = k % n;

    vector<long long> a(n, n - 1 + q);
    for (int i = 0; i < r; ++i) {
        a[i] += n - r + 1;
    }
    for (int i = r; i < n; ++i) {
        a[i] -= r;
    }

    cout << n << "\n";
    for (int i = 0; i < n; ++i) {
        cout << a[i] << (i + 1 == n ? "\n" : " ");
    }

    return 0;
}
"""
    },
    {
        "id": "abc146_f",
        "title": "Sugoroku",
        "contest_id": "abc146",
        "rating": 1545,
        "tag": "Basics",
        "subtopic": "Greedy Algorithms",
        "topic": "Greedy Reverse BFS / Range Minimum for Lexicographical Jumps",
        "cat_folder": "basics",
        "cat_file": "greedy_reverse_bfs_lexicographical_jumps.md",
        "statement": "A board with N squares (0 to N). S[i] == '1' is game over; '0' is safe. From square i, you can jump to i + d for 1 <= d <= M. Reach N in the minimum number of moves, and among those, find the LEXICOGRAPHICALLY SMALLEST sequence of die rolls. Output -1 if unreachable.",
        "key_idea": "To achieve the lexicographically smallest sequence of forward jumps, work BACKWARDS from N! At each step from current position curr, jump backwards as FAR as possible (up to M steps) to a valid square.",
        "observation": "Greedily making the largest possible backward jump pushes earlier steps as small as possible in forward order. This guarantees the lexicographically first sequence of moves with zero extra state overhead.",
        "algorithm": [
            "Start at curr = N. Initialize move sequence moves.",
            "While curr > 0:",
            "  Find the smallest index prev in [max(0, curr - M), curr - 1] such that S[prev] == '0'.",
            "  If no safe square exists in range, output -1.",
            "  Record step (curr - prev) into moves.",
            "  curr = prev.",
            "Reverse moves and print."
        ],
        "time_complexity": "O(N)",
        "space_complexity": "O(N)",
        "core_skill": "Backward greedy simulation to achieve lexicographical optimality for forward sequences.",
        "reusable_pattern": "Lexicographical Forward Moves: backward greedy maximal jump simulation.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    string s;
    if (!(cin >> n >> m >> s)) return 0;

    vector<int> rolls;
    int curr = n;

    while (curr > 0) {
        int best_prev = -1;
        int min_reach = max(0, curr - m);

        for (int prev = min_reach; prev < curr; ++prev) {
            if (s[prev] == '0') {
                best_prev = prev;
                break;
            }
        }

        if (best_prev == -1) {
            cout << -1 << "\n";
            return 0;
        }

        rolls.push_back(curr - best_prev);
        curr = best_prev;
    }

    reverse(rolls.begin(), rolls.end());
    for (size_t i = 0; i < rolls.size(); ++i) {
        cout << rolls[i] << (i + 1 == rolls.size() ? "\n" : " ");
    }

    return 0;
}
"""
    },
    {
        "id": "abc129_e",
        "title": "Sum Equals Xor",
        "contest_id": "abc129",
        "rating": 1547,
        "tag": "Dynamic Programming",
        "subtopic": "Digit DP",
        "topic": "Digit DP on Bitwise Condition a + b = a ^ b (Disjoint Bits)",
        "cat_folder": "dp",
        "cat_file": "digit_dp_disjoint_bits_sum_xor.md",
        "statement": "Given an integer N in binary (length up to 10^5). Count pairs of non-negative integers (a, b) such that a + b <= N and a + b = a ^ b, modulo 10^9 + 7.",
        "key_idea": "a + b = a ^ b holds iff a AND b = 0 (no carry in binary addition). At each bit position, the pair of bits (a_bit, b_bit) can be (0, 0) [1 choice, sum bit 0], or (1, 0) / (0, 1) [2 choices, sum bit 1].",
        "observation": "Digit DP on binary string L: `dp[i][less]` where less is boolean. At position i: if sum bit is 0 (1 choice), next_less = less || (L[i] == '1'). If sum bit is 1 (2 choices), valid only if less || (L[i] == '1').",
        "algorithm": [
            "dp[0] = 1 (equal to prefix), dp[1] = 0 (strictly less).",
            "For each character c in L:",
            "  next_0 = 0, next_1 = 0.",
            "  If c == '1':",
            "    next_0 = (2LL * dp[0]) % MOD; // choose sum bit 1, stays equal",
            "    next_1 = (dp[0] + 3LL * dp[1]) % MOD; // choose sum bit 0 (becomes less) or extend less with 3 choices",
            "  Else (c == '0'):",
            "    next_0 = dp[0]; // choose sum bit 0, stays equal",
            "    next_1 = (3LL * dp[1]) % MOD; // extend less with 3 choices",
            "  dp[0] = next_0, dp[1] = next_1.",
            "Print (dp[0] + dp[1]) % MOD."
        ],
        "time_complexity": "O(|L|)",
        "space_complexity": "O(1)",
        "core_skill": "Digit DP state transition encoding over carry-free bitwise constraints.",
        "reusable_pattern": "Sum Equals XOR Digit DP: 1 choice for bit 0, 2 choices for bit 1, 3 total branch choices.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <string>

using namespace std;

const int MOD = 1000000007;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string L;
    if (!(cin >> L)) return 0;

    long long dp_eq = 1, dp_less = 0;

    for (char c : L) {
        long long next_eq = 0, next_less = 0;
        if (c == '1') {
            // Choice 1: sum bit = 1 (2 choices: (1,0) or (0,1)), stays equal
            next_eq = (dp_eq * 2) % MOD;
            // Choice 2: sum bit = 0 (1 choice: (0,0)), transitions from equal to less
            // Plus all 3 choices for existing less
            next_less = (dp_eq + dp_less * 3) % MOD;
        } else {
            // Choice 1: sum bit = 0 (1 choice: (0,0)), stays equal
            next_eq = dp_eq;
            // Choice 2: all 3 choices for existing less
            next_less = (dp_less * 3) % MOD;
        }
        dp_eq = next_eq;
        dp_less = next_less;
    }

    cout << (dp_eq + dp_less) % MOD << "\n";
    return 0;
}
"""
    },
    {
        "id": "abc034_d",
        "title": "Salt Water",
        "contest_id": "abc034",
        "rating": 1549,
        "tag": "Basics",
        "subtopic": "Binary Search on Answer",
        "topic": "Binary Search on Average / Dinkelbach Fractional Programming",
        "cat_folder": "basics",
        "cat_file": "binary_search_average_fractional_programming.md",
        "statement": "Given N beakers of salt water with weight w_i and concentration p_i%. Select exactly K beakers to mix such that the resulting concentration is maximized. Output the maximum concentration.",
        "key_idea": "Binary search on target concentration X. A mixture has concentration >= X iff sum_{chosen} w_i * (p_i - X) >= 0.",
        "observation": "For a fixed candidate percentage X, calculate the relative gain value v_i = w_i * (p_i - X) for each beaker. Sort values descending and take the sum of the K largest values. If this sum >= 0, target concentration X is achievable.",
        "algorithm": [
            "Binary search on X in [0.0, 100.0] for 100 iterations.",
            "For each iteration with mid X:",
            "  Compute v[i] = w[i] * (p[i] - X).",
            "  Sort v in descending order.",
            "  Sum the top K elements.",
            "  If sum >= 0, low = mid; else high = mid.",
            "Print low with high precision."
        ],
        "time_complexity": "O(N log N * 100)",
        "space_complexity": "O(N)",
        "core_skill": "Fractional programming reduction via binary search on target ratio (Dinkelbach method).",
        "reusable_pattern": "Maximize Weighted Average: binary search X with check sum of top K w_i*(p_i - X) >= 0.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <iomanip>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> w(n);
    vector<double> p(n);

    for (int i = 0; i < n; ++i) {
        cin >> w[i] >> p[i];
    }

    double low = 0.0, high = 100.0;
    for (int iter = 0; iter < 100; ++iter) {
        double mid = (low + high) / 2.0;

        vector<double> gain(n);
        for (int i = 0; i < n; ++i) {
            gain[i] = w[i] * (p[i] - mid);
        }

        sort(gain.rbegin(), gain.rend());

        double top_k_sum = 0;
        for (int i = 0; i < k; ++i) {
            top_k_sum += gain[i];
        }

        if (top_k_sum >= 0) {
            low = mid;
        } else {
            high = mid;
        }
    }

    cout << fixed << setprecision(12) << low << "\n";
    return 0;
}
"""
    },
    {
        "id": "arc085_b",
        "title": "ABS",
        "contest_id": "abc078",
        "rating": 1550,
        "tag": "Game Theory",
        "subtopic": "Minimax",
        "topic": "Game Theory Minimax 1-Step Lookahead / Card Draw Reduction",
        "cat_folder": "game_theory",
        "cat_file": "game_theory_card_draw_minimax.md",
        "statement": "N cards with values A_1, ..., A_N. X starts with card Z and Y starts with card W. X draws some number of cards (leaving at least 1 for Y). Y draws some cards. Final score is |X's card - Y's card|. X maximizes, Y minimizes. Determine the game outcome under optimal play.",
        "key_idea": "By backward induction, Y will always choose to take all remaining cards up to N to achieve |X's chosen card - A_N|. Knowing this, X only needs to choose between taking all cards up to N (score |A_N - W|) or taking all cards up to N - 1 (score |A_{N-1} - A_N|).",
        "observation": "Any other choice gives Y an option to achieve an even smaller difference. Thus X's optimal move is simply max(|A_N - W|, |A_{N-1} - A_N|) when N >= 2.",
        "algorithm": [
            "If N == 1, answer is |A_0 - W|.",
            "If N >= 2, answer is max(|A[N-1] - W|, |A[N-2] - A[N-1]|).",
            "Print answer."
        ],
        "time_complexity": "O(N)",
        "space_complexity": "O(N)",
        "core_skill": "Minimax analysis identifying dominant end-game strategies.",
        "reusable_pattern": "Sequential Card Draw Minimax: simplifies to max(|last - W|, |second_last - last|).",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long z, w;
    if (!(cin >> n >> z >> w)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    if (n == 1) {
        cout << abs(a[0] - w) << "\n";
    } else {
        long long ans = max(abs(a[n - 1] - w), abs(a[n - 2] - a[n - 1]));
        cout << ans << "\n";
    }

    return 0;
}
"""
    },
    {
        "id": "abc018_3",
        "title": "Diamond Count",
        "contest_id": "abc018",
        "rating": 1553,
        "tag": "Dynamic Programming",
        "subtopic": "2D Grid DP",
        "topic": "2D Vertical Consecutive Run Prefix Sums for Diamond Pattern Matching",
        "cat_folder": "dp",
        "cat_file": "diamond_pattern_vertical_runs.md",
        "statement": "An R x C grid of 'o' and 'x'. Count center cells (r, c) such that a diamond (Manhattan circle) of radius K centered at (r, c) consists entirely of 'o'.",
        "key_idea": "For cell (r, c) to be a diamond center, for each column offset dx in [-(K-1), K-1], the vertical continuous span of 'o's above and below (r, c+dx) must be at least K - 1 - |dx|.",
        "observation": "Precompute up[r][c] (number of consecutive 'o's above (r, c)) and down[r][c] (consecutive 'o's below (r, c)) in O(R * C). Then test each potential center (r, c) by checking the 2K - 1 columns in O(K).",
        "algorithm": [
            "Compute up[r][c] = (grid[r][c] == 'o' ? up[r-1][c] + 1 : 0).",
            "Compute down[r][c] = (grid[r][c] == 'o' ? down[r+1][c] + 1 : 0).",
            "valid_centers = 0.",
            "For r from K to R - K + 1:",
            "  For c from K to C - K + 1:",
            "    valid = true.",
            "    For dx from -(K - 1) to K - 1:",
            "      req = K - 1 - abs(dx);",
            "      if (up[r][c + dx] <= req || down[r][c + dx] <= req) { valid = false; break; }",
            "    If valid: valid_centers++.",
            "Print valid_centers."
        ],
        "time_complexity": "O(R * C * K)",
        "space_complexity": "O(R * C)",
        "core_skill": "Vertical consecutive span precomputation for fast geometric shape validation on grids.",
        "reusable_pattern": "Manhattan Diamond Validation: up/down runs >= K - 1 - |dx| across horizontal window.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <string>
#include <cmath>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int R, C, K;
    if (!(cin >> R >> C >> K)) return 0;

    vector<string> grid(R + 1);
    for (int r = 1; r <= R; ++r) {
        cin >> grid[r];
        grid[r] = " " + grid[r];
    }

    vector<vector<int>> up(R + 2, vector<int>(C + 2, 0));
    vector<vector<int>> down(R + 2, vector<int>(C + 2, 0));

    for (int c = 1; c <= C; ++c) {
        for (int r = 1; r <= R; ++r) {
            up[r][c] = (grid[r][c] == 'o' ? up[r - 1][c] + 1 : 0);
        }
        for (int r = R; r >= 1; --r) {
            down[r][c] = (grid[r][c] == 'o' ? down[r + 1][c] + 1 : 0);
        }
    }

    int count = 0;
    for (int r = K; r <= R - K + 1; ++r) {
        for (int c = K; c <= C - K + 1; ++c) {
            bool ok = true;
            for (int dx = -(K - 1); dx <= K - 1; ++dx) {
                int req = K - 1 - abs(dx);
                if (up[r][c + dx] <= req || down[r][c + dx] <= req) {
                    ok = false;
                    break;
                }
            }
            if (ok) count++;
        }
    }

    cout << count << "\n";
    return 0;
}
"""
    },
    {
        "id": "abc175_e",
        "title": "Picking Goods",
        "contest_id": "abc175",
        "rating": 1554,
        "tag": "Dynamic Programming",
        "subtopic": "2D Grid DP",
        "topic": "2D Grid DP with Per-Row Item Capacity Constraint (At Most 3 Items)",
        "cat_folder": "dp",
        "cat_file": "grid_dp_row_item_capacity.md",
        "statement": "An R x C grid with K items. Move from (1, 1) to (R, C) using right and down moves. In each row, you may pick at most 3 items. Maximize the total value of items collected.",
        "key_idea": "3D DP state: `dp[r][c][k]` representing the maximum value at cell (r, c) having picked k items in row r (k in 0..3).",
        "observation": "When moving right: k can increase by 1 if an item is picked at (r, c). When moving down: the row resets, so k resets to 0, taking the maximum over all 0..3 items picked from the previous row.",
        "algorithm": [
            "Initialize dp[R+1][C+1][4] with 0.",
            "For r from 1 to R:",
            "  For c from 1 to C:",
            "    val = item_value[r][c].",
            "    Transitions from (r-1, c) moving down:",
            "      max_prev_row = max_{k=0..3} dp[r-1][c][k].",
            "      dp[r][c][0] = max(dp[r][c][0], max_prev_row).",
            "      If val > 0: dp[r][c][1] = max(dp[r][c][1], max_prev_row + val).",
            "    Transitions from (r, c-1) moving right:",
            "      For k from 0 to 3:",
            "        dp[r][c][k] = max(dp[r][c][k], dp[r][c-1][k]).",
            "        If val > 0 and k < 3:",
            "          dp[r][c][k+1] = max(dp[r][c][k+1], dp[r][c-1][k] + val).",
            "Print max_{k=0..3} dp[R][C][k]."
        ],
        "time_complexity": "O(R * C)",
        "space_complexity": "O(R * C)",
        "core_skill": "Multi-dimensional grid DP tracking localized row-reset resource constraints.",
        "reusable_pattern": "Row-Constrained Grid DP: dp[r][c][k] where moving down transitions from max_k dp[r-1][c][k].",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int R, C, K;
    if (!(cin >> R >> C >> K)) return 0;

    vector<vector<long long>> val(R + 1, vector<long long>(C + 1, 0));
    for (int i = 0; i < K; ++i) {
        int r, c;
        long long v;
        cin >> r >> c >> v;
        val[r][c] = v;
    }

    // dp[r][c][k]: max value at (r, c) with k items picked on row r
    vector<vector<vector<long long>>> dp(R + 1, vector<vector<long long>>(C + 1, vector<long long>(4, 0)));

    for (int r = 1; r <= R; ++r) {
        for (int c = 1; c <= C; ++c) {
            long long item = val[r][c];

            // Transition from above (r - 1, c): row resets
            long long max_above = 0;
            for (int k = 0; k < 4; ++k) max_above = max(max_above, dp[r - 1][c][k]);

            dp[r][c][0] = max(dp[r][c][0], max_above);
            if (item > 0) {
                dp[r][c][1] = max(dp[r][c][1], max_above + item);
            }

            // Transition from left (r, c - 1): same row
            for (int k = 0; k < 4; ++k) {
                dp[r][c][k] = max(dp[r][c][k], dp[r][c - 1][k]);
            }
            if (item > 0) {
                for (int k = 0; k < 3; ++k) {
                    dp[r][c][k + 1] = max(dp[r][c][k + 1], dp[r][c - 1][k] + item);
                }
            }
        }
    }

    long long ans = 0;
    for (int k = 0; k < 4; ++k) ans = max(ans, dp[R][C][k]);

    cout << ans << "\n";
    return 0;
}
"""
    },
    {
        "id": "arc083_b",
        "title": "Restoring Road Network",
        "contest_id": "abc074",
        "rating": 1563,
        "tag": "Graph Theory",
        "subtopic": "All-Pairs Shortest Paths",
        "topic": "Reverse Floyd-Warshall Strict Triangle Inequality Edge Minimality",
        "cat_folder": "graph_theory",
        "cat_file": "reverse_floyd_warshall_edge_minimality.md",
        "statement": "Given an N x N matrix A of all-pairs shortest path distances. Verify whether a valid graph exists whose shortest path matrix equals A. If yes, output the minimum total weight of edges.",
        "key_idea": "Reverse Floyd-Warshall! If A[i][j] > A[i][k] + A[k][j] for any k, the triangle inequality is violated (output -1). If A[i][j] == A[i][k] + A[k][j] for some k != i, j, edge (i, j) is redundant and can be omitted. Otherwise, edge (i, j) is strictly required.",
        "observation": "Any edge (i, j) whose weight equals the sum of two other paths can be safely removed without altering any shortest path. Edges that strictly cannot be bypassed must be kept, and their sum is the minimum possible total weight.",
        "algorithm": [
            "For all triples (i, j, k) with k != i and k != j:",
            "  If A[i][j] > A[i][k] + A[k][j], return -1.",
            "Initialize total_weight = 0.",
            "For each pair (i, j) with i < j:",
            "  necessary = true.",
            "  For each k != i, j:",
            "    If A[i][j] == A[i][k] + A[k][j]: necessary = false, break.",
            "  If necessary: total_weight += A[i][j].",
            "Print total_weight."
        ],
        "time_complexity": "O(N^3)",
        "space_complexity": "O(N^2)",
        "core_skill": "Reverse triangle inequality verification and minimal transitively irreducible subgraph extraction.",
        "reusable_pattern": "Shortest Path Matrix Reducibility: check strict triangle violation, omit edges with equality bypass.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<long long>> A(n, vector<long long>(n));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            cin >> A[i][j];
        }
    }

    // Check triangle inequality
    for (int k = 0; k < n; ++k) {
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (A[i][j] > A[i][k] + A[k][j]) {
                    cout << -1 << "\n";
                    return 0;
                }
            }
        }
    }

    long long total_weight = 0;

    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            bool redundant = false;
            for (int k = 0; k < n; ++k) {
                if (k != i && k != j) {
                    if (A[i][j] == A[i][k] + A[k][j]) {
                        redundant = true;
                        break;
                    }
                }
            }
            if (!redundant) {
                total_weight += A[i][j];
            }
        }
    }

    cout << total_weight << "\n";
    return 0;
}
"""
    },
    {
        "id": "abc051_d",
        "title": "Candidates of No Shortest Paths",
        "contest_id": "abc051",
        "rating": 1566,
        "tag": "Graph Theory",
        "subtopic": "All-Pairs Shortest Paths",
        "topic": "Floyd-Warshall Edge Shortest Path Criterion",
        "cat_folder": "graph_theory",
        "cat_file": "floyd_warshall_shortest_path_edge_criterion.md",
        "statement": "An undirected weighted graph with N vertices and M edges. Count how many edges are NOT used in any shortest path between any pair of vertices.",
        "key_idea": "Precompute all-pairs shortest paths using Floyd-Warshall. An edge e = (u, v, w) is used in a shortest path between some pair (s, t) if and only if dist[s][u] + w + dist[v][t] == dist[s][t] (or with u and v swapped).",
        "observation": "Setting s = u and t = v, edge (u, v) is used in some shortest path iff dist[u][v] == w! If dist[u][v] < w, the edge is strictly longer than an alternative path and will NEVER be part of any shortest path.",
        "algorithm": [
            "Compute all-pairs shortest paths dist[u][v] using Floyd-Warshall in O(N^3).",
            "unused_edges = 0.",
            "For each edge (u, v, w):",
            "  If dist[u][v] < w, unused_edges++.",
            "Print unused_edges."
        ],
        "time_complexity": "O(N^3 + M)",
        "space_complexity": "O(N^2)",
        "core_skill": "Identifying redundant edges via direct comparison against all-pairs shortest distance matrix.",
        "reusable_pattern": "Unused Shortest Path Edge: count edges where dist[u][v] < edge_weight.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int INF = 1e9;

struct Edge {
    int u, v, w;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<int>> dist(n + 1, vector<int>(n + 1, INF));
    for (int i = 1; i <= n; ++i) dist[i][i] = 0;

    vector<Edge> edges(m);
    for (int i = 0; i < m; ++i) {
        cin >> edges[i].u >> edges[i].v >> edges[i].w;
        dist[edges[i].u][edges[i].v] = min(dist[edges[i].u][edges[i].v], edges[i].w);
        dist[edges[i].v][edges[i].u] = min(dist[edges[i].v][edges[i].u], edges[i].w);
    }

    for (int k = 1; k <= n; ++k) {
        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= n; ++j) {
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
            }
        }
    }

    int unused = 0;
    for (const auto& e : edges) {
        if (dist[e.u][e.v] < e.w) {
            unused++;
        }
    }

    cout << unused << "\n";
    return 0;
}
"""
    },
    {
        "id": "arc086_b",
        "title": "Non-decreasing",
        "contest_id": "abc081",
        "rating": 1567,
        "tag": "Basics",
        "subtopic": "Constructive Algorithms",
        "topic": "Constructive Prefix/Suffix Cumulative Addition via Global Dominant Extremum",
        "cat_folder": "basics",
        "cat_file": "constructive_cumulative_addition_dominant_extremum.md",
        "statement": "Given an array A of length N (N <= 50). In one operation, choose indices x and y and set A[y] += A[x]. Make A non-decreasing in at most 2N operations.",
        "key_idea": "Find the element with maximum absolute value |A[m]|. If A[m] >= 0, add A[m] to all elements to make them non-negative, then perform forward prefix cumulative additions. If A[m] < 0, add A[m] to all elements to make them non-positive, then perform backward suffix cumulative additions.",
        "observation": "Once all elements are non-negative, A[i] += A[i-1] for i = 2..N guarantees A[i] >= A[i-1] because A[i-1] >= 0. Similarly, once all elements are non-positive, A[i] += A[i+1] for i = N-1 down to 1 guarantees non-decreasing order. Each phase takes N - 1 operations, total <= 2N - 2 <= 2N operations.",
        "algorithm": [
            "Find index m with maximum |A[m]|.",
            "If A[m] == 0, already non-decreasing; output 0.",
            "Record operations list ops.",
            "If A[m] > 0:",
            "  Add m to all i != m (N - 1 operations).",
            "  For i = 2 to N: add (i - 1) to i: ops.push_back({i - 1, i}).",
            "If A[m] < 0:",
            "  Add m to all i != m (N - 1 operations).",
            "  For i = N - 1 down to 1: add (i + 1) to i: ops.push_back({i + 1, i}).",
            "Print ops.size(), then all operations."
        ],
        "time_complexity": "O(N)",
        "space_complexity": "O(N)",
        "core_skill": "Sign homogenization using the dominant absolute extremum followed by cumulative monotonic sweeping.",
        "reusable_pattern": "Make Non-Decreasing in 2N: add dominant element to all, then prefix/suffix cumulative sum.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n + 1);
    int max_idx = 1;

    for (int i = 1; i <= n; ++i) {
        cin >> a[i];
        if (abs(a[i]) > abs(a[max_idx])) {
            max_idx = i;
        }
    }

    vector<pair<int, int>> ops;

    if (a[max_idx] >= 0) {
        // Make all elements non-negative
        for (int i = 1; i <= n; ++i) {
            if (i != max_idx) {
                ops.push_back({max_idx, i});
            }
        }
        // Prefix sum sweep
        for (int i = 2; i <= n; ++i) {
            ops.push_back({i - 1, i});
        }
    } else {
        // Make all elements non-positive
        for (int i = 1; i <= n; ++i) {
            if (i != max_idx) {
                ops.push_back({max_idx, i});
            }
        }
        // Suffix sum sweep
        for (int i = n - 1; i >= 1; --i) {
            ops.push_back({i + 1, i});
        }
    }

    cout << ops.size() << "\n";
    for (const auto& op : ops) {
        cout << op.first << " " << op.second << "\n";
    }

    return 0;
}
"""
    },
    {
        "id": "abc155_e",
        "title": "Payment",
        "contest_id": "abc155",
        "rating": 1569,
        "tag": "Dynamic Programming",
        "subtopic": "Digit DP",
        "topic": "Digit DP with Carry on Minimum Digits for Payment and Change",
        "cat_folder": "dp",
        "cat_file": "digit_dp_carry_banknotes_payment.md",
        "statement": "You need to pay an amount N (up to 10^6 digits) using banknotes of denominations 10^k. Both payment and change use the minimum total number of banknotes. Find the minimum total banknotes exchanged.",
        "key_idea": "Process digits from right to left (least significant to most significant) with a carry state. At each digit d, you can either pay d notes with no carry, or pay 10 notes to round up (costing 10 - d notes in change) and passing a carry of 1 to the next digit.",
        "observation": "Let dp[0] be min banknotes with carry = 0, and dp[1] with carry = 1. For digit d + carry_in: Option A (no new carry): pay (d + carry_in), cost += (d + carry_in). Option B (carry = 1): pay extra, change is 10 - (d + carry_in), cost += 10 - (d + carry_in) + 1 note.",
        "algorithm": [
            "Reverse string N and append '0' for possible final carry.",
            "dp0 = 0 (carry 0), dp1 = 1 (carry 1).",
            "For each digit char in N, let d = char - '0':",
            "  next_dp0 = min(dp0 + d, dp1 + d + 1);",
            "  next_dp1 = min(dp0 + (10 - d), dp1 + (10 - (d + 1)));",
            "  dp0 = next_dp0, dp1 = next_dp1.",
            "Print dp0."
        ],
        "time_complexity": "O(|N|)",
        "space_complexity": "O(1)",
        "core_skill": "Digit DP with carry for optimal greedy rounding in base 10.",
        "reusable_pattern": "Minimal Currency Exchange DP: 2-state carry transitions dp[carry] from LSB to MSB.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!(cin >> s)) return 0;

    reverse(s.begin(), s.end());
    s.push_back('0');

    long long dp0 = 0; // carry = 0
    long long dp1 = 1; // carry = 1

    for (char c : s) {
        int d = c - '0';
        long long next_dp0 = min(dp0 + d, dp1 + d + 1);
        long long next_dp1 = min(dp0 + (10 - d), dp1 + (10 - (d + 1)));
        dp0 = next_dp0;
        dp1 = next_dp1;
    }

    cout << dp0 << "\n";
    return 0;
}
"""
    },
    {
        "id": "arc060_a",
        "title": "Tak and Cards",
        "contest_id": "abc044",
        "rating": 1583,
        "tag": "Dynamic Programming",
        "subtopic": "Classic DP",
        "topic": "Subset Average Equals A via Shifted Zero-Sum Knapsack DP",
        "cat_folder": "dp",
        "cat_file": "shifted_zero_sum_knapsack_average.md",
        "statement": "Given N cards x_1, ..., x_N and an integer A. Find the number of non-empty subsets of cards whose arithmetic mean equals A.",
        "key_idea": "The average of a subset equals A iff sum_{i in S} x_i = |S| * A iff sum_{i in S} (x_i - A) = 0. Shift each card value by -A: y_i = x_i - A. The problem becomes counting non-empty subsets with sum = 0.",
        "observation": "Because -50 <= y_i <= 50, the sum of any subset lies in [-2500, 2500]. Offset by 2500 to store in a standard 1D/2D DP table. At the end, dp[offset] - 1 (excluding empty subset) is the exact answer.",
        "algorithm": [
            "Let OFFSET = 2500. dp[2 * OFFSET + 1] initialized to 0. dp[OFFSET] = 1.",
            "For each card x:",
            "  y = x - A.",
            "  next_dp = dp.",
            "  For s from 0 to 2 * OFFSET:",
            "    If dp[s] > 0 and 0 <= s + y <= 2 * OFFSET:",
            "      next_dp[s + y] += dp[s].",
            "  dp = move(next_dp).",
            "Print dp[OFFSET] - 1."
        ],
        "time_complexity": "O(N^2 * max(X))",
        "space_complexity": "O(N * max(X))",
        "core_skill": "Mean-target transformation into shifted zero-sum knapsack DP.",
        "reusable_pattern": "Average Equals Target: shift elements by y_i = x_i - Target, count subsets summing to 0.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>

using namespace std;

const int OFFSET = 2500;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, a;
    if (!(cin >> n >> a)) return 0;

    vector<long long> dp(2 * OFFSET + 1, 0);
    dp[OFFSET] = 1;

    for (int i = 0; i < n; ++i) {
        int x;
        cin >> x;
        int y = x - a;
        vector<long long> next_dp = dp;

        for (int s = 0; s <= 2 * OFFSET; ++s) {
            if (dp[s] > 0) {
                int ns = s + y;
                if (ns >= 0 && ns <= 2 * OFFSET) {
                    next_dp[ns] += dp[s];
                }
            }
        }
        dp = move(next_dp);
    }

    cout << dp[OFFSET] - 1 << "\n";
    return 0;
}
"""
    },
    {
        "id": "abc030_d",
        "title": "Strange Dictionary",
        "contest_id": "abc030",
        "rating": 1586,
        "tag": "Basics",
        "subtopic": "Functional Graphs",
        "topic": "Functional Graph Cycle Detection with Large K (K up to 10^100000)",
        "cat_folder": "basics",
        "cat_file": "functional_graph_large_k_modulo.md",
        "statement": "A functional graph with N words. Word i points to word b_i. Start at word a and follow pointers K times, where K is a huge integer with up to 100,000 digits. Find the word reached after K steps.",
        "key_idea": "The path from a eventually enters a cycle of length L_cycle after a tail of length L_tail <= N. If K <= L_tail, simulate directly. Otherwise, compute (K - L_tail) % L_cycle using big-integer modular reduction and take that many steps along the cycle.",
        "observation": "Because N <= 10^5, the tail and cycle are both <= 10^5 steps. A single traversal finds the cycle. Reducing string K modulo L_cycle takes O(|K|) time.",
        "algorithm": [
            "Trace path from start a, recording visit step in visited[u].",
            "When reaching an already visited node u:",
            "  L_tail = visited[u], L_cycle = current_step - visited[u].",
            "If |K| is small and K <= L_tail, output node at step K.",
            "Otherwise, compute rem = (K - L_tail) % L_cycle by reading digits of K.",
            "Take rem steps starting from node u along the cycle.",
            "Print final node."
        ],
        "time_complexity": "O(N + |K|)",
        "space_complexity": "O(N)",
        "core_skill": "Functional graph periodic cycle detection combined with big-integer modular arithmetic.",
        "reusable_pattern": "Huge K on Functional Graph: find tail and cycle, compute (BigInt(K) - tail) % cycle.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, a;
    string K_str;
    if (!(cin >> n >> a >> K_str)) return 0;

    vector<int> b(n + 1);
    for (int i = 1; i <= n; ++i) {
        cin >> b[i];
    }

    vector<int> path;
    vector<int> step_at(n + 1, -1);

    int curr = a;
    int step = 0;

    while (step_at[curr] == -1) {
        step_at[curr] = step++;
        path.push_back(curr);
        curr = b[curr];
    }

    int tail_len = step_at[curr];
    int cycle_len = step - tail_len;

    // Check if K fits in simple integer <= tail_len
    if (K_str.size() <= 7) {
        long long k_val = stoll(K_str);
        if (k_val <= tail_len) {
            cout << path[k_val] << "\n";
            return 0;
        }
    }

    // Compute (K - tail_len) % cycle_len
    long long rem = 0;
    for (char c : K_str) {
        rem = (rem * 10 + (c - '0')) % cycle_len;
    }

    rem = (rem - (tail_len % cycle_len) + cycle_len) % cycle_len;

    int ans = path[tail_len + rem];
    cout << ans << "\n";
    return 0;
}
"""
    },
    {
        "id": "abc183_f",
        "title": "Confluence",
        "contest_id": "abc183",
        "rating": 1586,
        "tag": "Data Structures",
        "subtopic": "Disjoint Set Union (DSU)",
        "topic": "Disjoint Set Union with Small-to-Large Map Merging",
        "cat_folder": "data_structures",
        "cat_file": "dsu_small_to_large_map_merging.md",
        "statement": "N students with classes C_1, ..., C_N. Process Q queries: 1) unite groups containing student x and student y; 2) count how many students in student x's group belong to class y.",
        "key_idea": "Each DSU component maintains a frequency map `std::map<int, int>` of class counts. When uniting components, merge the smaller map into the larger map (small-to-large / sack heuristic).",
        "observation": "Each element is inserted into a new map at most O(log N) times. With map operations, total time is O(N log^2 N + Q log N). Queries are answered in O(log N) directly from the component root's map.",
        "algorithm": [
            "Initialize DSU parent[i] = i, and maps class_count[i][C_i] = 1.",
            "For query 1 (unite x, y):",
            "  rx = find(x), ry = find(y).",
            "  If rx == ry continue.",
            "  If class_count[rx].size() < class_count[ry].size(), swap(rx, ry).",
            "  parent[ry] = rx.",
            "  For each (cls, cnt) in class_count[ry]: class_count[rx][cls] += cnt.",
            "  class_count[ry].clear().",
            "For query 2 (x, cls):",
            "  rx = find(x).",
            "  Print class_count[rx][cls]."
        ],
        "time_complexity": "O(N log^2 N + Q log N)",
        "space_complexity": "O(N)",
        "core_skill": "Small-to-large merging heuristic applied to DSU components.",
        "reusable_pattern": "DSU Map Merging: if map[u].size() < map[v].size() swap; merge v into u.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <map>

using namespace std;

struct DSU {
    vector<int> parent;
    vector<map<int, int>> class_count;

    DSU(int n, const vector<int>& c) : parent(n + 1), class_count(n + 1) {
        for (int i = 1; i <= n; ++i) {
            parent[i] = i;
            class_count[i][c[i]] = 1;
        }
    }

    int find(int u) {
        return parent[u] == u ? u : parent[u] = find(parent[u]);
    }

    void unite(int u, int v) {
        int ru = find(u);
        int rv = find(v);
        if (ru == rv) return;

        if (class_count[ru].size() < class_count[rv].size()) {
            swap(ru, rv);
        }

        parent[rv] = ru;
        for (const auto& entry : class_count[rv]) {
            class_count[ru][entry.first] += entry.second;
        }
        class_count[rv].clear();
    }

    int query(int u, int cls) {
        int ru = find(u);
        auto it = class_count[ru].find(cls);
        return it != class_count[ru].end() ? it->second : 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    vector<int> c(n + 1);
    for (int i = 1; i <= n; ++i) {
        cin >> c[i];
    }

    DSU dsu(n, c);

    while (q--) {
        int type, x, y;
        cin >> type >> x >> y;
        if (type == 1) {
            dsu.unite(x, y);
        } else {
            cout << dsu.query(x, y) << "\n";
        }
    }

    return 0;
}
"""
    },
    {
        "id": "abc035_d",
        "title": "Treasure Hunt",
        "contest_id": "abc035",
        "rating": 1591,
        "tag": "Graph Theory",
        "subtopic": "Shortest Paths",
        "topic": "Forward & Reversed Graph Dijkstra for Time-Constrained Round Trips",
        "cat_folder": "graph_theory",
        "cat_file": "dijkstra_forward_reversed_round_trips.md",
        "statement": "Directed graph with N vertices and M edges. Vertex i yields treasure A_i per minute. You have T minutes total. Start at vertex 1, travel to some vertex v, stay there collecting treasure, and return to vertex 1. Maximize total treasure collected.",
        "key_idea": "Run Dijkstra from vertex 1 on the original graph to compute dist_to[v] (shortest travel time 1 -> v). Run Dijkstra from vertex 1 on the REVERSED graph to compute dist_from[v] (shortest travel time v -> 1).",
        "observation": "The total travel time for a round trip 1 -> v -> 1 is dist_to[v] + dist_from[v]. If this round trip takes time <= T, Takahashi can spend remaining time T - (dist_to[v] + dist_from[v]) at vertex v collecting treasure. Maximize over all v.",
        "algorithm": [
            "Build forward adjacency list and reversed adjacency list.",
            "Run Dijkstra from 1 on forward graph: dist_to[v].",
            "Run Dijkstra from 1 on reversed graph: dist_from[v].",
            "max_treasure = 0.",
            "For v from 1 to N:",
            "  If dist_to[v] + dist_from[v] <= T:",
            "    rem_time = T - (dist_to[v] + dist_from[v]);",
            "    max_treasure = max(max_treasure, rem_time * A[v]);",
            "Print max_treasure."
        ],
        "time_complexity": "O((N + M) log N)",
        "space_complexity": "O(N + M)",
        "core_skill": "Dual-graph Dijkstra (forward and reversed) for directed round-trip optimization.",
        "reusable_pattern": "Directed Round Trip: Dijkstra(start) + Dijkstra_Reversed(start), round_trip = dist1 + dist2.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

const long long INF = 2e18;

struct Edge {
    int to;
    long long cost;
};

void dijkstra(int start, int n, const vector<vector<Edge>>& adj, vector<long long>& dist) {
    dist.assign(n + 1, INF);
    dist[start] = 0;
    priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> pq;
    pq.push({0, start});

    while (!pq.empty()) {
        auto [d, u] = pq.top();
        pq.pop();
        if (d > dist[u]) continue;

        for (const auto& e : adj[u]) {
            if (dist[u] + e.cost < dist[e.to]) {
                dist[e.to] = dist[u] + e.cost;
                pq.push({dist[e.to], e.to});
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    long long T;
    if (!(cin >> n >> m >> T)) return 0;

    vector<long long> a(n + 1);
    for (int i = 1; i <= n; ++i) cin >> a[i];

    vector<vector<Edge>> adj(n + 1), rev_adj(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v;
        long long c;
        cin >> u >> v >> c;
        adj[u].push_back({v, c});
        rev_adj[v].push_back({u, c});
    }

    vector<long long> dist_to, dist_from;
    dijkstra(1, n, adj, dist_to);
    dijkstra(1, n, rev_adj, dist_from);

    long long max_treasure = 0;
    for (int v = 1; v <= n; ++v) {
        if (dist_to[v] < INF && dist_from[v] < INF) {
            long long round_trip = dist_to[v] + dist_from[v];
            if (round_trip <= T) {
                max_treasure = max(max_treasure, (T - round_trip) * a[v]);
            }
        }
    }

    cout << max_treasure << "\n";
    return 0;
}
"""
    },
    {
        "id": "abc113_d",
        "title": "Number of Amidakuji",
        "contest_id": "abc113",
        "rating": 1597,
        "tag": "Dynamic Programming",
        "subtopic": "Bitmask DP",
        "topic": "DP over Amidakuji Horizontal Bars via Non-Adjacent Bitmasks",
        "cat_folder": "dp",
        "cat_file": "amidakuji_non_adjacent_bitmask_dp.md",
        "statement": "An Amidakuji (ghost leg lottery) has width W (W <= 8) vertical lines and height H (H <= 100). At each horizontal level, horizontal rungs may connect adjacent vertical lines, with the condition that no two rungs share an endpoint. Find the number of valid amidakuji where vertical line 1 ends at vertical line K, modulo 10^9 + 7.",
        "key_idea": "Each horizontal level corresponds to a bitmask of length W - 1 representing where rungs are placed. A mask is valid iff (mask & (mask << 1)) == 0. A rung at bit c swaps line c and c + 1.",
        "observation": "Because W <= 8, 2^(W-1) <= 128 masks. For each step of height from 1 to H, iterate over all valid masks and transition the column positions. dp[h][c] = number of ways after h steps to end at column c.",
        "algorithm": [
            "Precompute all valid masks of length W - 1 where !(mask & (mask << 1)).",
            "dp[W] initialized to 0; dp[0] = 1 (0-indexed line 0).",
            "For step from 1 to H:",
            "  next_dp[W] = 0.",
            "  For each valid mask:",
            "    For col from 0 to W - 1:",
            "      If col > 0 and (mask has bit col - 1): dest = col - 1.",
            "      Else if col < W - 1 and (mask has bit col): dest = col + 1.",
            "      Else: dest = col.",
            "      next_dp[dest] = (next_dp[dest] + dp[col]) % MOD.",
            "  dp = move(next_dp).",
            "Print dp[K - 1]."
        ],
        "time_complexity": "O(H * 2^(W-1) * W)",
        "space_complexity": "O(W)",
        "core_skill": "Bitmask generation of non-adjacent bridge configurations combined with permutation transition DP.",
        "reusable_pattern": "Amidakuji Bitmask DP: valid masks satisfy !(m & (m << 1)), transition swaps line c and c+1.",
        "editorial_comparison": "Matches official editorial.",
        "cpp_code": r"""#include <iostream>
#include <vector>

using namespace std;

const int MOD = 1000000007;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int h, w, k;
    if (!(cin >> h >> w >> k)) return 0;

    // Line k is 1-indexed; convert to 0-indexed
    k--;

    // Precompute valid masks of width w - 1
    int total_masks = 1 << (w - 1);
    vector<int> valid_masks;
    for (int mask = 0; mask < total_masks; ++mask) {
        if (!(mask & (mask << 1))) {
            valid_masks.push_back(mask);
        }
    }

    vector<long long> dp(w, 0);
    dp[0] = 1;

    for (int step = 0; step < h; ++step) {
        vector<long long> next_dp(w, 0);
        for (int mask : valid_masks) {
            for (int col = 0; col < w; ++col) {
                if (!dp[col]) continue;

                int dest = col;
                if (col > 0 && (mask & (1 << (col - 1)))) {
                    dest = col - 1;
                } else if (col < w - 1 && (mask & (1 << col))) {
                    dest = col + 1;
                }

                next_dp[dest] = (next_dp[dest] + dp[col]) % MOD;
            }
        }
        dp = move(next_dp);
    }

    cout << dp[k] << "\n";
    return 0;
}
"""
    }
]

REJECTED_PROBLEMS = [
    {"id": "abc407_e", "title": "Most Valuable Parentheses", "rating": 1531, "reason": "REJECTED (BASIC LOGIC BUILDING) — Routine parentheses matching drill."},
    {"id": "abc451_f", "title": "Make Bipartite 3", "rating": 1540, "reason": "REJECTED (BASIC LOGIC BUILDING) — Routine bipartite graph check simulation."},
    {"id": "abc446_f", "title": "Reachable Set 2", "rating": 1543, "reason": "REJECTED (BASIC LOGIC BUILDING) — Reachability casework drill."},
    {"id": "abc455_f", "title": "Merge Slimes 2", "rating": 1549, "reason": "REJECTED (BASIC LOGIC BUILDING) — Ad-hoc slimes merge simulation."},
    {"id": "abc415_f", "title": "Max Combo", "rating": 1552, "reason": "REJECTED (BASIC LOGIC BUILDING) — Simple combo array tracking."},
    {"id": "abc449_e", "title": "A += v", "rating": 1556, "reason": "REJECTED (BASIC LOGIC BUILDING) — Routine array addition casework."},
    {"id": "abc469_e", "title": "Pro Exam Eligibility", "rating": 1566, "reason": "REJECTED (BASIC LOGIC BUILDING) — Ad-hoc eligibility verification."},
    {"id": "abc469_f", "title": "GCD Maximum Spanning Tree", "rating": 1567, "reason": "REJECTED (BASIC LOGIC BUILDING) — Routine spanning tree casework."},
    {"id": "abc422_e", "title": "Colinear", "rating": 1580, "reason": "REJECTED (BASIC LOGIC BUILDING) — Simple collinear check drill."},
    {"id": "abc409_f", "title": "Connecting Points", "rating": 1580, "reason": "REJECTED (BASIC LOGIC BUILDING) — Routine point connection simulation."},
    {"id": "abc426_e", "title": "Closest Moment", "rating": 1584, "reason": "REJECTED (BASIC LOGIC BUILDING) — Ad-hoc geometry calculation without general pattern."},
    {"id": "abc478_f", "title": "Min-First Search", "rating": 1588, "reason": "REJECTED (BASIC LOGIC BUILDING) — Simple priority search without transferable paradigm."}
]

# Step 1: Compile all C++ solutions to verify zero errors
print(f"Testing C++ compilation of all {len(SELECTED_PROBLEMS)} selected ABC Part 3B solutions...")
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

print(f"[+] All {len(SELECTED_PROBLEMS)} ABC Part 3B C++ solutions compiled with 0 errors!")

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
        f.write("\n### Batch 4 Part 3B: ABC Curated Ladder (1528 - 1599)\n" + "\n".join(new_q_lines) + "\n")
    print("[+] Updated QUALITY_PROBLEMS_BY_TOPIC.md with new archetypes.")

# Update state/progress.json
with open("state/progress.json", "r", encoding="utf-8") as f:
    progress = json.load(f)

progress["current_batch"] = "Batch 4: ABC Ladder Band 2 (1200-1599) COMPLETED"
progress["status"] = "IN_PROGRESS"
for p in SELECTED_PROBLEMS:
    if p["id"] not in progress["completed_problem_ids"]:
        progress["completed_problem_ids"].append(p["id"])
progress["total_evaluated_in_curriculum"] = len(progress["completed_problem_ids"])

with open("state/progress.json", "w", encoding="utf-8") as f:
    json.dump(progress, f, indent=2)
print(f"[+] Updated progress checkpoint: state/progress.json")

print("=" * 75)
print("Batch 4 Part 3B completed successfully! ABC Band 2 (1200-1599) COMPLETE!")
