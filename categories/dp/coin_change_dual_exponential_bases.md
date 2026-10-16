# Coin Change / Minimum Steps with Dual Exponential Bases

**Domain**: `Dynamic Programming`  
**Subtopic**: `Classic DP`  

This workbook contains curated, high-quality competitive programming problems teaching **Coin Change / Minimum Steps with Dual Exponential Bases**.

---

## Curated Problems

### [problem:AtCoder-abc099_c] — Strange Bank
- **Contest**: `abc099`
- **Rating / Difficulty**: 1101
- **Specific Skill**: Coin Change / Minimum Steps with Dual Exponential Bases
- **Individual Analysis**: [`../../analysis/AtCoder-abc099_c.md`](../../analysis/AtCoder-abc099_c.md)
- **Problem Statement Summary**: Withdraw N yen using 1 yen, powers of 6 (6, 36, 216...), and powers of 9 (9, 81, 729...). Find the minimum total withdrawals for N <= 100,000.
- **Core Insight**: Since N <= 10^5, the total number of denominations <= 100,000 is small (only 1 + 6 + 5 = 12 coins). Formulate 1D DP: dp[i] = min_{coin} (dp[i - coin] + 1) in O(N * C).
- **Complexity**: Time: `O(N * log N)` | Space: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> coins = {1};
    for (int p6 = 6; p6 <= n; p6 *= 6) coins.push_back(p6);
    for (int p9 = 9; p9 <= n; p9 *= 9) coins.push_back(p9);

    vector<int> dp(n + 1, 1e9);
    dp[0] = 0;

    for (int i = 1; i <= n; ++i) {
        for (int c : coins) {
            if (i >= c) {
                dp[i] = min(dp[i], dp[i - c] + 1);
            }
        }
    }

    cout << dp[n] << "\n";
    return 0;
}
```
