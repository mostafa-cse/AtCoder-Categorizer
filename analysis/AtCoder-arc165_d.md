# Problem Analysis: AtCoder-arc165_d — D. Substring Comparison

**Problem ID**: `AtCoder-arc165_d`  
**Contest**: `arc165`  
**Rating / Difficulty**: 2589  
**URL**: https://atcoder.jp/contests/arc165/tasks/arc165_d  
**VJudge Tag**: `[problem:AtCoder-arc165_d]`  
**Category File**: [`../categories/graph_theory/substring_comparison_iterative_scc_contraction.md`](../categories/graph_theory/substring_comparison_iterative_scc_contraction.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Graph Connectivity`  
- **Topic (Skill)**: `Strongly Connected Components (SCC)`  

---

## 1. Problem Statement & Key Idea
Determine if there exists a sequence $X$ satisfying $M$ lexicographical constraints $X[A_i, B_i] < X[C_i, D_i]$.

## 2. Core Observation & Invariant
Each constraint requires $X_{A_i} \le X_{C_i}$. Cycles of $\le$ relations enforce equality $X_u = X_v$ across SCC components. When $X_{A_i} = X_{C_i}$, the constraint advances to the next character $X[A_i+1, B_i] < X[C_i+1, D_i]$. If identical characters occur when both substrings end, a contradiction is reached.

## 3. Step-by-Step Algorithm
1. 1. Maintain DSU of equal indices.
2. 2. Iteratively advance pointers for constraints where $A_i$ and $C_i$ are in the same component. Detect prefix conflicts.
3. 3. Build directed graph between contracted component roots.
4. 4. Run Tarjan's SCC. If non-trivial SCCs exist, unite component vertices and repeat.
5. 5. If no cycles and no pointers advance, the DAG can be topologically ordered; return Yes.

## 4. Complexity Analysis
- **Time Complexity**: `O(N(N + M))`
- **Space Complexity**: `O(N + M)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Constraint {
    int A, B, C, D;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    if (!(cin >> N >> M)) return 0;

    vector<Constraint> constraints(M);
    for (int i = 0; i < M; ++i) {
        cin >> constraints[i].A >> constraints[i].B >> constraints[i].C >> constraints[i].D;
    }

    vector<int> comp(N + 1);
    for (int i = 1; i <= N; ++i) comp[i] = i;

    auto find = [&](auto& self, int i) -> int {
        return comp[i] == i ? i : (comp[i] = self(self, comp[i]));
    };

    auto unite = [&](int i, int j) -> bool {
        int ri = find(find, i);
        int rj = find(find, j);
        if (ri != rj) {
            comp[ri] = rj;
            return true;
        }
        return false;
    };

    while (true) {
        bool advanced_any = false;
        vector<Constraint> next_constraints;

        for (auto& c : constraints) {
            while (find(find, c.A) == find(find, c.C)) {
                if (c.A == c.B && c.C == c.D) {
                    cout << "No\n";
                    return 0;
                } else if (c.A == c.B && c.C < c.D) {
                    c.A = -1; // satisfied
                    advanced_any = true;
                    break;
                } else if (c.A < c.B && c.C == c.D) {
                    cout << "No\n";
                    return 0;
                } else {
                    c.A++;
                    c.C++;
                    advanced_any = true;
                }
            }
            if (c.A != -1) {
                next_constraints.push_back(c);
            }
        }
        constraints = move(next_constraints);

        vector<vector<int>> adj(N + 1);
        vector<int> nodes;
        vector<bool> in_nodes(N + 1, false);

        for (const auto& c : constraints) {
            int u = find(find, c.A);
            int v = find(find, c.C);
            if (u != v) {
                adj[u].push_back(v);
                if (!in_nodes[u]) { in_nodes[u] = true; nodes.push_back(u); }
                if (!in_nodes[v]) { in_nodes[v] = true; nodes.push_back(v); }
            }
        }

        vector<int> idx_map(N + 1, -1), low(N + 1, -1);
        vector<bool> on_stack(N + 1, false);
        vector<int> st;
        int timer = 0;
        vector<vector<int>> sccs;

        auto dfs = [&](auto& self, int u) -> void {
            idx_map[u] = low[u] = timer++;
            st.push_back(u);
            on_stack[u] = true;

            for (int v : adj[u]) {
                if (idx_map[v] == -1) {
                    self(self, v);
                    low[u] = min(low[u], low[v]);
                } else if (on_stack[v]) {
                    low[u] = min(low[u], idx_map[v]);
                }
            }

            if (low[u] == idx_map[u]) {
                vector<int> scc;
                while (true) {
                    int v = st.back();
                    st.pop_back();
                    on_stack[v] = false;
                    scc.push_back(v);
                    if (v == u) break;
                }
                sccs.push_back(scc);
            }
        };

        for (int node : nodes) {
            if (idx_map[node] == -1) {
                dfs(dfs, node);
            }
        }

        bool merged_any = false;
        for (const auto& scc : sccs) {
            if (scc.size() > 1) {
                merged_any = true;
                int root = scc[0];
                for (size_t i = 1; i < scc.size(); ++i) {
                    unite(scc[i], root);
                }
            }
        }

        if (!merged_any && !advanced_any) {
            cout << "Yes\n";
            return 0;
        }
    }

    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
