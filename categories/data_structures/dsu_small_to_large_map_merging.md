# Disjoint Set Union with Small-to-Large Map Merging

**Domain**: `Data Structures`  
**Subtopic**: `Disjoint Set Union (DSU)`  

This workbook contains curated, high-quality competitive programming problems teaching **Disjoint Set Union with Small-to-Large Map Merging**.

---

## Curated Problems

### `[problem:AtCoder-abc183_f]` — Confluence
- **Rating / Difficulty**: 1586
- **Contest**: `abc183`
- **Analysis**: [`analysis/AtCoder-abc183_f.md`](../../analysis/AtCoder-abc183_f.md)
- **Key Idea**: Each DSU component maintains a frequency map `std::map<int, int>` of class counts. When uniting components, merge the smaller map into the larger map (small-to-large / sack heuristic).
- **Time Complexity**: `O(N log^2 N + Q log N)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <map>

using namespace std;

struct DSU {
    vector<int> parent;
    vector<map<int, int>> class_count;

    DSU(int n, const vector<int>& c) : parent(n + 1), class_count(n + 1) {
        for (int i = 1; i <= n; ++i) {
            parent[i] = i;
            class_count[i][c[i]] = 1;
        }
    }

    int find(int u) {
        return parent[u] == u ? u : parent[u] = find(parent[u]);
    }

    void unite(int u, int v) {
        int ru = find(u);
        int rv = find(v);
        if (ru == rv) return;

        if (class_count[ru].size() < class_count[rv].size()) {
            swap(ru, rv);
        }

        parent[rv] = ru;
        for (const auto& entry : class_count[rv]) {
            class_count[ru][entry.first] += entry.second;
        }
        class_count[rv].clear();
    }

    int query(int u, int cls) {
        int ru = find(u);
        auto it = class_count[ru].find(cls);
        return it != class_count[ru].end() ? it->second : 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    vector<int> c(n + 1);
    for (int i = 1; i <= n; ++i) {
        cin >> c[i];
    }

    DSU dsu(n, c);

    while (q--) {
        int type, x, y;
        cin >> type >> x >> y;
        if (type == 1) {
            dsu.unite(x, y);
        } else {
            cout << dsu.query(x, y) << "\n";
        }
    }

    return 0;
}
```
