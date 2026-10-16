# DP with Range Transitions Accelerated by Prefix Sums

**Domain**: `Dynamic Programming`  
**Subtopic**: `DP Optimization`  

This workbook contains curated, high-quality competitive programming problems teaching **DP with Range Transitions Accelerated by Prefix Sums**.

---

## Curated Problems

### [problem:AtCoder-abc179_d] — Leaping Tak
- **Contest**: `abc179`
- **Rating / Difficulty**: 1251
- **Specific Skill**: DP with Range Transitions Accelerated by Prefix Sums
- **Individual Analysis**: [`../../analysis/AtCoder-abc179_d.md`](../../analysis/AtCoder-abc179_d.md)
- **Problem Statement Summary**: Start at cell 1, reach cell N. You can jump by any distance in K given intervals [L_i, R_i]. Find the number of paths from 1 to N modulo 998244353.
- **Core Insight**: The transition sum_{d = L}^{R} dp[i - d] is a contiguous range sum on previous DP values: sum_{x = max(1, i - R)}^{i - L} dp[x]. Maintaining prefix sums pref[x] = sum_{y=1}^x dp[y] allows each interval range sum to be computed in O(1)!
- **Complexity**: Time: `O(N * K)` | Space: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MOD = 998244353;

struct Interval {
    int l, r;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<Interval> intervals(k);
    for (int i = 0; i < k; ++i) {
        cin >> intervals[i].l >> intervals[i].r;
    }

    vector<long long> dp(n + 1, 0);
    vector<long long> pref(n + 1, 0);

    dp[1] = 1;
    pref[1] = 1;

    for (int i = 2; i <= n; ++i) {
        for (const auto& iv : intervals) {
            int r_idx = i - iv.l;
            int l_idx = max(1, i - iv.r);
            if (l_idx <= r_idx && r_idx >= 1) {
                long long term = (pref[r_idx] - pref[l_idx - 1] + MOD) % MOD;
                dp[i] = (dp[i] + term) % MOD;
            }
        }
        pref[i] = (pref[i - 1] + dp[i]) % MOD;
    }

    cout << dp[n] << "\n";
    return 0;
}
```
