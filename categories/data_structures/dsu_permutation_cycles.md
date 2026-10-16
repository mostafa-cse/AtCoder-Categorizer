# Permutation Position Cycles via DSU

**Domain**: `Data Structures`  
**Subtopic**: `Disjoint Set Union`  

This workbook contains curated, high-quality competitive programming problems teaching **Permutation Position Cycles via DSU**.

---

## Curated Problems

### [problem:AtCoder-arc097_b] — Equals
- **Contest**: `abc097`
- **Rating / Difficulty**: 1270
- **Specific Skill**: Permutation Position Cycles via DSU
- **Individual Analysis**: [`../../analysis/AtCoder-arc097_b.md`](../../analysis/AtCoder-arc097_b.md)
- **Problem Statement Summary**: Given permutation p_1..p_N. You can swap p_{x_j} and p_{y_j} for M given pairs (x_j, y_j) any number of times. Maximize the count of indices i where p_i == i.
- **Core Insight**: Build a Disjoint Set Union (DSU) where each given pair (x, y) unites the positions x and y. An element p_i can eventually be placed at position i if and only if its current position i and its target position p_i belong to the SAME connected component: find(i) == find(p_i)!
- **Complexity**: Time: `O((N + M) * alpha(N))` | Space: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <numeric>

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
        if (root_i != root_j) {
            parent[root_i] = root_j;
        }
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<int> p(n + 1);
    for (int i = 1; i <= n; ++i) {
        cin >> p[i];
    }

    DSU dsu(n);
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        dsu.unite(u, v);
    }

    int ans = 0;
    for (int i = 1; i <= n; ++i) {
        if (dsu.find(i) == dsu.find(p[i])) {
            ans++;
        }
    }

    cout << ans << "\n";
    return 0;
}
```
