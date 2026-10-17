# Exact Cardinality Modulo Remainder Knapsack DP

**Domain**: `Dynamic Programming`  
**Subtopic**: `Knapsack DP`  

This workbook contains curated, high-quality competitive programming problems teaching **Exact Cardinality Modulo Remainder Knapsack DP**.

---

## Curated Problems

### `[problem:AtCoder-abc192_f]` — Potion
- **Rating / Difficulty**: 1783
- **Contest**: `abc192`
- **Analysis**: [`analysis/AtCoder-abc192_f.md`](../../analysis/AtCoder-abc192_f.md)
- **Key Idea**: Iterate over the exact number of ingredients k from 1 to N. For a fixed k, we need to choose k elements whose sum S <= X satisfies S = X (mod k) and maximizes S. Run a 2D Knapsack DP dp[c][r] = max sum of c items with remainder r mod k.
- **Time Complexity**: `O(N^4)`
- **Space Complexity**: `O(N^2)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const long long INF = 4e18;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long x;
    if (!(cin >> n >> x)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    long long min_time = INF;

    for (int k = 1; k <= n; ++k) {
        long long target_rem = x % k;
        vector<vector<long long>> dp(k + 1, vector<long long>(k, -1));
        dp[0][0] = 0;

        for (long long val : a) {
            for (int c = k - 1; c >= 0; --c) {
                for (int r = 0; r < k; ++r) {
                    if (dp[c][r] != -1) {
                        int next_r = (r + val) % k;
                        dp[c + 1][next_r] = max(dp[c + 1][next_r], dp[c][r] + val);
                    }
                }
            }
        }

        if (dp[k][target_rem] > 0 && dp[k][target_rem] <= x) {
            min_time = min(min_time, (x - dp[k][target_rem]) / k);
        }
    }

    cout << min_time << "\n";
    return 0;
}
```
