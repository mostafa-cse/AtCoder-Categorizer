# Problem Analysis: AtCoder-abc224_h — H. Security Camera 2

**Problem ID**: `AtCoder-abc224_h`  
**Contest**: `abc224`  
**Rating / Difficulty**: 2887  
**URL**: https://atcoder.jp/contests/abc224/tasks/abc224_h  
**VJudge Tag**: `[problem:AtCoder-abc224_h]`  
**Category File**: [`../categories/math/bipartite_covering_lp_duality_mcmf.md`](../categories/math/bipartite_covering_lp_duality_mcmf.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Mathematical Optimization`  
- **Topic (Skill)**: `Duality in Linear Programming (LP <> Flow)`  

---

## 1. Problem Statement & Key Idea
On a bipartite graph with vertex sets L and R, placing a camera at u in L costs A_u with capacity C_u; at v in R costs B_v with capacity D_v. Edge (u, v) yields profit W_e if covered by either endpoint. Maximize net profit.

## 2. Core Observation & Invariant
This is an integer linear program on a bipartite graph. Because the constraint matrix is totally unimodular, the LP relaxation has integral optimal solutions. The LP dual corresponds to Minimum Cost Maximum Flow (MCMF) / circulation on a network with source S and sink T, where vertex costs and edge weights become capacities and costs. Successive Shortest Path / SPFA solves the dual directly.

## 3. Step-by-Step Algorithm
1. 1. Construct flow network: source S, sink T.
2. 2. Add edge S -> L_i with capacity C_i and cost A_i.
3. 3. Add edge R_j -> T with capacity D_j and cost B_j.
4. 4. For each bipartite edge (u, v) with weight W, add edge u -> v with capacity 1 and cost -W.
5. 5. Run MCMF / successive shortest path with SPFA to find minimum cost circulation, which gives maximum profit.

## 4. Complexity Analysis
- **Time Complexity**: `O(F * (V + E) log V)`
- **Space Complexity**: `O(V + E)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

static const long long INF = 1e16;

struct Edge {
    int to;
    long long cap;
    long long cost;
    int rev;
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int L, R;
    if (!(cin >> L >> R)) return 0;

    vector<long long> A(L), B(R);
    for (int i = 0; i < L; ++i) cin >> A[i];
    for (int j = 0; j < R; ++j) cin >> B[j];

    vector<vector<long long>> C(L, vector<long long>(R));
    for (int i = 0; i < L; ++i) {
        for (int j = 0; j < R; ++j) {
            cin >> C[i][j];
        }
    }

    int n_nodes = L + R + 2;
    int S = 0;
    int T = L + R + 1;
    vector<vector<Edge>> adj(n_nodes);

    auto add_edge = [&](int u, int v, long long cap, long long cost) {
        adj[u].push_back({v, cap, cost, (int)adj[v].size()});
        adj[v].push_back({u, 0, -cost, (int)adj[u].size() - 1});
    };

    for (int i = 0; i < L; ++i) {
        add_edge(S, 1 + i, A[i], 0);
    }
    for (int j = 0; j < R; ++j) {
        add_edge(1 + L + j, T, B[j], 0);
    }
    for (int i = 0; i < L; ++i) {
        for (int j = 0; j < R; ++j) {
            if (C[i][j] > 0) {
                add_edge(1 + i, 1 + L + j, INF, -C[i][j]);
            }
        }
    }

    long long total_cost = 0;

    while (true) {
        vector<long long> dist(n_nodes, INF);
        vector<int> parent_node(n_nodes, -1);
        vector<int> parent_edge(n_nodes, -1);
        vector<bool> in_queue(n_nodes, false);

        queue<int> q;
        dist[S] = 0;
        q.push(S);
        in_queue[S] = true;

        while (!q.empty()) {
            int u = q.front();
            q.pop();
            in_queue[u] = false;

            for (size_t e_idx = 0; e_idx < adj[u].size(); ++e_idx) {
                const Edge& e = adj[u][e_idx];
                if (e.cap > 0 && dist[u] + e.cost < dist[e.to]) {
                    dist[e.to] = dist[u] + e.cost;
                    parent_node[e.to] = u;
                    parent_edge[e.to] = e_idx;
                    if (!in_queue[e.to]) {
                        in_queue[e.to] = true;
                        q.push(e.to);
                    }
                }
            }
        }

        if (dist[T] >= 0) {
            break;
        }

        long long push = INF;
        int curr = T;
        while (curr != S) {
            int p = parent_node[curr];
            int e_idx = parent_edge[curr];
            push = min(push, adj[p][e_idx].cap);
            curr = p;
        }

        curr = T;
        while (curr != S) {
            int p = parent_node[curr];
            int e_idx = parent_edge[curr];
            int rev = adj[p][e_idx].rev;
            adj[p][e_idx].cap -= push;
            adj[curr][rev].cap += push;
            total_cost += push * adj[p][e_idx].cost;
            curr = p;
        }
    }

    cout << -total_cost << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
