# Forest Connected Components Identity (C = V - E) via Contribution to Sum

**Domain**: `Combinatorics`  
**Subtopic**: `Linearity of Expectation`  

This workbook contains curated, high-quality competitive programming problems teaching **Forest Connected Components Identity (C = V - E) via Contribution to Sum**.

---

## Curated Problems

### `[problem:AtCoder-abc173_f]` — Intervals on Tree
- **Rating / Difficulty**: 1892
- **Contest**: `abc173`
- **Analysis**: [`analysis/AtCoder-abc173_f.md`](../../analysis/AtCoder-abc173_f.md)
- **Key Idea**: Any induced subgraph of a tree is an acyclic graph (a forest). For every forest, Connected Components = Vertices - Edges. Thus, sum C(L, R) = sum V(L, R) - sum E(L, R).
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    long long total_v = 0;
    for (long long v = 1; v <= n; ++v) {
        total_v += v * (n - v + 1);
    }

    long long total_e = 0;
    for (int i = 0; i < n - 1; ++i) {
        long long u, v;
        cin >> u >> v;
        if (u > v) swap(u, v);
        total_e += u * (n - v + 1);
    }

    cout << total_v - total_e << "\n";
    return 0;
}
```
