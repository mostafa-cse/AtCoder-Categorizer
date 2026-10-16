# Euler Tour Subtree Range Query + Depth Coordinate Binary Search

**Domain**: `Graph Theory`  
**Subtopic**: `Trees`  

This workbook contains curated, high-quality competitive programming problems teaching **Euler Tour Subtree Range Query + Depth Coordinate Binary Search**.

---

## Curated Problems

### `[problem:AtCoder-abc202_e]` — Count Descendants
- **Rating / Difficulty**: 1638
- **Contest**: `abc202`
- **Analysis**: [`analysis/AtCoder-abc202_e.md`](../../analysis/AtCoder-abc202_e.md)
- **Key Idea**: Flatten the tree using an Euler tour. A vertex v is in the subtree of u iff in[u] <= in[v] < out[u]. For each depth d, store all in[v] of vertices at depth d in sorted order.
- **Time Complexity**: `O((N + Q) log N)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<vector<int>> adj;
vector<int> tin, tout, depth;
vector<vector<int>> depth_nodes;
int timer_cnt = 0;

void dfs(int u, int p, int d) {
    depth[u] = d;
    tin[u] = ++timer_cnt;
    depth_nodes[d].push_back(tin[u]);

    for (int v : adj[u]) {
        if (v != p) {
            dfs(v, u, d + 1);
        }
    }
    tout[u] = timer_cnt;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    adj.resize(n + 1);
    tin.resize(n + 1);
    tout.resize(n + 1);
    depth.resize(n + 1);
    depth_nodes.resize(n + 1);

    for (int i = 2; i <= n; ++i) {
        int p;
        cin >> p;
        adj[p].push_back(i);
    }

    dfs(1, 0, 0);

    int q;
    cin >> q;
    while (q--) {
        int u, d;
        cin >> u >> d;
        if (d >= (int)depth_nodes.size()) {
            cout << 0 << "\n";
            continue;
        }

        const auto& vec = depth_nodes[d];
        auto it1 = lower_bound(vec.begin(), vec.end(), tin[u]);
        auto it2 = upper_bound(vec.begin(), vec.end(), tout[u]);
        cout << (it2 - it1) << "\n";
    }

    return 0;
}
```
