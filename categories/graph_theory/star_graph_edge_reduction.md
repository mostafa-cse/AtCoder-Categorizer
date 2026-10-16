# Star Graph Baseline with Redundant Edge Reduction

**Domain**: `Graph Theory`  
**Subtopic**: `Constructive Graph Theory`  

This workbook contains curated, high-quality competitive programming problems teaching **Star Graph Baseline with Redundant Edge Reduction**.

---

## Curated Problems

### `[problem:AtCoder-abc131_e]` — Friendships
- **Rating / Difficulty**: 1433
- **Contest**: `abc131`
- **Analysis**: [`analysis/AtCoder-abc131_e.md`](../../analysis/AtCoder-abc131_e.md)
- **Key Idea**: A star graph with center 1 connected to leaves 2..N achieves the maximum possible number of distance-2 pairs: C(N-1, 2). Adding an edge between two leaves reduces the count of distance-2 pairs by exactly 1.
- **Time Complexity**: `O(N^2)`
- **Space Complexity**: `O(N^2)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    int max_k = (n - 1) * (n - 2) / 2;
    if (k > max_k) {
        cout << -1 << "\n";
        return 0;
    }

    vector<pair<int, int>> edges;
    // Base star graph
    for (int i = 2; i <= n; ++i) {
        edges.push_back({1, i});
    }

    // Add leaf edges to reduce distance-2 count by 1 each
    int needed = max_k - k;
    for (int u = 2; u <= n && needed > 0; ++u) {
        for (int v = u + 1; v <= n && needed > 0; ++v) {
            edges.push_back({u, v});
            needed--;
        }
    }

    cout << edges.size() << "\n";
    for (const auto& e : edges) {
        cout << e.first << " " << e.second << "\n";
    }

    return 0;
}
```
