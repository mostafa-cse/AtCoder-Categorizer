# Problem Analysis: AtCoder-abc204_e — Rush Hour 2

**Problem ID**: `AtCoder-abc204_e`  
**Contest**: `abc204`  
**Rating / Difficulty**: 1710  
**URL**: https://atcoder.jp/contests/abc204/tasks/abc204_e  
**VJudge Tag**: `[problem:AtCoder-abc204_e]`  
**Category File**: [`../categories/graph_theory/dijkstra_convex_delay_derivative.md`](../categories/graph_theory/dijkstra_convex_delay_derivative.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Shortest Paths`  
- **Topic (Skill)**: `Dijkstra with Convex Time-Dependent Delay / Derivative Optimization`  

---

## 1. Problem Statement & Key Idea
Given a directed graph with N vertices and M edges. Traversing edge i starting at time t >= 0 takes C_i + floor(D_i / (t + 1)) time. Find the minimum time to travel from vertex 1 to vertex N.

**Key Insight**: Standard Dijkstra where arrival time via edge (u, v) is t' + C_i + floor(D_i / (t' + 1)) for some wait time t' >= dist[u]. The function f(t') = t' + D_i / (t' + 1) is convex with continuous minimum near t' + 1 approx sqrt(D_i).

## 2. Core Observation & Invariant
Optimal departure time t' is either dist[u] (if dist[u] >= sqrt(D_i) - 1) or one of the integers immediately adjacent to round(sqrt(D_i)) - 1.

## 3. Step-by-Step Algorithm
1. Initialize dist array with INF, dist[1] = 0.
2. Use min-priority queue (dist, u).
3. When relaxing edge (u, v, C, D):
4.   best_t = dist[u].
5.   target_t = max((long long)dist[u], (long long)round(sqrt(D)) - 1);
6.   Check candidate t' in {dist[u], target_t - 1, target_t, target_t + 1} where t' >= dist[u].
7.   Find min arrival time t' + C + D / (t' + 1).
8.   If arrival time < dist[v], update dist[v] and push to PQ.
9. Print dist[N] if finite, else -1.

## 4. Complexity Analysis
- **Time Complexity**: `O(M log N)`
- **Space Complexity**: `O(N + M)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <cmath>
#include <algorithm>

using namespace std;

const long long INF = 1e18;

struct Edge {
    int to;
    long long c, d;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<Edge>> adj(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v;
        long long c, d;
        cin >> u >> v >> c >> d;
        adj[u].push_back({v, c, d});
        adj[v].push_back({u, c, d});
    }

    vector<long long> dist(n + 1, INF);
    priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> pq;

    dist[1] = 0;
    pq.push({0, 1});

    while (!pq.empty()) {
        auto [d_cur, u] = pq.top();
        pq.pop();

        if (d_cur > dist[u]) continue;

        for (auto& edge : adj[u]) {
            long long best_arrival = INF;
            long long t_opt = (long long)round(sqrt(edge.d)) - 1;
            
            vector<long long> candidates = {dist[u], t_opt - 1, t_opt, t_opt + 1};
            for (long long t : candidates) {
                if (t >= dist[u]) {
                    long long arr = t + edge.c + edge.d / (t + 1);
                    best_arrival = min(best_arrival, arr);
                }
            }

            if (best_arrival < dist[edge.to]) {
                dist[edge.to] = best_arrival;
                pq.push({best_arrival, edge.to});
            }
        }
    }

    cout << (dist[n] == INF ? -1 : dist[n]) << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Optimizing convex time-delay functions at graph transitions within Dijkstra's algorithm.
- **Reusable Pattern**: `Dijkstra with Wait Time: Check sqrt(D) critical points clamped to dist[u].`
