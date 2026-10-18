# Problem Analysis: AtCoder-abc374_g — G. Only One Product Name

**Problem ID**: `AtCoder-abc374_g`  
**Contest**: `abc374`  
**Rating / Difficulty**: 2608  
**URL**: https://atcoder.jp/contests/abc374/tasks/abc374_g  
**VJudge Tag**: `[problem:AtCoder-abc374_g]`  
**Category File**: [`../categories/graph_theory/only_one_product_name_bipartite_matching.md`](../categories/graph_theory/only_one_product_name_bipartite_matching.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Matching`  
- **Topic (Skill)**: `Bipartite Matching (HopCroft Karp Algorithm and Kuhn's Algorithm)`  

---

## 1. Problem Statement & Key Idea
Given N 2-letter uppercase product names, construct the minimum number of strings such that each product appears as a substring, and no unused length-2 substring is formed.

## 2. Core Observation & Invariant
Model products as vertices in a directed graph G, with an edge u -> v if the 2nd character of u equals the 1st character of v. Strings in the NG list correspond to directed walks. Compacting G into its SCC condensation DAG G', the problem reduces to finding the minimum path cover on G'. By Dilworth's theorem, minimum path cover equals V' - max_bipartite_matching.

## 3. Step-by-Step Algorithm
1. Find SCCs of G using Kosaraju's algorithm.
2. Build reachability DAG G' using Floyd-Warshall transitive closure.
3. Construct bipartite graph of SCCs and compute maximum bipartite matching with Kuhn's algorithm. Output num_scc - matching.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^3)`
- **Space Complexity**: `O(N^2)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    if (!(cin >> N)) return 0;

    vector<string> S(N);
    for (int i = 0; i < N; ++i) {
        cin >> S[i];
    }

    vector<vector<int>> adj(N), radj(N);
    for (int u = 0; u < N; ++u) {
        for (int v = 0; v < N; ++v) {
            if (S[u][1] == S[v][0]) {
                adj[u].push_back(v);
                radj[v].push_back(u);
            }
        }
    }

    vector<bool> visited(N, false);
    vector<int> order;

    auto dfs1 = [&](auto& self, int u) -> void {
        visited[u] = true;
        for (int v : adj[u]) {
            if (!visited[v]) self(self, v);
        }
        order.push_back(u);
    };

    for (int i = 0; i < N; ++i) {
        if (!visited[i]) dfs1(dfs1, i);
    }

    vector<int> scc_id(N, -1);
    int num_scc = 0;

    auto dfs2 = [&](auto& self, int u, int cid) -> void {
        scc_id[u] = cid;
        for (int v : radj[u]) {
            if (scc_id[v] == -1) self(self, v, cid);
        }
    };

    for (int i = N - 1; i >= 0; --i) {
        int u = order[i];
        if (scc_id[u] == -1) {
            dfs2(dfs2, u, num_scc++);
        }
    }

    vector<vector<bool>> reach(num_scc, vector<bool>(num_scc, false));
    for (int u = 0; u < N; ++u) {
        for (int v : adj[u]) {
            int cu = scc_id[u], cv = scc_id[v];
            if (cu != cv) reach[cu][cv] = true;
        }
    }

    // Transitive closure (Warshall)
    for (int k = 0; k < num_scc; ++k) {
        for (int i = 0; i < num_scc; ++i) {
            if (reach[i][k]) {
                for (int j = 0; j < num_scc; ++j) {
                    if (reach[k][j]) reach[i][j] = true;
                }
            }
        }
    }

    // Maximum bipartite matching
    vector<int> match_to(num_scc, -1);
    vector<bool> vis(num_scc, false);

    auto dfs_match = [&](auto& self, int u) -> bool {
        for (int v = 0; v < num_scc; ++v) {
            if (reach[u][v] && !vis[v]) {
                vis[v] = true;
                if (match_to[v] == -1 || self(self, match_to[v])) {
                    match_to[v] = u;
                    return true;
                }
            }
        }
        return false;
    };

    int matching = 0;
    for (int u = 0; u < num_scc; ++u) {
        fill(vis.begin(), vis.end(), false);
        if (dfs_match(dfs_match, u)) {
            matching++;
        }
    }

    cout << (num_scc - matching) << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
