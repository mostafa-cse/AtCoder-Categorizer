# Potentialized Disjoint Set Union (Weighted DSU)

**Domain**: `Data Structures`  
**Subtopic**: `Disjoint Set Union (DSU)`  

This workbook contains curated, high-quality competitive programming problems teaching **Potentialized Disjoint Set Union (Weighted DSU)**.

---

## Curated Problems

### `[problem:AtCoder-arc090_b]` — People on a Line
- **Rating / Difficulty**: 1452
- **Contest**: `abc087`
- **Analysis**: [`analysis/AtCoder-arc090_b.md`](../../analysis/AtCoder-arc090_b.md)
- **Key Idea**: Use Potentialized (Weighted) DSU to maintain relative distance offsets pos[u] - pos[root[u]].
- **Time Complexity**: `O((N + M) * alpha(N))`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>

using namespace std;

struct WeightedDSU {
    vector<int> parent;
    vector<long long> weight; // weight[i] = pos[i] - pos[parent[i]]

    WeightedDSU(int n) : parent(n + 1), weight(n + 1, 0) {
        for (int i = 0; i <= n; ++i) parent[i] = i;
    }

    int find(int u) {
        if (parent[u] == u) return u;
        int root = find(parent[u]);
        weight[u] += weight[parent[u]];
        return parent[u] = root;
    }

    // Enforce pos[v] - pos[u] = d
    bool unite(int u, int v, long long d) {
        int ru = find(u);
        int rv = find(v);
        if (ru == rv) {
            return (weight[v] - weight[u] == d);
        }
        parent[rv] = ru;
        weight[rv] = d + weight[u] - weight[v];
        return true;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    WeightedDSU dsu(n);

    for (int i = 0; i < m; ++i) {
        int l, r;
        long long d;
        cin >> l >> r >> d;
        if (!dsu.unite(l, r, d)) {
            cout << "No\n";
            return 0;
        }
    }

    cout << "Yes\n";
    return 0;
}
```
