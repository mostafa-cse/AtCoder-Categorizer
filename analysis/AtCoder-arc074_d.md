# Problem Analysis: AtCoder-arc074_d — Lotus Leaves

**Problem ID**: `AtCoder-arc074_d`  
**Contest**: `arc074`  
**Rating / Difficulty**: 2208  
**URL**: https://atcoder.jp/contests/arc074/tasks/arc074_d  
**VJudge Tag**: `[problem:AtCoder-arc074_d]`  
**Category File**: [`../categories/graph_theory/lotus_leaves_bipartite_grid_lines_vertex_min_cut.md`](../categories/graph_theory/lotus_leaves_bipartite_grid_lines_vertex_min_cut.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Flow and Min Cut`  
- **Topic (Skill)**: `Maximum Flow / Minimum Cut`  

---

## 1. Problem Statement & Key Idea
Minimum vertex cut on bipartite row/column incidence graph solved via Dinic maximum flow.

## 2. Core Observation & Invariant
Jumping along the same row or column corresponds to moving along row vertices R_i and column vertices C_j. A leaf at (i, j) connects row R_i and column C_j. Removing a leaf removes the incidence edge between R_i and C_j. S and T define source and sink row/column endpoints.

## 3. Step-by-Step Algorithm
1. 1. If S and T share a row or column, the frog can jump directly; output -1.
2. 2. Create row nodes 1..H and column nodes H+1..H+W.
3. 3. Add Source connected to r_S and C_{c_S} with infinite capacity.
4. 4. Add r_T and C_{c_T} connected to Sink with infinite capacity.
5. 5. For each leaf 'o' at (i, j), add an undirected edge between R_i and C_j with capacity 1.
6. 6. Run Dinic's algorithm; the max flow equals the minimum leaves to remove.

## 4. Complexity Analysis
- **Time Complexity**: `O(V^2 E) with V <= 202, E <= 10^4 (< 10 ms)`
- **Space Complexity**: `O(V + E)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

const int INF = 1e9;

struct Edge {
    int to;
    int cap;
    int flow;
    int rev;
};

vector<vector<Edge>> adj;
vector<int> level, ptr;

void add_edge(int from, int to, int cap) {
    adj[from].push_back({to, cap, 0, (int)adj[to].size()});
    adj[to].push_back({from, 0, 0, (int)adj[from].size() - 1});
}

void add_undirected_edge(int u, int v, int cap) {
    adj[u].push_back({v, cap, 0, (int)adj[v].size()});
    adj[v].push_back({u, cap, 0, (int)adj[u].size() - 1});
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

int dfs(int v, int t, int pushed) {
    if (pushed == 0) return 0;
    if (v == t) return pushed;
    for (int& cid = ptr[v]; cid < (int)adj[v].size(); ++cid) {
        auto& edge = adj[v][cid];
        int tr = edge.to;
        if (level[v] + 1 != level[tr] || edge.cap - edge.flow == 0) continue;
        int tr_pushed = dfs(tr, t, min(pushed, edge.cap - edge.flow));
        if (tr_pushed == 0) continue;
        edge.flow += tr_pushed;
        adj[tr][edge.rev].flow -= tr_pushed;
        return tr_pushed;
    }
    return 0;
}

int dinic(int s, int t) {
    int flow = 0;
    while (bfs(s, t)) {
        fill(ptr.begin(), ptr.end(), 0);
        while (int pushed = dfs(s, t, INF)) {
            flow += pushed;
        }
    }
    return flow;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int H, W;
    if (!(cin >> H >> W)) return 0;

    vector<string> grid(H);
    int sr = -1, sc = -1, tr = -1, tc = -1;

    for (int i = 0; i < H; ++i) {
        cin >> grid[i];
        for (int j = 0; j < W; ++j) {
            if (grid[i][j] == 'S') {
                sr = i + 1;
                sc = j + 1;
            } else if (grid[i][j] == 'T') {
                tr = i + 1;
                tc = j + 1;
            }
        }
    }

    if (sr == tr || sc == tc) {
        cout << -1 << "\n";
        return 0;
    }

    int total_nodes = H + W + 2;
    int S_node = H + W + 1;
    int T_node = H + W + 2;

    adj.assign(total_nodes + 1, vector<Edge>());
    level.resize(total_nodes + 1);
    ptr.resize(total_nodes + 1);

    // Source connects to start row and col
    add_edge(S_node, sr, INF);
    add_edge(S_node, H + sc, INF);

    // Target row and col connect to Sink
    add_edge(tr, T_node, INF);
    add_edge(H + tc, T_node, INF);

    // For leaves 'o', undirected capacity 1
    for (int i = 0; i < H; ++i) {
        for (int j = 0; j < W; ++j) {
            if (grid[i][j] == 'o') {
                add_undirected_edge(i + 1, H + j + 1, 1);
            }
        }
    }

    int max_flow = dinic(S_node, T_node);
    if (max_flow >= INF) {
        cout << -1 << "\n";
    } else {
        cout << max_flow << "\n";
    }

    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
