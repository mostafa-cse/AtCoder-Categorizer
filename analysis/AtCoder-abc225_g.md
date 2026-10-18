# Problem Analysis: AtCoder-abc225_g — G. X

**Problem ID**: `AtCoder-abc225_g`  
**Contest**: `abc225`  
**Rating / Difficulty**: 2566  
**URL**: https://atcoder.jp/contests/abc225/tasks/abc225_g  
**VJudge Tag**: `[problem:AtCoder-abc225_g]`  
**Category File**: [`../categories/graph_theory/x_grid_project_selection_dinic_min_cut.md`](../categories/graph_theory/x_grid_project_selection_dinic_min_cut.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Flow and Min Cut`  
- **Topic (Skill)**: `Maximum Closure Problem`  

---

## 1. Problem Statement & Key Idea
Given an $H \times W$ grid with values $A_{i, j}$, choose squares to draw X's on to maximize $\sum A_{i, j} - C \times (\text{number of segments})$. A main diagonal segment starts at $(i, j)$ if $(i, j)$ is chosen and $(i-1, j-1)$ is NOT chosen. An anti diagonal segment starts at $(i, j)$ if $(i, j)$ is chosen and $(i-1, j+1)$ is NOT chosen. Model as Min-Cut on a flow network.

## 2. Core Observation & Invariant
In an $S-T$ cut where $u \in S$ means square $u$ is chosen: if $u$ is not chosen ($u \in T$), we lose $A_{i, j}$ (edge $S \to u$ with capacity $A_{i, j}$). If $u$ is chosen and its diagonal predecessor $v$ is not chosen, directed edge $u \to v$ is cut with cost $C$. If no predecessor exists, edge $u \to T$ has capacity $C$. Max score = $\sum A_{i, j} - \text{MinCut}$.

## 3. Step-by-Step Algorithm
1. 1. Create Source $S$ and Sink $T$.
2. 2. For each square $(r, c)$ with node $u$:
3.    a. Add edge $S \to u$ with capacity $A_{r, c}$.
4.    b. If $r > 0$ and $c > 0$, add edge $u \to node(r-1, c-1)$ with capacity $C$; else add edge $u \to T$ with capacity $C$.
5.    c. If $r > 0$ and $c < W - 1$, add edge $u \to node(r-1, c+1)$ with capacity $C$; else add edge $u \to T$ with capacity $C$.
6. 3. Compute max flow from $S$ to $T$ using Dinic's algorithm.
7. 4. Output $\sum A_{r, c} - \text{max\_flow}$.

## 4. Complexity Analysis
- **Time Complexity**: `O(V^2 E) \approx O(H W \sqrt{H W})`
- **Space Complexity**: `O(H W)`

## 5. C++ Source Code
```cpp

#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

const long long INF = 1e18;

struct Dinic {
    struct Edge {
        int to;
        long long cap, flow;
        int rev;
    };
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

    int H, W;
    long long C;
    if (!(cin >> H >> W >> C)) return 0;

    vector<vector<long long>> A(H, vector<long long>(W));
    long long total_A = 0;
    for (int i = 0; i < H; ++i) {
        for (int j = 0; j < W; ++j) {
            cin >> A[i][j];
            total_A += A[i][j];
        }
    }

    auto node = [&](int r, int c) {
        return r * W + c;
    };

    int S = H * W;
    int T = H * W + 1;
    Dinic dinic(H * W + 2);

    for (int r = 0; r < H; ++r) {
        for (int c = 0; c < W; ++c) {
            int u = node(r, c);
            dinic.add_edge(S, u, A[r][c]);

            // Main diagonal from (r-1, c-1) to (r, c)
            if (r > 0 && c > 0) {
                dinic.add_edge(u, node(r - 1, c - 1), C);
            } else {
                dinic.add_edge(u, T, C);
            }

            // Anti diagonal from (r-1, c+1) to (r, c)
            if (r > 0 && c < W - 1) {
                dinic.add_edge(u, node(r - 1, c + 1), C);
            } else {
                dinic.add_edge(u, T, C);
            }
        }
    }

    long long cut = dinic.max_flow(S, T);
    long long ans = total_A - cut;

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
