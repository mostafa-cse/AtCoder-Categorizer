# Problem Analysis: AtCoder-abc208_d — Shortest Path Queries 2

**Problem ID**: `AtCoder-abc208_d`  
**Contest**: `abc208`  
**Rating / Difficulty**: 1190  
**URL**: https://atcoder.jp/contests/abc208/tasks/abc208_d  
**VJudge Tag**: `[problem:AtCoder-abc208_d]`  
**Category File**: [`../categories/graph_theory/floyd_warshall_intermediate_accumulation.md`](../categories/graph_theory/floyd_warshall_intermediate_accumulation.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `All-Pairs Shortest Paths`  
- **Topic (Skill)**: `Floyd-Warshall Intermediate Vertex State Accumulation`  

---

## 1. Problem Statement & Key Idea
Directed weighted graph with N vertices. Let f(s, t, k) be the shortest path from s to t using only intermediate vertices in {1..k}. Compute sum_{k=1}^N sum_{s=1}^N sum_{t=1}^N f(s, t, k).

**Key Idea**: The standard Floyd-Warshall DP state dist[s][t] after iteration k is PRECISELY the shortest path between s and t using only intermediate vertices in {1..k}!

## 2. Core Observation & Invariant
Execute the standard 3 nested loops of Floyd-Warshall with outer variable k. Immediately after relaxing all pairs (s, t) through intermediate vertex k, add all finite distances dist[s][t] to the total answer. This solves the problem directly in O(N^3).

## 3. Step-by-Step Algorithm
1. Initialize dist matrix with INF on non-edges, 0 on diagonal, and weights on directed edges.
2. Initialize total = 0.
3. For k = 1 to N:
4.   For s = 1 to N: for t = 1 to N: dist[s][t] = min(dist[s][t], dist[s][k] + dist[k][t]); if dist[s][t] < INF: total += dist[s][t].
5. Print total.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^3)`
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

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Understanding the dynamic programming subproblem invariant of the Floyd-Warshall outer loop.
- **Reusable Pattern**: `Floyd-Warshall prefix vertex queries: accumulate dist[s][t] inside the k-loop.`
