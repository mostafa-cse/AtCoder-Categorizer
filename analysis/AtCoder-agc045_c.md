# Problem Analysis: AtCoder-agc045_c — C - Range Set

**Problem ID**: `AtCoder-agc045_c`  
**Contest**: `agc045`  
**Rating / Difficulty**: 2758  
**URL**: https://atcoder.jp/contests/agc045/tasks/agc045_c  
**VJudge Tag**: `[problem:AtCoder-agc045_c]`  
**Category File**: [`../categories/dynamic_programming_dp/range_set_reachability_automaton_dp.md`](../categories/dynamic_programming_dp/range_set_reachability_automaton_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Intro to DP`  
- **Topic (Skill)**: `Knapsack and Basic Dynamic Programming`  

---

## 1. Problem Statement & Key Idea
Starting from an all-zero string of length N, we can choose A consecutive characters and replace them with 0, or choose B consecutive characters and replace them with 1, any number of times. Find the number of reachable strings modulo 10^9 + 7.

## 2. Core Observation & Invariant
By symmetry, assume A <= B. A string is reachable if and only if replacing all runs of 0s of length >= A with 1s produces at least one run of 1s of length >= B. We count invalid strings (those that do not produce any run of 1s of length >= B) using dynamic programming. In an invalid string, surviving 0-runs have length < A (acting as delimiters of length 1..A-1), and the segments between delimiters must have length L < B and contain only 0-runs of length >= A. Precomputing the number of such segments of length L via 1D DP allows computing the total invalid strings in O(N^2) time.

## 3. Step-by-Step Algorithm
1. 1. If A > B, swap A and B.
2. 2. Precompute f(L) (valid segments of length L starting and ending with 1) and f_pref(L) (starting segments of length L) using prefix-sum accelerated DP in O(N) time.
3. 3. Run the main DP: DP0[i] (invalid prefixes ending with a surviving 0-run) and DP1[i] (invalid prefixes ending with a 1-block of length < B).
4. 4. Sum invalid configurations and subtract from 2^N modulo 10^9 + 7.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MOD = 1000000007;

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

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, a, b;
    if (!(cin >> n >> a >> b)) return 0;

    if (a > b) swap(a, b);

    int max_L = max(n, b) + 5;

    // Precompute dp1, dp0, f_all, f_pref, f_suff
    vector<long long> dp1(max_L, 0), dp0(max_L, 0), dp1_pref(max_L, 0);
    dp1[0] = 1;
    dp1_pref[0] = 1;

    for (int i = 1; i < max_L; ++i) {
        dp1[i] = (dp1[i - 1] + dp0[i - 1]) % MOD;
        if (i >= a) {
            dp0[i] = dp1_pref[i - a];
        } else {
            dp0[i] = 0;
        }
        dp1_pref[i] = (dp1_pref[i - 1] + dp1[i]) % MOD;
    }

    vector<long long> f_all(max_L, 0), f_pref(max_L, 0);
    for (int i = 0; i < max_L; ++i) {
        f_all[i] = (dp1[i] + dp0[i]) % MOD;
        f_pref[i] = dp1[i];
    }
    const auto& f_suff = f_pref;

    // f(L): starts with 1, ends with 1
    vector<long long> dp1_c(max_L, 0), dp0_c(max_L, 0), dp1_c_pref(max_L, 0);
    dp1_c[1] = 1;
    dp1_c_pref[1] = 1;

    for (int i = 2; i < max_L; ++i) {
        dp1_c[i] = (dp1_c[i - 1] + dp0_c[i - 1]) % MOD;
        if (i - a >= 1) {
            dp0_c[i] = dp1_c_pref[i - a];
        } else {
            dp0_c[i] = 0;
        }
        dp1_c_pref[i] = (dp1_c_pref[i - 1] + dp1_c[i]) % MOD;
    }
    const auto& f = dp1_c;

    // Main DP of length N
    vector<long long> DP0(n + 1, 0), DP1(n + 1, 0);

    for (int d = 1; d <= min(n, a - 1); ++d) {
        DP0[d] = (DP0[d] + 1) % MOD;
    }
    for (int L = 1; L <= min(n, b - 1); ++L) {
        DP1[L] = (DP1[L] + f_pref[L]) % MOD;
    }

    for (int i = 1; i <= n; ++i) {
        if (DP1[i] != 0) {
            for (int d = 1; d < a && i + d <= n; ++d) {
                DP0[i + d] = (DP0[i + d] + DP1[i]) % MOD;
            }
        }
        if (DP0[i] != 0) {
            for (int L = 1; L < b && i + L <= n; ++L) {
                DP1[i + L] = (DP1[i + L] + DP0[i] * f[L]) % MOD;
            }
        }
    }

    long long invalid = DP0[n];
    for (int L = 1; L <= min(n, b - 1); ++L) {
        invalid = (invalid + DP0[n - L] * f_suff[L]) % MOD;
    }

    if (n < b) {
        invalid = (invalid + f_all[n]) % MOD;
    }

    long long total = power(2, n);
    long long ans = (total - invalid) % MOD;
    if (ans < 0) ans += MOD;

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
