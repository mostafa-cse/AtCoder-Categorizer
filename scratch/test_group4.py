import json
import subprocess
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

tasks = json.load(open('scratch/part3a_scraped_tasks.json', encoding='utf-8'))

def compile_cpp(code, exe_name):
    cpp_path = f"scratch/{exe_name}.cpp"
    exe_path = f"scratch/{exe_name}.exe"
    with open(cpp_path, "w", encoding="utf-8") as f:
        f.write(code)
    cmd = ["g++", "-std=c++17", "-O2", cpp_path, "-o", exe_path]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Compilation failed for {exe_name}:")
        print(res.stderr)
        return False
    return True

def run_tests(exe_name, task_id):
    exe_path = f"scratch/{exe_name}.exe"
    samples = tasks[task_id]['samples']
    print(f"\n--- Testing {task_id} ({len(samples)} samples) ---")
    all_passed = True
    for i, s in enumerate(samples):
        inp = s['input']
        expected = s['output'].strip()
        p = subprocess.run([exe_path], input=inp, capture_output=True, text=True)
        actual = p.stdout.strip()
        
        # normalize whitespace for outputs
        actual_norm = " ".join(actual.split())
        expected_norm = " ".join(expected.split())
        passed = (actual_norm == expected_norm)
            
        if passed:
            print(f"Sample {i+1}: PASS")
        else:
            print(f"Sample {i+1}: FAIL")
            print(f"  Input: {repr(inp[:100])}")
            print(f"  Expected: {repr(expected[:100])}")
            print(f"  Actual:   {repr(actual[:100])}")
            all_passed = False
    return all_passed

# --- Code 1: arc049_c ---
cpp_arc049_c = r"""
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

struct Edge {
    int u, v;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, A;
    if (!(cin >> N >> A)) return 0;
    vector<Edge> type1(A);
    for (int i = 0; i < A; ++i) {
        cin >> type1[i].u >> type1[i].v;
    }

    int B;
    cin >> B;
    vector<Edge> type2(B);
    for (int i = 0; i < B; ++i) {
        cin >> type2[i].u >> type2[i].v;
    }

    int ans = 0;

    // Iterate through all 2^B choices for Type 2 constraints
    for (int mask = 0; mask < (1 << B); ++mask) {
        vector<vector<int>> adj(N + 1);
        vector<int> in_degree(N + 1, 0);
        vector<bool> forbidden(N + 1, false);

        // Type 1: x depends on y (y -> x)
        for (const auto& e : type1) {
            adj[e.v].push_back(e.u);
        }

        // Type 2:
        for (int i = 0; i < B; ++i) {
            if (mask & (1 << i)) {
                // Choice 1: u must be painted before v (u -> v)
                adj[type2[i].u].push_back(type2[i].v);
            } else {
                // Choice 2: u is forbidden
                forbidden[type2[i].u] = true;
            }
        }

        // Propagate forbidden status to all reachable vertices
        queue<int> q;
        for (int i = 1; i <= N; ++i) {
            if (forbidden[i]) q.push(i);
        }
        while (!q.empty()) {
            int u = q.front();
            q.pop();
            for (int v : adj[u]) {
                if (!forbidden[v]) {
                    forbidden[v] = true;
                    q.push(v);
                }
            }
        }

        // In the remaining vertices, find cycles using Kahn's algorithm (topological sort)
        vector<int> deg(N + 1, 0);
        for (int u = 1; u <= N; ++u) {
            if (forbidden[u]) continue;
            for (int v : adj[u]) {
                if (!forbidden[v]) {
                    deg[v]++;
                }
            }
        }

        queue<int> topo_q;
        int painted = 0;
        for (int i = 1; i <= N; ++i) {
            if (!forbidden[i] && deg[i] == 0) {
                topo_q.push(i);
            }
        }

        while (!topo_q.empty()) {
            int u = topo_q.front();
            topo_q.pop();
            painted++;
            for (int v : adj[u]) {
                if (!forbidden[v]) {
                    deg[v]--;
                    if (deg[v] == 0) {
                        topo_q.push(v);
                    }
                }
            }
        }

        ans = max(ans, painted);
    }

    cout << ans << "\n";
    return 0;
}
"""

