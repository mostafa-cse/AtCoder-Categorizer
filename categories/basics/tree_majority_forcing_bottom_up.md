# Greedy Leaf-Upwards Forcing on Tree Majority Constraints

**Domain**: `Greedy`  
**Subtopic**: `Tree Algorithms`  

This workbook contains curated, high-quality competitive programming problems teaching **Greedy Leaf-Upwards Forcing on Tree Majority Constraints**.

---

## Curated Problems

### `[problem:AtCoder-arc161_c]` — Dyed by Majority (Odd Tree)
- **Rating / Difficulty**: 1746
- **Contest**: `arc161`
- **Analysis**: [`analysis/AtCoder-arc161_c.md`](../../analysis/AtCoder-arc161_c.md)
- **Key Idea**: Process vertices bottom-up by tree depth. Since degree d is odd, each vertex u needs >= (d + 1) / 2 neighbors matching S[u]. Propagating leaf constraints upwards forces parent colors greedily.
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <algorithm>

using namespace std;

void solve() {
    int n;
    cin >> n;

    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    string s;
    cin >> s;

    vector<int> parent(n + 1, 0);
    vector<int> order;
    queue<int> q;

    parent[1] = 1;
    q.push(1);
    while (!q.empty()) {
        int u = q.front(); q.pop();
        order.push_back(u);
        for (int v : adj[u]) {
            if (v != parent[u]) {
                parent[v] = u;
                q.push(v);
            }
        }
    }

    reverse(order.begin(), order.end());
    string ans(n + 1, '?');
    vector<int> count_b(n + 1, 0), count_w(n + 1, 0);

    for (int u : order) {
        int deg = adj[u].size();
        int need = (deg + 1) / 2;

        char target = s[u - 1];
        if (target == 'B') {
            if (count_b[u] < need) {
                int p = parent[u];
                if (ans[p] == 'W') {
                    cout << -1 << "\n";
                    return;
                }
                ans[p] = 'B';
            }
        } else {
            if (count_w[u] < need) {
                int p = parent[u];
                if (ans[p] == 'B') {
                    cout << -1 << "\n";
                    return;
                }
                ans[p] = 'W';
            }
        }

        if (ans[u] == '?') ans[u] = 'B';
        if (u != 1) {
            int p = parent[u];
            if (ans[u] == 'B') count_b[p]++;
            else count_w[p]++;
        }
    }

    // Verify
    vector<int> final_b(n + 1, 0), final_w(n + 1, 0);
    for (int u = 1; u <= n; ++u) {
        for (int v : adj[u]) {
            if (ans[v] == 'B') final_b[u]++;
            else final_w[u]++;
        }
    }

    for (int u = 1; u <= n; ++u) {
        char maj = (final_b[u] > final_w[u]) ? 'B' : 'W';
        if (maj != s[u - 1]) {
            cout << -1 << "\n";
            return;
        }
    }

    cout << ans.substr(1) << "\n";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    if (cin >> t) {
        while (t--) solve();
    }
    return 0;
}
```
