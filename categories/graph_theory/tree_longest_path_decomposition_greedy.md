# Tree Longest Path Decomposition and Greedy Subtree Weight

**Domain**: `Graph Theory`  
**Subtopic**: `Trees`  

This workbook contains curated, high-quality competitive programming problems teaching **Tree Longest Path Decomposition and Greedy Subtree Weight**.

---

## Curated Problems

### `[problem:AtCoder-abc369_g]` — As far as possible
- **Rating / Difficulty**: 2055
- **Contest**: `abc369`
- **Analysis**: [`analysis/AtCoder-abc369_g.md`](../../analysis/AtCoder-abc369_g.md)
- **Key Idea**: The shortest walk visiting a set S of vertices and starting/ending at 1 traverses every edge in the minimal subtree spanning S U {1} exactly twice. To maximize this subtree weight by picking K vertices, we root the tree at 1 and decompose the tree into disjoint paths by iteratively choosing the deepest child (heavy-light style longest-path decomposition). By submodularity of subtree edge weights, the optimal selection for any K is greedily formed by the sum of lengths of the top K paths in this longest-path decomposition.
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Edge {
    int to;
    long long w;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<Edge>> adj(n + 1);
    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        long long w;
        cin >> u >> v >> w;
        adj[u].push_back({v, w});
        adj[v].push_back({u, w});
    }

    vector<long long> max_d(n + 1, 0);
    vector<int> heavy(n + 1, 0);

    auto dfs1 = [&](auto& self, int u, int p) -> void {
        for (auto& e : adj[u]) {
            if (e.to == p) continue;
            self(self, e.to, u);
            if (max_d[e.to] + e.w > max_d[u]) {
                max_d[u] = max_d[e.to] + e.w;
                heavy[u] = e.to;
            }
        }
    };
    dfs1(dfs1, 1, 0);

    vector<long long> paths;
    auto dfs2 = [&](auto& self, int u, int p, long long cur_len) -> void {
        if (heavy[u] != 0) {
            long long w = 0;
            for (auto& e : adj[u]) {
                if (e.to == heavy[u]) {
                    w = e.w;
                    break;
                }
            }
            self(self, heavy[u], u, cur_len + w);
        } else {
            paths.push_back(cur_len);
        }
        for (auto& e : adj[u]) {
            if (e.to == p || e.to == heavy[u]) continue;
            self(self, e.to, u, e.w);
        }
    };
    dfs2(dfs2, 1, 0, 0);

    sort(paths.rbegin(), paths.rend());

    long long current_sum = 0;
    int num_paths = paths.size();
    for (int k = 1; k <= n; ++k) {
        if (k - 1 < num_paths) {
            current_sum += paths[k - 1];
        }
        cout << current_sum * 2 << "\n";
    }
    return 0;
}
```
