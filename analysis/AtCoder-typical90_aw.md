# Problem Analysis: AtCoder-typical90_aw — Flip Digits 2

**Problem ID**: `AtCoder-typical90_aw`  
**Contest**: `typical90` (Kyopro Typical 90, Problem 049)  
**Rating / Difficulty**: 2150 (★6)  
**URL**: https://atcoder.jp/contests/typical90/tasks/typical90_aw  
**VJudge Tag**: `[problem:AtCoder-typical90_aw]`  
**Category File**: [`../categories/graph_theory/mst_kruskal.md`](../categories/graph_theory/mst_kruskal.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Minimum Spanning Tree (MST)`  
- **Topic (Skill)**: `Difference Array Graph Transformation & Minimum Spanning Tree (Kruskal)`  

---

## 1. Problem Statement & Key Idea
Binary string of length N. M operations with cost C_i flip bits in [L_i, R_i]. Find minimum cost to make it possible to reach any binary string, or -1 if impossible.

**Core Idea**: Range flip in array A corresponds to two point flips in difference array D_i = A_i ^ A_{i-1} at positions L and R + 1.

## 2. Core Observation & Invariant
Flipping [L, R] adds an edge between vertex L - 1 and vertex R in a graph of N + 1 vertices! Reaching all 2^N states is equivalent to the graph being connected. The minimum cost to connect N + 1 vertices is the Minimum Spanning Tree (Kruskal's algorithm)!

## 3. Step-by-Step Algorithm
1. Create graph with N + 1 vertices (0 to N).
2. For each operation (C, L, R): add edge between L - 1 and R with weight C.
3. Run Kruskal's MST algorithm using DSU.
4. If MST connects all N + 1 vertices (uses N edges), return MST cost; else return -1.

## 4. Complexity Analysis
Time: O(M log M), Space: O(N + M).

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct DSU {
    vector<int> parent;
    DSU(int n) : parent(n) {
        for (int i = 0; i < n; ++i) parent[i] = i;
    }
    int find(int i) {
        if (parent[i] == i) return i;
        return parent[i] = find(parent[i]);
    }
    bool unite(int i, int j) {
        int root_i = find(i), root_j = find(j);
        if (root_i != root_j) {
            parent[root_i] = root_j;
            return true;
        }
        return false;
    }
};

struct Edge {
    int u, v;
    long long cost;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<Edge> edges(m);
    for (int i = 0; i < m; ++i) {
        int c, l, r;
        cin >> c >> l >> r;
        edges[i] = {l - 1, r, (long long)c};
    }

    sort(edges.begin(), edges.end(), [](const Edge& a, const Edge& b) {
        return a.cost < b.cost;
    });

    DSU dsu(n + 1);
    long long total_cost = 0;
    int edges_used = 0;

    for (const auto& e : edges) {
        if (dsu.unite(e.u, e.v)) {
            total_cost += e.cost;
            edges_used++;
            if (edges_used == n) break;
        }
    }

    if (edges_used == n) {
        cout << total_cost << "\n";
    } else {
        cout << -1 << "\n";
    }
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Difference array range flip mapped to spanning tree on auxiliary graph.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: XOR range update reduction to edge connectivity and Kruskal's Minimum Spanning Tree.
- **Reusable Pattern**: `Difference Array Graph Reduction to MST.`

---
Back to [Difference Array Graph Transformation & Minimum Spanning Tree (Kruskal)](../categories/graph_theory/mst_kruskal.md) | [Categories Directory](../categories/README.md)