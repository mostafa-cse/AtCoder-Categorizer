# Modular Congruence-Constrained Set Partitions (Constrained Stirling Numbers)

**Domain**: `Combinatorics`  
**Subtopic**: `Stirling Numbers & Partition Lattice`  

This workbook contains curated, high-quality competitive programming problems teaching **Modular Congruence-Constrained Set Partitions (Constrained Stirling Numbers)**.

---

## Curated Problems

### `[problem:AtCoder-abc217_g]` — Groups
- **Rating / Difficulty**: 2047
- **Contest**: `abc217`
- **Analysis**: [`analysis/AtCoder-abc217_g.md`](../../analysis/AtCoder-abc217_g.md)
- **Key Idea**: Insert elements 1, 2, ..., N in increasing order. When inserting x, it cannot be placed in any group containing an element congruent to x mod M. The previously placed elements congruent to x mod M are x - M, x - 2M, ... (exactly floor((x - 1) / M) elements). Since all previous elements were legally partitioned, each of these floor((x - 1) / M) elements resides in a distinct group! Thus, out of j existing groups, exactly floor((x - 1) / M) groups are forbidden for x. We can place x into any of the j - floor((x - 1) / M) allowed existing groups, or create a new group. This generalizes Stirling Numbers of the Second Kind: dp[i][j] = dp[i-1][j-1] + dp[i-1][j] * max(0, j - floor((i - 1) / M)).
- **Time Complexity**: `O(N^2)`
- **Space Complexity**: `O(N^2)`
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

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<long long>> dp(n + 1, vector<long long>(n + 1, 0));
    dp[0][0] = 1;

    for (int i = 1; i <= n; ++i) {
        int forbidden = (i - 1) / m;
        for (int j = 1; j <= i; ++j) {
            long long choices = max(0, j - forbidden);
            dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j] * choices) % MOD;
        }
    }

    for (int k = 1; k <= n; ++k) {
        cout << dp[n][k] << "\n";
    }

    return 0;
}
```
