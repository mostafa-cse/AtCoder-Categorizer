# Maximum Clique via Bitmask Verification

**Domain**: `Basics`  
**Subtopic**: `Exhaustive Search`  

This workbook contains curated, high-quality competitive programming problems teaching **Maximum Clique via Bitmask Verification**.

---

## Curated Problems

### `[problem:AtCoder-abc002_4]` — Faction
- **Rating / Difficulty**: 1418
- **Contest**: `abc002`
- **Analysis**: [`analysis/AtCoder-abc002_4.md`](../../analysis/AtCoder-abc002_4.md)
- **Key Idea**: Since N <= 12 is very small, enumerate all 2^N subsets of politicians using bitmasks and verify pairwise mutual acquaintance in O(N^2).
- **Time Complexity**: `O(2^N * N^2)`
- **Space Complexity**: `O(N^2)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<bool>> adj(n, vector<bool>(n, false));
    for (int i = 0; i < n; ++i) adj[i][i] = true;

    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        --u; --v;
        adj[u][v] = adj[v][u] = true;
    }

    int max_clique = 1;
    int total_masks = 1 << n;

    for (int mask = 1; mask < total_masks; ++mask) {
        int size = __builtin_popcount(mask);
        if (size <= max_clique) continue;

        bool is_clique = true;
        for (int i = 0; i < n; ++i) {
            if (!(mask & (1 << i))) continue;
            for (int j = i + 1; j < n; ++j) {
                if (!(mask & (1 << j))) continue;
                if (!adj[i][j]) {
                    is_clique = false;
                    break;
                }
            }
            if (!is_clique) break;
        }

        if (is_clique) {
            max_clique = size;
        }
    }

    cout << max_clique << "\n";
    return 0;
}
```
