# Problem Analysis: AtCoder-abc146_d — Coloring Edges on Tree

**Problem ID**: `AtCoder-abc146_d`  
**Contest**: `abc146`  
**Rating / Difficulty**: 1192  
**URL**: https://atcoder.jp/contests/abc146/tasks/abc146_d  
**VJudge Tag**: `[problem:AtCoder-abc146_d]`  
**Category File**: [`../categories/graph_theory/greedy_edge_coloring_trees.md`](../categories/graph_theory/greedy_edge_coloring_trees.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Tree Coloring`  
- **Topic (Skill)**: `Greedy Edge Coloring of Trees via Maximum Degree Bound`  

---

## 1. Problem Statement & Key Idea
Given a tree with N vertices. Color each edge such that any two edges sharing a vertex have different colors. Minimize the number of colors used (N <= 10^5).

**Key Idea**: By Vizing's theorem (or basic degree bounds on trees), the minimum number of colors to edge-color a tree equals the maximum degree Delta = max_v deg(v).

## 2. Core Observation & Invariant
Run BFS or DFS from root 1. When visiting vertex u with incoming edge color c_parent: iterate through all children v, assigning colors 1, 2, 3... skipping c_parent. Because children incident edges are assigned distinct colors != c_parent, all adjacent edge pairs have different colors using exactly Delta colors.

## 3. Step-by-Step Algorithm
1. Find maximum degree Delta among all vertices.
2. Run BFS from root 1 tracking (u, parent_edge_color).
3. For each unvisited child v of u: assign next available color != parent_edge_color to edge (u, v).
4. Output Delta, then print the assigned color of each edge in original input order.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

struct Edge {
    int to, id;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<Edge>> adj(n + 1);
    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back({v, i});
        adj[v].push_back({u, i});
    }

    int max_deg = 0;
    for (int i = 1; i <= n; ++i) {
        max_deg = max(max_deg, (int)adj[i].size());
    }

    vector<int> edge_color(n - 1, 0);
    vector<bool> visited(n + 1, false);
    queue<pair<int, int>> q; // {vertex, incoming_color}

    visited[1] = true;
    q.push({1, 0});

    while (!q.empty()) {
        auto [u, parent_color] = q.front();
        q.pop();

        int color = 1;
        for (const auto& e : adj[u]) {
            if (!visited[e.to]) {
                visited[e.to] = true;
                if (color == parent_color) color++;
                edge_color[e.id] = color;
                q.push({e.to, color});
                color++;
            }
        }
    }

    cout << max_deg << "\n";
    for (int i = 0; i < n - 1; ++i) {
        cout << edge_color[i] << "\n";
    }

    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Optimal tree edge coloring in Delta colors via greedy parent-color avoidance.
- **Reusable Pattern**: `Tree edge coloring: assign colors 1..Delta to children edges skipping parent color.`
