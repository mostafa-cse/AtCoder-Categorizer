# Small-to-Large Tree Rerooting for Online Forest Queries

**Domain**: `Data Structures (DS)`  
**Subtopic**: `Disjoint Set Union (DSU)`  

This workbook contains curated, high-quality competitive programming problems teaching **Small-to-Large Tree Rerooting for Online Forest Queries**.

---

## Curated Problems

### `[problem:AtCoder-abc350_g]` — Mediator
- **Rating / Difficulty**: 2058
- **Contest**: `abc350`
- **Analysis**: [`analysis/AtCoder-abc350_g.md`](../../analysis/AtCoder-abc350_g.md)
- **Key Idea**: In a forest, any two vertices have at most one common neighbor. By maintaining parent pointers for each rooted tree, a common neighbor between u and v must be one of: parent[u] == parent[v], parent[parent[u]] == v, or parent[parent[v]] == u. When merging trees via edge (u, v), we re-root the smaller component at u in O(size) and set parent[u] = v. By small-to-large merging, each vertex is rerooted at most O(log N) times, giving O(N log N + Q) total time.
- **Time Complexity**: `O(N log N + Q)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MOD = 998244353;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    vector<int> parent(n + 1, 0);
    vector<int> sz(n + 1, 1);
    vector<vector<int>> adj(n + 1);

    long long last_ans = 0;

    auto reroot = [&](int root) {
        vector<int> order;
        vector<int> p_old(n + 1, 0);
        vector<int> q_list = {root};
        p_old[root] = 0;
        int head = 0;
        while (head < (int)q_list.size()) {
            int u = q_list[head++];
            order.push_back(u);
            for (int v : adj[u]) {
                if (v != p_old[u]) {
                    p_old[v] = u;
                    q_list.push_back(v);
                }
            }
        }
        for (int i = 1; i < (int)order.size(); ++i) {
            int u = order[i];
            parent[u] = p_old[u];
        }
        parent[root] = 0;
    };

    while (q--) {
        long long a, b, c;
        cin >> a >> b >> c;
        long long type = 1 + (((a * (1 + last_ans)) % MOD) % 2);
        long long u = 1 + (((b * (1 + last_ans)) % MOD) % n);
        long long v = 1 + (((c * (1 + last_ans)) % MOD) % n);

        if (type == 1) {
            adj[u].push_back(v);
            adj[v].push_back(u);
            if (sz[u] > sz[v]) {
                swap(u, v);
            }
            reroot(u);
            parent[u] = v;
            sz[v] += sz[u];
        } else {
            int ans = 0;
            if (parent[u] != 0 && parent[u] == parent[v]) {
                ans = parent[u];
            } else if (parent[u] != 0 && parent[parent[u]] == v) {
                ans = parent[u];
            } else if (parent[v] != 0 && parent[parent[v]] == u) {
                ans = parent[v];
            }
            cout << ans << "\n";
            last_ans = ans;
        }
    }
    return 0;
}
```
