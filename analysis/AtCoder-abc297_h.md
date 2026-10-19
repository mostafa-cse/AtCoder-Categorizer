# Problem Analysis: AtCoder-abc297_h — Ex - Diff Adjacent

**Problem ID**: `AtCoder-abc297_h`  
**Contest**: `abc297`  
**Rating / Difficulty**: 2855  
**URL**: https://atcoder.jp/contests/abc297/tasks/abc297_h  
**VJudge Tag**: `[problem:AtCoder-abc297_h]`  
**Category File**: [`../categories/math/splendid_compositions_adjacent_diff_generating_function.md`](../categories/math/splendid_compositions_adjacent_diff_generating_function.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Polynomial`  
- **Topic (Skill)**: `Generating Functions`  

---

## 1. Problem Statement & Key Idea
A sequence of positive integers is splendid if all adjacent terms are distinct. Find the sum of lengths of all splendid sequences whose sum of elements is N modulo 998244353.

## 2. Core Observation & Invariant
Let f(x, y) be the bivariate generating function where [x^N y^M] f(x, y) is the count of splendid compositions of N with length M. By PIE on adjacent equal elements, g(x, y) = sum_{i=1}^inf x^i y / (1 + x^i y), so f(x, y) = 1 / (1 - g(x, y)). The sum of lengths is given by d/dy f(x, y)|_{y=1} = P(x) / Q(x)^2, where Q(x) = 1 - sum_{i=1}^inf x^i / (1 + x^i) and P(x) = sum_{i=1}^inf x^i / (1 + x^i)^2. Expanding P(x) and Q(x) via divisor sums takes O(N log N) time, followed by NTT polynomial inversion and multiplication.

## 3. Step-by-Step Algorithm
1. 1. Compute coefficients of Q(x) = 1 - sum_{i=1}^N sum_{k=1}^{N/i} (-1)^{k-1} x^{ik} in O(N log N) via sieve.
2. 2. Compute coefficients of P(x) = sum_{i=1}^N sum_{k=1}^{N/i} k * (-1)^{k-1} x^{ik} in O(N log N) via sieve.
3. 3. Compute polynomial inverse inv_Q = 1 / Q mod x^{N+1} using Newton's method with NTT in O(N log N).
4. 4. Compute inv_Q2 = inv_Q^2 mod x^{N+1} using NTT multiplication.
5. 5. Compute h(x) = P(x) * inv_Q2 mod x^{N+1} using NTT.
6. 6. Output h[N] modulo 998244353.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N)`
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
                a[i + j] = (u + v >= MOD ? u + v - MOD : u + v);
                a[i + j + len / 2] = (u - v < 0 ? u - v + MOD : u - v);
                w = (w * wlen) % MOD;
            }
        }
    }
    if (invert) {
        long long n_inv = modInverse(n);
        for (long long& x : a) x = (x * n_inv) % MOD;
    }
}

vector<long long> multiply(vector<long long> const& a, vector<long long> const& b, int max_len) {
    vector<long long> fa(a.begin(), a.end()), fb(b.begin(), b.end());
    int n = 1;
    while (n < (int)(fa.size() + fb.size())) n <<= 1;
    fa.resize(n);
    fb.resize(n);
    ntt(fa, false);
    ntt(fb, false);
    for (int i = 0; i < n; i++) fa[i] = (fa[i] * fb[i]) % MOD;
    ntt(fa, true);
    if ((int)fa.size() > max_len) fa.resize(max_len);
    return fa;
}

vector<long long> poly_inv(const vector<long long>& a, int deg) {
    vector<long long> res = {modInverse(a[0])};
    while ((int)res.size() < deg) {
        int len = res.size() * 2;
        vector<long long> cur_a(len, 0);
        for (int i = 0; i < min((int)a.size(), len); ++i) cur_a[i] = a[i];

        vector<long long> cur_res = res;
        int n = 1;
        while (n < 2 * len) n <<= 1;
        cur_a.resize(n);
        cur_res.resize(n);

        ntt(cur_a, false);
        ntt(cur_res, false);
        for (int i = 0; i < n; i++) {
            long long term = (2 - cur_a[i] * cur_res[i] % MOD + MOD) % MOD;
            cur_res[i] = (cur_res[i] * term) % MOD;
        }
        ntt(cur_res, true);
        cur_res.resize(len);
        res = move(cur_res);
    }
    res.resize(deg);
    return res;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> Q(n + 1, 0);
    vector<long long> P(n + 1, 0);

    Q[0] = 1;
    for (int i = 1; i <= n; ++i) {
        long long sign = 1;
        for (int k = 1; i * k <= n; ++k) {
            int m = i * k;
            if (sign == 1) {
                Q[m] = (Q[m] - 1 + MOD) % MOD;
                P[m] = (P[m] + k) % MOD;
            } else {
                Q[m] = (Q[m] + 1) % MOD;
                P[m] = (P[m] - k + MOD) % MOD;
            }
            sign = -sign;
        }
    }

    // inv_Q = 1 / Q mod x^{n+1}
    vector<long long> inv_Q = poly_inv(Q, n + 1);

    // inv_Q2 = inv_Q^2 mod x^{n+1}
    vector<long long> inv_Q2 = multiply(inv_Q, inv_Q, n + 1);

    // h = P * inv_Q2 mod x^{n+1}
    vector<long long> h = multiply(P, inv_Q2, n + 1);

    cout << h[n] << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
