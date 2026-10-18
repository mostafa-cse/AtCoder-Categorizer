# Problem Analysis: AtCoder-abc279_g — At Most 2 Colors

**Problem ID**: `AtCoder-abc279_g`  
**Contest**: `abc279`  
**Rating / Difficulty**: 2431  
**URL**: https://atcoder.jp/contests/abc279/tasks/abc279_g  
**VJudge Tag**: `[problem:AtCoder-abc279_g]`  
**Category File**: [`../categories/dynamic_programming/at_most_two_colors_sliding_window_1d1d_dp.md`](../categories/dynamic_programming/at_most_two_colors_sliding_window_1d1d_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `DP Optimizations`  
- **Topic (Skill)**: `1D1D DP Optimization`  

---

## 1. Problem Statement & Key Idea
Count colorings where every K-window has at most 2 colors by tracking the rightmost position of the second-to-last color in a 1D DP and optimizing transitions with sliding window prefix sums in O(N) time.

## 2. Core Observation & Invariant
In any valid window of size K, one color always occupies the final square. The state collapses to dp[i-1], the rightmost occurrence of the other color within the window, plus a variable sing tracking monochrome K-windows.

## 3. Step-by-Step Algorithm
1. 1. Initialize sing = C and dp array of size N + 5 to 0.
2. 2. For i from 2 to N: if i - K >= 0, add dp[i - K] to sing.
3. 3. Compute dp[i - 1] = sing * (C - 1) + (sum_{j=i-K+1}^{i-2} dp[j]) using running prefix sums.
4. 4. Update running prefix sums with dp[i - 1].
5. 5. Sum sing and dp[i] for all i in [max(1, N - K + 1), N] modulo 998244353.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

using ll = long long;
const ll MOD = 998244353;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    ll c;
    if (!(cin >> n >> k >> c)) return 0;

    vector<ll> dp(n + 5, 0);
    vector<ll> dp_sum(n + 5, 0);
    ll sing = c % MOD;

    for (int i = 2; i <= n; i++) {
        if (i - k >= 0) {
            sing = (sing + dp[i - k]) % MOD;
        }

        dp[i - 1] = (sing * ((c - 1) % MOD)) % MOD;
        dp[i - 1] = (dp[i - 1] + dp_sum[i - 2]) % MOD;
        if (i - k >= 0) {
            dp[i - 1] = (dp[i - 1] - dp_sum[i - k] + MOD) % MOD;
        }

        dp_sum[i - 1] = (dp_sum[i - 2] + dp[i - 1]) % MOD;
    }

    ll res = sing;
    for (int i = max(1, n - k + 1); i <= n; i++) {
        res = (res + dp[i]) % MOD;
    }

    cout << (res % MOD + MOD) % MOD << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
