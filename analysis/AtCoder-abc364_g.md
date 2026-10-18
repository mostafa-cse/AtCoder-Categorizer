# Problem Analysis: AtCoder-abc364_g — G. Last Major City

**Problem ID**: `AtCoder-abc364_g`  
**Contest**: `abc364`  
**Rating / Difficulty**: 2455  
**URL**: https://atcoder.jp/contests/abc364/tasks/abc364_g  
**VJudge Tag**: `[problem:AtCoder-abc364_g]`  
**Category File**: [`../categories/graph_theory/last_major_city_minimum_steiner_tree.md`](../categories/graph_theory/last_major_city_minimum_steiner_tree.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Minimum Spanning Tree (MST)`  
- **Topic (Skill)**: `Steiner Tree Problem`  

---

## 1. Problem Statement & Key Idea
Given a graph with $N \le 4000$ cities and $M \le 8000$ edges, cities $1 \dots K-1$ ($K \le 10$) are fixed major cities. For each city $i \in [K, N]$, find the minimum cost of a tree connecting $1 \dots K-1$ and $i$. This is solved by the Dreyfus-Wagner Minimum Steiner Tree algorithm on terminal set $T = \{1, \dots, K-1\}$, where $dp[mask][v]$ represents the minimum tree connecting $mask \subseteq T$ rooted at vertex $v$.

## 2. Core Observation & Invariant
Because $K - 1 \le 9$, the number of terminal masks is at most $2^9 = 512$. For each mask, we perform submask splitting $dp[mask][v] = \min_{sub} (dp[sub][v] + dp[mask \setminus sub][v])$ followed by Dijkstra edge relaxation across the entire graph.

## 3. Step-by-Step Algorithm
1. 1. Set terminals $T = \{0, 1, \dots, K-2\}$ ($0$-indexed). Total masks $= 2^{K-1}$.
2. 2. Initialize $dp[1 \ll i][i] = 0$ for each terminal $i$, and all other entries to $\infty$.
3. 3. For $mask = 1 \dots 2^{K-1} - 1$:
4.    - Submask merging: for all non-empty submasks $sub \subsetneq mask$, update $dp[mask][v] = \min(dp[mask][v], dp[sub][v] + dp[mask \setminus sub][v])$ for each $v$.
5.    - Run Dijkstra on the graph initialized with current $dp[mask][v]$ to relax edge transitions.
6. 4. For each city $i = K-1 \dots N-1$, output $dp[2^{K-1} - 1][i]$.

## 4. Complexity Analysis
- **Time Complexity**: `O(3^{K-1} N + 2^{K-1} M log N)`
- **Space Complexity**: `O(2^{K-1} N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

static const long long INF = 1e18;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M, K;
    if (!(cin >> N >> M >> K)) return 0;

    vector<vector<pair<int, long long>>> adj(N);
    for (int i = 0; i < M; ++i) {
        int u, v;
        long long c;
        cin >> u >> v >> c;
        u--; v--;
        adj[u].push_back({v, c});
        adj[v].push_back({u, c});
    }

    int num_term = K - 1;
    int num_masks = 1 << num_term;
    vector<vector<long long>> dp(num_masks, vector<long long>(N, INF));

    for (int i = 0; i < num_term; ++i) {
        dp[1 << i][i] = 0;
    }

    for (int mask = 1; mask < num_masks; ++mask) {
        // Submask merging
        for (int sub = (mask - 1) & mask; sub > (mask ^ sub); sub = (sub - 1) & mask) {
            int other = mask ^ sub;
            for (int v = 0; v < N; ++v) {
                if (dp[sub][v] != INF && dp[other][v] != INF) {
                    long long val = dp[sub][v] + dp[other][v];
                    if (val < dp[mask][v]) {
                        dp[mask][v] = val;
                    }
                }
            }
        }

        // Dijkstra
        priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> pq;
        for (int v = 0; v < N; ++v) {
            if (dp[mask][v] != INF) {
                pq.push({dp[mask][v], v});
            }
        }

        while (!pq.empty()) {
            auto [d, u] = pq.top();
            pq.pop();
            if (d > dp[mask][u]) continue;

            for (auto& edge : adj[u]) {
                int v = edge.first;
                long long c = edge.second;
                if (d + c < dp[mask][v]) {
                    dp[mask][v] = d + c;
                    pq.push({d + c, v});
                }
            }
        }
    }

    int full_mask = num_masks - 1;
    for (int i = K - 1; i < N; ++i) {
        cout << dp[full_mask][i] << "\n";
    }
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
