# Problem Analysis: AtCoder-arc103_d — F - Distance Sums on a Tree

**Problem ID**: `AtCoder-arc103_d`  
**Contest**: `arc103`  
**Rating / Difficulty**: 2836  
**URL**: https://atcoder.jp/contests/arc103/tasks/arc103_d  
**VJudge Tag**: `[problem:AtCoder-arc103_d]`  
**Category File**: [`../categories/graph_theory/tree_reconstruction_distance_sum_centroid_greedy.md`](../categories/graph_theory/tree_reconstruction_distance_sum_centroid_greedy.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `More Tree Stuff`  
- **Topic (Skill)**: `Rerooting Technique`  

---

## 1. Problem Statement & Key Idea
Given N distinct integers D_1, ..., D_N representing the sum of tree distances from each vertex to all other vertices, reconstruct the tree or determine that none exists.

## 2. Core Observation & Invariant
By tree distance properties, moving across edge (u, v) changes the distance sum by D(u) - D(v) = N - 2 * sz(u), where sz(u) is the subtree size of u directed away from v. The vertex with the maximum D_u must be a leaf (sz(u) = 1). Its parent v must uniquely have D(v) = D(u) - (N - 2 * sz(u)). Processing vertices in descending order of D greedily identifies each parent, accumulating subtree sizes. Finally, verifying the distance sum of the centroid/root on the reconstructed tree confirms correctness.

## 3. Step-by-Step Algorithm
1. 1. Map each D_i to vertex id i, and sort vertices in descending order of D_i.
2. 2. Initialize subtree size sz[u] = 1 for all vertices.
3. 3. For each vertex u from largest to second smallest D:
4.    a. Target parent distance is target_D = D[u] - (N - 2 * sz[u]).
5.    b. Look up target_D in hash map. If not found or v == u, return -1.
6.    c. Add edge (u, v) and update sz[v] += sz[u].
7. 4. Verify that root (minimum D) has sz[root] == N.
8. 5. Run BFS from root to compute actual distance sum and verify it matches D[root].
9. 6. Print the N-1 edges if valid, else -1.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <queue>

using namespace std;

typedef long long ll;

struct Vertex {
    ll d;
    int id;
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<Vertex> items(n);
    map<ll, int> d_to_id;
    for (int i = 0; i < n; ++i) {
        cin >> items[i].d;
        items[i].id = i + 1;
        d_to_id[items[i].d] = i + 1;
    }

    sort(items.begin(), items.end(), [](const Vertex& a, const Vertex& b) {
        return a.d > b.d;
    });

    vector<ll> sz(n + 1, 1);
    vector<pair<int, int>> edges;

    for (int i = 0; i < n - 1; ++i) {
        ll val = items[i].d;
        int u = items[i].id;
        ll s_u = sz[u];
        ll target_d = val - (n - 2 * s_u);

        auto it = d_to_id.find(target_d);
        if (it == d_to_id.end()) {
            cout << -1 << "\n";
            return 0;
        }
        int v = it->second;
        if (v == u) {
            cout << -1 << "\n";
            return 0;
        }
        edges.push_back({u, v});
        sz[v] += s_u;
    }

    int root = items.back().id;
    if (sz[root] != n) {
        cout << -1 << "\n";
        return 0;
    }

    // Verify distance sum from root
    vector<vector<int>> adj(n + 1);
    for (const auto& e : edges) {
        adj[e.first].push_back(e.second);
        adj[e.second].push_back(e.first);
    }

    vector<int> dist(n + 1, -1);
    dist[root] = 0;
    queue<int> q;
    q.push(root);

    ll actual_sum = 0;
    int visited_count = 0;

    while (!q.empty()) {
        int curr = q.front();
        q.pop();
        visited_count++;
        actual_sum += dist[curr];

        for (int nxt : adj[curr]) {
            if (dist[nxt] == -1) {
                dist[nxt] = dist[curr] + 1;
                q.push(nxt);
            }
        }
    }

    if (visited_count != n || actual_sum != items.back().d) {
        cout << -1 << "\n";
        return 0;
    }

    for (const auto& e : edges) {
        cout << e.first << " " << e.second << "\n";
    }
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
