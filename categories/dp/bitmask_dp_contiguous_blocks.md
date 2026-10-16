# Bitmask DP with Contiguous Element Tracking

**Domain**: `Dynamic Programming`  
**Subtopic**: `Bit Related DP`  

This workbook contains curated, high-quality competitive programming problems teaching **Bitmask DP with Contiguous Element Tracking**.

---

## Curated Problems

### `[problem:AtCoder-abc215_e]` — Chain Contestant
- **Rating / Difficulty**: 1413
- **Contest**: `abc215`
- **Analysis**: [`analysis/AtCoder-abc215_e.md`](../../analysis/AtCoder-abc215_e.md)
- **Key Idea**: Use bitmask DP where the state tracks the set of contest types already completed, along with the most recent contest type.
- **Time Complexity**: `O(N * 2^10 * 10)`
- **Space Complexity**: `O(2^10 * 10)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <string>
#include <vector>

using namespace std;

const int MOD = 998244353;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    string s;
    if (!(cin >> n >> s)) return 0;

    // dp[mask][last_type]: mask in 0..1023, last_type in 0..9
    vector<vector<int>> dp(1024, vector<int>(10, 0));

    for (char ch : s) {
        int x = ch - 'A';
        vector<vector<int>> next_dp = dp;

        // Start a new subsequence consisting solely of x
        next_dp[1 << x][x] = (next_dp[1 << x][x] + 1) % MOD;

        for (int mask = 1; mask < 1024; ++mask) {
            for (int last = 0; last < 10; ++last) {
                int val = dp[mask][last];
                if (!val) continue;

                if (last == x) {
                    // Continue the same contiguous block
                    next_dp[mask][x] = (next_dp[mask][x] + val) % MOD;
                } else if (!(mask & (1 << x))) {
                    // Start a new block of type x that was never visited
                    next_dp[mask | (1 << x)][x] = (next_dp[mask | (1 << x)][x] + val) % MOD;
                }
            }
        }
        dp = move(next_dp);
    }

    long long ans = 0;
    for (int mask = 1; mask < 1024; ++mask) {
        for (int last = 0; last < 10; ++last) {
            ans = (ans + dp[mask][last]) % MOD;
        }
    }

    cout << ans << "\n";
    return 0;
}
```
