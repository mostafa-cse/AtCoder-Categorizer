# Problem Analysis: AtCoder-abc205_f — Grid and Tokens

**Problem ID**: `AtCoder-abc205_f`  
**Contest**: `abc205`  
**Rating / Difficulty**: 2082  
**URL**: https://atcoder.jp/contests/abc205/tasks/abc205_f  
**VJudge Tag**: `[problem:AtCoder-abc205_f]`  
**Category File**: [`../categories/graph_theory/vertex_capacitated_bipartite_max_flow.md`](../categories/graph_theory/vertex_capacitated_bipartite_max_flow.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Flow and Min Cut`  
- **Topic (Skill)**: `Maximum Flow / Minimum Cut`  

---

## 1. Problem Statement & Key Idea
On an H x W grid, N tokens are placed. Token i must be placed at (r_i, c_i) with A_i <= r_i <= C_i and B_i <= c_i <= D_i. No two tokens may share the same row or column. Find the maximum number of tokens that can be placed.

**Key Insight**: Each token can be chosen at most once (capacity 1 on token), can occupy at most one row, and can occupy at most one column. Furthermore, each row can host at most 1 token, and each column can host at most 1 token. We model this as a maximum flow network with node splitting: Source -> Row nodes (capacity 1) -> Token_in nodes (capacity 1) -> Token_out nodes (capacity 1) -> Column nodes (capacity 1) -> Sink.

## 2. Core Observation & Invariant
Enforcing both row-uniqueness, column-uniqueness, and token-uniqueness simultaneously is solved via a 4-layer flow network with unit edge and vertex capacities.

## 3. Step-by-Step Algorithm
1. Construct network: Source S, Row nodes 1..H, Token_in 1..N, Token_out 1..N, Column nodes 1..W, Sink T.
2. Add edge S -> Row r with capacity 1 for all r in [1, H].
3. Add edge Row r -> Token_in i with capacity 1 for all r in [A_i, C_i].
4. Add edge Token_in i -> Token_out i with capacity 1 for all i in [1, N] (vertex capacity).
5. Add edge Token_out i -> Col c with capacity 1 for all c in [B_i, D_i].
6. Add edge Col c -> Sink T with capacity 1 for all c in [1, W].
7. Compute maximum bipartite flow using Dinic's algorithm.

## 4. Complexity Analysis
- **Time Complexity**: `O(V^2 E) with Dinic, practically O(N * (H + W))`
- **Space Complexity**: `O(H + W + N + E)`

## 5. Core Skill & Reusable Pattern
- **Core Skill**: Vertex splitting and bipartite flow modeling for multi-constraint unit matching.
- **Reusable Pattern**: Token placement under simultaneous row and column exclusion constraints modeled as Source -> Rows -> Tokens -> Columns -> Sink.

## 6. Editorial Comparison & Alternative Approaches
Matches official editorial.

## 7. Verified C++17 Implementation
```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

struct Edge {
    int to;
    int cap;
    int flow;
    int rev;
};

struct Dinic {
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
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int h, w, n;
    if (!(cin >> h >> w >> n)) return 0;

    int S = 0;
    int row_start = 1;
    int token_in_start = row_start + h;
    int token_out_start = token_in_start + n;
    int col_start = token_out_start + n;
    int T = col_start + w;

    Dinic dinic(T + 1);

    for (int r = 1; r <= h; ++r) {
        dinic.add_edge(S, row_start + r - 1, 1);
    }
    for (int c = 1; c <= w; ++c) {
        dinic.add_edge(col_start + c - 1, T, 1);
    }

    for (int i = 0; i < n; ++i) {
        int a, b, c, d;
        cin >> a >> b >> c >> d;
        int t_in = token_in_start + i;
        int t_out = token_out_start + i;
        dinic.add_edge(t_in, t_out, 1);

        for (int r = a; r <= c; ++r) {
            dinic.add_edge(row_start + r - 1, t_in, 1);
        }
        for (int col = b; col <= d; ++col) {
            dinic.add_edge(t_out, col_start + col - 1, 1);
        }
    }

    cout << dinic.max_flow(S, T) << "\n";
    return 0;
}
```
