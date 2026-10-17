# Tree Diameter

**Domain**: `Graph Theory`  
**Subtopic**: `Graph Traversal`  

This workbook contains curated, high-quality competitive programming problems teaching **Tree Diameter**.

---

## Curated Problems

### `[problem:AtCoder-arc117_d]` — Miracle Tree
- **Rating / Difficulty**: 2115
- **Contest**: `arc117`
- **Analysis**: [`analysis/AtCoder-arc117_d.md`](../../analysis/AtCoder-arc117_d.md)
- **Key Idea**: If we traverse the tree in an Euler tour stepping along edges and incrementing a global time counter at each step, any two vertices have label difference >= tree distance (by triangle inequality). A standard tour visits each edge twice (taking 2(N-1) steps). To minimize the maximum time without returning to the root, we save steps equal to the depth of the last visited leaf! To maximize this savings, the path from the root to the last visited leaf must be the tree diameter. We find the diameter endpoints S and T, root at S, and visit the diameter child last at each branching step.
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int n;
vector<vector<int>> adj;
vector<int> dist_node;

void dfs_dist(int u, int p, int d) {
    dist_node[u] = d;
    for (int v : adj[u]) {
        if (v != p) dfs_dist(v, u, d + 1);
    }
}

int get_farthest(int start) {
    dist_node.assign(n + 1, 0);
    dfs_dist(start, 0, 0);
    int best = start;
    for (int i = 1; i <= n; ++i) {
        if (dist_node[i] > dist_node[best]) best = i;
    }
    return best;
}

vector<bool> on_diam;

bool find_path(int u, int p, int target) {
    if (u == target) {
        on_diam[u] = true;
        return true;
    }
    for (int v : adj[u]) {
        if (v != p && find_path(v, u, target)) {
            on_diam[u] = true;
            return true;
        }
    }
    return false;
}

vector<int> E;
int cur_time = 1;

void dfs_euler(int u, int p) {
    E[u] = cur_time;
    vector<int> non_diam_children;
    int diam_child = -1;
    for (int v : adj[u]) {
        if (v == p) continue;
        if (on_diam[v]) diam_child = v;
        else non_diam_children.push_back(v);
    }

    for (int v : non_diam_children) {
        cur_time++;
        dfs_euler(v, u);
        cur_time++;
    }

    if (diam_child != -1) {
        cur_time++;
        dfs_euler(diam_child, u);
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n)) return 0;

    adj.assign(n + 1, vector<int>());
    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    int S = get_farthest(1);
    int T = get_farthest(S);

    on_diam.assign(n + 1, false);
    find_path(S, 0, T);

    E.assign(n + 1, 0);
    dfs_euler(S, 0);

    for (int i = 1; i <= n; ++i) {
        cout << E[i] << (i == n ? "" : " ");
    }
    cout << "\n";

    return 0;
}
```
