# Tree Rerooting DP on Topological Linear Extensions

**Domain**: `Dynamic Programming (DP)`  
**Subtopic**: `Tree DP`  

This workbook contains curated, high-quality competitive programming problems teaching **Tree Rerooting DP on Topological Linear Extensions**.

---

## Curated Problems

### `[problem:AtCoder-abc160_f]` — Distributing Integers
- **Rating / Difficulty**: 2048
- **Contest**: `abc160`
- **Analysis**: [`analysis/AtCoder-abc160_f.md`](../../analysis/AtCoder-abc160_f.md)
- **Key Idea**: The condition means the set of labeled vertices is always connected. When rooted at vertex k, each child's label must be greater than its parent's label. This is the definition of a topological linear extension of a tree poset rooted at k, given by the formula N! / prod_{v=1}^N sz(v). To compute this for all N vertices in O(N), we use Tree Rerooting DP (All-Directions Tree DP). When rerooting from u to adjacent neighbor v, only the subtree sizes of u and v change: sz(u) becomes N - sz(v), and sz(v) becomes N. Thus ans(v) = ans(u) * sz(v) * inv(N - sz(v)) % MOD.
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 1e9 + 7;

long long power(long long base, long long exp) {
    long long res = 1;
    base %= MOD;
    while (exp > 0) {
        if (exp % 2 == 1) res = (res * base) % MOD;
        base = (base * base) % MOD;
        exp /= 2;
    }
    return res;
}

long long mod_inv(long long n) {
    return power(n, MOD - 2);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    vector<long long> fact(n + 1), inv(n + 1);
    fact[0] = 1;
    inv[0] = 1;
    for (int i = 1; i <= n; ++i) {
        fact[i] = (fact[i - 1] * i) % MOD;
        inv[i] = mod_inv(i);
    }

    vector<int> sz(n + 1, 0);

    auto dfs1 = [&](auto& self, int u, int p) -> void {
        sz[u] = 1;
        for (int v : adj[u]) {
            if (v != p) {
                self(self, v, u);
                sz[u] += sz[v];
            }
        }
    };

    dfs1(dfs1, 1, 0);

    // Compute ans[1] = N! / prod sz[v]
    long long ans1 = fact[n];
    for (int v = 1; v <= n; ++v) {
        ans1 = (ans1 * inv[sz[v]]) % MOD;
    }

    vector<long long> ans(n + 1);
    ans[1] = ans1;

    auto dfs2 = [&](auto& self, int u, int p) -> void {
        for (int v : adj[u]) {
            if (v != p) {
                // Reroot u -> v:
                // sz[v] was subtree size from u
                // in v's view, u becomes a child of size (n - sz[v])
                ans[v] = ans[u] * sz[v] % MOD * inv[n - sz[v]] % MOD;
                self(self, v, u);
            }
        }
    };

    dfs2(dfs2, 1, 0);

    for (int i = 1; i <= n; ++i) {
        cout << ans[i] << "\n";
    }

    return 0;
}
```
