# Problem Analysis: AtCoder-abc138_d — Ki

**Problem ID**: `AtCoder-abc138_d`  
**Contest**: `abc138`  
**Rating / Difficulty**: 920  
**URL**: https://atcoder.jp/contests/abc138/tasks/abc138_d  
**VJudge Tag**: `[problem:AtCoder-abc138_d]`  
**Category File**: [`../categories/data_structures/tree_subtree_imos.md`](../categories/data_structures/tree_subtree_imos.md)  

- **Tag (Domain)**: `Data Structures`  
- **Subtopic**: `Trees & Difference Arrays`  
- **Topic (Skill)**: `Tree Subtree Imos / Prefix Sum DFS Propagation`  

---

## 1. Problem Statement & Key Idea
Given a tree rooted at vertex 1 with N vertices. Q queries add value x to all vertices in the subtree rooted at vertex p. Find the final values of all vertices.

**Key Idea**: Instead of modifying all subtree vertices for each query in O(N), place an increment +x at the root of the subtree val[p] += x (tree difference array / imos).

## 2. Core Observation & Invariant
Run a single DFS from root 1. The cumulative sum of values along the path from root 1 to vertex u gives the total additions applied to all ancestor subtrees containing u.

## 3. Step-by-Step Algorithm
1. Initialize tree adjacency list and val array of size N + 1 to 0.
2. For each query (p, x): val[p] += x.
3. Run DFS(u, parent): for each neighbor v != parent, val[v] += val[u], DFS(v, u).
4. Print val[1..N].

## 4. Complexity Analysis
- **Time Complexity**: `O(N + Q)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>

using namespace std;

void dfs(int u, int p, const vector<vector<int>>& adj, vector<long long>& val) {
    for (int v : adj[u]) {
        if (v != p) {
            val[v] += val[u];
            dfs(v, u, adj, val);
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    vector<long long> val(n + 1, 0);
    for (int i = 0; i < q; ++i) {
        int p;
        long long x;
        cin >> p >> x;
        val[p] += x;
    }

    dfs(1, 0, adj, val);

    for (int i = 1; i <= n; ++i) {
        cout << val[i] << (i == n ? '\n' : ' ');
    }

    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Subtree range updates via top-down prefix sum propagation on trees.
- **Reusable Pattern**: `Tree Imos: add at subtree root, propagate down in single DFS.`
