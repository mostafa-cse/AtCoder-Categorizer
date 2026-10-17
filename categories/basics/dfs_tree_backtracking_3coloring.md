# DFS Tree Order Backtracking on Small-Graph 3-Coloring with Root Symmetry

**Domain**: `Basics`  
**Subtopic**: `Backtracking / DFS Tree`  

This workbook contains curated, high-quality competitive programming problems teaching **DFS Tree Order Backtracking on Small-Graph 3-Coloring with Root Symmetry**.

---

## Curated Problems

### `[problem:AtCoder-abc199_d]` — RGB Coloring 2
- **Rating / Difficulty**: 1804
- **Contest**: `abc199`
- **Analysis**: [`analysis/AtCoder-abc199_d.md`](../../analysis/AtCoder-abc199_d.md)
- **Key Idea**: The graph splits into connected components. For each component, build a DFS tree. Fix the root's color to 0 (multiply result by 3 by symmetry). Backtrack through vertices in DFS preorder: each vertex has at most 2 valid colors (different from its parent), reducing search states to at most 2^{N-1} <= 2^{19} ~ 5 * 10^5.
- **Time Complexity**: `O(3 * 2^N)`
- **Space Complexity**: `O(N + M)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>

using namespace std;

int n, m;
vector<vector<int>> adj;
vector<bool> visited;
vector<int> comp_order;
vector<int> color;

void get_dfs_order(int u) {
    visited[u] = true;
    comp_order.push_back(u);
    for (int v : adj[u]) {
        if (!visited[v]) get_dfs_order(v);
    }
}

long long dfs_color(int idx) {
    if (idx == (int)comp_order.size()) return 1;

    int u = comp_order[idx];
    long long ways = 0;

    for (int c = 0; c < 3; ++c) {
        bool ok = true;
        for (int v : adj[u]) {
            if (color[v] == c) {
                ok = false;
                break;
            }
        }
        if (ok) {
            color[u] = c;
            ways += dfs_color(idx + 1);
            color[u] = -1;
        }
    }

    return ways;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n >> m)) return 0;

    adj.assign(n, vector<int>());
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        --u; --v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    visited.assign(n, false);
    color.assign(n, -1);
    long long total_ans = 1;

    for (int i = 0; i < n; ++i) {
        if (!visited[i]) {
            comp_order.clear();
            get_dfs_order(i);

            color[comp_order[0]] = 0;
            long long comp_ways = 3LL * dfs_color(1);
            color[comp_order[0]] = -1;

            total_ans *= comp_ways;
        }
    }

    cout << total_ans << "\n";
    return 0;
}
```
