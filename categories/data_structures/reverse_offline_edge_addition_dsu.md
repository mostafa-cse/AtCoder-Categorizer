# Reverse Offline Edge Addition with DSU Connected Component Pairs

**Domain**: `Data Structures`  
**Subtopic**: `Disjoint Set Union`  

This workbook contains curated, high-quality competitive programming problems teaching **Reverse Offline Edge Addition with DSU Connected Component Pairs**.

---

## Curated Problems

### [problem:AtCoder-abc120_d] — Decayed Bridges
- **Contest**: `abc120`
- **Rating / Difficulty**: 1355
- **Specific Skill**: Reverse Offline Edge Addition with DSU Connected Component Pairs
- **Individual Analysis**: [`../../analysis/AtCoder-abc120_d.md`](../../analysis/AtCoder-abc120_d.md)
- **Problem Statement Summary**: N islands initially connected by M bridges. In each step i from 1 to M, bridge i collapses. 'Inconvenience' is the number of pairs (u, v) with u < v that cannot reach each other. Find inconvenience after each bridge collapses.
- **Core Insight**: Initially (with no bridges), all C(N, 2) pairs are disconnected. When adding an edge between u and v: if u and v are in different DSU components of size sz[u] and sz[v], adding this bridge connects sz[u] * sz[v] new pairs of islands, decreasing inconvenience by sz[u] * sz[v]!
- **Complexity**: Time: `O((N + M) * alpha(N))` | Space: `O(N + M)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

struct DSU {
    vector<int> parent;
    vector<int> sz;
    DSU(int n) : parent(n + 1), sz(n + 1, 1) {
        iota(parent.begin(), parent.end(), 0);
    }
    int find(int i) {
        if (parent[i] == i) return i;
        return parent[i] = find(parent[i]);
    }
    bool unite(int i, int j, long long& delta) {
        int root_i = find(i);
        int root_j = find(j);
        if (root_i != root_j) {
            delta = (long long)sz[root_i] * sz[root_j];
            parent[root_i] = root_j;
            sz[root_j] += sz[root_i];
            return true;
        }
        delta = 0;
        return false;
    }
};

struct Edge {
    int u, v;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<Edge> edges(m);
    for (int i = 0; i < m; ++i) {
        cin >> edges[i].u >> edges[i].v;
    }

    DSU dsu(n);
    long long cur_inconvenience = (long long)n * (n - 1) / 2;
    vector<long long> ans(m);

    for (int i = m - 1; i >= 0; --i) {
        ans[i] = cur_inconvenience;
        long long delta = 0;
        dsu.unite(edges[i].u, edges[i].v, delta);
        cur_inconvenience -= delta;
    }

    for (int i = 0; i < m; ++i) {
        cout << ans[i] << "\n";
    }

    return 0;
}
```
