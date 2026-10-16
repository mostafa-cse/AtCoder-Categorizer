# Digit DP Modulo 13

**Domain**: `Dynamic Programming`  
**Subtopic**: `Digit DP`  

This workbook contains curated, high-quality competitive programming problems teaching **Digit DP Modulo 13**.

---

## Curated Problems

### [problem:AtCoder-abc135_d] — Digits Parade
- **Contest**: `abc135`
- **Rating / Difficulty**: 1334
- **Specific Skill**: Digit DP Modulo 13
- **Individual Analysis**: [`../../analysis/AtCoder-abc135_d.md`](../../analysis/AtCoder-abc135_d.md)
- **Problem Statement Summary**: Given a string S containing digits and '?'. Replace each '?' with a digit 0..9 such that the resulting integer equals 5 modulo 13. Count valid integers modulo 10^9 + 7.
- **Core Insight**: Let dp[r] be the number of ways to form a prefix whose value is r modulo 13. Base case: dp[0] = 1. When appending digit d, remainder transitions from r to (r * 10 + d) % 13. If S[i] is a fixed digit d, only that transition is used; if '?', branch over all d in 0..9. Final answer is dp[5].
- **Complexity**: Time: `O(|S| * 13 * 10)` | Space: `O(13)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <string>
#include <vector>

using namespace std;

const int MOD = 1e9 + 7;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!(cin >> s)) return 0;

    vector<long long> dp(13, 0);
    dp[0] = 1;

    for (char c : s) {
        vector<long long> next_dp(13, 0);
        if (c == '?') {
            for (int d = 0; d <= 9; ++d) {
                for (int r = 0; r < 13; ++r) {
                    int nr = (r * 10 + d) % 13;
                    next_dp[nr] = (next_dp[nr] + dp[r]) % MOD;
                }
            }
        } else {
            int d = c - '0';
            for (int r = 0; r < 13; ++r) {
                int nr = (r * 10 + d) % 13;
                next_dp[nr] = (next_dp[nr] + dp[r]) % MOD;
            }
        }
        dp = move(next_dp);
    }

    cout << dp[5] << "\n";
    return 0;
}
```
