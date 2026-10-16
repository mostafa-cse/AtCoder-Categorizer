# Tree Edge Frequencies via DFS + Subset Sum Knapsack

**Domain**: `Dynamic Programming`  
**Subtopic**: `Classic DP`  

This workbook contains curated, high-quality competitive programming problems teaching **Tree Edge Frequencies via DFS + Subset Sum Knapsack**.

---

## Curated Problems

### `[problem:AtCoder-abc222_e]` — Red and Blue Tree
- **Rating / Difficulty**: 1491
- **Contest**: `abc222`
- **Analysis**: [`analysis/AtCoder-abc222_e.md`](../../analysis/AtCoder-abc222_e.md)
- **Key Idea**: Compute the traversal frequency freq[e] of each edge over the M - 1 paths. R - B = K and R + B = total_freq => 2 * R = total_freq + K. This reduces to counting edge subsets with sum R.
- **Time Complexity**: `O(M * N + N * target)`
- **Space Complexity**: `O(N + target)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 998244353;

struct Edge {
    int to;
    int id;
};

bool dfs(int u, int target, int parent, const vector<vector<Edge>>& adj, vector<int>& edge_count) {
    if (u == target) return true;
    for (const auto& e : adj[u]) {
        if (e.to != parent) {
            if (dfs(e.to, target, u, adj, edge_count)) {
                edge_count[e.id]++;
                return true;
            }
        }
    }
    return false;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, k;
    if (!(cin >> n >> m >> k)) return 0;

    vector<int> a(m);
    for (int i = 0; i < m; ++i) cin >> a[i];

    vector<vector<Edge>> adj(n + 1);
    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back({v, i});
        adj[v].push_back({u, i});
    }

    vector<int> edge_count(n - 1, 0);
    for (int i = 0; i < m - 1; ++i) {
        dfs(a[i], a[i + 1], -1, adj, edge_count);
    }

    long long s = 0;
    for (int x : edge_count) s += x;

    if (s + k < 0 || (s + k) % 2 != 0) {
        cout << 0 << "\n";
        return 0;
    }

    long long target = (s + k) / 2;
    vector<int> dp(target + 1, 0);
    dp[0] = 1;

    for (int w : edge_count) {
        for (int j = target; j >= w; --j) {
            dp[j] = (dp[j] + dp[j - w]) % MOD;
        }
    }

    cout << dp[target] << "\n";
    return 0;
}
```
