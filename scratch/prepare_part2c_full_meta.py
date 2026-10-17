import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/part2c_scraped_tasks.json', 'r', encoding='utf-8') as f:
    scraped = json.load(f)

# Helper for sample retrieval
def get_samples(pid):
    s_list = scraped[pid]['samples']
    # If samples were structured in raw_pres (e.g. arc052_c)
    if not s_list and pid == 'arc052_c':
        pres = scraped[pid]['raw_pres']
        # pre 1, 2 is sample 1; 3, 4 is sample 2; 5, 6 is sample 3
        s_list = [
            {'input': pres[1], 'output': pres[2]},
            {'input': pres[3], 'output': pres[4]},
            {'input': pres[5], 'output': pres[6]}
        ]
    # Remove duplicates from s_list
    seen = set()
    uniq = []
    for s in s_list:
        key = (s['input'].strip(), s['output'].strip())
        if key not in seen:
            seen.add(key)
            uniq.append(s)
    return uniq

meta = [
    {
        "id": "arc202_c",
        "contest_id": "arc202",
        "title": "C. Repunits",
        "rating": 2274,
        "domain": "Number Theory",
        "subtopic": "Multiplicative Functions",
        "topic": "Mobius Function and Mobius Inversion",
        "category_file": "categories/number_theory/mobius_inversion_repunit_lcm.md",
        "slug": "mobius_inversion_repunit_lcm",
        "core_tags": ["Number Theory", "Möbius Inversion", "Repunits", "Strong Divisibility Sequence", "LCM", "Sieve"],
        "invariant": "Repunits $R_n = (10^n - 1)/9$ form a strong divisibility sequence satisfying $\\gcd(R_a, R_b) = R_{\\gcd(a, b)}$. By multiplicative Möbius inversion, $R_n = \\prod_{d | n} f(d)$ where $f(d) = \\prod_{c | d} R_c^{\\mu(d/c)}$, and $\\mathrm{LCM}(R_{A_1}, \\dots, R_{A_k}) = \\prod_{d \\in \\bigcup_{i=1}^k \\mathrm{divisors}(A_i)} f(d)$.",
        "editorial_reduction": "1. Note that $\\gcd(10^a - 1, 10^b - 1) = 10^{\\gcd(a, b)} - 1$, which implies repunits $R_n = (10^n - 1)/9$ satisfy $\\gcd(R_a, R_b) = R_{\\gcd(a, b)}$.\\n2. For any strong divisibility sequence, the lattice of elements under $\\gcd$ and $\\mathrm{lcm}$ is isomorphic to the divisibility poset of their indices. Decomposing $R_n$ multiplicatively via Möbius inversion yields $R_n = \\prod_{d | n} f(d)$ where $f(d) = \\prod_{c | d} R_c^{\\mu(d/c)} \\pmod{998244353}$.\\n3. The least common multiple of any subset is the product of $f(d)$ over the union of all divisors of the indices: $\\mathrm{LCM}(R_{A_1}, \\dots, R_{A_k}) = \\prod_{d \\in D_k} f(d)$, where $D_k = \\bigcup_{i=1}^k \\mathrm{divisors}(A_i)$.\\n4. Precompute $\\mu(k)$, $R_k$, and $f(d)$ for all $d \\le 200000$ using a linear sieve and divisor transitions in $O(M \\log M)$ where $M = 2 \\times 10^5$. Maintain a global boolean array `seen[d]` and running cumulative product. For each query $A_k$, factorize $A_k$ in $O(d(A_k))$, multiply in $f(d)$ for newly discovered divisors, and output the cumulative LCM in $O(1)$.",
        "cpp_solution": r"""#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

static const int MOD = 998244353;

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

const int MAXV = 200000;
int mu[MAXV + 1];
vector<int> primes;
bool is_prime[MAXV + 1];
long long R[MAXV + 1];
long long invR[MAXV + 1];
long long f[MAXV + 1];
vector<int> divisors_list[MAXV + 1];
bool seen[MAXV + 1];

void sieve() {
    fill(is_prime + 2, is_prime + MAXV + 1, true);
    mu[1] = 1;
    for (int i = 2; i <= MAXV; i++) {
        if (is_prime[i]) {
            primes.push_back(i);
            mu[i] = -1;
        }
        for (int p : primes) {
            if (i * p > MAXV) break;
            is_prime[i * p] = false;
            if (i % p == 0) {
                mu[i * p] = 0;
                break;
            } else {
                mu[i * p] = -mu[i];
            }
        }
    }

    long long inv9 = modInverse(9);
    for (int i = 1; i <= MAXV; i++) {
        long long num = (power(10, i) - 1 + MOD) % MOD;
        R[i] = (num * inv9) % MOD;
        invR[i] = modInverse(R[i]);
        f[i] = 1;
    }

    for (int c = 1; c <= MAXV; c++) {
        for (int d = c; d <= MAXV; d += c) {
            divisors_list[d].push_back(c);
            int k = d / c;
            if (mu[k] == 1) {
                f[d] = (f[d] * R[c]) % MOD;
            } else if (mu[k] == -1) {
                f[d] = (f[d] * invR[c]) % MOD;
            }
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    sieve();

    int n;
    if (!(cin >> n)) return 0;
    long long current_lcm = 1;
    for (int i = 0; i < n; i++) {
        int a;
        cin >> a;
        for (int d : divisors_list[a]) {
            if (!seen[d]) {
                seen[d] = true;
                current_lcm = (current_lcm * f[d]) % MOD;
            }
        }
        cout << current_lcm << "\n";
    }

    return 0;
}
""",
        "sample_tests": get_samples("arc202_c")
    },
    {
        "id": "abc215_g",
        "contest_id": "abc215",
        "title": "G. Colorful Candies 2",
        "rating": 2276,
        "domain": "Math",
        "subtopic": "Probabilities and Expected Values",
        "topic": "Probabilities and Expected Values",
        "category_file": "categories/math/expected_distinct_colors_hypergeometric_frequency_compression.md",
        "slug": "expected_distinct_colors_hypergeometric_frequency_compression",
        "core_tags": ["Math", "Expected Value", "Linearity of Expectation", "Hypergeometric Probability", "Frequency Compression"],
        "invariant": "By linearity of expectation, the expected number of distinct colors in a sample of size $K$ equals the sum of probabilities that each color is present: $E[C] = \\sum_{c} (1 - \\binom{N - cnt_c}{K} / \\binom{N}{K})$. Grouping colors by frequency compresses the evaluation to at most $\\sqrt{2N}$ unique sizes.",
        "editorial_reduction": "1. Express the expected number of distinct colors using indicator random variables for each color: $E_K = \\sum_{c} P(\\text{color } c \\text{ is chosen})$.\\n2. The probability of choosing color $c$ when sampling $K$ candies uniformly without replacement is $1 - \\frac{\\binom{N - cnt_c}{K}}{\\binom{N}{K}}$, where $cnt_c$ is the number of candies of color $c$.\\n3. Summing across all colors gives $E_K = (\\text{total distinct colors}) - \\frac{1}{\\binom{N}{K}} \\sum_{c} \\binom{N - cnt_c}{K}$.\\n4. Since $\\sum_{c} cnt_c = N$, the number of distinct frequency values $s \\in \\{cnt_c\\}$ is bounded by $\\sqrt{2N} \\approx 316$. We compress the sum to $\\sum_{s} \\text{freq}[s] \\cdot \\binom{N - s}{K}$, where $\\text{freq}[s]$ is the number of colors appearing exactly $s$ times.\\n5. For each $K = 1, \\dots, N$, compute the sum over all non-zero frequencies in $O(\\sqrt{N})$ time. Total time complexity is $O(N \\sqrt{N})$, completing comfortably within 0.1s.",
        "cpp_solution": r"""#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

static const int MOD = 998244353;

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

const int MAXN = 50005;
long long fact[MAXN];
long long invFact[MAXN];

void init_fact() {
    fact[0] = 1;
    invFact[0] = 1;
    for (int i = 1; i < MAXN; i++) {
        fact[i] = (fact[i - 1] * i) % MOD;
    }
    invFact[MAXN - 1] = modInverse(fact[MAXN - 1]);
    for (int i = MAXN - 2; i >= 1; i--) {
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

    init_fact();

    int n;
    if (!(cin >> n)) return 0;

    map<int, int> color_count;
    for (int i = 0; i < n; i++) {
        int c;
        cin >> c;
        color_count[c]++;
    }

    int total_colors = color_count.size();
    map<int, int> freq_count;
    for (auto const& [col, cnt] : color_count) {
        freq_count[cnt]++;
    }

    vector<pair<int, int>> freqs(freq_count.begin(), freq_count.end());

    for (int k = 1; k <= n; k++) {
        long long inv_ways = modInverse(nCr(n, k));
        long long sum_unselected = 0;
        for (auto const& [s, num_cols] : freqs) {
            long long ways = nCr(n - s, k);
            if (ways > 0) {
                sum_unselected = (sum_unselected + 1LL * num_cols * ways) % MOD;
            }
        }
        long long unselected_prob = (sum_unselected * inv_ways) % MOD;
        long long ans = (total_colors - unselected_prob + MOD) % MOD;
        cout << ans << "\n";
    }

    return 0;
}
""",
        "sample_tests": get_samples("abc215_g")
    },
    {
        "id": "arc175_d",
        "contest_id": "arc175",
        "title": "D. LIS on Tree 2",
        "rating": 2276,
        "domain": "Basics",
        "subtopic": "Greedy and Constructive",
        "topic": "Basic Constructive Algorithms",
        "category_file": "categories/basics/constructive_tree_permutation_target_lis_sum.md",
        "slug": "constructive_tree_permutation_target_lis_sum",
        "core_tags": ["Basics", "Constructive", "Tree", "LIS", "Greedy Subtree Sum"],
        "invariant": "In any rooted tree, extending the LIS at vertex $u$ increments the LIS value of all vertices in its subtree $T_u$, contributing exactly $|T_u|$ to $\\sum L_i$. Since subtree sizes form an additive hierarchy, greedy selection by descending subtree size solves the subset sum exactly, and ranking vertices by signed depths $x_u = \\pm d_u$ reconstructs the permutation.",
        "editorial_reduction": "1. Along any root-to-node path, adding node $u$ either increments the LIS by 1 or leaves it unchanged. Minimum total sum is $N$ (strictly decreasing top-to-bottom); maximum is $N + \\sum_{i=1}^N d_i = \\sum_{i=1}^N |T_i|$. If $K < N$ or $K > N + \\sum d_i$, output `No`.\\n2. If vertex $u$ is chosen to extend the LIS, it adds $|T_u|$ to the total sum $\\sum L_i$. The problem reduces to choosing a subset of vertices $S \\subseteq \\{2, \\dots, N\\}$ such that $\\sum_{u \\in S} |T_u| = K - N$.\\n3. By tree structural induction, greedy selection over $u \\in \\{2, \\dots, N\\}$ sorted by descending $|T_u|$ is guaranteed to achieve $K - N$ if achievable.\\n4. To construct $P$: define $x_1 = 0$; for each $i \\ge 2$, set $x_i = d_i$ if $i \\in S$, and $x_i = -d_i$ if $i \\notin S$. Sorting all vertices by $x_i$ ascending and assigning permutation labels $1, \\dots, N$ ensures that along every branch, vertices in $S$ are strictly increasing while vertices not in $S$ are strictly smaller, achieving the target LIS sum in $O(N \\log N)$.",
        "cpp_solution": r"""#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

using namespace std;

int n;
long long k;
vector<vector<int>> adj;
vector<int> sz;
vector<int> depth;
vector<int> parent_node;
vector<bool> in_S;

void dfs(int u, int p, int d) {
    depth[u] = d;
    parent_node[u] = p;
    sz[u] = 1;
    for (int v : adj[u]) {
        if (v != p) {
            dfs(v, u, d + 1);
            sz[u] += sz[v];
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    if (!(cin >> n >> k)) return 0;

    adj.assign(n + 1, vector<int>());
    for (int i = 0; i < n - 1; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    sz.assign(n + 1, 0);
    depth.assign(n + 1, 0);
    parent_node.assign(n + 1, 0);
    dfs(1, 0, 0);

    long long sum_depth = 0;
    for (int i = 1; i <= n; i++) {
        sum_depth += depth[i];
    }

    long long min_val = n;
    long long max_val = n + sum_depth;

    if (k < min_val || k > max_val) {
        cout << "No\n";
        return 0;
    }

    long long rem = k - n;
    vector<int> order(n - 1);
    iota(order.begin(), order.end(), 2);
    sort(order.begin(), order.end(), [](int a, int b) {
        return sz[a] > sz[b];
    });

    in_S.assign(n + 1, false);
    for (int u : order) {
        if (sz[u] <= rem) {
            in_S[u] = true;
            rem -= sz[u];
        }
    }

    if (rem != 0) {
        cout << "No\n";
        return 0;
    }

    vector<pair<int, int>> nodes;
    nodes.reserve(n);
    nodes.push_back({0, 1});
    for (int i = 2; i <= n; i++) {
        int val = in_S[i] ? depth[i] : -depth[i];
        nodes.push_back({val, i});
    }

    sort(nodes.begin(), nodes.end(), [](const pair<int, int>& a, const pair<int, int>& b) {
        if (a.first != b.first) return a.first < b.first;
        return a.second < b.second;
    });

    vector<int> P(n + 1);
    for (int rank = 1; rank <= n; rank++) {
        int u = nodes[rank - 1].second;
        P[u] = rank;
    }

    cout << "Yes\n";
    for (int i = 1; i <= n; i++) {
        cout << P[i] << (i == n ? "" : " ");
    }
    cout << "\n";

    return 0;
}
""",
        "sample_tests": get_samples("arc175_d")
    },
    {
        "id": "abc143_f",
        "contest_id": "abc143",
        "title": "F. Distinct Numbers",
        "rating": 2277,
        "domain": "Basics",
        "subtopic": "Leveraging Monotonicity",
        "topic": "Binary Search",
        "category_file": "categories/basics/binary_search_frequency_capped_subset_partition.md",
        "slug": "binary_search_frequency_capped_subset_partition",
        "core_tags": ["Basics", "Binary Search", "Prefix Sum", "Gale-Ryser", "Frequency Capping"],
        "invariant": "$X$ operations choosing $K$ distinct elements are feasible if and only if the total capped count $\\sum_i \\min(c_i, X) \\ge K \\cdot X$. Inverting this relationship allows determining the maximum $X$ for each $K$ via binary search or suffix-maximum sweep over $K \\le \\lfloor S(X) / X \\rfloor$.",
        "editorial_reduction": "1. Let $c_1, \\dots, c_m$ be the frequencies of each distinct number in the input. In $X$ operations of size $K$, each distinct number can be chosen at most once per operation, hence at most $\\min(c_i, X)$ times in total.\\n2. By the Gale-Ryser / Hajnal-Szemerédi theorem for bipartite degree sequences, the condition $\\sum_i \\min(c_i, X) \\ge K \\cdot X$ is both necessary and sufficient to form $X$ subsets of size $K$ with distinct elements.\\n3. Let $S(X) = \\sum_i \\min(c_i, X)$. By precomputing the frequency distribution of counts using prefix sums, $S(X)$ can be computed in $O(1)$ for each $X \\in [1, N]$.\\n4. For each $X$, the maximum subset size for which $X$ operations is possible is $K_{max}(X) = \\lfloor S(X) / X \\rfloor$. Setting $\\text{ans}[K_{max}(X)] = \\max(\\text{ans}[K_{max}(X)], X)$ and taking a backward suffix maximum sweep $\\text{ans}[K] = \\max(\\text{ans}[K], \\text{ans}[K+1])$ yields the answer for all $K \\in [1, N]$ in $O(N)$ total time.",
        "cpp_solution": r"""#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> freq(n + 1, 0);
    for (int i = 0; i < n; i++) {
        int a;
        cin >> a;
        freq[a]++;
    }

    vector<int> count_of_freq(n + 1, 0);
    for (int i = 1; i <= n; i++) {
        if (freq[i] > 0) {
            count_of_freq[freq[i]]++;
        }
    }

    vector<long long> sum_c(n + 1, 0);
    vector<long long> count_c(n + 1, 0);
    for (int v = 1; v <= n; v++) {
        sum_c[v] = sum_c[v - 1] + 1LL * v * count_of_freq[v];
        count_c[v] = count_c[v - 1] + count_of_freq[v];
    }

    long long total_elements = count_c[n];

    vector<int> ans(n + 2, 0);
    for (int x = 1; x <= n; x++) {
        long long s_x = sum_c[x] + 1LL * x * (total_elements - count_c[x]);
        int k = s_x / x;
        if (k > n) k = n;
        ans[k] = max(ans[k], x);
    }

    for (int k = n; k >= 1; k--) {
        ans[k] = max(ans[k], ans[k + 1]);
    }

    for (int k = 1; k <= n; k++) {
        cout << ans[k] << "\n";
    }

    return 0;
}
""",
        "sample_tests": get_samples("abc143_f")
    },
    {
        "id": "abc273_f",
        "contest_id": "abc273",
        "title": "F. Hammer 2",
        "rating": 2277,
        "domain": "Dynamic Programming (DP)",
        "subtopic": "Classic DP",
        "topic": "Interval DP / Range DP / Matrix Chain Multiplication (MCM)",
        "category_file": "categories/dynamic_programming_dp/interval_dp_1d_coordinate_hammer_wall_reachability.md",
        "slug": "interval_dp_1d_coordinate_hammer_wall_reachability",
        "core_tags": ["Dynamic Programming (DP)", "Interval DP", "Coordinate Compression", "1D Navigation"],
        "invariant": "On a 1D line starting at 0, the set of visited coordinates always forms a contiguous interval $[l, r]$ containing 0, with the player situated at either $l$ or $r$. Expanding to $l - 1$ or $r + 1$ is valid if and only if any wall encountered has its associated hammer located within $[l, r]$.",
        "editorial_reduction": "1. Collect all critical points: start 0, goal $X$, wall locations $Y_i$, and hammer locations $Z_i$ ($2N + 2 \\le 3002$ points). Compress coordinates into a sorted array of unique values.\\n2. Define interval DP state: $dp[l][r][0]$ is the minimum distance to have visited the compressed range $[l, r]$ ending at left endpoint $l$; $dp[l][r][1]$ is the minimum distance ending at right endpoint $r$.\\n3. Transitions from state $(l, r, \\text{side})$ expand by 1 step: moving left to $l - 1$ is allowed if $l - 1$ is not a wall or if its required hammer index lies in $[l, r]$; moving right to $r + 1$ is similarly conditioned.\\n4. Once an interval $[l, r]$ covers the goal coordinate $X$, update the global answer $\\text{ans} = \\min(\\text{ans}, dp[l][r][0], dp[l][r][1])$. Total complexity is $O(M^2)$ where $M \\le 3000$, executing in under 0.1s.",
        "cpp_solution": r"""#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

const long long INF = 1e18;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    long long x;
    if (!(cin >> n >> x)) return 0;

    vector<long long> y(n), z(n);
    vector<long long> coords;
    coords.push_back(0);
    coords.push_back(x);

    for (int i = 0; i < n; i++) {
        cin >> y[i];
        coords.push_back(y[i]);
    }
    for (int i = 0; i < n; i++) {
        cin >> z[i];
        coords.push_back(z[i]);
    }

    sort(coords.begin(), coords.end());
    coords.erase(unique(coords.begin(), coords.end()), coords.end());

    int m = coords.size();
    int s = lower_bound(coords.begin(), coords.end(), 0) - coords.begin();
    int g = lower_bound(coords.begin(), coords.end(), x) - coords.begin();

    vector<int> req(m, -1);
    for (int i = 0; i < n; i++) {
        int wall_idx = lower_bound(coords.begin(), coords.end(), y[i]) - coords.begin();
        int hammer_idx = lower_bound(coords.begin(), coords.end(), z[i]) - coords.begin();
        req[wall_idx] = hammer_idx;
    }

    vector<vector<vector<long long>>> dp(m, vector<vector<long long>>(m, vector<long long>(2, INF)));
    dp[s][s][0] = 0;
    dp[s][s][1] = 0;

    long long ans = INF;

    for (int len = 1; len <= m; len++) {
        for (int l = 0; l + len - 1 < m; l++) {
            int r = l + len - 1;

            if (l <= g && g <= r) {
                ans = min({ans, dp[l][r][0], dp[l][r][1]});
                continue;
            }

            for (int side = 0; side < 2; side++) {
                long long cur_dist = dp[l][r][side];
                if (cur_dist >= INF) continue;

                long long cur_pos = (side == 0 ? coords[l] : coords[r]);

                if (l > 0) {
                    int nxt = l - 1;
                    int needed_hammer = req[nxt];
                    if (needed_hammer == -1 || (needed_hammer >= l && needed_hammer <= r)) {
                        long long d = cur_dist + abs(coords[nxt] - cur_pos);
                        dp[nxt][r][0] = min(dp[nxt][r][0], d);
                    }
                }

                if (r + 1 < m) {
                    int nxt = r + 1;
                    int needed_hammer = req[nxt];
                    if (needed_hammer == -1 || (needed_hammer >= l && needed_hammer <= r)) {
                        long long d = cur_dist + abs(coords[nxt] - cur_pos);
                        dp[l][nxt][1] = min(dp[l][nxt][1], d);
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
""",
        "sample_tests": get_samples("abc273_f")
    },
    {
        "id": "arc052_c",
        "contest_id": "arc052",
        "title": "C. 高橋くんと不思議な道",
        "rating": 2277,
        "domain": "Graph Theory",
        "subtopic": "Shortest Paths",
        "topic": "Dijkstra's Algorithm",
        "category_file": "categories/graph_theory/dijkstra_quadratic_b_edge_state_pruning.md",
        "slug": "dijkstra_quadratic_b_edge_state_pruning",
        "core_tags": ["Graph Theory", "Shortest Paths", "Dijkstra", "Quadratic Edge Cost", "State Pruning"],
        "invariant": "Using $k$ Type B edges incurs quadratic cost $k(k+1)/2$. Since any simple Type A path costs $< N$, taking more than $\\sqrt{2N} \\approx 141$ Type B edges cannot compensate for Type A savings. For $k < B$, we maintain exact Type A cost $dist[u][k]$; for $k \\ge B$, only the minimum $k$ is needed.",
        "editorial_reduction": "1. Type A edges cost 1 each, while the $k$-th Type B edge costs $k$, so traversing $k$ Type B edges adds $\\sum_{j=1}^k j = \\frac{k(k+1)}{2}$.\\n2. The total cost of reaching vertex $u$ with $a$ Type A edges and $k$ Type B edges is $a + \\frac{k(k+1)}{2}$.\\n3. For $k \\le B = 150$, maintain $dist[u][k]$, the minimum Type A count to reach $u$ with exactly $k$ Type B edges. State transitions in Dijkstra prioritize total cost $a + k(k+1)/2$.\\n4. For $k \\ge B$, each additional Type B edge costs $\\ge 150 > N$. Two paths with $k_1 < k_2$ can never be overtaken by $k_2$ because saving at most $N$ Type A edges cannot offset the quadratic penalty. Thus for $k \\ge B$, we only maintain $\\min(k)$ at each vertex.\\n5. Run Dijkstra on states $(u, k, a)$ with this two-regime pruning. Total state count is $O(N \\sqrt{N} + M)$, which solves the problem in $O(N \\sqrt{N} \\log(N \\sqrt{N}))$.",
        "cpp_solution": r"""#include <iostream>
#include <vector>
#include <queue>
#include <tuple>
#include <algorithm>

using namespace std;

const long long INF = 1e18;

struct Edge {
    int to;
    int type;
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<Edge>> adj(n);
    for (int i = 0; i < m; i++) {
        int c, u, v;
        cin >> c >> u >> v;
        adj[u].push_back({v, c});
        adj[v].push_back({u, c});
    }

    const int B = 150;
    vector<vector<int>> dist(n, vector<int>(B, 1e9));
    vector<pair<int, int>> min_b(n, {1e9, 1e9});

    typedef tuple<long long, int, int, int> State;
    priority_queue<State, vector<State>, greater<State>> pq;

    dist[0][0] = 0;
    pq.push({0, 0, 0, 0});

    vector<long long> ans(n, INF);

    while (!pq.empty()) {
        auto [cost, u, k, a] = pq.top();
        pq.pop();

        ans[u] = min(ans[u], cost);

        if (k < B) {
            if (a > dist[u][k]) continue;
        } else {
            if (make_pair(k, a) > min_b[u]) continue;
        }

        for (const auto& e : adj[u]) {
            int v = e.to;
            int nk = k + e.type;
            int na = a + (1 - e.type);
            long long ncost = na + 1LL * nk * (nk + 1) / 2;

            if (nk < B) {
                if (na < dist[v][nk]) {
                    dist[v][nk] = na;
                    pq.push({ncost, v, nk, na});
                }
            } else {
                pair<int, int> p = {nk, na};
                if (p < min_b[v]) {
                    min_b[v] = p;
                    pq.push({ncost, v, nk, na});
                }
            }
        }
    }

    for (int i = 0; i < n; i++) {
        cout << ans[i] << "\n";
    }

    return 0;
}
""",
        "sample_tests": get_samples("arc052_c")
    },
    {
        "id": "arc080_c",
        "contest_id": "arc080",
        "title": "E. Young Maids",
        "rating": 2277,
        "domain": "Data Structures (DS)",
        "subtopic": "Segment Tree",
        "topic": "Segment Tree (Point Update Range Query)",
        "category_file": "categories/data_structures_ds/segment_tree_lexicographical_permutation_rmq_pair_peeling.md",
        "slug": "segment_tree_lexicographical_permutation_rmq_pair_peeling",
        "core_tags": ["Data Structures (DS)", "Segment Tree", "Priority Queue", "Greedy", "Parity RMQ"],
        "invariant": "In any sequence of adjacent pair removals, every removed pair $(x, y)$ originally occupied an even-length interval between them and had alternating parities relative to the subarray boundary. The problem greedily decouples into independent even-length subsegments $[l, pos(x)-1]$, $[pos(x)+1, pos(y)-1]$, and $[pos(y)+1, r]$ managed by a priority queue.",
        "editorial_reduction": "1. Prepending pairs to $q$ means the first pair in $q$ was the LAST pair removed from $p$. In reverse, to make $q$ lexicographically smallest, we greedily pick the minimum possible $x$ and corresponding $y$ at each step.\\n2. When two elements $x, y$ are removed from an even-length interval $[l, r]$, all elements between them must have been removed in pairs, meaning the number of elements between $x$ and $y$ is even, and the elements before $x$ and after $y$ also have even counts.\\n3. Hence, $x$ must share the same parity as $l$, and $y$ must have opposite parity and appear after $x$. To minimize $(x, y)$, choose $x = \\arg\\min_{i \\equiv l \\pmod 2, i \\in [l, r]} p[i]$ and $y = \\arg\\min_{j \\not\\equiv l \\pmod 2, j \\in [pos(x)+1, r]} p[j]$.\\n4. After choosing $(x, y)$, the interval $[l, r]$ splits into up to 3 even-length intervals: $[l, pos(x)-1]$, $[pos(x)+1, pos(y)-1]$, and $[pos(y)+1, r]$.\\n5. Maintain all active intervals in a `std::priority_queue` keyed by their minimum $x$ value. Finding $(x, y)$ per interval is performed via RMQ on two Segment Trees (one for even indices, one for odd). Overall time is $O(N \\log N)$.",
        "cpp_solution": r"""#include <iostream>
#include <vector>
#include <queue>
#include <tuple>
#include <algorithm>

using namespace std;

const int INF = 1e9;

struct SegmentTree {
    int n;
    vector<pair<int, int>> tree;

    void init(int n_) {
        n = n_;
        tree.assign(4 * n + 1, {INF, -1});
    }

    void update(int node, int l, int r, int idx, int val) {
        if (l == r) {
            tree[node] = {val, idx};
            return;
        }
        int mid = (l + r) / 2;
        if (idx <= mid) update(2 * node, l, mid, idx, val);
        else update(2 * node + 1, mid + 1, r, idx, val);
        tree[node] = min(tree[2 * node], tree[2 * node + 1]);
    }

    pair<int, int> query(int node, int l, int r, int ql, int qr) {
        if (ql > r || qr < l) return {INF, -1};
        if (ql <= l && r <= qr) return tree[node];
        int mid = (l + r) / 2;
        return min(query(2 * node, l, mid, ql, qr), query(2 * node + 1, mid + 1, r, ql, qr));
    }
} st[2];

struct Interval {
    int l, r;
    int x_val, x_idx;
    int y_val, y_idx;

    bool operator>(const Interval& other) const {
        return x_val > other.x_val;
    }
};

Interval make_interval(int l, int r, int n) {
    int parity_l = l % 2;
    pair<int, int> qx = st[parity_l].query(1, 0, n - 1, l, r);
    int x_val = qx.first;
    int x_idx = qx.second;

    int parity_r = 1 - parity_l;
    pair<int, int> qy = st[parity_r].query(1, 0, n - 1, x_idx + 1, r);
    int y_val = qy.first;
    int y_idx = qy.second;

    return {l, r, x_val, x_idx, y_val, y_idx};
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> p(n);
    st[0].init(n);
    st[1].init(n);

    for (int i = 0; i < n; i++) {
        cin >> p[i];
        st[i % 2].update(1, 0, n - 1, i, p[i]);
    }

    priority_queue<Interval, vector<Interval>, greater<Interval>> pq;
    pq.push(make_interval(0, n - 1, n));

    vector<int> q;
    q.reserve(n);

    while (!pq.empty()) {
        Interval cur = pq.top();
        pq.pop();

        q.push_back(cur.x_val);
        q.push_back(cur.y_val);

        if (cur.l <= cur.x_idx - 1) {
            pq.push(make_interval(cur.l, cur.x_idx - 1, n));
        }
        if (cur.x_idx + 1 <= cur.y_idx - 1) {
            pq.push(make_interval(cur.x_idx + 1, cur.y_idx - 1, n));
        }
        if (cur.y_idx + 1 <= cur.r) {
            pq.push(make_interval(cur.y_idx + 1, cur.r, n));
        }
    }

    for (int i = 0; i < n; i++) {
        cout << q[i] << (i == n - 1 ? "" : " ");
    }
    cout << "\n";

    return 0;
}
""",
        "sample_tests": get_samples("arc080_c")
    },
    {
        "id": "arc227_d",
        "contest_id": "arc227",
        "title": "D. Median of Binary Strings",
        "rating": 2277,
        "domain": "Graph Theory",
        "subtopic": "Satisfiability",
        "topic": "2 SAT",
        "category_file": "categories/graph_theory/two_sat_majority_polymorphism_pairwise_projection.md",
        "slug": "two_sat_majority_polymorphism_pairwise_projection",
        "core_tags": ["Graph Theory", "2-SAT", "Universal Algebra", "Majority Polymorphism", "Bitset Projection"],
        "invariant": "By universal algebra / clone theory, relations invariant under a majority (median) polymorphism are exactly 2-ary (binary clauses in 2-SAT). Therefore, a binary string $T$ can be generated by iterated median operations if and only if for every pair of coordinates $(j, k)$, the 2-bit projection $(T_j, T_k)$ appears in the initial set of strings.",
        "editorial_reduction": "1. The coordinate-wise majority operation on 3 binary vectors $D_i = \\text{maj}(A_i, B_i, C_i)$ satisfies the Pigeonhole Principle: out of 3 strings, any two properties holding in at least 2 strings must hold simultaneously in at least one string ($2 + 2 - 3 = 1$).\\n2. Consequently, if a specific pair of bits $(b_1, b_2)$ never appears at positions $(j, k)$ in any initial string $S_1, \\dots, S_N$, it can never appear in any string generated by majority operations.\\n3. Conversely, Baker-Pixley theorem and CSP polymorphism theory establish that 2-consistency is complete for majority polymorphisms: $T$ is derivable if and only if every pairwise restriction $(T_j, T_k)$ is realizable by some $S_i$.\\n4. For all pairs $0 \\le j < k < M$ and bit values $b_1, b_2 \\in \\{0, 1\\}$, precompute whether $(S_{i, j}, S_{i, k}) = (b_1, b_2)$ occurs using `std::bitset<500>` operations: $(\\text{mask}[j][b_1] \\& \\text{mask}[k][b_2]).\\text{any}()$. Precomputation takes $O(M^2 N / 64)$.\\n5. For each query string $T_q$, check all $M(M-1)/2$ coordinate pairs in $O(M^2)$. Total time is $O(M^2 N / 64 + Q M^2)$, running in under 0.05s.",
        "cpp_solution": r"""#include <iostream>
#include <vector>
#include <string>
#include <bitset>

using namespace std;

const int MAXM = 505;
const int MAXN = 505;

bitset<MAXN> pos_mask[MAXM][2];
bool valid_pair[MAXM][MAXM][2][2];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m, q;
    if (!(cin >> n >> m >> q)) return 0;

    for (int i = 0; i < n; i++) {
        string s;
        cin >> s;
        for (int j = 0; j < m; j++) {
            pos_mask[j][s[j] - '0'].set(i);
        }
    }

    for (int j = 0; j < m; j++) {
        for (int k = j; k < m; k++) {
            for (int b1 = 0; b1 < 2; b1++) {
                for (int b2 = 0; b2 < 2; b2++) {
                    if ((pos_mask[j][b1] & pos_mask[k][b2]).any()) {
                        valid_pair[j][k][b1][b2] = true;
                    }
                }
            }
        }
    }

    for (int qi = 0; qi < q; qi++) {
        string t;
        cin >> t;
        bool ok = true;
        for (int j = 0; j < m && ok; j++) {
            int b1 = t[j] - '0';
            for (int k = j; k < m; k++) {
                int b2 = t[k] - '0';
                if (!valid_pair[j][k][b1][b2]) {
                    ok = false;
                    break;
                }
            }
        }
        if (ok) {
            cout << "Yes\n";
        } else {
            cout << "No\n";
        }
    }

    return 0;
}
""",
        "sample_tests": get_samples("arc227_d")
    },
    {
        "id": "abc276_g",
        "contest_id": "abc276",
        "title": "G. Count Sequences",
        "rating": 2278,
        "domain": "Basics",
        "subtopic": "Basic Counting",
        "topic": "Stars and Bars",
        "category_file": "categories/basics/stars_and_bars_modular_difference_hockey_stick.md",
        "slug": "stars_and_bars_modular_difference_hockey_stick",
        "core_tags": ["Basics", "Basic Counting", "Stars and Bars", "Hockey Stick Identity", "Combinatorics"],
        "invariant": "Adjacent differences $d_i = a_{i+1} - a_i \\not\\equiv 0 \\pmod 3$ decompose as $x_i + 3y_i$ with $x_i \\in \\{1, 2\\}$. Fixing the count of $x_i = 1$ leaves the non-negative integer solutions to $\\sum y_i \\le L = \\lfloor(M-B)/3\\rfloor$, which evaluates in $O(1)$ via the hockey stick identity.",
        "editorial_reduction": "1. Let $d_i = a_{i+1} - a_i$. Since $a_i \\le a_{i+1}$ and $a_i \\not\\equiv a_{i+1} \\pmod 3$, each difference satisfies $d_i \\ge 1$ and $d_i \\bmod 3 \\in \\{1, 2\\}$.\\n2. Decompose $d_i = x_i + 3 y_i$ where $x_i \\in \\{1, 2\\}$ and $y_i \\ge 0$. Suppose $c$ of the $N-1$ differences have $x_i = 1$, and $(N-1-c)$ have $x_i = 2$. There are $\\binom{N-1}{c}$ ways to choose their positions.\\n3. The base sum is $B = c + 2(N-1-c)$. The condition $a_N \\le M$ becomes $a_1 + 3\\sum_{i=1}^{N-1} y_i \\le M - B$. For a fixed sum $K = \\sum y_i$, $a_1$ can take any integer value in $[0, M - B - 3K]$, which has $M - B + 1 - 3K$ choices.\\n4. Summing over $K$ from $0$ to $L = \\lfloor(M-B)/3\\rfloor$: $\\sum_{K=0}^L (M-B+1 - 3K) \\binom{K + N - 2}{N - 2} = (M-B+1)\\binom{L+N-1}{N-1} - 3(N-1)\\binom{L+N-1}{N}$ by the hockey stick identity!\\n5. Iterating $c$ from $0$ to $N-1$ computes each term in $O(1)$. Total time is $O(N + M)$ for precomputing factorials.",
        "cpp_solution": r"""#include <iostream>
#include <vector>

using namespace std;

static const int MOD = 998244353;

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

const int MAX = 14000005;
long long fact[MAX];
long long invFact[MAX];

void init_fact(int limit) {
    fact[0] = 1;
    invFact[0] = 1;
    for (int i = 1; i <= limit; i++) {
        fact[i] = (fact[i - 1] * i) % MOD;
    }
    invFact[limit] = modInverse(fact[limit]);
    for (int i = limit - 1; i >= 1; i--) {
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

    int n, m;
    if (!(cin >> n >> m)) return 0;

    int max_val = n + m / 3 + 5;
    init_fact(max_val);

    long long ans = 0;
    for (int c = 0; c < n; c++) {
        long long B = 1LL * c * 1 + 1LL * (n - 1 - c) * 2;
        if (B > m) continue;

        int L = (m - B) / 3;
        long long term1 = (m - B + 1) % MOD * nCr(L + n - 1, n - 1) % MOD;
        long long term2 = 3LL * (n - 1) % MOD * nCr(L + n - 1, n) % MOD;
        long long ways_y = (term1 - term2 + MOD) % MOD;
        long long ways_c = nCr(n - 1, c);

        ans = (ans + ways_c * ways_y) % MOD;
    }

    cout << ans << "\n";

    return 0;
}
""",
        "sample_tests": get_samples("abc276_g")
    },
    {
        "id": "arc170_d",
        "contest_id": "arc170",
        "title": "D. Triangle Card Game",
        "rating": 2279,
        "domain": "Game Theory",
        "subtopic": "Grundy Number / Nim",
        "topic": "Grundy Number and Basic Game Theory",
        "category_file": "categories/game_theory/triangle_card_game_minimax_distance_gap_search.md",
        "slug": "triangle_card_game_minimax_distance_gap_search",
        "core_tags": ["Game Theory", "Minimax", "Triangle Inequality", "Binary Search", "Extremal Analysis"],
        "invariant": "For an opening card $a \\in A$, Bob can win if and only if either playing $B_{\\min}$ prevents any triangle ($|a - B_{\\min}| < c < a + B_{\\min}$ has count 0 in $A \\setminus \\{a\\}$), or there exists $b \\in B$ whose distance to $A \\setminus \\{a\\}$ is at least $a$. Alice wins if she has any opening move where Bob cannot win.",
        "editorial_reduction": "1. Triangle condition for $(a, b, c)$ is $|a - b| < c < a + b$. Alice chooses $a$, Bob chooses $b$, then Alice chooses $c \\in A \\setminus \\{a\\}$. Alice wins if she can find any valid $c$.\\n2. For Bob to win against $a$: Bob must pick $b$ such that NO $c \\in A \\setminus \\{a\\}$ satisfies $|a - b| < c < a + b$. If $b < a$, Bob is always best off playing his minimum card $b = B_{\\min}$. Thus condition 1 is: no $c \\in A \\setminus \\{a\\}$ lies in $(|a - B_{\\min}|, a + B_{\\min})$.\\n3. If $b \\ge a$, Bob wins if $\\min_{c \\in A \\setminus \\{a\\}} |b - c| \\ge a$. Let $d_1(b)$ be the distance from $b$ to its closest neighbor in $A$, and $d_2(b)$ to its second closest neighbor.\\n4. The maximum distance in $A \\setminus \\{a\\}$ is $\\max(global\\_mx, max\\_d2[a])$, where $global\\_mx = \\max_{b} d_1(b)$ and $max\\_d2[a]$ is the maximum $d_2(b)$ over $b$ whose unique closest neighbor is $a$.\\n5. Bob wins against $a$ if condition 1 or condition 2 holds. If there is any $a$ where Bob loses both, Alice wins. Time complexity per test case is $O(N \\log N)$.",
        "cpp_solution": r"""#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

void solve_test() {
    int n;
    if (!(cin >> n)) return;

    vector<long long> a(n), b(n);
    for (int i = 0; i < n; i++) cin >> a[i];
    for (int i = 0; i < n; i++) cin >> b[i];

    sort(a.begin(), a.end());
    sort(b.begin(), b.end());

    long long b_min = b[0];

    long long global_mx = 0;
    vector<long long> max_d2(n, 0);

    for (int i = 0; i < n; i++) {
        long long val = b[i];
        int pos = lower_bound(a.begin(), a.end(), val) - a.begin();

        vector<pair<long long, int>> cands;
        for (int offset = -2; offset <= 2; offset++) {
            int idx = pos + offset;
            if (idx >= 0 && idx < n) {
                cands.push_back({abs(val - a[idx]), idx});
            }
        }
        sort(cands.begin(), cands.end());

        long long d1 = cands[0].first;
        int idx1 = cands[0].second;
        long long d2 = (cands.size() > 1 ? cands[1].first : d1);

        global_mx = max(global_mx, d1);
        max_d2[idx1] = max(max_d2[idx1], d2);
    }

    bool alice_wins = false;

    for (int i = 0; i < n; i++) {
        long long cur_a = a[i];

        long long low = abs(cur_a - b_min);
        long long high = cur_a + b_min;

        int cnt = upper_bound(a.begin(), a.end(), high - 1) - upper_bound(a.begin(), a.end(), low);
        if (low < cur_a && cur_a < high) {
            cnt--;
        }

        bool bob_wins_cond1 = (cnt == 0);
        long long max_dist = max(global_mx, max_d2[i]);
        bool bob_wins_cond2 = (max_dist >= cur_a);

        if (!bob_wins_cond1 && !bob_wins_cond2) {
            alice_wins = true;
            break;
        }
    }

    if (alice_wins) {
        cout << "Alice\n";
    } else {
        cout << "Bob\n";
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    if (cin >> t) {
        while (t--) {
            solve_test();
        }
    }
    return 0;
}
""",
        "sample_tests": get_samples("arc170_d")
    },
    {
        "id": "abc474_g",
        "contest_id": "abc474",
        "title": "G. LRUD Moving 2",
        "rating": 2280,
        "domain": "Graph Theory",
        "subtopic": "Hamiltonian Path",
        "topic": "Hamiltonian Path and Cycle",
        "category_file": "categories/graph_theory/grid_hamiltonian_path_parity_serpentine_construction.md",
        "slug": "grid_hamiltonian_path_parity_serpentine_construction",
        "core_tags": ["Graph Theory", "Hamiltonian Path", "Grid Graph", "Bipartite Parity", "Constructive"],
        "invariant": "In an $N \\times N$ grid, start $(1, 1)$ and end $(N, N)$ have identical bipartite colors iff $N$ is odd, so even $N$ has no Hamiltonian path. Net horizontal displacement requires $R - L = N - 1$, and parity matching restricts $K$ to even values in $[N - 1, (N^2 - 1)/2]$, realized via serpentine column-loop folding.",
        "editorial_reduction": "1. Color the grid as a bipartite chessboard with color $(r + c) \\bmod 2$. A Hamiltonian path visiting all $N^2$ cells has $N^2 - 1$ steps. If $N$ is even, $N^2 - 1$ is odd, which requires start and end to have different colors. But $(1, 1)$ and $(N, N)$ both have color 0. Thus $N$ must be odd.\\n2. Since the path starts at column 1 and ends at column $N$, $R - L = N - 1$. An odd-index matching argument proves that $K$ (number of 'R' moves) must be even and satisfy $N - 1 \\le K \\le (N^2 - 1)/2$.\\n3. Let $M = (N - 1)/2$ and surplus $S = (K - (N - 1))/2$. Partition $S$ into $M$ non-increasing integers $T_1 \\ge T_2 \\ge \\dots \\ge T_M \\ge 0$ such that $\\sum T_i = S$.\\n4. Traverse the grid row pairs with serpentine loops: for each $i = 1 \\dots M$, move right $2T_i$ steps, down 1, left $2T_i$ steps, down 1; then traverse columns with vertical loops of height $2(M - \\sum [T_v \\ge j])$ interspersed with 'R' moves. Time complexity per testcase is $O(N^2)$.",
        "cpp_solution": r"""#include <iostream>
#include <vector>
#include <string>

using namespace std;

void solve_test() {
    int n;
    long long k;
    if (!(cin >> n >> k)) return;

    if (n % 2 == 0 || k % 2 == 1 || k < n - 1 || k > (1LL * n * n - 1) / 2) {
        cout << "No\n";
        return;
    }

    int m = (n - 1) / 2;
    long long s = (k - (n - 1)) / 2;

    vector<int> t(m);
    for (int i = 0; i < m; i++) {
        t[i] = (s + m - 1 - i) / m;
    }

    string ans;
    ans.reserve(n * n);

    for (int v : t) {
        ans.append(2 * v, 'R');
        ans.push_back('D');
        ans.append(2 * v, 'L');
        ans.push_back('D');
    }

    for (int j = 1; j <= m; j++) {
        int cnt = 0;
        for (int v : t) {
            if (v >= j) cnt++;
        }
        int d = 2 * (m - cnt);
        ans.push_back('R');
        ans.append(d, 'U');
        ans.push_back('R');
        ans.append(d, 'D');
    }

    cout << "Yes\n";
    cout << ans << "\n";
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    if (cin >> t) {
        while (t--) {
            solve_test();
        }
    }
    return 0;
}
""",
        "sample_tests": get_samples("abc474_g")
    },
    {
        "id": "abc150_f",
        "contest_id": "abc150",
        "title": "F. Xor Shift",
        "rating": 2281,
        "domain": "Strings",
        "subtopic": "String Matching",
        "topic": "Knuth Morris Pratt (KMP) and Prefix Automaton",
        "category_file": "categories/strings/kmp_cyclic_xor_difference_matching.md",
        "slug": "kmp_cyclic_xor_difference_matching",
        "core_tags": ["Strings", "KMP", "Cyclic Shift", "XOR Differences", "Pattern Matching"],
        "invariant": "The relation $a_{(i+k) \\bmod N} \\oplus x = b_i$ eliminates $x$ upon taking adjacent circular XOR differences $A'_j = a_{(j+1) \\bmod N} \\oplus a_j$ and $B'_i = b_{(i+1) \\bmod N} \\oplus b_i$. A valid cyclic shift $k$ corresponds exactly to an exact match of pattern $B'$ in the doubled text $A' A'$, found via KMP in $O(N)$.",
        "editorial_reduction": "1. The problem asks for all pairs $(k, x)$ such that $a_{(i+k) \\bmod N} \\oplus x = b_i$ for all $0 \\le i < N$.\\n2. For $i = 0$, $x = a_k \\oplus b_0$. For any adjacent pair of indices, XORing equations gives $a_{(i+1+k) \\bmod N} \\oplus a_{(i+k) \\bmod N} = b_{i+1} \\oplus b_i$, completely eliminating $x$.\\n3. Define difference sequences $A'_j = a_{(j+1) \\bmod N} \\oplus a_j$ and $B'_i = b_{(i+1) \\bmod N} \\oplus b_i$. A shift $k$ is valid if and only if $A'_{(i+k) \\bmod N} = B'_i$ for all $0 \\le i < N$. Once this holds, setting $x = a_k \\oplus b_0$ satisfies all equations by induction.\\n4. Finding all valid shifts $k$ is equivalent to finding all occurrences of pattern $B'$ of length $N$ in the doubled text $A' A'$ of length $2N - 1$.\\n5. Run the Knuth-Morris-Pratt (KMP) algorithm over integer arrays in $O(N)$ time and space, printing each $(k, a_k \\oplus b_0)$ in ascending order of $k$.",
        "cpp_solution": r"""#include <iostream>
#include <vector>

using namespace std;

vector<int> compute_pi(const vector<int>& p) {
    int m = p.size();
    vector<int> pi(m, 0);
    for (int i = 1; i < m; i++) {
        int j = pi[i - 1];
        while (j > 0 && p[i] != p[j]) {
            j = pi[j - 1];
        }
        if (p[i] == p[j]) j++;
        pi[i] = j;
    }
    return pi;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> a(n), b(n);
    for (int i = 0; i < n; i++) cin >> a[i];
    for (int i = 0; i < n; i++) cin >> b[i];

    vector<int> diff_a(2 * n);
    vector<int> diff_b(n);

    for (int i = 0; i < n; i++) {
        diff_a[i] = a[(i + 1) % n] ^ a[i];
        diff_a[i + n] = diff_a[i];
        diff_b[i] = b[(i + 1) % n] ^ b[i];
    }

    vector<int> pi = compute_pi(diff_b);

    int j = 0;
    for (int i = 0; i < 2 * n - 1; i++) {
        while (j > 0 && diff_a[i] != diff_b[j]) {
            j = pi[j - 1];
        }
        if (diff_a[i] == diff_b[j]) {
            j++;
        }
        if (j == n) {
            int k = i - n + 1;
            if (k < n) {
                int x = a[k] ^ b[0];
                cout << k << " " << x << "\n";
            }
            j = pi[j - 1];
        }
    }

    return 0;
}
""",
        "sample_tests": get_samples("abc150_f")
    },
    {
        "id": "arc223_d",
        "contest_id": "arc223",
        "title": "D. Xpectation of Cards in Hand with Laboratory",
        "rating": 2281,
        "domain": "Math",
        "subtopic": "Probabilities and Expected Values",
        "topic": "Gambler's Ruin",
        "category_file": "categories/math/gamblers_ruin_reflection_principle_first_passage_expectation.md",
        "slug": "gamblers_ruin_reflection_principle_first_passage_expectation",
        "core_tags": ["Math", "Expected Value", "Gambler's Ruin", "Reflection Principle", "Catalan", "Ballot Theorem"],
        "invariant": "Each card drawn from the deck advances a random walk in $(a, b)$ where the hand runs out of draw cards exactly when $b - a = K$ for the first time. The number of paths hitting this absorbing barrier is given by the reflection principle $\\binom{a+b-1}{a} - \\binom{a+b-1}{a-1}$, while paths never reaching it yield the full deck hand size $B$.",
        "editorial_reduction": "1. Drawing 2 cards and discarding 1 draw card leaves the net count of draw cards in hand as $\\frac{a - b + K}{2}$. The hand runs out of draw cards iff $b = a + K$.\\n2. By the reflection principle (ballot theorem), the number of card sequences where $b = a + K$ occurs for the first time at step $a + b$ is $(\\binom{a+b-1}{a} - \\binom{a+b-1}{a-1}) \\times \\binom{A-a+B-b}{A-a}$. At this moment, exactly $b$ normal cards are in hand.\\n3. If the deck is exhausted before the hand runs out of draw cards (which can only happen if $B < A + K$), the path never hits the line $b - a = K$. The number of such sequences is $\\binom{A+B}{A} - \\binom{A+B}{A+K}$, and the final hand contains all $B$ normal cards. If $B \\ge A + K$, this event has probability 0.\\n4. Summing the product of final hand sizes and their corresponding path counts, then dividing by $\\binom{A+B}{A}$, yields the expected hand size in $O(A + B)$ time.",
        "cpp_solution": r"""#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

static const int MOD = 998244353;

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

const int MAX = 20000005;
long long fact[MAX];
long long invFact[MAX];

void init_fact(int limit) {
    fact[0] = 1;
    invFact[0] = 1;
    for (int i = 1; i <= limit; i++) {
        fact[i] = (fact[i - 1] * i) % MOD;
    }
    invFact[limit] = modInverse(fact[limit]);
    for (int i = limit - 1; i >= 1; i--) {
        invFact[i] = (invFact[i + 1] * (i + 1)) % MOD;
    }
}

long long nCr(int n, int r) {
    if (r < 0 || r > n) return 0;
    return fact[n] * invFact[r] % MOD * invFact[n - r] % MOD;
}

void solve_test() {
    int A, B, K;
    if (!(cin >> A >> B >> K)) return;

    long long total_arrangements = nCr(A + B, A);

    long long ways_exhausted = 0;
    if (B < A + K) {
        ways_exhausted = (nCr(A + B, A) - nCr(A + B, A + K) + MOD) % MOD;
    }
    long long sum_hand = (1LL * B * ways_exhausted) % MOD;

    int max_a = min(A, B - K);
    for (int a = 0; a <= max_a; a++) {
        int b = a + K;
        int step = a + b;
        long long ways_first = (nCr(step - 1, a) - nCr(step - 1, a - 1) + MOD) % MOD;
        long long ways_rem = nCr(A - a + B - b, A - a);
        long long ways = ways_first * ways_rem % MOD;
        sum_hand = (sum_hand + 1LL * b * ways) % MOD;
    }

    long long ans = (sum_hand * modInverse(total_arrangements)) % MOD;
    cout << ans << "\n";
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    init_fact(20000000);

    int t;
    if (cin >> t) {
        while (t--) {
            solve_test();
        }
    }
    return 0;
}
""",
        "sample_tests": get_samples("arc223_d")
    },
    {
        "id": "arc151_d",
        "contest_id": "arc151",
        "title": "D. Binary Representations and Queries",
        "rating": 2282,
        "domain": "Math",
        "subtopic": "Convolution",
        "topic": "Fast Walsh Hadamard Transform (FWHT) and its Variations",
        "category_file": "categories/math/fwht_tensor_product_independent_bit_transformations.md",
        "slug": "fwht_tensor_product_independent_bit_transformations",
        "core_tags": ["Math", "FWHT", "Linear Algebra", "Tensor Product", "Fast Walsh-Hadamard Transform"],
        "invariant": "Each query $(X_i, Y_i)$ applies an elementary $2 \\times 2$ shear matrix along dimension $X_i$ on the $N$-dimensional hypercube. Transformations acting on distinct bit dimensions commute; matrix multiplication accumulates operations per bit $X$, which are then applied via the FWHT butterfly algorithm in $O(Q + N 2^N)$.",
        "editorial_reduction": "1. For a query $(X, Y)$, pairs of indices differing only at bit $X$ are updated independently: if $Y = 0$, $\\begin{pmatrix} A_u \\\\ A_v \\end{pmatrix} \\gets \\begin{pmatrix} 1 & 0 \\\\ 1 & 1 \\end{pmatrix} \\begin{pmatrix} A_u \\\\ A_v \\end{pmatrix}$; if $Y = 1$, $\\begin{pmatrix} A_u \\\\ A_v \\end{pmatrix} \\gets \\begin{pmatrix} 1 & 1 \\\\ 0 & 1 \\end{pmatrix} \\begin{pmatrix} A_u \\\\ A_v \\end{pmatrix}$.\\n2. In the hypercube tensor product representation, a transformation on bit $X_1$ and a transformation on bit $X_2$ commute whenever $X_1 \\ne X_2$. Thus, queries on each bit $X \\in [0, N-1]$ can be aggregated independently.\\n3. For each bit $X$, multiply the sequence of $2 \\times 2$ matrices in order to obtain the net transformation matrix $M_X$.\\n4. Apply each $M_X$ across all $2^{N-1}$ pairs using the Fast Walsh-Hadamard Transform (FWHT) / SOS-DP butterfly sweep. Total time complexity is $O(Q + N 2^N)$, executing in ~0.03s for $N = 18$.",
        "cpp_solution": r"""#include <iostream>
#include <vector>

using namespace std;

static const int MOD = 998244353;

struct Mat2 {
    long long a, b, c, d;
};

Mat2 mul(const Mat2& m1, const Mat2& m2) {
    return {
        (m1.a * m2.a + m1.b * m2.c) % MOD,
        (m1.a * m2.b + m1.b * m2.d) % MOD,
        (m1.c * m2.a + m1.d * m2.c) % MOD,
        (m1.c * m2.b + m1.d * m2.d) % MOD
    };
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    int sz = 1 << n;
    vector<long long> a(sz);
    for (int i = 0; i < sz; i++) cin >> a[i];

    vector<Mat2> trans(n, {1, 0, 0, 1});

    for (int i = 0; i < q; i++) {
        int x, y;
        cin >> x >> y;
        Mat2 cur;
        if (y == 0) {
            cur = {1, 0, 1, 1};
        } else {
            cur = {1, 1, 0, 1};
        }
        trans[x] = mul(cur, trans[x]);
    }

    for (int bit = 0; bit < n; bit++) {
        Mat2 m = trans[bit];
        for (int mask = 0; mask < sz; mask++) {
            if (!(mask & (1 << bit))) {
                int u = mask;
                int v = mask | (1 << bit);
                long long au = a[u];
                long long av = a[v];
                a[u] = (m.a * au + m.b * av) % MOD;
                a[v] = (m.c * au + m.d * av) % MOD;
            }
        }
    }

    for (int i = 0; i < sz; i++) {
        cout << a[i] << (i == sz - 1 ? "" : " ");
    }
    cout << "\n";

    return 0;
}
""",
        "sample_tests": get_samples("arc151_d")
    },
    {
        "id": "codefestival_2016_qualC_d",
        "contest_id": "code-festival-2016-qualc",
        "title": "D. Friction",
        "rating": 2283,
        "domain": "Dynamic Programming (DP)",
        "subtopic": "Classic DP",
        "topic": "Edit Distance",
        "category_file": "categories/dynamic_programming_dp/edit_distance_column_sinking_friction_alignment.md",
        "slug": "edit_distance_column_sinking_friction_alignment",
        "core_tags": ["Dynamic Programming (DP)", "Edit Distance", "Alignment DP", "Grid Decomposition", "Independent Columns"],
        "invariant": "Total friction cost decomposes additively into independent interactions between adjacent column pairs $(j, j+1)$. The relative sequence of sinking operations for two adjacent columns corresponds to a 2D alignment grid walk from $(0, 0)$ to $(H, H)$, isomorphic to Edit Distance DP.",
        "editorial_reduction": "1. Friction only occurs between horizontally adjacent columns. Because any collection of valid pairwise sinking schedules can be realized by a global linear extension, the minimum total cost equals the sum of independent pairwise minimums over $j = 0, \\dots, W-2$.\\n2. For adjacent columns $j$ and $j+1$, let $i$ and $k$ be the number of times columns $j$ and $j+1$ have been lowered. The blocks remaining in column $j$ are originally at $r \\in [0, H - 1 - i]$ situated at row $r + i$, and in column $j+1$ at $s \\in [0, H - 1 - k]$ situated at row $s + k$.\\n3. Two blocks are horizontally adjacent when $r + i = s + k \\iff s = r + i - k$. The number of matching colors at state $(i, k)$ is $\\text{cost}(i, k) = \\sum_{r = \\max(0, k - i)}^{H - 1 - i} [c_{r, j} == c_{r + i - k, j+1}]$.\\n4. The optimal lowering schedule is computed via edit distance / grid alignment DP: $DP(i, k) = \\min(DP(i+1, k) + \\text{cost}(i, k), DP(i, k+1) + \\text{cost}(i, k))$, with base case $DP(H, H) = 0$.\\n5. Computing the DP for all $W - 1$ column pairs takes $O(W H^2)$ total operations, which finishes in ~0.04s for $H, W \\le 300$.",
        "cpp_solution": r"""#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int h, w;
    if (!(cin >> h >> w)) return 0;

    vector<string> grid(h);
    for (int i = 0; i < h; i++) {
        cin >> grid[i];
    }

    long long total_ans = 0;

    for (int j = 0; j < w - 1; j++) {
        vector<vector<int>> match_cost(h + 1, vector<int>(h + 1, 0));
        for (int i = 0; i <= h; i++) {
            for (int k = 0; k <= h; k++) {
                int cnt = 0;
                int start_r = max(0, k - i);
                int end_r = h - i;
                for (int r = start_r; r < end_r; r++) {
                    int s = r + i - k;
                    if (s >= 0 && s < h - k) {
                        if (grid[r][j] == grid[s][j + 1]) {
                            cnt++;
                        }
                    }
                }
                match_cost[i][k] = cnt;
            }
        }

        vector<vector<int>> dp(h + 1, vector<int>(h + 1, 1e9));
        dp[h][h] = 0;

        for (int i = h; i >= 0; i--) {
            for (int k = h; k >= 0; k--) {
                if (i == h && k == h) continue;
                int cur = 1e9;
                if (i + 1 <= h) {
                    cur = min(cur, dp[i + 1][k] + match_cost[i][k]);
                }
                if (k + 1 <= h) {
                    cur = min(cur, dp[i][k + 1] + match_cost[i][k]);
                }
                dp[i][k] = cur;
            }
        }

        total_ans += dp[0][0];
    }

    cout << total_ans << "\n";

    return 0;
}
""",
        "sample_tests": get_samples("codefestival_2016_qualC_d")
    },
    {
        "id": "agc032_c",
        "contest_id": "agc032",
        "title": "C. Three Circuits",
        "rating": 2284,
        "domain": "Graph Theory",
        "subtopic": "Eulerian Path",
        "topic": "Eulerian Path and Cycle",
        "category_file": "categories/graph_theory/eulerian_three_circuit_degree_decomposition.md",
        "slug": "eulerian_three_circuit_degree_decomposition",
        "core_tags": ["Graph Theory", "Eulerian Path", "Circuit Partition", "Degree Analysis", "Topological Decomposition"],
        "invariant": "Partitioning edges into circuits requires every vertex to have an even degree. If $\\max \\deg \\ge 6$ or the count of degree-4 vertices $c_4 \\ge 3$, 3 circuits always exist; if $c_4 \\le 1$, impossible; if $c_4 = 2$, 3 circuits exist iff the two degree-4 vertices are connected by 2 paths and have independent simple loops, decidable via path tracing.",
        "editorial_reduction": "1. Every circuit is an Eulerian subgraph, so all vertex degrees must be even. If any vertex has an odd degree, output `No`.\\n2. Since degree-2 vertices only subdivide paths, branching points must have degree $\\ge 4$. If any vertex has degree $\\ge 6$, edges can be paired into $\\ge 3$ intersecting cycles, yielding `Yes`.\\n3. If max degree is 4: count vertices with degree 4 ($c_4$). If $c_4 \\ge 3$, routing through the 3 branching nodes always permits $\\ge 3$ edge-disjoint circuits (`Yes`). If $c_4 \\le 1$, the graph is a single cycle or figure-eight, which can only decompose into at most 2 circuits (`No`).\\n4. For $c_4 = 2$ with degree-4 vertices $u$ and $v$: if all 4 paths from $u$ terminate at $v$ (4-strand theta graph), any circuit must alternate between $u$ and $v$ and thus consume an even number of paths, allowing at most $\\lfloor 4 / 2 \\rfloor = 2$ circuits (`No`). However, if at least one path from $u$ returns to $u$ without visiting $v$, the graph decomposes into a loop at $u$, a loop at $v$, and 2 paths between $u$ and $v$, giving exactly 3 circuits (`Yes`).\\n5. Path tracing from $u$ along degree-2 paths runs in $O(N + M)$ time.",
        "cpp_solution": r"""#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<int>> adj(n + 1);
    vector<int> deg(n + 1, 0);

    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
        deg[u]++;
        deg[v]++;
    }

    for (int i = 1; i <= n; i++) {
        if (deg[i] % 2 != 0) {
            cout << "No\n";
            return 0;
        }
    }

    int c4 = 0;
    bool has_ge6 = false;
    vector<int> deg4_nodes;

    for (int i = 1; i <= n; i++) {
        if (deg[i] >= 6) {
            has_ge6 = true;
        } else if (deg[i] == 4) {
            c4++;
            deg4_nodes.push_back(i);
        }
    }

    if (has_ge6 || c4 >= 3) {
        cout << "Yes\n";
        return 0;
    }

    if (c4 <= 1) {
        cout << "No\n";
        return 0;
    }

    int u = deg4_nodes[0];
    int v = deg4_nodes[1];

    bool loop_at_u = false;
    for (int start_nbr : adj[u]) {
        int prev = u;
        int cur = start_nbr;
        while (cur != u && cur != v) {
            int nxt = -1;
            for (int neighbor : adj[cur]) {
                if (neighbor != prev) {
                    nxt = neighbor;
                    break;
                }
            }
            prev = cur;
            cur = nxt;
        }
        if (cur == u) {
            loop_at_u = true;
            break;
        }
    }

    if (loop_at_u) {
        cout << "Yes\n";
    } else {
        cout << "No\n";
    }

    return 0;
}
""",
        "sample_tests": get_samples("agc032_c")
    }
]

with open('scratch/part5_part2c_meta.json', 'w', encoding='utf-8') as f:
    json.dump(meta, f, indent=2, ensure_ascii=False)

print(f"Successfully generated scratch/part5_part2c_meta.json with {len(meta)} problems!")
