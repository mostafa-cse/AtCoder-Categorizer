# 2-State DP on Subarray Deletion to Match Target Sum

**Domain**: `Dynamic Programming`  
**Subtopic**: `Classic DP`  

This workbook contains curated, high-quality competitive programming problems teaching **2-State DP on Subarray Deletion to Match Target Sum**.

---

## Curated Problems

### `[problem:AtCoder-abc275_f]` — Erase Subarrays
- **Rating / Difficulty**: 1608
- **Contest**: `abc275`
- **Analysis**: [`analysis/AtCoder-abc275_f.md`](../../analysis/AtCoder-abc275_f.md)
- **Key Idea**: Dynamic programming maintaining whether the previous element was deleted or retained. `dp[sum][state]` where state 0 = retained, state 1 = deleted.
- **Time Complexity**: `O(N * M)`
- **Space Complexity**: `O(M)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int INF = 1e9;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<int> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    // dp[sum][state]: state 0 = kept, state 1 = erased
    vector<vector<int>> dp(m + 1, vector<int>(2, INF));
    dp[0][0] = 0;

    for (int x : a) {
        vector<vector<int>> next_dp(m + 1, vector<int>(2, INF));
        for (int s = 0; s <= m; ++s) {
            // Erase x
            next_dp[s][1] = min(dp[s][1], dp[s][0] + 1);

            // Keep x
            if (s + x <= m) {
                next_dp[s + x][0] = min(dp[s][0], dp[s][1]);
            }
        }
        dp = move(next_dp);
    }

    for (int z = 1; z <= m; ++z) {
        int ans = min(dp[z][0], dp[z][1]);
        cout << (ans >= INF ? -1 : ans) << "\n";
    }

    return 0;
}
```
