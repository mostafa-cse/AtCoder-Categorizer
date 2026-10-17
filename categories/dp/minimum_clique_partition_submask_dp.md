# Minimum Clique Partition via O(3^N) Submask Enumeration DP

**Domain**: `Dynamic Programming`  
**Subtopic**: `Bitmask DP`  

This workbook contains curated, high-quality competitive programming problems teaching **Minimum Clique Partition via O(3^N) Submask Enumeration DP**.

---

## Curated Problems

### `[problem:AtCoder-abc187_f]` — Close Group
- **Rating / Difficulty**: 1895
- **Contest**: `abc187`
- **Analysis**: [`analysis/AtCoder-abc187_f.md`](../../analysis/AtCoder-abc187_f.md)
- **Key Idea**: Step 1: Identify all subsets mask that are cliques in O(N * 2^N). For these subsets, dp[mask] = 1. Step 2: For other subsets, partition into two non-empty disjoint submasks: dp[mask] = min_{sub} (dp[sub] + dp[mask ^ sub]).
- **Time Complexity**: `O(3^N)`
- **Space Complexity**: `O(2^N)`
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

    vector<int> adj(n, 0);
    for (int i = 0; i < n; ++i) adj[i] |= (1 << i);

    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        --u; --v;
        adj[u] |= (1 << v);
        adj[v] |= (1 << u);
    }

    int total_masks = 1 << n;
    vector<int> dp(total_masks, INF);

    // Identify cliques
    for (int mask = 1; mask < total_masks; ++mask) {
        bool is_clique = true;
        for (int i = 0; i < n; ++i) {
            if ((mask >> i) & 1) {
                if ((mask & adj[i]) != mask) {
                    is_clique = false;
                    break;
                }
            }
        }
        if (is_clique) dp[mask] = 1;
    }

    // Submask enumeration DP
    for (int mask = 1; mask < total_masks; ++mask) {
        if (dp[mask] == 1) continue;

        for (int sub = (mask - 1) & mask; sub > (mask ^ sub); sub = (sub - 1) & mask) {
            dp[mask] = min(dp[mask], dp[sub] + dp[mask ^ sub]);
        }
    }

    cout << dp[total_masks - 1] << "\n";
    return 0;
}
```
