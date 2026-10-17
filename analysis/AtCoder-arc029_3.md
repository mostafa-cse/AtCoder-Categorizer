# Problem Analysis: AtCoder-arc029_3 — 高橋君と国家

**Problem ID**: `AtCoder-arc029_3`  
**Contest**: `arc029`  
**Rating / Difficulty**: 1973  
**URL**: https://atcoder.jp/contests/arc029/tasks/arc029_3  
**VJudge Tag**: `[problem:AtCoder-arc029_3]`  
**Category File**: [`../categories/graph_theory/super_source_mst_vertex_activation.md`](../categories/graph_theory/super_source_mst_vertex_activation.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Minimum Spanning Tree`  
- **Topic (Skill)**: `Super-Source Vertex Activation Transformation for Minimum Spanning Tree`  

---

## 1. Problem Statement & Key Idea
N cities, M roads. City i can build a trade port for cost c_i. Road j connects a_j, b_j with cost r_j. Find minimum cost so every city is connected to at least one trade port.

Building a trade port at city i can be modeled as adding an edge between city i and a virtual 'super-source' vertex 0 with weight c_i. The requirement that every city has a path to at least one trade port is equivalent to requiring that every city is connected to vertex 0! Thus, the problem reduces directly to finding the Minimum Spanning Tree on N + 1 vertices (vertices 0..N) using Kruskal's algorithm with DSU.

## 2. Core Observation & Invariant
Vertex costs are transformed into edges to an auxiliary super-source, unifying vertex activation with edge connectivity.

## 3. Step-by-Step Algorithm
1. Create graph with N + 1 vertices (0 to N).
2. Add edge (0, i) with weight c_i for each city i in 1..N.
3. Add road edges (a_j, b_j) with weight r_j.
4. Sort all N + M edges by weight ascending.
5. Run Kruskal's algorithm with DSU to find MST weight.
6. Print total MST weight.

## 4. Complexity Analysis
- **Time Complexity**: `O((N + M) log(N + M))`
- **Space Complexity**: `O(N + M)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

using namespace std;

struct Edge {
    int u, v;
    long long w;
};

struct DSU {
    vector<int> parent;
    DSU(int n) : parent(n) {
        iota(parent.begin(), parent.end(), 0);
    }
    int find(int v) {
        if (v == parent[v]) return v;
        return parent[v] = find(parent[v]);
    }
    bool unite(int a, int b) {
        a = find(a);
        b = find(b);
        if (a != b) {
            parent[b] = a;
            return true;
        }
        return false;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<Edge> edges;
    for (int i = 1; i <= n; ++i) {
        long long c;
        cin >> c;
        edges.push_back({0, i, c});
    }

    for (int i = 0; i < m; ++i) {
        int u, v;
        long long r;
        cin >> u >> v >> r;
        edges.push_back({u, v, r});
    }

    sort(edges.begin(), edges.end(), [](const Edge& a, const Edge& b) {
        return a.w < b.w;
    });

    DSU dsu(n + 1);
    long long total_cost = 0;
    int edges_used = 0;

    for (const auto& e : edges) {
        if (dsu.unite(e.u, e.v)) {
            total_cost += e.w;
            edges_used++;
            if (edges_used == n) break;
        }
    }

    cout << total_cost << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Super-source graph modeling for facility location and vertex activation via MST.
- **Reusable Pattern**: `Super-Source MST: Connect facility candidate i to dummy node 0 with weight c_i; run Kruskal.`
