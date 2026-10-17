# Problem Analysis: AtCoder-abc401_g — Push Simultaneously

**Problem ID**: `AtCoder-abc401_g`  
**Contest**: `abc401`  
**Rating / Difficulty**: 2022  
**URL**: https://atcoder.jp/contests/abc401/tasks/abc401_g  
**VJudge Tag**: `[problem:AtCoder-abc401_g]`  
**Category File**: [`../categories/graph_theory/bottleneck_bipartite_matching_binary_search.md`](../categories/graph_theory/bottleneck_bipartite_matching_binary_search.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Network Flow`  
- **Topic (Skill)**: `Bottleneck Maximum Bipartite Matching via Binary Search on Continuous Distance`  

---

## 1. Problem Statement & Key Idea
N people at positions (sx_i, sy_i) move at speed <= 1 m/s to simultaneously push N buttons at (gx_j, gy_j) (one person per button). Find the minimum time t required.

**Key Idea**: Each person must be assigned to a unique button such that the Euclidean distance is <= t. This is the Bottleneck Bipartite Matching problem: minimize the maximum edge weight in a perfect matching. We binary search on time t. For a candidate t, build a bipartite graph with an edge between person i and button j iff dist(person_i, button_j) <= t. Check if a perfect matching of size N exists using Hopcroft-Karp or Dinic's Algorithm in O(N^2.5).

## 2. Core Observation & Invariant
Simultaneous button pressing under speed limit <= 1 is equivalent to continuous distance thresholding for perfect bipartite matching.

## 3. Step-by-Step Algorithm
1. Compute pairwise Euclidean distances d[i][j] between all people and buttons.
2. Binary search on t in [0, 2e18] for 80 iterations:
3.   Build bipartite graph: add edge i -> j if d[i][j] <= t.
4.   Run Hopcroft-Karp algorithm.
5.   If max matching == N: t is feasible, try smaller t.
6.   Else: t is infeasible, try larger t.
7. Print t with high precision.

## 4. Complexity Analysis
- **Time Complexity**: `O(iters * N^2.5)`
- **Space Complexity**: `O(N^2)`

## 5. Core Algorithmic Skill & Learning Takeaway
Continuous bottleneck matching via binary search and Hopcroft-Karp bipartite matching.

**Reusable Pattern**: Bottleneck Bipartite Matching: Binary search on threshold T; connect (u, v) iff cost(u, v) <= T; check if max_matching == N.

## 6. Comparison with Alternative Approaches
Matches official editorial.

## 7. Verified Clean C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <cmath>
#include <iomanip>
#include <queue>

using namespace std;

struct HopcroftKarp {
    int n, m;
    vector<vector<int>> adj;
    vector<int> pair_u, pair_v, dist;

    HopcroftKarp(int n, int m) : n(n), m(m), adj(n + 1), pair_u(n + 1, 0), pair_v(m + 1, 0), dist(n + 1) {}

    void add_edge(int u, int v) {
        adj[u].push_back(v);
    }

    bool bfs() {
        queue<int> q;
        for (int u = 1; u <= n; ++u) {
            if (pair_u[u] == 0) {
                dist[u] = 0;
                q.push(u);
            } else {
                dist[u] = 1e9;
            }
        }
        dist[0] = 1e9;

        while (!q.empty()) {
            int u = q.front();
            q.pop();

            if (dist[u] < dist[0]) {
                for (int v : adj[u]) {
                    if (dist[pair_v[v]] == 1e9) {
                        dist[pair_v[v]] = dist[u] + 1;
                        q.push(pair_v[v]);
                    }
                }
            }
        }
        return dist[0] != 1e9;
    }

    bool dfs(int u) {
        if (u != 0) {
            for (int v : adj[u]) {
                if (dist[pair_v[v]] == dist[u] + 1) {
                    if (dfs(pair_v[v])) {
                        pair_v[v] = u;
                        pair_u[u] = v;
                        return true;
                    }
                }
            }
            dist[u] = 1e9;
            return false;
        }
        return true;
    }

    int max_matching() {
        int matching = 0;
        while (bfs()) {
            for (int u = 1; u <= n; ++u) {
                if (pair_u[u] == 0 && dfs(u)) {
                    matching++;
                }
            }
        }
        return matching;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<pair<double, double>> s(n), g(n);
    for (int i = 0; i < n; ++i) cin >> s[i].first >> s[i].second;
    for (int i = 0; i < n; ++i) cin >> g[i].first >> g[i].second;

    vector<vector<double>> dist(n, vector<double>(n));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            dist[i][j] = hypot(s[i].first - g[j].first, s[i].second - g[j].second);
        }
    }

    auto check = [&](double t) {
        HopcroftKarp hk(n, n);
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (dist[i][j] <= t) {
                    hk.add_edge(i + 1, j + 1);
                }
            }
        }
        return hk.max_matching() == n;
    };

    double low = 0.0, high = 3e18;
    for (int iter = 0; iter < 90; ++iter) {
        double mid = low + (high - low) / 2.0;
        if (check(mid)) {
            high = mid;
        } else {
            low = mid;
        }
    }

    cout << fixed << setprecision(10) << high << "\n";
    return 0;
}
```
