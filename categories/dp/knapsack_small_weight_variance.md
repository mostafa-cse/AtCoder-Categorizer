# Knapsack with Small Weight Variance [W, W+3]

**Domain**: `Dynamic Programming`  
**Subtopic**: `Classic DP`  

This workbook contains curated, high-quality competitive programming problems teaching **Knapsack with Small Weight Variance [W, W+3]**.

---

## Curated Problems

### `[problem:AtCoder-arc073_b]` — Simple Knapsack
- **Rating / Difficulty**: 1477
- **Contest**: `abc060`
- **Analysis**: [`analysis/AtCoder-arc073_b.md`](../../analysis/AtCoder-arc073_b.md)
- **Key Idea**: Partition items into 4 groups by offset d = w_i - w_1 in {0, 1, 2, 3}. Sort each group by value descending, and iterate over how many items are selected from each group.
- **Time Complexity**: `O(N^4)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long W;
    if (!(cin >> n >> W)) return 0;

    long long w1;
    vector<long long> g[4];

    for (int i = 0; i < n; ++i) {
        long long w, v;
        cin >> w >> v;
        if (i == 0) w1 = w;
        g[w - w1].push_back(v);
    }

    for (int d = 0; d < 4; ++d) {
        sort(g[d].rbegin(), g[d].rend());
    }

    vector<long long> pref[4];
    for (int d = 0; d < 4; ++d) {
        pref[d].resize(g[d].size() + 1, 0);
        for (size_t i = 0; i < g[d].size(); ++i) {
            pref[d][i + 1] = pref[d][i] + g[d][i];
        }
    }

    long long ans = 0;

    for (size_t c0 = 0; c0 <= g[0].size(); ++c0) {
        for (size_t c1 = 0; c1 <= g[1].size(); ++c1) {
            for (size_t c2 = 0; c2 <= g[2].size(); ++c2) {
                for (size_t c3 = 0; c3 <= g[3].size(); ++c3) {
                    long long total_items = c0 + c1 + c2 + c3;
                    long long total_weight = total_items * w1 + 1 * c1 + 2 * c2 + 3 * c3;
                    if (total_weight <= W) {
                        ans = max(ans, pref[0][c0] + pref[1][c1] + pref[2][c2] + pref[3][c3]);
                    }
                }
            }
        }
    }

    cout << ans << "\n";
    return 0;
}
```
