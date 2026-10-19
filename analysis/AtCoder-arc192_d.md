# Problem Analysis: AtCoder-arc192_d — D - Fraction Line

**Problem ID**: `AtCoder-arc192_d`  
**Contest**: `arc192`  
**Rating / Difficulty**: 2722  
**URL**: https://atcoder.jp/contests/arc192/tasks/arc192_d  
**VJudge Tag**: `[problem:AtCoder-arc192_d]`  
**Category File**: [`../categories/basics/fraction_line_gcd_lcm.md`](../categories/basics/fraction_line_gcd_lcm.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Very Basic Math`  
- **Topic (Skill)**: `GCD and LCM`  

---

## 1. Problem Statement & Key Idea
For rational x = P/Q in lowest terms, f(x) = P * Q. Given sequence A of length N-1, find the sum of scores prod(S_i) modulo 998244353 over all good sequences S where f(S_i / S_{i+1}) = A_i and gcd(S_1, ..., S_N) = 1.

## 2. Core Observation & Invariant
The condition f(S_i / S_{i+1}) = A_i decouples independently across distinct prime factors p! For a fixed prime p, let a_j be the exponent of p in A_j, and s_j be the exponent of p in S_j. Then |s_j - s_{j+1}| = a_j, and gcd(S) = 1 requires min(s_j) = 0. The contribution to the score for prime p is p^{sum s_j}. Since sum a_j <= N * log(max A), we can use DP for each prime p: dp[k][flag] represents the current exponent s_j = k and whether 0 has been reached (flag in {0, 1}). Transitions step by +a_j and -a_j, multiplying by p^k at each step. The final answer is the product of sum dp[k][1] over all prime factors.

## 3. Step-by-Step Algorithm
1. 1. For each prime p <= max(A):
2.    a. Extract exponent vector a_j of p in each A_j. If sum(a_j) == 0, continue.
3.    b. Precompute powers of p modulo 998244353 up to sum(a_j).
4.    c. Initialize DP table dp[k][0] = p^k for k > 0, and dp[0][1] = 1.
5.    d. For each step j from 0 to N - 2, update transitions to k - a_j (setting flag=1 if k - a_j == 0) and k + a_j (preserving flag).
6.    e. Sum dp[k][1] across all k, and multiply into the global answer modulo 998244353.
7. 2. Output the accumulated answer.

## 4. Complexity Analysis
- **Time Complexity**: `O(N * max(A) + N^2 * log(max(A)))`
- **Space Complexity**: `O(N * log(max(A)))`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

using namespace std;

const int MOD = 998244353;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    if (!(cin >> N)) return 0;

    vector<int> A(N - 1);
    int max_A = 0;
    for (int i = 0; i < N - 1; ++i) {
        cin >> A[i];
        max_A = max(max_A, A[i]);
    }

    long long ans = 1;

    for (int p = 2; p <= max_A; ++p) {
        vector<int> a(N - 1, 0);
        int sa = 0;
        for (int j = 0; j < N - 1; ++j) {
            while (A[j] % p == 0) {
                a[j]++;
                A[j] /= p;
            }
            sa += a[j];
        }

        if (sa == 0) continue;

        vector<long long> pows(sa + 1, 1);
        for (int j = 1; j <= sa; ++j) {
            pows[j] = (pows[j - 1] * p) % MOD;
        }

        // dp[k][flag]: k in [0, sa], flag in [0, 1]
        vector<vector<long long>> dp(sa + 1, vector<long long>(2, 0));
        for (int k = 0; k <= sa; ++k) {
            dp[k][0] = pows[k];
        }
        dp[0][0] = 0;
        dp[0][1] = 1;

        for (int j = 0; j < N - 1; ++j) {
            vector<vector<long long>> ndp(sa + 1, vector<long long>(2, 0));
            int step = a[j];
            for (int k = 0; k <= sa; ++k) {
                // Down step: k - step
                if (k - step >= 0) {
                    int nxt_k = k - step;
                    int nxt_flag = (nxt_k == 0 ? 1 : 0);

                    long long mult = pows[nxt_k];
                    ndp[nxt_k][nxt_flag] = (ndp[nxt_k][nxt_flag] + dp[k][0] * mult) % MOD;
                    ndp[nxt_k][1] = (ndp[nxt_k][1] + dp[k][1] * mult) % MOD;
                }
                // Up step: k + step
                if (step != 0 && k + step <= sa) {
                    int nxt_k = k + step;
                    long long mult = pows[nxt_k];
                    ndp[nxt_k][0] = (ndp[nxt_k][0] + dp[k][0] * mult) % MOD;
                    ndp[nxt_k][1] = (ndp[nxt_k][1] + dp[k][1] * mult) % MOD;
                }
            }
            dp = move(ndp);
        }

        long long nsum = 0;
        for (int k = 0; k <= sa; ++k) {
            nsum = (nsum + dp[k][1]) % MOD;
        }

        ans = (ans * nsum) % MOD;
    }

    cout << ans << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
