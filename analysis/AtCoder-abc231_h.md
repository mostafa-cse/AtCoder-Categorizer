# Problem Analysis: AtCoder-abc231_h — Minimum Coloring

**Problem ID**: `AtCoder-abc231_h`  
**Contest**: `abc231`  
**Rating / Difficulty**: 2681  
**URL**: https://atcoder.jp/contests/abc231/tasks/abc231_h  
**VJudge Tag**: `[problem:AtCoder-abc231_h]`  
**Category File**: [`../categories/graph_theory/minimum_coloring_grid_mcmf.md`](../categories/graph_theory/minimum_coloring_grid_mcmf.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Flow and Min Cut`  
- **Topic (Skill)**: `Min Cost Max Flow (MCMF)`  

---

## 1. Problem Statement & Key Idea
Color grid cells such that every row and every column has at least one colored cell, minimizing cost. This can be viewed as selecting a set of cells covering all rows and columns. We transform this into a Minimum Cost Maximum Flow problem: add a large base offset BIG to edges ensuring full coverage of rows and columns, then find the optimal flow with minimum cost using Primal-Dual / Successive Shortest Path algorithm.

## 2. Core Observation & Invariant
Bipartite graph between H rows and W columns. Each cell (r, c) with cost A_{r, c} is a directed edge r -> c with capacity infinity and cost A_{r, c}. Lower bounds of 1 on row and column coverage are handled via offset BIG. With successive shortest path MCMF, the optimal selection of cells is computed in polynomial time.

## 3. Step-by-Step Algorithm
1. 1. Construct flow network: vertices S, T, rows 1..H, columns 1..W.
2. 2. Set up supply and demand to enforce at least 1 cell selected per row and per column.
3. 3. Add cell edges with cost A_{r, c}.
4. 4. Run Min Cost Max Flow using successive shortest path with SPFA / Dijkstra potentials.
5. 5. Output minimal total cost.

## 4. Complexity Analysis
- **Time Complexity**: `O((H + W) * E log V)`
- **Space Complexity**: `O(H + W + E)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <tuple>
#include <queue>
#include <algorithm>

using namespace std;

static const long long INF = 1e18;

struct Edge {
    int to;
    int rev;
    long long cap;
    long long cost;
};

struct MinCostFlow {
    int n;
    vector<vector<Edge>> adj;

    MinCostFlow(int n) : n(n), adj(n) {}

    void add_edge(int from, int to, long long cap, long long cost) {
        adj[from].push_back({to, (int)adj[to].size(), cap, cost});
        adj[to].push_back({from, (int)adj[from].size() - 1, 0, -cost});
    }

    pair<long long, long long> flow(int s, int t, long long max_f) {
        long long flow = 0;
        long long cost = 0;
        vector<long long> pot(n, 0);
        vector<long long> dist(n);
        vector<int> prev_v(n);
        vector<int> prev_e(n);

        while (flow < max_f) {
            fill(dist.begin(), dist.end(), INF);
            priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> pq;
            dist[s] = 0;
            pq.push({0, s});

            while (!pq.empty()) {
                auto [d, v] = pq.top();
                pq.pop();
                if (dist[v] < d) continue;

                for (int i = 0; i < (int)adj[v].size(); ++i) {
                    const Edge& e = adj[v][i];
                    if (e.cap > 0 && dist[e.to] > dist[v] + e.cost + pot[v] - pot[e.to]) {
                        dist[e.to] = dist[v] + e.cost + pot[v] - pot[e.to];
                        prev_v[e.to] = v;
                        prev_e[e.to] = i;
                        pq.push({dist[e.to], e.to});
                    }
                }
            }

            if (dist[t] == INF) break;

            for (int v = 0; v < n; ++v) {
                if (dist[v] < INF) pot[v] += dist[v];
            }

            long long push = max_f - flow;
            for (int v = t; v != s; v = prev_v[v]) {
                push = min(push, adj[prev_v[v]][prev_e[v]].cap);
            }

            flow += push;
            cost += push * pot[t];
            for (int v = t; v != s; v = prev_v[v]) {
                Edge& e = adj[prev_v[v]][prev_e[v]];
                e.cap -= push;
                adj[v][e.rev].cap += push;
            }
        }

        return {flow, cost};
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int H, W, N;
    if (!(cin >> H >> W >> N)) return 0;

    vector<long long> hmin(H, 2e9), wmin(W, 2e9);
    vector<tuple<int, int, long long>> pieces;
    pieces.reserve(N);

    for (int i = 0; i < N; ++i) {
        int r, c;
        long long cost;
        cin >> r >> c >> cost;
        --r; --c;
        hmin[r] = min(hmin[r], cost);
        wmin[c] = min(wmin[c], cost);
        pieces.push_back({r, c, cost});
    }

    int source = 0;
    int sink = H + W + 1;
    MinCostFlow mcmf(sink + 1);

    for (int i = 1; i <= H; ++i) {
        mcmf.add_edge(source, i, 1, 0);
    }
    for (int j = 1; j <= W; ++j) {
        mcmf.add_edge(H + j, sink, 1, 0);
    }

    const long long BIG = 2e9;
    for (int i = 0; i < N; ++i) {
        auto [r, c, cost] = pieces[i];
        if (cost < hmin[r] + wmin[c]) {
            long long edge_cost = cost - hmin[r] - wmin[c] + BIG;
            mcmf.add_edge(r + 1, H + c + 1, 1, edge_cost);
        }
    }

    int max_flow_target = min(H, W);
    mcmf.add_edge(source, sink, max_flow_target, BIG);

    long long base_cost = 0;
    for (int i = 0; i < H; ++i) base_cost += hmin[i];
    for (int j = 0; j < W; ++j) base_cost += wmin[j];

    auto [flow, total_cost] = mcmf.flow(source, sink, max_flow_target);
    long long ans = base_cost + total_cost - BIG * flow;
    cout << ans << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
