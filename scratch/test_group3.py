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

# --- Code 1: abc295_f ---
cpp_abc295_f = r"""
#include <iostream>
#include <string>
#include <vector>
#include <cmath>

using namespace std;

// Count total occurrences of S in integers 1..N
long long count_occurrences(long long N, const string& S) {
    if (N <= 0) return 0;
    string N_str = to_string(N);
    int L_N = N_str.size();
    int M = S.size();

    long long total = 0;

    // Helper: 10^p
    auto p10 = [](int p) -> long long {
        long long res = 1;
        for (int i = 0; i < p; ++i) res *= 10;
        return res;
    };

    // Case 1: numbers of length D < L_N
    for (int D = M; D < L_N; ++D) {
        for (int p = 0; p <= D - M; ++p) {
            if (p == 0) {
                if (S[0] == '0') continue;
                // pref is empty, suf has D - M digits
                total += p10(D - M);
            } else {
                // pref has p digits (1..9 for first, 0..9 for rest) -> 9 * 10^(p-1)
                // suf has D - M - p digits -> 10^(D - M - p)
                long long pref_choices = 9 * p10(p - 1);
                long long suf_choices = p10(D - M - p);
                total += pref_choices * suf_choices;
            }
        }
    }

    // Case 2: numbers of length D == L_N
    int D = L_N;
    for (int p = 0; p <= D - M; ++p) {
        int suf_len = D - M - p;
        long long suf_pow = p10(suf_len);

        if (p == 0) {
            if (S[0] == '0') continue;
            string N_mid = N_str.substr(p, M);
            if (S < N_mid) {
                total += suf_pow;
            } else if (S == N_mid) {
                if (suf_len == 0) {
                    total += 1;
                } else {
                    long long N_suf = stoll(N_str.substr(p + M, suf_len));
                    total += N_suf + 1;
                }
            }
        } else {
            long long N_pref = stoll(N_str.substr(0, p));
            long long min_pref = p10(p - 1);

            // strictly smaller prefixes: [min_pref, N_pref - 1]
            if (N_pref > min_pref) {
                long long num_smaller = N_pref - min_pref;
                total += num_smaller * suf_pow;
            }

            // prefix equals N_pref
            string N_mid = N_str.substr(p, M);
            if (S < N_mid) {
                total += suf_pow;
            } else if (S == N_mid) {
                if (suf_len == 0) {
                    total += 1;
                } else {
                    long long N_suf = stoll(N_str.substr(p + M, suf_len));
                    total += N_suf + 1;
                }
            }
        }
    }

    return total;
}

void solve() {
    string S;
    long long L, R;
    if (!(cin >> S >> L >> R)) return;
    long long ans = count_occurrences(R, S) - count_occurrences(L - 1, S);
    cout << ans << "\n";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    if (cin >> T) {
        while (T--) solve();
    }
    return 0;
}
"""

# --- Code 2: abc209_f ---
cpp_abc209_f = r"""
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 1000000007;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    if (!(cin >> N)) return 0;
    vector<long long> H(N);
    for (int i = 0; i < N; ++i) cin >> H[i];

    vector<int> dp = {1};

    for (int i = 0; i < N - 1; ++i) {
        int n = i + 2; // size of new dp table
        int old_sz = dp.size();
        vector<int> pref(old_sz + 1, 0);
        for (int k = 0; k < old_sz; ++k) {
            pref[k + 1] = (pref[k] + dp[k]) % MOD;
        }

        vector<int> nxt(n, 0);
        long long h_prev = H[i];
        long long h_cur = H[i + 1];

        for (int j = 0; j < n; ++j) {
            if (h_prev < h_cur) {
                // pos[i] > pos[i+1], so old rank k >= j
                // sum for k in [j, old_sz - 1]
                if (j < old_sz) {
                    int val = (pref[old_sz] - pref[j]) % MOD;
                    if (val < 0) val += MOD;
                    nxt[j] = val;
                } else {
                    nxt[j] = 0;
                }
            } else if (h_prev > h_cur) {
                // pos[i] < pos[i+1], so old rank k < j
                // sum for k in [0, min(j-1, old_sz-1)]
                int lim = min(j, old_sz);
                nxt[j] = pref[lim];
            } else {
                // equal: any previous rank
                nxt[j] = pref[old_sz];
            }
        }
        dp = move(nxt);
    }

    int ans = 0;
    for (int x : dp) ans = (ans + x) % MOD;
    cout << ans << "\n";
    return 0;
}
"""

