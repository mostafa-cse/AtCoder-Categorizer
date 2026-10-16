# Problem Analysis: AtCoder-abc021_c — Shortest Path Count

**Problem ID**: `AtCoder-abc021_c`  
**Contest**: `abc021`  
**Rating / Difficulty**: 1324  
**URL**: https://atcoder.jp/contests/abc021/tasks/abc021_c  
**VJudge Tag**: `[problem:AtCoder-abc021_c]`  
**Category File**: [`../categories/graph_theory/bfs_shortest_path_counting_dag.md`](../categories/graph_theory/bfs_shortest_path_counting_dag.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `BFS`  
- **Topic (Skill)**: `BFS Shortest Path Counting on DAG`  

---

## 1. Problem Statement & Key Idea
An unweighted connected graph with N vertices and M edges. Count the number of shortest paths from vertex a to vertex b, modulo 10^9 + 7.

**Key Idea**: Standard BFS computes both shortest distances dist[u] and path counts ways[u].

## 2. Core Observation & Invariant
When popping vertex u in BFS: for neighbor v: (1) if dist[v] == -1 (first time seen), set dist[v] = dist[u] + 1, ways[v] = ways[u], and push v to queue; (2) if dist[v] == dist[u] + 1 (another shortest path to v), add ways[u] to ways[v] modulo 10^9 + 7.

## 3. Step-by-Step Algorithm
1. Initialize dist array to -1, ways array to 0; dist[a] = 0, ways[a] = 1.
2. Queue q.push(a).
3. While queue is not empty: pop u.
4. For neighbor v of u: if dist[v] == -1: dist[v] = dist[u] + 1, ways[v] = ways[u], q.push(v); else if dist[v] == dist[u] + 1: ways[v] = (ways[v] + ways[u]) % MOD.
5. Output ways[b].

## 4. Complexity Analysis
- **Time Complexity**: `O(N + M)`
- **Space Complexity**: `O(N + M)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

const int MOD = 1e9 + 7;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, a, b, m;
    if (!(cin >> n >> a >> b >> m)) return 0;

    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    vector<int> dist(n + 1, -1);
    vector<long long> ways(n + 1, 0);
    queue<int> q;

    dist[a] = 0;
    ways[a] = 1;
    q.push(a);

    while (!q.empty()) {
        int u = q.front();
        q.pop();

        for (int v : adj[u]) {
            if (dist[v] == -1) {
                dist[v] = dist[u] + 1;
                ways[v] = ways[u];
                q.push(v);
            } else if (dist[v] == dist[u] + 1) {
                ways[v] = (ways[v] + ways[u]) % MOD;
            }
        }
    }

    cout << ways[b] << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Counting shortest paths in unweighted graphs simultaneously with BFS queue expansion.
- **Reusable Pattern**: `Shortest path count BFS: if dist[v] == dist[u] + 1, ways[v] += ways[u].`
