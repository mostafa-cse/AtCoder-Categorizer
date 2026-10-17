# Problem Analysis: AtCoder-arc071_d — F. Infinite Sequence

**Problem ID**: `AtCoder-arc071_d`  
**Contest**: `arc071`  
**Rating / Difficulty**: 2336  
**URL**: https://atcoder.jp/contests/arc071/tasks/arc071_d  
**VJudge Tag**: `[problem:AtCoder-arc071_d]`  
**Category File**: [`../categories/dynamic_programming/infinite_sequence_stabilization_dp.md`](../categories/dynamic_programming/infinite_sequence_stabilization_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Intro to DP`  
- **Topic (Skill)**: `Knapsack and Basic Dynamic Programming`  

---

## 1. Problem Statement & Key Idea
Count valid infinite sequences where each value $a_i$ forces the next $a_i$ elements to be identical and stabilizes at step $n$. Two consecutive values $\ge 2$ lock the sequence, yielding a linear DP solved with prefix sums in $O(n)$.

## 2. Core Observation & Invariant
Two consecutive values $\ge 2$ in the sequence lock all subsequent values into an identical constant. A sequence avoids locking up to length $i$ if and only if it consists of 1s separated by isolated numbers $\ge 2$, leading to linear DP $dp[i] = dp[i-1] + \sum_{j=0}^{i-3} dp[j]$.

## 3. Step-by-Step Algorithm
1. Define $dp[i]$ as the number of valid sequences of length $i$ ending in 1 that have not locked into a constant.
2. Compute $dp[i]$ in $O(1)$ per state using running prefix sums.
3. Aggregate configurations where the sequence locks at step $i \in [1, n-2]$, locks at step $n-1$, never locks before $n$, or is identically 1 in $O(n)$ total time.

## 4. Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;

    if (n == 1) {
        cout << 1 << "\n";
        return 0;
    }

    const long long MOD = 1000000007;

    vector<long long> dp(n + 1, 0);
    vector<long long> pref(n + 1, 0);

    dp[0] = 1;
    pref[0] = 1;
    if (n >= 1) {
        dp[1] = 1;
        pref[1] = (pref[0] + dp[1]) % MOD;
    }
    if (n >= 2) {
        dp[2] = 1;
        pref[2] = (pref[1] + dp[2]) % MOD;
    }

    for (int i = 3; i <= n; ++i) {
        dp[i] = (dp[i - 1] + pref[i - 3]) % MOD;
        pref[i] = (pref[i - 1] + dp[i]) % MOD;
    }

    long long sum_n2 = 0;
    for (int i = 1; i <= n - 2; ++i) {
        sum_n2 = (sum_n2 + dp[i]) % MOD;
    }

    long long sum_n1 = 0;
    for (int i = 1; i <= n - 1; ++i) {
        sum_n1 = (sum_n1 + dp[i]) % MOD;
    }

    long long term1 = n % MOD;
    long long term2 = ((n - 1) % MOD) * ((n - 1) % MOD) % MOD;
    long long term3 = (((n - 1) % MOD) * ((n - 1) % MOD) % MOD) * sum_n2 % MOD;
    long long term4 = ((n - 1) % MOD) * sum_n1 % MOD;

    long long ans = (term1 + term2 + term3 + term4) % MOD;
    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
