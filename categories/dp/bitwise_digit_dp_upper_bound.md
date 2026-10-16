# Bitwise Digit DP with Upper Bound Constraint

**Domain**: `Dynamic Programming`  
**Subtopic**: `Digit DP`  

This workbook contains curated, high-quality competitive programming problems teaching **Bitwise Digit DP with Upper Bound Constraint**.

---

## Curated Problems

### `[problem:AtCoder-abc117_d]` — XXOR
- **Rating / Difficulty**: 1423
- **Contest**: `abc117`
- **Analysis**: [`analysis/AtCoder-abc117_d.md`](../../analysis/AtCoder-abc117_d.md)
- **Key Idea**: Process bits from most significant (bit 45) down to 0 using Digit DP tracking whether X is already strictly less than K.
- **Time Complexity**: `O(log K)`
- **Space Complexity**: `O(log K)`
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
    long long k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> a(n);
    vector<int> cnt(46, 0);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        for (int b = 0; b <= 45; ++b) {
            if ((a[i] >> b) & 1) {
                cnt[b]++;
            }
        }
    }

    // dp[b][less]: max contribution from bit 45 down to b
    vector<vector<long long>> dp(47, vector<long long>(2, -1));
    dp[46][0] = 0;

    for (int b = 45; b >= 0; --b) {
        int kb = (k >> b) & 1;
        for (int less = 0; less < 2; ++less) {
            if (dp[b + 1][less] == -1) continue;

            int max_d = less ? 1 : kb;
            for (int d = 0; d <= max_d; ++d) {
                int next_less = less || (d < kb);
                long long contrib = 1LL * (d ? (n - cnt[b]) : cnt[b]) * (1LL << b);
                dp[b][next_less] = max(dp[b][next_less], dp[b + 1][less] + contrib);
            }
        }
    }

    cout << max(dp[0][0], dp[0][1]) << "\n";
    return 0;
}
```
