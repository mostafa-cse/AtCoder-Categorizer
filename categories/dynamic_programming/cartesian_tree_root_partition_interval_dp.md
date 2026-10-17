# Cartesian Tree Root Partition Interval DP under Argmax Constraints

**Domain**: `Dynamic Programming (DP)`  
**Subtopic**: `Interval DP / Range DP`  

This workbook contains curated, high-quality competitive programming problems teaching **Cartesian Tree Root Partition Interval DP under Argmax Constraints**.

---

## Curated Problems

### `[problem:AtCoder-arc183_c]` — Not Argmax
- **Rating / Difficulty**: 2018
- **Contest**: `arc183`
- **Analysis**: [`analysis/AtCoder-arc183_c.md`](../../analysis/AtCoder-arc183_c.md)
- **Key Idea**: Permutation maximums partition subsegments into Cartesian trees. For any interval [l, r], suppose position x in [l, r] holds the maximum value. Then x is the maximum of every subsegment [L, R] subset of [l, r] containing x. Thus x is valid as root iff no condition (L_i, R_i, X_i = x) satisfies l <= L_i <= x <= R_i <= r. If valid, the left subsegment [l, x-1] and right subsegment [x+1, r] are independent subproblems, combined with binom(r - l, x - l). This yields an O(N^3) Interval DP.
- **Time Complexity**: `O(N^3 + M)`
- **Space Complexity**: `O(N^2)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MOD = 998244353;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    // forbidden[x][l] = minimal R such that condition (L, R, x) has L >= l
    // or store conditions per x
    struct Query {
        int l, r;
    };
    vector<vector<Query>> conds(n + 1);
    for (int i = 0; i < m; ++i) {
        int l, r, x;
        cin >> l >> r >> x;
        conds[x].push_back({l, r});
    }

    // precompute combinations
    vector<vector<long long>> C(n + 1, vector<long long>(n + 1, 0));
    for (int i = 0; i <= n; ++i) {
        C[i][0] = 1;
        for (int j = 1; j <= i; ++j) {
            C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % MOD;
        }
    }

    // forbidden_root[l][r][x] can be checked:
    // x is forbidden in [l, r] iff there is some (L, R, x) with l <= L && R <= r
    // For each x and l, let min_r[x][l] be the minimum R over all conditions with L >= l
    vector<vector<int>> min_r(n + 1, vector<int>(n + 2, n + 2));
    for (int x = 1; x <= n; ++x) {
        for (const auto& q : conds[x]) {
            min_r[x][q.l] = min(min_r[x][q.l], q.r);
        }
        for (int l = n; l >= 1; --l) {
            min_r[x][l] = min(min_r[x][l], min_r[x][l + 1]);
        }
    }

    // dp[l][r]
    vector<vector<long long>> dp(n + 2, vector<long long>(n + 2, 0));
    for (int i = 1; i <= n + 1; ++i) {
        dp[i][i - 1] = 1;
    }

    for (int len = 1; len <= n; ++len) {
        for (int l = 1; l <= n - len + 1; ++l) {
            int r = l + len - 1;
            long long sum_ways = 0;

            for (int x = l; x <= r; ++x) {
                // Check if x is forbidden for interval [l, r]
                // Forbidden iff min_r[x][l] <= r
                if (min_r[x][l] <= r) continue;

                long long left_ways = dp[l][x - 1];
                long long right_ways = dp[x + 1][r];
                long long comb = C[r - l][x - l];

                long long cur = (left_ways * right_ways) % MOD;
                cur = (cur * comb) % MOD;
                sum_ways = (sum_ways + cur) % MOD;
            }
            dp[l][r] = sum_ways;
        }
    }

    cout << dp[1][n] << "\n";
    return 0;
}
```
