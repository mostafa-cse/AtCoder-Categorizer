# Problem Analysis: AtCoder-abc143_e — Travel by Car

**Problem ID**: `AtCoder-abc143_e`  
**Contest**: `abc143`  
**Rating / Difficulty**: 1695  
**URL**: https://atcoder.jp/contests/abc143/tasks/abc143_e  
**VJudge Tag**: `[problem:AtCoder-abc143_e]`  
**Category File**: [`../categories/graph_theory/dual_floyd_warshall_refuel_hops.md`](../categories/graph_theory/dual_floyd_warshall_refuel_hops.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `All-Pairs Shortest Paths`  
- **Topic (Skill)**: `Dual Floyd-Warshall (Distance Reachability then Refuel Count)`  

---

## 1. Problem Statement & Key Idea
An undirected weighted graph with N cities and M roads. A car has fuel tank capacity L. You can refuel to full capacity L at any city for free. Process Q queries (s, t): minimum number of refuels needed to travel from s to t, or -1 if unreachable.

**Key Insight**: Dual Floyd-Warshall! Phase 1: Floyd-Warshall to compute shortest physical distance between all pairs. Two cities can reach each other with a single full tank iff dist[u][v] <= L. Phase 2: Build a new graph where edge weight is 1 if dist[u][v] <= L, and run Floyd-Warshall to find minimum refuel hops.

## 2. Core Observation & Invariant
Any trip between s and t requiring minimum refuels corresponds to the shortest path in the unweighted reachability graph where an edge exists iff dist[u][v] <= L. Total refuels is (shortest_tank_hops - 1).

## 3. Step-by-Step Algorithm
1. Phase 1: Compute shortest physical distances dist[u][v] using Floyd-Warshall.
2. Phase 2: Build tank_dist[u][v] = (dist[u][v] <= L ? 1 : INF).
3. Run Floyd-Warshall on tank_dist.
4. For each query (s, t):
5.   If tank_dist[s][t] >= INF, print -1.
6.   Else print tank_dist[s][t] - 1.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^3 + Q)`
- **Space Complexity**: `O(N^2)`

## 5. Complete C++ Solution
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

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Hierarchical graph abstraction via dual Floyd-Warshall stages.
- **Reusable Pattern**: `Dual Floyd-Warshall: Phase 1 computes physical reachability; Phase 2 computes hop counts.`
