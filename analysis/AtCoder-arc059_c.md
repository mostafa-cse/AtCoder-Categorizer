# Problem Analysis: AtCoder-arc059_c — E. Children and Candies

**Problem ID**: `AtCoder-arc059_c`  
**Contest**: `arc059`  
**Rating / Difficulty**: 2189  
**URL**: https://atcoder.jp/contests/arc059/tasks/arc059_c  
**VJudge Tag**: `[problem:AtCoder-arc059_c]`  
**Category File**: [`../categories/math/polynomial_generating_function_convolution_dp_power_sums.md`](../categories/math/polynomial_generating_function_convolution_dp_power_sums.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Polynomial`  
- **Topic (Skill)**: `Generating Functions`  

---

## 1. Problem Statement & Key Idea
Sum prod_{i=1}^N x_i^{c_i} over all x_i in [A_i, B_i] and all candy allocations sum_{i=1}^N c_i = C with c_i >= 0 modulo 10^9+7. The sum factorizes into polynomial convolution where child i has generating function P_i(t) = sum_{k=0}^C (sum_{x=A_i}^{B_i} x^k) t^k.

## 2. Core Observation & Invariant
The problem is finding the coefficient of t^C in prod_{i=1}^N P_i(t). Precomputing power sum tables S(k, m) = sum_{x=1}^m x^k mod MOD in O(C * max_B) time allows evaluating interval power sums sum_{x=A_i}^{B_i} x^k = S(k, B_i) - S(k, A_i - 1) in O(1). Standard polynomial DP convolving one child at a time runs in O(N C^2) time.

## 3. Step-by-Step Algorithm
1. Precompute power sums S[k][m] = sum_{x=1}^m x^k mod (10^9+7) for all k, m <= 400.
2. Initialize dp[0] = 1, and dp[c] = 0 for c in [1, C].
3. For each child i from 1 to N: compute f[k] = (S[k][B_i] - S[k][A_i - 1]) mod MOD for k in [0, C].
4. Convolve: for c from 0 to C, for k from 0 to C - c: next_dp[c + k] = (next_dp[c + k] + dp[c] * f[k]) mod MOD.
5. Set dp = next_dp.
6. Output dp[C].

## 4. Complexity Analysis
- **Time Complexity**: `O(C * max_B + N * C^2)`
- **Space Complexity**: `O(max_B * C + C)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 1000000007;
const int MAXV = 405;

long long S[MAXV][MAXV]; // S[k][m] = sum_{x=1}^m x^k

void precompute() {
    for (int m = 1; m < MAXV; ++m) {
        long long cur = 1; // m^k
        for (int k = 0; k < MAXV; ++k) {
            S[k][m] = (S[k][m - 1] + cur) % MOD;
            cur = (cur * m) % MOD;
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    precompute();

    int N, C;
    if (!(cin >> N >> C)) return 0;

    vector<int> A(N + 1), B(N + 1);
    for (int i = 1; i <= N; ++i) cin >> A[i];
    for (int i = 1; i <= N; ++i) cin >> B[i];

    vector<long long> dp(C + 1, 0);
    dp[0] = 1;

    for (int i = 1; i <= N; ++i) {
        vector<long long> next_dp(C + 1, 0);
        vector<long long> f(C + 1, 0);
        for (int k = 0; k <= C; ++k) {
            f[k] = (S[k][B[i]] - S[k][A[i] - 1] + MOD) % MOD;
        }

        for (int c = 0; c <= C; ++c) {
            if (dp[c] == 0) continue;
            for (int k = 0; c + k <= C; ++k) {
                next_dp[c + k] = (next_dp[c + k] + dp[c] * f[k]) % MOD;
            }
        }
        dp = move(next_dp);
    }

    cout << dp[C] << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
