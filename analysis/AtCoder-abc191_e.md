# Problem Analysis: AtCoder-abc191_e — Come Back Quickly

**Problem ID**: `AtCoder-abc191_e`  
**Contest**: `abc191`  
**Rating / Difficulty**: 1323  
**URL**: https://atcoder.jp/contests/abc191/tasks/abc191_e  
**VJudge Tag**: `[problem:AtCoder-abc191_e]`  
**Category File**: [`../categories/graph_theory/dijkstra_shortest_directed_cycle.md`](../categories/graph_theory/dijkstra_shortest_directed_cycle.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Shortest Paths`  
- **Topic (Skill)**: `Multi-Source Dijkstra Shortest Cycle / Self-Loop Detection`  

---

## 1. Problem Statement & Key Idea
A directed weighted graph with N vertices and M edges. For each vertex i in 1..N, find the minimum length of a directed cycle that starts and ends at vertex i (or -1 if none exists).

**Key Idea**: For a fixed vertex i, the shortest cycle from i back to i is either a self-loop (i -> i) or the minimum over outgoing edges (i -> v, cost c) of (c + dist(v, i)).

## 2. Core Observation & Invariant
Because N <= 2000, we can run Dijkstra's algorithm once from each vertex i! To cleanly find the shortest cycle from i to i, initialize dist array to INF. Push all immediate outgoing edges (i -> v, c) into the priority queue with initial distance c (instead of dist[i] = 0). When vertex i is popped from the priority queue, the extracted distance is the exact shortest cycle!

## 3. Step-by-Step Algorithm
1. Store adjacency list with edge weights.
2. For each vertex i from 1 to N:
3.   Initialize dist array to INF, min_heap priority_queue.
4.   For each edge i -> v with weight c: if c < dist[v]: dist[v] = c, pq.push({c, v}).
5.   Run Dijkstra: pop (d, u). If u == i, answer is d, break.
6.   Relax outgoing edges: if d + weight < dist[next]: dist[next] = d + weight, push.
7.   Output dist[i] (or -1 if INF).

## 4. Complexity Analysis
- **Time Complexity**: `O(N * (M log N))`
- **Space Complexity**: `O(N + M)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

struct Edge {
    int to;
    long long w;
};

const long long INF = 4e18;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<Edge>> adj(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v;
        long long c;
        cin >> u >> v >> c;
        adj[u].push_back({v, c});
    }

    for (int i = 1; i <= n; ++i) {
        vector<long long> dist(n + 1, INF);
        priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> pq;

        for (const auto& e : adj[i]) {
            if (e.w < dist[e.to]) {
                dist[e.to] = e.w;
                pq.push({e.w, e.to});
            }
        }

        long long cycle_len = -1;
        while (!pq.empty()) {
            auto [d, u] = pq.top();
            pq.pop();

            if (u == i) {
                cycle_len = d;
                break;
            }
            if (d > dist[u]) continue;

            for (const auto& e : adj[u]) {
                if (d + e.w < dist[e.to]) {
                    dist[e.to] = d + e.w;
                    pq.push({d + e.w, e.to});
                }
            }
        }

        cout << cycle_len << "\n";
    }

    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Shortest cycle detection on directed graphs by seeding Dijkstra with 1-hop outgoing edges.
- **Reusable Pattern**: `Shortest cycle containing root: seed priority queue with immediate neighbors {cost(root, v), v}.`
