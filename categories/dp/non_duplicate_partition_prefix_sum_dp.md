# Non-Duplicate Contiguous Partition DP Accelerated by Monotonic Left-Bound Prefix Sums

**Domain**: `Dynamic Programming (DP)`  
**Subtopic**: `Two Pointers / Prefix Sum DP`  

This workbook contains curated, high-quality competitive programming problems teaching **Non-Duplicate Contiguous Partition DP Accelerated by Monotonic Left-Bound Prefix Sums**.

---

## Curated Problems

### `[problem:AtCoder-abc017_4]` — サプリメント
- **Rating / Difficulty**: 1956
- **Contest**: `abc017`
- **Analysis**: [`analysis/AtCoder-abc017_4.md`](../../analysis/AtCoder-abc017_4.md)
- **Key Idea**: Let dp[i] be the number of valid partitions of prefix 1..i. dp[i] = sum_{j = L_i}^{i - 1} dp[j], where L_i is the smallest index such that subarray f[L_i + 1..i] contains no duplicates. The boundary L_i is monotonically non-decreasing: L_i = max(L_{i-1}, last_pos[f_i]). Because L_i is monotonic, the transition is a range sum query over dp[L_i..i-1], maintained in O(1) via prefix sums of dp.
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N + M)`
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

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<int> f(n + 1);
    for (int i = 1; i <= n; ++i) {
        cin >> f[i];
    }

    vector<int> dp(n + 1, 0);
    vector<int> pref(n + 2, 0);
    vector<int> last_pos(m + 1, 0);

    dp[0] = 1;
    pref[1] = 1;

    int L = 0;
    for (int i = 1; i <= n; ++i) {
        L = max(L, last_pos[f[i]]);
        dp[i] = (pref[i] - pref[L] + MOD) % MOD;
        pref[i + 1] = (pref[i] + dp[i]) % MOD;
        last_pos[f[i]] = i;
    }

    cout << dp[n] << "\n";
    return 0;
}
```
