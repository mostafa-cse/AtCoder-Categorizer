# Problem Analysis: AtCoder-apc001_e — E. Antennas on Tree

**Problem ID**: `AtCoder-apc001_e`  
**Contest**: `apc001`  
**Rating / Difficulty**: 2167  
**URL**: https://atcoder.jp/contests/apc001/tasks/apc001_e  
**VJudge Tag**: `[problem:AtCoder-apc001_e]`  
**Category File**: [`../categories/dp/metric_dimension_tree_dp_high_degree_root.md`](../categories/dp/metric_dimension_tree_dp_high_degree_root.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Dp on Different Structures`  
- **Topic (Skill)**: `DP on Trees and DAGs`  

---

## 1. Problem Statement & Key Idea
Determine the minimum number of antennas required to uniquely identify any invaded vertex on a tree. Removing any vertex v with degree k must leave at least k - 1 connected components containing at least one antenna. If max degree <= 2, the tree is a path (answer 1). Otherwise, root the tree at any vertex of degree >= 3 and solve via simple bottom-up Tree DP.

## 2. Core Observation & Invariant
Rooting at a vertex r of degree >= 3 guarantees that for every vertex u != r, the parent component already contains an antenna. Thus, for every node u, at most one child subtree can have 0 antennas. For leaf u, f(u) = 0. For internal node u with z children having f(v) = 0, f(u) = sum(f(v)) + max(0, z - 1). The answer is f(r).

## 3. Step-by-Step Algorithm
1. If N <= 2 or max degree <= 2, output 1.
2. Locate any vertex root with degree >= 3.
3. Perform DFS from root: for each child v of u, compute res = dfs(v). Accumulate sum s += res and count zeros z += (res == 0).
4. For a leaf (no children), return 0. For internal node, return s + max(0, z - 1).
5. Return and print dfs(root, -1).

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    if (!(cin >> N)) return 0;

    if (N <= 2) {
        cout << 1 << "\n";
        return 0;
    }

    vector<vector<int>> adj(N);
    for (int i = 0; i < N - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    int root = -1;
    for (int i = 0; i < N; ++i) {
        if ((int)adj[i].size() >= 3) {
            root = i;
            break;
        }
    }

    if (root == -1) {
        cout << 1 << "\n";
        return 0;
    }

    auto dfs = [&](auto& self, int u, int p) -> int {
        int s = 0, z = 0;
        bool is_leaf = true;
        for (int v : adj[u]) {
            if (v != p) {
                is_leaf = false;
                int res = self(self, v, u);
                s += res;
                if (res == 0) z++;
            }
        }
        if (is_leaf) return 0;
        return s + max(0, z - 1);
    };

    cout << dfs(dfs, root, -1) << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
