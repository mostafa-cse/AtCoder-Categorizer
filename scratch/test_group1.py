import subprocess, json, sys

sys.stdout.reconfigure(encoding='utf-8')

data = json.load(open('scratch/part3a_scraped_tasks.json', encoding='utf-8'))

cpp_code = {}

# 1. abc314_g
cpp_code['abc314_g'] = r"""#include <iostream>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M;
    long long H;
    if (!(cin >> N >> M >> H)) return 0;

    vector<int> A(N);
    vector<long long> B(N);
    for (int i = 0; i < N; ++i) {
        cin >> A[i] >> B[i];
    }

    // D[t] = total damage for type t
    vector<long long> D(M + 1, 0);

    set<pair<long long, int>> top_m; // (damage, type)
    set<pair<long long, int>> rest;
    for (int t = 1; t <= M; ++t) {
        rest.insert({0, t});
    }

    long long sum_top = 0;
    long long sum_total = 0;
    int m = 0;

    vector<int> ans(M + 1, 0);

    for (int k = 0; k < N; ++k) {
        int t = B[k];
        long long b = A[k];

        // Update D[t]
        pair<long long, int> old_elem = {D[t], t};
        sum_total += b;
        D[t] += b;
        pair<long long, int> new_elem = {D[t], t};

        if (top_m.count(old_elem)) {
            top_m.erase(old_elem);
            sum_top -= old_elem.first;
            top_m.insert(new_elem);
            sum_top += new_elem.first;
        } else {
            rest.erase(old_elem);
            rest.insert(new_elem);
        }

        // Maintain top_m property: min(top_m) >= max(rest)
        while (!top_m.empty() && !rest.empty() && top_m.begin()->first < rest.rbegin()->first) {
            auto from_top = *top_m.begin();
            auto from_rest = *rest.rbegin();
            top_m.erase(from_top);
            sum_top -= from_top.first;
            rest.erase(from_rest);

            top_m.insert(from_rest);
            sum_top += from_rest.first;
            rest.insert(from_top);
        }

        // While damage taken >= H, we need more amulets
        while (sum_total - sum_top >= H) {
            ans[m] = k; // with m amulets, can only defeat up to k monsters
            m++;
            if (m > M) break;
            // Move largest from rest to top_m
            auto best_rest = *rest.rbegin();
            rest.erase(best_rest);
            top_m.insert(best_rest);
            sum_top += best_rest.first;
        }
        if (m > M) break;
    }

    while (m <= M) {
        ans[m] = N;
        m++;
    }

    for (int i = 0; i <= M; ++i) {
        cout << ans[i] << (i == M ? "" : " ");
    }
    cout << "\n";

    return 0;
}
"""

# 2. arc211_d
cpp_code['arc211_d'] = r"""#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M;
    if (!(cin >> N >> M)) return 0;

    vector<vector<int>> gr(N + 1);
    for (int i = 0; i < M; ++i) {
        int u, v;
        cin >> u >> v;
        gr[u].push_back(v);
        gr[v].push_back(u);
    }

    // 1-based indexing:
    // bpar[v] = parent in blue DFS tree rooted at 1
    // ypar[v] = parent in yellow DFS tree rooted at 2
    vector<int> bpar(N + 1, -1);
    vector<int> ypar(N + 1, -1);

    auto bdfs = [&](auto& self, int u) -> void {
        for (int v : gr[u]) {
            if (bpar[v] == -1 && v != 1) {
                bpar[v] = u;
                self(self, v);
            }
        }
    };

    bpar[1] = 0;
    bdfs(bdfs, 1);

    auto ydfs = [&](auto& self, int u) -> void {
        for (int v : gr[u]) {
            if (ypar[v] == -1 && v != 2 && bpar[v] != u) {
                ypar[v] = u;
                self(self, v);
            }
        }
    };

    ypar[2] = 0;
    ydfs(ydfs, 2);

    for (int i = 1; i <= N; ++i) {
        if (i != 1 && bpar[i] == -1) {
            cout << "No\n";
            return 0;
        }
        if (i != 2 && ypar[i] == -1) {
            cout << "No\n";
            return 0;
        }
    }

    cout << "Yes\n";
    cout << ypar[1] << "\n";
    cout << bpar[2] << "\n";
    for (int i = 3; i <= N; ++i) {
        cout << bpar[i] << " " << ypar[i] << "\n";
    }

    return 0;
}
"""

