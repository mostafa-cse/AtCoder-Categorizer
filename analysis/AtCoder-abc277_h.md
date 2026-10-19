# Problem Analysis: AtCoder-abc277_h — Ex. Constrained Sums

**Problem ID**: `AtCoder-abc277_h`  
**Contest**: `abc277`  
**Rating / Difficulty**: 2917  
**URL**: https://atcoder.jp/contests/abc277/tasks/abc277_h  
**VJudge Tag**: `[problem:AtCoder-abc277_h]`  
**Category File**: [`../categories/graph_theory/bounded_variable_sum_constraints_2sat.md`](../categories/graph_theory/bounded_variable_sum_constraints_2sat.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Satisfiability`  
- **Topic (Skill)**: `System Of Difference Constraints`  

---

## 1. Problem Statement & Key Idea
Given N integer variables x_i in [0, M] and Q constraints of the form x_i + x_j <= S or x_i + x_j >= S, find a valid integer assignment or report none exists.

## 2. Core Observation & Invariant
Since M is small (M <= 100), define boolean variables P(i, v) representing the proposition (x_i >= v) for 1 <= v <= M. Natural implications enforce ordering: P(i, v) => P(i, v-1). A constraint x_i + x_j <= S translates to: if x_i >= v then x_j <= S - v, which means P(i, v) => not P(j, S - v + 1). Similarly, x_i + x_j >= S translates to: not P(i, v) => P(j, S - v + 1). All constraints are 2-SAT clauses! This yields a 2-SAT instance with O(N * M) variables.

## 3. Step-by-Step Algorithm
1. 1. Create boolean variables P(i, v) for i in [1, N] and v in [1, M].
2. 2. Add domain order clauses: P(i, v) => P(i, v-1).
3. 3. Translate each upper bound constraint x_i + x_j <= S into clauses P(i, v) => not P(j, S - v + 1).
4. 4. Translate each lower bound constraint x_i + x_j >= S into clauses not P(i, v) => P(j, S - v + 1).
5. 5. Run Tarjan's SCC algorithm to solve 2-SAT.
6. 6. If P(i, v) and not P(i, v) share an SCC, return -1.
7. 7. Otherwise, assign x_i = max { v : P(i, v) is true } (or 0 if all false). Output the solution.

## 4. Complexity Analysis
- **Time Complexity**: `O(N * M + Q * M)`
- **Space Complexity**: `O(N * M + Q * M)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct TwoSat {
    int n_vars;
    int n_nodes;
    vector<vector<int>> adj;

    TwoSat(int n) : n_vars(n), n_nodes(2 * n), adj(2 * n) {}

    // lit: 2*x for x, 2*x+1 for ~x
    void add_clause(int lit1, int lit2) {
        adj[lit1 ^ 1].push_back(lit2);
        adj[lit2 ^ 1].push_back(lit1);
    }

    void add_imp(int lit1, int lit2) {
        add_clause(lit1 ^ 1, lit2);
    }

    bool solve(vector<bool>& assignment) {
        vector<int> dfn(n_nodes, -1), low(n_nodes, -1), scc(n_nodes, -1);
        vector<bool> in_stack(n_nodes, false);
        vector<int> stk;
        stk.reserve(n_nodes);
        int timer = 0, scc_cnt = 0;

        // Iterative Tarjan to prevent deep recursion stack overflow
        vector<int> edge_idx(n_nodes, 0);
        for (int i = 0; i < n_nodes; ++i) {
            if (dfn[i] != -1) continue;

            vector<int> call_stk;
            call_stk.push_back(i);
            dfn[i] = low[i] = timer++;
            stk.push_back(i);
            in_stack[i] = true;

            while (!call_stk.empty()) {
                int u = call_stk.back();
                if (edge_idx[u] < (int)adj[u].size()) {
                    int v = adj[u][edge_idx[u]++];
                    if (dfn[v] == -1) {
                        dfn[v] = low[v] = timer++;
                        stk.push_back(v);
                        in_stack[v] = true;
                        call_stk.push_back(v);
                    } else if (in_stack[v]) {
                        low[u] = min(low[u], dfn[v]);
                    }
                } else {
                    call_stk.pop_back();
                    if (!call_stk.empty()) {
                        int p = call_stk.back();
                        low[p] = min(low[p], low[u]);
                    }
                    if (low[u] == dfn[u]) {
                        while (true) {
                            int node = stk.back();
                            stk.pop_back();
                            in_stack[node] = false;
                            scc[node] = scc_cnt;
                            if (node == u) break;
                        }
                        scc_cnt++;
                    }
                }
            }
        }

        assignment.assign(n_vars, false);
        for (int i = 0; i < n_vars; ++i) {
            if (scc[2 * i] == scc[2 * i + 1]) {
                return false;
            }
            assignment[i] = (scc[2 * i] < scc[2 * i + 1]);
        }
        return true;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M, Q;
    if (!(cin >> N >> M >> Q)) return 0;

    int total_vars = N * M;
    TwoSat solver(total_vars);

    auto var_id = [&](int i, int v) {
        return (i - 1) * M + (v - 1);
    };

    // Prefix implications: X_i >= v + 1 => X_i >= v
    for (int i = 1; i <= N; ++i) {
        for (int v = 1; v < M; ++v) {
            int v1 = var_id(i, v + 1);
            int v0 = var_id(i, v);
            solver.add_imp(2 * v1, 2 * v0);
        }
    }

    for (int q = 0; q < Q; ++q) {
        int A, B, L, R;
        cin >> A >> B >> L >> R;

        int pairs[2][2] = {
            {A, B},
            {B, A}
        };

        for (int p = 0; p < 2; ++p) {
            int a_var = pairs[p][0];
            int b_var = pairs[p][1];

            // 1. X_A + X_B <= R
            for (int u = 1; u <= M; ++u) {
                int v = R + 1 - u;
                if (v <= 0) {
                    int lit = 2 * var_id(a_var, u);
                    solver.add_clause(lit ^ 1, lit ^ 1);
                } else if (1 <= v && v <= M) {
                    solver.add_imp(2 * var_id(a_var, u), 2 * var_id(b_var, v) ^ 1);
                }
            }

            // 2. X_A + X_B >= L
            for (int u = 1; u <= M; ++u) {
                int v = L + 1 - u;
                if (v > M) {
                    int lit = 2 * var_id(a_var, u);
                    solver.add_clause(lit, lit);
                } else if (1 <= v && v <= M) {
                    solver.add_imp(2 * var_id(a_var, u) ^ 1, 2 * var_id(b_var, v));
                }
            }
        }
    }

    vector<bool> assignment;
    if (!solver.solve(assignment)) {
        cout << -1 << "\n";
        return 0;
    }

    for (int i = 1; i <= N; ++i) {
        int val = 0;
        for (int v = 1; v <= M; ++v) {
            if (assignment[var_id(i, v)]) {
                val++;
            }
        }
        cout << val << (i == N ? "" : " ");
    }
    cout << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
