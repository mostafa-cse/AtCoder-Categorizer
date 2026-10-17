# Problem Analysis: AtCoder-arc026_4 — D. Highway Construction

**Problem ID**: `AtCoder-arc026_4`  
**Contest**: `arc026`  
**Rating / Difficulty**: 2297  
**URL**: https://atcoder.jp/contests/arc026/tasks/arc026_4  
**VJudge Tag**: `[problem:AtCoder-arc026_4]`  
**Category File**: [`../categories/basics/binary_search_01_fractional_programming_mst.md`](../categories/basics/binary_search_01_fractional_programming_mst.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Leveraging Monotonicity`  
- **Topic (Skill)**: `Binary Search`  

---

## 1. Problem Statement & Key Idea
Given a connected undirected multigraph with edge costs $C_i$ and construction times $T_i$, find a connected spanning subgraph that minimizes the overall cost-to-time ratio $\frac{\sum C_e}{\sum T_e}$.

## 2. Core Observation & Invariant
In 0-1 fractional programming minimizing $\frac{\sum C_e}{\sum T_e} \le \lambda$, the objective is equivalent to determining whether there exists a connected spanning subgraph such that $\sum (C_e - \lambda T_e) \le 0$. Since we may include extra edges with $C_e - \lambda T_e < 0$, the optimal edge selection takes an MST on transformed weights $w_e = C_e - \lambda T_e$, plus all remaining negative edges.

## 3. Step-by-Step Algorithm
1. 1. We wish to minimize the ratio $\lambda = \frac{\sum C_e}{\sum T_e}$ over any connected spanning subgraph.
2. 2. Binary search on $\lambda \in [0, 10^6]$. For a fixed $\lambda$, the condition $\frac{\sum C_e}{\sum T_e} \le \lambda$ is equivalent to $\sum (C_e - \lambda T_e) \le 0$.
3. 3. Each edge has transformed weight $w_e(\lambda) = C_e - \lambda T_e$.
4. 4. To minimize the total weight of a connected spanning subgraph:
5.    - We must select at least a spanning tree to ensure connectivity.
6.    - Any remaining edge with $w_e(\lambda) < 0$ can be freely added to further decrease the sum.
7.    - Run Kruskal's algorithm on $w_e(\lambda)$: always take tree edges that connect components. For non-tree edges, take them if and only if $w_e(\lambda) < 0$.
8. 5. If the resulting sum is $\le 0$, $\lambda$ is achievable $\implies$ search left; otherwise search right. Running 80 iterations yields precision well within $10^{-3}$.

## 4. Complexity Analysis
- **Time Complexity**: `O(K \cdot M \log M)`
- **Space Complexity**: `O(N + M)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>
#include <iomanip>
#include <cmath>

using namespace std;

struct Edge {
    int u, v;
    long long c, t;
    double weight;
};

struct DSU {
    vector<int> parent;
    DSU(int n) {
        parent.resize(n);
        iota(parent.begin(), parent.end(), 0);
    }
    int find(int i) {
        if (parent[i] == i) return i;
        return parent[i] = find(parent[i]);
    }
    bool unite(int i, int j) {
        int ri = find(i), rj = find(j);
        if (ri != rj) {
            parent[ri] = rj;
            return true;
        }
        return false;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M;
    if (!(cin >> N >> M)) return 0;

    vector<Edge> edges(M);
    for (int i = 0; i < M; ++i) {
        cin >> edges[i].u >> edges[i].v >> edges[i].c >> edges[i].t;
    }

    auto check = [&](double lambda) {
        for (int i = 0; i < M; ++i) {
            edges[i].weight = edges[i].c - lambda * edges[i].t;
        }

        sort(edges.begin(), edges.end(), [](const Edge& a, const Edge& b) {
            return a.weight < b.weight;
        });

        DSU dsu(N);
        double total = 0;
        int tree_edges = 0;

        for (const auto& e : edges) {
            if (dsu.unite(e.u, e.v)) {
                total += e.weight;
                tree_edges++;
            } else if (e.weight < 0) {
                total += e.weight;
            }
        }

        return total <= 0;
    };

    double low = 0.0, high = 1e6;
    for (int iter = 0; iter < 80; ++iter) {
        double mid = (low + high) / 2.0;
        if (check(mid)) {
            high = mid;
        } else {
            low = mid;
        }
    }

    cout << fixed << setprecision(7) << high << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
