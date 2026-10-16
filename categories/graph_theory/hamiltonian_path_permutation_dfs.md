# Hamiltonian Path Permutation DFS

**Domain**: `Graph Theory`  
**Subtopic**: `Hamiltonian Paths`  

This workbook contains curated, high-quality competitive programming problems teaching **Hamiltonian Path Permutation DFS**.

---

## Curated Problems

### [problem:AtCoder-abc054_c] — One-stroke Path
- **Contest**: `abc054`
- **Rating / Difficulty**: 1244
- **Specific Skill**: Hamiltonian Path Permutation DFS
- **Individual Analysis**: [`../../analysis/AtCoder-abc054_c.md`](../../analysis/AtCoder-abc054_c.md)
- **Problem Statement Summary**: Given an undirected graph with N vertices and M edges. Count the number of paths starting at vertex 1 that visit every vertex exactly once (N <= 8).
- **Core Insight**: Because N <= 8, the total number of permutations of vertices starting with vertex 1 is (N - 1)! <= 7! = 5040. We can either test all permutations with std::next_permutation or perform a simple backtracking DFS with visited bitmask.
- **Complexity**: Time: `O(N!)` | Space: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>

using namespace std;

int n, m;
vector<vector<int>> adj;

int dfs(int u, int mask) {
    if (mask == (1 << n) - 1) return 1;

    int total_paths = 0;
    for (int v : adj[u]) {
        if (!((mask >> v) & 1)) {
            total_paths += dfs(v, mask | (1 << v));
        }
    }
    return total_paths;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n >> m)) return 0;

    adj.resize(n);
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        u--; v--; // 0-indexed
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    cout << dfs(0, 1) << "\n";
    return 0;
}
```
