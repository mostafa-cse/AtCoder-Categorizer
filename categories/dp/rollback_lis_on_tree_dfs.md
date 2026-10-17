# Rollback LIS on Tree via DFS Call-Stack Undo

**Domain**: `Dynamic Programming`  
**Subtopic**: `Tree DFS / LIS`  

This workbook contains curated, high-quality competitive programming problems teaching **Rollback LIS on Tree via DFS Call-Stack Undo**.

---

## Curated Problems

### `[problem:AtCoder-abc165_f]` — LIS on Tree
- **Rating / Difficulty**: 1843
- **Contest**: `abc165`
- **Analysis**: [`analysis/AtCoder-abc165_f.md`](../../analysis/AtCoder-abc165_f.md)
- **Key Idea**: Maintain the standard Patience Sorting LIS array dp[k] during a DFS traversal. When visiting node u with value A_u, binary search the replacement position pos, record the overwritten value (pos, old_val), update dp[pos] = A_u, record ans[u] = size of dp, recurse on children, and rollback dp[pos] = old_val on exit.
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int n;
vector<long long> a;
vector<vector<int>> adj;
vector<int> ans;
vector<long long> dp;

void dfs(int u, int p) {
    auto it = lower_bound(dp.begin(), dp.end(), a[u]);
    int pos = it - dp.begin();
    bool added = (it == dp.end());
    long long old_val = added ? -1 : *it;

    if (added) {
        dp.push_back(a[u]);
    } else {
        dp[pos] = a[u];
    }

    ans[u] = dp.size();

    for (int v : adj[u]) {
        if (v != p) {
            dfs(v, u);
        }
    }

    // Rollback
    if (added) {
        dp.pop_back();
    } else {
        dp[pos] = old_val;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n)) return 0;

    a.assign(n + 1, 0);
    for (int i = 1; i <= n; ++i) cin >> a[i];

    adj.assign(n + 1, vector<int>());
    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    ans.assign(n + 1, 0);
    dfs(1, 0);

    for (int i = 1; i <= n; ++i) {
        cout << ans[i] << "\n";
    }

    return 0;
}
```
