# Equivalence Relation Component Collapse via DSU

**Domain**: `Data Structures`  
**Subtopic**: `Disjoint Set Union (DSU)`  

This workbook contains curated, high-quality competitive programming problems teaching **Equivalence Relation Component Collapse via DSU**.

---

## Curated Problems

### [problem:AtCoder-abc206_d] — KAIBUNsyo
- **Contest**: `abc206`
- **Rating / Difficulty**: 879
- **Specific Skill**: Equivalence Relation Component Collapse via DSU
- **Individual Analysis**: [`../../analysis/AtCoder-abc206_d.md`](../../analysis/AtCoder-abc206_d.md)
- **Problem Statement Summary**: Given an array A of length N <= 200000. In one operation, choose two integers x and y and replace all occurrences of x with y. Find the minimum operations to make A a palindrome.
- **Core Insight**: Treat each distinct value as a node in an equivalence graph, with an edge between A[i] and A[N - 1 - i]. To make all values in a connected component of size V_c identical, we need exactly V_c - 1 replacement operations. Summing over all components, answer is total distinct values minus number of connected components, solved immediately via DSU.
- **Complexity**: Time: `O(N * alpha(V))` | Space: `O(V)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

struct DSU {
    vector<int> parent;
    DSU(int n) : parent(n) {
        iota(parent.begin(), parent.end(), 0);
    }
    int find(int i) {
        if (parent[i] == i)
            return i;
        return parent[i] = find(parent[i]);
    }
    bool unite(int i, int j) {
        int root_i = find(i);
        int root_j = find(j);
        if (root_i != root_j) {
            parent[root_i] = root_j;
            return true;
        }
        return false;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> a(n);
    int max_val = 0;
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        max_val = max(max_val, a[i]);
    }

    DSU dsu(max_val + 1);
    int ops = 0;

    for (int i = 0; i < n / 2; ++i) {
        int u = a[i];
        int v = a[n - 1 - i];
        if (u != v) {
            if (dsu.unite(u, v)) {
                ops++;
            }
        }
    }

    cout << ops << "\n";
    return 0;
}
```
