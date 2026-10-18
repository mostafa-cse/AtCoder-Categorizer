# Problem Analysis: AtCoder-abc461_g — G. Graph Problem 2026

**Problem ID**: `AtCoder-abc461_g`  
**Contest**: `abc461`  
**Rating / Difficulty**: 2391  
**URL**: https://atcoder.jp/contests/abc461/tasks/abc461_g  
**VJudge Tag**: `[problem:AtCoder-abc461_g]`  
**Category File**: [`../categories/graph_theory/half_integral_independent_set_dinic_min_cut.md`](../categories/graph_theory/half_integral_independent_set_dinic_min_cut.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Flow and Min Cut`  
- **Topic (Skill)**: `Maximum Closure Problem`  

---

## 1. Problem Statement & Key Idea
The integer vertex weight sum under edge bounds W_u + W_v <= 2026 attains its LP bound at half-integers W_j in {0, 1013, 2026}. Solved via Dinic's min cut on the bipartite double cover in O((N + M) sqrt(N)) time.

## 2. Core Observation & Invariant
The continuous relaxation of max-weight independent set subject to W_u + W_v <= 2026 possesses the half-integrality property (Nemhauser-Trotter): basic optimal solutions have W_j in {0, 1013, 2026}. On the bipartite double cover of the graph with source capacities 1013 to u_L, sink capacities 1013 from u_R, and infinity cross edges (u_L -> v_R, v_L -> u_R), max flow equals the min cut, achieving the maximum total weight 2026 * N - min_cut.

## 3. Step-by-Step Algorithm
1. Construct a bipartite network with 2N vertices: S = 0, T = 2N + 1, left vertices 1..N, right vertices N+1..2N.
2. Add edges S -> u with capacity 1013 and u+N -> T with capacity 1013 for all u in [1, N].
3. For each undirected edge (u, v), add infinite capacity edges u -> v+N and v -> u+N.
4. Run Dinic's max flow algorithm and output 2026 * N - max_flow in O((N + M) sqrt(N)) time.

## 4. Complexity Analysis
- **Time Complexity**: `O((N + M) \sqrt{N})`
- **Space Complexity**: `O(N + M)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

using ll = long long;

struct Edge {
    int to;
    ll cap;
    int rev;
};

struct Dinic {
    int n;
    vector<vector<Edge>> adj;
    vector<int> level, ptr;

    Dinic(int n) : n(n), adj(n), level(n), ptr(n) {}

    void add_edge(int from, int to, ll cap) {
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
            for (auto &e : adj[v]) {
                if (e.cap > 0 && level[e.to] == -1) {
                    level[e.to] = level[v] + 1;
                    q.push(e.to);
                }
            }
        }
        return level[t] != -1;
    }

    ll dfs(int v, int t, ll pushed) {
        if (pushed == 0) return 0;
        if (v == t) return pushed;
        for (int &cid = ptr[v]; cid < (int)adj[v].size(); ++cid) {
            auto &e = adj[v][cid];
            int tr = e.to;
            if (level[v] + 1 != level[tr] || e.cap == 0) continue;
            ll tr_pushed = dfs(tr, t, min(pushed, e.cap));
            if (tr_pushed == 0) continue;
            e.cap -= tr_pushed;
            adj[tr][e.rev].cap += tr_pushed;
            return tr_pushed;
        }
        return 0;
    }

    ll max_flow(int s, int t) {
        ll flow = 0;
        while (bfs(s, t)) {
            fill(ptr.begin(), ptr.end(), 0);
            while (ll pushed = dfs(s, t, 1e18)) {
                flow += pushed;
            }
        }
        return flow;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N, M;
    if (!(cin >> N >> M)) return 0;

    int S = 0, T = 2 * N + 1;
    Dinic dinic(2 * N + 2);
    ll INF = 1e15;

    for (int i = 1; i <= N; i++) {
        dinic.add_edge(S, i, 1013);
        dinic.add_edge(N + i, T, 1013);
    }

    for (int i = 0; i < M; i++) {
        int u, v;
        cin >> u >> v;
        dinic.add_edge(u, N + v, INF);
        dinic.add_edge(v, N + u, INF);
    }

    ll flow = dinic.max_flow(S, T);
    ll ans = 2026LL * N - flow;
    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
