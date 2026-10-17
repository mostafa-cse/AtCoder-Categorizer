# Virtual Tree / Auxiliary Tree

**Domain**: `Graph Theory`  
**Subtopic**: `More Tree Stuff`  

This workbook contains curated, high-quality competitive programming problems teaching **Virtual Tree / Auxiliary Tree**.

---

## Curated Problems

### `[problem:AtCoder-abc359_g]` — Sum of Tree Distance
- **Rating / Difficulty**: 2095
- **Contest**: `abc359`
- **Analysis**: [`analysis/AtCoder-abc359_g.md`](../../analysis/AtCoder-abc359_g.md)
- **Key Idea**: The distance between u and v is depth[u] + depth[v] - 2 * depth[LCA(u, v)]. For any color c with vertices V_c, sum_{u, v in V_c} (depth[u] + depth[v]) = (|V_c| - 1) * sum_{u in V_c} depth[u]. The critical part is computing sum_{u, v in V_c} depth[LCA(u, v)]. For each edge e = (p, child), this edge is traversed by all pairs of nodes of color c where one node lies in child's subtree and the other lies outside. Alternatively, using small-to-large merging (DSU on tree) with frequency maps, or virtual trees for each color, we can count the number of pairs passing through each subtree in O(N log N) total time.
- **Time Complexity**: `O(N log^2 N) with maps, or O(N log N) with virtual tree`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <map>

using namespace std;

int n;
vector<int> a;
vector<vector<int>> adj;
vector<int> depth;
long long total_ans = 0;

map<int, int>* dfs(int u, int p, int d) {
    depth[u] = d;
    map<int, int>* cur_map = new map<int, int>();
    (*cur_map)[a[u]] = 1;

    for (int v : adj[u]) {
        if (v == p) continue;
        map<int, int>* child_map = dfs(v, u, d + 1);

        if (child_map->size() > cur_map->size()) {
            swap(cur_map, child_map);
        }

        for (auto& entry : *child_map) {
            int color = entry.first;
            int cnt = entry.second;
            if (cur_map->count(color)) {
                long long pairs = 1LL * cnt * (*cur_map)[color];
                total_ans -= 2LL * d * pairs;
                (*cur_map)[color] += cnt;
            } else {
                (*cur_map)[color] = cnt;
            }
        }
        delete child_map;
    }
    return cur_map;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n)) return 0;

    a.resize(n + 1);
    for (int i = 1; i <= n; ++i) cin >> a[i];

    adj.assign(n + 1, vector<int>());
    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    depth.assign(n + 1, 0);

    // Run DFS with small-to-large
    map<int, int>* root_map = dfs(1, 0, 0);

    // Add depth[u] * (color_count - 1)
    for (int u = 1; u <= n; ++u) {
        int color = a[u];
        int count_color = (*root_map)[color];
        total_ans += 1LL * depth[u] * (count_color - 1);
    }

    delete root_map;

    cout << total_ans << "\n";
    return 0;
}
```
