# Order-Dependent 0-1 Knapsack (Sorting by Time Before DP)

**Domain**: `Dynamic Programming`  
**Subtopic**: `Classic DP`  

This workbook contains curated, high-quality competitive programming problems teaching **Order-Dependent 0-1 Knapsack (Sorting by Time Before DP)**.

---

## Curated Problems

### `[problem:AtCoder-abc145_e]` — All-you-can-eat
- **Rating / Difficulty**: 1528
- **Contest**: `abc145`
- **Analysis**: [`analysis/AtCoder-abc145_e.md`](../../analysis/AtCoder-abc145_e.md)
- **Key Idea**: The final dish ordered can exceed time limit T. By sorting dishes by eating time A_i ascending, the dish that exceeds T can always be assumed to be the LAST dish processed in the DP sequence.
- **Time Complexity**: `O(N * T)`
- **Space Complexity**: `O(T)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, T;
    if (!(cin >> n >> T)) return 0;

    vector<pair<int, int>> dishes(n);
    for (int i = 0; i < n; ++i) {
        cin >> dishes[i].first >> dishes[i].second;
    }

    // Sort by eating time ascending
    sort(dishes.begin(), dishes.end());

    vector<int> dp(T, 0);
    int ans = 0;

    for (int i = 0; i < n; ++i) {
        int a = dishes[i].first;
        int b = dishes[i].second;

        // Try using dish i as the final (overflowing) dish
        for (int t = 0; t < T; ++t) {
            ans = max(ans, dp[t] + b);
        }

        // Standard 0-1 knapsack transition for time < T
        for (int t = T - 1; t >= a; --t) {
            dp[t] = max(dp[t], dp[t - a] + b);
        }
    }

    cout << ans << "\n";
    return 0;
}
```
