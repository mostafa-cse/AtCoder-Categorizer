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
