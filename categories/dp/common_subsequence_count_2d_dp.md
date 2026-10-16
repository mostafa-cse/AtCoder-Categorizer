# 2D DP Counting Common Subsequences with 2D Prefix Sums

**Domain**: `Dynamic Programming`  
**Subtopic**: `Classic DP`  

This workbook contains curated, high-quality competitive programming problems teaching **2D DP Counting Common Subsequences with 2D Prefix Sums**.

---

## Curated Problems

### `[problem:AtCoder-abc130_e]` — Common Subsequence
- **Rating / Difficulty**: 1676
- **Contest**: `abc130`
- **Analysis**: [`analysis/AtCoder-abc130_e.md`](../../analysis/AtCoder-abc130_e.md)
- **Key Idea**: 2D DP with 2D prefix sums. `dp[i][j]` = number of pairs of identical subsequences using prefixes S[1..i] and T[1..j].
- **Time Complexity**: `O(N * M)`
- **Space Complexity**: `O(N * M)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 1000000007;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<int> s(n + 1), t(m + 1);
    for (int i = 1; i <= n; ++i) cin >> s[i];
    for (int j = 1; j <= m; ++j) cin >> t[j];

    vector<vector<long long>> dp(n + 1, vector<long long>(m + 1, 0));

    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            dp[i][j] = (dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + MOD) % MOD;
            if (s[i] == t[j]) {
                dp[i][j] = (dp[i][j] + dp[i - 1][j - 1] + 1) % MOD;
            }
        }
    }

    // Including the empty pair
    cout << (dp[n][m] + 1) % MOD << "\n";
    return 0;
}
```
