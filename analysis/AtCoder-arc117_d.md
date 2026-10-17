# Problem Analysis: AtCoder-arc117_d — Miracle Tree

**Problem ID**: `AtCoder-arc117_d`  
**Contest**: `arc117`  
**Rating / Difficulty**: 2115  
**URL**: https://atcoder.jp/contests/arc117/tasks/arc117_d  
**VJudge Tag**: `[problem:AtCoder-arc117_d]`  
**Category File**: [`../categories/graph_theory/tree_diameter_euler_tour_labeling.md`](../categories/graph_theory/tree_diameter_euler_tour_labeling.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Graph Traversal`  
- **Topic (Skill)**: `Tree Diameter`  

---

## 1. Problem Statement & Key Idea
Given a tree T with N vertices, assign distinct positive integers E_v to all vertices such that |E_u - E_v| >= dist(u, v) for all pairs (u, v). Minimize the maximum label max_v E_v.

**Key Insight**: If we traverse the tree in an Euler tour stepping along edges and incrementing a global time counter at each step, any two vertices have label difference >= tree distance (by triangle inequality). A standard tour visits each edge twice (taking 2(N-1) steps). To minimize the maximum time without returning to the root, we save steps equal to the depth of the last visited leaf! To maximize this savings, the path from the root to the last visited leaf must be the tree diameter. We find the diameter endpoints S and T, root at S, and visit the diameter child last at each branching step.

## 2. Core Observation & Invariant
Euler tour traversal times naturally satisfy distance lower bounds |E_u - E_v| >= dist(u, v); visiting diameter endpoints first and last minimizes peak label.

## 3. Step-by-Step Algorithm
1. Find tree diameter endpoints S and T via two BFS/DFS passes.
2. Root tree at S and mark all edges along the path from S to T.
3. Run DFS starting at S: at each vertex u, visit non-diameter children first, and diameter child last.
4. Maintain global counter t starting at 1; assign E[u] = t upon first visit, incrementing t on each step and backtrack.
5. Output the resulting vertex labels E_1, ..., E_N.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. Core Skill & Reusable Pattern
- **Core Skill**: Tree diameter Euler tour traversal for optimal metric labeling.
- **Reusable Pattern**: Metric label assignment satisfying |E_u - E_v| >= dist(u, v) minimized via diameter-guided DFS Euler tour.

## 6. Editorial Comparison & Alternative Approaches
Matches official editorial.

## 7. Verified C++17 Implementation
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int n;
vector<vector<int>> adj;
vector<int> dist_node;

void dfs_dist(int u, int p, int d) {
    dist_node[u] = d;
    for (int v : adj[u]) {
        if (v != p) dfs_dist(v, u, d + 1);
    }
}

int get_farthest(int start) {
    dist_node.assign(n + 1, 0);
    dfs_dist(start, 0, 0);
    int best = start;
    for (int i = 1; i <= n; ++i) {
        if (dist_node[i] > dist_node[best]) best = i;
    }
    return best;
}

vector<bool> on_diam;

bool find_path(int u, int p, int target) {
    if (u == target) {
        on_diam[u] = true;
        return true;
    }
    for (int v : adj[u]) {
        if (v != p && find_path(v, u, target)) {
            on_diam[u] = true;
            return true;
        }
    }
    return false;
}

vector<int> E;
int cur_time = 1;

void dfs_euler(int u, int p) {
    E[u] = cur_time;
    vector<int> non_diam_children;
    int diam_child = -1;
    for (int v : adj[u]) {
        if (v == p) continue;
        if (on_diam[v]) diam_child = v;
        else non_diam_children.push_back(v);
    }

    for (int v : non_diam_children) {
        cur_time++;
        dfs_euler(v, u);
        cur_time++;
    }

    if (diam_child != -1) {
        cur_time++;
        dfs_euler(diam_child, u);
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n)) return 0;

    adj.assign(n + 1, vector<int>());
    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    int S = get_farthest(1);
    int T = get_farthest(S);

    on_diam.assign(n + 1, false);
    find_path(S, 0, T);

    E.assign(n + 1, 0);
    dfs_euler(S, 0);

    for (int i = 1; i <= n; ++i) {
        cout << E[i] << (i == n ? "" : " ");
    }
    cout << "\n";

    return 0;
}
```
