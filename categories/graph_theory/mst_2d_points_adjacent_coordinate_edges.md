# Minimum Spanning Tree on 2D Points via Adjacent Coordinate Edges

**Domain**: `Graph Theory`  
**Subtopic**: `Minimum Spanning Tree`  

This workbook contains curated, high-quality competitive programming problems teaching **Minimum Spanning Tree on 2D Points via Adjacent Coordinate Edges**.

---

## Curated Problems

### `[problem:AtCoder-arc076_b]` — Built?
- **Rating / Difficulty**: 1615
- **Contest**: `abc065`
- **Analysis**: [`analysis/AtCoder-arc076_b.md`](../../analysis/AtCoder-arc076_b.md)
- **Key Idea**: The complete graph has N*(N-1)/2 edges, which is too dense for N = 10^5. In any MST under min-coordinate metric, we only need edges between adjacent points when sorted by x-coordinate, and adjacent points when sorted by y-coordinate.
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

struct Point {
    int id;
    long long x, y;
};

struct Edge {
    int u, v;
    long long cost;
    bool operator<(const Edge& other) const {
        return cost < other.cost;
    }
};

struct DSU {
    vector<int> parent;
    DSU(int n) : parent(n + 1) {
        iota(parent.begin(), parent.end(), 0);
    }
    int find(int u) {
        return parent[u] == u ? u : parent[u] = find(parent[u]);
    }
    bool unite(int u, int v) {
        int ru = find(u), rv = find(v);
        if (ru == rv) return false;
        parent[ru] = rv;
        return true;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<Point> pts(n);
    for (int i = 0; i < n; ++i) {
        pts[i].id = i;
        cin >> pts[i].x >> pts[i].y;
    }

    vector<Edge> edges;

    // Adjacent edges by X
    sort(pts.begin(), pts.end(), [](const Point& a, const Point& b) {
        return a.x < b.x;
    });
    for (int i = 0; i < n - 1; ++i) {
        edges.push_back({pts[i].id, pts[i + 1].id, pts[i + 1].x - pts[i].x});
    }

    // Adjacent edges by Y
    sort(pts.begin(), pts.end(), [](const Point& a, const Point& b) {
        return a.y < b.y;
    });
    for (int i = 0; i < n - 1; ++i) {
        edges.push_back({pts[i].id, pts[i + 1].id, pts[i + 1].y - pts[i].y});
    }

    sort(edges.begin(), edges.end());

    DSU dsu(n);
    long long mst_cost = 0;
    int edges_used = 0;

    for (const auto& e : edges) {
        if (dsu.unite(e.u, e.v)) {
            mst_cost += e.cost;
            if (++edges_used == n - 1) break;
        }
    }

    cout << mst_cost << "\n";
    return 0;
}
```
