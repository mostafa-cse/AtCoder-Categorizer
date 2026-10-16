# Problem Analysis: AtCoder-abc075_c — Bridge

**Problem ID**: `AtCoder-abc075_c`  
**Contest**: `abc075`  
**Rating / Difficulty**: 1067  
**URL**: https://atcoder.jp/contests/abc075/tasks/abc075_c  
**VJudge Tag**: `[problem:AtCoder-abc075_c]`  
**Category File**: [`../categories/graph_theory/bridge_detection_dsu_removal.md`](../categories/graph_theory/bridge_detection_dsu_removal.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Connectivity & Bridges`  
- **Topic (Skill)**: `Cut-Edge / Bridge Detection via DFS / DSU Edge Removal`  

---

## 1. Problem Statement & Key Idea
Given a connected undirected graph with N vertices and M edges (N, M <= 50). Count the number of bridges (edges whose removal increases connected components).

**Key Idea**: An edge e is a bridge if and only if removing e leaves the graph disconnected.

## 2. Core Observation & Invariant
Because N, M <= 50 are very small, we can test each edge independently in O(M): remove edge e, build DSU with the remaining M - 1 edges, and check if all vertices belong to a single connected component.

## 3. Step-by-Step Algorithm
1. Store all M edges.
2. Initialize bridge_count = 0.
3. For each edge i from 0 to M - 1: initialize DSU on N vertices; add all edges j != i; if DSU has > 1 connected component, bridge_count++.
4. Print bridge_count.

## 4. Complexity Analysis
- **Time Complexity**: `O(M^2 * alpha(N))`
- **Space Complexity**: `O(N + M)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

struct DSU {
    vector<int> parent;
    int components;
    DSU(int n) : parent(n + 1), components(n) {
        iota(parent.begin(), parent.end(), 0);
    }
    int find(int i) {
        if (parent[i] == i) return i;
        return parent[i] = find(parent[i]);
    }
    void unite(int i, int j) {
        int root_i = find(i);
        int root_j = find(j);
        if (root_i != root_j) {
            parent[root_i] = root_j;
            components--;
        }
    }
};

struct Edge {
    int u, v;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<Edge> edges(m);
    for (int i = 0; i < m; ++i) {
        cin >> edges[i].u >> edges[i].v;
    }

    int bridges = 0;
    for (int i = 0; i < m; ++i) {
        DSU dsu(n);
        for (int j = 0; j < m; ++j) {
            if (i == j) continue;
            dsu.unite(edges[j].u, edges[j].v);
        }
        if (dsu.components > 1) {
            bridges++;
        }
    }

    cout << bridges << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Bridge identification via brute-force edge removal and DSU connectivity.
- **Reusable Pattern**: `Bridge test by removal: unite all edges except i, check if component count > 1.`
