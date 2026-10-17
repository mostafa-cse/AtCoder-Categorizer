# Problem Analysis: AtCoder-arc112_d — Skate

**Problem ID**: `AtCoder-arc112_d`  
**Contest**: `arc112`  
**Rating / Difficulty**: 2028  
**URL**: https://atcoder.jp/contests/arc112/tasks/arc112_d  
**VJudge Tag**: `[problem:AtCoder-arc112_d]`  
**Category File**: [`../categories/graph_theory/row_column_bipartite_dsu_sliding_reachability.md`](../categories/graph_theory/row_column_bipartite_dsu_sliding_reachability.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Connected Components`  
- **Topic (Skill)**: `Row-Column Bipartite Graph DSU for Grid Sliding Reachability`  

---

## 1. Problem Statement & Key Idea
An H x W grid has obstacles '#'. A skater slides continuously in cardinal directions until hitting a wall '#' or boundary. Find the minimum number of walls to add so that every cell is reachable from the starting configuration.

**Key Idea**: Movement along a row or column can switch direction when an obstacle '#' is encountered. Thus each obstacle (r, c) acts as an edge between row r and column c in a bipartite graph with vertices R_1..R_H and C_1..C_W. The grid boundaries and corners naturally connect row 1, row H, col 1, col W together into a single 'outer boundary' component. For all cells to be reachable, either all rows must belong to the boundary component, or all columns must belong to the boundary component. The minimum additional obstacles needed equals min(unconnected_rows, unconnected_cols).

## 2. Core Observation & Invariant
Sliding dynamics reduce the 2D grid to a row-column bipartite graph where obstacles are edges, and full reachability requires spanning all rows or all columns.

## 3. Step-by-Step Algorithm
1. Initialize DSU on H + W vertices (1..H for rows, H+1..H+W for columns).
2. Unite boundaries: row 1, row H, col 1, col W are all in the boundary component.
3. For each '#' at (r, c): unite(r, H + c).
4. Identify the boundary component root = dsu.find(1).
5. Count distinct row components disconnected from the boundary root.
6. Count distinct column components disconnected from the boundary root.
7. Output min(row_components, col_components).

## 4. Complexity Analysis
- **Time Complexity**: `O(H * W * alpha(H + W))`
- **Space Complexity**: `O(H + W)`

## 5. Core Algorithmic Skill & Learning Takeaway
Row-column bipartite graph modeling of sliding obstacle reachability.

**Reusable Pattern**: Row-Column Bipartite DSU: Connect row r and col c for each obstacle; answer is minimum unlinked rows/cols.

## 6. Comparison with Alternative Approaches
Matches official editorial.

## 7. Verified Clean C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <numeric>
#include <set>
#include <algorithm>

using namespace std;

struct DSU {
    vector<int> parent;
    DSU(int n) : parent(n + 1) {
        iota(parent.begin(), parent.end(), 0);
    }
    int find(int i) {
        if (parent[i] == i) return i;
        return parent[i] = find(parent[i]);
    }
    void unite(int i, int j) {
        int root_i = find(i);
        int root_j = find(j);
        if (root_i != root_j) parent[root_i] = root_j;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int h, w;
    if (!(cin >> h >> w)) return 0;

    vector<string> grid(h);
    for (int i = 0; i < h; ++i) {
        cin >> grid[i];
    }

    DSU dsu(h + w);

    // Row 1, Row H, Col 1, Col W are naturally connected via borders
    dsu.unite(1, h);
    dsu.unite(1, h + 1);
    dsu.unite(1, h + w);

    for (int r = 0; r < h; ++r) {
        for (int c = 0; c < w; ++c) {
            if (grid[r][c] == '#') {
                dsu.unite(r + 1, h + c + 1);
            }
        }
    }

    int boundary_root = dsu.find(1);

    set<int> row_roots;
    for (int r = 1; r <= h; ++r) {
        int rt = dsu.find(r);
        if (rt != boundary_root) {
            row_roots.insert(rt);
        }
    }

    set<int> col_roots;
    for (int c = 1; c <= w; ++c) {
        int rt = dsu.find(h + c);
        if (rt != boundary_root) {
            col_roots.insert(rt);
        }
    }

    cout << min(row_roots.size(), col_roots.size()) << "\n";
    return 0;
}
```
