# Problem Analysis: AtCoder-arc036_d — 偶数メートル

**Problem ID**: `AtCoder-arc036_d`  
**Contest**: `arc036`  
**Rating / Difficulty**: 2227  
**URL**: https://atcoder.jp/contests/arc036/tasks/arc036_d  
**VJudge Tag**: `[problem:AtCoder-arc036_d]`  
**Category File**: [`../categories/data_structures/bipartite_dsu_parity_path_reachability.md`](../categories/data_structures/bipartite_dsu_parity_path_reachability.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Disjoint Set Union (DSU)`  
- **Topic (Skill)**: `Augmented DSU / Weighted DSU`  

---

## 1. Problem Statement & Key Idea
Process edge additions and queries asking if two cities can be connected by an even-length walk in a dynamic undirected graph.

## 2. Core Observation & Invariant
Because backtracking along an edge adds an even distance (2 * z), any path parity can be adjusted by traversing an odd cycle. If two nodes are in a component with an odd cycle, both even and odd walks exist. If the component is bipartite, only paths with parity matching the 2-coloring exist. Doubling the graph nodes into 2N vertices (u: even, u+N: odd) seamlessly tracks component parity and odd cycles.

## 3. Step-by-Step Algorithm
1. 1. Maintain a DSU of size 2N + 2.
2. 2. For edge addition (u, v, z):
3.    - If z is even: union(u, v) and union(u+N, v+N).
4.    - If z is odd: union(u, v+N) and union(u+N, v).
5. 3. For query (u, v): check if find(u) == find(v). If true, output YES; otherwise NO.

## 4. Complexity Analysis
- **Time Complexity**: `O((N + Q) * alpha(N))`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

struct DSU {
    vector<int> parent;
    DSU(int n) : parent(n) {
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
        }
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    DSU dsu(2 * n + 2);

    for (int i = 0; i < q; ++i) {
        int w, x, y, z;
        cin >> w >> x >> y >> z;
        if (w == 1) {
            if (z % 2 == 0) {
                dsu.unite(x, y);
                dsu.unite(x + n, y + n);
            } else {
                dsu.unite(x, y + n);
                dsu.unite(x + n, y);
            }
        } else {
            if (dsu.find(x) == dsu.find(y)) {
                cout << "YES\n";
            } else {
                cout << "NO\n";
            }
        }
    }

    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
