# Problem Analysis: AtCoder-abc247_g — Dream Team

**Problem ID**: `AtCoder-abc247_g`  
**Contest**: `abc247`  
**Rating / Difficulty**: 2159  
**URL**: https://atcoder.jp/contests/abc247/tasks/abc247_g  
**VJudge Tag**: `[problem:AtCoder-abc247_g]`  
**Category File**: [`../categories/graph_theory/mcmf_primal_dual_bipartite_matching_all_sizes.md`](../categories/graph_theory/mcmf_primal_dual_bipartite_matching_all_sizes.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Flow and Min Cut`  
- **Topic (Skill)**: `Min Cost Max Flow (MCMF)`  

---

## 1. Problem Statement & Key Idea
Select a dream team of size k maximizing total power such that all universities and subjects are distinct. Formulated as maximum weight bipartite matching solved via successive shortest path Min-Cost Max-Flow (Primal-Dual) across all matching sizes k.

## 2. Core Observation & Invariant
Universities (<= 150) form the left partition and subjects (<= 150) form the right partition. For each pair (u, v), only retain the maximum power person. By negating costs (or setting cost = BIG - C_{u, v}), each unit of augmented flow from Source to Sink adds exactly 1 person while maximizing power. The algorithm stops when no augmenting path exists.

## 3. Step-by-Step Algorithm
1. Deduplicate input edges between university A_i and subject B_i, keeping max C_i.
2. Build bipartite flow network with Source 0, Sink 301, capacities 1 from S to universities and subjects to T.
3. Add edges from universities to subjects with capacity 1 and cost BIG - C_{u, v}.
4. Run successive shortest path (Dijkstra with Johnson potentials) augmenting 1 unit of flow per step.
5. Record and output the maximum power for each team size k = 1, 2, ...

## 4. Complexity Analysis
- **Time Complexity**: `O(V * E log V)`
- **Space Complexity**: `O(V + E)`

## 5. C++ Source Code (Verified & Clean)
```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

const long long INF = 1e18;
const long long BIG_COST = 1e9 + 7;

struct Edge {
    int to;
    int cap;
    long long cost;
    int rev;
};

struct MCMF {
    int n;
    vector<vector<Edge>> g;
    vector<long long> h, dist;
    vector<int> prevv, preve;

    MCMF(int n) : n(n), g(n), h(n, 0), dist(n), prevv(n), preve(n) {}

    void add_edge(int from, int to, int cap, long long cost) {
        g[from].push_back({to, cap, cost, (int)g[to].size()});
        g[to].push_back({from, 0, -cost, (int)g[from].size() - 1});
    }

    pair<int, long long> augment(int s, int t) {
        priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> pq;
        fill(dist.begin(), dist.end(), INF);
        dist[s] = 0;
        pq.push({0, s});

        while (!pq.empty()) {
            auto [d, v] = pq.top();
            pq.pop();
            if (dist[v] < d) continue;

            for (int i = 0; i < (int)g[v].size(); ++i) {
                Edge& e = g[v][i];
                if (e.cap > 0 && dist[e.to] > dist[v] + e.cost + h[v] - h[e.to]) {
                    dist[e.to] = dist[v] + e.cost + h[v] - h[e.to];
                    prevv[e.to] = v;
                    preve[e.to] = i;
                    pq.push({dist[e.to], e.to});
                }
            }
        }

        if (dist[t] == INF) return {0, 0};

        for (int v = 0; v < n; ++v) h[v] += dist[v];

        int d = 1;
        for (int v = t; v != s; v = prevv[v]) {
            d = min(d, g[prevv[v]][preve[v]].cap);
        }
        for (int v = t; v != s; v = prevv[v]) {
            Edge& e = g[prevv[v]][preve[v]];
            e.cap -= d;
            g[v][e.rev].cap += d;
        }

        return {d, h[t]};
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    int max_a[155][155];
    for (int i = 0; i <= 150; ++i) {
        for (int j = 0; j <= 150; ++j) {
            max_a[i][j] = -1;
        }
    }

    for (int i = 0; i < n; ++i) {
        int a, b;
        long long c;
        cin >> a >> b >> c;
        if (c > max_a[a][b]) {
            max_a[a][b] = c;
        }
    }

    int s = 0, t = 301;
    MCMF flow(305);

    for (int i = 1; i <= 150; ++i) {
        flow.add_edge(s, i, 1, 0);
        flow.add_edge(150 + i, t, 1, 0);
    }

    for (int i = 1; i <= 150; ++i) {
        for (int j = 1; j <= 150; ++j) {
            if (max_a[i][j] != -1) {
                flow.add_edge(i, 150 + j, 1, BIG_COST - max_a[i][j]);
            }
        }
    }

    vector<long long> ans;
    long long total_cost = 0;
    while (true) {
        auto [f, c] = flow.augment(s, t);
        if (f == 0) break;
        total_cost += c;
        int k = ans.size() + 1;
        long long max_power = 1LL * k * BIG_COST - total_cost;
        ans.push_back(max_power);
    }

    cout << ans.size() << "\n";
    for (long long val : ans) {
        cout << val << "\n";
    }

    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
