# Floyd-Warshall Intermediate Vertex State Accumulation

**Domain**: `Graph Theory`  
**Subtopic**: `All-Pairs Shortest Paths`  

This workbook contains curated, high-quality competitive programming problems teaching **Floyd-Warshall Intermediate Vertex State Accumulation**.

---

## Curated Problems

### [problem:AtCoder-abc208_d] — Shortest Path Queries 2
- **Contest**: `abc208`
- **Rating / Difficulty**: 1190
- **Specific Skill**: Floyd-Warshall Intermediate Vertex State Accumulation
- **Individual Analysis**: [`../../analysis/AtCoder-abc208_d.md`](../../analysis/AtCoder-abc208_d.md)
- **Problem Statement Summary**: Directed weighted graph with N vertices. Let f(s, t, k) be the shortest path from s to t using only intermediate vertices in {1..k}. Compute sum_{k=1}^N sum_{s=1}^N sum_{t=1}^N f(s, t, k).
- **Core Insight**: Execute the standard 3 nested loops of Floyd-Warshall with outer variable k. Immediately after relaxing all pairs (s, t) through intermediate vertex k, add all finite distances dist[s][t] to the total answer. This solves the problem directly in O(N^3).
- **Complexity**: Time: `O(N^3)` | Space: `O(N^2)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const long long INF = 1e15;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<long long>> dist(n + 1, vector<long long>(n + 1, INF));
    for (int i = 1; i <= n; ++i) dist[i][i] = 0;

    for (int i = 0; i < m; ++i) {
        int u, v;
        long long c;
        cin >> u >> v >> c;
        dist[u][v] = min(dist[u][v], c);
    }

    long long ans = 0;

    for (int k = 1; k <= n; ++k) {
        for (int s = 1; s <= n; ++s) {
            for (int t = 1; t <= n; ++t) {
                dist[s][t] = min(dist[s][t], dist[s][k] + dist[k][t]);
                if (dist[s][t] < INF) {
                    ans += dist[s][t];
                }
            }
        }
    }

    cout << ans << "\n";
    return 0;
}
```
