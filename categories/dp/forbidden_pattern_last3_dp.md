# Dynamic Programming on Last 3 Characters / Forbidden Pattern Counting

**Domain**: `Dynamic Programming`  
**Subtopic**: `Classic DP`  

This workbook contains curated, high-quality competitive programming problems teaching **Dynamic Programming on Last 3 Characters / Forbidden Pattern Counting**.

---

## Curated Problems

### `[problem:AtCoder-abc122_d]` — We Like AGC
- **Rating / Difficulty**: 1533
- **Contest**: `abc122`
- **Analysis**: [`analysis/AtCoder-abc122_d.md`](../../analysis/AtCoder-abc122_d.md)
- **Key Idea**: Forbidden 3-character patterns: 'AGC', 'GAC', 'ACG'. Forbidden 4-character patterns: 'A?GC' (e.g. AGTC->ATGC), 'AG?C'. The validity of appending a character depends only on the last 3 characters.
- **Time Complexity**: `O(N * 4^4)`
- **Space Complexity**: `O(4^3)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 1000000007;

// A=0, G=1, C=2, T=3, dummy=4
bool is_valid(int c1, int c2, int c3, int c4) {
    // Contains "AGC"
    if (c2 == 0 && c3 == 1 && c4 == 2) return false;
    // Swap c3, c4 -> GAC
    if (c2 == 1 && c3 == 0 && c4 == 2) return false;
    // Swap c3, c4 -> ACG
    if (c2 == 0 && c3 == 2 && c4 == 1) return false;
    // Swap c2, c3 -> A?GC
    if (c1 == 0 && c2 == 1 && c4 == 2) return false;
    // Swap c1, c2 -> AG?C
    if (c1 == 0 && c3 == 1 && c4 == 2) return false;
    return true;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    int dp[5][5][5] = {0};
    dp[4][4][4] = 1;

    for (int len = 0; len < n; ++len) {
        int next_dp[5][5][5] = {0};
        for (int c1 = 0; c1 < 5; ++c1) {
            for (int c2 = 0; c2 < 5; ++c2) {
                for (int c3 = 0; c3 < 5; ++c3) {
                    if (!dp[c1][c2][c3]) continue;
                    for (int c4 = 0; c4 < 4; ++c4) {
                        if (is_valid(c1, c2, c3, c4)) {
                            next_dp[c2][c3][c4] = (next_dp[c2][c3][c4] + dp[c1][c2][c3]) % MOD;
                        }
                    }
                }
            }
        }
        for (int c1 = 0; c1 < 5; ++c1) {
            for (int c2 = 0; c2 < 5; ++c2) {
                for (int c3 = 0; c3 < 5; ++c3) {
                    dp[c1][c2][c3] = next_dp[c1][c2][c3];
                }
            }
        }
    }

    int ans = 0;
    for (int c1 = 0; c1 < 4; ++c1) {
        for (int c2 = 0; c2 < 4; ++c2) {
            for (int c3 = 0; c3 < 4; ++c3) {
                ans = (ans + dp[c1][c2][c3]) % MOD;
            }
        }
    }

    cout << ans << "\n";
    return 0;
}
```
