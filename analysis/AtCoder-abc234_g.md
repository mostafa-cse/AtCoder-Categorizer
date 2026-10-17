# Problem Analysis: AtCoder-abc234_g — G. Divide a Sequence

**Problem ID**: `AtCoder-abc234_g`  
**Contest**: `abc234`  
**Rating / Difficulty**: 2306  
**URL**: https://atcoder.jp/contests/abc234/tasks/abc234_g  
**VJudge Tag**: `[problem:AtCoder-abc234_g]`  
**Category File**: [`../categories/data_structures/dual_monotonic_stack_linear_dp.md`](../categories/data_structures/dual_monotonic_stack_linear_dp.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Segment Tree`  
- **Topic (Skill)**: `Segment Tree with Lazy Propagation`  

---

## 1. Problem Statement & Key Idea
Given array $A$, compute $\sum \prod (\max(B_i) - \min(B_i))$ over all $2^{N-1}$ compositions of $A$ into contiguous blocks, modulo 998244353.

## 2. Core Observation & Invariant
The product sum over partition blocks factors into $(\max(B) - \min(B)) dp[j] = \max(B) dp[j] - \min(B) dp[j]$, decoupling the maximum and minimum contributions independently.

## 3. Step-by-Step Algorithm
1. Maintain two monotonic stacks: one tracking non-increasing maximum values and one tracking non-decreasing minimum values alongside their accumulated $dp$ sums.
2. On inserting $A_i$, pop dominated elements while maintaining prefix sums $S_{\max}$ and $S_{\min}$ in $O(1)$ amortized time.
3. Compute $dp[i] = (S_{\max} - S_{\min}) \bmod 998244353$ in strictly linear $O(N)$ time.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 998244353;

struct Element {
    long long val;
    long long sum_dp;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    if (!(cin >> N)) return 0;
    vector<long long> A(N + 1);
    for (int i = 1; i <= N; ++i) cin >> A[i];

    vector<long long> dp(N + 1, 0);
    dp[0] = 1;

    vector<Element> st_max, st_min;
    long long S_max = 0, S_min = 0;

    for (int i = 1; i <= N; ++i) {
        long long cur_max_dp = dp[i - 1];
        while (!st_max.empty() && st_max.back().val <= A[i]) {
            S_max = (S_max - st_max.back().val * st_max.back().sum_dp) % MOD;
            cur_max_dp = (cur_max_dp + st_max.back().sum_dp) % MOD;
            st_max.pop_back();
        }
        st_max.push_back({A[i], cur_max_dp});
        S_max = (S_max + A[i] * cur_max_dp) % MOD;

        long long cur_min_dp = dp[i - 1];
        while (!st_min.empty() && st_min.back().val >= A[i]) {
            S_min = (S_min - st_min.back().val * st_min.back().sum_dp) % MOD;
            cur_min_dp = (cur_min_dp + st_min.back().sum_dp) % MOD;
            st_min.pop_back();
        }
        st_min.push_back({A[i], cur_min_dp});
        S_min = (S_min + A[i] * cur_min_dp) % MOD;

        dp[i] = (S_max - S_min) % MOD;
        if (dp[i] < 0) dp[i] += MOD;
    }

    cout << dp[N] << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
