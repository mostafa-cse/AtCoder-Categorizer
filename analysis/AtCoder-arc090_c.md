# Problem Analysis: AtCoder-arc090_c — E. Avoiding Collision

**Problem ID**: `AtCoder-arc090_c`  
**Contest**: `arc090`  
**Rating / Difficulty**: 2319  
**URL**: https://atcoder.jp/contests/arc090/tasks/arc090_c  
**VJudge Tag**: `[problem:AtCoder-arc090_c]`  
**Category File**: [`../categories/graph_theory/dijkstra_collision_avoidance_complementary_counting.md`](../categories/graph_theory/dijkstra_collision_avoidance_complementary_counting.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Shortest Paths`  
- **Topic (Skill)**: `Dijkstra's Algorithm`  

---

## 1. Problem Statement & Key Idea
Given an undirected weighted graph, Takahashi travels from $S$ to $T$ and Aoki from $T$ to $S$ along shortest paths at constant speed. Count pairs of shortest paths where they never meet (neither at a vertex nor along an edge), modulo $10^9+7$.

## 2. Core Observation & Invariant
Two travelers traveling at speed 1 along shortest paths of length $L$ can only collide at time $t = L/2$. The collision must occur at a unique location: either at a vertex with $2 \cdot d_S(v) = L$, or strictly inside an edge $(u, v)$ where $2 \cdot d_S(u) < L$ and $2 \cdot d_T(v) < L$.

## 3. Step-by-Step Algorithm
1. Run Dijkstra from $S$ and from $T$ to find shortest distances and path counts.
2. Apply complementary counting: total path pairs is $(\text{paths}(S \to T))^2$.
3. Subtract collisions at vertices where $2 \cdot d_S(v) = L$ and edges where $2 \cdot d_S(u) < L$ and $2 \cdot d_T(v) < L$, with each collision contributing $(\text{paths}_S[u] \times \text{paths}_T[v])^2$.

## 4. Complexity Analysis
- **Time Complexity**: `O((N + M) \log N)`
- **Space Complexity**: `O(N + M)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

const int MOD = 1000000007;

struct Edge {
    int to;
    long long cost;
};

void dijkstra(int n, int src, const vector<vector<Edge>>& adj, vector<long long>& dist, vector<long long>& paths) {
    dist.assign(n + 1, 1e18);
    paths.assign(n + 1, 0);

    priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> pq;
    dist[src] = 0;
    paths[src] = 1;
    pq.push({0, src});

    while (!pq.empty()) {
        auto [d, u] = pq.top();
        pq.pop();

        if (d > dist[u]) continue;

        for (const auto& e : adj[u]) {
            int v = e.to;
            long long w = e.cost;
            if (dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
                paths[v] = paths[u];
                pq.push({dist[v], v});
            } else if (dist[u] + w == dist[v]) {
                paths[v] = (paths[v] + paths[u]) % MOD;
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    int s, t;
    cin >> s >> t;

    struct RawEdge {
        int u, v;
        long long d;
    };
    vector<RawEdge> edges(m);
    vector<vector<Edge>> adj(n + 1);

    for (int i = 0; i < m; ++i) {
        cin >> edges[i].u >> edges[i].v >> edges[i].d;
        adj[edges[i].u].push_back({edges[i].v, edges[i].d});
        adj[edges[i].v].push_back({edges[i].u, edges[i].d});
    }

    vector<long long> dist_s, paths_s;
    vector<long long> dist_t, paths_t;

    dijkstra(n, s, adj, dist_s, paths_s);
    dijkstra(n, t, adj, dist_t, paths_t);

    long long L = dist_s[t];
    long long total_pairs = (paths_s[t] * paths_s[t]) % MOD;

    long long collide = 0;

    for (int v = 1; v <= n; ++v) {
        if (dist_s[v] + dist_t[v] == L && 2 * dist_s[v] == L) {
            long long ways = (paths_s[v] * paths_t[v]) % MOD;
            collide = (collide + ways * ways) % MOD;
        }
    }

    for (const auto& e : edges) {
        int u = e.u;
        int v = e.v;
        long long d = e.d;

        if (dist_s[u] + d + dist_t[v] == L && 2 * dist_s[u] < L && 2 * dist_t[v] < L) {
            long long ways = (paths_s[u] * paths_t[v]) % MOD;
            collide = (collide + ways * ways) % MOD;
        }
        if (dist_s[v] + d + dist_t[u] == L && 2 * dist_s[v] < L && 2 * dist_t[u] < L) {
            long long ways = (paths_s[v] * paths_t[u]) % MOD;
            collide = (collide + ways * ways) % MOD;
        }
    }

    long long ans = (total_pairs - collide) % MOD;
    if (ans < 0) ans += MOD;

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
