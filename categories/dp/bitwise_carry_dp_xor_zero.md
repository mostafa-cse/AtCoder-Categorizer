# Bit-by-Bit Carry DP with XOR-Zero Parity Constraint

**Domain**: `Dynamic Programming`  
**Subtopic**: `Bitwise DP`  

This workbook contains curated, high-quality competitive programming problems teaching **Bit-by-Bit Carry DP with XOR-Zero Parity Constraint**.

---

## Curated Problems

### `[problem:AtCoder-arc116_d]` — I Wanna Win The Game
- **Rating / Difficulty**: 1718
- **Contest**: `arc116`
- **Analysis**: [`analysis/AtCoder-arc116_d.md`](../../analysis/AtCoder-arc116_d.md)
- **Key Idea**: The XOR sum is zero if and only if at every bit position b, an even number of elements have the b-th bit set. Process bits from 0 to 12. At bit b, choosing 2j elements to have bit b set contributes 2j * 2^b to the sum.
- **Time Complexity**: `O(N * M)`
- **Space Complexity**: `O(M)`
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

    vector<vector<long long>> C(n + 1, vector<long long>(n + 1, 0));
    for (int i = 0; i <= n; ++i) {
        C[i][0] = 1;
        for (int j = 1; j <= i; ++j) {
            C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % MOD;
        }
    }

    vector<long long> dp(m + 1, 0);
    dp[0] = 1;

    for (int b = 0; (1 << b) <= m; ++b) {
        int weight = 1 << b;
        vector<long long> next_dp(m + 1, 0);

        for (int j = 0; 2 * j <= n; ++j) {
            int count_set = 2 * j;
            int add = count_set * weight;
            if (add > m) break;
            long long ways = C[n][count_set];

            for (int s = 0; s + add <= m; ++s) {
                if (dp[s] > 0) {
                    next_dp[s + add] = (next_dp[s + add] + dp[s] * ways) % MOD;
                }
            }
        }
        dp = move(next_dp);
    }

    cout << dp[m] << "\n";
    return 0;
}
```
