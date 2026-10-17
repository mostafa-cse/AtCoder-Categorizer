# All-Pairs Shortest Path Distance Scaling Inequality Counting via Dijkstra and Binary Search

**Domain**: `Graph Theory`  
**Subtopic**: `Shortest Paths`  

This workbook contains curated, high-quality competitive programming problems teaching **All-Pairs Shortest Path Distance Scaling Inequality Counting via Dijkstra and Binary Search**.

---

## Curated Problems

### `[problem:AtCoder-arc025_3]` — ウサギとカメ
- **Rating / Difficulty**: 1954
- **Contest**: `arc025`
- **Analysis**: [`analysis/AtCoder-arc025_3.md`](../../analysis/AtCoder-arc025_3.md)
- **Key Idea**: The condition is dist(s, t) * R < dist(s, r) * T. For each starting vertex s, run Dijkstra to obtain all distances dist(s, v). Sort the non-source vertices by distance. For each chosen goal vertex t, the required condition on rabbit vertex r is dist(s, r) > dist(s, t) * R / T. Using binary search (upper_bound) on the sorted distances, count valid r vertices in O(log N), excluding s and t.
- **Time Complexity**: `O(N * (M log N + N log N))`
- **Space Complexity**: `O(N + M)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

const long long INF = 1e18;

struct Edge {
    int to;
    long long w;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    long long R, T;
    if (!(cin >> n >> m >> R >> T)) return 0;

    vector<vector<Edge>> adj(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v;
        long long w;
        cin >> u >> v >> w;
        adj[u].push_back({v, w});
        adj[v].push_back({u, w});
    }

    long long total_count = 0;

    for (int s = 1; s <= n; ++s) {
        vector<long long> dist(n + 1, INF);
        priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> pq;

        dist[s] = 0;
        pq.push({0, s});

        while (!pq.empty()) {
            auto [d, u] = pq.top();
            pq.pop();

            if (d > dist[u]) continue;

            for (const auto& e : adj[u]) {
                if (dist[e.to] > d + e.w) {
                    dist[e.to] = d + e.w;
                    pq.push({dist[e.to], e.to});
                }
            }
        }

        vector<long long> dlist;
        for (int v = 1; v <= n; ++v) {
            if (v != s && dist[v] < INF) {
                dlist.push_back(dist[v]);
            }
        }
        sort(dlist.begin(), dlist.end());

        for (int t = 1; t <= n; ++t) {
            if (t == s || dist[t] == INF) continue;

            long long lhs = dist[t] * R;
            long long threshold = lhs / T;

            int valid_r = dlist.end() - upper_bound(dlist.begin(), dlist.end(), threshold);
            if (dist[t] > threshold) {
                valid_r--;
            }
            total_count += valid_r;
        }
    }

    cout << total_count << "\n";
    return 0;
}
```
