# Problem Analysis: AtCoder-arc116_e — Spread of Information

**Problem ID**: `AtCoder-arc116_e`  
**Contest**: `arc116`  
**Rating / Difficulty**: 2236  
**URL**: https://atcoder.jp/contests/arc116/tasks/arc116_e  
**VJudge Tag**: `[problem:AtCoder-arc116_e]`  
**Category File**: [`../categories/graph_theory/tree_dominating_set_binary_search_dfs_spread.md`](../categories/graph_theory/tree_dominating_set_binary_search_dfs_spread.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Graph Traversal`  
- **Topic (Skill)**: `Depth First Search (DFS)`  

---

## 1. Problem Statement & Key Idea
Find the minimum time T for information to spread to all vertices of a tree from at most K chosen source vertices.

## 2. Core Observation & Invariant
Binary search on the answer T in [1, N]. The decision problem asks whether all vertices can be covered by <= K centers of radius T (Tree T-Dominating Set). In a rooted tree, a bottom-up post-order DFS greedily covers vertices: each node tracks max uncovered distance d and min center distance c in its subtree. If c + d <= T, the deepest uncovered vertex is covered by an existing center (d = -inf). If d == T, no ancestor can cover this deepest vertex, forcing a center at the current node.

## 3. Step-by-Step Algorithm
1. 1. Binary search on time T in [1, N].
2. 2. To check feasibility for time T, run bottom-up DFS from root 1:
3.    - Initialize d = 0 (node itself uncovered) and c = INF.
4.    - Aggregate child returns: d = max(d, child_d + 1), c = min(c, child_c + 1).
5.    - If c + d <= T, set d = -INF (covered).
6.    - If d == T, place a center: increment center count, set c = 0, d = -INF.
7. 3. After DFS, if root has d >= 0, place an additional center at root.
8. 4. Feasible iff total centers <= K.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

static const int INF = 1e9;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    auto check = [&](int T) -> bool {
        int centers = 0;

        auto dfs = [&](auto& self, int u, int p) -> pair<int, int> {
            int d = 0; // max_uncovered distance
            int c = INF; // min_center distance

            for (int v : adj[u]) {
                if (v == p) continue;
                auto [dv, cv] = self(self, v, u);
                if (dv != -INF) {
                    d = max(d, dv + 1);
                }
                if (cv != INF) {
                    c = min(c, cv + 1);
                }
            }

            if (c + d <= T) {
                d = -INF;
            }

            if (d == T) {
                centers++;
                c = 0;
                d = -INF;
            }

            return {d, c};
        };

        auto [d_root, c_root] = dfs(dfs, 1, 0);
        if (d_root >= 0) {
            centers++;
        }

        return centers <= k;
    };

    int low = 1, high = n, ans = n;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (check(mid)) {
            ans = mid;
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }

    cout << ans << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
