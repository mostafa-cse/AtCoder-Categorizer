# Cut-Edge / Bridge Detection via DFS / DSU Edge Removal

**Domain**: `Graph Theory`  
**Subtopic**: `Connectivity & Bridges`  

This workbook contains curated, high-quality competitive programming problems teaching **Cut-Edge / Bridge Detection via DFS / DSU Edge Removal**.

---

## Curated Problems

### [problem:AtCoder-abc075_c] — Bridge
- **Contest**: `abc075`
- **Rating / Difficulty**: 1067
- **Specific Skill**: Cut-Edge / Bridge Detection via DFS / DSU Edge Removal
- **Individual Analysis**: [`../../analysis/AtCoder-abc075_c.md`](../../analysis/AtCoder-abc075_c.md)
- **Problem Statement Summary**: Given a connected undirected graph with N vertices and M edges (N, M <= 50). Count the number of bridges (edges whose removal increases connected components).
- **Core Insight**: Because N, M <= 50 are very small, we can test each edge independently in O(M): remove edge e, build DSU with the remaining M - 1 edges, and check if all vertices belong to a single connected component.
- **Complexity**: Time: `O(M^2 * alpha(N))` | Space: `O(N + M)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

struct DSU {
    vector<int> parent;
    int components;
    DSU(int n) : parent(n + 1), components(n) {
        iota(parent.begin(), parent.end(), 0);
    }
    int find(int i) {
        if (parent[i] == i) return i;
        return parent[i] = find(parent[i]);
    }
    void unite(int i, int j) {
        int root_i = find(i);
        int root_j = find(j);
        if (root_i != root_j) {
            parent[root_i] = root_j;
            components--;
        }
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

    vector<Edge> edges(m);
    for (int i = 0; i < m; ++i) {
        cin >> edges[i].u >> edges[i].v;
    }

    int bridges = 0;
    for (int i = 0; i < m; ++i) {
        DSU dsu(n);
        for (int j = 0; j < m; ++j) {
            if (i == j) continue;
            dsu.unite(edges[j].u, edges[j].v);
        }
        if (dsu.components > 1) {
            bridges++;
        }
    }

    cout << bridges << "\n";
    return 0;
}
```
