# Problem Analysis: AtCoder-typical90_bs — Fuzzy Priority

**Problem ID**: `AtCoder-typical90_bs`  
**Contest**: `typical90` (Kyopro Typical 90, Problem 071)  
**Rating / Difficulty**: 2550 (★7)  
**URL**: https://atcoder.jp/contests/typical90/tasks/typical90_bs  
**VJudge Tag**: `[problem:AtCoder-typical90_bs]`  
**Category File**: [`../categories/graph_theory/topological_sort_kahn.md`](../categories/graph_theory/topological_sort_kahn.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Topological Sort`  
- **Topic (Skill)**: `K Distinct Topological Sorts via Kahn Backtracking`  

---

## 1. Problem Statement & Key Idea
Given a DAG with N vertices and M edges, output K distinct topological sort permutations, or output -1 if fewer than K distinct valid topological orderings exist.

**Core Idea**: Backtracking search over Kahn's algorithm: branch when multiple in-degree 0 vertices are available until K permutations are found.

## 2. Core Observation & Invariant
Maintain set of available in-degree 0 vertices. At each step, branch by selecting any available vertex. Terminate as soon as K permutations are collected, bounding search complexity.

## 3. Step-by-Step Algorithm
1. Compute in-degrees.
2. DFS(order, available_set):
   - If order.size() == N: record permutation; if collected K, stop.
   - For vertex u in available_set: branch, decrement child in-degrees, recurse, backtrack.

## 4. Complexity Analysis
Time: O(K * (N + M)), Space: O(N + M).

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int n, m, k;
vector<vector<int>> adj;
vector<int> in_degree;
vector<vector<int>> results;
vector<int> cur_order;
vector<int> zero_deg;

void dfs() {
    if ((int)results.size() == k) return;
    if ((int)cur_order.size() == n) {
        results.push_back(cur_order);
        return;
    }
    if (zero_deg.empty()) return;

    int sz = zero_deg.size();
    for (int i = 0; i < sz; ++i) {
        int u = zero_deg[i];
        cur_order.push_back(u);

        vector<int> next_zero;
        for (int j = 0; j < sz; ++j) {
            if (i != j) next_zero.push_back(zero_deg[j]);
        }

        for (int v : adj[u]) {
            in_degree[v]--;
            if (in_degree[v] == 0) {
                next_zero.push_back(v);
            }
        }

        swap(zero_deg, next_zero);
        dfs();
        swap(zero_deg, next_zero);

        for (int v : adj[u]) {
            in_degree[v]++;
        }
        cur_order.pop_back();

        if ((int)results.size() == k) return;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n >> m >> k)) return 0;

    adj.resize(n + 1);
    in_degree.assign(n + 1, 0);

    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        in_degree[v]++;
    }

    for (int i = 1; i <= n; ++i) {
        if (in_degree[i] == 0) zero_deg.push_back(i);
    }

    dfs();

    if ((int)results.size() < k) {
        cout << -1 << "\n";
    } else {
        for (const auto& p : results) {
            for (int i = 0; i < n; ++i) {
                cout << p[i] << (i + 1 == n ? "" : " ");
            }
            cout << "\n";
        }
    }
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Backtracking search on Kahn's algorithm finding K topological sorts.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: K-shortest topological sorts, in-degree backtracking, and early termination on query budgets.
- **Reusable Pattern**: `Kahn Algorithm Backtracking for K Topological Sorts.`

---
Back to [K Distinct Topological Sorts via Kahn Backtracking](../categories/graph_theory/topological_sort_kahn.md) | [Categories Directory](../categories/README.md)