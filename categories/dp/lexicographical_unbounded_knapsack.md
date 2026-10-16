# Unbounded Knapsack for Lexicographically Largest Number

**Domain**: `Dynamic Programming`  
**Subtopic**: `Classic DP`  

This workbook contains curated, high-quality competitive programming problems teaching **Unbounded Knapsack for Lexicographically Largest Number**.

---

## Curated Problems

### `[problem:AtCoder-abc118_d]` — Match Matching
- **Rating / Difficulty**: 1657
- **Contest**: `abc118`
- **Analysis**: [`analysis/AtCoder-abc118_d.md`](../../analysis/AtCoder-abc118_d.md)
- **Key Idea**: The larger integer is first determined by having MORE DIGITS. If two integers have the same number of digits, compare lexicographically. Use unbounded knapsack DP: dp[n] = maximum number of digits formable with n matchsticks.
- **Time Complexity**: `O(N * M)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

const int match_costs[10] = {0, 2, 5, 5, 4, 5, 6, 3, 7, 6};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<int> a(m);
    for (int i = 0; i < m; ++i) {
        cin >> a[i];
    }
    sort(a.rbegin(), a.rend());

    vector<int> dp(n + 1, -1e9);
    dp[0] = 0;

    for (int i = 1; i <= n; ++i) {
        for (int d : a) {
            int c = match_costs[d];
            if (i >= c && dp[i - c] >= 0) {
                dp[i] = max(dp[i], dp[i - c] + 1);
            }
        }
    }

    string ans = "";
    int curr = n;

    while (curr > 0) {
        for (int d : a) {
            int c = match_costs[d];
            if (curr >= c && dp[curr - c] == dp[curr] - 1) {
                ans += to_string(d);
                curr -= c;
                break;
            }
        }
    }

    cout << ans << "\n";
    return 0;
}
```
