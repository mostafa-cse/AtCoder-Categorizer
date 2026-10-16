# Tree Multi-Source BFS Voronoi Territory Partition

**Domain**: `Graph Theory`  
**Subtopic**: `Trees`  

This workbook contains curated, high-quality competitive programming problems teaching **Tree Multi-Source BFS Voronoi Territory Partition**.

---

## Curated Problems

### `[problem:AtCoder-arc078_b]` — Fennec VS. Snuke
- **Rating / Difficulty**: 1431
- **Contest**: `abc067`
- **Analysis**: [`analysis/AtCoder-arc078_b.md`](../../analysis/AtCoder-arc078_b.md)
- **Key Idea**: In a tree, the game decomposes into a Voronoi diagram on tree distances: Fennec captures vertex v if dist(1, v) <= dist(N, v); otherwise Snuke captures v.
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

void bfs(int start, const vector<vector<int>>& adj, vector<int>& dist) {
    dist[start] = 0;
    queue<int> q;
    q.push(start);
    while (!q.empty()) {
        int u = q.front();
        q.pop();
        for (int v : adj[u]) {
            if (dist[v] == -1) {
                dist[v] = dist[u] + 1;
                q.push(v);
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    vector<int> dist1(n + 1, -1), distN(n + 1, -1);
    bfs(1, adj, dist1);
    bfs(n, adj, distN);

    int fennec = 0, snuke = 0;
    for (int i = 1; i <= n; ++i) {
        if (dist1[i] <= distN[i]) {
            fennec++;
        } else {
            snuke++;
        }
    }

    cout << (fennec > snuke ? "Fennec" : "Snuke") << "\n";
    return 0;
}
```
