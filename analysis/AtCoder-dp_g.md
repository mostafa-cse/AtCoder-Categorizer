# Problem Analysis: AtCoder-dp_g — Longest Path

**Problem ID**: `AtCoder-dp_g`  
**Contest**: `dp` (Educational DP Contest)  
**Rating / Difficulty**: 1350  
**URL**: https://atcoder.jp/contests/dp/tasks/dp_g  
**VJudge Tag**: `[problem:AtCoder-dp_g]`  
**Category File**: [`../categories/dp/dp_on_trees.md`](../categories/dp/dp_on_trees.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Dp on Different Structures`  
- **Topic (Skill)**: `DP on Trees and DAGs`  

---

## 1. Problem Statement & Key Idea
Find the length of the longest directed path in a Directed Acyclic Graph (DAG) with N vertices and M edges.

**Core Idea**: Since the graph has no directed cycles, topological ordering exists. The longest path starting at u is dp[u] = 1 + max_{(u, v) in E} dp[v].

## 2. Core Observation & Invariant
Acyclic structure guarantees no circular dependencies. Memoized DFS evaluates each vertex and edge exactly once.

## 3. Step-by-Step Algorithm
1. Memoized DFS: memo[u] = -1.
2. DFS(u): if memo[u] != -1 return memo[u]. ans = 0. For each neighbor v: ans = max(ans, 1 + DFS(v)). memo[u] = ans.
3. Return max_{u} DFS(u).

## 4. Complexity Analysis
Time: O(V + E), Space: O(V + E).

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int dfs(int u, const vector<vector<int>>& adj, vector<int>& memo) {
    if (memo[u] != -1) return memo[u];
    int best = 0;
    for (int v : adj[u]) {
        best = max(best, 1 + dfs(v, adj, memo));
    }
    return memo[u] = best;
}

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

    vector<int> memo(n + 1, -1);
    int ans = 0;
    for (int i = 1; i <= n; ++i) {
        ans = max(ans, dfs(i, adj, memo));
    }

    cout << ans << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Topological sort DP on DAG.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Topological ordering as the fundamental validity condition for DAG DP.
- **Reusable Pattern**: `Memoized DFS transition over DAG edges.`

---
Back to [DP on Trees and DAGs](../categories/dp/dp_on_trees.md) | [Categories Directory](../categories/README.md)