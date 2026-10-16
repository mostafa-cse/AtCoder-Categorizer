# Problem Analysis: AtCoder-abc168_d — .. (Double Dots)

**Problem ID**: `AtCoder-abc168_d`  
**Contest**: `abc168`  
**Rating / Difficulty**: 804  
**URL**: https://atcoder.jp/contests/abc168/tasks/abc168_d  
**VJudge Tag**: `[problem:AtCoder-abc168_d]`  
**Category File**: [`../categories/graph_theory/bfs_parent_reconstruction.md`](../categories/graph_theory/bfs_parent_reconstruction.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Shortest Paths`  
- **Topic (Skill)**: `Shortest Path Tree / BFS Parent Reconstruction`  

---

## 1. Problem Statement & Key Idea
Given a connected unweighted graph with N vertices and M edges. Place a signpost at each vertex i (i >= 2) pointing to an adjacent vertex such that following the signposts reaches vertex 1 in the minimum number of steps.

**Key Idea**: In an unweighted graph, standard Breadth-First Search (BFS) from vertex 1 computes the exact shortest path tree. For each neighbor v reached from u with dist[v] == -1, record parent[v] = u.

## 2. Core Observation & Invariant
Since all edge weights are 1, the first time vertex v is reached from vertex u during BFS guarantees that dist[v] = dist[u] + 1 is minimal. Directing an arrow from v to u ensures optimal descent to root 1.

## 3. Step-by-Step Algorithm
1. Initialize dist array to -1 for all vertices 1..N and parent array to 0.
2. Set dist[1] = 0 and push vertex 1 into a queue.
3. While queue is not empty, pop u and inspect each adjacent vertex v.
4. If dist[v] == -1, set dist[v] = dist[u] + 1, parent[v] = u, and push v to queue.
5. Output 'Yes', then print parent[i] for each i from 2 to N.

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
        adj[v].push_back(u);
    }

    vector<int> dist(n + 1, -1);
    vector<int> parent(n + 1, 0);
    queue<int> q;

    dist[1] = 0;
    q.push(1);

    while (!q.empty()) {
        int u = q.front();
        q.pop();

        for (int v : adj[u]) {
            if (dist[v] == -1) {
                dist[v] = dist[u] + 1;
                parent[v] = u;
                q.push(v);
            }
        }
    }

    cout << "Yes\n";
    for (int i = 2; i <= n; ++i) {
        cout << parent[i] << "\n";
    }

    return 0;
}
```

## 6. Editorial Comparison & Alignment
Identical to official editorial. Graph is guaranteed connected, so all vertices are reached.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Shortest path tree reconstruction using BFS predecessors.
- **Reusable Pattern**: `BFS parent tracking: parent[v] = u when expanding unvisited neighbor v.`
