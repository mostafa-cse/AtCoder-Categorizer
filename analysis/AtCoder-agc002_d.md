# Problem Analysis: AtCoder-agc002_d — D. Stamp Rally

**Problem ID**: `AtCoder-agc002_d`  
**Contest**: `agc002`  
**Rating / Difficulty**: 2514  
**URL**: https://atcoder.jp/contests/agc002/tasks/agc002_d  
**VJudge Tag**: `[problem:AtCoder-agc002_d]`  
**Category File**: [`../categories/data_structures_ds/stamp_rally_parallel_binary_search_dsu.md`](../categories/data_structures_ds/stamp_rally_parallel_binary_search_dsu.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Disjoint Set Union (DSU)`  
- **Topic (Skill)**: `Reachability Tree / DSU Tree / Kruskal Reconstruction Tree (KRT)`  

---

## 1. Problem Statement & Key Idea
Given an undirected graph of $N$ vertices and $M$ edges with weights $1 \dots M$, answer $Q$ queries: find the minimum edge weight $w$ such that at least $z$ distinct vertices can be visited starting from $x$ and $y$ using only edges with weight $\le w$. Using edges $\le w$, the set of reachable vertices is the union of the connected components of $x$ and $y$, containing $sz(find(x)) + sz(find(y)) - [find(x) == find(y)] sz(find(x))$ vertices.

## 2. Core Observation & Invariant
The number of reachable vertices is monotonically non-decreasing with respect to $w$. Thus, we can binary search for the minimum $w \in [1, M]$ for each query. Parallel Binary Search maintains the search intervals $[L_q, R_q]$ for all queries simultaneously. In each of $\lceil \log_2 M \rceil$ rounds, edges $1 \dots M$ are added to a DSU, and queries with midpoint $mid = (L_q + R_q) / 2$ are checked in $O(1)$ time.

## 3. Step-by-Step Algorithm
1. 1. Initialize binary search range $[L_q, R_q] = [1, M]$ for each query $q \in [1, Q]$.
2. 2. Run Parallel Binary Search for $\lceil \log_2 M \rceil$ rounds:
3.    a. Group queries by their midpoint $mid = (L_q + R_q) / 2$.
4.    b. Reset a DSU with component size tracking.
5.    c. Iterate edges $e = 1 \dots M$: union endpoints of edge $e$.
6.    d. Process all queries assigned to $mid = e$: compute reachable component size $|C(x) \cup C(y)|$.
7.    e. If reachable count $\ge z_q$, update $ans_q = mid$ and set $R_q = mid - 1$; else set $L_q = mid + 1$.
8. 3. Output $ans_q$ for all queries.

## 4. Complexity Analysis
- **Time Complexity**: `O((M + Q) \log M \cdot \alpha(N))`
- **Space Complexity**: `O(N + M + Q)`

## 5. C++ Source Code
```cpp

#include <iostream>
#include <vector>

using namespace std;

struct DSU {
    vector<int> parent;
    vector<int> sz;
    DSU(int n) : parent(n + 1), sz(n + 1, 1) {
        for (int i = 0; i <= n; ++i) parent[i] = i;
    }
    int find(int i) {
        if (parent[i] == i) return i;
        return parent[i] = find(parent[i]);
    }
    void unite(int i, int j) {
        int root_i = find(i);
        int root_j = find(j);
        if (root_i != root_j) {
            if (sz[root_i] < sz[root_j]) swap(root_i, root_j);
            parent[root_j] = root_i;
            sz[root_i] += sz[root_j];
        }
    }
};

struct Edge {
    int u, v;
};

struct Query {
    int x, y, z;
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<Edge> edges(m + 1);
    for (int i = 1; i <= m; ++i) {
        cin >> edges[i].u >> edges[i].v;
    }

    int q;
    if (!(cin >> q)) return 0;

    vector<Query> queries(q);
    for (int i = 0; i < q; ++i) {
        cin >> queries[i].x >> queries[i].y >> queries[i].z;
    }

    vector<int> L(q, 1), R(q, m), ans(q, m);

    while (true) {
        bool has_active = false;
        vector<vector<int>> mids(m + 1);
        for (int i = 0; i < q; ++i) {
            if (L[i] <= R[i]) {
                has_active = true;
                int mid = L[i] + (R[i] - L[i]) / 2;
                mids[mid].push_back(i);
            }
        }
        if (!has_active) break;

        DSU dsu(n);
        for (int e = 1; e <= m; ++e) {
            dsu.unite(edges[e].u, edges[e].v);
            for (int q_idx : mids[e]) {
                int x = queries[q_idx].x;
                int y = queries[q_idx].y;
                int z = queries[q_idx].z;
                int rx = dsu.find(x);
                int ry = dsu.find(y);
                int total_sz = (rx == ry) ? dsu.sz[rx] : (dsu.sz[rx] + dsu.sz[ry]);
                if (total_sz >= z) {
                    ans[q_idx] = e;
                    R[q_idx] = e - 1;
                } else {
                    L[q_idx] = e + 1;
                }
            }
        }
    }

    for (int i = 0; i < q; ++i) {
        cout << ans[i] << "\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
