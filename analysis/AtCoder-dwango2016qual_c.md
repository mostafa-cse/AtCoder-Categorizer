# Problem Analysis: AtCoder-dwango2016qual_c — C. メンテナンス明け

**Problem ID**: `AtCoder-dwango2016qual_c`  
**Contest**: `dwango2016-prelims`  
**Rating / Difficulty**: 2384  
**URL**: https://atcoder.jp/contests/dwango2016-prelims/tasks/dwango2016qual_c  
**VJudge Tag**: `[problem:AtCoder-dwango2016qual_c]`  
**Category File**: [`../categories/graph_theory/sleep_risk_adversarial_dijkstra.md`](../categories/graph_theory/sleep_risk_adversarial_dijkstra.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Shortest Paths`  
- **Topic (Skill)**: `Dijkstra's Algorithm`  

---

## 1. Problem Statement & Key Idea
Find the path from src to dst minimizing worst-case travel time when falling asleep carries the commuter to the terminus. After computing baseline distances d_{normal} to dst, each line edge e = (u -> v) carries risk P(e) = dist(u, T) + d_{normal}(T). Reverse Dijkstra solving dp(u) = min_e max(w(e) + dp(v), P(e)) runs in O((N + \sum L_i) \log N) time.

## 2. Core Observation & Invariant
When riding an edge e = (u -> v) on line L, falling asleep carries the passenger to the terminus T in that direction with penalty P(e) = dist_L(u, T) + d_{normal}(T). The optimal adversarial step from u minimizes max(w(e) + dp(v), P(e)), which defines a monotonic Dijkstra operator backwards from dst.

## 3. Step-by-Step Algorithm
1. Run Dijkstra from dst on the original network to compute d_{normal}(u) for all stations.
2. For each line L, precompute distances to both termini to obtain P(e) for all directed edges in O(1).
3. Reverse all edges and run a min-priority queue backwards from dst with dp[dst] = 0, relaxing dp[u] = min(dp[u], max(w + dp[v], P)) until src is settled.

## 4. Complexity Analysis
- **Time Complexity**: `O((N + \sum L_i) \log N)`
- **Space Complexity**: `O(N + \sum L_i)`

## 5. C++ Source Code
```cpp

#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

const long long INF = 1e18;

struct RevEdge {
    int u;
    long long w;
    long long P;
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int N, M, src, dst;
    if (!(cin >> N >> M >> src >> dst)) return 0;

    struct Line {
        int L;
        vector<int> stations;
        vector<long long> weights;
    };

    vector<Line> lines(M);
    vector<vector<pair<int, long long>>> adj(N);

    for (int i = 0; i < M; ++i) {
        cin >> lines[i].L;
        lines[i].stations.resize(lines[i].L);
        for (int j = 0; j < lines[i].L; ++j) cin >> lines[i].stations[j];
        lines[i].weights.resize(lines[i].L - 1);
        for (int j = 0; j < lines[i].L - 1; ++j) {
            cin >> lines[i].weights[j];
            int u = lines[i].stations[j];
            int v = lines[i].stations[j + 1];
            long long w = lines[i].weights[j];
            adj[u].push_back({v, w});
            adj[v].push_back({u, w});
        }
    }

    // 1. Dijkstra from dst
    vector<long long> d_normal(N, INF);
    priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> pq;
    d_normal[dst] = 0;
    pq.push({0, dst});
    while (!pq.empty()) {
        auto [d, u] = pq.top();
        pq.pop();
        if (d > d_normal[u]) continue;
        for (auto& edge : adj[u]) {
            int v = edge.first;
            long long w = edge.second;
            if (d + w < d_normal[v]) {
                d_normal[v] = d + w;
                pq.push({d + w, v});
            }
        }
    }

    // 2. Build rev_edges
    vector<vector<RevEdge>> rev_edges(N);
    for (int l = 0; l < M; ++l) {
        int L = lines[l].L;
        auto& st = lines[l].stations;
        auto& wt = lines[l].weights;
        vector<long long> pref(L, 0);
        for (int j = 0; j < L - 1; ++j) {
            pref[j + 1] = pref[j] + wt[j];
        }
        long long total_len = pref[L - 1];
        int T_fwd = st[L - 1];
        int T_bwd = st[0];

        // Forward edges: st[j] -> st[j+1]
        for (int j = 0; j < L - 1; ++j) {
            int u = st[j];
            int v = st[j + 1];
            long long w = wt[j];
            long long P = (total_len - pref[j]) + d_normal[T_fwd];
            rev_edges[v].push_back({u, w, P});
        }

        // Backward edges: st[j+1] -> st[j]
        for (int j = 0; j < L - 1; ++j) {
            int u = st[j + 1];
            int v = st[j];
            long long w = wt[j];
            long long P = pref[j + 1] + d_normal[T_bwd];
            rev_edges[v].push_back({u, w, P});
        }
    }

    // 3. Dijkstra backwards from dst on game DP
    vector<long long> dp(N, INF);
    dp[dst] = 0;
    pq.push({0, dst});
    while (!pq.empty()) {
        auto [d, v] = pq.top();
        pq.pop();
        if (d > dp[v]) continue;
        if (v == src) break;
        for (auto& edge : rev_edges[v]) {
            int u = edge.u;
            long long cand = max(edge.w + d, edge.P);
            if (cand < dp[u]) {
                dp[u] = cand;
                pq.push({cand, u});
            }
        }
    }

    cout << dp[src] << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
