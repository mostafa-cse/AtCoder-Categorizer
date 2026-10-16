# DAG Topological Minimum Ancestor Cost DP

**Domain**: `Dynamic Programming`  
**Subtopic**: `DAG DP`  

This workbook contains curated, high-quality competitive programming problems teaching **DAG Topological Minimum Ancestor Cost DP**.

---

## Curated Problems

### [problem:AtCoder-abc188_e] — Peddler
- **Contest**: `abc188`
- **Rating / Difficulty**: 1170
- **Specific Skill**: DAG Topological Minimum Ancestor Cost DP
- **Individual Analysis**: [`../../analysis/AtCoder-abc188_e.md`](../../analysis/AtCoder-abc188_e.md)
- **Problem Statement Summary**: N towns in a DAG with edges X_i -> Y_i (X_i < Y_i). Gold price at town i is A_i. Buy gold at town x and sell at town y reachable from x. Maximize profit A_y - A_x.
- **Core Insight**: Since edges strictly satisfy X_i < Y_i, vertices 1..N are already topologically sorted! Process u from 1 to N: initialize min_anc[v] = INF. For each neighbor v of u, update min_anc[v] = min({min_anc[v], min_anc[u], A_u}). The maximum profit selling at v is A_v - min_anc[v].
- **Complexity**: Time: `O(N + M)` | Space: `O(N + M)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const long long INF = 4e18;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<long long> a(n + 1);
    for (int i = 1; i <= n; ++i) {
        cin >> a[i];
    }

    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
    }

    vector<long long> min_anc(n + 1, INF);
    long long max_profit = -INF;

    for (int u = 1; u <= n; ++u) {
        if (min_anc[u] != INF) {
            max_profit = max(max_profit, a[u] - min_anc[u]);
        }
        long long current_min = min(min_anc[u], a[u]);
        for (int v : adj[u]) {
            min_anc[v] = min(min_anc[v], current_min);
        }
    }

    cout << max_profit << "\n";
    return 0;
}
```
