# Backward Game Theory DP modulo 7 with Controllable State Sets

**Domain**: `Game Theory`  
**Subtopic**: `Minimax`  

This workbook contains curated, high-quality competitive programming problems teaching **Backward Game Theory DP modulo 7 with Controllable State Sets**.

---

## Curated Problems

### `[problem:AtCoder-abc195_e]` — Lucky 7 Battle
- **Rating / Difficulty**: 1609
- **Contest**: `abc195`
- **Analysis**: [`analysis/AtCoder-abc195_e.md`](../../analysis/AtCoder-abc195_e.md)
- **Key Idea**: Backward induction! Work backwards from round N to 0. Maintain the set of winning remainders W subseteq {0..6} from which Takahashi can guarantee victory.
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(1)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    string s, x;
    if (!(cin >> n >> s >> x)) return 0;

    // dp[r]: true if Takahashi can win starting with remainder r
    vector<bool> dp(7, false);
    dp[0] = true;

    for (int i = n - 1; i >= 0; --i) {
        int d = s[i] - '0';
        bool is_t = (x[i] == 'T');
        vector<bool> next_dp(7, false);

        for (int r = 0; r < 7; ++r) {
            int r0 = (10 * r) % 7;
            int r1 = (10 * r + d) % 7;

            if (is_t) {
                // Takahashi wants at least one branch to win
                next_dp[r] = (dp[r0] || dp[r1]);
            } else {
                // Aoki forces both branches to be winning for Takahashi to win
                next_dp[r] = (dp[r0] && dp[r1]);
            }
        }
        dp = move(next_dp);
    }

    cout << (dp[0] ? "Takahashi" : "Aoki") << "\n";
    return 0;
}
```
