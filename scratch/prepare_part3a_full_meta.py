import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/part3a_scraped_tasks.json', 'r', encoding='utf-8') as f:
    scraped = json.load(f)

def get_samples(pid):
    s_list = scraped[pid]['samples']
    seen = set()
    uniq = []
    for s in s_list:
        key = (s['input'].strip(), s['output'].strip())
        if key not in seen:
            seen.add(key)
            uniq.append(s)
    return uniq

# C++ code for each problem
cpp_codes = {
    "abc314_g": r"""#include <iostream>
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
""",

    "arc211_d": r"""#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    if (!(cin >> N >> M)) return 0;

    vector<vector<int>> adj(N + 1);
    for (int i = 0; i < M; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    vector<int> bpar(N + 1, 0), ypar(N + 1, 0);

    // Blue DFS from 1
    vector<bool> vis(N + 1, false);
    auto dfs_blue = [&](auto& self, int u) -> void {
        vis[u] = true;
        for (int v : adj[u]) {
            if (!vis[v]) {
                bpar[v] = u;
                self(self, v);
            }
        }
    };
    dfs_blue(dfs_blue, 1);

    // Yellow DFS from 2, avoiding bpar
    fill(vis.begin(), vis.end(), false);
    auto dfs_yellow = [&](auto& self, int u) -> void {
        vis[u] = true;
        for (int v : adj[u]) {
            if (!vis[v] && bpar[v] != u) {
                ypar[v] = u;
                self(self, v);
            }
        }
    };
    dfs_yellow(dfs_yellow, 2);

    for (int i = 1; i <= N; ++i) {
        if (i != 1 && bpar[i] == 0) {
            cout << "No\n";
            return 0;
        }
        if (i != 2 && ypar[i] == 0) {
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
""",

    "arc229_f": r"""#include <iostream>
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
""",

    "abc281_g": r"""#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    long long MOD;
    if (!(cin >> N >> MOD)) return 0;

    vector<vector<long long>> C(N + 1, vector<long long>(N + 1, 0));
    for (int i = 0; i <= N; ++i) {
        C[i][0] = 1;
        for (int j = 1; j <= i; ++j) {
            C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % MOD;
        }
    }

    vector<long long> p2(N * N + 1, 1);
    for (int i = 1; i <= N * N; ++i) {
        p2[i] = (p2[i - 1] * 2) % MOD;
    }

    auto power = [&](long long base, long long exp) -> long long {
        long long res = 1;
        base %= MOD;
        while (exp > 0) {
            if (exp % 2 == 1) res = (res * base) % MOD;
            base = (base * base) % MOD;
            exp /= 2;
        }
        return res;
    };

    vector<vector<long long>> dp(N + 1, vector<long long>(N + 1, 0));
    dp[1][1] = 1;

    for (int i = 1; i < N - 1; ++i) {
        for (int j = 1; j <= i; ++j) {
            if (dp[i][j] == 0) continue;

            for (int k = 1; i + k <= N - 1; ++k) {
                long long ways_choose = C[N - 1 - i][k];
                long long ways_internal = p2[k * (k - 1) / 2];
                long long p_base = (p2[j] - 1 + MOD) % MOD;
                long long ways_cross = power(p_base, k);

                long long total_ways = ways_choose * ways_internal % MOD * ways_cross % MOD;
                dp[i + k][k] = (dp[i + k][k] + dp[i][j] * total_ways) % MOD;
            }
        }
    }

    long long ans = 0;
    for (int j = 1; j <= N - 1; ++j) {
        if (dp[N - 1][j] == 0) continue;
        long long ways_cross = (p2[j] - 1 + MOD) % MOD;
        ans = (ans + dp[N - 1][j] * ways_cross) % MOD;
    }

    cout << ans << "\n";
    return 0;
}
""",

    "abc379_g": r"""#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cstdint>

using namespace std;

const int MOD = 998244353;

struct HashTable {
    static const int SIZE = 1 << 16;
    static const int MASK = SIZE - 1;
    uint32_t keys[SIZE];
    int vals[SIZE];
    int head[SIZE];
    int nxt[SIZE];
    int sz;

    void clear() {
        fill(head, head + SIZE, -1);
        sz = 0;
    }

    void add(uint32_t k, int v) {
        int h = (k * 2654435761u) & MASK;
        for (int e = head[h]; e != -1; e = nxt[e]) {
            if (keys[e] == k) {
                vals[e] = (vals[e] + v) % MOD;
                return;
            }
        }
        keys[sz] = k;
        vals[sz] = v;
        nxt[sz] = head[h];
        head[h] = sz++;
    }
};

HashTable ht_cur, ht_nxt;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int H, W;
    if (!(cin >> H >> W)) return 0;
    vector<string> grid(H);
    for (int i = 0; i < H; ++i) cin >> grid[i];

    if (W > H) {
        vector<string> transposed(W, string(H, ' '));
        for (int i = 0; i < H; ++i) {
            for (int j = 0; j < W; ++j) {
                transposed[j][i] = grid[i][j];
            }
        }
        grid = transposed;
        swap(H, W);
    }

    ht_cur.clear();
    ht_cur.add(0, 1);

    int shift = 2 * (W - 1);

    for (int r = 0; r < H; ++r) {
        for (int c = 0; c < W; ++c) {
            ht_nxt.clear();
            char ch = grid[r][c];

            for (int i = 0; i < ht_cur.sz; ++i) {
                uint32_t m = ht_cur.keys[i];
                int ways = ht_cur.vals[i];

                int top = (m & 3);
                int left = ((m >> shift) & 3);

                for (int val = 0; val < 3; ++val) {
                    if (ch != '?' && ch - '1' != val) continue;
                    if (r > 0 && val == top) continue;
                    if (c > 0 && val == left) continue;

                    uint32_t nm = (m >> 2) | ((uint32_t)val << shift);
                    ht_nxt.add(nm, ways);
                }
            }
            ht_cur = ht_nxt;
        }
    }

    int ans = 0;
    for (int i = 0; i < ht_cur.sz; ++i) {
        ans = (ans + ht_cur.vals[i]) % MOD;
    }
    cout << ans << "\n";
    return 0;
}
""",

    "arc159_c": r"""#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    if (!(cin >> N)) return 0;
    vector<long long> A(N);
    long long sum = 0;
    for (int i = 0; i < N; ++i) {
        cin >> A[i];
        sum += A[i];
    }

    vector<vector<int>> ops;

    long long rem = (sum % N + N) % N;
    if (N % 2 != 0) {
        if (rem != 0) {
            cout << "No\n";
            return 0;
        }
    } else {
        if (rem != 0 && rem != N / 2) {
            cout << "No\n";
            return 0;
        }
        if (rem == N / 2) {
            vector<int> p(N);
            for (int i = 0; i < N; ++i) p[i] = i + 1;
            ops.push_back(p);
            for (int i = 0; i < N; ++i) A[i] += p[i];
        }
    }

    auto transfer = [&](int u, int v) {
        vector<int> p1(N), p2(N);
        p1[u] = 1; p2[u] = N - 1;
        p1[v] = 2; p2[v] = N;

        int cur_val1 = 3;
        for (int i = 0; i < N; ++i) {
            if (i == u || i == v) continue;
            p1[i] = cur_val1;
            p2[i] = N + 1 - cur_val1;
            cur_val1++;
        }
        ops.push_back(p1);
        ops.push_back(p2);
        for (int i = 0; i < N; ++i) {
            A[i] += p1[i] + p2[i];
        }
    };

    while (true) {
        long long mn = *min_element(A.begin(), A.end());
        long long mx = *max_element(A.begin(), A.end());
        if (mn == mx) break;

        int u = -1, v = -1;
        for (int i = 0; i < N; ++i) {
            if (A[i] == mx) u = i;
            if (A[i] == mn) v = i;
        }
        transfer(u, v);
    }

    cout << "Yes\n";
    cout << ops.size() << "\n";
    for (const auto& p : ops) {
        for (int i = 0; i < N; ++i) {
            cout << p[i] << (i == N - 1 ? "" : " ");
        }
        cout << "\n";
    }
    return 0;
}
""",

    "abc234_g": r"""#include <iostream>
#include <vector>

using namespace std;

const int MOD = 998244353;

struct Element {
    long long val;
    long long sum_dp;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    if (!(cin >> N)) return 0;
    vector<long long> A(N + 1);
    for (int i = 1; i <= N; ++i) cin >> A[i];

    vector<long long> dp(N + 1, 0);
    dp[0] = 1;

    vector<Element> st_max, st_min;
    long long S_max = 0, S_min = 0;

    for (int i = 1; i <= N; ++i) {
        long long cur_max_dp = dp[i - 1];
        while (!st_max.empty() && st_max.back().val <= A[i]) {
            S_max = (S_max - st_max.back().val * st_max.back().sum_dp) % MOD;
            cur_max_dp = (cur_max_dp + st_max.back().sum_dp) % MOD;
            st_max.pop_back();
        }
        st_max.push_back({A[i], cur_max_dp});
        S_max = (S_max + A[i] * cur_max_dp) % MOD;

        long long cur_min_dp = dp[i - 1];
        while (!st_min.empty() && st_min.back().val >= A[i]) {
            S_min = (S_min - st_min.back().val * st_min.back().sum_dp) % MOD;
            cur_min_dp = (cur_min_dp + st_min.back().sum_dp) % MOD;
            st_min.pop_back();
        }
        st_min.push_back({A[i], cur_min_dp});
        S_min = (S_min + A[i] * cur_min_dp) % MOD;

        dp[i] = (S_max - S_min) % MOD;
        if (dp[i] < 0) dp[i] += MOD;
    }

    cout << dp[N] << "\n";
    return 0;
}
""",

    "abc258_f": r"""#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

struct AccessPoint {
    long long x, y;
    long long cost;
};

long long highway_dist(long long x1, long long y1, long long x2, long long y2, long long B) {
    bool v1 = (x1 % B == 0);
    bool h1 = (y1 % B == 0);
    bool v2 = (x2 % B == 0);
    bool h2 = (y2 % B == 0);

    if (v1 && v2) {
        if (x1 == x2) return abs(y1 - y2);
        long long min_y = min(y1, y2);
        long long max_y = max(y1, y2);
        long long next_B = (min_y / B) * B;
        if (next_B < min_y) next_B += B;
        if (next_B <= max_y) {
            return abs(x1 - x2) + abs(y1 - y2);
        } else {
            long long Y0 = (min_y / B) * B;
            long long Y1 = Y0 + B;
            long long d0 = (y1 - Y0) + (y2 - Y0);
            long long d1 = (Y1 - y1) + (Y1 - y2);
            return abs(x1 - x2) + min(d0, d1);
        }
    }

    if (h1 && h2) {
        if (y1 == y2) return abs(x1 - x2);
        long long min_x = min(x1, x2);
        long long max_x = max(x1, x2);
        long long next_B = (min_x / B) * B;
        if (next_B < min_x) next_B += B;
        if (next_B <= max_x) {
            return abs(x1 - x2) + abs(y1 - y2);
        } else {
            long long X0 = (min_x / B) * B;
            long long X1 = X0 + B;
            long long d0 = (x1 - X0) + (x2 - X0);
            long long d1 = (X1 - x1) + (X1 - x2);
            return abs(y1 - y2) + min(d0, d1);
        }
    }

    return abs(x1 - x2) + abs(y1 - y2);
}

void solve() {
    long long B, K, Sx, Sy, Gx, Gy;
    cin >> B >> K >> Sx >> Sy >> Gx >> Gy;

    long long ans = K * (abs(Sx - Gx) + abs(Sy - Gy));

    vector<AccessPoint> pts_S;
    long long xL = (Sx / B) * B;
    long long xR = xL + B;
    long long yD = (Sy / B) * B;
    long long yU = yD + B;

    pts_S.push_back({xL, Sy, K * abs(Sx - xL)});
    pts_S.push_back({xR, Sy, K * abs(Sx - xR)});
    pts_S.push_back({Sx, yD, K * abs(Sy - yD)});
    pts_S.push_back({Sx, yU, K * abs(Sy - yU)});

    vector<AccessPoint> pts_G;
    long long gxL = (Gx / B) * B;
    long long gxR = gxL + B;
    long long gyD = (Gy / B) * B;
    long long gyU = gyD + B;

    pts_G.push_back({gxL, Gy, K * abs(Gx - gxL)});
    pts_G.push_back({gxR, Gy, K * abs(Gx - gxR)});
    pts_G.push_back({Gx, gyD, K * abs(Gy - gyD)});
    pts_G.push_back({Gx, gyU, K * abs(Gy - gyU)});

    for (const auto& ps : pts_S) {
        for (const auto& pg : pts_G) {
            long long cur = ps.cost + pg.cost + highway_dist(ps.x, ps.y, pg.x, pg.y, B);
            ans = min(ans, cur);
        }
    }

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
""",

    "abc295_f": r"""#include <iostream>
#include <string>
#include <vector>
#include <cmath>

using namespace std;

long long count_occurrences(long long N, const string& S) {
    if (N <= 0) return 0;
    string N_str = to_string(N);
    int L_N = N_str.size();
    int M = S.size();

    long long total = 0;

    auto p10 = [](int p) -> long long {
        long long res = 1;
        for (int i = 0; i < p; ++i) res *= 10;
        return res;
    };

    for (int D = M; D < L_N; ++D) {
        for (int p = 0; p <= D - M; ++p) {
            if (p == 0) {
                if (S[0] == '0') continue;
                total += p10(D - M);
            } else {
                long long pref_choices = 9 * p10(p - 1);
                long long suf_choices = p10(D - M - p);
                total += pref_choices * suf_choices;
            }
        }
    }

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

            if (N_pref > min_pref) {
                long long num_smaller = N_pref - min_pref;
                total += num_smaller * suf_pow;
            }

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
""",

    "abc209_f": r"""#include <iostream>
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
        int n = i + 2;
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
                if (j < old_sz) {
                    int val = (pref[old_sz] - pref[j]) % MOD;
                    if (val < 0) val += MOD;
                    nxt[j] = val;
                } else {
                    nxt[j] = 0;
                }
            } else if (h_prev > h_cur) {
                int lim = min(j, old_sz);
                nxt[j] = pref[lim];
            } else {
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
""",

    "agc024_d": r"""#include <iostream>
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
        parent[u] = -1;

        q.push(v);
        dist[v] = 0;
        parent[v] = -1;

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

        long long leaves = 2;
        for (int d = 0; d < max_d; ++d) {
            leaves *= max(1, max_c[d]);
        }
        update(col, leaves);
    }

    cout << best_color << " " << best_leaves << "\n";
    return 0;
}
""",

    "arc068_c": r"""#include <iostream>
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
""",

    "arc049_c": r"""#include <iostream>
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

    for (int mask = 0; mask < (1 << B); ++mask) {
        vector<vector<int>> adj(N + 1);
        vector<int> in_degree(N + 1, 0);
        vector<bool> forbidden(N + 1, false);

        for (const auto& e : type1) {
            adj[e.v].push_back(e.u);
        }

        for (int i = 0; i < B; ++i) {
            if (mask & (1 << i)) {
                adj[type2[i].u].push_back(type2[i].v);
            } else {
                forbidden[type2[i].u] = true;
            }
        }

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
""",

    "arc044_c": r"""#include <iostream>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

const long long INF = 1e16;

long long solve_1d(int L, const map<int, vector<int>>& events_by_t) {
    vector<long long> dp(L + 1, 0);

    for (const auto& kv : events_by_t) {
        vector<int> pts = kv.second;
        sort(pts.begin(), pts.end());

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

        vector<pair<int, long long>> updates;

        for (auto& iv : intervals) {
            int l = iv.first;
            int r = iv.second;

            long long m1 = INF;
            long long m2 = INF;
            for (int x = l; x <= r; ++x) {
                if (dp[x] < INF) {
                    m1 = min(m1, dp[x] + x);
                    m2 = min(m2, dp[x] - x);
                }
                dp[x] = INF;
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
""",

    "exawizards2019_e": r"""#include <iostream>
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
        int n = i - 1;
        if (n >= 1) {
            if (n - 1 >= W - 1) {
                long long term = nCr(n - 1, W - 1) * pow_half[n] % MOD;
                S_W = (S_W + term) % MOD;
            }
            if (n - 1 >= B - 1) {
                long long term = nCr(n - 1, B - 1) * pow_half[n] % MOD;
                S_B = (S_B + term) % MOD;
            }
        }

        long long diff = (S_W - S_B) % MOD;
        if (diff < 0) diff += MOD;

        long long ans = (half + half * diff) % MOD;
        cout << ans << "\n";
    }

    return 0;
}
""",

    "panasonic2020_e": r"""#include <iostream>
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
}

meta = [
    {
        "id": "abc314_g",
        "contest_id": "abc314",
        "title": "G. Amulets",
        "rating": 2301,
        "domain": "Basics",
        "subtopic": "Standard Template Library (STL)",
        "topic": "Priority Queue / Heap",
        "category_file": "categories/basics/prefix_immunity_dual_heap.md",
        "slug": "prefix_immunity_dual_heap",
        "core_tags": ["Basics", "Standard Template Library (STL)", "Priority Queue / Heap", "Greedy", "Two Pointers"],
        "invariant": "For any prefix of monsters and $k$ amulets, it is strictly optimal to grant immunity to the $k$ monster types with the largest accumulated damage in that prefix.",
        "editorial_reduction": "Maintain two balanced heaps/sets partitioning monster types into the top-$k$ highest total damage and the remaining types.\nAs $k$ increases, dynamically advance the maximum defeatable prefix of monsters using two pointers.\nUpdating a monster's damage or balancing heaps takes $O(\\log M)$ time per operation.",
        "time_complexity": "O((N + M) \\log M)",
        "space_complexity": "O(N + M)",
        "samples": get_samples("abc314_g"),
        "cpp_solution": cpp_codes["abc314_g"]
    },
    {
        "id": "arc211_d",
        "contest_id": "arc211",
        "title": "D. Two Signposts",
        "rating": 2301,
        "domain": "Graph Theory",
        "subtopic": "Graph Traversal",
        "topic": "Topological Sorting",
        "category_file": "categories/graph_theory/dual_dfs_signpost_orientation.md",
        "slug": "dual_dfs_signpost_orientation",
        "core_tags": ["Graph Theory", "Graph Traversal", "Topological Sorting", "DFS Tree", "Constructive"],
        "invariant": "A valid signpost orientation for each color forms a directed spanning tree rooted at that color's destination with no cycles, subject to the condition that no vertex points along the same directed edge in both trees.",
        "editorial_reduction": "Construct the blue signposts by running DFS rooted at vertex 1, orienting edges towards the parent to establish a spanning tree directed to 1.\nConstruct yellow signposts via DFS rooted at vertex 2, enforcing the constraint that the yellow parent edge must not coincide with the blue parent edge.\nIf either DFS fails to visit all vertices, output No; otherwise, output the two valid parent pointer arrays.",
        "time_complexity": "O(N + M)",
        "space_complexity": "O(N + M)",
        "samples": get_samples("arc211_d"),
        "cpp_solution": cpp_codes["arc211_d"]
    },
    {
        "id": "arc229_f",
        "contest_id": "arc229",
        "title": "F. Card Game",
        "rating": 2302,
        "domain": "Combinatorics",
        "subtopic": "Techniques",
        "topic": "Contribution Technique",
        "category_file": "categories/combinatorics/component_partitioning_edge_contribution.md",
        "slug": "component_partitioning_edge_contribution",
        "core_tags": ["Combinatorics", "Techniques", "Contribution Technique", "Graph Theory", "Extremal Graph Theory"],
        "invariant": "A graph represents a valid configuration of cards if and only if every connected component has at least 3 vertices or is a non-isolated edge structure without isolated $K_2$ components.",
        "editorial_reduction": "Sort costs $C_i$ non-decreasingly and isolate vertex $N$ with the largest cost $C_{N-1}$.\nPartition the remaining $N-1$ vertices into $k$ non-empty connected components, leaving $e = N - 1 - k$ surplus edges.\nEvaluate the exact edge cost contribution: if $e \\ge 2k$, surplus edges can be assigned cost $C_0$; otherwise, parity constraints require $(e \\bmod 2) C_0$.\nMinimize the total contribution across all $1 \\le k \\le N-1$ in $O(N)$ time using prefix sums.",
        "time_complexity": "O(N \\log N)",
        "space_complexity": "O(N)",
        "samples": get_samples("arc229_f"),
        "cpp_solution": cpp_codes["arc229_f"]
    },
    {
        "id": "abc281_g",
        "contest_id": "abc281",
        "title": "G. Farthest City",
        "rating": 2304,
        "domain": "Graph Theory",
        "subtopic": "Graph Counting",
        "topic": "Counting Labeled Graphs",
        "category_file": "categories/graph_theory/layered_bfs_dag_graph_counting.md",
        "slug": "layered_bfs_dag_graph_counting",
        "core_tags": ["Graph Theory", "Graph Counting", "Counting Labeled Graphs", "Dynamic Programming (DP)", "BFS Layering"],
        "invariant": "The condition that vertex $N$ has strictly greater distance from vertex 1 than all other vertices implies $N$ is the unique vertex in the final layer $D$ of the BFS DAG.",
        "editorial_reduction": "Define $dp[i][j]$ as the number of valid graph structures formed by placing $i$ intermediate vertices with the last layer containing $j$ vertices.\nTransition by adding a new layer of $k$ vertices from the remaining unplaced labeled vertices: choose vertices with $\\binom{N-1-i}{k}$, choose internal edges with $2^{k(k-1)/2}$, and connect each new vertex to at least one vertex in the previous layer with $(2^j - 1)^k$.\nFinally, connect vertex $N$ to the last layer using $(2^j - 1)$ choices in $O(N^3)$ total time.",
        "time_complexity": "O(N^3)",
        "space_complexity": "O(N^2)",
        "samples": get_samples("abc281_g"),
        "cpp_solution": cpp_codes["abc281_g"]
    },
    {
        "id": "abc379_g",
        "contest_id": "abc379",
        "title": "G. Count Grid 3-coloring",
        "rating": 2304,
        "domain": "Miscellaneous",
        "subtopic": "General",
        "topic": "Broken Profile DP / Plug DP",
        "category_file": "categories/miscellaneous/broken_profile_grid_3coloring.md",
        "slug": "broken_profile_grid_3coloring",
        "core_tags": ["Miscellaneous", "General", "Broken Profile DP / Plug DP", "Dynamic Programming (DP)", "Bitmask DP"],
        "invariant": "Since $H \\times W \\le 200$, transposing ensures $W \\le 14$. The frontier profile of the last $W$ assigned cells completely determines validity of subsequent cell assignments.",
        "editorial_reduction": "Transpose grid if $W > H$ so that $W \\le 14$. Encode the boundary profile of the last $W$ cells using 2 bits per cell in an unsigned 32-bit integer.\nPerform cell-by-cell broken profile dynamic programming across all $H \\times W$ cells.\nAt each cell, verify color compatibility with top and left neighbors and update profiles via bit shifts and open-addressing hash aggregation.",
        "time_complexity": "O(H W \\cdot 3 \\cdot 2^{W-1})",
        "space_complexity": "O(2^{W})",
        "samples": get_samples("abc379_g"),
        "cpp_solution": cpp_codes["abc379_g"]
    },
    {
        "id": "arc159_c",
        "contest_id": "arc159",
        "title": "C. Permutation Addition",
        "rating": 2304,
        "domain": "Basics",
        "subtopic": "Greedy and Constructive",
        "topic": "Basic Constructive Algorithms",
        "category_file": "categories/basics/complementary_permutation_pair_transfer.md",
        "slug": "complementary_permutation_pair_transfer",
        "core_tags": ["Basics", "Greedy and Constructive", "Basic Constructive Algorithms", "Invariants", "Modular Arithmetic"],
        "invariant": "Adding a permutation adds $N(N+1)/2$ to the total sum. A uniform state is achievable if and only if $\\sum A_i \\equiv 0 \\pmod N$ for odd $N$, or $\\sum A_i \\in \\{0, N/2\\} \\pmod N$ for even $N$.",
        "editorial_reduction": "If $N$ is even and $\\sum A_i \\equiv N/2 \\pmod N$, apply one standard permutation $(1, \\dots, N)$ to reach $\\sum A_i \\equiv 0 \\pmod N$.\nConstruct a pair of complementary permutations $(P_1, P_2)$ that transfers exactly 1 unit from the current maximum element index $u$ to the minimum element index $v$ while adding $N+1$ uniformly to all other positions.\nRepeatedly transfer unit mass until all elements become equal, requiring at most $2 \\times 2500 \\le 5000$ operations.",
        "time_complexity": "O(N \\sum |A_i|)",
        "space_complexity": "O(N)",
        "samples": get_samples("arc159_c"),
        "cpp_solution": cpp_codes["arc159_c"]
    },
    {
        "id": "abc234_g",
        "contest_id": "abc234",
        "title": "G. Divide a Sequence",
        "rating": 2306,
        "domain": "Data Structures (DS)",
        "subtopic": "Segment Tree",
        "topic": "Segment Tree with Lazy Propagation",
        "category_file": "categories/data_structures/dual_monotonic_stack_linear_dp.md",
        "slug": "dual_monotonic_stack_linear_dp",
        "core_tags": ["Data Structures (DS)", "Segment Tree", "Segment Tree with Lazy Propagation", "Monotonic Stack", "Dynamic Programming (DP)"],
        "invariant": "The product sum over partition blocks factors into $(\\max(B) - \\min(B)) dp[j] = \\max(B) dp[j] - \\min(B) dp[j]$, decoupling the maximum and minimum contributions independently.",
        "editorial_reduction": "Maintain two monotonic stacks: one tracking non-increasing maximum values and one tracking non-decreasing minimum values alongside their accumulated $dp$ sums.\nOn inserting $A_i$, pop dominated elements while maintaining prefix sums $S_{\\max}$ and $S_{\\min}$ in $O(1)$ amortized time.\nCompute $dp[i] = (S_{\\max} - S_{\\min}) \\bmod 998244353$ in strictly linear $O(N)$ time.",
        "time_complexity": "O(N)",
        "space_complexity": "O(N)",
        "samples": get_samples("abc234_g"),
        "cpp_solution": cpp_codes["abc234_g"]
    },
    {
        "id": "abc258_f",
        "contest_id": "abc258",
        "title": "F. Main Street",
        "rating": 2306,
        "domain": "Graph Theory",
        "subtopic": "Shortest Paths",
        "topic": "Dijkstra's Algorithm",
        "category_file": "categories/graph_theory/grid_highway_projection_shortest_path.md",
        "slug": "grid_highway_projection_shortest_path",
        "core_tags": ["Graph Theory", "Shortest Paths", "Dijkstra's Algorithm", "Geometry", "Manhattan Distance"],
        "invariant": "Any optimal trajectory between arbitrary grid points uses at most one entry and exit segment on regular streets to access the highway grid, projecting $S$ and $G$ onto their 4 bounding highway lines.",
        "editorial_reduction": "Generate the 4 orthogonal projection points of $S$ onto adjacent highway grid lines $x = \\lfloor S_x/B \\rfloor B, \\dots$ and similarly for $G$.\nCompute shortest path distances along the regular highway grid between all $4 \\times 4 = 16$ pairs of access points, taking detours into account if both points lie on the same cell boundary.\nTake the minimum over all 16 highway paths and the direct regular street Manhattan distance.",
        "time_complexity": "O(T)",
        "space_complexity": "O(1)",
        "samples": get_samples("abc258_f"),
        "cpp_solution": cpp_codes["abc258_f"]
    },
    {
        "id": "abc295_f",
        "contest_id": "abc295",
        "title": "F. substr = S",
        "rating": 2306,
        "domain": "Dynamic Programming (DP)",
        "subtopic": "Digit DP",
        "topic": "Digit DP",
        "category_file": "categories/dynamic_programming/digit_dp_substring_occurrence_linearity.md",
        "slug": "digit_dp_substring_occurrence_linearity",
        "core_tags": ["Dynamic Programming (DP)", "Digit DP", "Linearity of Expectation", "Combinatorics", "Prefix Sums"],
        "invariant": "By linearity of occurrences, the total occurrences of $S$ in numbers $\\le N$ equals the sum over all possible total lengths $D$ and starting offsets $p$ of the number of integers matching $S$ at position $p$.",
        "editorial_reduction": "Express $\\sum_{k=L}^R f(k) = \\text{count}(R) - \\text{count}(L-1)$.\nFor a fixed bound $N$, iterate over all possible digit lengths $D \\le \\text{len}(N)$ and starting positions $p \\in [0, D - |S|]$.\nDirectly evaluate the number of valid prefixes and suffixes that keep the reconstructed number $\\le N$ without full automaton construction.",
        "time_complexity": "O(T \\cdot (\\log_{10} R)^2)",
        "space_complexity": "O(1)",
        "samples": get_samples("abc295_f"),
        "cpp_solution": cpp_codes["abc295_f"]
    },
    {
        "id": "abc209_f",
        "contest_id": "abc209",
        "title": "F. Deforestation",
        "rating": 2307,
        "domain": "Dynamic Programming (DP)",
        "subtopic": "Intro to DP",
        "topic": "Knapsack and Basic Dynamic Programming",
        "category_file": "categories/dynamic_programming/permutation_relative_rank_insertion_dp.md",
        "slug": "permutation_relative_rank_insertion_dp",
        "core_tags": ["Dynamic Programming (DP)", "Intro to DP", "Knapsack and Basic Dynamic Programming", "Permutation DP", "Prefix Sums"],
        "invariant": "For adjacent trees $(i, i+1)$, cutting $i$ before $i+1$ pays $H_{i+1}$, whereas cutting $i+1$ before $i$ pays $H_i$. Minimizing total cost imposes strict relative order constraints on adjacent cutting positions.",
        "editorial_reduction": "Deduce that $H_i < H_{i+1}$ requires $pos[i] > pos[i+1]$, and $H_i > H_{i+1}$ requires $pos[i] < pos[i+1]$.\nUse permutation insertion DP where $dp[j]$ tracks the number of permutations of prefix trees where the newest tree is placed at relative rank $j$.\nAccelerate transitions across ranks using prefix sums to achieve $O(N^2)$ time.",
        "time_complexity": "O(N^2)",
        "space_complexity": "O(N)",
        "samples": get_samples("abc209_f"),
        "cpp_solution": cpp_codes["abc209_f"]
    },
    {
        "id": "agc024_d",
        "contest_id": "agc024",
        "title": "D. Isomorphism Freak",
        "rating": 2307,
        "domain": "Miscellaneous",
        "subtopic": "General",
        "topic": "Tree Isomorphism",
        "category_file": "categories/miscellaneous/tree_isomorphism_center_leaf_minimization.md",
        "slug": "tree_isomorphism_center_leaf_minimization",
        "core_tags": ["Miscellaneous", "General", "Tree Isomorphism", "Trees", "Graph Theory", "Constructive"],
        "invariant": "A tree with minimum colorfulness must be completely symmetric with respect to either a central vertex (giving radius $D$, colorfulness $D+1$) or a central edge (giving radius $D$, colorfulness $D+1$).",
        "editorial_reduction": "Iterate over all $N$ vertices as candidate centers, calculating maximum depth and maximum branch degrees at each distance level.\nIterate over all $N-1$ edges as candidate bicenters, rooting two symmetrical halves across the central bridge.\nMinimize colorfulness first, and among ties minimize total leaf count $\\prod \\max(\\text{degrees})$ in $O(N^2)$ time.",
        "time_complexity": "O(N^2)",
        "space_complexity": "O(N)",
        "samples": get_samples("agc024_d"),
        "cpp_solution": cpp_codes["agc024_d"]
    },
    {
        "id": "arc068_c",
        "contest_id": "arc068",
        "title": "E. Snuke Line",
        "rating": 2307,
        "domain": "Data Structures (DS)",
        "subtopic": "Square Root Decomposition",
        "topic": "Splitting Objects into Light and Heavy / Case Processing",
        "category_file": "categories/data_structures/harmonic_query_offline_fenwick_threshold.md",
        "slug": "harmonic_query_offline_fenwick_threshold",
        "core_tags": ["Data Structures (DS)", "Square Root Decomposition", "Splitting Objects into Light and Heavy / Case Processing", "Fenwick Tree", "Harmonic Series"],
        "invariant": "Any interval of length $\\ge d$ is guaranteed to contain at least one multiple of $d$. Intervals of length $< d$ contain at most one multiple of $d$ and can be queried via point evaluations.",
        "editorial_reduction": "Sort and bucket intervals by their lengths $len_i = r_i - l_i + 1$.\nAs step size $d$ increases from $1$ to $M$, retire intervals with length $d - 1$ from the heavy count and insert them into a Fenwick tree (range add $[l_i, r_i]$).\nQuery all multiples $k \\cdot d \\le M$ in the Fenwick tree, yielding total complexity $O(N \\log M + M \\log^2 M)$.",
        "time_complexity": "O(N \\log M + M \\log^2 M)",
        "space_complexity": "O(N + M)",
        "samples": get_samples("arc068_c"),
        "cpp_solution": cpp_codes["arc068_c"]
    },
    {
        "id": "arc049_c",
        "contest_id": "arc049",
        "title": "C. ぬりまーす",
        "rating": 2308,
        "domain": "Graph Theory",
        "subtopic": "Graph Traversal",
        "topic": "Topological Sorting",
        "category_file": "categories/graph_theory/branching_2sat_conflict_topological_cycle.md",
        "slug": "branching_2sat_conflict_topological_cycle",
        "core_tags": ["Graph Theory", "Graph Traversal", "Topological Sorting", "2-SAT", "Cycle Detection", "Bitmask Branching"],
        "invariant": "Each Type 2 constraint $(u, v)$ requires either $u$ is painted before $v$ (adding directed edge $u \\to v$) or $u$ is never painted (marking $u$ as forbidden).",
        "editorial_reduction": "Since $B \\le 10$, branch over all $2^B \\le 1024$ assignments of Type 2 constraints.\nFor each assignment, construct the dependency graph with Type 1 edges $y \\to x$ and Type 2 Choice 1 edges $u \\to v$.\nPropagate forbidden status to all reachable descendants, then run Kahn's topological sort on remaining vertices to detect and eliminate cycles, maximizing the number of painted vertices.",
        "time_complexity": "O(2^B (N + A + B))",
        "space_complexity": "O(N + A + B)",
        "samples": get_samples("arc049_c"),
        "cpp_solution": cpp_codes["arc049_c"]
    },
    {
        "id": "arc044_c",
        "contest_id": "arc044",
        "title": "C. ビーム",
        "rating": 2309,
        "domain": "Dynamic Programming (DP)",
        "subtopic": "Intro to DP",
        "topic": "Knapsack and Basic Dynamic Programming",
        "category_file": "categories/dynamic_programming/orthogonal_1d_beam_escape_interval_dp.md",
        "slug": "orthogonal_1d_beam_escape_interval_dp",
        "core_tags": ["Dynamic Programming (DP)", "Intro to DP", "Knapsack and Basic Dynamic Programming", "Coordinate Decoupling", "Interval DP"],
        "invariant": "Vertical beams restrict only X coordinates and horizontal beams restrict only Y coordinates, rendering movement costs along X and Y completely decoupled and independent.",
        "editorial_reduction": "Decompose the problem into two independent 1D problems for $W$ and $H$.\nIn 1D, at each beam event time $t$, contiguous segments of attacked coordinates $[l, r]$ force any occupant to escape to $l-1$ or $r+1$ with distance cost.\nMaintain $dp[x]$ dynamically, updating boundary positions and invalidating blocked cells in $O((W + H + Q) \\log Q)$ time.",
        "time_complexity": "O(W + H + Q \\log Q)",
        "space_complexity": "O(W + H + Q)",
        "samples": get_samples("arc044_c"),
        "cpp_solution": cpp_codes["arc044_c"]
    },
    {
        "id": "exawizards2019_e",
        "contest_id": "exawizards2019",
        "title": "E. Black or White",
        "rating": 2309,
        "domain": "Math",
        "subtopic": "Probabilities and Expected Values",
        "topic": "Gambler's Ruin",
        "category_file": "categories/math/exhaustion_boundary_incremental_binomial_tails.md",
        "slug": "exhaustion_boundary_incremental_binomial_tails",
        "core_tags": ["Math", "Probabilities and Expected Values", "Gambler's Ruin", "Combinatorics", "Random Walk"],
        "invariant": "Before either color is exhausted, each chocolate chosen is Black with probability $1/2$. Once White is exhausted, all remaining chocolates are Black with probability 1; once Black is exhausted, Black has probability 0.",
        "editorial_reduction": "Express $P(i\\text{-th is Black}) = 1/2 + 1/2 [P(\\text{White exhausted before } i) - P(\\text{Black exhausted before } i)]$.\nThe probability that White was exhausted in the first $n = i-1$ flips is the binomial tail $\\sum_{k=W}^n \\binom{n}{k} (1/2)^n$.\nUpdate tail sums incrementally via $S(n) = S(n-1) + \\binom{n-1}{W-1} (1/2)^n$ in $O(1)$ per step.",
        "time_complexity": "O(B + W)",
        "space_complexity": "O(B + W)",
        "samples": get_samples("exawizards2019_e"),
        "cpp_solution": cpp_codes["exawizards2019_e"]
    },
    {
        "id": "panasonic2020_e",
        "contest_id": "panasonic2020",
        "title": "E. Three Substrings",
        "rating": 2309,
        "domain": "Strings",
        "subtopic": "String Matching",
        "topic": "String Matching using Bitsets",
        "category_file": "categories/strings/pairwise_wildcard_alignment_filtering_span.md",
        "slug": "pairwise_wildcard_alignment_filtering_span",
        "core_tags": ["Strings", "String Matching", "String Matching using Bitsets", "Brute Force", "Wildcard Matching"],
        "invariant": "Three strings $a, b, c$ can be embedded at relative offsets $(0, i, j)$ if and only if all three pairwise overlaps $(a, b)$ at $i$, $(a, c)$ at $j$, and $(b, c)$ at $j - i$ are mutually consistent.",
        "editorial_reduction": "Precompute compatibility tables for each pair of strings over all relative shifts in $[-4000, 4000]$ in $O(|a||b| + |b||c| + |a||c|)$ time.\nIterate over valid shift offsets $(i, j) \\in [-2000, 2000]^2$, pruning incompatible pairs in $O(1)$ via the precomputed table.\nCompute the span $\\max(|a|, i+|b|, j+|c|) - \\min(0, i, j)$ and output the global minimum.",
        "time_complexity": "O(|a||b| + |a||c| + |b||c| + L^2)",
        "space_complexity": "O(L)",
        "samples": get_samples("panasonic2020_e"),
        "cpp_solution": cpp_codes["panasonic2020_e"]
    }
]

with open('scratch/part5_part3a_meta.json', 'w', encoding='utf-8') as f:
    json.dump(meta, f, indent=2, ensure_ascii=False)

print(f"Successfully generated scratch/part5_part3a_meta.json with {len(meta)} problems.")
