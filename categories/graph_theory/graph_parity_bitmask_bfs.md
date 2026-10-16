# Shortest Path on Graph with Bitmask Parities (0-1 BFS)

**Domain**: `Graph Theory`  
**Subtopic**: `Breadth-First Search (BFS)`  

This workbook contains curated, high-quality competitive programming problems teaching **Shortest Path on Graph with Bitmask Parities (0-1 BFS)**.

---

## Curated Problems

### `[problem:AtCoder-abc244_f]` — Shortest Good Path
- **Rating / Difficulty**: 1661
- **Contest**: `abc244`
- **Analysis**: [`analysis/AtCoder-abc244_f.md`](../../analysis/AtCoder-abc244_f.md)
- **Key Idea**: Multi-source BFS on the state space (u, mask) where u is the current vertex and mask in 0..2^N - 1 is the bitmask of odd-visit vertices. Moving from u to v toggles bit v in mask.
- **Time Complexity**: `O(N * 2^N + M * 2^N)`
- **Space Complexity**: `O(N * 2^N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<int>> adj(n);
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        --u; --v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    int total_masks = 1 << n;
    vector<vector<int>> dist(n, vector<int>(total_masks, -1));
    queue<pair<int, int>> q;

    for (int i = 0; i < n; ++i) {
        dist[i][1 << i] = 1;
        q.push({i, 1 << i});
    }

    while (!q.empty()) {
        auto [u, mask] = q.front();
        q.pop();

        for (int v : adj[u]) {
            int next_mask = mask ^ (1 << v);
            if (dist[v][next_mask] == -1) {
                dist[v][next_mask] = dist[u][mask] + 1;
                q.push({v, next_mask});
            }
        }
    }

    long long total_len = 0;
    for (int mask = 1; mask < total_masks; ++mask) {
        int min_d = 1e9;
        for (int u = 0; u < n; ++u) {
            if (dist[u][mask] != -1) {
                min_d = min(min_d, dist[u][mask]);
            }
        }
        total_len += min_d;
    }

    cout << total_len << "\n";
    return 0;
}
```
