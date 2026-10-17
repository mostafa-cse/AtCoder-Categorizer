# Tree Node Removal Max-Component Decomposition / Centroid Prerequisite

**Domain**: `Graph Theory`  
**Subtopic**: `Trees`  

This workbook contains curated, high-quality competitive programming problems teaching **Tree Node Removal Max-Component Decomposition / Centroid Prerequisite**.

---

## Curated Problems

### `[problem:AtCoder-arc028_3]` — 高橋王国の分割統治
- **Rating / Difficulty**: 1748
- **Contest**: `arc028`
- **Analysis**: [`analysis/AtCoder-arc028_3.md`](../../analysis/AtCoder-arc028_3.md)
- **Key Idea**: When vertex u is removed, the remaining tree decomposes into components formed by its child subtrees in the DFS tree (each of size sz[v]) and the component containing its parent (of size N - sz[u]).
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int n;
vector<vector<int>> adj;
vector<int> sz;
vector<int> ans;

void dfs(int u, int p) {
    sz[u] = 1;
    int max_c = 0;

    for (int v : adj[u]) {
        if (v != p) {
            dfs(v, u);
            sz[u] += sz[v];
            max_c = max(max_c, sz[v]);
        }
    }

    ans[u] = max(n - sz[u], max_c);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n)) return 0;

    adj.assign(n, vector<int>());
    sz.assign(n, 0);
    ans.assign(n, 0);

    for (int i = 1; i < n; ++i) {
        int p;
        cin >> p;
        adj[p].push_back(i);
        adj[i].push_back(p);
    }

    dfs(0, -1);

    for (int i = 0; i < n; ++i) {
        cout << ans[i] << "\n";
    }

    return 0;
}
```
