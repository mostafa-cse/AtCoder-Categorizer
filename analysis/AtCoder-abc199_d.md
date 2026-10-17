# Problem Analysis: AtCoder-abc199_d — RGB Coloring 2

**Problem ID**: `AtCoder-abc199_d`  
**Contest**: `abc199`  
**Rating / Difficulty**: 1804  
**URL**: https://atcoder.jp/contests/abc199/tasks/abc199_d  
**VJudge Tag**: `[problem:AtCoder-abc199_d]`  
**Category File**: [`../categories/basics/dfs_tree_backtracking_3coloring.md`](../categories/basics/dfs_tree_backtracking_3coloring.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Backtracking / DFS Tree`  
- **Topic (Skill)**: `DFS Tree Order Backtracking on Small-Graph 3-Coloring with Root Symmetry`  

---

## 1. Problem Statement & Key Idea
Given a simple undirected graph with N vertices (N <= 20) and M edges. Color each vertex Red, Green, or Blue such that no two adjacent vertices have the same color. Count the number of valid colorings.

**Key Insight**: The graph splits into connected components. For each component, build a DFS tree. Fix the root's color to 0 (multiply result by 3 by symmetry). Backtrack through vertices in DFS preorder: each vertex has at most 2 valid colors (different from its parent), reducing search states to at most 2^{N-1} <= 2^{19} ~ 5 * 10^5.

## 2. Core Observation & Invariant
Product of ways over all connected components gives the total valid colorings.

## 3. Step-by-Step Algorithm
1. Find connected components.
2. For each component, run DFS to obtain visiting order.
3. Fix root color = 0.
4. Backtrack through remaining vertices in DFS order: try colors in {0, 1, 2} not matching any colored neighbor.
5. Component ways = 3 * backtrack_ways.
6. Total answer is product of ways over all components.

## 4. Complexity Analysis
- **Time Complexity**: `O(3 * 2^N)`
- **Space Complexity**: `O(N + M)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>

using namespace std;

int n, m;
vector<vector<int>> adj;
vector<bool> visited;
vector<int> comp_order;
vector<int> color;

void get_dfs_order(int u) {
    visited[u] = true;
    comp_order.push_back(u);
    for (int v : adj[u]) {
        if (!visited[v]) get_dfs_order(v);
    }
}

long long dfs_color(int idx) {
    if (idx == (int)comp_order.size()) return 1;

    int u = comp_order[idx];
    long long ways = 0;

    for (int c = 0; c < 3; ++c) {
        bool ok = true;
        for (int v : adj[u]) {
            if (color[v] == c) {
                ok = false;
                break;
            }
        }
        if (ok) {
            color[u] = c;
            ways += dfs_color(idx + 1);
            color[u] = -1;
        }
    }

    return ways;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n >> m)) return 0;

    adj.assign(n, vector<int>());
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        --u; --v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    visited.assign(n, false);
    color.assign(n, -1);
    long long total_ans = 1;

    for (int i = 0; i < n; ++i) {
        if (!visited[i]) {
            comp_order.clear();
            get_dfs_order(i);

            color[comp_order[0]] = 0;
            long long comp_ways = 3LL * dfs_color(1);
            color[comp_order[0]] = -1;

            total_ans *= comp_ways;
        }
    }

    cout << total_ans << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Pruning small-graph 3-coloring backtracking using DFS tree hierarchy and root rotational symmetry.
- **Reusable Pattern**: `Small Graph 3-Coloring: Fix root color * 3 + backtrack in DFS tree traversal order.`
