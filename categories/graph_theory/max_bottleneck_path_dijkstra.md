# Maximum Bottleneck Path via Modified Dijkstra / Min-Vertex Path Capacity

**Domain**: `Graph Theory`  
**Subtopic**: `Shortest Paths`  

This workbook contains curated, high-quality competitive programming problems teaching **Maximum Bottleneck Path via Modified Dijkstra / Min-Vertex Path Capacity**.

---

## Curated Problems

### `[problem:AtCoder-arc056_b]` — 駐車場
- **Rating / Difficulty**: 1726
- **Contest**: `arc056`
- **Analysis**: [`analysis/AtCoder-arc056_b.md`](../../analysis/AtCoder-arc056_b.md)
- **Key Idea**: The bottleneck capacity of a path is min_{v in path} v. Car i can reach i iff the maximum bottleneck path from S to i has capacity >= i. Compute max bottleneck path from S to all vertices using modified Dijkstra.
- **Time Complexity**: `O((N + M) log N)`
- **Space Complexity**: `O(N + M)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, s;
    if (!(cin >> n >> m >> s)) return 0;

    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    vector<int> cap(n + 1, 0);
    priority_queue<pair<int, int>> pq;

    cap[s] = s;
    pq.push({s, s});

    while (!pq.empty()) {
        auto [c, u] = pq.top();
        pq.pop();

        if (c < cap[u]) continue;

        for (int v : adj[u]) {
            int next_c = min(c, v);
            if (next_c > cap[v]) {
                cap[v] = next_c;
                pq.push({next_c, v});
            }
        }
    }

    for (int i = 1; i <= n; ++i) {
        if (cap[i] >= i) {
            cout << i << "\n";
        }
    }

    return 0;
}
```
