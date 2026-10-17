# Cycle Length upon Edge Addition via Tree LCA (dist(u, v) + 1)

**Domain**: `Graph Theory`  
**Subtopic**: `Tree LCA`  

This workbook contains curated, high-quality competitive programming problems teaching **Cycle Length upon Edge Addition via Tree LCA (dist(u, v) + 1)**.

---

## Curated Problems

### `[problem:AtCoder-abc014_4]` — 閉路
- **Rating / Difficulty**: 1856
- **Contest**: `abc014`
- **Analysis**: [`analysis/AtCoder-abc014_4.md`](../../analysis/AtCoder-abc014_4.md)
- **Key Idea**: Adding edge (u, v) creates a cycle consisting of the tree path between u and v plus the new edge. Cycle length = dist(u, v) + 1 = depth[u] + depth[v] - 2 * depth[LCA(u, v)] + 1.
- **Time Complexity**: `O((N + Q) log N)`
- **Space Complexity**: `O(N log N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>

using namespace std;

int n, q;
vector<vector<int>> adj;
vector<int> depth;
int up[20][100005];

void dfs(int u, int p, int d) {
    depth[u] = d;
    up[0][u] = p;
    for (int k = 1; k < 20; ++k) {
        up[k][u] = up[k - 1][up[k - 1][u]];
    }
    for (int v : adj[u]) {
        if (v != p) dfs(v, u, d + 1);
    }
}

int get_lca(int u, int v) {
    if (depth[u] < depth[v]) swap(u, v);
    for (int k = 19; k >= 0; --k) {
        if (depth[u] - (1 << k) >= depth[v]) {
            u = up[k][u];
        }
    }
    if (u == v) return u;
    for (int k = 19; k >= 0; --k) {
        if (up[k][u] != up[k][v]) {
            u = up[k][u];
            v = up[k][v];
        }
    }
    return up[0][u];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n)) return 0;

    adj.assign(n + 1, vector<int>());
    depth.assign(n + 1, 0);

    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    dfs(1, 1, 0);

    cin >> q;
    while (q--) {
        int u, v;
        cin >> u >> v;
        int lca = get_lca(u, v);
        int cycle_len = depth[u] + depth[v] - 2 * depth[lca] + 1;
        cout << cycle_len << "\n";
    }

    return 0;
}
```
