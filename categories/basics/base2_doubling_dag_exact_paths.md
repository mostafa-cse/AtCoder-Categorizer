# Base-2 Doubling DAG Construction for Exact Path Interval [0, L - 1]

**Domain**: `Basics`  
**Subtopic**: `Constructive`  

This workbook contains curated, high-quality competitive programming problems teaching **Base-2 Doubling DAG Construction for Exact Path Interval [0, L - 1]**.

---

## Curated Problems

### `[problem:AtCoder-arc102_b]` — All Your Paths are Different Lengths
- **Rating / Difficulty**: 1810
- **Contest**: `abc108`
- **Analysis**: [`analysis/AtCoder-arc102_b.md`](../../analysis/AtCoder-arc102_b.md)
- **Key Idea**: Find largest r such that 2^r <= L. Create a spine of vertices 1 to r + 1. Between vertex i and i + 1, add two edges with weights 0 and 2^{i-1}. This produces all path lengths in [0, 2^r - 1]. Then for remaining bits in L, add bypass edges directly to vertex r + 1.
- **Time Complexity**: `O(log L)`
- **Space Complexity**: `O(log L)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>

using namespace std;

struct Edge {
    int u, v, w;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int L;
    if (!(cin >> L)) return 0;

    int r = 0;
    while ((1 << (r + 1)) <= L) r++;

    int n = r + 1;
    vector<Edge> edges;

    for (int i = 1; i <= r; ++i) {
        edges.push_back({i, i + 1, 0});
        edges.push_back({i, i + 1, 1 << (i - 1)});
    }

    int cur_val = 1 << r;
    for (int k = r - 1; k >= 0; --k) {
        if ((L >> k) & 1) {
            edges.push_back({k + 1, n, cur_val});
            cur_val += (1 << k);
        }
    }

    cout << n << " " << edges.size() << "\n";
    for (auto& e : edges) {
        cout << e.u << " " << e.v << " " << e.w << "\n";
    }

    return 0;
}
```
