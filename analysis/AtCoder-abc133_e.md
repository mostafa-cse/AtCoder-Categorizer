# Problem Analysis: AtCoder-abc133_e — Virus Tree 2

**Problem ID**: `AtCoder-abc133_e`  
**Contest**: `abc133`  
**Rating / Difficulty**: 1505  
**URL**: https://atcoder.jp/contests/abc133/tasks/abc133_e  
**VJudge Tag**: `[problem:AtCoder-abc133_e]`  
**Category File**: [`../categories/combinatorics/distance2_tree_coloring.md`](../categories/combinatorics/distance2_tree_coloring.md)  

- **Tag (Domain)**: `Combinatorics`  
- **Subtopic**: `Tree Combinatorics`  
- **Topic (Skill)**: `Distance-2 Tree Coloring Combinatorics via DFS`  

---

## 1. Problem Statement & Key Idea
Given a tree with N vertices and K colors. Find the number of ways to color the vertices such that no two vertices at distance <= 2 share the same color, modulo 10^9 + 7.

**Key Insight**: Root the tree at vertex 1 and traverse top-down. The root has K choices. Its children have (K - 1), (K - 2), etc. For any deeper vertex v, its parent, grandparent, and already-colored siblings forbid colors, leaving K - 2 - (sibling index) choices.

## 2. Core Observation & Invariant
For each node v, if v is root: K choices. For root's children: (K - 1), (K - 2), etc. For any child of a non-root vertex: 2 colors are used by ancestors (parent and grandparent). If the node has c children, the number of ways to color them is P(K - 2, c) = (K - 2) * (K - 3) * ... * (K - 2 - c + 1).

## 3. Step-by-Step Algorithm
1. Root tree at 1 and run DFS.
2. ans = K.
3. For each vertex u:
4.   Let children_count = count of children of u.
5.   available_colors = (u == 1 ? K - 1 : K - 2).
6.   For i = 0 to children_count - 1:
7.     choices = available_colors - i.
8.     If choices <= 0, return 0.
9.     ans = (ans * choices) % MOD.
10. Print ans.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 1000000007;

long long ans = 1;
int K;

void dfs(int u, int p, const vector<vector<int>>& adj) {
    int available = (u == 1 ? K - 1 : K - 2);
    int used = 0;

    for (int v : adj[u]) {
        if (v != p) {
            long long choices = available - used;
            if (choices <= 0) {
                ans = 0;
                return;
            }
            ans = (ans * choices) % MOD;
            used++;
            dfs(v, u, adj);
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n >> K)) return 0;

    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    ans = K;
    dfs(1, 0, adj);

    cout << ans << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Top-down tree traversal with local conflict counting for distance-constrained graph coloring.
- **Reusable Pattern**: `Distance-2 Tree Coloring: root has K, root children have P(K-1, c), others have P(K-2, c).`
