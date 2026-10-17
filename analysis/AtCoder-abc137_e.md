# Problem Analysis: AtCoder-abc137_e — Coins Respawn

**Problem ID**: `AtCoder-abc137_e`  
**Contest**: `abc137`  
**Rating / Difficulty**: 1740  
**URL**: https://atcoder.jp/contests/abc137/tasks/abc137_e  
**VJudge Tag**: `[problem:AtCoder-abc137_e]`  
**Category File**: [`../categories/graph_theory/bellman_ford_constrained_negative_cycle.md`](../categories/graph_theory/bellman_ford_constrained_negative_cycle.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Shortest Paths`  
- **Topic (Skill)**: `Bellman-Ford Constrained Negative Cycle Reachability (1 -> cycle -> N)`  

---

## 1. Problem Statement & Key Idea
Directed graph with N vertices, M edges, edge rewards C_i. You start at vertex 1 and want to reach vertex N. Traversing any edge costs P coins (net gain C_i - P). Find max coins earned, or determine if arbitrarily large coins can be collected.

**Key Insight**: Negate rewards to edge weights w_i = P - C_i to convert into shortest path. An infinite gain exists iff there is a negative cycle that is simultaneously reachable from 1 AND can reach N.

## 2. Core Observation & Invariant
Filter the graph first: only retain vertices u where u is reachable from 1 and can reach N. Then run Bellman-Ford for N iterations; any relaxation on iteration N indicates an infinite gain loop on an active path.

## 3. Step-by-Step Algorithm
1. Run forward BFS from 1 to find reachable nodes from1.
2. Run backward BFS from N on reversed graph to find nodes that can reach N toN.
3. Only keep edges where both endpoints have from1 && toN.
4. Initialize dist[1..N] = INF, dist[1] = 0.
5. Relax edges N - 1 times.
6. Run N-th iteration: if any edge is relaxed, print -1 (infinite gain).
7. Else print max(0LL, -dist[N]).

## 4. Complexity Analysis
- **Time Complexity**: `O(N * M)`
- **Space Complexity**: `O(N + M)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

const long long INF = 1e18;

struct Edge {
    int u, v;
    long long w;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    long long p;
    if (!(cin >> n >> m >> p)) return 0;

    vector<Edge> edges;
    vector<vector<int>> fwd(n + 1), bwd(n + 1);

    for (int i = 0; i < m; ++i) {
        int u, v;
        long long c;
        cin >> u >> v >> c;
        edges.push_back({u, v, p - c});
        fwd[u].push_back(v);
        bwd[v].push_back(u);
    }

    // Reachability from 1
    vector<bool> from1(n + 1, false);
    queue<int> q;
    from1[1] = true;
    q.push(1);
    while (!q.empty()) {
        int u = q.front(); q.pop();
        for (int v : fwd[u]) {
            if (!from1[v]) {
                from1[v] = true;
                q.push(v);
            }
        }
    }

    // Reachability to N
    vector<bool> toN(n + 1, false);
    toN[n] = true;
    q.push(n);
    while (!q.empty()) {
        int u = q.front(); q.pop();
        for (int v : bwd[u]) {
            if (!toN[v]) {
                toN[v] = true;
                q.push(v);
            }
        }
    }

    vector<Edge> active_edges;
    for (auto& e : edges) {
        if (from1[e.u] && toN[e.u] && from1[e.v] && toN[e.v]) {
            active_edges.push_back(e);
        }
    }

    vector<long long> dist(n + 1, INF);
    dist[1] = 0;

    for (int iter = 1; iter < n; ++iter) {
        for (auto& e : active_edges) {
            if (dist[e.u] != INF && dist[e.u] + e.w < dist[e.v]) {
                dist[e.v] = dist[e.u] + e.w;
            }
        }
    }

    bool has_neg_cycle = false;
    for (auto& e : active_edges) {
        if (dist[e.u] != INF && dist[e.u] + e.w < dist[e.v]) {
            has_neg_cycle = true;
            break;
        }
    }

    if (has_neg_cycle) {
        cout << -1 << "\n";
    } else {
        cout << max(0LL, -dist[n]) << "\n";
    }

    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Negative cycle detection restricted to active source-sink path subgraphs.
- **Reusable Pattern**: `Path-Constrained Negative Cycle: Filter active nodes with dual BFS before Bellman-Ford.`
