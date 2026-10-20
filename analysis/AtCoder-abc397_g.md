# Problem Analysis: AtCoder-abc397_g — G. Maximize Distance

**Problem ID**: `AtCoder-abc397_g`  
**Contest**: `abc397`  
**Rating / Difficulty**: 2947  
**URL**: https://atcoder.jp/contests/abc397/tasks/abc397_g  
**VJudge Tag**: `[problem:AtCoder-abc397_g]`  
**Category File**: [`../categories/math/directed_shortest_path_augmentation_lp_duality_min_cost_flow.md`](../categories/math/directed_shortest_path_augmentation_lp_duality_min_cost_flow.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Mathematical Optimization`  
- **Topic (Skill)**: `Duality in Linear Programming (LP <> Flow)`  

---

## 1. Problem Statement & Key Idea
In a directed graph with N vertices and M edges of weight 0, choose exactly K edges to set to weight 1 to maximize the shortest path distance from 1 to N.

## 2. Core Observation & Invariant
Binary search on the target distance d. By LP duality, checking if shortest path distance >= d can be achieved is equivalent to finding potentials x_u in {0, ..., d} with x_1 = 0, x_N = d and x_v - x_u <= 1 such that sum_{(u, v)} [x_v - x_u = 1] <= K. This is a multi-label project selection (k-value min-cut) problem on a graph with N x d nodes, where difference constraints x_v - x_u <= 1 are infinity-capacity edges and unit penalties are capacity-1 edges.

## 3. Step-by-Step Algorithm
1. 1. Binary search d in [0, N].
2. 2. For each mid, construct min-cut graph with nodes (u, k) for u in [1, N], k in [1, d].
3. 3. Add monotonicity edges (u, k) -> (u, k-1) with capacity infinity.
4. 4. For each edge (u, v), add (v, k) -> (u, k) with capacity 1, and for k >= 2, (v, k) -> (u, k-1) with capacity infinity.
5. 5. Connect Source -> (N, d) and (1, 1) -> Sink with capacity infinity.
6. 6. Run Dinic's max flow; if min-cut <= K, distance d is feasible.

## 4. Complexity Analysis
- **Time Complexity**: `O(log N * Dinic(V = Nd, E = Md))`
- **Space Complexity**: `O(Nd + Md)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

static const long long INF = 1e15;

struct Edge {
    int to;
    long long cap;
    int rev;
};

class Dinic {
public:
    int n;
    vector<vector<Edge>> graph;
    vector<int> level;
    vector<int> ptr;

    Dinic(int n) : n(n), graph(n), level(n), ptr(n) {}

    void add_edge(int from, int to, long long cap) {
        graph[from].push_back({to, cap, (int)graph[to].size()});
        graph[to].push_back({from, 0, (int)graph[from].size() - 1});
    }

    bool bfs(int s, int t) {
        fill(level.begin(), level.end(), -1);
        level[s] = 0;
        queue<int> q;
        q.push(s);
        while (!q.empty()) {
            int u = q.front();
            q.pop();
            for (const auto& e : graph[u]) {
                if (e.cap > 0 && level[e.to] < 0) {
                    level[e.to] = level[u] + 1;
                    q.push(e.to);
                }
            }
        }
        return level[t] >= 0;
    }

    long long dfs(int u, int t, long long f) {
        if (u == t) return f;
        for (int& i = ptr[u]; i < (int)graph[u].size(); ++i) {
            auto& e = graph[u][i];
            if (e.cap > 0 && level[e.to] == level[u] + 1) {
                long long pushed = dfs(e.to, t, min(f, e.cap));
                if (pushed > 0) {
                    e.cap -= pushed;
                    graph[e.to][e.rev].cap += pushed;
                    return pushed;
                }
            }
        }
        return 0;
    }

    long long max_flow(int s, int t) {
        long long flow = 0;
        while (bfs(s, t)) {
            fill(ptr.begin(), ptr.end(), 0);
            while (long long pushed = dfs(s, t, INF)) {
                flow += pushed;
            }
        }
        return flow;
    }
};

long long min_cost_for_d(int n, const vector<pair<int, int>>& edges, int d) {
    if (d == 0) return 0;

    auto node_id = [d](int u, int k) {
        return 2 + (u - 1) * d + (k - 1);
    };

    int total_nodes = 2 + n * d;
    Dinic dinic(total_nodes);

    // x_1 = 0 -> (1, 1) -> sink (inf)
    dinic.add_edge(node_id(1, 1), 1, INF);

    // x_n = d -> source -> (n, d) (inf)
    dinic.add_edge(0, node_id(n, d), INF);

    // Monotonicity: (u, k) -> (u, k - 1) (inf)
    for (int u = 1; u <= n; ++u) {
        for (int k = 2; k <= d; ++k) {
            dinic.add_edge(node_id(u, k), node_id(u, k - 1), INF);
        }
    }

    // Edges (u, v):
    // Penalty cost: (v, k) -> (u, k) cap 1
    // Hard constraint x_v - x_u <= 1: (v, k) -> (u, k - 1) cap INF
    for (const auto& e : edges) {
        int u = e.first;
        int v = e.second;
        for (int k = 1; k <= d; ++k) {
            dinic.add_edge(node_id(v, k), node_id(u, k), 1);
            if (k >= 2) {
                dinic.add_edge(node_id(v, k), node_id(u, k - 1), INF);
            }
        }
    }

    return dinic.max_flow(0, 1);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    long long k;
    if (!(cin >> n >> m >> k)) return 0;

    vector<pair<int, int>> edges(m);
    for (int i = 0; i < m; ++i) {
        cin >> edges[i].first >> edges[i].second;
    }

    int low = 0, high = n;
    int ans = 0;

    while (low <= high) {
        int mid = low + (high - low) / 2;
        long long cost = min_cost_for_d(n, edges, mid);
        if (cost <= k) {
            ans = mid;
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }

    cout << ans << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
