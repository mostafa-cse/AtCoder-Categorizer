# Problem Analysis: AtCoder-arc022_3 — Romeo and Juliet

**Problem ID**: `AtCoder-arc022_3`  
**Contest**: `arc022`  
**Rating / Difficulty**: 1694  
**URL**: https://atcoder.jp/contests/arc022/tasks/arc022_3  
**VJudge Tag**: `[problem:AtCoder-arc022_3]`  
**Category File**: [`../categories/graph_theory/tree_diameter_endpoints_2pass.md`](../categories/graph_theory/tree_diameter_endpoints_2pass.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Tree Diameter`  
- **Topic (Skill)**: `Tree Diameter Endpoints via 2-Pass BFS/DFS`  

---

## 1. Problem Statement & Key Idea
Given a tree with N vertices. Find two vertices u and v such that the distance between them is maximized (i.e. the two endpoints of the tree diameter).

**Key Insight**: Canonical 2-pass BFS algorithm: 1) Run BFS from an arbitrary starting vertex (e.g. 1) to find the farthest vertex u; 2) Run BFS from vertex u to find the farthest vertex v. (u, v) is guaranteed to be a diameter of the tree.

## 2. Core Observation & Invariant
Any vertex farthest from an arbitrary node is guaranteed to be an endpoint of some diameter of the tree. A second BFS from that endpoint identifies the opposite endpoint.

## 3. Step-by-Step Algorithm
1. BFS 1 from vertex 1: find node u with maximum distance from 1.
2. BFS 2 from node u: find node v with maximum distance from u.
3. Print u and v.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

pair<int, int> bfs(int start, int n, const vector<vector<int>>& adj) {
    vector<int> dist(n + 1, -1);
    queue<int> q;
    dist[start] = 0;
    q.push(start);

    int farthest_node = start;
    int max_d = 0;

    while (!q.empty()) {
        int u = q.front();
        q.pop();

        if (dist[u] > max_d) {
            max_d = dist[u];
            farthest_node = u;
        }

        for (int v : adj[u]) {
            if (dist[v] == -1) {
                dist[v] = dist[u] + 1;
                q.push(v);
            }
        }
    }
    return {farthest_node, max_d};
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    auto [u, d1] = bfs(1, n, adj);
    auto [v, d2] = bfs(u, n, adj);

    cout << u << " " << v << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Double-sweep BFS/DFS for tree diameter endpoint identification.
- **Reusable Pattern**: `Tree Diameter Endpoints: BFS(1) -> u, BFS(u) -> v; diameter endpoints are (u, v).`
