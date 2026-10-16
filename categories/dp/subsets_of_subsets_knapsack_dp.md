# 3-Choice State Dynamic Programming on Subsets of Subsets

**Domain**: `Dynamic Programming`  
**Subtopic**: `Classic DP`  

This workbook contains curated, high-quality competitive programming problems teaching **3-Choice State Dynamic Programming on Subsets of Subsets**.

---

## Curated Problems

### `[problem:AtCoder-abc169_f]` — Knapsack for All Subsets
- **Rating / Difficulty**: 1698
- **Contest**: `abc169`
- **Analysis**: [`analysis/AtCoder-abc169_f.md`](../../analysis/AtCoder-abc169_f.md)
- **Key Idea**: Rephrase: we are choosing a subset T, and within T, choosing a subset U whose sum is S. For each element A_i, there are 3 independent choices: 1) A_i not in T; 2) A_i in T but not in U; 3) A_i in T and in U.
- **Time Complexity**: `O(N * S)`
- **Space Complexity**: `O(S)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 998244353;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, S;
    if (!(cin >> n >> S)) return 0;

    vector<int> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    vector<long long> dp(S + 1, 0);
    dp[0] = 1;

    for (int x : a) {
        for (int s = S; s >= 0; --s) {
            long long ways = (dp[s] * 2) % MOD;
            if (s >= x) {
                ways = (ways + dp[s - x]) % MOD;
            }
            dp[s] = ways;
        }
    }

    cout << dp[S] << "\n";
    return 0;
}
```
