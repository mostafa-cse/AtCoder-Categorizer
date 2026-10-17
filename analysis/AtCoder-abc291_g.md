# Problem Analysis: AtCoder-abc291_g — G. OR Sum

**Problem ID**: `AtCoder-abc291_g`  
**Contest**: `abc291`  
**Rating / Difficulty**: 2176  
**URL**: https://atcoder.jp/contests/abc291/tasks/abc291_g  
**VJudge Tag**: `[problem:AtCoder-abc291_g]`  
**Category File**: [`../categories/math/cyclic_or_convolution_bitwise_ntt.md`](../categories/math/cyclic_or_convolution_bitwise_ntt.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Convolution`  
- **Topic (Skill)**: `Fast Fourier Transform (FFT)`  

---

## 1. Problem Statement & Key Idea
Maximize sum_{i=0}^{N-1} (A_i | B_{(i+k)%N}) over all cyclic shifts k in [0, N-1]. Decompose numbers into 5 bits. For each bit b, x | y = 1 - (1 - x)(1 - y). Compute cyclic cross-correlations of (1 - A) and (1 - B) across all shifts using Number Theoretic Transform (NTT) under modulo 998244353.

## 2. Core Observation & Invariant
The bitwise OR sum decomposes linearly across the 5 independent bit positions 0 <= bit < 5. For each bit, x_i | y_j = 1 - u_i * v_j where u_i = 1 - x_i and v_j = 1 - y_j. The sum sum_i u_i * v_{(i+k)%N} is a cyclic cross-correlation, computed by reversing u and convolving with duplicated v (length 2N) via NTT in O(N log N) time.

## 3. Step-by-Step Algorithm
1. For each bit b in 0..4:
2.   Construct array u of length N with u[N - 1 - i] = 1 - ((A[i] >> b) & 1).
3.   Construct array v of length 2N with v[i] = v[i + N] = 1 - ((B[i] >> b) & 1).
4.   Convolve u and v using NTT modulo 998244353.
5.   For each shift k in 0..N-1, the number of (1, 1) zero-pairs is conv[N - 1 + k], meaning N - conv[N - 1 + k] positions have bit b set in OR.
6.   Add (N - conv[N - 1 + k]) * 2^b to total_score[k].
7. Output max_{k} total_score[k].

## 4. Complexity Analysis
- **Time Complexity**: `O(5 * N log N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
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

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    if (!(cin >> N)) return 0;

    vector<int> A(N), B(N);
    for (int i = 0; i < N; ++i) cin >> A[i];
    for (int i = 0; i < N; ++i) cin >> B[i];

    int sz = 1;
    while (sz < 3 * N) sz <<= 1;

    vector<long long> score(N, 0);

    for (int bit = 0; bit < 5; ++bit) {
        vector<long long> u(sz, 0), v(sz, 0);
        for (int i = 0; i < N; ++i) {
            u[N - 1 - i] = 1 - ((A[i] >> bit) & 1);
            v[i] = 1 - ((B[i] >> bit) & 1);
            v[i + N] = v[i];
        }

        ntt(u, false);
        ntt(v, false);
        for (int i = 0; i < sz; ++i) {
            u[i] = (u[i] * v[i]) % MOD;
        }
        ntt(u, true);

        long long bit_val = 1LL << bit;
        for (int k = 0; k < N; ++k) {
            long long zero_pairs = u[N - 1 + k];
            long long one_pairs = N - zero_pairs;
            score[k] += one_pairs * bit_val;
        }
    }

    long long ans = 0;
    for (int k = 0; k < N; ++k) {
        ans = max(ans, score[k]);
    }
    cout << ans << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
