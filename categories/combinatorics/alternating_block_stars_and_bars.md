# Alternating Block Partitioning via Stars and Bars

**Domain**: `Combinatorics`  
**Subtopic**: `Stars and Bars`  

This workbook contains curated, high-quality competitive programming problems teaching **Alternating Block Partitioning via Stars and Bars**.

---

## Curated Problems

### [problem:AtCoder-abc132_d] — Blue and Red Balls
- **Contest**: `abc132`
- **Rating / Difficulty**: 1167
- **Specific Skill**: Alternating Block Partitioning via Stars and Bars
- **Individual Analysis**: [`../../analysis/AtCoder-abc132_d.md`](../../analysis/AtCoder-abc132_d.md)
- **Problem Statement Summary**: There are K blue balls and N - K red balls. In each operation, collect a contiguous block of blue balls. For each i in 1..K, find the number of arrangements requiring exactly i operations, modulo 10^9 + 7.
- **Core Insight**: Dividing K blue balls into i non-empty blocks is C(K - 1, i - 1) via Stars and Bars. These i blue blocks must be separated by at least one red ball, which means choosing i distinct insertion slots among the (N - K + 1) available positions between the red balls: C(N - K + 1, i). By rule of product, answer is C(K - 1, i - 1) * C(N - K + 1, i).
- **Complexity**: Time: `O(N^2) or O(N)` | Space: `O(N^2)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 1e9 + 7;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<vector<long long>> c(n + 2, vector<long long>(n + 2, 0));
    for (int i = 0; i <= n + 1; ++i) {
        c[i][0] = 1;
        for (int j = 1; j <= i; ++j) {
            c[i][j] = (c[i - 1][j - 1] + c[i - 1][j]) % MOD;
        }
    }

    int red = n - k;
    for (int i = 1; i <= k; ++i) {
        if (i > red + 1) {
            cout << 0 << "\n";
        } else {
            long long blue_ways = c[k - 1][i - 1];
            long long red_ways = c[red + 1][i];
            long long ans = (blue_ways * red_ways) % MOD;
            cout << ans << "\n";
        }
    }

    return 0;
}
```
