# Problem Analysis: AtCoder-soundhound2018_summer_qual_e — E. + Graph

**Problem ID**: `AtCoder-soundhound2018_summer_qual_e`  
**Contest**: `soundhound2018_summer_qual`  
**Rating / Difficulty**: 2164  
**URL**: https://atcoder.jp/contests/soundhound2018_summer_qual/tasks/soundhound2018_summer_qual_e  
**VJudge Tag**: `[problem:AtCoder-soundhound2018_summer_qual_e]`  
**Category File**: [`../categories/graph_theory/edge_sum_linear_system_bipartite_odd_cycle.md`](../categories/graph_theory/edge_sum_linear_system_bipartite_odd_cycle.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Graph Traversal`  
- **Topic (Skill)**: `Depth First Search (DFS)`  

---

## 1. Problem Statement & Key Idea
Determine the number of positive integer vertex labelings on a connected graph such that for every edge (u, v), x_u + x_v = s_e. Fix x_1 = t. Every vertex value x_v is parameterized as sgn[v] * t + C[v]. An odd cycle produces an equation fixing t to a unique integer; a bipartite graph yields a continuous bounding interval [t_min, t_max] of valid positive integers.

## 2. Core Observation & Invariant
Traversing a spanning tree from root 1, edge x_u + x_v = s implies x_v = -sgn[u]*t + (s - C[u]), forcing sgn[v] = -sgn[u]. Non-tree edges between same-sign vertices form an odd cycle: sgn[u]*t + C[u] + sgn[v]*t + C[v] = s, uniquely solving for t. Non-tree edges between opposite-sign vertices must satisfy C[u] + C[v] = s. For bipartite graphs, x_v >= 1 imposes lower bounds t >= 1 - C[v] (when sgn = +1) and upper bounds t <= C[v] - 1 (when sgn = -1).

## 3. Step-by-Step Algorithm
1. Run BFS/DFS from vertex 1 with sgn[1] = 1, C[1] = 0.
2. For every traversed edge (u, v, s): if v unvisited, assign sgn[v] = -sgn[u], C[v] = s - C[u].
3. If v already visited with sgn[v] == sgn[u]: solve 2*sgn[u]*t = s - C[u] - C[v]. Check divisibility and consistency with any previously fixed t.
4. If v already visited with sgn[v] != sgn[u]: check consistency C[u] + C[v] == s. If violated, output 0.
5. If t is uniquely fixed: verify t > 0 and sgn[v]*t + C[v] > 0 for all v; output 1 if valid, 0 otherwise.
6. If no odd cycle: compute L = max_{sgn=1}(1 - C[v]) and R = min_{sgn=-1}(C[v] - 1). Output max(0LL, R - L + 1).

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

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    struct Edge {
        int to;
        long long s;
    };
    vector<vector<Edge>> adj(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v;
        long long s;
        cin >> u >> v >> s;
        adj[u].push_back({v, s});
        adj[v].push_back({u, s});
    }

    vector<int> sgn(n + 1, 0);
    vector<long long> C(n + 1, 0);
    vector<bool> visited(n + 1, false);

    sgn[1] = 1;
    C[1] = 0;
    visited[1] = true;

    queue<int> q;
    q.push(1);
    long long fixed_t = -1;
    bool has_fixed = false;

    while (!q.empty()) {
        int u = q.front();
        q.pop();

        for (auto& e : adj[u]) {
            int v = e.to;
            long long s = e.s;
            if (!visited[v]) {
                visited[v] = true;
                sgn[v] = -sgn[u];
                C[v] = s - C[u];
                q.push(v);
            } else {
                if (sgn[v] != -sgn[u]) {
                    long long diff = s - C[u] - C[v];
                    long long denom = 2LL * sgn[u];
                    if (diff % denom != 0) {
                        cout << 0 << "\n";
                        return 0;
                    }
                    long long t_cand = diff / denom;
                    if (has_fixed && fixed_t != t_cand) {
                        cout << 0 << "\n";
                        return 0;
                    }
                    has_fixed = true;
                    fixed_t = t_cand;
                } else {
                    if (C[v] != s - C[u]) {
                        cout << 0 << "\n";
                        return 0;
                    }
                }
            }
        }
    }

    if (has_fixed) {
        if (fixed_t <= 0) {
            cout << 0 << "\n";
            return 0;
        }
        for (int i = 1; i <= n; ++i) {
            long long val = (long long)sgn[i] * fixed_t + C[i];
            if (val <= 0) {
                cout << 0 << "\n";
                return 0;
            }
        }
        cout << 1 << "\n";
    } else {
        long long L = 1, R = 1e18;
        for (int i = 1; i <= n; ++i) {
            if (sgn[i] == 1) {
                L = max(L, 1LL - C[i]);
            } else {
                R = min(R, C[i] - 1LL);
            }
        }
        cout << max(0LL, R - L + 1) << "\n";
    }

    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
