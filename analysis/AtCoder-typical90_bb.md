# Problem Analysis: AtCoder-typical90_bb — Takahashi Number

**Problem ID**: `AtCoder-typical90_bb`  
**Contest**: `typical90` (Kyopro Typical 90, Problem 054)  
**Rating / Difficulty**: 2150 (★6)  
**URL**: https://atcoder.jp/contests/typical90/tasks/typical90_bb  
**VJudge Tag**: `[problem:AtCoder-typical90_bb]`  
**Category File**: [`../categories/graph_theory/hypergraph_bfs.md`](../categories/graph_theory/hypergraph_bfs.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Graph Modeling & Transformations`  
- **Topic (Skill)**: `Auxiliary Intermediate Node for Clique / Hypergraph Compression in BFS`  

---

## 1. Problem Statement & Key Idea
N authors, M research papers. Paper i is co-authored by K_i authors. Co-authors have collaboration distance 1. Find the Takahashi number (shortest distance from author 1) for all authors.

**Core Idea**: Connecting all pairs of authors in each paper directly creates sum K_i^2 edges (TLE/MLE). Introduce an auxiliary vertex for each paper!

## 2. Core Observation & Invariant
For paper i, add undirected edges between paper node P_i and each of its authors. Distance between authors in the auxiliary bipartite graph is exactly 2 * original_distance.

## 3. Step-by-Step Algorithm
1. Build bipartite graph with N + M vertices (1..N authors, N+1..N+M papers).
2. For paper j: add edge between author u and paper node N + j.
3. Run standard unweighted BFS from author 1.
4. For author i: distance is dist[i] / 2 (or -1 if unreachable).

## 4. Complexity Analysis
Time: O(N + sum K_i), Space: O(N + sum K_i).

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<int>> adj(n + m + 1);

    for (int i = 1; i <= m; ++i) {
        int k;
        cin >> k;
        int paper_node = n + i;
        for (int j = 0; j < k; ++j) {
            int author;
            cin >> author;
            adj[author].push_back(paper_node);
            adj[paper_node].push_back(author);
        }
    }

    vector<int> dist(n + m + 1, -1);
    queue<int> q;

    dist[1] = 0;
    q.push(1);

    while (!q.empty()) {
        int u = q.front();
        q.pop();

        for (int v : adj[u]) {
            if (dist[v] == -1) {
                dist[v] = dist[u] + 1;
                q.push(v);
            }
        }
    }

    for (int i = 1; i <= n; ++i) {
        if (dist[i] == -1) cout << -1 << "\n";
        else cout << dist[i] / 2 << "\n";
    }
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Bipartite auxiliary node graph modeling for hyperedge / clique reduction.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Replacing quadratic clique edges with auxiliary star hubs and hypergraph BFS.
- **Reusable Pattern**: `Auxiliary Hub Node Clique Compression.`

---
Back to [Auxiliary Intermediate Node for Clique / Hypergraph Compression in BFS](../categories/graph_theory/hypergraph_bfs.md) | [Categories Directory](../categories/README.md)