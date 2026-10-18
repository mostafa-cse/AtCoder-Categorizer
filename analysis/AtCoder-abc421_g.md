# Problem Analysis: AtCoder-abc421_g — G. Increase to make it Increasing

**Problem ID**: `AtCoder-abc421_g`  
**Contest**: `abc421`  
**Rating / Difficulty**: 2410  
**URL**: https://atcoder.jp/contests/abc421/tasks/abc421_g  
**VJudge Tag**: `[problem:AtCoder-abc421_g]`  
**Category File**: [`../categories/graph_theory/min_cost_flow_difference_array_monotonicity.md`](../categories/graph_theory/min_cost_flow_difference_array_monotonicity.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Flow and Min Cut`  
- **Topic (Skill)**: `Min Cost Max Flow (MCMF)`  

---

## 1. Problem Statement & Key Idea
Add 1 to given intervals [L_i, R_i] to make array A non-decreasing with minimum total operations. In the difference array, each interval operation moves one unit of value from R_i to L_i - 1, which models directly as Minimum Cost Flow.

## 2. Core Observation & Invariant
Let d_0 = A_1, d_i = A_{i+1} - A_i for 1 <= i < N. Monotonicity requires d_i >= 0 for all 0 <= i < N. An operation on [L_i, R_i] subtracts 1 from d_{R_i} and adds 1 to d_{L_i - 1}. Negative deficit nodes demand balls, positive nodes supply balls, and node N has infinite supply.

## 3. Step-by-Step Algorithm
1. 1. Construct a flow network with nodes 0 to N plus source S and sink T.
2. 2. Connect S to i with capacity d_i, cost 0 if d_i >= 0; connect i to T with capacity -d_i, cost 0 if d_i < 0.
3. 3. Connect S to N with capacity INF, cost 0.
4. 4. For each interval [L_i, R_i], add edge from R_i to L_i - 1 with capacity INF and cost 1.
5. 5. Run Min Cost Flow of total required demand; if full flow is sent, output cost, else -1.

## 4. Complexity Analysis
- **Time Complexity**: `O(N * max(A) * (N + M) log(N + M))`
- **Space Complexity**: `O(N + M)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

const int INF = 1e9;

struct Edge {
    int to, cap, flow, cost, rev;
};

struct MinCostFlow {
    int n;
    vector<vector<Edge>> adj;
    vector<int> dist, potential, parent_edge, parent_node;

    MinCostFlow(int n) : n(n), adj(n), dist(n), potential(n, 0), parent_edge(n), parent_node(n) {}

    void add_edge(int from, int to, int cap, int cost) {
        adj[from].push_back({to, cap, 0, cost, (int)adj[to].size()});
        adj[to].push_back({from, 0, 0, -cost, (int)adj[from].size() - 1});
    }

    pair<int, int> min_cost_flow(int s, int t, int max_flow) {
        int flow = 0, cost = 0;
        while (flow < max_flow) {
            priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
            fill(dist.begin(), dist.end(), INF);
            dist[s] = 0;
            pq.push({0, s});

            while (!pq.empty()) {
                auto [d, u] = pq.top();
                pq.pop();
                if (d > dist[u]) continue;

                for (int i = 0; i < (int)adj[u].size(); i++) {
                    Edge &e = adj[u][i];
                    if (e.cap - e.flow > 0 && dist[e.to] > dist[u] + e.cost + potential[u] - potential[e.to]) {
                        dist[e.to] = dist[u] + e.cost + potential[u] - potential[e.to];
                        parent_node[e.to] = u;
                        parent_edge[e.to] = i;
                        pq.push({dist[e.to], e.to});
                    }
                }
            }

            if (dist[t] == INF) break;

            for (int i = 0; i < n; i++) {
                if (dist[i] < INF) potential[i] += dist[i];
            }

            int push = max_flow - flow;
            for (int v = t; v != s; v = parent_node[v]) {
                Edge &e = adj[parent_node[v]][parent_edge[v]];
                push = min(push, e.cap - e.flow);
            }

            flow += push;
            cost += push * potential[t];

            for (int v = t; v != s; v = parent_node[v]) {
                Edge &e = adj[parent_node[v]][parent_edge[v]];
                e.flow += push;
                adj[v][e.rev].flow -= push;
            }
        }
        return {flow, cost};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<int> a(n);
    int s = n + 1, t = s + 1;
    MinCostFlow mcf(t + 1);

    int req = 0;
    for (int i = 0; i < n; i++) {
        cin >> a[i];
        int dif = a[i] - (i > 0 ? a[i - 1] : 0);
        if (dif >= 0) {
            mcf.add_edge(s, i, dif, 0);
        } else {
            mcf.add_edge(i, t, -dif, 0);
            req += -dif;
        }
    }

    mcf.add_edge(s, n, INF, 0);

    for (int i = 0; i < m; i++) {
        int l, r;
        cin >> l >> r;
        mcf.add_edge(r, l - 1, INF, 1);
    }

    auto [flow, cost] = mcf.min_cost_flow(s, t, req);
    if (flow < req) {
        cout << -1 << "\n";
    } else {
        cout << cost << "\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
