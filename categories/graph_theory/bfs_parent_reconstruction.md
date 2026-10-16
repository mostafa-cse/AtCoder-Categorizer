# Shortest Path Tree / BFS Parent Reconstruction

**Domain**: `Graph Theory`  
**Subtopic**: `Shortest Paths`  

This workbook contains curated, high-quality competitive programming problems teaching **Shortest Path Tree / BFS Parent Reconstruction**.

---

## Curated Problems

### [problem:AtCoder-abc168_d] — .. (Double Dots)
- **Contest**: `abc168`
- **Rating / Difficulty**: 804
- **Specific Skill**: Shortest Path Tree / BFS Parent Reconstruction
- **Individual Analysis**: [`../../analysis/AtCoder-abc168_d.md`](../../analysis/AtCoder-abc168_d.md)
- **Problem Statement Summary**: Given a connected unweighted graph with N vertices and M edges. Place a signpost at each vertex i (i >= 2) pointing to an adjacent vertex such that following the signposts reaches vertex 1 in the minimum number of steps.
- **Core Insight**: Since all edge weights are 1, the first time vertex v is reached from vertex u during BFS guarantees that dist[v] = dist[u] + 1 is minimal. Directing an arrow from v to u ensures optimal descent to root 1.
- **Complexity**: Time: `O(N + M)` | Space: `O(N + M)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

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

    vector<int> dist(n + 1, -1);
    vector<int> parent(n + 1, 0);
    queue<int> q;

    dist[1] = 0;
    q.push(1);

    while (!q.empty()) {
        int u = q.front();
        q.pop();

        for (int v : adj[u]) {
            if (dist[v] == -1) {
                dist[v] = dist[u] + 1;
                parent[v] = u;
                q.push(v);
            }
        }
    }

    cout << "Yes\n";
    for (int i = 2; i <= n; ++i) {
        cout << parent[i] << "\n";
    }

    return 0;
}
```
