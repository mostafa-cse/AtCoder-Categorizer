# DFS Tree

**Domain**: `Graph Theory`  
**Subtopic**: `Graph Traversal`  

This workbook contains curated, high-quality competitive programming problems teaching **DFS Tree**.

---

## Curated Problems

### `[problem:AtCoder-abc244_g]` — Construct Good Path
- **Rating / Difficulty**: 2117
- **Contest**: `abc244`
- **Analysis**: [`analysis/AtCoder-abc244_g.md`](../../analysis/AtCoder-abc244_g.md)
- **Key Idea**: Build a DFS spanning tree of the graph. Traverse the tree. When returning from a child v to parent u, check if the current visit parity of v matches S_v. If not, take an immediate 2-step detour u -> v -> u! This detour flips the parity of v while visiting u twice (leaving u's parity completely unchanged). Backtracking in this bottom-up manner fixes all vertices' parities. If the root's parity is incorrect at the very end, simply omit the final step of the walk.
- **Time Complexity**: `O(N + M)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

int n, m;
vector<vector<int>> adj;
string s;
vector<bool> visited;
vector<int> path;
vector<int> cur_parity;

void dfs(int u) {
    visited[u] = true;
    path.push_back(u);
    cur_parity[u] ^= 1;

    for (int v : adj[u]) {
        if (!visited[v]) {
            dfs(v);
            path.push_back(u);
            cur_parity[u] ^= 1;

            if (cur_parity[v] != (s[v - 1] - '0')) {
                path.push_back(v);
                cur_parity[v] ^= 1;
                path.push_back(u);
                cur_parity[u] ^= 1;
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n >> m)) return 0;

    adj.assign(n + 1, vector<int>());
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    cin >> s;

    visited.assign(n + 1, false);
    cur_parity.assign(n + 1, 0);

    dfs(1);

    if (cur_parity[1] != (s[0] - '0')) {
        path.pop_back();
        cur_parity[1] ^= 1;
    }

    cout << path.size() << "\n";
    for (int i = 0; i < (int)path.size(); ++i) {
        cout << path[i] << (i + 1 == (int)path.size() ? "" : " ");
    }
    cout << "\n";

    return 0;
}
```
