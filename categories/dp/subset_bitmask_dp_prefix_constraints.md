# Subset Bitmask DP with Prefix Count Constraints

**Domain**: `Dynamic Programming`  
**Subtopic**: `Bitmask DP`  

This workbook contains curated, high-quality competitive programming problems teaching **Subset Bitmask DP with Prefix Count Constraints**.

---

## Curated Problems

### `[problem:AtCoder-abc199_e]` — Permutation
- **Rating / Difficulty**: 1814
- **Contest**: `abc199`
- **Analysis**: [`analysis/AtCoder-abc199_e.md`](../../analysis/AtCoder-abc199_e.md)
- **Key Idea**: Standard bitmask DP over subsets: dp[mask] is the number of valid prefixes using the elements in mask. The length of the prefix is popcount(mask). Validate all constraints with X_i == popcount(mask) before transitioning.
- **Time Complexity**: `O(N * 2^N)`
- **Space Complexity**: `O(2^N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>

using namespace std;

struct Constraint {
    int y, z;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<Constraint>> cons(n + 1);
    for (int i = 0; i < m; ++i) {
        int x, y, z;
        cin >> x >> y >> z;
        cons[x].push_back({y, z});
    }

    int total_masks = 1 << n;
    vector<long long> dp(total_masks, 0);
    dp[0] = 1;

    for (int mask = 0; mask < total_masks; ++mask) {
        if (dp[mask] == 0) continue;

        int k = __builtin_popcount(mask);

        bool valid = true;
        for (auto& c : cons[k]) {
            int count_le = 0;
            for (int i = 0; i < c.y; ++i) {
                if ((mask >> i) & 1) count_le++;
            }
            if (count_le > c.z) {
                valid = false;
                break;
            }
        }

        if (!valid) {
            dp[mask] = 0;
            continue;
        }

        for (int i = 0; i < n; ++i) {
            if (!((mask >> i) & 1)) {
                dp[mask | (1 << i)] += dp[mask];
            }
        }
    }

    cout << dp[total_masks - 1] << "\n";
    return 0;
}
```
