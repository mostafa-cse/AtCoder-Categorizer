# Problem Analysis: AtCoder-abc142_f — Pure

**Problem ID**: `AtCoder-abc142_f`  
**Contest**: `abc142`  
**Rating / Difficulty**: 1919  
**URL**: https://atcoder.jp/contests/abc142/tasks/abc142_f  
**VJudge Tag**: `[problem:AtCoder-abc142_f]`  
**Category File**: [`../categories/graph_theory/induced_directed_cycle_shortest_bfs.md`](../categories/graph_theory/induced_directed_cycle_shortest_bfs.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Cycles / BFS`  
- **Topic (Skill)**: `Induced Directed Cycle Extraction via Shortest Cycle BFS Search`  

---

## 1. Problem Statement & Key Idea
Given a directed graph with N vertices and M edges. Find an induced subgraph where every vertex has in-degree 1 and out-degree 1 (an induced simple directed cycle with zero chord edges), or report -1.

Any chord in a directed cycle splits it into strictly shorter directed cycles. Therefore, a directed cycle of MINIMUM LENGTH in the graph cannot have any chord edges, making it guaranteed to be an induced cycle! Finding the shortest directed cycle is achieved by running BFS from every vertex s in O(N * (N + M)).

## 2. Core Observation & Invariant
Min-length cycle has no chords => Every vertex in the cycle has indegree 1 and outdegree 1 in the induced subgraph.

## 3. Step-by-Step Algorithm
1. For each vertex s = 1..N:
2.   Run BFS from s.
3.   If an edge u -> s is encountered, cycle length is dist[u] + 1.
4.   Track the global minimum cycle length and reconstruct the cycle path.
5. If no cycle found, output -1.
6. Otherwise print cycle size and vertices in cyclic order.

## 4. Complexity Analysis
- **Time Complexity**: `O(N * (N + M))`
- **Space Complexity**: `O(N + M)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

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

    int min_len = n + 1;
    vector<int> best_cycle;

    for (int s = 1; s <= n; ++s) {
        vector<int> dist(n + 1, -1);
        vector<int> parent(n + 1, -1);
        queue<int> q;

        dist[s] = 0;
        q.push(s);

        int cycle_end = -1;

        while (!q.empty()) {
            int u = q.front();
            q.pop();

            bool found = false;
            for (int v : adj[u]) {
                if (v == s && dist[u] + 1 < min_len) {
                    min_len = dist[u] + 1;
                    cycle_end = u;
                    found = true;
                    break;
                }
                if (dist[v] == -1) {
                    dist[v] = dist[u] + 1;
                    parent[v] = u;
                    q.push(v);
                }
            }
            if (found) break;
        }

        if (cycle_end != -1) {
            vector<int> path;
            int curr = cycle_end;
            while (curr != s) {
                path.push_back(curr);
                curr = parent[curr];
            }
            path.push_back(s);
            reverse(path.begin(), path.end());
            best_cycle = path;
        }
    }

    if (best_cycle.empty()) {
        cout << -1 << "\n";
    } else {
        cout << best_cycle.size() << "\n";
        for (int node : best_cycle) {
            cout << node << "\n";
        }
    }

    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Proving that minimal cycles are chordless, reducing induced cycle extraction to All-Pairs BFS.
- **Reusable Pattern**: `Chordless Cycle Extraction: The shortest directed cycle in G is always an induced cycle.`
