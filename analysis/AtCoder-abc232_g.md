# Problem Analysis: AtCoder-abc232_g — G. Modulo Shortest Path

**Problem ID**: `AtCoder-abc232_g`  
**Contest**: `abc232`  
**Rating / Difficulty**: 2550  
**URL**: https://atcoder.jp/contests/abc232/tasks/abc232_g  
**VJudge Tag**: `[problem:AtCoder-abc232_g]`  
**Category File**: [`../categories/graph_theory/modulo_shortest_path_cycle_graph_dijkstra.md`](../categories/graph_theory/modulo_shortest_path_cycle_graph_dijkstra.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Shortest Paths`  
- **Topic (Skill)**: `[Trick] Dijkstra on Segment Tree`  

---

## 1. Problem Statement & Key Idea
Find shortest path from 1 to $N$ on a directed complete graph where edge $i \to j$ has weight $(A_i + B_j) \bmod M$. Notice $(A_i + B_j) \bmod M = (B_j - (-A_i)) \bmod M$. This is exactly the clockwise distance on a cycle of length $M$ from coordinate $(-A_i) \bmod M$ to coordinate $B_j$! Instead of $N^2$ edges, place all $B_j$ on a cycle of $N$ nodes connected by their coordinate differences.

## 2. Core Observation & Invariant
Each vertex $i$ only needs to connect to the smallest $B_j \ge (-A_i \bmod M)$ and to $B_{\pi_1}$ (the wrap-around point). Traveling clockwise along the cycle preserves the exact modular distances to all other $B_j$. From each cycle node, a 0-weight edge connects to the corresponding original vertex $j$. The resulting graph has $2N$ vertices and at most $4N$ edges, solved in $O(N \log N)$ using Dijkstra.

## 3. Step-by-Step Algorithm
1. 1. Sort pairs $(B_j, j)$ in ascending order of $B_j$.
2. 2. Create $2N$ vertices: 0 to $N-1$ (original vertices), $N$ to $2N-1$ (cycle nodes).
3. 3. Add directed edges along the cycle: $N + k \to N + (k + 1) \bmod N$ with cost $(B_{k+1} - B_k + M) \bmod M$.
4. 4. Add edge from cycle node $N + k \to k$ with weight 0.
5. 5. For each vertex $i$, find smallest $B_j \ge (M - A_i) \bmod M$ via binary search, add edge from $i$ to that cycle node; also add edge to $B_0$ (wrap-around).
6. 6. Run Dijkstra from vertex 0 to vertex $N-1$.

## 4. Complexity Analysis
- **Time Complexity**: `O(N \log N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp

#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

const long long INF = 1e18;

struct Edge {
    int to;
    long long cost;
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    long long m;
    if (!(cin >> n >> m)) return 0;

    vector<long long> a(n), b(n);
    for (int i = 0; i < n; ++i) cin >> a[i];
    for (int i = 0; i < n; ++i) cin >> b[i];

    // Node 0 to n-1: original vertices 1 to n
    // Node n to 2n-1: cycle vertices sorted by B_j
    vector<pair<long long, int>> sorted_b(n);
    for (int i = 0; i < n; ++i) {
        sorted_b[i] = {b[i], i};
    }
    sort(sorted_b.begin(), sorted_b.end());

    vector<vector<Edge>> adj(2 * n);

    // Cycle edges between adjacent sorted B
    for (int i = 0; i < n; ++i) {
        int nxt = (i + 1) % n;
        long long diff = (sorted_b[nxt].first - sorted_b[i].first + m) % m;
        adj[n + i].push_back({n + nxt, diff});
        // edge from cycle node to original vertex
        adj[n + i].push_back({sorted_b[i].second, 0});
    }

    // Edges from original vertices into cycle nodes
    for (int i = 0; i < n; ++i) {
        long long target = (m - a[i]) % m;
        // Find smallest B_j >= target
        auto it = lower_bound(sorted_b.begin(), sorted_b.end(), make_pair(target, -1));
        if (it != sorted_b.end()) {
            int idx = it - sorted_b.begin();
            long long cost = it->first - target;
            adj[i].push_back({n + idx, cost});
        }
        // Also wrap-around to the first sorted B
        int idx = 0;
        long long cost = (sorted_b[0].first - target + m) % m;
        adj[i].push_back({n + idx, cost});
    }

    // Dijkstra from 0 (vertex 1) to n-1 (vertex n)
    vector<long long> dist(2 * n, INF);
    priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> pq;

    dist[0] = 0;
    pq.push({0, 0});

    while (!pq.empty()) {
        auto [d, u] = pq.top();
        pq.pop();

        if (d > dist[u]) continue;
        if (u == n - 1) break;

        for (const auto& e : adj[u]) {
            if (dist[e.to] > d + e.cost) {
                dist[e.to] = d + e.cost;
                pq.push({dist[e.to], e.to});
            }
        }
    }

    cout << dist[n - 1] << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
