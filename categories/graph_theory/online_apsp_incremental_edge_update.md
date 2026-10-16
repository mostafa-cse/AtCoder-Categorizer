# Online All-Pairs Shortest Path Incremental Edge Addition

**Domain**: `Graph Theory`  
**Subtopic**: `All-Pairs Shortest Paths`  

This workbook contains curated, high-quality competitive programming problems teaching **Online All-Pairs Shortest Path Incremental Edge Addition**.

---

## Curated Problems

### `[problem:AtCoder-arc035_c]` — Traffic Conditions in AtCoder Kingdom
- **Rating / Difficulty**: 1655
- **Contest**: `arc035`
- **Analysis**: [`analysis/AtCoder-arc035_c.md`](../../analysis/AtCoder-arc035_c.md)
- **Key Idea**: When a new edge (X, Y, Z) is added, the new shortest path between any pair (i, j) can only change by routing through (X, Y): dist'[i][j] = min({dist[i][j], dist[i][X] + Z + dist[Y][j], dist[i][Y] + Z + dist[X][j]}).
- **Time Complexity**: `O(N^3 + K * N^2)`
- **Space Complexity**: `O(N^2)`
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
        long long w;
        cin >> u >> v >> w;
        dist[u][v] = min(dist[u][v], w);
        dist[v][u] = min(dist[v][u], w);
    }

    for (int k = 1; k <= n; ++k) {
        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= n; ++j) {
                if (dist[i][k] + dist[k][j] < dist[i][j]) {
                    dist[i][j] = dist[i][k] + dist[k][j];
                }
            }
        }
    }

    long long cur_sum = 0;
    for (int i = 1; i <= n; ++i) {
        for (int j = i + 1; j <= n; ++j) {
            cur_sum += dist[i][j];
        }
    }

    int k_roads;
    cin >> k_roads;

    while (k_roads--) {
        int x, y;
        long long z;
        cin >> x >> y >> z;

        if (z < dist[x][y]) {
            for (int i = 1; i <= n; ++i) {
                for (int j = i + 1; j <= n; ++j) {
                    long long alt1 = dist[i][x] + z + dist[y][j];
                    long long alt2 = dist[i][y] + z + dist[x][j];
                    long long new_d = min({dist[i][j], alt1, alt2});
                    if (new_d < dist[i][j]) {
                        cur_sum -= (dist[i][j] - new_d);
                        dist[i][j] = dist[j][i] = new_d;
                    }
                }
            }
        }
        cout << cur_sum << "\n";
    }

    return 0;
}
```
