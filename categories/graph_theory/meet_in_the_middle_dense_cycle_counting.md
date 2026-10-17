# Cycle Detection

**Domain**: `Graph Theory`  
**Subtopic**: `Cycles`  

This workbook contains curated, high-quality competitive programming problems teaching **Cycle Detection**.

---

## Curated Problems

### `[problem:AtCoder-abc411_g]` — Count Cycles
- **Rating / Difficulty**: 2088
- **Contest**: `abc411`
- **Analysis**: [`analysis/AtCoder-abc411_g.md`](../../analysis/AtCoder-abc411_g.md)
- **Key Idea**: With N <= 20, we can use Bitmask DP to count simple cycles. Every simple cycle has a unique minimum-indexed vertex v_0. For each choice of v_0 in [0, N-1], consider the induced subgraph on vertices {v_0, v_0 + 1, ..., N-1}. We define dp[mask][u] as the number of simple paths starting at v_0 and ending at u using the subset of vertices mask (with v_0 always included). A cycle is closed when an edge exists from u back to v_0 and the cycle has length >= 3. Since every cycle is counted in both directions (clockwise and counterclockwise), we sum all valid closures and divide by 2.
- **Time Complexity**: `O(2^N * N^2)`
- **Space Complexity**: `O(2^N * N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 998244353;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<int> adj(n, 0);
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        --u; --v;
        adj[u] |= (1 << v);
        adj[v] |= (1 << u);
    }

    long long total_cycles = 0;

    for (int v0 = 0; v0 < n; ++v0) {
        int sub_size = n - v0;
        int num_masks = 1 << sub_size;
        vector<vector<int>> dp(num_masks, vector<int>(sub_size, 0));

        dp[1][0] = 1;

        for (int mask = 1; mask < num_masks; ++mask) {
            for (int u_rel = 0; u_rel < sub_size; ++u_rel) {
                int ways = dp[mask][u_rel];
                if (!ways) continue;

                int u = v0 + u_rel;

                // Check if can close cycle to v0
                if (__builtin_popcount(mask) >= 3 && ((adj[u] >> v0) & 1)) {
                    total_cycles = (total_cycles + ways) % MOD;
                }

                int available_neighbors = adj[u] >> v0;
                int candidate_mask = available_neighbors & ~mask;

                while (candidate_mask > 0) {
                    int w_rel = __builtin_ctz(candidate_mask);
                    candidate_mask &= candidate_mask - 1;
                    int next_mask = mask | (1 << w_rel);
                    dp[next_mask][w_rel] = (dp[next_mask][w_rel] + ways) % MOD;
                }
            }
        }
    }

    long long inv2 = (MOD + 1) / 2;
    long long ans = (total_cycles % MOD * inv2) % MOD;
    cout << ans << "\n";

    return 0;
}
```
