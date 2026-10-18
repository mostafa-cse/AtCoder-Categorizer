# Problem Analysis: AtCoder-arc061_c — E. Snuke's Subway Trip

**Problem ID**: `AtCoder-arc061_c`  
**Contest**: `arc061`  
**Rating / Difficulty**: 2502  
**URL**: https://atcoder.jp/contests/arc061/tasks/arc061_c  
**VJudge Tag**: `[problem:AtCoder-arc061_c]`  
**Category File**: [`../categories/graph_theory/snukes_subway_trip_bipartite_01_bfs.md`](../categories/graph_theory/snukes_subway_trip_bipartite_01_bfs.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Graph Traversal`  
- **Topic (Skill)**: `Breadth First Search (BFS)`  

---

## 1. Problem Statement & Key Idea
Find minimum subway fare to travel from station 1 to station $N$. Each company charges 1 fare when boarded, and transfers between lines of the same company are free. Construct a state graph: for each station $u$ and company $c$ operating at $u$, create an auxiliary vertex $(u, c)$. Add directed edge $u \to (u, c)$ with weight 1 (boarding), and $(u, c) \to u$ with weight 0 (alighting). Track edges connecting station $p$ and $q$ under company $c$ become 0-weight bidirectional edges $(p, c) \leftrightarrow (q, c)$. Run 0-1 BFS from station 1 to station $N$.

## 2. Core Observation & Invariant
Because edge weights are strictly 0 and 1, Dijkstra is unnecessary; 0-1 BFS using a double-ended queue computes the shortest path in linear time $O(N + M)$.

## 3. Step-by-Step Algorithm
1. 1. Create unique node IDs for station-company pairs $(u, c)$ alongside original stations $1 \dots N$.
2. 2. Add edge $u \to (u, c)$ with weight 1, and $(u, c) \to u$ with weight 0.
3. 3. For each track $(p, q, c)$, add edges $(p, c) \leftrightarrow (q, c)$ with weight 0.
4. 4. Run 0-1 BFS with a deque starting at vertex 1 with distance 0.
5. 5. Pop vertex $u$; if $u = N$, return $dist[N]$.
6. 6. Traverse neighbors: if weight 0, push front; if weight 1, push back.
7. 7. Output $dist[N]$ or -1 if unreachable.

## 4. Complexity Analysis
- **Time Complexity**: `O(N + M)`
- **Space Complexity**: `O(N + M)`

## 5. C++ Source Code
```cpp

#include <iostream>
#include <vector>
#include <deque>
#include <map>

using namespace std;

struct Edge {
    int to;
    int w;
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    map<pair<int, int>, int> comp_v;
    int next_id = n + 1;

    vector<vector<Edge>> adj(n + 1);

    auto get_node = [&](int u, int c) -> int {
        auto it = comp_v.find({u, c});
        if (it != comp_v.end()) return it->second;
        int id = next_id++;
        comp_v[{u, c}] = id;
        if (id >= (int)adj.size()) adj.resize(id + 1);
        adj[u].push_back({id, 1}); // Boarding company c: cost 1
        adj[id].push_back({u, 0}); // Alighting at station u: cost 0
        return id;
    };

    for (int i = 0; i < m; ++i) {
        int p, q, c;
        cin >> p >> q >> c;
        int u = get_node(p, c);
        int v = get_node(q, c);
        adj[u].push_back({v, 0});
        adj[v].push_back({u, 0});
    }

    int total_nodes = next_id;
    vector<int> dist(total_nodes, -1);
    deque<int> dq;

    dist[1] = 0;
    dq.push_back(1);

    while (!dq.empty()) {
        int u = dq.front();
        dq.pop_front();

        if (u == n) {
            cout << dist[u] << "\n";
            return 0;
        }

        for (auto& edge : adj[u]) {
            int v = edge.to;
            int w = edge.w;
            if (dist[v] == -1 || dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
                if (w == 0) {
                    dq.push_front(v);
                } else {
                    dq.push_back(v);
                }
            }
        }
    }

    cout << dist[n] << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
