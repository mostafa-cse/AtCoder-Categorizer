# Tree Edge Cut Orienting with Subtree Difference Array DFS

**Domain**: `Data Structures`  
**Subtopic**: `Tree Difference Arrays`  

This workbook contains curated, high-quality competitive programming problems teaching **Tree Edge Cut Orienting with Subtree Difference Array DFS**.

---

## Curated Problems

### [problem:AtCoder-abc187_e] — Through Path
- **Contest**: `abc187`
- **Rating / Difficulty**: 1358
- **Specific Skill**: Tree Edge Cut Orienting with Subtree Difference Array DFS
- **Individual Analysis**: [`../../analysis/AtCoder-abc187_e.md`](../../analysis/AtCoder-abc187_e.md)
- **Problem Statement Summary**: Given a tree with N vertices. Q queries: (t, e, x) where edge e connects a and b. If t=1, add x to all vertices reachable from a without crossing edge e. If t=2, add x to all vertices reachable from b without crossing edge e. Find final values.
- **Core Insight**: Root the tree at vertex 1 and compute depth[v]. Between endpoints a and b of edge e, let deeper endpoint be child, other be parent. (1) If we want to add x to child's component: add +x to child's subtree! (2) If we want to add x to parent's component: add +x to ALL vertices (global val[1] += x) and subtract -x from child's subtree (val[child] -= x). Propagate in a single DFS!
- **Complexity**: Time: `O(N + Q)` | Space: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>

using namespace std;

struct Edge {
    int u, v;
};

void get_depth(int u, int p, int d, const vector<vector<int>>& adj, vector<int>& depth) {
    depth[u] = d;
    for (int v : adj[u]) {
        if (v != p) {
            get_depth(v, u, d + 1, adj, depth);
        }
    }
}

void dfs_propagate(int u, int p, const vector<vector<int>>& adj, vector<long long>& val) {
    for (int v : adj[u]) {
        if (v != p) {
            val[v] += val[u];
            dfs_propagate(v, u, adj, val);
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<int>> adj(n + 1);
    vector<Edge> edges(n);
    for (int i = 1; i <= n - 1; ++i) {
        cin >> edges[i].u >> edges[i].v;
        adj[edges[i].u].push_back(edges[i].v);
        adj[edges[i].v].push_back(edges[i].u);
    }

    vector<int> depth(n + 1, 0);
    get_depth(1, 0, 1, adj, depth);

    vector<long long> val(n + 1, 0);
    int q;
    cin >> q;

    while (q--) {
        int t, e;
        long long x;
        cin >> t >> e >> x;

        int u = edges[e].u;
        int v = edges[e].v;
        int from_node = (t == 1 ? u : v);
        int other_node = (t == 1 ? v : u);

        if (depth[from_node] > depth[other_node]) {
            val[from_node] += x;
        } else {
            val[1] += x;
            val[other_node] -= x;
        }
    }

    dfs_propagate(1, 0, adj, val);

    for (int i = 1; i <= n; ++i) {
        cout << val[i] << "\n";
    }

    return 0;
}
```
