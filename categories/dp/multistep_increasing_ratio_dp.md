# 4-Step Increasing Sequence with 2x Ratio via Coordinate Prefix Sums

**Domain**: `Dynamic Programming`  
**Subtopic**: `Classic DP`  

This workbook contains curated, high-quality competitive programming problems teaching **4-Step Increasing Sequence with 2x Ratio via Coordinate Prefix Sums**.

---

## Curated Problems

### `[problem:AtCoder-arc043_b]` — Difficulty
- **Rating / Difficulty**: 1606
- **Contest**: `arc043`
- **Analysis**: [`analysis/AtCoder-arc043_b.md`](../../analysis/AtCoder-arc043_b.md)
- **Key Idea**: Multi-stage DP. Sort difficulties D. Let dp[k][i] be the number of valid k-problem sequences ending with D[i]. Transitions sum over all j where 2 * D[j] <= D[i], accelerated using prefix sums.
- **Time Complexity**: `O(4 * N log N)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MOD = 1000000007;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> d(n);
    for (int i = 0; i < n; ++i) {
        cin >> d[i];
    }

    sort(d.begin(), d.end());

    vector<long long> dp(n, 1);

    for (int stage = 1; stage <= 3; ++stage) {
        vector<long long> pref(n + 1, 0);
        for (int i = 0; i < n; ++i) {
            pref[i + 1] = (pref[i] + dp[i]) % MOD;
        }

        vector<long long> next_dp(n, 0);
        for (int i = 0; i < n; ++i) {
            int target = d[i] / 2;
            int count = upper_bound(d.begin(), d.end(), target) - d.begin();
            next_dp[i] = pref[count];
        }
        dp = move(next_dp);
    }

    long long ans = 0;
    for (int i = 0; i < n; ++i) {
        ans = (ans + dp[i]) % MOD;
    }

    cout << ans << "\n";
    return 0;
}
```
