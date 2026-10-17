# Super-Source Vertex Activation Transformation for Minimum Spanning Tree

**Domain**: `Graph Theory`  
**Subtopic**: `Minimum Spanning Tree`  

This workbook contains curated, high-quality competitive programming problems teaching **Super-Source Vertex Activation Transformation for Minimum Spanning Tree**.

---

## Curated Problems

### `[problem:AtCoder-arc029_3]` — 高橋君と国家
- **Rating / Difficulty**: 1973
- **Contest**: `arc029`
- **Analysis**: [`analysis/AtCoder-arc029_3.md`](../../analysis/AtCoder-arc029_3.md)
- **Key Idea**: Building a trade port at city i can be modeled as adding an edge between city i and a virtual 'super-source' vertex 0 with weight c_i. The requirement that every city has a path to at least one trade port is equivalent to requiring that every city is connected to vertex 0! Thus, the problem reduces directly to finding the Minimum Spanning Tree on N + 1 vertices (vertices 0..N) using Kruskal's algorithm with DSU.
- **Time Complexity**: `O((N + M) log(N + M))`
- **Space Complexity**: `O(N + M)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

using namespace std;

struct Edge {
    int u, v;
    long long w;
};

struct DSU {
    vector<int> parent;
    DSU(int n) : parent(n) {
        iota(parent.begin(), parent.end(), 0);
    }
    int find(int v) {
        if (v == parent[v]) return v;
        return parent[v] = find(parent[v]);
    }
    bool unite(int a, int b) {
        a = find(a);
        b = find(b);
        if (a != b) {
            parent[b] = a;
            return true;
        }
        return false;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<Edge> edges;
    for (int i = 1; i <= n; ++i) {
        long long c;
        cin >> c;
        edges.push_back({0, i, c});
    }

    for (int i = 0; i < m; ++i) {
        int u, v;
        long long r;
        cin >> u >> v >> r;
        edges.push_back({u, v, r});
    }

    sort(edges.begin(), edges.end(), [](const Edge& a, const Edge& b) {
        return a.w < b.w;
    });

    DSU dsu(n + 1);
    long long total_cost = 0;
    int edges_used = 0;

    for (const auto& e : edges) {
        if (dsu.unite(e.u, e.v)) {
            total_cost += e.w;
            edges_used++;
            if (edges_used == n) break;
        }
    }

    cout << total_cost << "\n";
    return 0;
}
```
