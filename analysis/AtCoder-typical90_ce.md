# Problem Analysis: AtCoder-typical90_ce — Colorful Graph

**Problem ID**: `AtCoder-typical90_ce`  
**Contest**: `typical90` (Kyopro Typical 90, Problem 083)  
**Rating / Difficulty**: 2300 (★6)  
**URL**: https://atcoder.jp/contests/typical90/tasks/typical90_ce  
**VJudge Tag**: `[problem:AtCoder-typical90_ce]`  
**Category File**: [`../categories/data_structures/sqrt_decomposition_graph.md`](../categories/data_structures/sqrt_decomposition_graph.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Square Root Decomposition`  
- **Topic (Skill)**: `Square Root Decomposition on Graph Vertex Degrees (Heavy-Light)`  

---

## 1. Problem Statement & Key Idea
Graph with N, M <= 2*10^5. Q <= 2*10^5 queries: given (x, y), print color of vertex x, then color x and all its neighbors with color y.

**Core Idea**: Square Root Decomposition on vertex degrees: partition vertices into Light (degree < B) and Heavy (degree >= B) where B = sqrt(M).

## 2. Core Observation & Invariant
There are at most 2M / B <= 2 * sqrt(M) heavy vertices. Light vertices query all neighbors in O(B). Heavy vertices push updates to light neighbors or keep a timestamp tag checked by adjacent heavy nodes.

## 3. Step-by-Step Algorithm
1. Threshold B = sqrt(2 * M).
2. Vertices with deg >= B are Heavy.
3. For each vertex: keep list of adjacent heavy vertices.
4. Query (x, y): determine color of x by checking x's own color vs latest timestamp among heavy neighbors. Color x and update x.

## 4. Complexity Analysis
Time: O((N + M + Q) * sqrt(M)), Space: O(N + M).

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

const int MAXN = 200005;

struct Update {
    int color, time;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    int B = max(1, (int)sqrt(2 * m));
    vector<bool> is_heavy(n + 1, false);
    for (int i = 1; i <= n; ++i) {
        if ((int)adj[i].size() >= B) is_heavy[i] = true;
    }

    vector<vector<int>> heavy_adj(n + 1);
    for (int u = 1; u <= n; ++u) {
        for (int v : adj[u]) {
            if (is_heavy[v]) heavy_adj[u].push_back(v);
        }
    }

    vector<int> col(n + 1, 1);
    vector<int> last_update(n + 1, 0);
    vector<Update> heavy_tag(n + 1, {1, 0});

    int q;
    cin >> q;
    for (int t = 1; t <= q; ++t) {
        int x, y;
        cin >> x >> y;

        int cur_color = col[x];
        int best_time = last_update[x];

        // Check heavy neighbors
        for (int h : heavy_adj[x]) {
            if (heavy_tag[h].time > best_time) {
                best_time = heavy_tag[h].time;
                cur_color = heavy_tag[h].color;
            }
        }

        cout << cur_color << "\n";

        // Update x and neighbors
        if (is_heavy[x]) {
            heavy_tag[x] = {y, t};
        } else {
            col[x] = y;
            last_update[x] = t;
            for (int v : adj[x]) {
                col[v] = y;
                last_update[v] = t;
            }
        }
    }
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Square root decomposition on vertex degrees partitioning into heavy and light hubs.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Sqrt decomposition on graphs, heavy-light degree balancing, and lazy timestamped propagation.
- **Reusable Pattern**: `Heavy-Light Vertex Degree Sqrt Decomposition.`

---
Back to [Square Root Decomposition on Graph Vertex Degrees (Heavy-Light)](../categories/data_structures/sqrt_decomposition_graph.md) | [Categories Directory](../categories/README.md)