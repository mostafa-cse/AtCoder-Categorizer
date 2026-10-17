# Automaton Transition DAG Shortest Non-Subsequence DP with Lexicographical Greedy Reconstruction

**Domain**: `Dynamic Programming (DP)`  
**Subtopic**: `Classic DP`  

This workbook contains curated, high-quality competitive programming problems teaching **Automaton Transition DAG Shortest Non-Subsequence DP with Lexicographical Greedy Reconstruction**.

---

## Curated Problems

### `[problem:AtCoder-arc081_c]` — Don't Be a Subsequence
- **Rating / Difficulty**: 2072
- **Contest**: `arc081`
- **Analysis**: [`analysis/AtCoder-arc081_c.md`](../../analysis/AtCoder-arc081_c.md)
- **Key Idea**: Subsequence matching operates as a transition DAG where from index i, choosing character c jumps to the first occurrence j = next_pos(i, c) >= i. Let dp[i] be the minimum length of a non-subsequence of the suffix A[i..|A|]. From index i, if character c does not appear, length is 1; otherwise length is 1 + dp[next_pos(i, c) + 1]. Computing dp backwards in O(26 |A|) gives optimal lengths. We then greedily reconstruct the lexicographically smallest string by picking the smallest character c achieving dp[i].
- **Time Complexity**: `O(26 * |A|)`
- **Space Complexity**: `O(26 * |A|)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

const int INF = 1e9 + 7;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!(cin >> s)) return 0;

    int n = s.size();
    vector<vector<int>> nxt(n + 2, vector<int>(26, n + 1));

    for (int i = n; i >= 1; --i) {
        for (int c = 0; c < 26; ++c) {
            nxt[i][c] = nxt[i + 1][c];
        }
        nxt[i][s[i - 1] - 'a'] = i;
    }

    vector<int> dp(n + 2, INF);
    dp[n + 1] = 1;

    for (int i = n; i >= 1; --i) {
        for (int c = 0; c < 26; ++c) {
            int p = nxt[i][c];
            if (p == n + 1) {
                dp[i] = 1;
            } else {
                dp[i] = min(dp[i], 1 + dp[p + 1]);
            }
        }
    }

    string ans = "";
    int cur = 1;
    while (cur <= n + 1) {
        for (int c = 0; c < 26; ++c) {
            int p = nxt[cur][c];
            int len = (p == n + 1 ? 1 : 1 + dp[p + 1]);
            if (len == dp[cur]) {
                ans += (char)('a' + c);
                cur = p + 1;
                break;
            }
        }
        if (cur > n) break;
    }

    cout << ans << "\n";
    return 0;
}
```
