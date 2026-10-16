# Problem Analysis: AtCoder-typical90_e — Restricted Digits

**Problem ID**: `AtCoder-typical90_e`  
**Contest**: `typical90` (Kyopro Typical 90, Problem 005)  
**Rating / Difficulty**: 2400 (★7)  
**URL**: https://atcoder.jp/contests/typical90/tasks/typical90_e  
**VJudge Tag**: `[problem:AtCoder-typical90_e]`  
**Category File**: [`../categories/dp/doubling_dp.md`](../categories/dp/doubling_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `DP on Different Structures`  
- **Topic (Skill)**: `Doubling DP / Matrix Exponentiation on Modular Digit Transitions`  

---

## 1. Problem Statement & Key Idea
Count N-digit positive integers (N <= 10^18) whose digits are chosen from a set of K non-zero digits and are divisible by B (B <= 1000). Modulo 10^9+7.

**Core Idea**: Because N is up to 10^18, sequential digit appending is too slow. Use binary doubling: concatenate numbers of length 2^p.

## 2. Core Observation & Invariant
Concatenating two numbers X and Y each of length L produces X * 10^L + Y. Thus remainder mod B is (rem(X) * 10^L + rem(Y)) % B. Compute dp[p][r] for length 2^p in O(B^2 log N).

## 3. Step-by-Step Algorithm
1. Base: dp[0][c % B] = count of digit c in allowed set.
2. Doubling step: dp[p+1][(r1 * pow10[p] + r2) % B] = sum(dp[p][r1] * dp[p][r2]).
3. Combine binary powers of N to get final remainder distribution.
4. Output answer at remainder 0.

## 4. Complexity Analysis
Time: O(B^2 log N), Space: O(B log N).

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 1e9 + 7;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    int b, k;
    if (!(cin >> n >> b >> k)) return 0;

    vector<int> c(k);
    for (int i = 0; i < k; ++i) cin >> c[i];

    // Compute powers of 10 mod B for step 2^p
    vector<long long> pow10(62);
    pow10[0] = 10 % b;
    for (int p = 1; p < 62; ++p) {
        pow10[p] = (pow10[p - 1] * pow10[p - 1]) % b;
    }

    // dp[p][r]: count of numbers of length 2^p with remainder r mod B
    vector<vector<long long>> dp(62, vector<long long>(b, 0));
    for (int digit : c) {
        dp[0][digit % b] = (dp[0][digit % b] + 1) % MOD;
    }

    for (int p = 0; p < 61; ++p) {
        long long shift = pow10[p];
        for (int r1 = 0; r1 < b; ++r1) {
            if (dp[p][r1] == 0) continue;
            for (int r2 = 0; r2 < b; ++r2) {
                if (dp[p][r2] == 0) continue;
                int nr = (r1 * shift + r2) % b;
                dp[p + 1][nr] = (dp[p + 1][nr] + dp[p][r1] * dp[p][r2]) % MOD;
            }
        }
    }

    // Combine powers for N
    vector<long long> res(b, 0);
    bool first = true;
    for (int p = 0; p < 62; ++p) {
        if ((n >> p) & 1) {
            if (first) {
                res = dp[p];
                first = false;
            } else {
                vector<long long> next_res(b, 0);
                long long shift = pow10[p];
                for (int r1 = 0; r1 < b; ++r1) {
                    if (dp[p][r1] == 0) continue;
                    for (int r2 = 0; r2 < b; ++r2) {
                        if (res[r2] == 0) continue;
                        int nr = (r1 + r2 * shift) % b;
                        next_res[nr] = (next_res[nr] + dp[p][r1] * res[r2]) % MOD;
                    }
                }
                res = next_res;
            }
        }
    }

    cout << res[0] << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Doubling DP on remainder transitions across power-of-two digit lengths.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Doubling DP on large digit lengths, modular arithmetic concatenation, and transition convolution.
- **Reusable Pattern**: `Doubling DP on digit concatenations.`

---
Back to [Doubling DP / Matrix Exponentiation on Modular Digit Transitions](../categories/dp/doubling_dp.md) | [Categories Directory](../categories/README.md)