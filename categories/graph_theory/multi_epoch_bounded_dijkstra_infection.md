# Dijkstra's Algorithm

**Domain**: `Graph Theory`  
**Subtopic**: `Shortest Paths`  

This workbook contains curated, high-quality competitive programming problems teaching **Dijkstra's Algorithm**.

---

## Curated Problems

### `[problem:AtCoder-abc307_f]` — Virus 2
- **Rating / Difficulty**: 2139
- **Contest**: `abc307`
- **Analysis**: [`analysis/AtCoder-abc307_f.md`](../../analysis/AtCoder-abc307_f.md)
- **Key Idea**: Modified Dijkstra where state is (day, remaining_distance_on_day). Transitions allow either continuing on the same day if remaining distance >= w, or starting the next available day nd where X_{nd} >= w with remaining distance X_{nd} - w. Priority queue orders states lexicographically by (day ascending, remaining_distance descending).
- **Time Complexity**: `O((N + M) log N)`
- **Space Complexity**: `O(N + M)`
- **Verified C++ Implementation**:
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
