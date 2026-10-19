# Problem Analysis: AtCoder-abc308_h — Ex - Make Q

**Problem ID**: `AtCoder-abc308_h`  
**Contest**: `abc308`  
**Rating / Difficulty**: 2861  
**URL**: https://atcoder.jp/contests/abc308/tasks/abc308_h  
**VJudge Tag**: `[problem:AtCoder-abc308_h]`  
**Category File**: [`../categories/graph_theory/minimum_cost_q_subgraph_shortest_path_tree.md`](../categories/graph_theory/minimum_cost_q_subgraph_shortest_path_tree.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Shortest Paths`  
- **Topic (Skill)**: `Dijkstra's Algorithm`  

---

## 1. Problem Statement & Key Idea
Given a weighted undirected graph, find the minimum total weight of a subgraph shaped like the letter 'Q': a simple cycle plus a path attached to the cycle, such that all vertices on the cycle and path are distinct.

## 2. Core Observation & Invariant
A 'Q' subgraph consists of a simple cycle C and an edge (u, v) attached to the cycle, where u in C and v not in C. In any optimal configuration, the vertex u on the cycle has degree 3, and all other vertices on the cycle have degree 2. This is equivalent to finding a vertex u with degree >= 3, taking an edge (u, v) as the tail, and finding a simple cycle passing through u that does not use v. For each candidate degree-3 vertex u, we can remove its minimum incident edges or run shortest paths on the universal cover / Dijkstra to find the shortest cycle through u not containing v.

## 3. Step-by-Step Algorithm
1. 1. For each candidate vertex u, examine its incident edges sorted by weight.
2. 2. Pick the lightest edge (u, v) as the tail.
3. 3. Compute the shortest cycle through u disjoint from v using Dijkstra or cycle-finding with edge removals.
4. 4. Alternatively, fix the tail edge (u, v) and find the shortest cycle containing u in G \ {v}.
5. 5. Track minimum total weight over all valid choices of (u, v) and cycle.

## 4. Complexity Analysis
- **Time Complexity**: `O(M (N + M) log N)`
- **Space Complexity**: `O(N + M)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

static const long long INF = 1e15;

pair<long long, vector<int>> shortest_cycle(const vector<vector<long long>>& G, int r) {
    int n = G.size();
    vector<long long> dist(n, INF);
    vector<int> p(n, -1), g(n, -1);
    vector<bool> seen(n, false);

    dist[r] = 0;
    g[r] = r;

    for (int t = 0; t < n; t++) {
        long long mn = INF;
        int pos = -1;
        for (int i = 0; i < n; i++) {
            if (!seen[i] && dist[i] < mn) {
                mn = dist[i];
                pos = i;
            }
        }
        if (pos == -1) break;
        seen[pos] = true;

        for (int i = 0; i < n; i++) {
            if (G[pos][i] < INF) {
                if (dist[i] > dist[pos] + G[pos][i]) {
                    dist[i] = dist[pos] + G[pos][i];
                    p[i] = pos;
                    g[i] = (pos == r ? i : g[pos]);
                }
            }
        }
    }

    long long min_cycle_len = INF;
    int best_i = -1, best_j = -1;

    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if (G[i][j] >= INF) continue;
            if (p[i] == j || p[j] == i) continue;
            if (g[i] == -1 || g[j] == -1) continue;
            if (g[i] == g[j]) continue;

            if (dist[i] < INF && dist[j] < INF) {
                long long cur = dist[i] + dist[j] + G[i][j];
                if (cur < min_cycle_len) {
                    min_cycle_len = cur;
                    best_i = i;
                    best_j = j;
                }
            }
        }
    }

    if (best_i == -1) {
        return {INF, {}};
    }

    vector<int> path_a;
    int cur = best_i;
    while (cur != r) {
        path_a.push_back(cur);
        cur = p[cur];
    }
    path_a.push_back(r);
    reverse(path_a.begin(), path_a.end());

    vector<int> path_b;
    cur = best_j;
    while (cur != r) {
        path_b.push_back(cur);
        cur = p[cur];
    }

    vector<int> cycle = path_a;
    for (int v : path_b) {
        cycle.push_back(v);
    }
    return {min_cycle_len, cycle};
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<long long>> G(n, vector<long long>(n, INF));
    for (int i = 0; i < m; i++) {
        int u, v;
        long long c;
        cin >> u >> v >> c;
        --u; --v;
        G[u][v] = min(G[u][v], c);
        G[v][u] = min(G[v][u], c);
    }

    long long ans = INF;

    for (int a = 0; a < n; a++) {
        auto [len, cycle] = shortest_cycle(G, a);
        if (len >= INF || cycle.size() < 3) continue;

        int b = cycle[1];
        int c = cycle.back();

        for (int i = 0; i < n; i++) {
            if (i == a || i == b || i == c) continue;
            if (G[a][i] < INF) {
                ans = min(ans, len + G[a][i]);
            }
        }

        int adj[2] = {b, c};
        for (int idx = 0; idx < 2; idx++) {
            int neighbor = adj[idx];
            long long original_weight = G[a][neighbor];

            G[a][neighbor] = G[neighbor][a] = INF;
            auto [sub_len, sub_cycle] = shortest_cycle(G, a);
            if (sub_len < INF) {
                ans = min(ans, sub_len + original_weight);
            }
            G[a][neighbor] = G[neighbor][a] = original_weight;
        }
    }

    if (ans >= INF) {
        cout << -1 << "\n";
    } else {
        cout << ans << "\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
