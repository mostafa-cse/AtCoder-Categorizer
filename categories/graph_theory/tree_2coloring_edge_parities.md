# Tree 2-Coloring via Edge Weight Parities

**Domain**: `Graph Theory`  
**Subtopic**: `Tree Coloring`  

This workbook contains curated, high-quality competitive programming problems teaching **Tree 2-Coloring via Edge Weight Parities**.

---

## Curated Problems

### [problem:AtCoder-abc126_d] — Even Relation
- **Contest**: `abc126`
- **Rating / Difficulty**: 1279
- **Specific Skill**: Tree 2-Coloring via Edge Weight Parities
- **Individual Analysis**: [`../../analysis/AtCoder-abc126_d.md`](../../analysis/AtCoder-abc126_d.md)
- **Problem Statement Summary**: Given a weighted tree with N vertices. Color vertices with 0 or 1 such that any two vertices with the same color have an EVEN shortest path distance.
- **Core Insight**: Notice that 2 * dist(root, LCA) is always even! Thus, dist(u, v) = dist(root, u) + dist(root, v) (mod 2). For dist(u, v) to be even, dist(root, u) and dist(root, v) must have the EXACT SAME parity! Therefore, we simply color each vertex based on the parity of its distance from root 1: color[u] = dist(1, u) % 2.
- **Complexity**: Time: `O(N)` | Space: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>

using namespace std;

struct Edge {
    int to;
    long long w;
};

void dfs(int u, int p, long long d, const vector<vector<Edge>>& adj, vector<int>& color) {
    color[u] = d % 2;
    for (const auto& e : adj[u]) {
        if (e.to != p) {
            dfs(e.to, u, d + e.w, adj, color);
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<Edge>> adj(n + 1);
    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        long long w;
        cin >> u >> v >> w;
        adj[u].push_back({v, w});
        adj[v].push_back({u, w});
    }

    vector<int> color(n + 1, 0);
    dfs(1, 0, 0, adj, color);

    for (int i = 1; i <= n; ++i) {
        cout << color[i] << "\n";
    }

    return 0;
}
```
