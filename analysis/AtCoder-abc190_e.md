# Problem Analysis: AtCoder-abc190_e — Magical Ornament

**Problem ID**: `AtCoder-abc190_e`  
**Contest**: `abc190`  
**Rating / Difficulty**: 1645  
**URL**: https://atcoder.jp/contests/abc190/tasks/abc190_e  
**VJudge Tag**: `[problem:AtCoder-abc190_e]`  
**Category File**: [`../categories/graph_theory/multisource_bfs_tsp_bitmask_dp.md`](../categories/graph_theory/multisource_bfs_tsp_bitmask_dp.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Traveling Salesperson Problem`  
- **Topic (Skill)**: `Multi-Source BFS on K Targets + TSP Bitmask DP`  

---

## 1. Problem Statement & Key Idea
An undirected graph with N vertices and M edges. Find the shortest path (in terms of number of vertices) that visits a given subset of K vertices C_1, ..., C_K in any order. K <= 17.

**Key Insight**: Compute all-pairs shortest paths between the K targets using K runs of BFS. Then solve the Traveling Salesperson Problem (TSP) on the complete graph of K targets using bitmask DP.

## 2. Core Observation & Invariant
Any shortest path visiting all K targets moves between targets along shortest paths in the original graph. K <= 17 means 2^17 * 17 ~ 2.2 * 10^6 states, running well within 1.0s.

## 3. Step-by-Step Algorithm
1. Run BFS from each target C_i to compute dist[i][j] (distance to target C_j).
2. If any two targets are in different components, output -1.
3. Initialize dp[1 << K][K] with INF.
4. Base case: dp[1 << i][i] = 1 for all i = 0..K-1.
5. For mask from 1 to (1 << K) - 1:
6.   For u = 0 to K - 1:
7.     if (!(mask & (1 << u))) continue;
8.     For v = 0 to K - 1:
9.       if (mask & (1 << v)) continue;
10.       dp[mask | (1 << v)][v] = min(dp[mask | (1 << v)][v], dp[mask][u] + dist[u][v]);
11. Output min_{u=0..K-1} dp[(1 << K) - 1][u].

## 4. Complexity Analysis
- **Time Complexity**: `O(K * (N + M) + K^2 * 2^K)`
- **Space Complexity**: `O(K * 2^K + N + M)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

const int INF = 1e9;

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

    int k;
    cin >> k;
    vector<int> c(k);
    for (int i = 0; i < k; ++i) {
        cin >> c[i];
    }

    // Pairwise distance matrix between targets
    vector<vector<int>> dist(k, vector<int>(k, INF));

    for (int i = 0; i < k; ++i) {
        vector<int> d(n + 1, -1);
        queue<int> q;
        d[c[i]] = 0;
        q.push(c[i]);

        while (!q.empty()) {
            int u = q.front();
            q.pop();
            for (int v : adj[u]) {
                if (d[v] == -1) {
                    d[v] = d[u] + 1;
                    q.push(v);
                }
            }
        }

        for (int j = 0; j < k; ++j) {
            if (d[c[j]] != -1) {
                dist[i][j] = d[c[j]];
            }
        }
    }

    // TSP Bitmask DP
    int total_masks = 1 << k;
    vector<vector<int>> dp(total_masks, vector<int>(k, INF));

    for (int i = 0; i < k; ++i) {
        dp[1 << i][i] = 1; // 1 vertex visited
    }

    for (int mask = 1; mask < total_masks; ++mask) {
        for (int u = 0; u < k; ++u) {
            if (dp[mask][u] == INF) continue;

            for (int v = 0; v < k; ++v) {
                if (!(mask & (1 << v))) {
                    if (dist[u][v] < INF) {
                        dp[mask | (1 << v)][v] = min(dp[mask | (1 << v)][v], dp[mask][u] + dist[u][v]);
                    }
                }
            }
        }
    }

    int ans = INF;
    for (int i = 0; i < k; ++i) {
        ans = min(ans, dp[total_masks - 1][i]);
    }

    cout << (ans >= INF ? -1 : ans) << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Dimensionality reduction from large sparse graph to small dense target graph solved by TSP bitmask DP.
- **Reusable Pattern**: `Target Subset Traversal: K runs of BFS to build target distance matrix + O(2^K * K^2) TSP DP.`
