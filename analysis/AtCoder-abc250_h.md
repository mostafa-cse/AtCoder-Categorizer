# Problem Analysis: AtCoder-abc250_h — Ex - Trespassing Takahashi

**Problem ID**: `AtCoder-abc250_h`  
**Contest**: `abc250`  
**Rating / Difficulty**: 2773  
**URL**: https://atcoder.jp/contests/abc250/tasks/abc250_h  
**VJudge Tag**: `[problem:AtCoder-abc250_h]`  
**Category File**: [`../categories/graph_theory/multi_source_dijkstra_mst_reachability.md`](../categories/graph_theory/multi_source_dijkstra_mst_reachability.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Shortest Paths`  
- **Topic (Skill)**: `Dijkstra's Algorithm`  

---

## 1. Problem Statement & Key Idea
In a weighted undirected graph with N vertices, houses are located at vertices 1 through K. Takahashi can travel between houses with stamina limit t without resting at non-house vertices. For Q queries (x, y, t), determine if Takahashi can travel between house x and house y.

## 2. Core Observation & Invariant
Any travel between houses through intermediate non-house vertices can be decomposed into transitions between Voronoi cells of houses. By running multi-source Dijkstra from all K houses simultaneously, each vertex v is assigned its closest house h(v) and distance d(v). For each edge (u, v) with cost c, traversing from h(u) to h(v) via edge (u, v) requires stamina d(u) + d(v) + c. This forms an auxiliary graph with at most M edges connecting the K houses. Answering reachability queries for stamina threshold t reduces to dynamic connectivity or Kruskal's MST on this auxiliary graph, solvable offline with DSU.

## 3. Step-by-Step Algorithm
1. 1. Initialize a multi-source Dijkstra priority queue with all house vertices 1..K at distance 0 with home[i] = i.
2. 2. Run Dijkstra to compute for all v in 1..N: dist[v] and home[v].
3. 3. For each original edge (u, v, c) where home[u] != home[v], create a macro-edge between home[u] and home[v] with weight dist[u] + dist[v] + c.
4. 4. Sort all macro-edges by weight ascending.
5. 5. Sort all Q queries (x_i, y_i, t_i) by threshold t_i ascending.
6. 6. Use a Disjoint Set Union (DSU) structure to unite houses for all macro-edges with weight <= t_i, then check if find(x_i) == find(y_i).
7. 7. Output Yes/No in original query order.

## 4. Complexity Analysis
- **Time Complexity**: `O((N + M) log N + (M + Q) log(M + Q))`
- **Space Complexity**: `O(N + M + Q)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

static const long long INF = 1e18;

struct OriginalEdge {
    int u, v;
    long long c;
};

struct Edge {
    int u, v;
    long long w;
    bool operator<(const Edge& other) const {
        return w < other.w;
    }
};

struct Query {
    int id;
    int x, y;
    long long t;
    bool operator<(const Query& other) const {
        return t < other.t;
    }
};

struct DSU {
    vector<int> parent;
    DSU(int n) : parent(n + 1) {
        for (int i = 0; i <= n; ++i) parent[i] = i;
    }
    int find(int i) {
        if (parent[i] == i)
            return i;
        return parent[i] = find(parent[i]);
    }
    void unite(int i, int j) {
        int root_i = find(i);
        int root_j = find(j);
        if (root_i != root_j) {
            parent[root_i] = root_j;
        }
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M, K;
    if (!(cin >> N >> M >> K)) return 0;

    vector<vector<pair<int, long long>>> adj(N + 1);
    vector<OriginalEdge> orig_edges(M);
    for (int i = 0; i < M; ++i) {
        int u, v;
        long long c;
        cin >> u >> v >> c;
        adj[u].push_back({v, c});
        adj[v].push_back({u, c});
        orig_edges[i] = {u, v, c};
    }

    int Q;
    cin >> Q;
    vector<Query> queries(Q);
    for (int i = 0; i < Q; ++i) {
        cin >> queries[i].x >> queries[i].y >> queries[i].t;
        queries[i].id = i;
    }

    // Multi-source Dijkstra
    vector<long long> dist(N + 1, INF);
    vector<int> near(N + 1, 0);
    priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> pq;

    for (int i = 1; i <= K; ++i) {
        dist[i] = 0;
        near[i] = i;
        pq.push({0, i});
    }

    while (!pq.empty()) {
        auto [d, u] = pq.top();
        pq.pop();

        if (d > dist[u]) continue;

        for (auto& edge : adj[u]) {
            int v = edge.first;
            long long weight = edge.second;
            if (dist[u] + weight < dist[v]) {
                dist[v] = dist[u] + weight;
                near[v] = near[u];
                pq.push({dist[v], v});
            }
        }
    }

    // Build edges between houses
    vector<Edge> house_edges;
    house_edges.reserve(M);
    for (int i = 0; i < M; ++i) {
        int u = orig_edges[i].u;
        int v = orig_edges[i].v;
        long long c = orig_edges[i].c;
        if (near[u] != 0 && near[v] != 0 && near[u] != near[v]) {
            house_edges.push_back({near[u], near[v], dist[u] + c + dist[v]});
        }
    }

    sort(house_edges.begin(), house_edges.end());
    sort(queries.begin(), queries.end());

    DSU dsu(K);
    vector<bool> ans(Q, false);
    size_t edge_idx = 0;

    for (int i = 0; i < Q; ++i) {
        while (edge_idx < house_edges.size() && house_edges[edge_idx].w <= queries[i].t) {
            dsu.unite(house_edges[edge_idx].u, house_edges[edge_idx].v);
            edge_idx++;
        }
        if (dsu.find(queries[i].x) == dsu.find(queries[i].y)) {
            ans[queries[i].id] = true;
        }
    }

    for (int i = 0; i < Q; ++i) {
        if (ans[i]) {
            cout << "Yes\n";
        } else {
            cout << "No\n";
        }
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
