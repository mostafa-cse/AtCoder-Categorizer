# Problem Analysis: AtCoder-abc226_h — H - Random Kth Max

**Problem ID**: `AtCoder-abc226_h`  
**Contest**: `abc226`  
**Rating / Difficulty**: 2813  
**URL**: https://atcoder.jp/contests/abc226/tasks/abc226_h  
**VJudge Tag**: `[problem:AtCoder-abc226_h]`  
**Category File**: [`../categories/math/order_statistics_uniform_random_variables_integration.md`](../categories/math/order_statistics_uniform_random_variables_integration.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Probabilities and Expected Values`  
- **Topic (Skill)**: `Probabilities and Expected Values`  

---

## 1. Problem Statement & Key Idea
Given N independent uniform random variables X_i ~ U(L_i, R_i), compute the expected value of their K-th largest element modulo 998244353.

## 2. Core Observation & Invariant
By tail probability integration, E[Y] = int_0^infty P(Y >= t) dt. The event that the K-th largest variable is >= t occurs iff at least K variables satisfy X_i >= t. For any t, p_i(t) = P(X_i >= t) is piecewise linear. Sorting all 2N endpoints {L_i, R_i} partitions the domain into intervals where each p_i(t) is a linear polynomial. Within each interval, the probability generating function prod (1 - p_i(t) + p_i(t) * x) has polynomial coefficients in t, which can be integrated analytically in closed form.

## 3. Step-by-Step Algorithm
1. 1. Collect and sort all boundary coordinates {L_i, R_i} into elementary intervals [t_j, t_{j+1}].
2. 2. For each interval, write p_i(t) = a_i + b_i * t.
3. 3. Compute polynomial DP for the probability that at least K variables are >= t.
4. 4. Integrate the resulting polynomial in t over [t_j, t_{j+1}].
5. 5. Sum the integrals across all intervals modulo 998244353.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^3)`
- **Space Complexity**: `O(N^2)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>

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
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<pair<long long, long long>> intervals(n);
    vector<long long> pts = {0};
    for (int i = 0; i < n; i++) {
        cin >> intervals[i].first >> intervals[i].second;
        pts.push_back(intervals[i].first);
        pts.push_back(intervals[i].second);
    }

    sort(pts.begin(), pts.end());
    pts.erase(unique(pts.begin(), pts.end()), pts.end());

    vector<long long> inv(n + 5, 1);
    for (int i = 1; i < n + 5; i++) {
        inv[i] = modInverse(i);
    }

    long long ans = 0;

    for (size_t idx = 0; idx + 1 < pts.size(); idx++) {
        long long v0 = pts[idx];
        long long v1 = pts[idx + 1];
        long long delta = v1 - v0;
        if (delta <= 0) continue;

        // dp[m] is a polynomial represented as vector of coefficients in x
        vector<vector<long long>> dp(n + 1, vector<long long>(1, 0));
        dp[0][0] = 1;

        for (int i = 0; i < n; i++) {
            long long l = intervals[i].first;
            long long r = intervals[i].second;
            long long inv_len = modInverse(r - l);

            long long alpha = 0, beta = 0;
            if (r <= v0) {
                alpha = 0;
                beta = 0;
            } else if (l >= v1) {
                alpha = 1;
                beta = 0;
            } else {
                alpha = ((r - v0) % MOD * inv_len) % MOD;
                beta = ((-inv_len) % MOD + MOD) % MOD;
            }

            long long one_minus_alpha = ((1 - alpha) % MOD + MOD) % MOD;
            long long one_minus_beta = ((-beta) % MOD + MOD) % MOD;

            vector<vector<long long>> next_dp(n + 1);
            for (int m = n; m >= 0; m--) {
                size_t sz = dp[m].size();
                if (m > 0 && dp[m - 1].size() > sz) sz = dp[m - 1].size();
                vector<long long> poly(sz + 1, 0);

                for (size_t deg = 0; deg < dp[m].size(); deg++) {
                    if (dp[m][deg] == 0) continue;
                    poly[deg] = (poly[deg] + dp[m][deg] * one_minus_alpha) % MOD;
                    poly[deg + 1] = (poly[deg + 1] + dp[m][deg] * one_minus_beta) % MOD;
                }
                if (m > 0) {
                    for (size_t deg = 0; deg < dp[m - 1].size(); deg++) {
                        if (dp[m - 1][deg] == 0) continue;
                        poly[deg] = (poly[deg] + dp[m - 1][deg] * alpha) % MOD;
                        poly[deg + 1] = (poly[deg + 1] + dp[m - 1][deg] * beta) % MOD;
                    }
                }
                next_dp[m] = move(poly);
            }
            dp = move(next_dp);
        }

        vector<long long> poly_sum(n + 2, 0);
        for (int m = k; m <= n; m++) {
            for (size_t deg = 0; deg < dp[m].size(); deg++) {
                poly_sum[deg] = (poly_sum[deg] + dp[m][deg]) % MOD;
            }
        }

        long long cur_delta_pow = delta % MOD;
        for (size_t deg = 0; deg < poly_sum.size(); deg++) {
            if (poly_sum[deg] != 0) {
                long long int_val = poly_sum[deg] * inv[deg + 1] % MOD * cur_delta_pow % MOD;
                ans = (ans + int_val) % MOD;
            }
            cur_delta_pow = (cur_delta_pow * (delta % MOD)) % MOD;
        }
    }

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
