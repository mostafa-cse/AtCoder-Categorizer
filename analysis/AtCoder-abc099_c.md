# Problem Analysis: AtCoder-abc099_c — Strange Bank

**Problem ID**: `AtCoder-abc099_c`  
**Contest**: `abc099`  
**Rating / Difficulty**: 1101  
**URL**: https://atcoder.jp/contests/abc099/tasks/abc099_c  
**VJudge Tag**: `[problem:AtCoder-abc099_c]`  
**Category File**: [`../categories/dp/coin_change_dual_exponential_bases.md`](../categories/dp/coin_change_dual_exponential_bases.md)  

- **Tag (Domain)**: `Dynamic Programming`  
- **Subtopic**: `Classic DP`  
- **Topic (Skill)**: `Coin Change / Minimum Steps with Dual Exponential Bases`  

---

## 1. Problem Statement & Key Idea
Withdraw N yen using 1 yen, powers of 6 (6, 36, 216...), and powers of 9 (9, 81, 729...). Find the minimum total withdrawals for N <= 100,000.

**Key Idea**: This is standard minimum coin change DP with coin denominations {1, 6^k, 9^k} <= N.

## 2. Core Observation & Invariant
Since N <= 10^5, the total number of denominations <= 100,000 is small (only 1 + 6 + 5 = 12 coins). Formulate 1D DP: dp[i] = min_{coin} (dp[i - coin] + 1) in O(N * C).

## 3. Step-by-Step Algorithm
1. Collect all powers of 6 <= N and powers of 9 <= N.
2. Initialize dp array of size N + 1 to INF; dp[0] = 0.
3. For i from 1 to N: dp[i] = dp[i - 1] + 1; for each coin in powers: if i >= coin: dp[i] = min(dp[i], dp[i - coin] + 1).
4. Output dp[N].

## 4. Complexity Analysis
- **Time Complexity**: `O(N * log N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> coins = {1};
    for (int p6 = 6; p6 <= n; p6 *= 6) coins.push_back(p6);
    for (int p9 = 9; p9 <= n; p9 *= 9) coins.push_back(p9);

    vector<int> dp(n + 1, 1e9);
    dp[0] = 0;

    for (int i = 1; i <= n; ++i) {
        for (int c : coins) {
            if (i >= c) {
                dp[i] = min(dp[i], dp[i - c] + 1);
            }
        }
    }

    cout << dp[n] << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Unbounded coin change DP over mixed geometric base denominations.
- **Reusable Pattern**: `Coin change DP: dp[i] = min(dp[i - coin] + 1).`
