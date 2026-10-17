# Problem Analysis: AtCoder-arc211_d — D. Two Signposts

**Problem ID**: `AtCoder-arc211_d`  
**Contest**: `arc211`  
**Rating / Difficulty**: 2301  
**URL**: https://atcoder.jp/contests/arc211/tasks/arc211_d  
**VJudge Tag**: `[problem:AtCoder-arc211_d]`  
**Category File**: [`../categories/graph_theory/dual_dfs_signpost_orientation.md`](../categories/graph_theory/dual_dfs_signpost_orientation.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Graph Traversal`  
- **Topic (Skill)**: `Topological Sorting`  

---

## 1. Problem Statement & Key Idea
Given an undirected graph of $N$ vertices and $M$ edges, place blue and yellow signposts at each vertex directed towards 1 and 2 respectively, such that following blue leads to 1, following yellow leads to 2, and no vertex has identical signpost orientations.

## 2. Core Observation & Invariant
A valid signpost orientation for each color forms a directed spanning tree rooted at that color's destination with no cycles, subject to the condition that no vertex points along the same directed edge in both trees.

## 3. Step-by-Step Algorithm
1. Construct the blue signposts by running DFS rooted at vertex 1, orienting edges towards the parent to establish a spanning tree directed to 1.
2. Construct yellow signposts via DFS rooted at vertex 2, enforcing the constraint that the yellow parent edge must not coincide with the blue parent edge.
3. If either DFS fails to visit all vertices, output No; otherwise, output the two valid parent pointer arrays.

## 4. Complexity Analysis
- **Time Complexity**: `O(N + M)`
- **Space Complexity**: `O(N + M)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    if (!(cin >> N >> M)) return 0;

    vector<vector<int>> adj(N + 1);
    for (int i = 0; i < M; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    vector<int> bpar(N + 1, 0), ypar(N + 1, 0);

    // Blue DFS from 1
    vector<bool> vis(N + 1, false);
    auto dfs_blue = [&](auto& self, int u) -> void {
        vis[u] = true;
        for (int v : adj[u]) {
            if (!vis[v]) {
                bpar[v] = u;
                self(self, v);
            }
        }
    };
    dfs_blue(dfs_blue, 1);

    // Yellow DFS from 2, avoiding bpar
    fill(vis.begin(), vis.end(), false);
    auto dfs_yellow = [&](auto& self, int u) -> void {
        vis[u] = true;
        for (int v : adj[u]) {
            if (!vis[v] && bpar[v] != u) {
                ypar[v] = u;
                self(self, v);
            }
        }
    };
    dfs_yellow(dfs_yellow, 2);

    for (int i = 1; i <= N; ++i) {
        if (i != 1 && bpar[i] == 0) {
            cout << "No\n";
            return 0;
        }
        if (i != 2 && ypar[i] == 0) {
            cout << "No\n";
            return 0;
        }
    }

    cout << "Yes\n";
    cout << ypar[1] << "\n";
    cout << bpar[2] << "\n";
    for (int i = 3; i <= N; ++i) {
        cout << bpar[i] << " " << ypar[i] << "\n";
    }
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
