# Problem Analysis: AtCoder-abc319_g — G. Counting Shortest Paths

**Problem ID**: `AtCoder-abc319_g`  
**Contest**: `abc319`  
**Rating / Difficulty**: 2185  
**URL**: https://atcoder.jp/contests/abc319/tasks/abc319_g  
**VJudge Tag**: `[problem:AtCoder-abc319_g]`  
**Category File**: [`../categories/graph_theory/complement_graph_bfs_layered_shortest_path_counting.md`](../categories/graph_theory/complement_graph_bfs_layered_shortest_path_counting.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Graph Traversal`  
- **Topic (Skill)**: `Breadth First Search (BFS)`  

---

## 1. Problem Statement & Key Idea
Given a complete graph with N vertices from which M edges are deleted, find the number of shortest paths from 1 to N modulo 998244353. Complement-graph BFS finds distance layers, and layer DP counts paths by subtracting deleted edge transitions.

## 2. Core Observation & Invariant
Explicitly representing the complement graph takes O(N^2) time. Maintaining unvisited vertices in an std::set allows finding all unvisited non-deleted neighbors of u in O((deg_del(u) + 1) log N) time, totaling O((N + M) log N) for the BFS. In the resulting DAG of shortest paths, dp[v] = sum_{u in L_{d-1}} dp[u] - sum_{u in L_{d-1}, (u, v) in E_del} dp[u], computable in O(N + M) time.

## 3. Step-by-Step Algorithm
1. Sort deleted adjacency lists for each vertex.
2. Initialize unvisited set with {2..N}. Run BFS from vertex 1: for each popped node u, find unvisited nodes in intervals between consecutive deleted neighbors using upper_bound, set their dist to dist[u] + 1, enqueue, and erase from unvisited set.
3. If dist[N] == -1, output -1.
4. Group vertices into layers L_0, L_1, ..., L_D by distance.
5. Initialize dp[1] = 1. For each layer d from 1 to D: compute S_{d-1} = sum_{u in L_{d-1}} dp[u] mod MOD. For each v in L_d, set dp[v] = (S_{d-1} - sum_{(u, v) in E_del, dist[u] == d-1} dp[u]) mod MOD.
6. Output dp[N].

## 4. Complexity Analysis
- **Time Complexity**: `O((N + M) log N)`
- **Space Complexity**: `O(N + M)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <set>
#include <queue>
#include <algorithm>

using namespace std;

const int MOD = 998244353;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    if (!(cin >> N >> M)) return 0;

    vector<vector<int>> del(N + 1);
    for (int i = 0; i < M; ++i) {
        int u, v;
        cin >> u >> v;
        del[u].push_back(v);
        del[v].push_back(u);
    }

    for (int i = 1; i <= N; ++i) {
        sort(del[i].begin(), del[i].end());
    }

    set<int> unvis;
    for (int i = 2; i <= N; ++i) unvis.insert(i);

    vector<int> dist(N + 1, -1);
    queue<int> q;

    dist[1] = 0;
    q.push(1);

    while (!q.empty()) {
        int u = q.front();
        q.pop();

        int prev_val = 0;
        vector<int> to_remove;

        for (int v : del[u]) {
            // Find all unvisited nodes in (prev_val, v)
            auto it = unvis.upper_bound(prev_val);
            while (it != unvis.end() && *it < v) {
                int node = *it;
                dist[node] = dist[u] + 1;
                q.push(node);
                to_remove.push_back(node);
                it = unvis.erase(it);
            }
            prev_val = v;
        }

        // Find all unvisited nodes > last deleted neighbor
        auto it = unvis.upper_bound(prev_val);
        while (it != unvis.end()) {
            int node = *it;
            dist[node] = dist[u] + 1;
            q.push(node);
            it = unvis.erase(it);
        }
    }

    if (dist[N] == -1) {
        cout << -1 << "\n";
        return 0;
    }

    int max_d = dist[N];
    vector<vector<int>> layers(max_d + 1);
    for (int i = 1; i <= N; ++i) {
        if (dist[i] != -1 && dist[i] <= max_d) {
            layers[dist[i]].push_back(i);
        }
    }

    vector<long long> dp(N + 1, 0);
    dp[1] = 1;

    for (int d = 1; d <= max_d; ++d) {
        long long sum_prev = 0;
        for (int u : layers[d - 1]) {
            sum_prev = (sum_prev + dp[u]) % MOD;
        }

        for (int v : layers[d]) {
            long long cur = sum_prev;
            for (int u : del[v]) {
                if (dist[u] == d - 1) {
                    cur = (cur - dp[u] + MOD) % MOD;
                }
            }
            dp[v] = cur;
        }
    }

    cout << dp[N] << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
