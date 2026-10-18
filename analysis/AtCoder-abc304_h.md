# Problem Analysis: AtCoder-abc304_h — Ex - Constrained Topological Sort

**Problem ID**: `AtCoder-abc304_h`  
**Contest**: `abc304`  
**Rating / Difficulty**: 2642  
**URL**: https://atcoder.jp/contests/abc304/tasks/abc304_h  
**VJudge Tag**: `[problem:AtCoder-abc304_h]`  
**Category File**: [`../categories/graph_theory/constrained_topological_sort.md`](../categories/graph_theory/constrained_topological_sort.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Graph Traversal`  
- **Topic (Skill)**: `Topological Sorting`  

---

## 1. Problem Statement & Key Idea
Given a directed graph of N vertices and M edges, find a permutation P satisfying P_u < P_v for all edges (u, v) and L_i <= P_i <= R_i for all i, or report impossible.

## 2. Core Observation & Invariant
Edges (u, v) imply R_u <= R_v - 1 and L_v >= L_u + 1. Tightening bounds in reverse topological order propagates deadlines to predecessors. In unit-execution deadline scheduling on DAGs (Jackson's rule / EDF), assigning positions k = 1, 2, ..., N greedily to the available vertex with the earliest modified deadline R_u is optimal and solves the problem.

## 3. Step-by-Step Algorithm
1. Detect cycles via topological sort. If cycle exists, output No.
2. Forward tighten L_v >= L_u + 1.
3. Reverse topological order tightening: R_u = min(R_u, min_{(u, v)} R_v - 1). If L_u > R_u, output No.
4. Track available vertices using in-degrees and release times L_u.
5. For position k = 1 ... N:
6. Add all ready vertices to a priority queue (min-heap ordered by R_u).
7. Pop vertex u with minimum R_u. If R_u < k, output No.
8. Set P_u = k, decrement successors' in-degrees, and release ready neighbors.
9. Output Yes and permutation P.

## 4. Complexity Analysis
- **Time Complexity**: `O((N + M) \log N)`
- **Space Complexity**: `O(N + M)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M;
    if (!(cin >> N >> M)) return 0;

    vector<vector<int>> adj(N + 1);
    vector<int> in_deg(N + 1, 0);

    for (int i = 0; i < M; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        in_deg[v]++;
    }

    vector<int> L(N + 1), R(N + 1);
    for (int i = 1; i <= N; ++i) {
        cin >> L[i] >> R[i];
    }

    // Cycle detection & topological sort
    queue<int> q;
    vector<int> cur_deg = in_deg;
    for (int i = 1; i <= N; ++i) {
        if (cur_deg[i] == 0) q.push(i);
    }

    vector<int> topo;
    topo.reserve(N);
    while (!q.empty()) {
        int u = q.front();
        q.pop();
        topo.push_back(u);
        for (int v : adj[u]) {
            cur_deg[v]--;
            if (cur_deg[v] == 0) q.push(v);
        }
    }

    if ((int)topo.size() < N) {
        cout << "No\n";
        return 0;
    }

    // Forward tightening: L_v >= L_u + 1
    for (int u : topo) {
        for (int v : adj[u]) {
            L[v] = max(L[v], L[u] + 1);
        }
    }

    // Backward tightening: R_u <= R_v - 1
    for (int i = N - 1; i >= 0; --i) {
        int u = topo[i];
        for (int v : adj[u]) {
            R[u] = min(R[u], R[v] - 1);
        }
        if (L[u] > R[u]) {
            cout << "No\n";
            return 0;
        }
    }

    // Greedy scheduling by EDF
    vector<vector<int>> ready_at(N + 2);
    for (int i = 1; i <= N; ++i) {
        if (in_deg[i] == 0) {
            int t = max(1, L[i]);
            if (t <= N) {
                ready_at[t].push_back(i);
            } else {
                cout << "No\n";
                return 0;
            }
        }
    }

    // Min-heap ordered by (R[u], u)
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    vector<int> P(N + 1, 0);
    cur_deg = in_deg;

    for (int k = 1; k <= N; ++k) {
        for (int u : ready_at[k]) {
            pq.push({R[u], u});
        }
        if (pq.empty()) {
            cout << "No\n";
            return 0;
        }
        auto [r_u, u] = pq.top();
        pq.pop();
        if (r_u < k) {
            cout << "No\n";
            return 0;
        }
        P[u] = k;
        for (int v : adj[u]) {
            cur_deg[v]--;
            if (cur_deg[v] == 0) {
                int t = max(k + 1, L[v]);
                if (t <= N) {
                    ready_at[t].push_back(v);
                } else {
                    cout << "No\n";
                    return 0;
                }
            }
        }
    }

    cout << "Yes\n";
    for (int i = 1; i <= N; ++i) {
        cout << P[i] << (i == N ? "" : " ");
    }
    cout << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
