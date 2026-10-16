# Problem Analysis: AtCoder-arc035_c — Traffic Conditions in AtCoder Kingdom

**Problem ID**: `AtCoder-arc035_c`  
**Contest**: `arc035`  
**Rating / Difficulty**: 1655  
**URL**: https://atcoder.jp/contests/arc035/tasks/arc035_c  
**VJudge Tag**: `[problem:AtCoder-arc035_c]`  
**Category File**: [`../categories/graph_theory/online_apsp_incremental_edge_update.md`](../categories/graph_theory/online_apsp_incremental_edge_update.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `All-Pairs Shortest Paths`  
- **Topic (Skill)**: `Online All-Pairs Shortest Path Incremental Edge Addition`  

---

## 1. Problem Statement & Key Idea
An undirected weighted graph with N vertices. Initially all-pairs shortest paths are given. Process K queries: a new road between X and Y with length Z is built. After each road addition, output the sum of shortest path distances between all pairs i < j.

**Key Insight**: When a new edge (X, Y, Z) is added, the new shortest path between any pair (i, j) can only change by routing through (X, Y): dist'[i][j] = min({dist[i][j], dist[i][X] + Z + dist[Y][j], dist[i][Y] + Z + dist[X][j]}).

## 2. Core Observation & Invariant
Updating all pairs takes O(N^2) per added road. For K <= 400 and N <= 400, total time is O(K * N^2) ~ 6.4 * 10^7 operations, well within time limit.

## 3. Step-by-Step Algorithm
1. Compute initial all-pairs shortest paths using Floyd-Warshall in O(N^3).
2. Calculate initial total sum of distances for all i < j.
3. For each new road (X, Y, Z):
4.   If Z >= dist[X][Y], edge is redundant; print current sum.
5.   Otherwise:
6.     For i from 1 to N:
7.       For j from i + 1 to N:
8.         new_dist = min({dist[i][j], dist[i][X] + Z + dist[Y][j], dist[i][Y] + Z + dist[X][j]});
9.         sum -= (dist[i][j] - new_dist);
10.         dist[i][j] = dist[j][i] = new_dist;
11.     Print updated sum.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^3 + K * N^2)`
- **Space Complexity**: `O(N^2)`

## 5. Complete C++ Solution
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

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Incremental dynamic Floyd-Warshall update in O(N^2) per edge insertion.
- **Reusable Pattern**: `Dynamic Edge Addition APSP: dist[i][j] = min(dist[i][j], dist[i][u] + w + dist[v][j]).`
