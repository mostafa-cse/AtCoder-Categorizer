# Binary Search on Min Same-Color Distance / Bipartite 2-Coloring Feasibility

**Domain**: `Graph Theory`  
**Subtopic**: `Bipartite Graphs`  

This workbook contains curated, high-quality competitive programming problems teaching **Binary Search on Min Same-Color Distance / Bipartite 2-Coloring Feasibility**.

---

## Curated Problems

### `[problem:AtCoder-arc165_c]` — Social Distance on Graph
- **Rating / Difficulty**: 1743
- **Contest**: `arc165`
- **Analysis**: [`analysis/AtCoder-arc165_c.md`](../../analysis/AtCoder-arc165_c.md)
- **Key Idea**: Binary search on target distance X. If two vertices have shortest path < X, they cannot share a color. Paths of length 1 with w < X require endpoints to have different colors (bipartite 2-coloring). Paths of length 2 require the sum of the two smallest edges incident to any vertex to be >= X.
- **Time Complexity**: `O((N + M) log(max_ans))`
- **Space Complexity**: `O(N + M)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

struct Edge {
    int to;
    long long w;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<Edge>> adj(n + 1);
    vector<vector<long long>> weights(n + 1);

    for (int i = 0; i < m; ++i) {
        int u, v;
        long long w;
        cin >> u >> v >> w;
        adj[u].push_back({v, w});
        adj[v].push_back({u, w});
        weights[u].push_back(w);
        weights[v].push_back(w);
    }

    long long max_possible = 2e18;
    for (int i = 1; i <= n; ++i) {
        if (weights[i].size() >= 2) {
            sort(weights[i].begin(), weights[i].end());
            max_possible = min(max_possible, weights[i][0] + weights[i][1]);
        }
    }

    auto is_feasible = [&](long long x) -> bool {
        vector<int> color(n + 1, 0);

        for (int i = 1; i <= n; ++i) {
            if (color[i] != 0) continue;
            queue<int> q;
            color[i] = 1;
            q.push(i);

            while (!q.empty()) {
                int u = q.front();
                q.pop();

                for (auto& e : adj[u]) {
                    if (e.w >= x) continue;
                    if (color[e.to] == 0) {
                        color[e.to] = 3 - color[u];
                        q.push(e.to);
                    } else if (color[e.to] == color[u]) {
                        return false;
                    }
                }
            }
        }
        return true;
    };

    long long low = 1, high = max_possible, ans = 1;
    while (low <= high) {
        long long mid = low + (high - low) / 2;
        if (is_feasible(mid)) {
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
