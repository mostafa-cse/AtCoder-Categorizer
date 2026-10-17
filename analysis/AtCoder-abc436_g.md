# Problem Analysis: AtCoder-abc436_g — Linear Inequation

**Problem ID**: `AtCoder-abc436_g`  
**Contest**: `abc436`  
**Rating / Difficulty**: 2164  
**URL**: https://atcoder.jp/contests/abc436/tasks/abc436_g  
**VJudge Tag**: `[problem:AtCoder-abc436_g]`  
**Category File**: [`../categories/math/bostan_mori_polynomial_transitions_linear_inequations.md`](../categories/math/bostan_mori_polynomial_transitions_linear_inequations.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Polynomial`  
- **Topic (Skill)**: `Generating Functions`  

---

## 1. Problem Statement & Key Idea
Count non-negative integer solutions to sum_{i=1}^N A_i x_i <= M modulo 998244353 for M <= 10^18. Solved using binary digit decomposition Bostan-Mori polynomial transitions.

## 2. Core Observation & Invariant
Decomposing x_i = 2 Q_i + R_i with R_i in {0, 1} yields 2 sum A_i Q_i + sum A_i R_i <= M. Let S(x) = prod_{i=1}^N (1 + x^{A_i}). Tracking polynomial coefficients coef where sum coef[M-i] f(A, i) is invariant, each step convolves S with coef and downsamples degrees by factor 2 (M <- M / 2).

## 3. Step-by-Step Algorithm
1. Compute polynomial S(x) = prod_{i=1}^N (1 + x^{A_i}) using knapsack DP, where deg(S) = sum A_i <= 10000.
2. Initialize coefficient vector coef = {1} representing state M.
3. While M > 0: compute polynomial convolution conv = S * coef using Number Theoretic Transform (NTT).
4. Downsample: accumulate conv[i] into result[M/2 - (M-i)/2] for i <= M. Set coef = result, M = M / 2.
5. Output coef[0] modulo 998244353.

## 4. Complexity Analysis
- **Time Complexity**: `O(log M * (sum A_i) log(sum A_i))`
- **Space Complexity**: `O(sum A_i)`

## 5. C++ Source Code (Verified & Clean)
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MOD = 998244353;
const int G = 3;

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

void ntt(vector<long long>& a, bool invert) {
    int n = a.size();
    for (int i = 1, j = 0; i < n; i++) {
        int bit = n >> 1;
        for (; j & bit; bit >>= 1) j ^= bit;
        j ^= bit;
        if (i < j) swap(a[i], a[j]);
    }

    for (int len = 2; len <= n; len <<= 1) {
        long long wlen = power(G, (MOD - 1) / len);
        if (invert) wlen = modInverse(wlen);
        for (int i = 0; i < n; i += len) {
            long long w = 1;
            for (int j = 0; j < len / 2; j++) {
                long long u = a[i + j];
                long long v = (a[i + j + len / 2] * w) % MOD;
                a[i + j] = (u + v < MOD ? u + v : u + v - MOD);
                a[i + j + len / 2] = (u - v >= 0 ? u - v : u - v + MOD);
                w = (w * wlen) % MOD;
            }
        }
    }

    if (invert) {
        long long n_inv = modInverse(n);
        for (long long& x : a) x = (x * n_inv) % MOD;
    }
}

vector<long long> multiply(vector<long long> const& a, vector<long long> const& b) {
    vector<long long> fa(a.begin(), a.end()), fb(b.begin(), b.end());
    int n = 1;
    while (n < (int)a.size() + (int)b.size()) n <<= 1;
    fa.resize(n);
    fb.resize(n);
    ntt(fa, false);
    ntt(fb, false);
    for (int i = 0; i < n; i++) fa[i] = (fa[i] * fb[i]) % MOD;
    ntt(fa, true);
    while (fa.size() > 1 && fa.back() == 0) fa.pop_back();
    return fa;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    unsigned long long M;
    if (!(cin >> n >> M)) return 0;

    vector<int> A(n);
    int sumA = 0;
    for (int i = 0; i < n; ++i) {
        cin >> A[i];
        sumA += A[i];
    }

    vector<long long> S(sumA + 1, 0);
    S[0] = 1;
    int cur_deg = 0;
    for (int a_val : A) {
        for (int i = cur_deg; i >= 0; --i) {
            if (S[i]) {
                S[i + a_val] = (S[i + a_val] + S[i]) % MOD;
            }
        }
        cur_deg += a_val;
    }

    vector<long long> coef = {1};

    while (M > 0) {
        vector<long long> conv = multiply(S, coef);
        int res_size = M / 2 - (M - min(M, (unsigned long long)conv.size() - 1)) / 2 + 1;
        vector<long long> result(res_size, 0);

        for (size_t i = 0; i < conv.size() && i <= M; ++i) {
            int target_idx = M / 2 - (M - i) / 2;
            result[target_idx] = (result[target_idx] + conv[i]) % MOD;
        }

        coef = move(result);
        M /= 2;
    }

    cout << coef[0] << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
