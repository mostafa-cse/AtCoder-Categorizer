# Problem Analysis: AtCoder-arc165_c — Social Distance on Graph

**Problem ID**: `AtCoder-arc165_c`  
**Contest**: `arc165`  
**Rating / Difficulty**: 1743  
**URL**: https://atcoder.jp/contests/arc165/tasks/arc165_c  
**VJudge Tag**: `[problem:AtCoder-arc165_c]`  
**Category File**: [`../categories/graph_theory/binary_search_bipartite_coloring_distance.md`](../categories/graph_theory/binary_search_bipartite_coloring_distance.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Bipartite Graphs`  
- **Topic (Skill)**: `Binary Search on Min Same-Color Distance / Bipartite 2-Coloring Feasibility`  

---

## 1. Problem Statement & Key Idea
Given an undirected weighted graph. Color each vertex red or blue. The distance between two vertices is the shortest path between them. Maximize the minimum distance between any two vertices of the same color.

**Key Insight**: Binary search on target distance X. If two vertices have shortest path < X, they cannot share a color. Paths of length 1 with w < X require endpoints to have different colors (bipartite 2-coloring). Paths of length 2 require the sum of the two smallest edges incident to any vertex to be >= X.

## 2. Core Observation & Invariant
A target X is feasible iff: (1) for every vertex v, the sum of its two smallest incident edge weights is >= X, and (2) the subgraph formed by all edges with weight < X is bipartite.

## 3. Step-by-Step Algorithm
1. For each vertex, sort incident edge weights.
2. Upper bound on X is min over all v of (smallest_weight + second_smallest_weight).
3. Binary search on X in [1, upper_bound]:
4.   Build subgraph of edges with weight < X.
5.   Run BFS/DFS to check if this subgraph is bipartite (2-colorable).
6.   If bipartite, low = X, else high = X - 1.
7. Print optimal X.

## 4. Complexity Analysis
- **Time Complexity**: `O((N + M) log(max_ans))`
- **Space Complexity**: `O(N + M)`

## 5. Complete C++ Solution
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

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Combining binary search with bipartite checking and 2-star local neighborhood constraints.
- **Reusable Pattern**: `Min Monochromatic Distance Bipartite Check: Feasible iff edges < X form bipartite graph and stars >= X.`
