# Topological Ordering Count via Bitmask DP

**Domain**: `Dynamic Programming`  
**Subtopic**: `Bitmask DP`  

This workbook contains curated, high-quality competitive programming problems teaching **Topological Ordering Count via Bitmask DP**.

---

## Curated Problems

### `[problem:AtCoder-abc041_d]` — Footrace
- **Rating / Difficulty**: 1670
- **Contest**: `abc041`
- **Analysis**: [`analysis/AtCoder-abc041_d.md`](../../analysis/AtCoder-abc041_d.md)
- **Key Idea**: Dynamic programming on subsets! `dp[mask]` = number of valid topological orderings of the subset of runners in mask. To transition, append a runner v not in mask provided no predecessor of v is missing from mask.
- **Time Complexity**: `O(N * 2^N)`
- **Space Complexity**: `O(2^N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<int> pred(n, 0);
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        --u; --v;
        pred[v] |= (1 << u);
    }

    int total_masks = 1 << n;
    vector<long long> dp(total_masks, 0);
    dp[0] = 1;

    for (int mask = 0; mask < total_masks; ++mask) {
        if (!dp[mask]) continue;

        for (int v = 0; v < n; ++v) {
            if (!(mask & (1 << v))) {
                if ((pred[v] & ~mask) == 0) {
                    dp[mask | (1 << v)] += dp[mask];
                }
            }
        }
    }

    cout << dp[total_masks - 1] << "\n";
    return 0;
}
```
