# Bottleneck Maximum Bipartite Matching via Binary Search on Continuous Distance

**Domain**: `Graph Theory`  
**Subtopic**: `Network Flow`  

This workbook contains curated, high-quality competitive programming problems teaching **Bottleneck Maximum Bipartite Matching via Binary Search on Continuous Distance**.

---

## Curated Problems

### `[problem:AtCoder-abc401_g]` — Push Simultaneously
- **Rating / Difficulty**: 2022
- **Contest**: `abc401`
- **Analysis**: [`analysis/AtCoder-abc401_g.md`](../../analysis/AtCoder-abc401_g.md)
- **Key Idea**: Each person must be assigned to a unique button such that the Euclidean distance is <= t. This is the Bottleneck Bipartite Matching problem: minimize the maximum edge weight in a perfect matching. We binary search on time t. For a candidate t, build a bipartite graph with an edge between person i and button j iff dist(person_i, button_j) <= t. Check if a perfect matching of size N exists using Hopcroft-Karp or Dinic's Algorithm in O(N^2.5).
- **Time Complexity**: `O(iters * N^2.5)`
- **Space Complexity**: `O(N^2)`
- **Verified C++ Implementation**:
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
