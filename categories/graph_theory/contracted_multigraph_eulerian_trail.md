# Eulerian Path and Cycle

**Domain**: `Graph Theory`  
**Subtopic**: `Eulerian Path`  

This workbook contains curated, high-quality competitive programming problems teaching **Eulerian Path and Cycle**.

---

## Curated Problems

### `[problem:AtCoder-abc286_g]` — Unique Walk
- **Rating / Difficulty**: 2135
- **Contest**: `abc286`
- **Analysis**: [`analysis/AtCoder-abc286_g.md`](../../analysis/AtCoder-abc286_g.md)
- **Key Idea**: Since non-special edges can be traversed arbitrarily many times without restriction, we can contract each connected component formed by non-special edges E \ S into a single super-vertex using DSU. The problem then reduces to determining if the contracted multigraph whose edge set is S possesses an Eulerian trail! An Eulerian trail exists iff the multigraph is connected (ignoring isolated vertices) and the number of vertices with odd degree is either 0 or 2.
- **Time Complexity**: `O(N + M alpha(N))`
- **Space Complexity**: `O(N + M)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

struct DSU {
    vector<int> parent;
    DSU(int n) : parent(n + 1) {
        iota(parent.begin(), parent.end(), 0);
    }
    int find(int i) {
        if (parent[i] == i) return i;
        return parent[i] = find(parent[i]);
    }
    void unite(int u, int v) {
        parent[find(u)] = find(v);
    }
};

struct Edge {
    int u, v;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<Edge> edges(m + 1);
    for (int i = 1; i <= m; ++i) {
        cin >> edges[i].u >> edges[i].v;
    }

    int k;
    cin >> k;
    vector<bool> is_special(m + 1, false);
    for (int i = 0; i < k; ++i) {
        int x;
        cin >> x;
        is_special[x] = true;
    }

    DSU dsu(n);
    for (int i = 1; i <= m; ++i) {
        if (!is_special[i]) {
            dsu.unite(edges[i].u, edges[i].v);
        }
    }

    vector<int> degree(n + 1, 0);
    DSU special_dsu(n);

    int first_special = -1;
    for (int i = 1; i <= m; ++i) {
        if (is_special[i]) {
            int root_u = dsu.find(edges[i].u);
            int root_v = dsu.find(edges[i].v);
            degree[root_u]++;
            degree[root_v]++;
            special_dsu.unite(root_u, root_v);
            first_special = root_u;
        }
    }

    bool connected = true;
    int odd_count = 0;
    for (int i = 1; i <= n; ++i) {
        if (dsu.find(i) == i && degree[i] > 0) {
            if (special_dsu.find(i) != special_dsu.find(first_special)) {
                connected = false;
            }
            if (degree[i] % 2 != 0) {
                odd_count++;
            }
        }
    }

    if (connected && (odd_count == 0 || odd_count == 2)) {
        cout << "Yes\n";
    } else {
        cout << "No\n";
    }

    return 0;
}
```
