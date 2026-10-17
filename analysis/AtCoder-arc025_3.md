# Problem Analysis: AtCoder-arc025_3 — ウサギとカメ

**Problem ID**: `AtCoder-arc025_3`  
**Contest**: `arc025`  
**Rating / Difficulty**: 1954  
**URL**: https://atcoder.jp/contests/arc025/tasks/arc025_3  
**VJudge Tag**: `[problem:AtCoder-arc025_3]`  
**Category File**: [`../categories/graph_theory/all_pairs_dijkstra_distance_scaling_inequality.md`](../categories/graph_theory/all_pairs_dijkstra_distance_scaling_inequality.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Shortest Paths`  
- **Topic (Skill)**: `All-Pairs Shortest Path Distance Scaling Inequality Counting via Dijkstra and Binary Search`  

---

## 1. Problem Statement & Key Idea
Weighted undirected graph with N vertices and M edges. Takahashi (rabbit) travels at speed R, Aoki (turtle) at speed T. Count ordered triplets of distinct vertices (s, r, t) such that the turtle takes strictly less time than the rabbit: dist(s, t) / T < dist(s, r) / R.

The condition is dist(s, t) * R < dist(s, r) * T. For each starting vertex s, run Dijkstra to obtain all distances dist(s, v). Sort the non-source vertices by distance. For each chosen goal vertex t, the required condition on rabbit vertex r is dist(s, r) > dist(s, t) * R / T. Using binary search (upper_bound) on the sorted distances, count valid r vertices in O(log N), excluding s and t.

## 2. Core Observation & Invariant
Fixing the source s and goal t decouples the search for r into an upper_bound query on the sorted distance array.

## 3. Step-by-Step Algorithm
1. For each vertex s in 1..N:
2.   Run Dijkstra to compute dist[s][v] for all v.
3.   Collect and sort distances to all v != s.
4.   For each goal t != s:
5.     Compute threshold = dist[s][t] * R / T.
6.     Find count of vertices with dist > threshold via upper_bound.
7.     If dist[s][t] > threshold, decrement count (since r cannot equal t).
8.     ans += count.
9. Print ans.

## 4. Complexity Analysis
- **Time Complexity**: `O(N * (M log N + N log N))`
- **Space Complexity**: `O(N + M)`

## 5. Complete C++ Solution
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

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: All-pairs shortest paths combined with binary search on scaled distance inequalities.
- **Reusable Pattern**: `Dijkstra Inequality Counting: Dijkstra from each source, sort distances, query valid pairs via upper_bound.`
