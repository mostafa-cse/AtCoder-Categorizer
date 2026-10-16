# Distance-2 Tree Coloring Combinatorics via DFS

**Domain**: `Combinatorics`  
**Subtopic**: `Tree Combinatorics`  

This workbook contains curated, high-quality competitive programming problems teaching **Distance-2 Tree Coloring Combinatorics via DFS**.

---

## Curated Problems

### `[problem:AtCoder-abc133_e]` — Virus Tree 2
- **Rating / Difficulty**: 1505
- **Contest**: `abc133`
- **Analysis**: [`analysis/AtCoder-abc133_e.md`](../../analysis/AtCoder-abc133_e.md)
- **Key Idea**: Root the tree at vertex 1 and traverse top-down. The root has K choices. Its children have (K - 1), (K - 2), etc. For any deeper vertex v, its parent, grandparent, and already-colored siblings forbid colors, leaving K - 2 - (sibling index) choices.
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 1000000007;

long long ans = 1;
int K;

void dfs(int u, int p, const vector<vector<int>>& adj) {
    int available = (u == 1 ? K - 1 : K - 2);
    int used = 0;

    for (int v : adj[u]) {
        if (v != p) {
            long long choices = available - used;
            if (choices <= 0) {
                ans = 0;
                return;
            }
            ans = (ans * choices) % MOD;
            used++;
            dfs(v, u, adj);
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n >> K)) return 0;

    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    ans = K;
    dfs(1, 0, adj);

    cout << ans << "\n";
    return 0;
}
```
