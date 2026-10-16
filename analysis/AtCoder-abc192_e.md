# Problem Analysis: AtCoder-abc192_e — Train

**Problem ID**: `AtCoder-abc192_e`  
**Contest**: `abc192`  
**Rating / Difficulty**: 1135  
**URL**: https://atcoder.jp/contests/abc192/tasks/abc192_e  
**VJudge Tag**: `[problem:AtCoder-abc192_e]`  
**Category File**: [`../categories/graph_theory/periodic_schedule_dijkstra.md`](../categories/graph_theory/periodic_schedule_dijkstra.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Dijkstra`  
- **Topic (Skill)**: `Periodic Departure Schedule Dijkstra`  

---

## 1. Problem Statement & Key Idea
A rail network has N cities and M train lines. Train line i connects A_i and B_i taking T_i time, but only departs at times that are multiples of K_i (0, K_i, 2*K_i...). Find the earliest time to travel from X to Y.

**Key Idea**: This is single-source shortest paths on a time-dependent graph, solved via Dijkstra's algorithm.

## 2. Core Observation & Invariant
If you arrive at city u at time cur_time, the earliest departure for line i with interval K is dep_time = ((cur_time + K - 1) / K) * K. The arrival at city v is dep_time + T. Because departure time is non-decreasing with arrival time, the greedy property of Dijkstra holds.

## 3. Step-by-Step Algorithm
1. Use priority_queue storing (current_time, vertex) with min-heap.
2. Initialize dist array to INF, dist[X] = 0.
3. While queue is not empty: pop (d, u); if d > dist[u] continue.
4. For each train (v, T, K) from u: departure = ((d + K - 1) / K) * K; if departure + T < dist[v]: dist[v] = departure + T, push.
5. Output dist[Y] (or -1 if INF).

## 4. Complexity Analysis
- **Time Complexity**: `O(M log N)`
- **Space Complexity**: `O(N + M)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

struct Edge {
    int to;
    long long t, k;
};

const long long INF = 4e18;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, x, y;
    if (!(cin >> n >> m >> x >> y)) return 0;

    vector<vector<Edge>> adj(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v;
        long long t, k;
        cin >> u >> v >> t >> k;
        adj[u].push_back({v, t, k});
        adj[v].push_back({u, t, k});
    }

    vector<long long> dist(n + 1, INF);
    priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> pq;

    dist[x] = 0;
    pq.push({0, x});

    while (!pq.empty()) {
        auto [d, u] = pq.top();
        pq.pop();

        if (d > dist[u]) continue;
        if (u == y) break;

        for (const auto& e : adj[u]) {
            long long dep = ((d + e.k - 1) / e.k) * e.k;
            long long arr = dep + e.t;
            if (arr < dist[e.to]) {
                dist[e.to] = arr;
                pq.push({arr, e.to});
            }
        }
    }

    cout << (dist[y] == INF ? -1 : dist[y]) << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Modifying Dijkstra transition costs for scheduled periodic transit intervals.
- **Reusable Pattern**: `Periodic departure: dep = ceil(cur_time / K) * K, arrival = dep + travel_time.`
