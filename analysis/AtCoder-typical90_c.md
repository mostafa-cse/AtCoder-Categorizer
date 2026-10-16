# Problem Analysis: AtCoder-typical90_c — Longest Circular Road

**Problem ID**: `AtCoder-typical90_c`  
**Contest**: `typical90` (Kyopro Typical 90, Problem 003)  
**Rating / Difficulty**: 1100 (★4)  
**URL**: https://atcoder.jp/contests/typical90/tasks/typical90_c  
**VJudge Tag**: `[problem:AtCoder-typical90_c]`  
**Category File**: [`../categories/graph_theory/tree_diameter.md`](../categories/graph_theory/tree_diameter.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Trees`  
- **Topic (Skill)**: `Tree Diameter / Double BFS-DFS`  

---

## 1. Problem Statement & Key Idea
Given a tree with N vertices, add exactly one new road between any two vertices u and v to form a cycle of maximum possible length. Output the maximum cycle length.

**Core Idea**: Adding edge (u, v) creates a cycle of length dist(u, v) + 1. Maximizing cycle length is identical to maximizing distance dist(u, v) in a tree (Tree Diameter).

## 2. Core Observation & Invariant
From any arbitrary start node, the farthest node u is guaranteed to be an endpoint of a tree diameter. A second BFS from u finds the farthest node v, yielding exact diameter D = dist(u, v).

## 3. Step-by-Step Algorithm
1. Run BFS from node 1; find node u with maximum distance.
2. Run BFS from node u; find maximum distance D = dist(u, v).
3. Result is D + 1.

## 4. Complexity Analysis
Time: O(N), Space: O(N).

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

pair<int, int> bfs(int start, const vector<vector<int>>& adj, int n) {
    vector<int> dist(n + 1, -1);
    queue<int> q;
    q.push(start);
    dist[start] = 0;
    int farthest = start;

    while (!q.empty()) {
        int u = q.front();
        q.pop();

        if (dist[u] > dist[farthest]) {
            farthest = u;
        }

        for (int v : adj[u]) {
            if (dist[v] == -1) {
                dist[v] = dist[u] + 1;
                q.push(v);
            }
        }
    }
    return {farthest, dist[farthest]};
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

    auto [u, _] = bfs(1, adj, n);
    auto [v, diameter] = bfs(u, adj, n);

    cout << diameter + 1 << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Tree diameter reduction and double BFS proof.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Tree diameter characterization, cycle maximization reduction, and 2-pass BFS/DFS algorithm.
- **Reusable Pattern**: `2-Pass BFS Tree Diameter.`

---
Back to [Tree Diameter / Double BFS-DFS](../categories/graph_theory/tree_diameter.md) | [Categories Directory](../categories/README.md)