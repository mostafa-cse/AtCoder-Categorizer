# Centroid Decomposition

**Domain**: `Data Structures (DS)`  
**Subtopic**: `Centroid Decomposition`  

This workbook contains curated, high-quality competitive programming problems teaching **Centroid Decomposition**.

---

## Curated Problems

### `[problem:AtCoder-abc291_h]` — Centroid Decomposition Tree
- **Rating / Difficulty**: 2090
- **Contest**: `abc291`
- **Analysis**: [`analysis/AtCoder-abc291_h.md`](../../analysis/AtCoder-abc291_h.md)
- **Key Idea**: The two required properties are precisely the defining invariants of the Centroid Decomposition Tree of T! The centroid of any tree splits the remaining components into sizes at most N / 2, and every path between vertices in different components passes through the centroid (which serves as their LCA in the centroid tree). Thus, the problem is solved by computing the Centroid Decomposition of the given tree T and outputting the centroid tree's parent pointers.
- **Time Complexity**: `O(N log N)`
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
vector<bool> removed;
vector<int> parent_r;

void get_sizes(int u, int p) {
    sz[u] = 1;
    for (int v : adj[u]) {
        if (v != p && !removed[v]) {
            get_sizes(v, u);
            sz[u] += sz[v];
        }
    }
}

int get_centroid(int u, int p, int total) {
    for (int v : adj[u]) {
        if (v != p && !removed[v] && sz[v] > total / 2) {
            return get_centroid(v, u, total);
        }
    }
    return u;
}

void decompose(int u, int p) {
    get_sizes(u, -1);
    int c = get_centroid(u, -1, sz[u]);

    parent_r[c] = p;
    removed[c] = true;

    for (int v : adj[c]) {
        if (!removed[v]) {
            decompose(v, c);
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n)) return 0;

    adj.assign(n + 1, vector<int>());
    sz.assign(n + 1, 0);
    removed.assign(n + 1, false);
    parent_r.assign(n + 1, -1);

    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    decompose(1, -1);

    for (int i = 1; i <= n; ++i) {
        cout << parent_r[i] << (i == n ? "" : " ");
    }
    cout << "\n";

    return 0;
}
```
