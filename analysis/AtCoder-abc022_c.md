# Problem Analysis: AtCoder-abc022_c — Blue Bird

**Problem ID**: `AtCoder-abc022_c`  
**Contest**: `abc022`  
**Rating / Difficulty**: 1505  
**URL**: https://atcoder.jp/contests/abc022/tasks/abc022_c  
**VJudge Tag**: `[problem:AtCoder-abc022_c]`  
**Category File**: [`../categories/graph_theory/shortest_cycle_through_source.md`](../categories/graph_theory/shortest_cycle_through_source.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `All-Pairs Shortest Paths`  
- **Topic (Skill)**: `Shortest Cycle through Source via All-Pairs Shortest Path`  

---

## 1. Problem Statement & Key Idea
An undirected weighted graph with N vertices (N <= 300) and M edges. Find the shortest simple cycle that passes through vertex 1, or -1 if no cycle exists.

**Key Insight**: A simple cycle passing through vertex 1 consists of 1 -> u -> ... -> v -> 1, where u and v are two distinct neighbors of 1, and the path from u to v does not pass through 1.

## 2. Core Observation & Invariant
Remove vertex 1 from the graph. Compute all-pairs shortest paths on the remaining vertices 2..N using Floyd-Warshall in O(N^3). Then minimize cost(1, u) + dist[u][v] + cost(1, v) over all pairs of distinct neighbors u, v of vertex 1.

## 3. Step-by-Step Algorithm
1. Store edge weights from vertex 1 to its neighbors.
2. Initialize dist[u][v] = INF for u, v in 2..N.
3. Run Floyd-Warshall on the induced subgraph of vertices 2..N.
4. ans = INF.
5. For all distinct neighbors u, v of 1:
6.   If dist[u][v] < INF:
7.     ans = min(ans, weight(1, u) + dist[u][v] + weight(1, v)).
8. Output ans if ans < INF, else -1.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^3)`
- **Space Complexity**: `O(N^2)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const long long INF = 1e16;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<long long>> dist(n + 1, vector<long long>(n + 1, INF));
    for (int i = 1; i <= n; ++i) dist[i][i] = 0;

    vector<pair<int, long long>> neighbors_1;

    for (int i = 0; i < m; ++i) {
        int u, v;
        long long l;
        cin >> u >> v >> l;
        if (u == 1) {
            neighbors_1.push_back({v, l});
        } else if (v == 1) {
            neighbors_1.push_back({u, l});
        } else {
            dist[u][v] = min(dist[u][v], l);
            dist[v][u] = min(dist[v][u], l);
        }
    }

    // Floyd-Warshall on vertices 2..N
    for (int k = 2; k <= n; ++k) {
        for (int i = 2; i <= n; ++i) {
            for (int j = 2; j <= n; ++j) {
                if (dist[i][k] + dist[k][j] < dist[i][j]) {
                    dist[i][j] = dist[i][k] + dist[k][j];
                }
            }
        }
    }

    long long ans = INF;
    int k = neighbors_1.size();
    for (int i = 0; i < k; ++i) {
        for (int j = i + 1; j < k; ++j) {
            int u = neighbors_1[i].first;
            int v = neighbors_1[j].first;
            long long cycle_cost = neighbors_1[i].second + dist[u][v] + neighbors_1[j].second;
            ans = min(ans, cycle_cost);
        }
    }

    cout << (ans >= INF ? -1 : ans) << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Cycle decomposition around an anchor node via subgraph all-pairs shortest paths.
- **Reusable Pattern**: `Shortest Cycle through S: remove S, run Floyd-Warshall, minimize w(S, u) + dist[u][v] + w(v, S).`
