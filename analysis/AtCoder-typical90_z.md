# Problem Analysis: AtCoder-typical90_z — Independent Set on a Tree

**Problem ID**: `AtCoder-typical90_z`  
**Contest**: `typical90` (Kyopro Typical 90, Problem 026)  
**Rating / Difficulty**: 1200 (★4)  
**URL**: https://atcoder.jp/contests/typical90/tasks/typical90_z  
**VJudge Tag**: `[problem:AtCoder-typical90_z]`  
**Category File**: [`../categories/graph_theory/bipartite_trees.md`](../categories/graph_theory/bipartite_trees.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Trees`  
- **Topic (Skill)**: `Bipartite 2-Coloring of Trees & Pigeonhole Independent Set`  

---

## 1. Problem Statement & Key Idea
Given a tree with N vertices (N even), find an independent set of size exactly N / 2.

**Core Idea**: Every tree is bipartite. 2-coloring vertices using BFS/DFS partitions vertices into two independent sets.

## 2. Core Observation & Invariant
By the Pigeonhole Principle, at least one of the two color classes must contain at least N / 2 vertices. Any subset of an independent set is independent; output any N/2 vertices from the larger class.

## 3. Step-by-Step Algorithm
1. Run BFS/DFS from vertex 1 to compute bipartite colors (0 and 1).
2. Group vertices by color: group0 and group1.
3. Take group with size >= N / 2.
4. Output first N / 2 vertices from that group.

## 4. Complexity Analysis
Time: O(N), Space: O(N).

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>

using namespace std;

void dfs(int u, int p, int c, const vector<vector<int>>& adj, vector<int>& color) {
    color[u] = c;
    for (int v : adj[u]) {
        if (v != p) {
            dfs(v, u, 1 - c, adj, color);
        }
    }
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

    vector<int> color(n + 1, 0);
    dfs(1, 0, 0, adj, color);

    vector<int> c0, c1;
    for (int i = 1; i <= n; ++i) {
        if (color[i] == 0) c0.push_back(i);
        else c1.push_back(i);
    }

    const vector<int>& chosen = (c0.size() >= c1.size()) ? c0 : c1;
    for (int i = 0; i < n / 2; ++i) {
        cout << chosen[i] << (i + 1 == n / 2 ? "" : " ");
    }
    cout << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Tree bipartiteness and pigeonhole principle independent set selection.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Bipartite coloring on trees and the pigeonhole principle for constructive subproblems.
- **Reusable Pattern**: `Bipartite 2-Coloring on Trees.`

---
Back to [Bipartite 2-Coloring of Trees & Pigeonhole Independent Set](../categories/graph_theory/bipartite_trees.md) | [Categories Directory](../categories/README.md)