# Problem Analysis: AtCoder-arc028_3 — 高橋王国の分割統治

**Problem ID**: `AtCoder-arc028_3`  
**Contest**: `arc028`  
**Rating / Difficulty**: 1748  
**URL**: https://atcoder.jp/contests/arc028/tasks/arc028_3  
**VJudge Tag**: `[problem:AtCoder-arc028_3]`  
**Category File**: [`../categories/graph_theory/tree_node_removal_max_component.md`](../categories/graph_theory/tree_node_removal_max_component.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Trees`  
- **Topic (Skill)**: `Tree Node Removal Max-Component Decomposition / Centroid Prerequisite`  

---

## 1. Problem Statement & Key Idea
Given a tree of N vertices. For each vertex i in 0 to N - 1, find the maximum size of a connected component formed when vertex i is removed from the tree.

**Key Insight**: When vertex u is removed, the remaining tree decomposes into components formed by its child subtrees in the DFS tree (each of size sz[v]) and the component containing its parent (of size N - sz[u]).

## 2. Core Observation & Invariant
Max component size upon removing u is max(N - sz[u], max_{v in children(u)} sz[v]). A single O(N) post-order DFS computes this for all vertices simultaneously.

## 3. Step-by-Step Algorithm
1. Root tree at vertex 0.
2. Run post-order DFS:
3.   sz[u] = 1.
4.   max_child = 0.
5.   For each child v of u:
6.     dfs(v, u).
7.     sz[u] += sz[v].
8.     max_child = max(max_child, sz[v]).
9.   ans[u] = max(N - sz[u], max_child).
10. Print ans[0..N-1].

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int n;
vector<vector<int>> adj;
vector<int> sz;
vector<int> ans;

void dfs(int u, int p) {
    sz[u] = 1;
    int max_c = 0;

    for (int v : adj[u]) {
        if (v != p) {
            dfs(v, u);
            sz[u] += sz[v];
            max_c = max(max_c, sz[v]);
        }
    }

    ans[u] = max(n - sz[u], max_c);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n)) return 0;

    adj.assign(n, vector<int>());
    sz.assign(n, 0);
    ans.assign(n, 0);

    for (int i = 1; i < n; ++i) {
        int p;
        cin >> p;
        adj[p].push_back(i);
        adj[i].push_back(p);
    }

    dfs(0, -1);

    for (int i = 0; i < n; ++i) {
        cout << ans[i] << "\n";
    }

    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Computing maximum connected component sizes under vertex deletion (tree centroid analysis).
- **Reusable Pattern**: `Tree Vertex Removal Components: ans[u] = max(N - sz[u], max_v sz[v]).`
