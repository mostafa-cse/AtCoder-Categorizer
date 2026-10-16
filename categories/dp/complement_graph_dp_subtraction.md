# Complement Graph DP / Total Sum Subtraction Trick

**Domain**: `Dynamic Programming`  
**Subtopic**: `DP Optimizations`  

This workbook contains curated, high-quality competitive programming problems teaching **Complement Graph DP / Total Sum Subtraction Trick**.

---

## Curated Problems

### `[problem:AtCoder-abc212_e]` — Safety Journey
- **Rating / Difficulty**: 1410
- **Contest**: `abc212`
- **Analysis**: [`analysis/AtCoder-abc212_e.md`](../../analysis/AtCoder-abc212_e.md)
- **Key Idea**: Instead of iterating over the dense available edges (O(N^2)), take the total sum of all DP states from the previous step and subtract the invalid transitions (self-loop and the M broken edges).
- **Time Complexity**: `O(K * (N + M))`
- **Space Complexity**: `O(N + M)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 998244353;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, k;
    if (!(cin >> n >> m >> k)) return 0;

    vector<pair<int, int>> broken(m);
    for (int i = 0; i < m; ++i) {
        cin >> broken[i].first >> broken[i].second;
    }

    vector<long long> dp(n + 1, 0);
    dp[1] = 1;

    for (int step = 0; step < k; ++step) {
        long long total_sum = 0;
        for (int i = 1; i <= n; ++i) {
            total_sum = (total_sum + dp[i]) % MOD;
        }

        vector<long long> next_dp(n + 1);
        for (int i = 1; i <= n; ++i) {
            next_dp[i] = (total_sum - dp[i] + MOD) % MOD;
        }

        for (const auto& edge : broken) {
            int u = edge.first;
            int v = edge.second;
            next_dp[v] = (next_dp[v] - dp[u] + MOD) % MOD;
            next_dp[u] = (next_dp[u] - dp[v] + MOD) % MOD;
        }

        dp = move(next_dp);
    }

    cout << dp[1] << "\n";
    return 0;
}
```
