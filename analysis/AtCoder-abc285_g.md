# Problem Analysis: AtCoder-abc285_g — G. Tatami

**Problem ID**: `AtCoder-abc285_g`  
**Contest**: `abc285`  
**Rating / Difficulty**: 2566  
**URL**: https://atcoder.jp/contests/abc285/tasks/abc285_g  
**VJudge Tag**: `[problem:AtCoder-abc285_g]`  
**Category File**: [`../categories/graph_theory/tatami_lr_bounded_flow.md`](../categories/graph_theory/tatami_lr_bounded_flow.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Flow and Min Cut`  
- **Topic (Skill)**: `L-R Flow`  

---

## 1. Problem Statement & Key Idea
Cover an $H \times W$ grid with $1 \times 1$ and $1 \times 2$ tiles such that every '1' is covered by a $1 \times 1$ tile, every '2' is covered by a $1 \times 2$ tile, and '?' can be covered by either.

## 2. Core Observation & Invariant
Every cell not covered by a $1 \times 2$ domino is naturally covered by a $1 \times 1$ tile. Thus, the problem reduces to matching adjacent cells such that every cell marked '2' has degree exactly 1, every cell marked '?' has degree $\le 1$, and '1' has degree 0. In the bipartite grid graph, this is equivalent to circulation with demands / maximum flow with lower and upper bounds (L-R flow).

## 3. Step-by-Step Algorithm
1. 1. Color grid cells by parity $(r + c) \pmod 2$ into Black and White partitions.
2. 2. Create source $S$, sink $T$, and super source/sink $S', T'$.
3. 3. For each cell with '2': Black cells require flow in $[1, 1]$ from $S$; White cells require flow in $[1, 1]$ to $T$.
4. 4. For each cell with '?': Black cells allow flow in $[0, 1]$ from $S$; White cells allow flow in $[0, 1]$ to $T$.
5. 5. Connect adjacent Black-White non-'1' cells with capacity $[0, 1]$.
6. 6. Add infinite back-edge $T \to S$ and balance deficits via $S'$ and $T'$.
7. 7. Run Dinic max flow from $S'$ to $T'$. A valid placement exists iff all demand edges from $S'$ are saturated.

## 4. Complexity Analysis
- **Time Complexity**: `O((HW)^{1.5}) via Dinic unit network`
- **Space Complexity**: `O(HW)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <string>
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
    vector<int> level, ptr;

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

    int H, W;
    if (!(cin >> H >> W)) return 0;
    vector<string> grid(H);
    for (int i = 0; i < H; ++i) cin >> grid[i];

    auto id = [&](int r, int c) {
        return r * W + c + 1;
    };

    int S = 0;
    int T = H * W + 1;
    int S_prime = T + 1;
    int T_prime = S_prime + 1;
    int num_nodes = T_prime + 1;

    vector<int> b(num_nodes, 0);
    Dinic dinic(num_nodes);

    auto add_demand_edge = [&](int u, int v, int low, int high) {
        dinic.add_edge(u, v, high - low);
        b[u] -= low;
        b[v] += low;
    };

    int dr[] = {0, 0, 1, -1};
    int dc[] = {1, -1, 0, 0};

    int count_2 = 0;

    for (int r = 0; r < H; ++r) {
        for (int c = 0; c < W; ++c) {
            char ch = grid[r][c];
            if (ch == '1') continue;
            int u = id(r, c);
            bool is_black = ((r + c) % 2 == 0);

            if (ch == '2') count_2++;

            if (is_black) {
                if (ch == '2') {
                    add_demand_edge(S, u, 1, 1);
                } else if (ch == '?') {
                    add_demand_edge(S, u, 0, 1);
                }
                for (int d = 0; d < 4; ++d) {
                    int nr = r + dr[d];
                    int nc = c + dc[d];
                    if (nr >= 0 && nr < H && nc >= 0 && nc < W && grid[nr][nc] != '1') {
                        int v = id(nr, nc);
                        add_demand_edge(u, v, 0, 1);
                    }
                }
            } else {
                if (ch == '2') {
                    add_demand_edge(u, T, 1, 1);
                } else if (ch == '?') {
                    add_demand_edge(u, T, 0, 1);
                }
            }
        }
    }

    add_demand_edge(T, S, 0, 1e9);

    int sum_b_pos = 0;
    for (int i = 0; i < num_nodes; ++i) {
        if (b[i] > 0) {
            dinic.add_edge(S_prime, i, b[i]);
            sum_b_pos += b[i];
        } else if (b[i] < 0) {
            dinic.add_edge(i, T_prime, -b[i]);
        }
    }

    int flow = dinic.max_flow(S_prime, T_prime);
    if (flow == sum_b_pos) {
        cout << "Yes\n";
    } else {
        cout << "No\n";
    }

    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
