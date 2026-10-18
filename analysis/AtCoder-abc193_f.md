# Problem Analysis: AtCoder-abc193_f — F. Zebraness

**Problem ID**: `AtCoder-abc193_f`  
**Contest**: `abc193`  
**Rating / Difficulty**: 2475  
**URL**: https://atcoder.jp/contests/abc193/tasks/abc193_f  
**VJudge Tag**: `[problem:AtCoder-abc193_f]`  
**Category File**: [`../categories/graph_theory/zebraness_bipartite_grid_min_cut.md`](../categories/graph_theory/zebraness_bipartite_grid_min_cut.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Flow and Min Cut`  
- **Topic (Skill)**: `Maximum Flow / Minimum Cut`  

---

## 1. Problem Statement & Key Idea
Maximize zebraness (adjacent pairs with different colors) on an $N \times N$ grid of 'B', 'W', and '?'. Flip colors on odd chessboard cells: odd 'B' becomes 'W', and odd 'W' becomes 'B'. In the flipped grid, different adjacent colors become identical colors. Maximizing identical adjacent pairs is equivalent to minimizing different adjacent pairs, which is solved by standard Minimum Cut on a flow network.

## 2. Core Observation & Invariant
On a bipartite grid, inverting labels on one partition transforms a dissimilarity maximization problem into a standard Potts model / minimum cut problem where adjacent pairs with different values pay a unit penalty.

## 3. Step-by-Step Algorithm
1. 1. Build flow network with source $S$ and sink $T$.
2. 2. For each cell $(r, c)$, let effective color be inverted if $(r + c)$ is odd.
3. 3. If effective color is 'B', add edge $S \to u$ with capacity $\infty$.
4. 4. If effective color is 'W', add edge $u \to T$ with capacity $\infty$.
5. 5. For each adjacent pair of cells $(u, v)$, add bidirectional edges $u \leftrightarrow v$ with capacity 1.
6. 6. Compute MinCut using Dinic's algorithm.
7. 7. Output $\text{Total adjacent edges} - MinCut = 2N(N - 1) - MinCut$.

## 4. Complexity Analysis
- **Time Complexity**: `O(V^2 E) \approx O(N^3)`
- **Space Complexity**: `O(N^2)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <algorithm>

using namespace std;

const int INF = 1e9;

struct Edge {
    int to;
    int cap;
    int rev;
};

class Dinic {
public:
    int n;
    vector<vector<Edge>> adj;
    vector<int> level;
    vector<int> ptr;

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
                if (edge.cap > 0 && level[edge.to] == -1) {
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
            while (int pushed = dfs(s, t, INF)) {
                flow += pushed;
            }
        }
        return flow;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    if (!(cin >> N)) return 0;

    vector<string> grid(N);
    for (int i = 0; i < N; ++i) cin >> grid[i];

    int s = 0;
    int t = N * N + 1;
    Dinic dinic(t + 1);

    int total_edges = 0;
    for (int r = 0; r < N; ++r) {
        for (int c = 0; c < N; ++c) {
            int u = 1 + r * N + c;
            char ch = grid[r][c];
            int is_odd = (r + c) % 2;

            char eff_color = ch;
            if (ch == 'B') eff_color = (is_odd ? 'W' : 'B');
            else if (ch == 'W') eff_color = (is_odd ? 'B' : 'W');

            if (eff_color == 'B') dinic.add_edge(s, u, INF);
            else if (eff_color == 'W') dinic.add_edge(u, t, INF);

            if (c + 1 < N) {
                int v = 1 + r * N + (c + 1);
                total_edges++;
                dinic.add_edge(u, v, 1);
                dinic.add_edge(v, u, 1);
            }
            if (r + 1 < N) {
                int v = 1 + (r + 1) * N + c;
                total_edges++;
                dinic.add_edge(u, v, 1);
                dinic.add_edge(v, u, 1);
            }
        }
    }

    int min_cut = dinic.max_flow(s, t);
    int ans = total_edges - min_cut;
    cout << ans << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
