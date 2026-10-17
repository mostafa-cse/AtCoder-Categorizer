# Knapsack and Basic Dynamic Programming

**Domain**: `Dynamic Programming (DP)`  
**Subtopic**: `Intro to DP`  

This workbook contains curated, high-quality competitive programming problems teaching **Knapsack and Basic Dynamic Programming**.

---

## Curated Problems

### `[problem:AtCoder-abc145_f]` — Laminate
- **Rating / Difficulty**: 2116
- **Contest**: `abc145`
- **Analysis**: [`analysis/AtCoder-abc145_f.md`](../../analysis/AtCoder-abc145_f.md)
- **Key Idea**: Changing at most K columns is equivalent to choosing M = N - K columns to KEEP at their original heights! The optimal choice for intermediate changed columns between two kept columns i and j is to set them to min(H_i, H_j), incurring cost max(0, H_j - H_i). We define dp[i][cnt] as the minimum cost for a prefix ending at kept column i with cnt columns kept. Transitions iterate over all previous kept columns i < j in O(N^2 * (N - K)).
- **Time Complexity**: `O(N^2 * (N - K))`
- **Space Complexity**: `O(N * (N - K))`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const long long INF = 1e18;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> h(n + 1, 0);
    for (int i = 1; i <= n; ++i) cin >> h[i];

    int m = n - k;
    if (m <= 0) {
        cout << 0 << "\n";
        return 0;
    }

    vector<vector<long long>> dp(n + 1, vector<long long>(m + 1, INF));
    dp[0][0] = 0;

    for (int i = 0; i <= n; ++i) {
        for (int cnt = 0; cnt <= m; ++cnt) {
            if (dp[i][cnt] >= INF) continue;
            for (int j = i + 1; j <= n; ++j) {
                if (cnt + 1 <= m) {
                    long long cost = max(0LL, h[j] - h[i]);
                    dp[j][cnt + 1] = min(dp[j][cnt + 1], dp[i][cnt] + cost);
                }
            }
        }
    }

    long long ans = INF;
    for (int i = 1; i <= n; ++i) {
        ans = min(ans, dp[i][m]);
    }

    cout << ans << "\n";
    return 0;
}
```
