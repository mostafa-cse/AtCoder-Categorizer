# Shortest Cycle through Source via All-Pairs Shortest Path

**Domain**: `Graph Theory`  
**Subtopic**: `All-Pairs Shortest Paths`  

This workbook contains curated, high-quality competitive programming problems teaching **Shortest Cycle through Source via All-Pairs Shortest Path**.

---

## Curated Problems

### `[problem:AtCoder-abc022_c]` — Blue Bird
- **Rating / Difficulty**: 1505
- **Contest**: `abc022`
- **Analysis**: [`analysis/AtCoder-abc022_c.md`](../../analysis/AtCoder-abc022_c.md)
- **Key Idea**: A simple cycle passing through vertex 1 consists of 1 -> u -> ... -> v -> 1, where u and v are two distinct neighbors of 1, and the path from u to v does not pass through 1.
- **Time Complexity**: `O(N^3)`
- **Space Complexity**: `O(N^2)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const long long INF = 1e16;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<long long>> dist(n + 1, vector<long long>(n + 1, INF));
    for (int i = 1; i <= n; ++i) dist[i][i] = 0;

    vector<pair<int, long long>> neighbors_1;

    for (int i = 0; i < m; ++i) {
        int u, v;
        long long l;
        cin >> u >> v >> l;
        if (u == 1) {
            neighbors_1.push_back({v, l});
        } else if (v == 1) {
            neighbors_1.push_back({u, l});
        } else {
            dist[u][v] = min(dist[u][v], l);
            dist[v][u] = min(dist[v][u], l);
        }
    }

    // Floyd-Warshall on vertices 2..N
    for (int k = 2; k <= n; ++k) {
        for (int i = 2; i <= n; ++i) {
            for (int j = 2; j <= n; ++j) {
                if (dist[i][k] + dist[k][j] < dist[i][j]) {
                    dist[i][j] = dist[i][k] + dist[k][j];
                }
            }
        }
    }

    long long ans = INF;
    int k = neighbors_1.size();
    for (int i = 0; i < k; ++i) {
        for (int j = i + 1; j < k; ++j) {
            int u = neighbors_1[i].first;
            int v = neighbors_1[j].first;
            long long cycle_cost = neighbors_1[i].second + dist[u][v] + neighbors_1[j].second;
            ans = min(ans, cycle_cost);
        }
    }

    cout << (ans >= INF ? -1 : ans) << "\n";
    return 0;
}
```
