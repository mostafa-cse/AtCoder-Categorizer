# Problem Analysis: AtCoder-abc117_d — XXOR

**Problem ID**: `AtCoder-abc117_d`  
**Contest**: `abc117`  
**Rating / Difficulty**: 1423  
**URL**: https://atcoder.jp/contests/abc117/tasks/abc117_d  
**VJudge Tag**: `[problem:AtCoder-abc117_d]`  
**Category File**: [`../categories/dp/bitwise_digit_dp_upper_bound.md`](../categories/dp/bitwise_digit_dp_upper_bound.md)  

- **Tag (Domain)**: `Dynamic Programming`  
- **Subtopic**: `Digit DP`  
- **Topic (Skill)**: `Bitwise Digit DP with Upper Bound Constraint`  

---

## 1. Problem Statement & Key Idea
Given N integers A_1, ..., A_N and an upper bound K (0 <= K <= 10^12). Find an integer X such that 0 <= X <= K that maximizes f(X) = sum_{i=1}^N (X XOR A_i).

**Key Insight**: Process bits from most significant (bit 45) down to 0 using Digit DP tracking whether X is already strictly less than K.

## 2. Core Observation & Invariant
For any bit b, setting the b-th bit of X to 0 yields cnt_ones[b] * 2^b in the total sum. Setting it to 1 yields (N - cnt_ones[b]) * 2^b. Bits are independent except for the upper bound prefix constraint of K.

## 3. Step-by-Step Algorithm
1. Compute bit counts cnt[b]: number of elements in A with the b-th bit set, for b = 45 down to 0.
2. Define dp[b][less] as the maximum XOR sum achievable from bit b down to 0, where less is boolean (true if X is strictly less than K).
3. Base case: dp[46][0] = 0, dp[46][1] = -1.
4. For bit b = 45 down to 0:
5.   kb = (K >> b) & 1.
6.   For less in {0, 1}:
7.     If dp[b+1][less] == -1 continue.
8.     Max allowed digit for bit b is: max_d = (less ? 1 : kb).
9.     For d in 0..max_d:
10.       next_less = less || (d < kb).
11.       contrib = 1LL * (d ? (N - cnt[b]) : cnt[b]) * (1LL << b).
12.       dp[b][next_less] = max(dp[b][next_less], dp[b+1][less] + contrib).
13. Print max(dp[0][0], dp[0][1]).

## 4. Complexity Analysis
- **Time Complexity**: `O(log K)`
- **Space Complexity**: `O(log K)`

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
    long long k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> a(n);
    vector<int> cnt(46, 0);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        for (int b = 0; b <= 45; ++b) {
            if ((a[i] >> b) & 1) {
                cnt[b]++;
            }
        }
    }

    // dp[b][less]: max contribution from bit 45 down to b
    vector<vector<long long>> dp(47, vector<long long>(2, -1));
    dp[46][0] = 0;

    for (int b = 45; b >= 0; --b) {
        int kb = (k >> b) & 1;
        for (int less = 0; less < 2; ++less) {
            if (dp[b + 1][less] == -1) continue;

            int max_d = less ? 1 : kb;
            for (int d = 0; d <= max_d; ++d) {
                int next_less = less || (d < kb);
                long long contrib = 1LL * (d ? (n - cnt[b]) : cnt[b]) * (1LL << b);
                dp[b][next_less] = max(dp[b][next_less], dp[b + 1][less] + contrib);
            }
        }
    }

    cout << max(dp[0][0], dp[0][1]) << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Digit DP on binary representations to enforce numerical upper bounds on bitwise optimizations.
- **Reusable Pattern**: `Bitwise Digit DP: dp[bit][less] with transitions d in 0..(less ? 1 : k_bit).`
