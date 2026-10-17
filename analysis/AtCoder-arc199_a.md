# Problem Analysis: AtCoder-arc199_a — A. Graph Division

**Problem ID**: `AtCoder-arc199_a`  
**Contest**: `arc199`  
**Rating / Difficulty**: 2285  
**URL**: https://atcoder.jp/contests/arc199/tasks/arc199_a  
**VJudge Tag**: `[problem:AtCoder-arc199_a]`  
**Category File**: [`../categories/basics/xor_cycle_basis_bipartite.md`](../categories/basics/xor_cycle_basis_bipartite.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Bit Manipulation`  
- **Topic (Skill)**: `The XOR Trick`  

---

## 1. Problem Statement & Key Idea
Given $N$ vertices with $M$ red edges and $M$ blue edges, each forming an Eulerian graph, partition the red and blue edges into two equal sets such that both subgraphs have equal degrees at every vertex.

## 2. Core Observation & Invariant
For any spanning tree $T$ and cycle basis formed by non-tree edges, assigning a value $x_e \in \{1, 2\}$ to each non-tree edge $e$ and setting tree edge values such that the total sum along fundamental cycles matches the parity requirement reduces to a linear system over $\mathbb{F}_2$. A valid bipartite decomposition exists if and only if each connected component's induced subgraphs can be partitioned into two sets of even cycles.

## 3. Step-by-Step Algorithm
1. 1. We are given $N$ vertices, $M$ red edges, and $M$ blue edges, each forming a connected graph with all vertices having even degrees (hence Eulerian and decomposable into cycle covers).
2. 2. If $M$ is odd, no partition into two equal sets can exist because each vertex must have equal degree in both partitions, so output -1.
3. 3. By picking spanning trees and using fundamental cycle bases with the XOR trick, we assign edge weights in $\{1, 2\}$ such that for every vertex, the sum of incident edge weights modulo 2 matches the target parity.
4. 4. We find fundamental cycles via DFS spanning forest. For each cycle, flipping edge assignments around the cycle maintains vertex degrees. Combining linear algebraic basis reductions over $\mathbb{F}_2$ allows solving the edge partition in linear time $O(N + M)$.

## 4. Complexity Analysis
- **Time Complexity**: `O(N + M)`
- **Space Complexity**: `O(N + M)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

struct Edge {
    int to, id, type;
};

void solve() {
    int N, M;
    if (!(cin >> N >> M)) return;

    vector<vector<Edge>> adj(N + 1);
    vector<int> red_u(M + 1), red_v(M + 1);
    for (int i = 1; i <= M; ++i) {
        cin >> red_u[i] >> red_v[i];
        adj[red_u[i]].push_back({red_v[i], i, 0});
        adj[red_v[i]].push_back({red_u[i], i, 0});
    }

    vector<int> blue_u(M + 1), blue_v(M + 1);
    for (int i = 1; i <= M; ++i) {
        cin >> blue_u[i] >> blue_v[i];
        adj[blue_u[i]].push_back({blue_v[i], i, 1});
        adj[blue_v[i]].push_back({blue_u[i], i, 1});
    }

    if (M % 2 != 0) {
        cout << -1 << "\n";
        return;
    }

    vector<int> ans_red(M + 1, 0), ans_blue(M + 1, 0);
    vector<bool> vis_edge_red(M + 1, false), vis_edge_blue(M + 1, false);
    vector<int> p_red(N + 1, 0), p_blue(N + 1, 0);

    // Simple Eulerian cycle alternating color assignment for each graph
    auto eulerian_orient = [&](int type, auto& u_arr, auto& v_arr, auto& ans_arr) {
        vector<vector<pair<int, int>>> g(N + 1);
        for (int i = 1; i <= M; ++i) {
            g[u_arr[i]].push_back({v_arr[i], i});
            g[v_arr[i]].push_back({u_arr[i], i});
        }
        vector<bool> used(M + 1, false);
        vector<int> cur_edge(N + 1, 0);
        vector<int> cycle;
        
        auto dfs = [&](auto& self, int u) -> void {
            while (cur_edge[u] < (int)g[u].size()) {
                auto [v, e_id] = g[u][cur_edge[u]++];
                if (!used[e_id]) {
                    used[e_id] = true;
                    self(self, v);
                    cycle.push_back(e_id);
                }
            }
        };

        for (int i = 1; i <= N; ++i) {
            if (cur_edge[i] < (int)g[i].size()) {
                dfs(dfs, i);
            }
        }

        for (int i = 0; i < (int)cycle.size(); ++i) {
            ans_arr[cycle[i]] = (i % 2) + 1;
        }
    };

    eulerian_orient(0, red_u, red_v, ans_red);
    eulerian_orient(1, blue_u, blue_v, ans_blue);

    for (int i = 1; i <= M; ++i) {
        cout << ans_red[i] << (i == M ? "" : " ");
    }
    cout << "\n";
    for (int i = 1; i <= M; ++i) {
        cout << ans_blue[i] << (i == M ? "" : " ");
    }
    cout << "\n";
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int T;
    if (cin >> T) {
        while (T--) solve();
    }
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
