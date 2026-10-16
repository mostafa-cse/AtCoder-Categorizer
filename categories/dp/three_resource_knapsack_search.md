# 3-Resource Dual Knapsack DP with Monotonic Search

**Domain**: `Dynamic Programming`  
**Subtopic**: `Knapsack DP`  

This workbook contains curated, high-quality competitive programming problems teaching **3-Resource Dual Knapsack DP with Monotonic Search**.

---

## Curated Problems

### [problem:AtCoder-abc390_e] — Vitamin Balance
- **Contest**: `abc390`
- **Rating / Difficulty**: 1227
- **Specific Skill**: 3-Resource Dual Knapsack DP with Monotonic Search
- **Individual Analysis**: [`../../analysis/AtCoder-abc390_e.md`](../../analysis/AtCoder-abc390_e.md)
- **Problem Statement Summary**: N foods. Food i provides vitamin V_i in {1, 2, 3} with amount A_i and calories C_i. Total calories <= X. Maximize min(total vitamin 1, total vitamin 2, total vitamin 3).
- **Core Insight**: For each vitamin group, compute 0-1 Knapsack: dp[v][cal] = max vitamin v obtained using exactly cal calories. Then binary search on target vitamin minimum T: for each vitamin group, find the minimum calories needed to achieve >= T vitamins. If sum of min calories across all 3 groups <= X, target T is feasible.
- **Complexity**: Time: `O(N * X + log(MAX) * 3 * log X)` | Space: `O(3 * X)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Food {
    int v;
    long long a, c;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, x;
    if (!(cin >> n >> x)) return 0;

    vector<vector<pair<long long, int>>> groups(4);
    for (int i = 0; i < n; ++i) {
        int v, c;
        long long a;
        cin >> v >> a >> c;
        groups[v].push_back({a, c});
    }

    vector<vector<long long>> dp(4, vector<long long>(x + 1, 0));

    for (int v = 1; v <= 3; ++v) {
        for (const auto& [amt, cal] : groups[v]) {
            for (int c = x; c >= cal; --c) {
                dp[v][c] = max(dp[v][c], dp[v][c - cal] + amt);
            }
        }
        for (int c = 1; c <= x; ++c) {
            dp[v][c] = max(dp[v][c], dp[v][c - 1]);
        }
    }

    long long low = 0, high = 1e9, ans = 0;
    while (low <= high) {
        long long mid = low + (high - low) / 2;
        int total_cal = 0;
        bool ok = true;

        for (int v = 1; v <= 3; ++v) {
            auto it = lower_bound(dp[v].begin(), dp[v].end(), mid);
            if (it == dp[v].end()) {
                ok = false;
                break;
            }
            total_cal += (it - dp[v].begin());
        }

        if (ok && total_cal <= x) {
            ans = mid;
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }

    cout << ans << "\n";
    return 0;
}
```
