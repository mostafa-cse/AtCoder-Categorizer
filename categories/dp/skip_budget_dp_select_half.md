# Non-Adjacent Selection via Skip-Budget DP

**Domain**: `Dynamic Programming`  
**Subtopic**: `Classic DP`  

This workbook contains curated, high-quality competitive programming problems teaching **Non-Adjacent Selection via Skip-Budget DP**.

---

## Curated Problems

### `[problem:AtCoder-abc162_f]` — Select Half
- **Rating / Difficulty**: 1764
- **Contest**: `abc162`
- **Analysis**: [`analysis/AtCoder-abc162_f.md`](../../analysis/AtCoder-abc162_f.md)
- **Key Idea**: To choose floor(N/2) non-adjacent elements out of N, the total number of 'extra skips' allowed is at most 1 (for even N) or at most 2 (for odd N). Maintain DP state dp[i][skip] tracking the maximum sum using skip extra skips.
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const long long INF = 1e18;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    int max_skips = (n % 2 == 0) ? 1 : 2;
    // dp[i][skip]: after considering elements up to index i-1, with 'skip' extra skips used
    vector<vector<long long>> dp(n + 2, vector<long long>(max_skips + 1, -INF));
    dp[0][0] = 0;

    for (int i = 0; i < n; ++i) {
        for (int s = 0; s <= max_skips; ++s) {
            if (dp[i][s] == -INF) continue;

            // Option 1: Pick a[i], must skip i+1, so jump to i+2
            int next_i = min(n, i + 2);
            dp[next_i][s] = max(dp[next_i][s], dp[i][s] + a[i]);

            // Option 2: Do not pick a[i], spend 1 extra skip, jump to i+1
            if (s + 1 <= max_skips) {
                dp[i + 1][s + 1] = max(dp[i + 1][s + 1], dp[i][s]);
            }
        }
    }

    long long ans = -INF;
    for (int s = 0; s <= max_skips; ++s) {
        ans = max(ans, dp[n][s]);
        ans = max(ans, dp[n + 1][s]);
    }

    cout << ans << "\n";
    return 0;
}
```
