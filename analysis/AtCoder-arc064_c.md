# Problem Analysis: AtCoder-arc064_c — Cosmic Rays

**Problem ID**: `AtCoder-arc064_c`  
**Contest**: `arc064`  
**Rating / Difficulty**: 1769  
**URL**: https://atcoder.jp/contests/arc064/tasks/arc064_c  
**VJudge Tag**: `[problem:AtCoder-arc064_c]`  
**Category File**: [`../categories/graph_theory/euclidean_barrier_dense_dijkstra.md`](../categories/graph_theory/euclidean_barrier_dense_dijkstra.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Shortest Paths`  
- **Topic (Skill)**: `Continuous Euclidean Distance on Circular Barriers via Dense Dijkstra`  

---

## 1. Problem Statement & Key Idea
Given a start point (x_s, y_s), a destination (x_t, y_t), and N circular barriers with center (x_i, y_i) and radius r_i. Inside a barrier, exposure to cosmic rays is 0. Find the minimum Euclidean distance traveled outside barriers.

**Key Insight**: The shortest path consists of straight lines between circles. The distance between two circles with centers (x_1, y_1), (x_2, y_2) and radii r_1, r_2 is max(0.0, hypot(x_1 - x_2, y_1 - y_2) - r_1 - r_2). Build a dense graph with N + 2 vertices and run Dijkstra in O(V^2).

## 2. Core Observation & Invariant
Since N <= 1000, an O(N^2) dense Dijkstra implementation without priority queue is optimal and runs in under 100 ms.

## 3. Step-by-Step Algorithm
1. Create vertices 0 to N + 1 where 0 is Start, N + 1 is End, and 1..N are circles.
2. Compute distance matrix dist[i][j] = max(0.0, dist(c_i, c_j) - r_i - r_j).
3. Run O(V^2) dense Dijkstra: at each step find unvisited node with minimum distance, mark visited, and relax neighbors.
4. Print min distance to End with 10 decimal digits of precision.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2)`
- **Space Complexity**: `O(N^2)`

## 5. Complete C++ Solution
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

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Modeling continuous geometric barrier traversal as discrete dense graph shortest path.
- **Reusable Pattern**: `Circular Barrier Shortest Path: Edge weight = max(0.0, center_dist - r1 - r2) + O(V^2) Dijkstra.`
