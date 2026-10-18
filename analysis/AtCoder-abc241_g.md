# Problem Analysis: AtCoder-abc241_g — Round Robin

**Problem ID**: `AtCoder-abc241_g`  
**Contest**: `abc241`  
**Rating / Difficulty**: 2422  
**URL**: https://atcoder.jp/contests/abc241/tasks/abc241_g  
**VJudge Tag**: `[problem:AtCoder-abc241_g]`  
**Category File**: [`../categories/graph_theory/round_robin_tournament_winner_max_flow.md`](../categories/graph_theory/round_robin_tournament_winner_max_flow.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Flow and Min Cut`  
- **Topic (Skill)**: `Maximum Flow / Minimum Cut`  

---

## 1. Problem Statement & Key Idea
Determine which players can win a round-robin tournament by greedily assigning all remaining matches involving candidate player k to k, and modeling the remaining non-k matches as a Maximum Flow network with upper bounds on opponents' total wins.

## 2. Core Observation & Invariant
For player k to be the unique winner, they must attain strictly more wins than any other player. To maximize k's win count, k must win every unplayed game involving k. Each other player i can then win at most (W_k - 1) - current_wins[i] matches, which maps directly to capacity constraints in a bipartite flow network.

## 3. Step-by-Step Algorithm
1. 1. For each candidate player k from 1 to N, assume k wins all remaining matches involving k, giving W_k wins.
2. 2. Check if any opponent already has >= W_k wins; if so, k cannot uniquely win.
3. 3. Construct a bipartite network: Source S connects to each unplayed match (u, v) with capacity 1.
4. 4. Each match (u, v) connects to player nodes u and v with capacity 1.
5. 5. Each player node i connects to Sink T with capacity (W_k - 1) - current_wins[i].
6. 6. Compute max flow with Dinic; if max flow equals the total number of unplayed non-k matches, player k can be the unique winner.

## 4. Complexity Analysis
- **Time Complexity**: `O(N * Dinic(V=N^2, E=N^2)) = O(N^4)`
- **Space Complexity**: `O(N^2)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

struct Dinic {
    struct Edge {
        int to, cap, rev;
    };
    int n;
    vector<vector<Edge>> adj;
    vector<int> level, ptr;

    Dinic(int n) : n(n), adj(n), level(n), ptr(n) {}

    void add_edge(int from, int to, int cap) {
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

    int dfs(int v, int t, int pushed) {
        if (pushed == 0 || v == t) return pushed;
        for (int& cid = ptr[v]; cid < (int)adj[v].size(); cid++) {
            auto& edge = adj[v][cid];
            int tr = edge.to;
            if (level[v] + 1 != level[tr] || edge.cap == 0) continue;
            int tr_pushed = dfs(tr, t, min(pushed, edge.cap));
            if (tr_pushed == 0) continue;
            edge.cap -= tr_pushed;
            adj[tr][edge.rev].cap += tr_pushed;
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

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<bool>> played(n + 1, vector<bool>(n + 1, false));
    vector<int> wins(n + 1, 0);

    for (int i = 0; i < m; i++) {
        int w, l;
        cin >> w >> l;
        played[w][l] = played[l][w] = true;
        wins[w]++;
    }

    vector<int> ans;

    for (int k = 1; k <= n; k++) {
        int extra_k = 0;
        vector<pair<int, int>> unplayed_other;
        for (int i = 1; i <= n; i++) {
            for (int j = i + 1; j <= n; j++) {
                if (played[i][j]) continue;
                if (i == k || j == k) {
                    extra_k++;
                } else {
                    unplayed_other.push_back({i, j});
                }
            }
        }

        int W_k = wins[k] + extra_k;
        bool possible = true;
        for (int i = 1; i <= n; i++) {
            if (i != k && wins[i] >= W_k) {
                possible = false;
                break;
            }
        }
        if (!possible) continue;

        int U = unplayed_other.size();
        int S = 0;
        int T = U + n + 1;
        Dinic dinic(T + 1);

        for (int m_idx = 0; m_idx < U; m_idx++) {
            int node_m = 1 + m_idx;
            dinic.add_edge(S, node_m, 1);
            dinic.add_edge(node_m, U + unplayed_other[m_idx].first, 1);
            dinic.add_edge(node_m, U + unplayed_other[m_idx].second, 1);
        }

        for (int i = 1; i <= n; i++) {
            if (i == k) continue;
            int cap = (W_k - 1) - wins[i];
            dinic.add_edge(U + i, T, cap);
        }

        if (dinic.max_flow(S, T) == U) {
            ans.push_back(k);
        }
    }

    for (size_t i = 0; i < ans.size(); i++) {
        cout << ans[i] << (i + 1 == ans.size() ? "" : " ");
    }
    cout << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
