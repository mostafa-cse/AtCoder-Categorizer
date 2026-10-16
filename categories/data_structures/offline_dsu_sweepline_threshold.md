# Offline Query Sorting with Disjoint Set Union Sweep-Line

**Domain**: `Data Structures`  
**Subtopic**: `Disjoint Set Union (DSU)`  

This workbook contains curated, high-quality competitive programming problems teaching **Offline Query Sorting with Disjoint Set Union Sweep-Line**.

---

## Curated Problems

### `[problem:AtCoder-abc040_d]` — Road Aging Countermeasures
- **Rating / Difficulty**: 1656
- **Contest**: `abc040`
- **Analysis**: [`analysis/AtCoder-abc040_d.md`](../../analysis/AtCoder-abc040_d.md)
- **Key Idea**: Offline query processing! Sort edges descending by year Y_i, and sort queries descending by threshold w. Maintain connected components using DSU.
- **Time Complexity**: `O((M + Q) log(M + Q))`
- **Space Complexity**: `O(N + M + Q)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

struct Edge {
    int u, v, y;
};

struct Query {
    int v, w, id;
};

struct DSU {
    vector<int> parent, sz;
    DSU(int n) : parent(n + 1), sz(n + 1, 1) {
        iota(parent.begin(), parent.end(), 0);
    }
    int find(int u) {
        return parent[u] == u ? u : parent[u] = find(parent[u]);
    }
    void unite(int u, int v) {
        int ru = find(u), rv = find(v);
        if (ru == rv) return;
        if (sz[ru] < sz[rv]) swap(ru, rv);
        parent[rv] = ru;
        sz[ru] += sz[rv];
    }
    int get_size(int u) {
        return sz[find(u)];
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<Edge> edges(m);
    for (int i = 0; i < m; ++i) {
        cin >> edges[i].u >> edges[i].v >> edges[i].y;
    }

    int q;
    cin >> q;
    vector<Query> queries(q);
    for (int i = 0; i < q; ++i) {
        cin >> queries[i].v >> queries[i].w;
        queries[i].id = i;
    }

    sort(edges.begin(), edges.end(), [](const Edge& a, const Edge& b) {
        return a.y > b.y;
    });

    sort(queries.begin(), queries.end(), [](const Query& a, const Query& b) {
        return a.w > b.w;
    });

    DSU dsu(n);
    vector<int> ans(q);
    int edge_idx = 0;

    for (const auto& qry : queries) {
        while (edge_idx < m && edges[edge_idx].y > qry.w) {
            dsu.unite(edges[edge_idx].u, edges[edge_idx].v);
            edge_idx++;
        }
        ans[qry.id] = dsu.get_size(qry.v);
    }

    for (int i = 0; i < q; ++i) {
        cout << ans[i] << "\n";
    }

    return 0;
}
```
