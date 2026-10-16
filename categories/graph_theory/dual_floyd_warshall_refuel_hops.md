# Dual Floyd-Warshall (Distance Reachability then Refuel Count)

**Domain**: `Graph Theory`  
**Subtopic**: `All-Pairs Shortest Paths`  

This workbook contains curated, high-quality competitive programming problems teaching **Dual Floyd-Warshall (Distance Reachability then Refuel Count)**.

---

## Curated Problems

### `[problem:AtCoder-abc143_e]` — Travel by Car
- **Rating / Difficulty**: 1695
- **Contest**: `abc143`
- **Analysis**: [`analysis/AtCoder-abc143_e.md`](../../analysis/AtCoder-abc143_e.md)
- **Key Idea**: Dual Floyd-Warshall! Phase 1: Floyd-Warshall to compute shortest physical distance between all pairs. Two cities can reach each other with a single full tank iff dist[u][v] <= L. Phase 2: Build a new graph where edge weight is 1 if dist[u][v] <= L, and run Floyd-Warshall to find minimum refuel hops.
- **Time Complexity**: `O(N^3 + Q)`
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
    long long L;
    if (!(cin >> n >> m >> L)) return 0;

    vector<vector<long long>> dist(n + 1, vector<long long>(n + 1, INF));
    for (int i = 1; i <= n; ++i) dist[i][i] = 0;

    for (int i = 0; i < m; ++i) {
        int u, v;
        long long w;
        cin >> u >> v >> w;
        dist[u][v] = min(dist[u][v], w);
        dist[v][u] = min(dist[v][u], w);
    }

    // Phase 1: Physical distances
    for (int k = 1; k <= n; ++k) {
        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= n; ++j) {
                if (dist[i][k] + dist[k][j] < dist[i][j]) {
                    dist[i][j] = dist[i][k] + dist[k][j];
                }
            }
        }
    }

    // Phase 2: Refuel hops
    vector<vector<long long>> hops(n + 1, vector<long long>(n + 1, INF));
    for (int i = 1; i <= n; ++i) {
        hops[i][i] = 0;
        for (int j = i + 1; j <= n; ++j) {
            if (dist[i][j] <= L) {
                hops[i][j] = hops[j][i] = 1;
            }
        }
    }

    for (int k = 1; k <= n; ++k) {
        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= n; ++j) {
                if (hops[i][k] + hops[k][j] < hops[i][j]) {
                    hops[i][j] = hops[i][k] + hops[k][j];
                }
            }
        }
    }

    int q;
    cin >> q;
    while (q--) {
        int s, t;
        cin >> s >> t;
        if (hops[s][t] >= INF) {
            cout << -1 << "\n";
        } else {
            cout << hops[s][t] - 1 << "\n";
        }
    }

    return 0;
}
```
