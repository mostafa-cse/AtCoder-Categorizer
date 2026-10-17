# Problem Analysis: AtCoder-abc197_f — Construct a Palindrome

**Problem ID**: `AtCoder-abc197_f`  
**Contest**: `abc197`  
**Rating / Difficulty**: 1945  
**URL**: https://atcoder.jp/contests/abc197/tasks/abc197_f  
**VJudge Tag**: `[problem:AtCoder-abc197_f]`  
**Category File**: [`../categories/graph_theory/bidirectional_pair_bfs_palindromic_walk.md`](../categories/graph_theory/bidirectional_pair_bfs_palindromic_walk.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `BFS / State Graphs`  
- **Topic (Skill)**: `Bidirectional Symmetric Pair BFS for Shortest Palindromic Graph Walk`  

---

## 1. Problem Statement & Key Idea
Given an undirected graph with N vertices and M edges labeled with lowercase English letters. Find the minimum length of a walk from 1 to N whose edge labels form a palindrome, or report -1.

A palindrome is symmetric: start from both endpoints (1, N) simultaneously. Define BFS state as (u, v) where u starts at 1 and v starts at N. From state (u, v), step to (u', v') if u has edge u -> u' labeled c and v has edge v -> v' with the same label c, increasing step distance by 2. When u == v, walk length is 2 * dist. When u and v share an edge, walk length is 2 * dist + 1.

## 2. Core Observation & Invariant
State graph of pairs (u, v) has N^2 states. BFS finds the global minimum distance efficiently.

## 3. Step-by-Step Algorithm
1. Build adjacency list with characters.
2. Initialize dist[u][v] = INF for all 1 <= u, v <= N.
3. Set dist[1][N] = 0 and push (1, N) to queue.
4. Run BFS: pop (u, v). If u == v, ans = min(ans, 2 * d). If edge (u, v) exists, ans = min(ans, 2 * d + 1).
5. Transition to (u', v') for matching edge characters c.
6. Print ans if < INF, else -1.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2 + M^2)`
- **Space Complexity**: `O(N^2)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <string>

using namespace std;

const int INF = 1e9;

struct Edge {
    int to;
    char c;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<Edge>> adj(n + 1);
    vector<vector<int>> is_edge(n + 1, vector<int>(n + 1, 0));

    for (int i = 0; i < m; ++i) {
        int u, v;
        char c;
        cin >> u >> v >> c;
        adj[u].push_back({v, c});
        adj[v].push_back({u, c});
        is_edge[u][v] = 1;
        is_edge[v][u] = 1;
    }

    vector<vector<int>> dist(n + 1, vector<int>(n + 1, INF));
    queue<pair<int, int>> q;

    dist[1][n] = 0;
    q.push({1, n});

    int ans = INF;

    while (!q.empty()) {
        auto [u, v] = q.front();
        q.pop();

        int d = dist[u][v];

        if (u == v) {
            ans = min(ans, 2 * d);
        }
        if (is_edge[u][v]) {
            ans = min(ans, 2 * d + 1);
        }

        for (const auto& eu : adj[u]) {
            for (const auto& ev : adj[v]) {
                if (eu.c == ev.c) {
                    if (dist[eu.to][ev.to] > d + 1) {
                        dist[eu.to][ev.to] = d + 1;
                        q.push({eu.to, ev.to});
                    }
                }
            }
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

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Bidirectional simultaneous search on pair states for palindromic graph walks.
- **Reusable Pattern**: `Palindromic Walk BFS: Pair state (u, v) moves to (u', v') iff edge labels match.`
