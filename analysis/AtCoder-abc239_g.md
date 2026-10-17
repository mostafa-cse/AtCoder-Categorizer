# Problem Analysis: AtCoder-abc239_g — Builder Takahashi

**Problem ID**: `AtCoder-abc239_g`  
**Contest**: `abc239`  
**Rating / Difficulty**: 2215  
**URL**: https://atcoder.jp/contests/abc239/tasks/abc239_g  
**VJudge Tag**: `[problem:AtCoder-abc239_g]`  
**Category File**: [`../categories/graph_theory/dinic_min_vertex_cut_builder_takahashi.md`](../categories/graph_theory/dinic_min_vertex_cut_builder_takahashi.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Flow and Min Cut`  
- **Topic (Skill)**: `Maximum Flow / Minimum Cut`  

---

## 1. Problem Statement & Key Idea
Find the minimum cost set of vertices to remove in an undirected graph with N <= 100 vertices and M <= 300 edges to disconnect vertex 1 from vertex N, and output the vertices removed.

## 2. Core Observation & Invariant
Standard minimum vertex cut reduces to minimum edge cut via vertex splitting. Each vertex v is split into v_in and v_out with capacity c_v. Undirected edge (u, v) becomes infinite capacity directed edges u_out -> v_in and v_out -> u_in. Reconstructing cut vertices corresponds to saturated split edges where v_in is reachable from source in the residual graph and v_out is unreachable.

## 3. Step-by-Step Algorithm
1. 1. Split each vertex v into 2*v (in) and 2*v+1 (out). Add edge 2*v -> 2*v+1 with capacity c_v (INF for v=1 and v=N).
2. 2. For each edge (u, v), add 2*u+1 -> 2*v and 2*v+1 -> 2*u with capacity INF.
3. 3. Run Dinic's algorithm to compute max flow from 1_out to N_in.
4. 4. Perform BFS from 1_out in the residual graph to find all reachable nodes.
5. 5. Identify vertices v where 2*v is reachable but 2*v+1 is unreachable; these form the minimum vertex cut.

## 4. Complexity Analysis
- **Time Complexity**: `O(V^2 E)`
- **Space Complexity**: `O(V + E)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

struct Edge {
    int to;
    long long cap;
    long long flow;
    int rev;
};

struct Dinic {
    int n;
    vector<vector<Edge>> adj;
    vector<int> level, ptr;

    Dinic(int n) : n(n), adj(n), level(n), ptr(n) {}

    void add_edge(int from, int to, long long cap) {
        adj[from].push_back({to, cap, 0, (int)adj[to].size()});
        adj[to].push_back({from, 0, 0, (int)adj[from].size() - 1});
    }

    bool bfs(int s, int t) {
        fill(level.begin(), level.end(), -1);
        level[s] = 0;
        queue<int> q;
        q.push(s);
        while (!q.empty()) {
            int v = q.front();
            q.pop();
            for (auto& edge : adj[v]) {
                if (edge.cap - edge.flow > 0 && level[edge.to] == -1) {
                    level[edge.to] = level[v] + 1;
                    q.push(edge.to);
                }
            }
        }
        return level[t] != -1;
    }

    long long dfs(int v, int t, long long pushed) {
        if (pushed == 0) return 0;
        if (v == t) return pushed;
        for (int& cid = ptr[v]; cid < (int)adj[v].size(); ++cid) {
            auto& edge = adj[v][cid];
            int tr = edge.to;
            if (level[v] + 1 != level[tr] || edge.cap - edge.flow == 0) continue;
            long long tr_pushed = dfs(tr, t, min(pushed, edge.cap - edge.flow));
            if (tr_pushed == 0) continue;
            edge.flow += tr_pushed;
            adj[tr][edge.rev].flow -= tr_pushed;
            return tr_pushed;
        }
        return 0;
    }

    long long max_flow(int s, int t) {
        long long flow = 0;
        while (bfs(s, t)) {
            fill(ptr.begin(), ptr.end(), 0);
            while (long long pushed = dfs(s, t, 1e18)) {
                flow += pushed;
            }
        }
        return flow;
    }

    vector<bool> reachable_from(int s) {
        vector<bool> vis(n, false);
        queue<int> q;
        q.push(s);
        vis[s] = true;
        while (!q.empty()) {
            int u = q.front();
            q.pop();
            for (auto& edge : adj[u]) {
                if (edge.cap - edge.flow > 0 && !vis[edge.to]) {
                    vis[edge.to] = true;
                    q.push(edge.to);
                }
            }
        }
        return vis;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<pair<int, int>> edges(m);
    for (int i = 0; i < m; i++) {
        cin >> edges[i].first >> edges[i].second;
        edges[i].first--; edges[i].second--;
    }

    vector<long long> c(n);
    for (int i = 0; i < n; i++) cin >> c[i];

    // Node v has vin = 2*v, vout = 2*v + 1
    const long long INF = 1e15;
    Dinic dinic(2 * n);

    for (int i = 0; i < n; i++) {
        if (i == 0 || i == n - 1) {
            dinic.add_edge(2 * i, 2 * i + 1, INF);
        } else {
            dinic.add_edge(2 * i, 2 * i + 1, c[i]);
        }
    }

    for (int i = 0; i < m; i++) {
        int u = edges[i].first, v = edges[i].second;
        dinic.add_edge(2 * u + 1, 2 * v, INF);
        dinic.add_edge(2 * v + 1, 2 * u, INF);
    }

    int s = 2 * 0 + 1; // start from 1_out
    int t = 2 * (n - 1); // end at n_in

    long long min_cost = dinic.max_flow(s, t);
    vector<bool> vis = dinic.reachable_from(s);

    vector<int> cut_vertices;
    for (int i = 1; i < n - 1; i++) {
        if (vis[2 * i] && !vis[2 * i + 1]) {
            cut_vertices.push_back(i + 1);
        }
    }

    cout << min_cost << "\n";
    cout << cut_vertices.size() << "\n";
    for (size_t i = 0; i < cut_vertices.size(); i++) {
        cout << cut_vertices[i] << (i + 1 == cut_vertices.size() ? "" : " ");
    }
    cout << "\n";

    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