# --- Code 3: agc024_d ---
cpp_agc024_d = r"""
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

int N;
vector<vector<int>> adj;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> N)) return 0;
    adj.assign(N + 1, vector<int>());
    vector<pair<int, int>> edges;
    for (int i = 0; i < N - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
        edges.push_back({u, v});
    }

    int best_color = 1e9;
    long long best_leaves = -1;

    auto update = [&](int col, long long lvs) {
        if (col < best_color) {
            best_color = col;
            best_leaves = lvs;
        } else if (col == best_color) {
            if (best_leaves == -1 || lvs < best_leaves) {
                best_leaves = lvs;
            }
        }
    };

    // Option 1: Vertex center
    for (int r = 1; r <= N; ++r) {
        vector<int> dist(N + 1, -1);
        vector<int> parent(N + 1, 0);
        queue<int> q;
        q.push(r);
        dist[r] = 0;
        int max_d = 0;
        while (!q.empty()) {
            int u = q.front();
            q.pop();
            max_d = max(max_d, dist[u]);
            for (int v : adj[u]) {
                if (dist[v] == -1) {
                    dist[v] = dist[u] + 1;
                    parent[v] = u;
                    q.push(v);
                }
            }
        }

        int col = max_d + 1;
        // Count max children at each depth d from 0 to max_d - 1
        vector<int> max_c(max_d, 0);
        for (int u = 1; u <= N; ++u) {
            int d = dist[u];
            if (d < max_d) {
                int ch = 0;
                for (int v : adj[u]) {
                    if (parent[v] == u) ch++;
                }
                max_c[d] = max(max_c[d], ch);
            }
        }

        long long leaves = 1;
        for (int d = 0; d < max_d; ++d) {
            leaves *= max(1, max_c[d]);
        }
        update(col, leaves);
    }

    // Option 2: Edge center
    for (auto edge : edges) {
        int u = edge.first;
        int v = edge.second;

        vector<int> dist(N + 1, -1);
        vector<int> parent(N + 1, 0);
        queue<int> q;
        q.push(u);
        dist[u] = 0;
        parent[u] = -1; // root

        q.push(v);
        dist[v] = 0;
        parent[v] = -1; // root

        int max_d = 0;
        while (!q.empty()) {
            int curr = q.front();
            q.pop();
            max_d = max(max_d, dist[curr]);
            for (int nxt : adj[curr]) {
                if ((curr == u && nxt == v) || (curr == v && nxt == u)) continue;
                if (dist[nxt] == -1) {
                    dist[nxt] = dist[curr] + 1;
                    parent[nxt] = curr;
                    q.push(nxt);
                }
            }
        }

        int col = max_d + 1;
        vector<int> max_c(max_d, 0);
        for (int node = 1; node <= N; ++node) {
            int d = dist[node];
            if (d < max_d) {
                int ch = 0;
                for (int nxt : adj[node]) {
                    if (parent[nxt] == node) ch++;
                }
                max_c[d] = max(max_c[d], ch);
            }
        }

        long long leaves = 2; // two sides of the edge
        for (int d = 0; d < max_d; ++d) {
            leaves *= max(1, max_c[d]);
        }
        update(col, leaves);
    }

    cout << best_color << " " << best_leaves << "\n";
    return 0;
}
"""

# --- Code 4: arc068_c ---
cpp_arc068_c = r"""
#include <iostream>
#include <vector>

using namespace std;

struct Fenwick {
    int n;
    vector<int> tree;
    Fenwick(int n) : n(n), tree(n + 2, 0) {}

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

    int N, M;
    if (!(cin >> N >> M)) return 0;

    // Group intervals by length: len = r - l + 1
    // len can be from 1 to M
    vector<vector<pair<int, int>>> by_len(M + 2);
    for (int i = 0; i < N; ++i) {
        int l, r;
        cin >> l >> r;
        int len = r - l + 1;
        if (len <= M) {
            by_len[len].push_back({l, r});
        }
    }

    Fenwick bit(M + 1);
    int long_count = N;

    for (int d = 1; d <= M; ++d) {
        // Any interval with length == d - 1 is now "short" for d
        for (auto& seg : by_len[d - 1]) {
            long_count--;
            bit.add(seg.first, 1);
            bit.add(seg.second + 1, -1);
        }

        int ans = long_count;
        for (int k = d; k <= M; k += d) {
            ans += bit.query(k);
        }
        cout << ans << "\n";
    }

    return 0;
}
"""

if __name__ == '__main__':
    compile_cpp(cpp_abc295_f, "test_abc295_f")
    run_tests("test_abc295_f", "abc295_f")

    compile_cpp(cpp_abc209_f, "test_abc209_f")
    run_tests("test_abc209_f", "abc209_f")

    compile_cpp(cpp_agc024_d, "test_agc024_d")
    run_tests("test_agc024_d", "agc024_d")

    compile_cpp(cpp_arc068_c, "test_arc068_c")
    run_tests("test_arc068_c", "arc068_c")
