# Problem Analysis: AtCoder-abc010_4 — 浮気予防

**Problem ID**: `AtCoder-abc010_4`  
**Contest**: `abc010`  
**Rating / Difficulty**: 1777  
**URL**: https://atcoder.jp/contests/abc010/tasks/abc010_4  
**VJudge Tag**: `[problem:AtCoder-abc010_4]`  
**Category File**: [`../categories/graph_theory/min_cut_max_flow_network_disconnection.md`](../categories/graph_theory/min_cut_max_flow_network_disconnection.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Network Flow`  
- **Topic (Skill)**: `Min-Cut / Max-Flow Model on Network Disconnection`  

---

## 1. Problem Statement & Key Idea
A social network has N people (0 to N - 1) and M friendship connections. Given G girls whom Takahashi (person 0) could potentially contact. Find the minimum number of friendship edges to delete so that Takahashi cannot contact any of the G girls.

**Key Insight**: Standard Min-Cut problem. Source is Takahashi (0). Create a supersink T. For each of the G girls, add an edge to T with capacity 1. For each original friendship edge (u, v), add bidirectional capacity 1. By the Max-Flow Min-Cut Theorem, min cut equals max flow from 0 to T.

## 2. Core Observation & Invariant
Running Dinic's Algorithm or Edmonds-Karp computes the maximum flow in O(V^2 E), which runs in under 1 ms for N <= 100.

## 3. Step-by-Step Algorithm
1. Build flow network with N + 1 vertices (0 to N, where N is supersink).
2. For each girl p_i: add directed edge (p_i, N) with capacity 1.
3. For each edge (u, v): add capacity 1 in both directions.
4. Run Dinic's Algorithm from source 0 to sink N.
5. Print max flow.

## 4. Complexity Analysis
- **Time Complexity**: `O(V^2 * E)`
- **Space Complexity**: `O(V + E)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

struct Edge {
    int to, rev;
    int cap, flow;
};

struct Dinic {
    int n, s, t;
    vector<vector<Edge>> adj;
    vector<int> level, ptr;

    Dinic(int n, int s, int t) : n(n), s(s), t(t), adj(n), level(n), ptr(n) {}

    void add_edge(int from, int to, int cap) {
        adj[from].push_back({to, (int)adj[to].size(), cap, 0});
        adj[to].push_back({from, (int)adj[from].size() - 1, 0, 0});
    }

    bool bfs() {
        fill(level.begin(), level.end(), -1);
        level[s] = 0;
        queue<int> q;
        q.push(s);

        while (!q.empty()) {
            int v = q.front(); q.pop();
            for (auto& edge : adj[v]) {
                if (edge.cap - edge.flow > 0 && level[edge.to] == -1) {
                    level[edge.to] = level[v] + 1;
                    q.push(edge.to);
                }
            }
        }
        return level[t] != -1;
    }

    int dfs(int v, int pushed) {
        if (pushed == 0 || v == t) return pushed;
        for (int& cid = ptr[v]; cid < (int)adj[v].size(); ++cid) {
            auto& edge = adj[v][cid];
            int tr = edge.to;
            if (level[v] + 1 != level[tr] || edge.cap - edge.flow == 0) continue;
            int tr_pushed = dfs(tr, min(pushed, edge.cap - edge.flow));
            if (tr_pushed == 0) continue;
            edge.flow += tr_pushed;
            adj[tr][edge.rev].flow -= tr_pushed;
            return tr_pushed;
        }
        return 0;
    }

    int max_flow() {
        int flow = 0;
        while (bfs()) {
            fill(ptr.begin(), ptr.end(), 0);
            while (int pushed = dfs(s, 1e9)) {
                flow += pushed;
            }
        }
        return flow;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, g, m;
    if (!(cin >> n >> g >> m)) return 0;

    int sink = n;
    Dinic dinic(n + 1, 0, sink);

    for (int i = 0; i < g; ++i) {
        int girl;
        cin >> girl;
        dinic.add_edge(girl, sink, 1);
    }

    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        dinic.add_edge(u, v, 1);
        dinic.add_edge(v, u, 1);
    }

    cout << dinic.max_flow() << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Modeling target disconnection and edge removal using min-cut / max-flow duality.
- **Reusable Pattern**: `Network Disconnection Min-Cut: Connect target set to super-sink with unit capacity and run Dinic.`
