# Greedy Edge Coloring of Trees via Maximum Degree Bound

**Domain**: `Graph Theory`  
**Subtopic**: `Tree Coloring`  

This workbook contains curated, high-quality competitive programming problems teaching **Greedy Edge Coloring of Trees via Maximum Degree Bound**.

---

## Curated Problems

### [problem:AtCoder-abc146_d] — Coloring Edges on Tree
- **Contest**: `abc146`
- **Rating / Difficulty**: 1192
- **Specific Skill**: Greedy Edge Coloring of Trees via Maximum Degree Bound
- **Individual Analysis**: [`../../analysis/AtCoder-abc146_d.md`](../../analysis/AtCoder-abc146_d.md)
- **Problem Statement Summary**: Given a tree with N vertices. Color each edge such that any two edges sharing a vertex have different colors. Minimize the number of colors used (N <= 10^5).
- **Core Insight**: Run BFS or DFS from root 1. When visiting vertex u with incoming edge color c_parent: iterate through all children v, assigning colors 1, 2, 3... skipping c_parent. Because children incident edges are assigned distinct colors != c_parent, all adjacent edge pairs have different colors using exactly Delta colors.
- **Complexity**: Time: `O(N)` | Space: `O(N)`
- **Verified C++ Implementation**:
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
