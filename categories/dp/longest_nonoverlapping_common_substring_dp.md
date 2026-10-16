# Longest Common Non-Overlapping Substring DP

**Domain**: `Dynamic Programming`  
**Subtopic**: `Classic DP`  

This workbook contains curated, high-quality competitive programming problems teaching **Longest Common Non-Overlapping Substring DP**.

---

## Curated Problems

### `[problem:AtCoder-abc141_e]` — Who Says a Pun?
- **Rating / Difficulty**: 1459
- **Contest**: `abc141`
- **Analysis**: [`analysis/AtCoder-abc141_e.md`](../../analysis/AtCoder-abc141_e.md)
- **Key Idea**: Use 2D Dynamic Programming to compute the Longest Common Prefix (LCP) between all pairs of suffixes. If the LCP between suffix i and suffix j is L, the non-overlapping constraint restricts the valid substring length to min(L, j - i).
- **Time Complexity**: `O(N^2)`
- **Space Complexity**: `O(N^2)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    string s;
    if (!(cin >> n >> s)) return 0;

    // dp[i][j] = LCP of S[i..] and S[j..]
    vector<vector<int>> dp(n + 1, vector<int>(n + 1, 0));
    int max_len = 0;

    for (int i = n - 1; i >= 0; --i) {
        for (int j = n - 1; j > i; --j) {
            if (s[i] == s[j]) {
                dp[i][j] = dp[i + 1][j + 1] + 1;
                max_len = max(max_len, min(dp[i][j], j - i));
            } else {
                dp[i][j] = 0;
            }
        }
    }

    cout << max_len << "\n";
    return 0;
}
```
