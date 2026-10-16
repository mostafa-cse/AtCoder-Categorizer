# 2D Bound 0-1 Knapsack DP (Capacity + Item Count Limit)

**Domain**: `Dynamic Programming`  
**Subtopic**: `Knapsack DP`  

This workbook contains curated, high-quality competitive programming problems teaching **2D Bound 0-1 Knapsack DP (Capacity + Item Count Limit)**.

---

## Curated Problems

### [problem:AtCoder-abc015_4] — Takahashi's Pain
- **Contest**: `abc015`
- **Rating / Difficulty**: 1388
- **Specific Skill**: 2D Bound 0-1 Knapsack DP (Capacity + Item Count Limit)
- **Individual Analysis**: [`../../analysis/AtCoder-abc015_4.md`](../../analysis/AtCoder-abc015_4.md)
- **Problem Statement Summary**: N screenshots, screenshot i has width A_i and value B_i. Select at most K screenshots with total width <= W to maximize total value (N <= 50, W <= 10000, K <= N).
- **Core Insight**: Define dp[k][w] = maximum value using exactly k items with total weight w. For each item (A_i, B_i), iterate backwards k from K down to 1 and w from W down to A_i: dp[k][w] = max(dp[k][w], dp[k - 1][w - A_i] + B_i).
- **Complexity**: Time: `O(N * K * W)` | Space: `O(K * W)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int w_limit, n, k_limit;
    if (!(cin >> w_limit >> n >> k_limit)) return 0;

    vector<vector<int>> dp(k_limit + 1, vector<int>(w_limit + 1, 0));

    for (int i = 0; i < n; ++i) {
        int a, b;
        cin >> a >> b;

        for (int k = k_limit; k >= 1; --k) {
            for (int w = w_limit; w >= a; --w) {
                dp[k][w] = max(dp[k][w], dp[k - 1][w - a] + b);
            }
        }
    }

    int ans = 0;
    for (int k = 1; k <= k_limit; ++k) {
        for (int w = 0; w <= w_limit; ++w) {
            ans = max(ans, dp[k][w]);
        }
    }

    cout << ans << "\n";
    return 0;
}
```
