# Problem Analysis: AtCoder-arc076_b — Built?

**Problem ID**: `AtCoder-arc076_b`  
**Contest**: `abc065`  
**Rating / Difficulty**: 1615  
**URL**: https://atcoder.jp/contests/abc065/tasks/arc076_b  
**VJudge Tag**: `[problem:AtCoder-arc076_b]`  
**Category File**: [`../categories/graph_theory/mst_2d_points_adjacent_coordinate_edges.md`](../categories/graph_theory/mst_2d_points_adjacent_coordinate_edges.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Minimum Spanning Tree`  
- **Topic (Skill)**: `Minimum Spanning Tree on 2D Points via Adjacent Coordinate Edges`  

---

## 1. Problem Statement & Key Idea
N towns in 2D plane with coordinates (x_i, y_i). Cost to build a road between towns i and j is min(|x_i - x_j|, |y_i - y_j|). Find the minimum cost to connect all towns.

**Key Insight**: The complete graph has N*(N-1)/2 edges, which is too dense for N = 10^5. In any MST under min-coordinate metric, we only need edges between adjacent points when sorted by x-coordinate, and adjacent points when sorted by y-coordinate.

## 2. Core Observation & Invariant
For any three points A, B, C with x_A <= x_B <= x_C, the edge (A, C) has cost x_C - x_A = (x_B - x_A) + (x_C - x_B) >= max(cost(A, B), cost(B, C)). Thus (A, C) is never needed in an MST. Sorting by x gives N - 1 candidate edges, and sorting by y gives N - 1 candidate edges. Run Kruskal on these 2N - 2 edges.

## 3. Step-by-Step Algorithm
1. Store points with IDs.
2. Sort points by x-coordinate: add edges between adjacent points (u, v) with cost x_{i+1} - x_i.
3. Sort points by y-coordinate: add edges between adjacent points (u, v) with cost y_{i+1} - y_i.
4. Total candidate edges = 2N - 2.
5. Run Kruskal's algorithm with DSU to find MST weight.
6. Print total MST weight.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
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

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Pruning dense geometric graph edges down to adjacent 1D projected edges for MST computation.
- **Reusable Pattern**: `Manhattan Min-Coordinate MST: sort by X and sort by Y, take adjacent edges, run Kruskal.`
