# Problem Analysis: AtCoder-abc263_e — Sugoroku 3

**Problem ID**: `AtCoder-abc263_e`  
**Contest**: `abc263`  
**Rating / Difficulty**: 1659  
**URL**: https://atcoder.jp/contests/abc263/tasks/abc263_e  
**VJudge Tag**: `[problem:AtCoder-abc263_e]`  
**Category File**: [`../categories/dp/expected_value_self_loop_dp.md`](../categories/dp/expected_value_self_loop_dp.md)  

- **Tag (Domain)**: `Dynamic Programming`  
- **Subtopic**: `Expected Value DP`  
- **Topic (Skill)**: `Expected Value DP with Self-Loop Formula + Range Sum Acceleration`  

---

## 1. Problem Statement & Key Idea
A board with N squares (1 to N). At square i, roll an integer die uniformly from 0 to A_i. Move from i to i + die. Find the expected number of rolls to reach square N, modulo 998244353.

**Key Insight**: At square i, rolling 0 causes a self-loop: E[i] = 1 + (1 / (A_i + 1)) * E[i] + (1 / (A_i + 1)) * sum_{j=1}^{A_i} E[i + j]. Solve the self-loop algebraically.

## 2. Core Observation & Invariant
Multiplying by (A_i + 1) and subtracting E[i]: A_i * E[i] = (A_i + 1) + sum_{j=1}^{A_i} E[i + j] => E[i] = ((A_i + 1) + sum_{j=1}^{A_i} E[i + j]) * inv(A_i) mod MOD. The range sum is maintained in O(1) using suffix sums.

## 3. Step-by-Step Algorithm
1. Initialize E[N] = 0.
2. Maintain suffix sums suf_E where suf_E[i] = sum_{k=i}^N E[k].
3. For i from N - 1 down to 1:
4.   sum_future = (suf_E[i + 1] - suf_E[min(n, i + A[i]) + 1] + MOD) % MOD.
5.   numerator = (A[i] + 1 + sum_future) % MOD.
6.   E[i] = (numerator * inv(A[i])) % MOD.
7.   suf_E[i] = (suf_E[i + 1] + E[i]) % MOD.
8. Print E[1].

## 4. Complexity Analysis
- **Time Complexity**: `O(N log(MOD))`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MOD = 998244353;

long long power(long long base, long long exp) {
    long long res = 1;
    base %= MOD;
    while (exp > 0) {
        if (exp % 2 == 1) res = (res * base) % MOD;
        base = (base * base) % MOD;
        exp /= 2;
    }
    return res;
}

long long modInverse(long long n) {
    return power(n, MOD - 2);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 1; i < n; ++i) {
        cin >> a[i];
    }

    vector<long long> E(n + 2, 0);
    vector<long long> suf(n + 2, 0);

    for (int i = n - 1; i >= 1; --i) {
        int r = min((long long)n, i + a[i]);
        long long sum_future = (suf[i + 1] - suf[r + 1] + MOD) % MOD;
        long long num = (a[i] + 1 + sum_future) % MOD;
        E[i] = (num * modInverse(a[i])) % MOD;
        suf[i] = (suf[i + 1] + E[i]) % MOD;
    }

    cout << E[1] << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Resolving self-loop expected value recurrences accelerated by suffix sum lookups.
- **Reusable Pattern**: `Self-Loop Expected Value: E[i] = (total_branches + sum_other_branches) * inv(active_branches).`
