# Edit Distance / Sequence Alignment DP with Cost Function

**Domain**: `Dynamic Programming`  
**Subtopic**: `Classic DP`  

This workbook contains curated, high-quality competitive programming problems teaching **Edit Distance / Sequence Alignment DP with Cost Function**.

---

## Curated Problems

### `[problem:AtCoder-abc185_e]` — Sequence Matching
- **Rating / Difficulty**: 1468
- **Contest**: `abc185`
- **Analysis**: [`analysis/AtCoder-abc185_e.md`](../../analysis/AtCoder-abc185_e.md)
- **Key Idea**: Classic Needleman-Wunsch sequence alignment DP. At each step, either delete A[i], delete B[j], or match/mismatch A[i] with B[j].
- **Time Complexity**: `O(N * M)`
- **Space Complexity**: `O(N * M)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<int> a(n + 1), b(m + 1);
    for (int i = 1; i <= n; ++i) cin >> a[i];
    for (int j = 1; j <= m; ++j) cin >> b[j];

    vector<vector<int>> dp(n + 1, vector<int>(m + 1, 0));
    for (int i = 0; i <= n; ++i) dp[i][0] = i;
    for (int j = 0; j <= m; ++j) dp[0][j] = j;

    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            int match_cost = (a[i] == b[j] ? 0 : 1);
            dp[i][j] = min({dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + match_cost});
        }
    }

    cout << dp[n][m] << "\n";
    return 0;
}
```
