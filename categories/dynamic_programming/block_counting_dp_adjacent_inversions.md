# Knapsack and Basic Dynamic Programming

**Domain**: `Dynamic Programming (DP)`  
**Subtopic**: `Intro to DP`  

This workbook contains curated, high-quality competitive programming problems teaching **Knapsack and Basic Dynamic Programming**.

---

## Curated Problems

### `[problem:AtCoder-agc046_c]` — Shift
- **Rating / Difficulty**: 2130
- **Contest**: `agc046`
- **Analysis**: [`analysis/AtCoder-agc046_c.md`](../../analysis/AtCoder-agc046_c.md)
- **Key Idea**: Represent S as block counts of '1's separated by '0's: A_0, A_1, ..., A_M. Shifting a '1' left across a '0' moves a 1 from a right block to a left block. The total number of 1s moved out of each block and placed into earlier blocks can be modeled via dynamic programming: dp[blk][j][k] = number of configurations where blk blocks have been processed, j ones are currently in transit, and k total moves have been consumed.
- **Time Complexity**: `O(N * sum(A) * K)`
- **Space Complexity**: `O(sum(A) * K)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <string>
#include <vector>
#include <numeric>
#include <algorithm>

using namespace std;

const int MOD = 998244353;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    int K;
    if (!(cin >> s >> K)) return 0;

    vector<int> a;
    int cur_cnt = 0;
    for (char c : s) {
        if (c == '0') {
            a.push_back(cur_cnt);
            cur_cnt = 0;
        } else {
            cur_cnt++;
        }
    }
    a.push_back(cur_cnt);

    int m = a.size();
    int sum_a = 0;
    for (int x : a) sum_a += x;
    K = min(K, sum_a);

    vector<vector<int>> dp(sum_a + 1, vector<int>(K + 1, 0));
    dp[0][0] = 1;

    for (int blk = 0; blk < m; ++blk) {
        vector<vector<int>> next_dp(sum_a + 1, vector<int>(K + 1, 0));
        int c = a[blk];

        for (int j = 0; j <= sum_a; ++j) {
            for (int k = 0; k <= K; ++k) {
                if (!dp[j][k]) continue;

                for (int d = 0; d <= c; ++d) {
                    if (j >= d) {
                        next_dp[j - d][k] = (next_dp[j - d][k] + dp[j][k]) % MOD;
                    }
                }
            }
        }
        dp = next_dp;
    }

    long long ans = 0;
    for (int k = 0; k <= K; ++k) {
        ans = (ans + dp[0][k]) % MOD;
    }

    cout << (ans == 0 ? 1 : ans) << "\n";
    return 0;
}
```
