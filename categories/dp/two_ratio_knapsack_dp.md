# 2-Ratio Knapsack DP / Ratio Reduction to Target GCD

**Domain**: `Dynamic Programming`  
**Subtopic**: `Classic DP`  

This workbook contains curated, high-quality competitive programming problems teaching **2-Ratio Knapsack DP / Ratio Reduction to Target GCD**.

---

## Curated Problems

### `[problem:AtCoder-abc054_d]` — Mixing Experiment
- **Rating / Difficulty**: 1655
- **Contest**: `abc054`
- **Analysis**: [`analysis/AtCoder-abc054_d.md`](../../analysis/AtCoder-abc054_d.md)
- **Key Idea**: 2D Knapsack DP maintaining the exact weights of substance A and B: dp[a][b] = minimum cost to obtain a grams of A and b grams of B. At the end, minimize dp[k * Ma][k * Mb] over all k >= 1.
- **Time Complexity**: `O(N * max_A * max_B)`
- **Space Complexity**: `O(max_A * max_B)`
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

    int n, ma, mb;
    if (!(cin >> n >> ma >> mb)) return 0;

    vector<vector<int>> dp(401, vector<int>(401, INF));
    dp[0][0] = 0;

    for (int i = 0; i < n; ++i) {
        int a, b, c;
        cin >> a >> b >> c;
        for (int sa = 400; sa >= a; --sa) {
            for (int sb = 400; sb >= b; --sb) {
                if (dp[sa - a][sb - b] < INF) {
                    dp[sa][sb] = min(dp[sa][sb], dp[sa - a][sb - b] + c);
                }
            }
        }
    }

    int ans = INF;
    for (int k = 1; k * ma <= 400 && k * mb <= 400; ++k) {
        ans = min(ans, dp[k * ma][k * mb]);
    }

    cout << (ans >= INF ? -1 : ans) << "\n";
    return 0;
}
```