# --- Code 2: arc044_c ---
cpp_arc044_c = r"""
#include <iostream>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

const long long INF = 1e16;

struct Beam {
    int t, d, x;
};

long long solve_1d(int L, const map<int, vector<int>>& events_by_t) {
    vector<long long> dp(L + 1, 0);

    for (const auto& kv : events_by_t) {
        vector<int> pts = kv.second;
        sort(pts.begin(), pts.end());

        // Group into maximal contiguous intervals [l, r]
        vector<pair<int, int>> intervals;
        int cur_l = pts[0], cur_r = pts[0];
        for (size_t i = 1; i < pts.size(); ++i) {
            if (pts[i] == cur_r + 1) {
                cur_r = pts[i];
            } else {
                intervals.push_back({cur_l, cur_r});
                cur_l = cur_r = pts[i];
            }
        }
        intervals.push_back({cur_l, cur_r});

        // Store updates so multiple intervals at the same time don't interfere
        vector<pair<int, long long>> updates;

        for (auto& iv : intervals) {
            int l = iv.first;
            int r = iv.second;

            long long m1 = INF; // min(dp[x] + x)
            long long m2 = INF; // min(dp[x] - x)
            for (int x = l; x <= r; ++x) {
                if (dp[x] < INF) {
                    m1 = min(m1, dp[x] + x);
                    m2 = min(m2, dp[x] - x);
                }
                dp[x] = INF; // attacked cell becomes invalid
            }

            if (l > 1 && m1 < INF) {
                updates.push_back({l - 1, m1 - l + 1});
            }
            if (r < L && m2 < INF) {
                updates.push_back({r + 1, m2 + r + 1});
            }
        }

        for (auto& up : updates) {
            dp[up.first] = min(dp[up.first], up.second);
        }
    }

    long long min_cost = INF;
    for (int x = 1; x <= L; ++x) {
        min_cost = min(min_cost, dp[x]);
    }
    return min_cost;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int W, H, Q;
    if (!(cin >> W >> H >> Q)) return 0;

    map<int, vector<int>> beams_x, beams_y;
    for (int i = 0; i < Q; ++i) {
        int t, d, x;
        cin >> t >> d >> x;
        if (d == 0) {
            beams_x[t].push_back(x);
        } else {
            beams_y[t].push_back(x);
        }
    }

    long long cost_x = solve_1d(W, beams_x);
    long long cost_y = solve_1d(H, beams_y);

    if (cost_x >= INF || cost_y >= INF) {
        cout << -1 << "\n";
    } else {
        cout << cost_x + cost_y << "\n";
    }

    return 0;
}
"""

# --- Code 3: exawizards2019_e ---
cpp_exawizards2019_e = r"""
#include <iostream>
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

    int B, W;
    if (!(cin >> B >> W)) return 0;

    int N = B + W;

    // Precompute factorials
    vector<long long> fact(N + 1, 1), invFact(N + 1, 1);
    for (int i = 1; i <= N; ++i) fact[i] = (fact[i - 1] * i) % MOD;
    invFact[N] = modInverse(fact[N]);
    for (int i = N - 1; i >= 0; --i) invFact[i] = (invFact[i + 1] * (i + 1)) % MOD;

    auto nCr = [&](int n, int r) -> long long {
        if (r < 0 || r > n) return 0;
        return fact[n] * invFact[r] % MOD * invFact[n - r] % MOD;
    };

    vector<long long> pow_half(N + 1, 1);
    long long half = modInverse(2);
    for (int i = 1; i <= N; ++i) pow_half[i] = (pow_half[i - 1] * half) % MOD;

    long long S_W = 0, S_B = 0;

    for (int i = 1; i <= N; ++i) {
        int n = i - 1; // number of flips before i-th chocolate
        if (n >= 1) {
            // S_W updates from S_W(n-1) to S_W(n)
            // S_W(n) = S_W(n-1) + C(n-1, W-1) * (1/2)^n
            if (n - 1 >= W - 1) {
                long long term = nCr(n - 1, W - 1) * pow_half[n] % MOD;
                S_W = (S_W + term) % MOD;
            }
            if (n - 1 >= B - 1) {
                long long term = nCr(n - 1, B - 1) * pow_half[n] % MOD;
                S_B = (S_B + term) % MOD;
            }
        }

        // ans = 1/2 + 1/2 * (S_W - S_B)
        long long diff = (S_W - S_B) % MOD;
        if (diff < 0) diff += MOD;

        long long ans = (half + half * diff) % MOD;
        cout << ans << "\n";
    }

    return 0;
}
"""

# --- Code 4: panasonic2020_e ---
cpp_panasonic2020_e = r"""
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

const int OFFSET = 4005;
const int MAX_SPAN = 8010;

bool ok_ab[MAX_SPAN];
bool ok_ac[MAX_SPAN];
bool ok_bc[MAX_SPAN];

void compute_match(const string& x, const string& y, bool ok[]) {
    int lx = x.size(), ly = y.size();
    for (int offset = -4000; offset <= 4000; ++offset) {
        bool match = true;
        for (int i = 0; i < ly; ++i) {
            int pos_x = offset + i;
            if (pos_x >= 0 && pos_x < lx) {
                if (x[pos_x] != '?' && y[i] != '?' && x[pos_x] != y[i]) {
                    match = false;
                    break;
                }
            }
        }
        ok[offset + OFFSET] = match;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string a, b, c;
    if (!(cin >> a >> b >> c)) return 0;

    int la = a.size(), lb = b.size(), lc = c.size();

    compute_match(a, b, ok_ab);
    compute_match(a, c, ok_ac);
    compute_match(b, c, ok_bc);

    int ans = la + lb + lc;

    for (int i = -2000; i <= 2000; ++i) {
        if (!ok_ab[i + OFFSET]) continue;
        for (int j = -2000; j <= 2000; ++j) {
            if (!ok_ac[j + OFFSET]) continue;
            if (!ok_bc[j - i + OFFSET]) continue;

            int left = min(0, min(i, j));
            int right = max(la, max(i + lb, j + lc));
            ans = min(ans, right - left);
        }
    }

    cout << ans << "\n";
    return 0;
}
"""

if __name__ == '__main__':
    compile_cpp(cpp_arc049_c, "test_arc049_c")
    run_tests("test_arc049_c", "arc049_c")

    compile_cpp(cpp_arc044_c, "test_arc044_c")
    run_tests("test_arc044_c", "arc044_c")

    compile_cpp(cpp_exawizards2019_e, "test_exawizards2019_e")
    run_tests("test_exawizards2019_e", "exawizards2019_e")

    compile_cpp(cpp_panasonic2020_e, "test_panasonic2020_e")
    run_tests("test_panasonic2020_e", "panasonic2020_e")