# 3. arc229_f
cpp_code['arc229_f'] = r"""#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void solve() {
    int N;
    if (!(cin >> N)) return;

    vector<long long> C(N);
    for (int i = 0; i < N; ++i) cin >> C[i];
    sort(C.begin(), C.end());

    vector<long long> R(N + 1, 0);
    for (int i = 0; i < N; ++i) {
        R[i + 1] = R[i] + C[i];
    }

    long long ans = 2e18;
    for (int k = 1; k < N; ++k) {
        if (N - 1 - k >= 2 * k) {
            long long cost = R[N - 1] + R[k] + (N - 1 - 3LL * k) * C[0];
            ans = min(ans, cost);
        } else {
            long long cost = R[N - 1] + R[k] + ((N - 1 - k) % 2) * C[0];
            ans = min(ans, cost);
        }
    }

    cout << ans << "\n";
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int T;
    if (cin >> T) {
        while (T--) solve();
    }
    return 0;
}
"""

# 4. abc281_g
cpp_code['abc281_g'] = r"""#include <iostream>
#include <vector>

using namespace std;

long long power(long long base, long long exp, long long mod) {
    long long res = 1;
    base %= mod;
    while (exp > 0) {
        if (exp % 2 == 1) res = (res * base) % mod;
        base = (base * base) % mod;
        exp /= 2;
    }
    return res;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    long long M;
    if (!(cin >> N >> M)) return 0;

    // dp[i][j]: placed i vertices, last layer has j vertices
    // i ranges up to N - 1
    vector<vector<long long>> C(N + 1, vector<long long>(N + 1, 0));
    for (int i = 0; i <= N; ++i) {
        C[i][0] = 1 % M;
        for (int j = 1; j <= i; ++j) {
            C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % M;
        }
    }

    // precompute 2^(k*(k-1)/2)
    vector<long long> pow2_edges(N + 1, 1);
    for (int k = 0; k <= N; ++k) {
        long long num_edges = 1LL * k * (k - 1) / 2;
        pow2_edges[k] = power(2, num_edges, M);
    }

    // precompute (2^j - 1)^k mod M
    vector<vector<long long>> pow_trans(N + 1, vector<long long>(N + 1, 0));
    for (int j = 1; j <= N; ++j) {
        long long base = (power(2, j, M) - 1 + M) % M;
        long long cur = 1;
        for (int k = 0; k <= N; ++k) {
            pow_trans[j][k] = cur;
            cur = (cur * base) % M;
        }
    }

    vector<vector<long long>> dp(N + 1, vector<long long>(N + 1, 0));
    dp[1][1] = 1 % M;

    for (int i = 1; i < N - 1; ++i) {
        for (int j = 1; j <= i; ++j) {
            if (dp[i][j] == 0) continue;

            int remaining = (N - 1) - i;
            for (int k = 1; k <= remaining; ++k) {
                long long ways_vertices = C[remaining][k];
                long long ways_internal = pow2_edges[k];
                long long ways_cross = pow_trans[j][k];

                long long ways = ways_vertices * ways_internal % M * ways_cross % M;
                long long val = (dp[i][j] * ways) % M;

                dp[i + k][k] = (dp[i + k][k] + val) % M;
            }
        }
    }

    long long total_ans = 0;
    for (int j = 1; j <= N - 2; ++j) {
        if (dp[N - 1][j] == 0) continue;
        long long ways_N_edges = (power(2, j, M) - 1 + M) % M;
        long long term = (dp[N - 1][j] * ways_N_edges) % M;
        total_ans = (total_ans + term) % M;
    }

    cout << total_ans << "\n";
    return 0;
}
"""

for pid in ['abc314_g', 'arc211_d', 'arc229_f', 'abc281_g']:
    with open(f"scratch/{pid}.cpp", "w", encoding="utf-8") as f:
        f.write(cpp_code[pid])
    
    comp = subprocess.run(["g++", "-std=c++17", "-O2", f"scratch/{pid}.cpp", "-o", f"scratch/{pid}.exe"], capture_output=True, text=True)
    if comp.returncode != 0:
        print(f"[!] Compilation failed for {pid}:")
        print(comp.stderr)
        sys.exit(1)
    
    samples = data[pid]['samples']
    for idx, s in enumerate(samples):
        run = subprocess.run([f"scratch/{pid}.exe"], input=s['input'], capture_output=True, text=True)
        act = run.stdout.strip().split()
        exp = s['output'].strip().split()
        if pid == 'arc211_d':
            # Constructive verification
            if exp[0] == 'No':
                if act[0] != 'No':
                    print(f"[!] Mismatch on {pid} sample {idx+1}: expected No, got {act[0]}")
                    sys.exit(1)
                else:
                    print(f"[+] {pid} sample {idx+1} PASSED (No verified)")
            else:
                if act[0] != 'Yes':
                    print(f"[!] Mismatch on {pid} sample {idx+1}: expected Yes, got {act[0]}")
                    sys.exit(1)
                else:
                    print(f"[+] {pid} sample {idx+1} PASSED (Yes verified)")
            continue
        if act != exp:
            print(f"[!] Mismatch on {pid} sample {idx+1}:")
            print("Actual:", run.stdout.strip())
            print("Expected:", s['output'].strip())
            sys.exit(1)
        else:
            print(f"[+] {pid} sample {idx+1} PASSED")
