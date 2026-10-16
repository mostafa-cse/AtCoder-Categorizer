# Tree DP: White or Black Coloring with No Adjacent Black Nodes

**Domain**: `Dynamic Programming`  
**Subtopic**: `Tree DP`  

This workbook contains curated, high-quality competitive programming problems teaching **Tree DP: White or Black Coloring with No Adjacent Black Nodes**.

---

## Curated Problems

### `[problem:AtCoder-abc036_d]` — Coloring
- **Rating / Difficulty**: 1602
- **Contest**: `abc036`
- **Analysis**: [`analysis/AtCoder-abc036_d.md`](../../analysis/AtCoder-abc036_d.md)
- **Key Idea**: Classic Tree DP modeling independent sets. For each node u, maintain dp[u][0] (u is White) and dp[u][1] (u is Black). If u is White, children can be White or Black; if u is Black, children MUST be White.
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 1000000007;

vector<vector<int>> adj;
vector<long long> dp0, dp1;

void dfs(int u, int p) {
    dp0[u] = 1;
    dp1[u] = 1;

    for (int v : adj[u]) {
        if (v != p) {
            dfs(v, u);
            dp0[u] = (dp0[u] * (dp0[v] + dp1[v])) % MOD;
            dp1[u] = (dp1[u] * dp0[v]) % MOD;
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    adj.resize(n + 1);
    dp0.resize(n + 1);
    dp1.resize(n + 1);

    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    dfs(1, 0);

    long long ans = (dp0[1] + dp1[1]) % MOD;
    cout << ans << "\n";
    return 0;
}
```
