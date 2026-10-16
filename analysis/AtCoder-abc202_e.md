# Problem Analysis: AtCoder-abc202_e — Count Descendants

**Problem ID**: `AtCoder-abc202_e`  
**Contest**: `abc202`  
**Rating / Difficulty**: 1638  
**URL**: https://atcoder.jp/contests/abc202/tasks/abc202_e  
**VJudge Tag**: `[problem:AtCoder-abc202_e]`  
**Category File**: [`../categories/graph_theory/euler_tour_depth_binary_search.md`](../categories/graph_theory/euler_tour_depth_binary_search.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Trees`  
- **Topic (Skill)**: `Euler Tour Subtree Range Query + Depth Coordinate Binary Search`  

---

## 1. Problem Statement & Key Idea
Given a rooted tree with N vertices (root = 1). Answer Q queries (u, d): count the number of vertices v such that v is a descendant of u and depth(v) == d.

**Key Insight**: Flatten the tree using an Euler tour. A vertex v is in the subtree of u iff in[u] <= in[v] < out[u]. For each depth d, store all in[v] of vertices at depth d in sorted order.

## 2. Core Observation & Invariant
The query (u, d) asks for the number of elements in the sorted list depth_in[d] that fall into the interval [in[u], out[u]). This is answered in O(log N) using std::lower_bound and std::upper_bound.

## 3. Step-by-Step Algorithm
1. Run DFS from root 1: assign in[u], out[u], and depth[u].
2. Insert in[u] into list depth_list[depth[u]].
3. For each query (u, d):
4.   Query range is [in[u], out[u]).
5.   ans = lower_bound(depth_list[d], out[u]) - lower_bound(depth_list[d], in[u]).
6.   Print ans.

## 4. Complexity Analysis
- **Time Complexity**: `O((N + Q) log N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<vector<int>> adj;
vector<int> tin, tout, depth;
vector<vector<int>> depth_nodes;
int timer_cnt = 0;

void dfs(int u, int p, int d) {
    depth[u] = d;
    tin[u] = ++timer_cnt;
    depth_nodes[d].push_back(tin[u]);

    for (int v : adj[u]) {
        if (v != p) {
            dfs(v, u, d + 1);
        }
    }
    tout[u] = timer_cnt;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    adj.resize(n + 1);
    tin.resize(n + 1);
    tout.resize(n + 1);
    depth.resize(n + 1);
    depth_nodes.resize(n + 1);

    for (int i = 2; i <= n; ++i) {
        int p;
        cin >> p;
        adj[p].push_back(i);
    }

    dfs(1, 0, 0);

    int q;
    cin >> q;
    while (q--) {
        int u, d;
        cin >> u >> d;
        if (d >= (int)depth_nodes.size()) {
            cout << 0 << "\n";
            continue;
        }

        const auto& vec = depth_nodes[d];
        auto it1 = lower_bound(vec.begin(), vec.end(), tin[u]);
        auto it2 = upper_bound(vec.begin(), vec.end(), tout[u]);
        cout << (it2 - it1) << "\n";
    }

    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Combining Euler Tour flattened subtree intervals with depth-bucketed binary search.
- **Reusable Pattern**: `Subtree Descendants at Depth D: in[u] <= in[v] < out[u] queried on depth_in[d] via binary search.`
