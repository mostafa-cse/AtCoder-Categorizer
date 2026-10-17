# DSU / Union Find

**Domain**: `Data Structures (DS)`  
**Subtopic**: `Disjoint Set Union (DSU)`  

This workbook contains curated, high-quality competitive programming problems teaching **DSU / Union Find**.

---

## Curated Problems

### `[problem:AtCoder-abc295_g]` — Minimum Path
- **Rating / Difficulty**: 2086
- **Contest**: `abc295`
- **Analysis**: [`analysis/AtCoder-abc295_g.md`](../../analysis/AtCoder-abc295_g.md)
- **Key Idea**: Initially, from any vertex x, the reachable vertices are only its descendants. When an edge u -> v is added, since v is an ancestor of u, all vertices on the path between v and u form a strongly connected component! Any query asking for the minimum reachable vertex in this cycle can now reach v (and since p_i < i, v has a smaller index than any other node on the path). By using DSU to contract each node along the tree path from u up to v into a single component whose representative stores the highest ancestor (minimum index), each tree edge is contracted at most once. Queries simply output the highest ancestor of the DSU component containing x.
- **Time Complexity**: `O((N + Q) alpha(N))`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

struct DSU {
    vector<int> parent;
    vector<int> min_ancestor;

    DSU(int n) : parent(n + 1), min_ancestor(n + 1) {
        iota(parent.begin(), parent.end(), 0);
        iota(min_ancestor.begin(), min_ancestor.end(), 0);
    }

    int find(int i) {
        if (parent[i] == i)
            return i;
        return parent[i] = find(parent[i]);
    }

    void unite(int u, int v) {
        int root_u = find(u);
        int root_v = find(v);
        if (root_u != root_v) {
            parent[root_u] = root_v;
            min_ancestor[root_v] = min(min_ancestor[root_v], min_ancestor[root_u]);
        }
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> p(n + 1);
    for (int i = 2; i <= n; ++i) {
        cin >> p[i];
    }

    DSU dsu(n);

    int q;
    if (!(cin >> q)) return 0;

    while (q--) {
        int type;
        cin >> type;
        if (type == 1) {
            int u, v;
            cin >> u >> v;
            u = dsu.min_ancestor[dsu.find(u)];
            while (u > v) {
                int par = p[u];
                dsu.unite(u, par);
                u = dsu.min_ancestor[dsu.find(u)];
            }
        } else {
            int x;
            cin >> x;
            cout << dsu.min_ancestor[dsu.find(x)] << "\n";
        }
    }

    return 0;
}
```
