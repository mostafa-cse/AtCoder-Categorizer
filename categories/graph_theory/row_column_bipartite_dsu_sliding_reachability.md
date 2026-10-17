# Row-Column Bipartite Graph DSU for Grid Sliding Reachability

**Domain**: `Graph Theory`  
**Subtopic**: `Connected Components`  

This workbook contains curated, high-quality competitive programming problems teaching **Row-Column Bipartite Graph DSU for Grid Sliding Reachability**.

---

## Curated Problems

### `[problem:AtCoder-arc112_d]` — Skate
- **Rating / Difficulty**: 2028
- **Contest**: `arc112`
- **Analysis**: [`analysis/AtCoder-arc112_d.md`](../../analysis/AtCoder-arc112_d.md)
- **Key Idea**: Movement along a row or column can switch direction when an obstacle '#' is encountered. Thus each obstacle (r, c) acts as an edge between row r and column c in a bipartite graph with vertices R_1..R_H and C_1..C_W. The grid boundaries and corners naturally connect row 1, row H, col 1, col W together into a single 'outer boundary' component. For all cells to be reachable, either all rows must belong to the boundary component, or all columns must belong to the boundary component. The minimum additional obstacles needed equals min(unconnected_rows, unconnected_cols).
- **Time Complexity**: `O(H * W * alpha(H + W))`
- **Space Complexity**: `O(H + W)`
- **Verified C++ Implementation**:
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
