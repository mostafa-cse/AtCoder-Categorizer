# TSP Bitmask DP with Asymmetric Metric

**Domain**: `Dynamic Programming`  
**Subtopic**: `Bitmask DP`  

This workbook contains curated, high-quality competitive programming problems teaching **TSP Bitmask DP with Asymmetric Metric**.

---

## Curated Problems

### [problem:AtCoder-abc180_e] — Traveling Salesman among Aerial Cities
- **Contest**: `abc180`
- **Rating / Difficulty**: 1256
- **Specific Skill**: TSP Bitmask DP with Asymmetric Metric
- **Individual Analysis**: [`../../analysis/AtCoder-abc180_e.md`](../../analysis/AtCoder-abc180_e.md)
- **Problem Statement Summary**: N 3D cities with coordinates (X_i, Y_i, Z_i). Moving from city p to q costs |X_p - X_q| + |Y_p - Y_q| + max(0, Z_q - Z_p). Find minimum cost to start at city 1, visit all cities, and return to city 1 (N <= 17).
- **Core Insight**: Define dp[mask][u] = minimum cost to visit the subset of vertices indicated by bitmask ending at vertex u. State space is 2^N * N. Transitions: for each unvisited vertex v: dp[mask | (1 << v)][v] = min(dp[mask | (1 << v)][v], dp[mask][u] + cost(u, v)). Return to 1 adds cost(u, 0).
- **Complexity**: Time: `O(2^N * N^2)` | Space: `O(2^N * N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

const long long INF = 4e18;

struct City {
    long long x, y, z;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<City> c(n);
    for (int i = 0; i < n; ++i) {
        cin >> c[i].x >> c[i].y >> c[i].z;
    }

    vector<vector<long long>> cost(n, vector<long long>(n));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            cost[i][j] = abs(c[i].x - c[j].x) + abs(c[i].y - c[j].y) + max(0LL, c[j].z - c[i].z);
        }
    }

    int total_masks = 1 << n;
    vector<vector<long long>> dp(total_masks, vector<long long>(n, INF));
    dp[1][0] = 0;

    for (int mask = 1; mask < total_masks; ++mask) {
        for (int u = 0; u < n; ++u) {
            if (dp[mask][u] == INF) continue;

            for (int v = 0; v < n; ++v) {
                if (!((mask >> v) & 1)) {
                    int next_mask = mask | (1 << v);
                    dp[next_mask][v] = min(dp[next_mask][v], dp[mask][u] + cost[u][v]);
                }
            }
        }
    }

    long long ans = INF;
    for (int u = 0; u < n; ++u) {
        ans = min(ans, dp[total_masks - 1][u] + cost[u][0]);
    }

    cout << ans << "\n";
    return 0;
}
```
