# Problem Analysis: AtCoder-typical90_l — Red Painting

**Problem ID**: `AtCoder-typical90_l`  
**Contest**: `typical90` (Kyopro Typical 90, Problem 012)  
**Rating / Difficulty**: 1250 (★4)  
**URL**: https://atcoder.jp/contests/typical90/tasks/typical90_l  
**VJudge Tag**: `[problem:AtCoder-typical90_l]`  
**Category File**: [`../categories/data_structures/online_grid_dsu.md`](../categories/data_structures/online_grid_dsu.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Disjoint Set Union (DSU)`  
- **Topic (Skill)**: `Grid Connectivity / Dynamic DSU`  

---

## 1. Problem Statement & Key Idea
H x W grid initially white. Q queries: (1) paint cell (r, c) red, (2) query if two red cells are in the same 4-connected component.

**Core Idea**: Linearize 2D coordinates to 1D integers (r * W + c) and maintain connectivity with Disjoint Set Union.

## 2. Core Observation & Invariant
When cell (r, c) becomes red, union it with any of its 4 orthogonal neighbors that are already red.

## 3. Step-by-Step Algorithm
1. Initialize DSU with H*W elements.
2. Query 1: mark is_red[u] = true; for each orthogonal neighbor v: if is_red[v], dsu.unite(u, v).
3. Query 2: if both are red and dsu.same(u, v): 'Yes' else 'No'.

## 4. Complexity Analysis
Time: O(Q alpha(HW)), Space: O(HW).

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>

using namespace std;

struct DSU {
    vector<int> parent, rank;
    DSU(int n) : parent(n), rank(n, 0) {
        for (int i = 0; i < n; ++i) parent[i] = i;
    }
    int find(int i) {
        if (parent[i] == i) return i;
        return parent[i] = find(parent[i]);
    }
    bool unite(int i, int j) {
        int root_i = find(i), root_j = find(j);
        if (root_i != root_j) {
            if (rank[root_i] < rank[root_j]) swap(root_i, root_j);
            parent[root_j] = root_i;
            if (rank[root_i] == rank[root_j]) rank[root_i]++;
            return true;
        }
        return false;
    }
    bool same(int i, int j) {
        return find(i) == find(j);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int h, w, q;
    if (!(cin >> h >> w >> q)) return 0;

    DSU dsu(h * w);
    vector<bool> is_red(h * w, false);

    int dr[] = {-1, 1, 0, 0};
    int dc[] = {0, 0, -1, 1};

    while (q--) {
        int type;
        cin >> type;
        if (type == 1) {
            int r, c;
            cin >> r >> c;
            --r; --c;
            int u = r * w + c;
            is_red[u] = true;
            for (int k = 0; k < 4; ++k) {
                int nr = r + dr[k], nc = c + dc[k];
                if (nr >= 0 && nr < h && nc >= 0 && nc < w) {
                    int v = nr * w + nc;
                    if (is_red[v]) dsu.unite(u, v);
                }
            }
        } else {
            int ra, ca, rb, cb;
            cin >> ra >> ca >> rb >> cb;
            --ra; --ca; --rb; --cb;
            int u = ra * w + ca, v = rb * w + cb;
            if (is_red[u] && is_red[v] && dsu.same(u, v)) {
                cout << "Yes\n";
            } else {
                cout << "No\n";
            }
        }
    }
    return 0;
}
```

## 6. Editorial Comparison & Alignment
2D-to-1D index linearization and online union-find connectivity.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Grid linearization and dynamic connected component maintenance with DSU.
- **Reusable Pattern**: `Online Grid DSU with Neighbor Unions.`

---
Back to [Grid Connectivity / Dynamic DSU](../categories/data_structures/online_grid_dsu.md) | [Categories Directory](../categories/README.md)