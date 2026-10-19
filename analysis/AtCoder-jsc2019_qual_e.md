# Problem Analysis: AtCoder-jsc2019_qual_e — Card Collector

**Problem ID**: `AtCoder-jsc2019_qual_e`  
**Contest**: `jsc2019_qual`  
**Rating / Difficulty**: 2691  
**URL**: https://atcoder.jp/contests/jsc2019_qual/tasks/jsc2019_qual_e  
**VJudge Tag**: `[problem:AtCoder-jsc2019_qual_e]`  
**Category File**: [`../categories/data_structures_ds/card_collector_dsu_pseudotree.md`](../categories/data_structures_ds/card_collector_dsu_pseudotree.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Disjoint Set Union (DSU)`  
- **Topic (Skill)**: `DSU / Union Find`  

---

## 1. Problem Statement & Key Idea
Each card at (R_i, C_i) represents an edge between row vertex R_i and column vertex H + C_i. A selection of cards is valid if each card can be assigned to either its row or column such that no row/column vertex receives more than 1 card. This is equivalent to orienting edges so that all in-degrees <= 1, which characterizes the bicircular matroid where every connected component has |E| <= |V| (at most 1 cycle per component). We solve this greedily using DSU with cycle tracking.

## 2. Core Observation & Invariant
A bipartite graph can be directed so all in-degrees <= 1 if and only if each component has at most as many edges as vertices (each component is a tree or a unicyclic pseudo-tree). By the greedy matroid property, sorting edges in descending order of value A_i and adding an edge whenever it does not create a component with >= 2 cycles yields the maximum possible total weight.

## 3. Step-by-Step Algorithm
1. 1. Represent rows 1..H and columns 1..W as H + W vertices in a DSU structure.
2. 2. For each component, maintain a boolean flag has_cycle, initially false.
3. 3. Sort all cards in descending order of value A_i.
4. 4. For each card with endpoints u and v:
5.    - Find roots ru and rv.
6.    - If ru == rv and not has_cycle[ru], mark has_cycle[ru] = true and add A_i to answer.
7.    - If ru != rv and not (has_cycle[ru] and has_cycle[rv]), unite ru and rv, set has_cycle[rv] = has_cycle[rv] or has_cycle[ru], and add A_i to answer.
8. 5. Output total weight.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N + (H + W) alpha(H + W))`
- **Space Complexity**: `O(N + H + W)`

## 5. C++ Source Code
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
    vector<bool> has_cycle;
    DSU(int n) : parent(n), has_cycle(n, false) {
        iota(parent.begin(), parent.end(), 0);
    }
    int find(int i) {
        if (parent[i] == i) return i;
        return parent[i] = find(parent[i]);
    }
    bool unite(int u, int v) {
        int ru = find(u);
        int rv = find(v);
        if (ru == rv) {
            if (!has_cycle[ru]) {
                has_cycle[ru] = true;
                return true;
            }
            return false;
        }
        if (has_cycle[ru] && has_cycle[rv]) {
            return false;
        }
        parent[ru] = rv;
        has_cycle[rv] = has_cycle[rv] || has_cycle[ru];
        return true;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, h, w;
    if (!(cin >> n >> h >> w)) return 0;

    vector<Edge> edges(n);
    for (int i = 0; i < n; ++i) {
        int r, c;
        long long a;
        cin >> r >> c >> a;
        edges[i] = {r, h + c, a};
    }

    sort(edges.begin(), edges.end(), [](const Edge& a, const Edge& b) {
        return a.w > b.w;
    });

    DSU dsu(h + w + 1);
    long long ans = 0;
    for (const auto& e : edges) {
        if (dsu.unite(e.u, e.v)) {
            ans += e.w;
        }
    }

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
