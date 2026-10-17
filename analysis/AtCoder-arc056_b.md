# Problem Analysis: AtCoder-arc056_b — 駐車場

**Problem ID**: `AtCoder-arc056_b`  
**Contest**: `arc056`  
**Rating / Difficulty**: 1726  
**URL**: https://atcoder.jp/contests/arc056/tasks/arc056_b  
**VJudge Tag**: `[problem:AtCoder-arc056_b]`  
**Category File**: [`../categories/graph_theory/max_bottleneck_path_dijkstra.md`](../categories/graph_theory/max_bottleneck_path_dijkstra.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Shortest Paths`  
- **Topic (Skill)**: `Maximum Bottleneck Path via Modified Dijkstra / Min-Vertex Path Capacity`  

---

## 1. Problem Statement & Key Idea
Given an undirected graph with N vertices and M edges. Car i starts outside at vertex S and can only traverse vertices with index >= i. Determine for each i in [1, N] whether car i can reach parking space i.

**Key Insight**: The bottleneck capacity of a path is min_{v in path} v. Car i can reach i iff the maximum bottleneck path from S to i has capacity >= i. Compute max bottleneck path from S to all vertices using modified Dijkstra.

## 2. Core Observation & Invariant
Let cap[u] be the max over all paths from S to u of the minimum vertex index on the path. Transition: cap[v] = max(cap[v], min(cap[u], v)). Use max-priority queue.

## 3. Step-by-Step Algorithm
1. Initialize cap[1..N] = 0, cap[S] = S.
2. Push (S, S) into max-priority queue.
3. While PQ not empty:
4.   pop (c, u). If c < cap[u], continue.
5.   For neighbor v of u:
6.     new_cap = min(c, v).
7.     if new_cap > cap[v]:
8.       cap[v] = new_cap, push (new_cap, v).
9. For i = 1 to N: if cap[i] >= i, print i.

## 4. Complexity Analysis
- **Time Complexity**: `O((N + M) log N)`
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

    int n, m, s;
    if (!(cin >> n >> m >> s)) return 0;

    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    vector<int> cap(n + 1, 0);
    priority_queue<pair<int, int>> pq;

    cap[s] = s;
    pq.push({s, s});

    while (!pq.empty()) {
        auto [c, u] = pq.top();
        pq.pop();

        if (c < cap[u]) continue;

        for (int v : adj[u]) {
            int next_c = min(c, v);
            if (next_c > cap[v]) {
                cap[v] = next_c;
                pq.push({next_c, v});
            }
        }
    }

    for (int i = 1; i <= n; ++i) {
        if (cap[i] >= i) {
            cout << i << "\n";
        }
    }

    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Modifying Dijkstra's algorithm for maximum bottleneck path capacity.
- **Reusable Pattern**: `Maximum Bottleneck Path: Max-heap Dijkstra with cap[v] = min(cap[u], edge_weight).`
