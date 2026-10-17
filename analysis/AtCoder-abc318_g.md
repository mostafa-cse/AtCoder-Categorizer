# Problem Analysis: AtCoder-abc318_g — G. Typical Path Problem

**Problem ID**: `AtCoder-abc318_g`  
**Contest**: `abc318`  
**Rating / Difficulty**: 2260  
**URL**: https://atcoder.jp/contests/abc318/tasks/abc318_g  
**VJudge Tag**: `[problem:AtCoder-abc318_g]`  
**Category File**: [`../categories/graph_theory/vertex_disjoint_paths_intermediate_node_flow.md`](../categories/graph_theory/vertex_disjoint_paths_intermediate_node_flow.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Flow and Min Cut`  
- **Topic (Skill)**: `Maximum Flow / Minimum Cut`  

---

## 1. Problem Statement & Key Idea
Given a connected undirected graph $G$ and distinct vertices $A, B, C$. Determine if there exists a simple path from $A$ to $C$ passing through $B$.

## 2. Core Observation & Invariant
A simple path connecting $A$ and $C$ via $B$ exists if and only if there exist two vertex-disjoint paths from $B$ to $A$ and from $B$ to $C$ (sharing no vertices other than $B$). We split every vertex $u \ne B$ into $u_{in} \to u_{out}$ with capacity 1 (and $B_{in} \to B_{out}$ with capacity 2). Source $S$ connects to $B_{in}$ with capacity 2; $A_{out}$ and $C_{out}$ connect to Sink $T$ with capacity 1. A valid path exists if and only if the maximum flow is 2.

## 3. Step-by-Step Algorithm
1. Build the vertex-split flow network with capacity 1 on vertex edges, capacity 2 on $B$, capacity $\infty$ on original undirected edges, and capacity 1 to Sink $T$ from $A$ and $C$.
2. Run Dinic's algorithm to compute max flow from $S$ to $T$.
3. If max flow is 2, output "Yes"; otherwise output "No".

## 4. Complexity Analysis
- **Time Complexity**: `O(N + M)`
- **Space Complexity**: `O(N + M)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

struct Dinic {
    struct Edge {
        int to;
        int cap;
        int flow;
        int rev;
    };
    int n;
    vector<vector<Edge>> adj;
    vector<int> level;
    vector<int> ptr;

    Dinic(int n) : n(n), adj(n), level(n), ptr(n) {}

    void add_edge(int from, int to, int cap) {
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

    int max_flow(int s, int t) {
        int flow = 0;
        while (bfs(s, t)) {
            fill(ptr.begin(), ptr.end(), 0);
            while (int pushed = dfs(s, t, 1e9)) {
                flow += pushed;
            }
        }
        return flow;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M;
    if (!(cin >> N >> M)) return 0;

    int A, B, C;
    cin >> A >> B >> C;

    // Vertex splitting:
    // For vertex u: in = 2*u - 1, out = 2*u
    // Source S = 0, Target T = 2*N + 1
    int S = 0;
    int T = 2 * N + 1;
    Dinic dinic(2 * N + 2);

    for (int u = 1; u <= N; ++u) {
        int cap = (u == B ? 2 : 1);
        dinic.add_edge(2 * u - 1, 2 * u, cap);
    }

    // Source connected to B_in with cap 2
    dinic.add_edge(S, 2 * B - 1, 2);

    // A_out and C_out connected to T with cap 1
    dinic.add_edge(2 * A, T, 1);
    dinic.add_edge(2 * C, T, 1);

    for (int i = 0; i < M; ++i) {
        int u, v;
        cin >> u >> v;
        // Undirected edge: out of u -> in of v, out of v -> in of u
        dinic.add_edge(2 * u, 2 * v - 1, 1);
        dinic.add_edge(2 * v, 2 * u - 1, 1);
    }

    int flow = dinic.max_flow(S, T);
    if (flow == 2) {
        cout << "Yes\n";
    } else {
        cout << "No\n";
    }

    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
