# Problem Analysis: AtCoder-abc180_e — Traveling Salesman among Aerial Cities

**Problem ID**: `AtCoder-abc180_e`  
**Contest**: `abc180`  
**Rating / Difficulty**: 1256  
**URL**: https://atcoder.jp/contests/abc180/tasks/abc180_e  
**VJudge Tag**: `[problem:AtCoder-abc180_e]`  
**Category File**: [`../categories/dp/tsp_bitmask_asymmetric_metric.md`](../categories/dp/tsp_bitmask_asymmetric_metric.md)  

- **Tag (Domain)**: `Dynamic Programming`  
- **Subtopic**: `Bitmask DP`  
- **Topic (Skill)**: `TSP Bitmask DP with Asymmetric Metric`  

---

## 1. Problem Statement & Key Idea
N 3D cities with coordinates (X_i, Y_i, Z_i). Moving from city p to q costs |X_p - X_q| + |Y_p - Y_q| + max(0, Z_q - Z_p). Find minimum cost to start at city 1, visit all cities, and return to city 1 (N <= 17).

**Key Idea**: This is the classical Traveling Salesperson Problem (TSP) on N <= 17 vertices with an asymmetric cost matrix.

## 2. Core Observation & Invariant
Define dp[mask][u] = minimum cost to visit the subset of vertices indicated by bitmask ending at vertex u. State space is 2^N * N. Transitions: for each unvisited vertex v: dp[mask | (1 << v)][v] = min(dp[mask | (1 << v)][v], dp[mask][u] + cost(u, v)). Return to 1 adds cost(u, 0).

## 3. Step-by-Step Algorithm
1. Precompute cost(u, v) = abs(X_u - X_v) + abs(Y_u - Y_v) + max(0LL, Z_v - Z_u).
2. Initialize dp[1 << N][N] to INF; dp[1][0] = 0.
3. Iterate mask from 1 to (1 << N) - 1: for each u in mask: if dp[mask][u] == INF continue; for v not in mask: dp[mask | (1 << v)][v] = min(dp[mask | (1 << v)][v], dp[mask][u] + cost(u, v)).
4. Compute ans = min_{u} (dp[(1 << N) - 1][u] + cost(u, 0)).
5. Output ans.

## 4. Complexity Analysis
- **Time Complexity**: `O(2^N * N^2)`
- **Space Complexity**: `O(2^N * N)`

## 5. Complete C++ Solution
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

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Bitmask exponential dynamic programming on asymmetric metric graphs.
- **Reusable Pattern**: `TSP Bitmask DP: dp[mask | (1 << v)][v] = min(..., dp[mask][u] + cost(u, v)).`
