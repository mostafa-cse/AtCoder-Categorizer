# Problem Analysis: AtCoder-abc132_e — Hopscotch Addict

**Problem ID**: `AtCoder-abc132_e`  
**Contest**: `abc132`  
**Rating / Difficulty**: 1625  
**URL**: https://atcoder.jp/contests/abc132/tasks/abc132_e  
**VJudge Tag**: `[problem:AtCoder-abc132_e]`  
**Category File**: [`../categories/graph_theory/modulo_expanded_graph_bfs.md`](../categories/graph_theory/modulo_expanded_graph_bfs.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Shortest Paths`  
- **Topic (Skill)**: `Modulo-3 Expanded Graph Shortest Path BFS`  

---

## 1. Problem Statement & Key Idea
Given a directed graph with N vertices and M edges. A valid move ('ken-ken-pa') consists of exactly 3 consecutive directed edges. Find the minimum number of moves to reach T from S, or -1 if impossible.

**Key Insight**: Split each vertex v into 3 states: (v, 0), (v, 1), and (v, 2) representing the step count modulo 3. Traversing an edge (u, v) advances state (u, m) to (v, (m + 1) % 3).

## 2. Core Observation & Invariant
Standard unweighted BFS on the expanded graph with 3N states and 3M edges. Reaching (T, 0) with distance d corresponds to d / 3 moves.

## 3. Step-by-Step Algorithm
1. Initialize dist[N + 1][3] with -1. dist[S][0] = 0.
2. Queue pushes (S, 0).
3. While queue is not empty, pop (u, step):
4.   If u == T and step == 0, return dist[u][0] / 3.
5.   next_step = (step + 1) % 3.
6.   For each directed neighbor v of u:
7.     If dist[v][next_step] == -1:
8.       dist[v][next_step] = dist[u][step] + 1;
9.       push (v, next_step);
10. If unreachable, return -1.

## 4. Complexity Analysis
- **Time Complexity**: `O(N + M)`
- **Space Complexity**: `O(N + M)`

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

    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
    }

    int s, t;
    cin >> s >> t;

    vector<vector<int>> dist(n + 1, vector<int>(3, -1));
    queue<pair<int, int>> q;

    dist[s][0] = 0;
    q.push({s, 0});

    while (!q.empty()) {
        auto [u, step] = q.front();
        q.pop();

        if (u == t && step == 0) {
            cout << dist[u][0] / 3 << "\n";
            return 0;
        }

        int next_step = (step + 1) % 3;
        for (int v : adj[u]) {
            if (dist[v][next_step] == -1) {
                dist[v][next_step] = dist[u][step] + 1;
                q.push({v, next_step});
            }
        }
    }

    cout << -1 << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: State-space graph expansion for modulo step-length path constraints.
- **Reusable Pattern**: `Modulo K Steps Graph BFS: vertex (u, step % K), edge to (v, (step + 1) % K).`
