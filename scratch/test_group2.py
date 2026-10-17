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
        # For arc159_c, output is constructive, so we might need a custom validator if multiple outputs are valid
        if task_id == 'arc159_c':
            passed = validate_arc159_c(inp, actual, expected)
        else:
            passed = (actual == expected)
            
        if passed:
            print(f"Sample {i+1}: PASS")
        else:
            print(f"Sample {i+1}: FAIL")
            print(f"  Input: {repr(inp[:100])}")
            print(f"  Expected: {repr(expected[:100])}")
            print(f"  Actual:   {repr(actual[:100])}")
            all_passed = False
    return all_passed

def validate_arc159_c(inp, actual, expected):
    lines = actual.split()
    if not lines:
        return False
    if expected.split()[0] == "No":
        return lines[0] == "No"
    if lines[0] != "Yes":
        return False
    
    inp_lines = inp.strip().split()
    N = int(inp_lines[0])
    A = [int(x) for x in inp_lines[1:N+1]]
    
    K = int(lines[1])
    if K > 10000:
        print(f"K = {K} exceeds 10000")
        return False
    
    tokens = lines[2:]
    if len(tokens) != K * N:
        print(f"Expected {K*N} tokens, got {len(tokens)}")
        return False
    
    for k in range(K):
        perm = [int(x) for x in tokens[k*N:(k+1)*N]]
        if sorted(perm) != list(range(1, N + 1)):
            print(f"Row {k} is not a permutation of 1..N: {perm}")
            return False
        for i in range(N):
            A[i] += perm[i]
            
    if len(set(A)) != 1:
        print(f"Elements not all equal: {A}")
        return False
    return True

# --- Code 1: abc379_g ---
cpp_abc379_g = r"""
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cstdint>

using namespace std;

const int MOD = 998244353;

// We use an open addressing hash table for fast profile transitions
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

    // Transpose if W > H so W <= 14
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
    uint32_t clear_top = ~(3u << shift);

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
"""

# --- Code 2: arc159_c ---
cpp_arc159_c = r"""
#include <iostream>
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

    // Check sum condition
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
            // Apply one standard permutation (1, 2, ..., N)
            vector<int> p(N);
            for (int i = 0; i < N; ++i) p[i] = i + 1;
            ops.push_back(p);
            for (int i = 0; i < N; ++i) A[i] += p[i];
        }
    }

    // Now sum % N == 0. Equalize elements using 2-step transfer of 1 unit.
    // Helper to transfer 1 from index u to index v
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
"""

# --- Code 3: abc234_g ---
cpp_abc234_g = r"""
#include <iostream>
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
"""

# --- Code 4: abc258_f ---
cpp_abc258_f = r"""
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

// Point on a highway or start/end
struct AccessPoint {
    long long x, y;
    long long cost; // cost to reach from S or to reach G
};

long long highway_dist(long long x1, long long y1, long long x2, long long y2, long long B) {
    bool v1 = (x1 % B == 0);
    bool h1 = (y1 % B == 0);
    bool v2 = (x2 % B == 0);
    bool h2 = (y2 % B == 0);

    // If both on vertical highways
    if (v1 && v2) {
        if (x1 == x2) return abs(y1 - y2);
        long long min_y = min(y1, y2);
        long long max_y = max(y1, y2);
        // check if a multiple of B exists in [min_y, max_y]
        long long next_B = (min_y / B) * B;
        if (next_B < min_y) next_B += B;
        if (next_B <= max_y) {
            return abs(x1 - x2) + abs(y1 - y2);
        } else {
            // Detour to Y0 = min_y / B * B or Y1 = Y0 + B
            long long Y0 = (min_y / B) * B;
            long long Y1 = Y0 + B;
            long long d0 = (y1 - Y0) + (y2 - Y0);
            long long d1 = (Y1 - y1) + (Y1 - y2);
            return abs(x1 - x2) + min(d0, d1);
        }
    }

    // If both on horizontal highways
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

    // Otherwise, one is vertical and one is horizontal
    return abs(x1 - x2) + abs(y1 - y2);
}

void solve() {
    long long B, K, Sx, Sy, Gx, Gy;
    cin >> B >> K >> Sx >> Sy >> Gx >> Gy;

    // Direct walk without highway
    long long ans = K * (abs(Sx - Gx) + abs(Sy - Gy));

    // Access points for S
    vector<AccessPoint> pts_S;
    long long xL = (Sx / B) * B;
    long long xR = xL + B;
    long long yD = (Sy / B) * B;
    long long yU = yD + B;

    pts_S.push_back({xL, Sy, K * abs(Sx - xL)});
    pts_S.push_back({xR, Sy, K * abs(Sx - xR)});
    pts_S.push_back({Sx, yD, K * abs(Sy - yD)});
    pts_S.push_back({Sx, yU, K * abs(Sy - yU)});

    // Access points for G
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
"""

if __name__ == '__main__':
    compile_cpp(cpp_abc379_g, "test_abc379_g")
    if not compile_cpp(cpp_abc379_g, "test_abc379_g"):
        print("Skipping abc379_g due to compilation failure")
    else:
        run_tests("test_abc379_g", "abc379_g")

    compile_cpp(cpp_arc159_c, "test_arc159_c")
    run_tests("test_arc159_c", "arc159_c")

    compile_cpp(cpp_abc234_g, "test_abc234_g")
    run_tests("test_abc234_g", "abc234_g")

    compile_cpp(cpp_abc258_f, "test_abc258_f")
    run_tests("test_abc258_f", "abc258_f")
