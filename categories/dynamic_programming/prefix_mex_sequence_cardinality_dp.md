# Prefix MEX Sequence State Tracking via Cardinality DP

**Domain**: `Dynamic Programming (DP)`  
**Subtopic**: `Classic DP`  

This workbook contains curated, high-quality competitive programming problems teaching **Prefix MEX Sequence State Tracking via Cardinality DP**.

---

## Curated Problems

### `[problem:AtCoder-arc170_c]` — Prefix Mex Sequence
- **Rating / Difficulty**: 2028
- **Contest**: `arc170`
- **Analysis**: [`analysis/AtCoder-arc170_c.md`](../../analysis/AtCoder-arc170_c.md)
- **Key Idea**: The prefix MEX depends only on the cardinality j of distinct values from {0, ..., M} present so far. If j distinct values are present: when S_i = 1, A_i must equal the current MEX (exactly 1 choice), increasing the present set size to j + 1. When S_i = 0, A_i must not equal the current MEX: we can either choose one of the j already present values (j choices, size remains j), or choose one of the remaining non-MEX values in [0, M] (M + 1 - j - 1 = M - j choices, size increases to j + 1). DP state: dp[i][j] = ways for prefix i with j distinct elements.
- **Time Complexity**: `O(N * min(N, M))`
- **Space Complexity**: `O(min(N, M))`
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

    vector<int> s(n);
    for (int i = 0; i < n; ++i) {
        cin >> s[i];
    }

    int max_j = min(n + 1, m + 1);
    vector<long long> dp(max_j + 1, 0);
    dp[0] = 1;

    for (int i = 0; i < n; ++i) {
        vector<long long> next_dp(max_j + 1, 0);

        for (int j = 0; j <= max_j; ++j) {
            if (dp[j] == 0) continue;

            if (s[i] == 1) {
                // Must pick MEX
                if (j + 1 <= max_j) {
                    next_dp[j + 1] = (next_dp[j + 1] + dp[j]) % MOD;
                }
            } else {
                // Must not pick MEX
                // 1. Pick from j already used numbers
                next_dp[j] = (next_dp[j] + dp[j] * j) % MOD;

                // 2. Pick an unused number != MEX: there are max(0, M - j) choices
                if (j < m && j + 1 <= max_j) {
                    next_dp[j + 1] = (next_dp[j + 1] + dp[j] * (m - j)) % MOD;
                }
            }
        }
        dp = move(next_dp);
    }

    long long ans = 0;
    for (int j = 0; j <= max_j; ++j) {
        ans = (ans + dp[j]) % MOD;
    }

    cout << ans << "\n";
    return 0;
}
```
