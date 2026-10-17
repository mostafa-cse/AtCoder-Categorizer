# Problem Analysis: AtCoder-abc295_g — Minimum Path

**Problem ID**: `AtCoder-abc295_g`  
**Contest**: `abc295`  
**Rating / Difficulty**: 2086  
**URL**: https://atcoder.jp/contests/abc295/tasks/abc295_g  
**VJudge Tag**: `[problem:AtCoder-abc295_g]`  
**Category File**: [`../categories/data_structures/cycle_contraction_tree_ancestors_dsu.md`](../categories/data_structures/cycle_contraction_tree_ancestors_dsu.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Disjoint Set Union (DSU)`  
- **Topic (Skill)**: `DSU / Union Find`  

---

## 1. Problem Statement & Key Idea
Given a rooted tree with N vertices rooted at 1, where every edge is directed from parent p_i to child i (so p_i < i). Process Q queries of two types: 1) Add a directed edge from u to v (where v is an ancestor of u). 2) Find the minimum numbered vertex reachable from x.

**Key Insight**: Initially, from any vertex x, the reachable vertices are only its descendants. When an edge u -> v is added, since v is an ancestor of u, all vertices on the path between v and u form a strongly connected component! Any query asking for the minimum reachable vertex in this cycle can now reach v (and since p_i < i, v has a smaller index than any other node on the path). By using DSU to contract each node along the tree path from u up to v into a single component whose representative stores the highest ancestor (minimum index), each tree edge is contracted at most once. Queries simply output the highest ancestor of the DSU component containing x.

## 2. Core Observation & Invariant
Back-edges to ancestors contract tree paths into strongly connected components. DSU with path compression collapses each tree edge at most once in O(alpha(N)).

## 3. Step-by-Step Algorithm
1. Initialize DSU for N vertices where min_ancestor[find(i)] = i.
2. For query 1 (add edge u -> v):
3.   While find(u) != find(v):
4.     Let top_u = min_ancestor[find(u)].
5.     If top_u <= v, break.
6.     Let parent_node = parent[top_u].
7.     Merge find(u) with find(parent_node), updating min_ancestor.
8.     u = parent_node.
9. For query 2 (query x):
10.   Output min_ancestor[find(x)].

## 4. Complexity Analysis
- **Time Complexity**: `O((N + Q) alpha(N))`
- **Space Complexity**: `O(N)`

## 5. Core Skill & Reusable Pattern
- **Core Skill**: Amortized tree path contraction using DSU to maintain strongly connected component representatives.
- **Reusable Pattern**: Adding back-edges to ancestors on a directed tree contracts ancestor paths into DSU components with amortized O(N alpha(N)) total merges.

## 6. Editorial Comparison & Alternative Approaches
Matches official editorial.

## 7. Verified C++17 Implementation
```cpp
#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

struct DSU {
    vector<int> parent;
    vector<int> min_ancestor;

    DSU(int n) : parent(n + 1), min_ancestor(n + 1) {
        iota(parent.begin(), parent.end(), 0);
        iota(min_ancestor.begin(), min_ancestor.end(), 0);
    }

    int find(int i) {
        if (parent[i] == i)
            return i;
        return parent[i] = find(parent[i]);
    }

    void unite(int u, int v) {
        int root_u = find(u);
        int root_v = find(v);
        if (root_u != root_v) {
            parent[root_u] = root_v;
            min_ancestor[root_v] = min(min_ancestor[root_v], min_ancestor[root_u]);
        }
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> p(n + 1);
    for (int i = 2; i <= n; ++i) {
        cin >> p[i];
    }

    DSU dsu(n);

    int q;
    if (!(cin >> q)) return 0;

    while (q--) {
        int type;
        cin >> type;
        if (type == 1) {
            int u, v;
            cin >> u >> v;
            u = dsu.min_ancestor[dsu.find(u)];
            while (u > v) {
                int par = p[u];
                dsu.unite(u, par);
                u = dsu.min_ancestor[dsu.find(u)];
            }
        } else {
            int x;
            cin >> x;
            cout << dsu.min_ancestor[dsu.find(x)] << "\n";
        }
    }

    return 0;
}
```
