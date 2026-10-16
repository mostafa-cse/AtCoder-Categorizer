# Dynamic 0-1 Knapsack with Rollback / Subtraction Undo

**Domain**: `Dynamic Programming`  
**Subtopic**: `Classic DP`  

This workbook contains curated, high-quality competitive programming problems teaching **Dynamic 0-1 Knapsack with Rollback / Subtraction Undo**.

---

## Curated Problems

### `[problem:AtCoder-abc321_f]` — #(subset sum = K) with Add and Erase
- **Rating / Difficulty**: 1645
- **Contest**: `abc321`
- **Analysis**: [`analysis/AtCoder-abc321_f.md`](../../analysis/AtCoder-abc321_f.md)
- **Key Idea**: Online 0-1 knapsack DP rollback! Adding element x transitions forward: dp[s] += dp[s - x]. Removing element x reverses the recurrence: dp[s] -= dp[s - x].
- **Time Complexity**: `O(Q * K)`
- **Space Complexity**: `O(K)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 998244353;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int q, k;
    if (!(cin >> q >> k)) return 0;

    vector<int> dp(k + 1, 0);
    dp[0] = 1;

    while (q--) {
        char type;
        int x;
        cin >> type >> x;

        if (type == '+') {
            for (int s = k; s >= x; --s) {
                dp[s] = (dp[s] + dp[s - x]) % MOD;
            }
        } else {
            for (int s = x; s <= k; ++s) {
                dp[s] = (dp[s] - dp[s - x] + MOD) % MOD;
            }
        }

        cout << dp[k] << "\n";
    }

    return 0;
}
```
