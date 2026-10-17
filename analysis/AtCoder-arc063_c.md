# Problem Analysis: AtCoder-arc063_c — E. Integers on a Tree

**Problem ID**: `AtCoder-arc063_c`  
**Contest**: `arc063`  
**Rating / Difficulty**: 2198  
**URL**: https://atcoder.jp/contests/arc063/tasks/arc063_c  
**VJudge Tag**: `[problem:AtCoder-arc063_c]`  
**Category File**: [`../categories/dp/tree_integers_interval_parity_dp.md`](../categories/dp/tree_integers_interval_parity_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Dp on Different Structures`  
- **Topic (Skill)**: `DP on Trees and DAGs`  

---

## 1. Problem Statement & Key Idea
Fill empty tree vertices so adjacent vertices differ by exactly 1, given K pre-assigned vertices. Bipartiteness enforces that (val[u] - depth[u]) mod 2 must be identical for all fixed vertices. A bottom-up DP intersects valid intervals [L_u, R_u], and a top-down greedy pass assigns consistent values in O(N) time.

## 2. Core Observation & Invariant
Each edge requires L_u >= L_v - 1 and R_u <= R_v + 1. If interval intersection [L_u, R_u] is non-empty and parity is globally consistent, valid assignments val[v] in {val[u] - 1, val[u] + 1} are guaranteed to exist.

## 3. Step-by-Step Algorithm
1. BFS from root 1 to find depths, parent pointers, and order.
2. Verify (val[u] - depth[u]) mod 2 is consistent across all K fixed vertices. If not, output No.
3. Initialize [L_u, R_u] = [val[u], val[u]] for fixed, [-INF, INF] for empty.
4. Bottom-up DP: update parent L_p = max(L_p, L_u - 1), R_p = min(R_p, R_u + 1). If L_p > R_p, output No.
5. Top-down DP: set root value L_1 (adjusted for parity). For each child u of p, set val[u] = val[p] - 1 if within [L_u, R_u], else val[p] + 1.
6. Output Yes and all vertex values.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int INF = 1e9;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    if (!(cin >> N)) return 0;

    vector<vector<int>> adj(N + 1);
    for (int i = 0; i < N - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    int K;
    cin >> K;
    vector<int> L(N + 1, -INF), R(N + 1, INF);
    vector<int> fixed_val(N + 1, -1);
    vector<int> fixed_nodes;

    for (int i = 0; i < K; ++i) {
        int v, p;
        cin >> v >> p;
        L[v] = p;
        R[v] = p;
        fixed_val[v] = p;
        fixed_nodes.push_back(v);
    }

    // BFS from node 1 to find depth, parent, and topological/BFS order
    vector<int> depth(N + 1, -1);
    vector<int> parent(N + 1, 0);
    vector<int> order;
    vector<int> q = {1};
    depth[1] = 0;

    for (int head = 0; head < (int)q.size(); ++head) {
        int u = q[head];
        order.push_back(u);
        for (int v : adj[u]) {
            if (depth[v] == -1) {
                depth[v] = depth[u] + 1;
                parent[v] = u;
                q.push_back(v);
            }
        }
    }

    // Check parity consistency
    int required_parity = -1;
    for (int v : fixed_nodes) {
        int p = (fixed_val[v] % 2 - depth[v] % 2 + 2) % 2;
        if (required_parity == -1) {
            required_parity = p;
        } else if (required_parity != p) {
            cout << "No\n";
            return 0;
        }
    }

    // Bottom-up DP: process in reverse BFS order
    for (int i = N - 1; i >= 1; --i) {
        int u = order[i];
        int p = parent[u];
        L[p] = max(L[p], L[u] - 1);
        R[p] = min(R[p], R[u] + 1);
        if (L[p] > R[p]) {
            cout << "No\n";
            return 0;
        }
    }

    // Top-down assignment: process in BFS order
    vector<int> ans(N + 1, 0);
    // Root value
    // Root must have parity (required_parity + depth[1]) % 2 = required_parity
    int root_val = L[1];
    if ((root_val % 2 + 2) % 2 != required_parity) {
        root_val++;
    }
    if (root_val > R[1]) {
        cout << "No\n";
        return 0;
    }
    ans[1] = root_val;

    for (int i = 1; i < N; ++i) {
        int u = order[i];
        int p = parent[u];
        // u must differ by 1 from ans[p] and be within [L[u], R[u]]
        if (ans[p] - 1 >= L[u] && ans[p] - 1 <= R[u]) {
            ans[u] = ans[p] - 1;
        } else if (ans[p] + 1 >= L[u] && ans[p] + 1 <= R[u]) {
            ans[u] = ans[p] + 1;
        } else {
            cout << "No\n";
            return 0;
        }
    }

    cout << "Yes\n";
    for (int i = 1; i <= N; ++i) {
        cout << ans[i] << "\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
