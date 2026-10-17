# Problem Analysis: AtCoder-abc181_f — Silver Woods

**Problem ID**: `AtCoder-abc181_f`  
**Contest**: `abc181`  
**Rating / Difficulty**: 2009  
**URL**: https://atcoder.jp/contests/abc181/tasks/abc181_f  
**VJudge Tag**: `[problem:AtCoder-abc181_f]`  
**Category File**: [`../categories/graph_theory/dsu_geometric_bottleneck_circle_clearance.md`](../categories/graph_theory/dsu_geometric_bottleneck_circle_clearance.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Connected Components`  
- **Topic (Skill)**: `DSU Geometric Bottleneck Percolation for Maximum Clearance Circle Passage`  

---

## 1. Problem Statement & Key Idea
In a 2D strip between y = -100 and y = 100 with N point obstacles, find the maximum radius r of a circle that can move from x = -infinity to x = +infinity without touching any obstacle or boundary.

**Key Idea**: A circle of radius r can pass through iff no connected component of obstacles blocks the channel from y = 100 to y = -100. The clearance between two obstacles i, j requires distance >= 2r. The clearance to the top boundary requires 100 - y_i >= 2r, and to the bottom requires y_i - (-100) >= 2r. The passage is blocked iff the top boundary and bottom boundary belong to the same connected component of edges with distance < 2r. Binary search on r with DSU connectivity check solves the problem.

## 2. Core Observation & Invariant
2D continuous passage clearance is dual to percolation connectivity between opposing boundaries in the proximity graph.

## 3. Step-by-Step Algorithm
1. Binary search on r in [0, 100] with 80 iterations for high precision.
2. For a fixed r:
3.   Initialize DSU with N + 2 vertices (0 to N - 1 for obstacles, N for top, N + 1 for bottom).
4.   For each obstacle i:
5.     If 100 - y_i < 2 * r: unite(i, top).
6.     If y_i - (-100) < 2 * r: unite(i, bottom).
7.   For every pair of obstacles i < j:
8.     If Euclidean distance(i, j) < 2 * r: unite(i, j).
9.   If top and bottom are connected: r is too large; else r is feasible.
10. Print final r with high precision.

## 4. Complexity Analysis
- **Time Complexity**: `O(iters * N^2 * alpha(N))`
- **Space Complexity**: `O(N)`

## 5. Core Algorithmic Skill & Learning Takeaway
Continuous geometric clearance dualization to graph boundary percolation.

**Reusable Pattern**: Channel Clearance Percolation: Connect boundaries and obstacles when distance < 2r; valid passage iff top and bottom remain disconnected.

## 6. Comparison with Alternative Approaches
Matches official editorial.

## 7. Verified Clean C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <cmath>
#include <numeric>
#include <iomanip>

using namespace std;

struct DSU {
    vector<int> parent;
    DSU(int n) : parent(n) {
        iota(parent.begin(), parent.end(), 0);
    }
    int find(int i) {
        if (parent[i] == i) return i;
        return parent[i] = find(parent[i]);
    }
    void unite(int i, int j) {
        int root_i = find(i);
        int root_j = find(j);
        if (root_i != root_j) parent[root_i] = root_j;
    }
    bool same(int i, int j) {
        return find(i) == find(j);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<pair<double, double>> pts(n);
    for (int i = 0; i < n; ++i) {
        cin >> pts[i].first >> pts[i].second;
    }

    int top_node = n, bot_node = n + 1;

    auto check = [&](double r) {
        DSU dsu(n + 2);
        double d2 = 2.0 * r;

        for (int i = 0; i < n; ++i) {
            if (100.0 - pts[i].second < d2) {
                dsu.unite(i, top_node);
            }
            if (pts[i].second - (-100.0) < d2) {
                dsu.unite(i, bot_node);
            }
        }

        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                double dist = hypot(pts[i].first - pts[j].first, pts[i].second - pts[j].second);
                if (dist < d2) {
                    dsu.unite(i, j);
                }
            }
        }

        return !dsu.same(top_node, bot_node);
    };

    double low = 0.0, high = 100.0;
    for (int iter = 0; iter < 80; ++iter) {
        double mid = (low + high) / 2.0;
        if (check(mid)) {
            low = mid;
        } else {
            high = mid;
        }
    }

    cout << fixed << setprecision(10) << low << "\n";
    return 0;
}
```
