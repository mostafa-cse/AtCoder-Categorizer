# Problem Analysis: AtCoder-agc052_c — C. Nondivisible Prefix Sums

**Problem ID**: `AtCoder-agc052_c`  
**Contest**: `agc052`  
**Rating / Difficulty**: 2936  
**URL**: https://atcoder.jp/contests/agc052/tasks/agc052_c  
**VJudge Tag**: `[problem:AtCoder-agc052_c]`  
**Category File**: [`../categories/combinatorics/nondivisible_prefix_sums_majority_complement_counting.md`](../categories/combinatorics/nondivisible_prefix_sums_majority_complement_counting.md)  

- **Tag (Domain)**: `Combinatorics`  
- **Subtopic**: `Techniques`  
- **Topic (Skill)**: `Contribution Technique`  

---

## 1. Problem Statement & Key Idea
Given N and prime P, count sequences A in {1, ..., P-1}^N that can be rearranged so that no prefix sum is divisible by P, modulo 998244353.

## 2. Core Observation & Invariant
A sequence CANNOT be rearranged to avoid sum = 0 (mod P) prefixes if and only if either: (1) total sum is divisible by P, or (2) one value v appears as an overwhelming majority such that the other elements cannot buffer the wraps modulo P. Scaling so that majority element is 1, the bad condition is M - sum(P - y_j) >= P, where M is the count of 1s and y_j are other elements. We count the complement using generating functions and contribution technique.

## 3. Step-by-Step Algorithm
1. 1. Total sequences is (P - 1)^N.
2. 2. Subtract sequences with sum A_i = 0 (mod P), computed via roots of unity / ((P-1)^N + (-1)^N (P-1)) / P.
3. 3. For the majority condition, choose majority value v (P-1 choices) and count sequences where M - sum(P - y_j) >= P via DP / polynomial expansion.
4. 4. Subtract bad majority cases and return result modulo 998244353.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>

using namespace std;

static const int MOD = 998244353;

long long power_mod(long long base, long long exp) {
    long long res = 1;
    base %= MOD;
    if (base < 0) base += MOD;
    while (exp > 0) {
        if (exp & 1) res = (res * base) % MOD;
        base = (base * base) % MOD;
        exp >>= 1;
    }
    return res;
}

long long mod_inverse(long long n) {
    return power_mod(n, MOD - 2);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    long long N, P;
    if (!(cin >> N >> P)) return 0;

    long long total = power_mod(P - 1, N);

    // Case 1: Sequences whose sum is divisible by P
    long long term = (power_mod(P - 1, N) + (P - 1) * (N % 2 == 0 ? 1 : -1)) % MOD;
    term = (term + MOD) % MOD;
    long long case1 = term * mod_inverse(P) % MOD;

    // Case 2: Sequences with sum NOT divisible by P, but dominated by some element
    long long case2 = 0;
    long long max_s = N - P;

    if (max_s >= 0) {
        vector<long long> fact(N + 1, 1), inv(N + 1, 1);
        for (int i = 1; i <= N; ++i) {
            fact[i] = (fact[i - 1] * i) % MOD;
        }
        inv[N] = mod_inverse(fact[N]);
        for (int i = N - 1; i >= 0; --i) {
            inv[i] = (inv[i + 1] * (i + 1)) % MOD;
        }

        auto nCr = [&](int n, int r) -> long long {
            if (r < 0 || r > n) return 0;
            return fact[n] * inv[r] % MOD * inv[n - r] % MOD;
        };

        vector<long long> dp(max_s + 1, 0);
        dp[0] = 1;

        for (int k = 0; k < N; ++k) {
            int M = N - k;
            for (int s = k; s <= max_s; ++s) {
                if (dp[s] && (M - s) >= P && (M - s) % P != 0) {
                    long long ways = nCr(N, k) * dp[s] % MOD;
                    case2 = (case2 + ways) % MOD;
                }
            }

            vector<long long> new_dp(max_s + 1, 0);
            vector<long long> pref(max_s + 2, 0);
            for (int i = 0; i <= max_s; ++i) {
                pref[i + 1] = (pref[i] + dp[i]) % MOD;
            }

            for (int s = 1; s <= max_s; ++s) {
                int l = max(0LL, s - (P - 2));
                int r = s - 1;
                if (l <= r) {
                    long long val = (pref[r + 1] - pref[l]) % MOD;
                    if (val < 0) val += MOD;
                    new_dp[s] = val;
                }
            }
            dp = move(new_dp);
        }
        case2 = (case2 * ((P - 1) % MOD)) % MOD;
    }

    long long ans = (total - case1 - case2) % MOD;
    if (ans < 0) ans += MOD;

    cout << ans << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
