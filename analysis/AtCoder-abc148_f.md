# Problem Analysis: AtCoder-abc148_f — Playing Tag on Tree

**Problem ID**: `AtCoder-abc148_f`  
**Contest**: `abc148`  
**Rating / Difficulty**: 1457  
**URL**: https://atcoder.jp/contests/abc148/tasks/abc148_f  
**VJudge Tag**: `[problem:AtCoder-abc148_f]`  
**Category File**: [`../categories/graph_theory/tree_bfs_evader_leaf_reachability.md`](../categories/graph_theory/tree_bfs_evader_leaf_reachability.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Trees`  
- **Topic (Skill)**: `Tree BFS Distances and Evader Leaf Reachability`  

---

## 1. Problem Statement & Key Idea
Takahashi (evader) starts at vertex u and Aoki (chaser) starts at vertex v in a tree with N vertices. Takahashi moves first. Takahashi wants to maximize the number of moves before being caught, Aoki wants to minimize it. Output the total number of moves Aoki makes before catching Takahashi.

**Key Insight**: Takahashi can safely reach any vertex x if and only if dist(u, x) < dist(v, x). Once at x, Takahashi can escape to the deepest subtree reachable before Aoki arrives, surviving until Aoki reaches that boundary.

## 2. Core Observation & Invariant
Since Aoki moves second, if Takahashi chooses to flee towards node x with dist(u, x) < dist(v, x), Aoki takes dist(v, x) steps to catch him. Takahashi survives dist(v, x) - 1 steps. The maximum surviving steps is max_{x: dist_u[x] < dist_v[x]} (dist_v[x] - 1).

## 3. Step-by-Step Algorithm
1. Compute dist_u[x] for all vertices using BFS from start u.
2. Compute dist_v[x] for all vertices using BFS from start v.
3. Initialize max_moves = 0.
4. For each vertex x from 1 to N:
5.   If dist_u[x] < dist_v[x]:
6.     max_moves = max(max_moves, dist_v[x] - 1).
7. Print max_moves.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

void bfs(int start, const vector<vector<int>>& adj, vector<int>& dist) {
    dist[start] = 0;
    queue<int> q;
    q.push(start);
    while (!q.empty()) {
        int u = q.front();
        q.pop();
        for (int v : adj[u]) {
            if (dist[v] == -1) {
                dist[v] = dist[u] + 1;
                q.push(v);
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, u, v;
    if (!(cin >> n >> u >> v)) return 0;

    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < n - 1; ++i) {
        int a, b;
        cin >> a >> b;
        adj[a].push_back(b);
        adj[b].push_back(a);
    }

    vector<int> dist_u(n + 1, -1), dist_v(n + 1, -1);
    bfs(u, adj, dist_u);
    bfs(v, adj, dist_v);

    int max_steps = 0;
    for (int i = 1; i <= n; ++i) {
        if (dist_u[i] < dist_v[i]) {
            max_steps = max(max_steps, dist_v[i] - 1);
        }
    }

    cout << max_steps << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Pursuit-evasion game distance inequality on trees.
- **Reusable Pattern**: `Tree Tag Game: max_{x: dist_evader(x) < dist_chaser(x)} (dist_chaser(x) - 1).`
