# Problem Analysis: AtCoder-arc078_b — Fennec VS. Snuke

**Problem ID**: `AtCoder-arc078_b`  
**Contest**: `abc067`  
**Rating / Difficulty**: 1431  
**URL**: https://atcoder.jp/contests/abc067/tasks/arc078_b  
**VJudge Tag**: `[problem:AtCoder-arc078_b]`  
**Category File**: [`../categories/graph_theory/tree_multi_source_bfs_partition.md`](../categories/graph_theory/tree_multi_source_bfs_partition.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Trees`  
- **Topic (Skill)**: `Tree Multi-Source BFS Voronoi Territory Partition`  

---

## 1. Problem Statement & Key Idea
In a tree with N vertices, Fennec starts at vertex 1 and Snuke starts at vertex N. Alternating turns, each paints an adjacent uncolored vertex in their color. When no moves are left, the player with strictly more colored vertices wins. Determine who wins under optimal play.

**Key Insight**: In a tree, the game decomposes into a Voronoi diagram on tree distances: Fennec captures vertex v if dist(1, v) <= dist(N, v); otherwise Snuke captures v.

## 2. Core Observation & Invariant
Because both players move at speed 1 on the unique path between 1 and N, neither player can cross the boundary once the opponent reaches it. Fennec claims all vertices strictly closer to 1 (or ties, since Fennec moves first).

## 3. Step-by-Step Algorithm
1. Run BFS/DFS from vertex 1 to compute dist1[v] for all vertices.
2. Run BFS/DFS from vertex N to compute distN[v] for all vertices.
3. Count vertices where dist1[v] <= distN[v] (Fennec's territory).
4. Count vertices where distN[v] < dist1[v] (Snuke's territory).
5. If Fennec's territory > Snuke's territory, print 'Fennec', else print 'Snuke'.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

void bfs(int start, const vector<vector<int>>& adj, vector<int>& dist) {
    dist[start] = 0;
    queue<int> q;
    q.push(start);
    while (!q.empty()) {
        int u = q.front();
        q.pop();
        for (int v : adj[u]) {
            if (dist[v] == -1) {
                dist[v] = dist[u] + 1;
                q.push(v);
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    vector<int> dist1(n + 1, -1), distN(n + 1, -1);
    bfs(1, adj, dist1);
    bfs(n, adj, distN);

    int fennec = 0, snuke = 0;
    for (int i = 1; i <= n; ++i) {
        if (dist1[i] <= distN[i]) {
            fennec++;
        } else {
            snuke++;
        }
    }

    cout << (fennec > snuke ? "Fennec" : "Snuke") << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Distance-based Voronoi territory partitioning on trees.
- **Reusable Pattern**: `Competitive tree expansion game: compare distances from starting positions dist(A, v) <= dist(B, v).`
