# System of Parity Constraints / DSU Component Count

**Domain**: `Data Structures`  
**Subtopic**: `Disjoint Set Union`  

This workbook contains curated, high-quality competitive programming problems teaching **System of Parity Constraints / DSU Component Count**.

---

## Curated Problems

### [problem:AtCoder-abc126_e] — 1 or 2
- **Contest**: `abc126`
- **Rating / Difficulty**: 1340
- **Specific Skill**: System of Parity Constraints / DSU Component Count
- **Individual Analysis**: [`../../analysis/AtCoder-abc126_e.md`](../../analysis/AtCoder-abc126_e.md)
- **Problem Statement Summary**: N cards with numbers 1 or 2. M clues: (X_i, Y_i, Z_i) means A_{X_i} + A_{Y_i} + Z_i is even. Find the minimum number of cards to reveal to determine all cards.
- **Core Insight**: Each clue defines an undirected edge between card X and card Y in a knowledge graph. In any connected component, revealing the value of just ONE card determines the values of all other cards in that component! Therefore, the minimum cards needed equals the number of connected components in the graph.
- **Complexity**: Time: `O((N + M) * alpha(N))` | Space: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

struct DSU {
    vector<int> parent;
    int components;
    DSU(int n) : parent(n + 1), components(n) {
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
            components--;
        }
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    DSU dsu(n);
    for (int i = 0; i < m; ++i) {
        int x, y, z;
        cin >> x >> y >> z;
        dsu.unite(x, y);
    }

    cout << dsu.components << "\n";
    return 0;
}
```
