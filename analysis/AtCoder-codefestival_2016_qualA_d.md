# Problem Analysis: AtCoder-codefestival_2016_qualA_d — Grid and Integers

**Problem ID**: `AtCoder-codefestival_2016_qualA_d`  
**Contest**: `code-festival-2016-quala`  
**Rating / Difficulty**: 2684  
**URL**: https://atcoder.jp/contests/code-festival-2016-quala/tasks/codefestival_2016_qualA_d  
**VJudge Tag**: `[problem:AtCoder-codefestival_2016_qualA_d]`  
**Category File**: [`../categories/graph_theory/grid_integers_difference_constraints.md`](../categories/graph_theory/grid_integers_difference_constraints.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Satisfiability`  
- **Topic (Skill)**: `System Of Difference Constraints`  

---

## 1. Problem Statement & Key Idea
Fill an R x C grid with non-negative integers such that every 2 x 2 subgrid satisfies a_{i, j} + a_{i+1, j+1} = a_{i, j+1} + a_{i+1, j}. This condition holds iff a_{i, j} = x_i + y_j for row potentials x_i and column potentials y_j. The given cells form edges in a bipartite graph with constraints x_i + y_j = a_k. Non-negativity requires min x_i + min y_j >= 0 in every connected component.

## 2. Core Observation & Invariant
In each connected component of the bipartite graph between row nodes and column nodes, setting a reference potential determines all other potentials. If any cycle produces conflicting potentials, no solution exists. A valid non-negative assignment exists iff each component satisfies min_{r in K} x_r + min_{c in K} y_c >= 0.

## 3. Step-by-Step Algorithm
1. 1. Build bipartite graph with R + C vertices and N edges with weight a_k.
2. 2. For each connected component, perform BFS/DFS to assign potentials.
3. 3. If an edge reaches an already visited vertex with a mismatched value, output 'No'.
4. 4. Compute m_r = min_{r in comp} x_r and m_c = min_{c in comp} y_c.
5. 5. If m_r + m_c < 0, output 'No'.
6. 6. If all components satisfy consistency and m_r + m_c >= 0, output 'Yes'.

## 4. Complexity Analysis
- **Time Complexity**: `O(R + C + N)`
- **Space Complexity**: `O(R + C + N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

const long long INF = 1e18;

struct Edge {
    int to;
    long long weight;
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int R, C, N;
    if (!(cin >> R >> C)) return 0;
    cin >> N;

    int total_nodes = R + C;
    vector<vector<Edge>> adj(total_nodes + 1);

    for (int i = 0; i < N; i++) {
        int r, c;
        long long a;
        cin >> r >> c >> a;
        int u = r;
        int v = R + c;
        adj[u].push_back({v, a});
        adj[v].push_back({u, a});
    }

    vector<bool> visited(total_nodes + 1, false);
    vector<long long> val(total_nodes + 1, 0);

    for (int i = 1; i <= total_nodes; i++) {
        if (visited[i] || adj[i].empty()) continue;

        long long min_row = INF;
        long long min_col = INF;

        queue<int> q;
        q.push(i);
        visited[i] = true;
        val[i] = 0;

        while (!q.empty()) {
            int u = q.front();
            q.pop();

            if (u <= R) {
                min_row = min(min_row, val[u]);
            } else {
                min_col = min(min_col, val[u]);
            }

            for (const auto& e : adj[u]) {
                int v = e.to;
                long long req = e.weight - val[u];
                if (visited[v]) {
                    if (val[v] != req) {
                        cout << "No\n";
                        return 0;
                    }
                } else {
                    visited[v] = true;
                    val[v] = req;
                    q.push(v);
                }
            }
        }

        if (min_row != INF && min_col != INF) {
            if (min_row + min_col < 0) {
                cout << "No\n";
                return 0;
            }
        }
    }

    cout << "Yes\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
