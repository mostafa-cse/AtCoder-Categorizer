# x2 +1 Trick

**Domain**: `Dynamic Programming (DP)`  
**Subtopic**: `More Tricks`  

This workbook contains curated, high-quality competitive programming problems teaching **x2 +1 Trick**.

---

## Curated Problems

### `[problem:AtCoder-arc107_d]` — Number of Multisets
- **Rating / Difficulty**: 2096
- **Contest**: `arc107`
- **Analysis**: [`analysis/AtCoder-arc107_d.md`](../../analysis/AtCoder-arc107_d.md)
- **Key Idea**: Let dp[n][k] be the number of multisets of size n summing to k. We can classify multisets based on whether they contain at least one element equal to 1. If it contains at least one 1: remove that 1, leaving a multiset of size n - 1 summing to k - 1, which gives dp[n - 1][k - 1]. If it contains NO 1s: every element in the multiset is <= 1/2. If we multiply every element by 2, we obtain a multiset of size n whose elements are powers of 1/2 summing to 2k! Thus, the second case gives dp[n][2k]. Putting these together gives the recurrence: dp[n][k] = dp[n - 1][k - 1] + dp[n][2k] (with base cases dp[0][0] = 1, and dp[n][k] = 0 for k > n).
- **Time Complexity**: `O(N^2)`
- **Space Complexity**: `O(N^2)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 998244353;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    if (k > n || k <= 0) {
        cout << 0 << "\n";
        return 0;
    }

    vector<vector<int>> dp(n + 1, vector<int>(n + 1, 0));
    dp[0][0] = 1;

    for (int i = 1; i <= n; ++i) {
        for (int j = i; j >= 1; --j) {
            dp[i][j] = dp[i - 1][j - 1];
            if (2 * j <= i) {
                dp[i][j] = (dp[i][j] + dp[i][2 * j]) % MOD;
            }
        }
    }

    cout << dp[n][k] << "\n";
    return 0;
}
```
