# Problem Analysis: AtCoder-typical90_am — Tree Distance

**Problem ID**: `AtCoder-typical90_am`  
**Contest**: `typical90` (Kyopro Typical 90, Problem 039)  
**Rating / Difficulty**: 1500 (★5)  
**URL**: https://atcoder.jp/contests/typical90/tasks/typical90_am  
**VJudge Tag**: `[problem:AtCoder-typical90_am]`  
**Category File**: [`../categories/graph_theory/tree_distance_contribution.md`](../categories/graph_theory/tree_distance_contribution.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Trees`  
- **Topic (Skill)**: `Contribution to the Sum / Edge Subtree Size Multiplication`  

---

## 1. Problem Statement & Key Idea
Given a tree with N vertices, compute the sum of distances between all N*(N - 1)/2 pairs of vertices: sum_{1 <= u < v <= N} dist(u, v).

**Core Idea**: Contribution to the Sum: Invert the problem from summing across pairs to summing across edges.

## 2. Core Observation & Invariant
Removing an edge e partitions the tree into two subtrees of sizes sz and N - sz. Exactly sz * (N - sz) paths must cross edge e! The total sum of distances is sum_{e} (sz_e * (N - sz_e)).

## 3. Step-by-Step Algorithm
1. Run DFS from vertex 1 to calculate subtree sizes sz[u].
2. For each node u != 1: the edge to parent has contribution sz[u] * (N - sz[u]).
3. Sum contributions across all N - 1 edges.

## 4. Complexity Analysis
Time: O(N), Space: O(N).

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>

using namespace std;

long long total_dist_sum = 0;
int n;

int dfs(int u, int p, const vector<vector<int>>& adj) {
    int sz = 1;
    for (int v : adj[u]) {
        if (v != p) {
            int child_sz = dfs(v, u, adj);
            total_dist_sum += (long long)child_sz * (n - child_sz);
            sz += child_sz;
        }
    }
    return sz;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n)) return 0;

    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    dfs(1, 0, adj);

    cout << total_dist_sum << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Linear-time all-pairs tree distance via edge contribution.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Contribution to the Sum principle and tree bipartition counts per edge.
- **Reusable Pattern**: `Edge Contribution to All-Pairs Tree Distance.`

---
Back to [Contribution to the Sum / Edge Subtree Size Multiplication](../categories/graph_theory/tree_distance_contribution.md) | [Categories Directory](../categories/README.md)