# Problem Analysis: AtCoder-agc024_d — D. Isomorphism Freak

**Problem ID**: `AtCoder-agc024_d`  
**Contest**: `agc024`  
**Rating / Difficulty**: 2307  
**URL**: https://atcoder.jp/contests/agc024/tasks/agc024_d  
**VJudge Tag**: `[problem:AtCoder-agc024_d]`  
**Category File**: [`../categories/miscellaneous/tree_isomorphism_center_leaf_minimization.md`](../categories/miscellaneous/tree_isomorphism_center_leaf_minimization.md)  

- **Tag (Domain)**: `Miscellaneous`  
- **Subtopic**: `General`  
- **Topic (Skill)**: `Tree Isomorphism`  

---

## 1. Problem Statement & Key Idea
Expand a tree $G$ by adding leaves so that all vertices in each color class have isomorphic rooted trees. Minimize colorfulness, and secondarily minimize the number of leaves.

## 2. Core Observation & Invariant
A tree with minimum colorfulness must be completely symmetric with respect to either a central vertex (giving radius $D$, colorfulness $D+1$) or a central edge (giving radius $D$, colorfulness $D+1$).

## 3. Step-by-Step Algorithm
1. Iterate over all $N$ vertices as candidate centers, calculating maximum depth and maximum branch degrees at each distance level.
2. Iterate over all $N-1$ edges as candidate bicenters, rooting two symmetrical halves across the central bridge.
3. Minimize colorfulness first, and among ties minimize total leaf count $\prod \max(\text{degrees})$ in $O(N^2)$ time.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

int N;
vector<vector<int>> adj;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> N)) return 0;
    adj.assign(N + 1, vector<int>());
    vector<pair<int, int>> edges;
    for (int i = 0; i < N - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
        edges.push_back({u, v});
    }

    int best_color = 1e9;
    long long best_leaves = -1;

    auto update = [&](int col, long long lvs) {
        if (col < best_color) {
            best_color = col;
            best_leaves = lvs;
        } else if (col == best_color) {
            if (best_leaves == -1 || lvs < best_leaves) {
                best_leaves = lvs;
            }
        }
    };

    // Option 1: Vertex center
    for (int r = 1; r <= N; ++r) {
        vector<int> dist(N + 1, -1);
        vector<int> parent(N + 1, 0);
        queue<int> q;
        q.push(r);
        dist[r] = 0;
        int max_d = 0;
        while (!q.empty()) {
            int u = q.front();
            q.pop();
            max_d = max(max_d, dist[u]);
            for (int v : adj[u]) {
                if (dist[v] == -1) {
                    dist[v] = dist[u] + 1;
                    parent[v] = u;
                    q.push(v);
                }
            }
        }

        int col = max_d + 1;
        vector<int> max_c(max_d, 0);
        for (int u = 1; u <= N; ++u) {
            int d = dist[u];
            if (d < max_d) {
                int ch = 0;
                for (int v : adj[u]) {
                    if (parent[v] == u) ch++;
                }
                max_c[d] = max(max_c[d], ch);
            }
        }

        long long leaves = 1;
        for (int d = 0; d < max_d; ++d) {
            leaves *= max(1, max_c[d]);
        }
        update(col, leaves);
    }

    // Option 2: Edge center
    for (auto edge : edges) {
        int u = edge.first;
        int v = edge.second;

        vector<int> dist(N + 1, -1);
        vector<int> parent(N + 1, 0);
        queue<int> q;
        q.push(u);
        dist[u] = 0;
        parent[u] = -1;

        q.push(v);
        dist[v] = 0;
        parent[v] = -1;

        int max_d = 0;
        while (!q.empty()) {
            int curr = q.front();
            q.pop();
            max_d = max(max_d, dist[curr]);
            for (int nxt : adj[curr]) {
                if ((curr == u && nxt == v) || (curr == v && nxt == u)) continue;
                if (dist[nxt] == -1) {
                    dist[nxt] = dist[curr] + 1;
                    parent[nxt] = curr;
                    q.push(nxt);
                }
            }
        }

        int col = max_d + 1;
        vector<int> max_c(max_d, 0);
        for (int node = 1; node <= N; ++node) {
            int d = dist[node];
            if (d < max_d) {
                int ch = 0;
                for (int nxt : adj[node]) {
                    if (parent[nxt] == node) ch++;
                }
                max_c[d] = max(max_c[d], ch);
            }
        }

        long long leaves = 2;
        for (int d = 0; d < max_d; ++d) {
            leaves *= max(1, max_c[d]);
        }
        update(col, leaves);
    }

    cout << best_color << " " << best_leaves << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
