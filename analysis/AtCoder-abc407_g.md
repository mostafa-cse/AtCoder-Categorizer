# Problem Analysis: AtCoder-abc407_g — G. Domino Covering SUM

**Problem ID**: `AtCoder-abc407_g`  
**Contest**: `abc407`  
**Rating / Difficulty**: 2190  
**URL**: https://atcoder.jp/contests/abc407/tasks/abc407_g  
**VJudge Tag**: `[problem:AtCoder-abc407_g]`  
**Category File**: [`../categories/graph_theory/min_cost_max_flow_bipartite_matching.md`](../categories/graph_theory/min_cost_max_flow_bipartite_matching.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Flow and Min Cut`  
- **Topic (Skill)**: `Min Cost Max Flow (MCMF)`  

---

## 1. Problem Statement & Key Idea
Place zero or more disjoint dominoes on an H x W grid to maximize the sum of uncovered cells. Uncovered sum equals total sum minus covered sum, so covering adjacent (u, v) yields a net gain of -(A_u + A_v). Shifting edge costs by OFFSET = 2e12 + 5 ensures non-negative edge costs, allowing Primal-Dual MCMF (Dijkstra with Johnson potentials) to find the optimum, terminating when path cost reaches OFFSET.

## 2. Core Observation & Invariant
Grid cells form a bipartite graph (L, R) partitioned by (r + c) mod 2. With shifted costs (A_u + A_v + OFFSET >= 0), augmenting path distances are non-decreasing. Augmenting a path of length dist < OFFSET saves (OFFSET - dist) > 0. The moment dist >= OFFSET, any further augmentation yields non-positive gain, giving the global maximum.

## 3. Step-by-Step Algorithm
1. Partition cells into L and R based on parity of (r + c).
2. Add edge S -> u in L with cap 1, cost 0; add edge v in R -> T with cap 1, cost 0.
3. For adjacent cells u in L and v in R, add directed edge u -> v with cap 1, cost A_u + A_v + OFFSET.
4. Run successive shortest path with Dijkstra and Johnson potentials.
5. If pot[t] >= OFFSET, break. Otherwise augment flow and accumulate (OFFSET - pot[t]).
6. Output sum_all + total_saved.

## 4. Complexity Analysis
- **Time Complexity**: `O((HW)^2 log(HW))`
- **Space Complexity**: `O(HW)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <numeric>

using namespace std;

const long long INF = 1e18;
const long long OFFSET = 2000000000005LL; // 2e12 + 5

struct Edge {
    int to;
    int rev;
    long long cap;
    long long cost;
};

struct MCMF {
    int n;
    vector<vector<Edge>> adj;
    vector<long long> pot;
    vector<long long> dist;
    vector<int> pv, pe;

    MCMF(int n) : n(n), adj(n), pot(n, 0), dist(n), pv(n), pe(n) {}

    void add_edge(int from, int to, long long cap, long long cost) {
        adj[from].push_back({to, (int)adj[to].size(), cap, cost});
        adj[to].push_back({from, (int)adj[from].size() - 1, 0, -cost});
    }

    // Push flow as long as reduced cost + potential difference < OFFSET
    // which means true cost < 0
    long long solve(int s, int t) {
        long long total_saved = 0;
        while (true) {
            priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> pq;
            fill(dist.begin(), dist.end(), INF);
            dist[s] = 0;
            pq.push({0, s});
            while (!pq.empty()) {
                auto [d, u] = pq.top();
                pq.pop();
                if (dist[u] < d) continue;
                for (int i = 0; i < (int)adj[u].size(); ++i) {
                    Edge &e = adj[u][i];
                    if (e.cap > 0 && dist[e.to] > dist[u] + e.cost + pot[u] - pot[e.to]) {
                        dist[e.to] = dist[u] + e.cost + pot[u] - pot[e.to];
                        pv[e.to] = u;
                        pe[e.to] = i;
                        pq.push({dist[e.to], e.to});
                    }
                }
            }
            if (dist[t] == INF) break;
            for (int i = 0; i < n; ++i) {
                if (dist[i] < INF) pot[i] += dist[i];
            }
            // The true cost of this augmenting path is pot[t] - OFFSET
            if (pot[t] >= OFFSET) {
                // Any further path will have true cost >= 0, so stop
                break;
            }
            // Augment 1 unit of flow
            long long flow = 1;
            for (int v = t; v != s; v = pv[v]) {
                flow = min(flow, adj[pv[v]][pe[v]].cap);
            }
            total_saved += (OFFSET - pot[t]) * flow;
            for (int v = t; v != s; v = pv[v]) {
                adj[pv[v]][pe[v]].cap -= flow;
                adj[v][adj[pv[v]][pe[v]].rev].cap += flow;
            }
        }
        return total_saved;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int H, W;
    if (!(cin >> H >> W)) return 0;

    vector<vector<long long>> A(H, vector<long long>(W));
    long long sum_all = 0;
    for (int i = 0; i < H; ++i) {
        for (int j = 0; j < W; ++j) {
            cin >> A[i][j];
            sum_all += A[i][j];
        }
    }

    int s = H * W, t = H * W + 1;
    MCMF mcmf(H * W + 2);

    int dr[] = {0, 0, 1, -1};
    int dc[] = {1, -1, 0, 0};

    for (int r = 0; r < H; ++r) {
        for (int c = 0; c < W; ++c) {
            int u = r * W + c;
            if ((r + c) % 2 == 0) {
                mcmf.add_edge(s, u, 1, 0);
                for (int d = 0; d < 4; ++d) {
                    int nr = r + dr[d];
                    int nc = c + dc[d];
                    if (nr >= 0 && nr < H && nc >= 0 && nc < W) {
                        int v = nr * W + nc;
                        long long cost = A[r][c] + A[nr][nc] + OFFSET;
                        mcmf.add_edge(u, v, 1, cost);
                    }
                }
            } else {
                mcmf.add_edge(u, t, 1, 0);
            }
        }
    }

    long long saved = mcmf.solve(s, t);
    cout << sum_all + saved << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
