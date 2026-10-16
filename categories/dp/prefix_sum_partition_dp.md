# Prefix Sum Transition Acceleration on Partition DP

**Domain**: `Dynamic Programming`  
**Subtopic**: `Linear DP`  

This workbook contains curated, high-quality competitive programming problems teaching **Prefix Sum Transition Acceleration on Partition DP**.

---

## Curated Problems

### [problem:AtCoder-abc178_d] — Redistribution
- **Contest**: `abc178`
- **Rating / Difficulty**: 875
- **Specific Skill**: Prefix Sum Transition Acceleration on Partition DP
- **Individual Analysis**: [`../../analysis/AtCoder-abc178_d.md`](../../analysis/AtCoder-abc178_d.md)
- **Problem Statement Summary**: Find the number of sequences of positive integers >= 3 whose sum is S (S <= 2000), modulo 10^9 + 7.
- **Core Insight**: Notice that sum_{k=0}^{i-3} dp[k] = (sum_{k=0}^{i-4} dp[k]) + dp[i-3] = dp[i-1] + dp[i-3]. Thus, dp[i] = dp[i-1] + dp[i-3] for all i >= 3, reducing naive O(S^2) transitions to O(1) per state!
- **Complexity**: Time: `O(S)` | Space: `O(S)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int s;
    if (!(cin >> s)) return 0;

    const int MOD = 1e9 + 7;
    vector<int> dp(s + 1, 0);
    dp[0] = 1;

    for (int i = 3; i <= s; ++i) {
        dp[i] = (dp[i - 1] + dp[i - 3]) % MOD;
    }

    cout << dp[s] << "\n";
    return 0;
}
```
