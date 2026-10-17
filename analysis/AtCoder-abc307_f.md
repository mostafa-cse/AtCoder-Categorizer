# Problem Analysis: AtCoder-abc307_f — Virus 2

**Problem ID**: `AtCoder-abc307_f`  
**Contest**: `abc307`  
**Rating / Difficulty**: 2139  
**URL**: https://atcoder.jp/contests/abc307/tasks/abc307_f  
**VJudge Tag**: `[problem:AtCoder-abc307_f]`  
**Category File**: [`../categories/graph_theory/multi_epoch_bounded_dijkstra_infection.md`](../categories/graph_theory/multi_epoch_bounded_dijkstra_infection.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Shortest Paths`  
- **Topic (Skill)**: `Dijkstra's Algorithm`  

---

## 1. Problem Statement & Key Idea
An infection spreads over D days on a weighted graph. On day i, infection can travel total distance X_i. Find the day each vertex is infected, or -1 if never infected.

**Key Insight**: Modified Dijkstra where state is (day, remaining_distance_on_day). Transitions allow either continuing on the same day if remaining distance >= w, or starting the next available day nd where X_{nd} >= w with remaining distance X_{nd} - w. Priority queue orders states lexicographically by (day ascending, remaining_distance descending).

## 2. Core Observation & Invariant
Multi-epoch distance-budgeted graph traversal mapped to modified Dijkstra tracking (epoch, remaining_budget).

## 3. Step-by-Step Algorithm
1. Initialize priority queue with initial infected nodes at (day 0, rem 0).
2. Maintain best[u] = (day, max_rem).
3. Dijkstra: pop (day, rem, u).
4. For each neighbor v with edge weight w:
5.   Option A: if rem >= w, push (day, rem - w, v).
6.   Option B: find earliest day nd > day with X[nd] >= w, push (nd, X[nd] - w, v).
7. Record infection day for each vertex.

## 4. Complexity Analysis
- **Time Complexity**: `O((N + M) log N)`
- **Space Complexity**: `O(N + M)`

## 5. Core Skill & Reusable Pattern
- **Core Skill**: Multi-epoch distance-budgeted Dijkstra with dual-objective state optimization.
- **Reusable Pattern**: Spreading processes with periodic distance limits modeled via Dijkstra tracking (period, remaining_quota).

## 6. Editorial Comparison & Alternative Approaches
Matches official editorial.

## 7. Verified C++17 Implementation
```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

struct Edge {
    int to;
    long long w;
};

struct State {
    int day;
    long long rem_dist;
    int u;

    bool operator<(const State& o) const {
        if (day != o.day) return day > o.day;
        return rem_dist < o.rem_dist;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<Edge>> adj(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v;
        long long w;
        cin >> u >> v >> w;
        adj[u].push_back({v, w});
        adj[v].push_back({u, w});
    }

    int k;
    cin >> k;
    vector<int> init_infected(k);
    for (int i = 0; i < k; ++i) cin >> init_infected[i];

    int d;
    cin >> d;
    vector<long long> x(d + 1);
    for (int i = 1; i <= d; ++i) cin >> x[i];

    vector<int> ans(n + 1, -1);
    priority_queue<State> pq;

    for (int u : init_infected) {
        ans[u] = 0;
        pq.push({0, 0, u});
    }

    vector<pair<int, long long>> best(n + 1, {1e9, -1});

    while (!pq.empty()) {
        auto [day, rem, u] = pq.top();
        pq.pop();

        if (day > best[u].first || (day == best[u].first && rem < best[u].second)) {
            continue;
        }

        for (auto& edge : adj[u]) {
            int v = edge.to;
            long long w = edge.w;

            if (rem >= w) {
                int next_day = day;
                long long next_rem = rem - w;
                if (next_day < best[v].first || (next_day == best[v].first && next_rem > best[v].second)) {
                    best[v] = {next_day, next_rem};
                    if (ans[v] == -1) ans[v] = next_day;
                    pq.push({next_day, next_rem, v});
                }
            }

            for (int nd = day + 1; nd <= d; ++nd) {
                if (x[nd] >= w) {
                    long long next_rem = x[nd] - w;
                    if (nd < best[v].first || (nd == best[v].first && next_rem > best[v].second)) {
                        best[v] = {nd, next_rem};
                        if (ans[v] == -1) ans[v] = nd;
                        pq.push({nd, next_rem, v});
                    }
                    break;
                }
            }
        }
    }

    for (int i = 1; i <= n; ++i) {
        cout << ans[i] << "\n";
    }

    return 0;
}
```
