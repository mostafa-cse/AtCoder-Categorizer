# Continuous Euclidean Distance on Circular Barriers via Dense Dijkstra

**Domain**: `Graph Theory`  
**Subtopic**: `Shortest Paths`  

This workbook contains curated, high-quality competitive programming problems teaching **Continuous Euclidean Distance on Circular Barriers via Dense Dijkstra**.

---

## Curated Problems

### `[problem:AtCoder-arc064_c]` — Cosmic Rays
- **Rating / Difficulty**: 1769
- **Contest**: `arc064`
- **Analysis**: [`analysis/AtCoder-arc064_c.md`](../../analysis/AtCoder-arc064_c.md)
- **Key Idea**: The shortest path consists of straight lines between circles. The distance between two circles with centers (x_1, y_1), (x_2, y_2) and radii r_1, r_2 is max(0.0, hypot(x_1 - x_2, y_1 - y_2) - r_1 - r_2). Build a dense graph with N + 2 vertices and run Dijkstra in O(V^2).
- **Time Complexity**: `O(N^2)`
- **Space Complexity**: `O(N^2)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <cmath>
#include <iomanip>

using namespace std;

struct Circle {
    double x, y, r;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    double xs, ys, xt, yt;
    if (!(cin >> xs >> ys >> xt >> yt)) return 0;

    int n;
    cin >> n;

    vector<Circle> pts;
    pts.push_back({xs, ys, 0});
    for (int i = 0; i < n; ++i) {
        double x, y, r;
        cin >> x >> y >> r;
        pts.push_back({x, y, r});
    }
    pts.push_back({xt, yt, 0});

    int total_nodes = n + 2;
    vector<vector<double>> adj(total_nodes, vector<double>(total_nodes));

    for (int i = 0; i < total_nodes; ++i) {
        for (int j = i; j < total_nodes; ++j) {
            double d = hypot(pts[i].x - pts[j].x, pts[i].y - pts[j].y);
            double w = max(0.0, d - pts[i].r - pts[j].r);
            adj[i][j] = adj[j][i] = w;
        }
    }

    vector<double> min_dist(total_nodes, 1e18);
    vector<bool> visited(total_nodes, false);
    min_dist[0] = 0;

    for (int iter = 0; iter < total_nodes; ++iter) {
        int u = -1;
        double best = 1e18;
        for (int i = 0; i < total_nodes; ++i) {
            if (!visited[i] && min_dist[i] < best) {
                best = min_dist[i];
                u = i;
            }
        }

        if (u == -1) break;
        visited[u] = true;

        for (int v = 0; v < total_nodes; ++v) {
            if (!visited[v] && min_dist[u] + adj[u][v] < min_dist[v]) {
                min_dist[v] = min_dist[u] + adj[u][v];
            }
        }
    }

    cout << fixed << setprecision(10) << min_dist[total_nodes - 1] << "\n";
    return 0;
}
```
