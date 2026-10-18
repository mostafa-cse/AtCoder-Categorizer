# Problem Analysis: AtCoder-abc326_g — G. Unlock Achievement

**Problem ID**: `AtCoder-abc326_g`  
**Contest**: `abc326`  
**Rating / Difficulty**: 2470  
**URL**: https://atcoder.jp/contests/abc326/tasks/abc326_g  
**VJudge Tag**: `[problem:AtCoder-abc326_g]`  
**Category File**: [`../categories/graph_theory/unlock_achievement_maximum_weight_closure.md`](../categories/graph_theory/unlock_achievement_maximum_weight_closure.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Flow and Min Cut`  
- **Topic (Skill)**: `Maximum Closure Problem`  

---

## 1. Problem Statement & Key Idea
Maximize net profit: achievement rewards minus skill upgrade costs. Model as Maximum Weight Closure on a directed DAG via Minimum Cut. Each achievement gives positive reward $A_i$ and depends on skill level nodes $(j, L_{i, j})$. Upgrading skill $j$ from level $l-1$ to $l$ incurs cost $C_j$, with level $(j, l)$ depending on level $(j, l-1)$. Dinic's algorithm computes the minimum cut.

## 2. Core Observation & Invariant
Because skill levels are bounded by 5, there are at most $4N \le 200$ skill upgrade steps. Each upgrade is a prerequisite for subsequent levels. The closed subgraph selection guarantees that selecting an achievement forces all required skill level upgrades, which is solved by standard project selection reduction.

## 3. Step-by-Step Algorithm
1. 1. Build flow network with source $S$ and sink $T$.
2. 2. For each skill $j$ and level $l \in [2, 5]$, add edge $(j, l) \to T$ with capacity $C_j$.
3. 3. Add prerequisite edge $(j, l) \to (j, l - 1)$ with capacity $\infty$ for $l > 2$.
4. 4. For each achievement $i$, add edge $S \to \text{Ach}_i$ with capacity $A_i$.
5. 5. For each required level $L_{i, j} \ge 2$, add edge $\text{Ach}_i \to (j, L_{i, j})$ with capacity $\infty$.
6. 6. Run Dinic's max flow to find MinCut. Output $\sum A_i - MinCut$.

## 4. Complexity Analysis
- **Time Complexity**: `O(V^2 E) \approx O((N + M)^3)`
- **Space Complexity**: `O(N + M)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

const long long INF = 1e18;

struct Edge {
    int to;
    long long cap;
    int rev;
};

class Dinic {
public:
    int n;
    vector<vector<Edge>> adj;
    vector<int> level;
    vector<int> ptr;

    Dinic(int n) : n(n), adj(n), level(n), ptr(n) {}

    void add_edge(int from, int to, long long cap) {
        adj[from].push_back({to, cap, (int)adj[to].size()});
        adj[to].push_back({from, 0, (int)adj[from].size() - 1});
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
                if (edge.cap > 0 && level[edge.to] == -1) {
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
            if (level[v] + 1 != level[tr] || edge.cap == 0) continue;
            long long tr_pushed = dfs(tr, t, min(pushed, edge.cap));
            if (tr_pushed == 0) continue;
            edge.cap -= tr_pushed;
            adj[tr][edge.rev].cap += tr_pushed;
            return tr_pushed;
        }
        return 0;
    }

    long long max_flow(int s, int t) {
        long long flow = 0;
        while (bfs(s, t)) {
            fill(ptr.begin(), ptr.end(), 0);
            while (long long pushed = dfs(s, t, INF)) {
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

    vector<long long> C(N);
    for (int i = 0; i < N; ++i) cin >> C[i];

    vector<long long> A(M);
    long long total_A = 0;
    for (int i = 0; i < M; ++i) {
        cin >> A[i];
        total_A += A[i];
    }

    vector<vector<int>> L(M, vector<int>(N));
    for (int i = 0; i < M; ++i) {
        for (int j = 0; j < N; ++j) {
            cin >> L[i][j];
        }
    }

    int s = 0;
    int t = 1 + 4 * N + M;
    Dinic dinic(t + 1);

    for (int j = 0; j < N; ++j) {
        for (int l = 2; l <= 5; ++l) {
            int u = 1 + j * 4 + (l - 2);
            dinic.add_edge(u, t, C[j]);
            if (l > 2) {
                int prev = 1 + j * 4 + (l - 3);
                dinic.add_edge(u, prev, INF);
            }
        }
    }

    for (int i = 0; i < M; ++i) {
        int ach_node = 1 + 4 * N + i;
        dinic.add_edge(s, ach_node, A[i]);
        for (int j = 0; j < N; ++j) {
            int req_l = L[i][j];
            if (req_l >= 2) {
                int req_node = 1 + j * 4 + (req_l - 2);
                dinic.add_edge(ach_node, req_node, INF);
            }
        }
    }

    long long min_cut = dinic.max_flow(s, t);
    long long ans = total_A - min_cut;
    cout << ans << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
