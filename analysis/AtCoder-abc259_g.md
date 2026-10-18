# Problem Analysis: AtCoder-abc259_g — Grid Card Game

**Problem ID**: `AtCoder-abc259_g`  
**Contest**: `abc259`  
**Rating / Difficulty**: 2428  
**URL**: https://atcoder.jp/contests/abc259/tasks/abc259_g  
**VJudge Tag**: `[problem:AtCoder-abc259_g]`  
**Category File**: [`../categories/graph_theory/grid_cards_row_col_selection_min_cut_closure.md`](../categories/graph_theory/grid_cards_row_col_selection_min_cut_closure.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Flow and Min Cut`  
- **Topic (Skill)**: `Maximum Closure Problem`  

---

## 1. Problem Statement & Key Idea
Maximize score in grid row/column selection with negative card conflicts by starting from the sum of all positive cards and subtracting the minimum s-t cut in a bipartite closure network.

## 2. Core Observation & Invariant
Selecting row i imposes a penalty equal to the sum of negative cards in row i; selecting col j imposes a penalty equal to negative cards in col j. Choosing neither incurs an opportunity loss of A_{i,j} for positive cards, and choosing both for a negative card is strictly forbidden (infinite capacity).

## 3. Step-by-Step Algorithm
1. 1. Calculate sum of all non-negative cards, ans = sum_{A_{i,j} >= 0} A_{i,j}.
2. 2. Build flow network: Source S connects to row node i with capacity equal to sum of |A_{i,k}| for negative cards in row i.
3. 3. Col node j connects to Sink T with capacity equal to sum of |A_{k,j}| for negative cards in col j.
4. 4. For positive A_{i,j} >= 0, add edge from row i to col j with capacity A_{i,j}.
5. 5. For negative A_{i,j} < 0, add edge from col j to row i with capacity INF.
6. 6. Compute max flow via Dinic and output ans - max_flow.

## 4. Complexity Analysis
- **Time Complexity**: `O((H + W)^2 * (H * W))`
- **Space Complexity**: `O(H * W)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

using ll = long long;
const ll INF = 1e18;

struct Dinic {
    struct Edge {
        int to;
        ll cap;
        int rev;
    };
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
            for (auto& edge : adj[v]) {
                if (edge.cap > 0 && level[edge.to] < 0) {
                    level[edge.to] = level[v] + 1;
                    q.push(edge.to);
                }
            }
        }
        return level[t] >= 0;
    }

    ll dfs(int v, int t, ll pushed) {
        if (pushed == 0 || v == t) return pushed;
        for (int& cid = ptr[v]; cid < (int)adj[v].size(); cid++) {
            auto& edge = adj[v][cid];
            int tr = edge.to;
            if (level[v] + 1 != level[tr] || edge.cap == 0) continue;
            ll tr_pushed = dfs(tr, t, min(pushed, edge.cap));
            if (tr_pushed == 0) continue;
            edge.cap -= tr_pushed;
            adj[tr][edge.rev].cap += tr_pushed;
            return tr_pushed;
        }
        return 0;
    }

    ll max_flow(int s, int t) {
        ll flow = 0;
        while (bfs(s, t)) {
            fill(ptr.begin(), ptr.end(), 0);
            while (ll pushed = dfs(s, t, INF)) {
                flow += pushed;
            }
        }
        return flow;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int h, w;
    if (!(cin >> h >> w)) return 0;

    vector<vector<ll>> a(h + 1, vector<ll>(w + 1));
    vector<ll> rsum(h + 1, 0), csum(w + 1, 0);
    int S = 0, T = h + w + 1;
    Dinic dinic(T + 1);
    ll ans = 0;

    for (int i = 1; i <= h; i++) {
        for (int j = 1; j <= w; j++) {
            cin >> a[i][j];
            if (a[i][j] >= 0) {
                dinic.add_edge(i, h + j, a[i][j]);
                ans += a[i][j];
            } else {
                dinic.add_edge(h + j, i, INF);
                rsum[i] -= a[i][j];
                csum[j] -= a[i][j];
            }
        }
    }

    for (int i = 1; i <= h; i++) dinic.add_edge(S, i, rsum[i]);
    for (int j = 1; j <= w; j++) dinic.add_edge(h + j, T, csum[j]);

    ll min_cut = dinic.max_flow(S, T);
    cout << ans - min_cut << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
