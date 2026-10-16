# Tree Subtree Imos / Prefix Sum DFS Propagation

**Domain**: `Data Structures`  
**Subtopic**: `Trees & Difference Arrays`  

This workbook contains curated, high-quality competitive programming problems teaching **Tree Subtree Imos / Prefix Sum DFS Propagation**.

---

## Curated Problems

### [problem:AtCoder-abc138_d] — Ki
- **Contest**: `abc138`
- **Rating / Difficulty**: 920
- **Specific Skill**: Tree Subtree Imos / Prefix Sum DFS Propagation
- **Individual Analysis**: [`../../analysis/AtCoder-abc138_d.md`](../../analysis/AtCoder-abc138_d.md)
- **Problem Statement Summary**: Given a tree rooted at vertex 1 with N vertices. Q queries add value x to all vertices in the subtree rooted at vertex p. Find the final values of all vertices.
- **Core Insight**: Run a single DFS from root 1. The cumulative sum of values along the path from root 1 to vertex u gives the total additions applied to all ancestor subtrees containing u.
- **Complexity**: Time: `O(N + Q)` | Space: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>

using namespace std;

void dfs(int u, int p, const vector<vector<int>>& adj, vector<long long>& val) {
    for (int v : adj[u]) {
        if (v != p) {
            val[v] += val[u];
            dfs(v, u, adj, val);
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    vector<long long> val(n + 1, 0);
    for (int i = 0; i < q; ++i) {
        int p;
        long long x;
        cin >> p >> x;
        val[p] += x;
    }

    dfs(1, 0, adj, val);

    for (int i = 1; i <= n; ++i) {
        cout << val[i] << (i == n ? '\n' : ' ');
    }

    return 0;
}
```
