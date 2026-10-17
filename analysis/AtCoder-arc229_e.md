# Problem Analysis: AtCoder-arc229_e — Taka and Hashi

**Problem ID**: `AtCoder-arc229_e`  
**Contest**: `arc229`  
**Rating / Difficulty**: 2004  
**URL**: https://atcoder.jp/contests/arc229/tasks/arc229_e  
**VJudge Tag**: `[problem:AtCoder-arc229_e]`  
**Category File**: [`../categories/graph_theory/multimodal_dual_dsu_equivalence_reachability.md`](../categories/graph_theory/multimodal_dual_dsu_equivalence_reachability.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Connected Components`  
- **Topic (Skill)**: `Multi-Modal Reachability via Dual DSU Equivalence Classes and Label-1 Traversal`  

---

## 1. Problem Statement & Key Idea
An undirected graph has edges labeled 1, 2, or 3. Takahashi can traverse label 1 edges. Takahashi can split into Taka (traverses label 2 edges) and Hashi (traverses label 3 edges). When both are at the same vertex, they merge back into Takahashi. Initially Takahashi is at vertex 1. Find all vertices where Takahashi can be.

**Key Idea**: Takahashi can move directly along label 1 edges. When splitting at u, Taka explores the connected component of u in G2, while Hashi explores the connected component of u in G3. They can merge at v if and only if v is in the same G2 component AND the same G3 component as u. Thus, splitting and merging allows instantaneous transitions between any two vertices that share the same equivalence class pair (comp_2[v], comp_3[v]). In the final reachability graph, vertices in the same (comp_2, comp_3) bucket are unified, along with all label 1 edges.

## 2. Core Observation & Invariant
Independent movement of two entities with a common rendezvous condition induces an equivalence relation defined by the intersection of their individual component partitions.

## 3. Step-by-Step Algorithm
1. Build DSU_2 on label 2 edges; record comp2[v] = DSU_2.find(v).
2. Build DSU_3 on label 3 edges; record comp3[v] = DSU_3.find(v).
3. Build DSU_all for overall reachability.
4. Group vertices by (comp2[v], comp3[v]); union all vertices within each group in DSU_all.
5. Union all endpoints of label 1 edges in DSU_all.
6. Collect all vertices v where DSU_all.find(v) == DSU_all.find(1). Output count and sorted vertices.

## 4. Complexity Analysis
- **Time Complexity**: `O((N + M) log N)`
- **Space Complexity**: `O(N + M)`

## 5. Core Algorithmic Skill & Learning Takeaway
Multi-agent reachability decomposition into independent component intersections.

**Reusable Pattern**: Component Intersection Graph: Vertices u, v can rendezvous across two subgraphs iff comp_A(u) == comp_A(v) and comp_B(u) == comp_B(v).

## 6. Comparison with Alternative Approaches
Matches official editorial.

## 7. Verified Clean C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>
#include <map>

using namespace std;

struct DSU {
    int n;
    vector<int> parent;
    DSU(int n) : n(n), parent(n + 1) {
        iota(parent.begin(), parent.end(), 0);
    }
    int find(int i) {
        if (parent[i] == i)
            return i;
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

void solve() {
    int n, m;
    if (!(cin >> n >> m)) return;

    struct Edge {
        int u, v, l;
    };
    vector<Edge> edges(m);
    for (int i = 0; i < m; ++i) {
        cin >> edges[i].u >> edges[i].v >> edges[i].l;
    }

    DSU dsu2(n), dsu3(n);
    for (const auto& e : edges) {
        if (e.l == 2) dsu2.unite(e.u, e.v);
        if (e.l == 3) dsu3.unite(e.u, e.v);
    }

    map<pair<int, int>, int> head;
    DSU dsu_all(n);

    for (int i = 1; i <= n; ++i) {
        pair<int, int> key = {dsu2.find(i), dsu3.find(i)};
        if (head.find(key) == head.end()) {
            head[key] = i;
        } else {
            dsu_all.unite(head[key], i);
        }
    }

    for (const auto& e : edges) {
        if (e.l == 1) {
            dsu_all.unite(e.u, e.v);
        }
    }

    int root1 = dsu_all.find(1);
    vector<int> ans;
    for (int i = 1; i <= n; ++i) {
        if (dsu_all.find(i) == root1) {
            ans.push_back(i);
        }
    }

    cout << ans.size() << "\n";
    for (size_t i = 0; i < ans.size(); ++i) {
        cout << ans[i] << (i + 1 == ans.size() ? "" : " ");
    }
    cout << "\n";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    if (cin >> t) {
        while (t--) {
            solve();
        }
    }
    return 0;
}
```
