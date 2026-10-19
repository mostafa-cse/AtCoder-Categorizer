# Problem Analysis: AtCoder-agc071_b — B - Maximum Bracket Subsequence

**Problem ID**: `AtCoder-agc071_b`  
**Contest**: `agc071`  
**Rating / Difficulty**: 2842  
**URL**: https://atcoder.jp/contests/agc071/tasks/agc071_b  
**VJudge Tag**: `[problem:AtCoder-agc071_b]`  
**Category File**: [`../categories/dynamic_programming/bracket_sequence_subsequence_dfa_prefix_balance_dp.md`](../categories/dynamic_programming/bracket_sequence_subsequence_dfa_prefix_balance_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Digit DP`  
- **Topic (Skill)**: `Digit DP`  

---

## 1. Problem Statement & Key Idea
Given N, K and a valid bracket sequence S of length K, count strings T of length N whose lexicographically largest valid bracket subsequence of length K is S modulo 998244353.

## 2. Core Observation & Invariant
Valid bracket sequences prefer ')' over '(' for lexicographical maximality. Decompose S into a copies of '()' followed by b prime/splendid bracket sequences (where the first is not '()'). If S = ()^{K/2}, T needs only contain S as a subsequence, yielding sum_{j=K}^N C(j-1, K-1) 2^{N-j}. Otherwise, analyzing the insertion positions of '(' and ')' into the prime components yields rational generating functions: b x^2 / (1-x)^{2a+b+3} for >= 1 insertions, and (b x + 1) / (1-x)^{2a+b+2} for 0 insertions. Extracting coefficients via negative binomial expansion solves the problem in O(1) or O(N) time.

## 3. Step-by-Step Algorithm
1. 1. If S equals () repeated K/2 times, compute sum_{j=K}^N C(j-1, K-1) * 2^(N-j) iteratively in O(N) time.
2. 2. Otherwise, count leading '()' blocks to determine a, and decompose the remainder of S into b prime components.
3. 3. Let m = N - K be the number of inserted characters.
4. 4. Contribution from >= 1 insertions is b * C(m - 2 + (2a + b + 3) - 1, (2a + b + 3) - 1).
5. 5. Contribution from 0 insertions is C(m + (2a + b + 2) - 1, (2a + b + 2) - 1) + b * C(m - 1 + (2a + b + 2) - 1, (2a + b + 2) - 1).
6. 6. Output the sum modulo 998244353.

## 4. Complexity Analysis
- **Time Complexity**: `O(N) for repetitive case, O(K) for general case`
- **Space Complexity**: `O(1)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <string>
#include <vector>

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

long long nCr(long long n, int r) {
    if (r < 0 || r > n) return 0;
    long long num = 1, den = 1;
    for (int i = 0; i < r; ++i) {
        num = (num * ((n - i) % MOD)) % MOD;
        den = (den * (i + 1)) % MOD;
    }
    return num * modInverse(den) % MOD;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, k;
    if (!(cin >> n >> k)) return 0;
    string s;
    cin >> s;

    string all_rep = "";
    for (int i = 0; i < k / 2; ++i) all_rep += "()";

    if (s == all_rep) {
        // ans = sum_{j = k}^n comb(j - 1, k - 1) * 2^(n - j)
        // Maintain comb(j - 1, k - 1) iteratively
        long long current_comb = 1; // comb(k - 1, k - 1)
        long long current_pow2 = power(2, n - k);
        long long inv2 = modInverse(2);

        long long ans = 0;
        for (int j = k; j <= n; ++j) {
            ans = (ans + current_comb * current_pow2) % MOD;
            // update comb(j, k - 1) = comb(j - 1, k - 1) * j / (j - (k - 1))
            if (j < n) {
                current_comb = current_comb * j % MOD * modInverse(j - k + 1) % MOD;
                current_pow2 = current_pow2 * inv2 % MOD;
            }
        }
        cout << ans << "\n";
        return 0;
    }

    int a = 0;
    int idx = 0;
    while (idx + 1 < k && s.substr(idx, 2) == "()") {
        a++;
        idx += 2;
    }

    int b = 0;
    int bal = 0;
    for (int i = idx; i < k; ++i) {
        if (s[i] == '(') bal++;
        else bal--;
        if (bal == 0) b++;
    }

    int m = n - k;
    int p1 = 2 * a + b + 3;
    long long term1 = 1LL * b * nCr(1LL * (m - 2) + p1 - 1, p1 - 1) % MOD;

    int p2 = 2 * a + b + 2;
    long long term2 = (nCr(1LL * m + p2 - 1, p2 - 1) + 1LL * b * nCr(1LL * (m - 1) + p2 - 1, p2 - 1)) % MOD;

    long long ans = (term1 + term2) % MOD;
    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
