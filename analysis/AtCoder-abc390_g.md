# Problem Analysis: AtCoder-abc390_g — G - Permutation Concatenation

**Problem ID**: `AtCoder-abc390_g`  
**Contest**: `abc390`  
**Rating / Difficulty**: 2508  
**URL**: https://atcoder.jp/contests/abc390/tasks/abc390_g  
**VJudge Tag**: `[problem:AtCoder-abc390_g]`  
**Category File**: [`../categories/math/permutation_concatenation_ntt_convolution.md`](../categories/math/permutation_concatenation_ntt_convolution.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Convolution`  
- **Topic (Skill)**: `Number Theoretic Transform (NTT)`  

---

## 1. Problem Statement & Key Idea
Compute the sum of integers formed by concatenating all $N!$ permutations of $(1, 2, \dots, N)$ modulo 998244353.

## 2. Core Observation & Invariant
Each number $x \in \{1, \dots, N\}$ has digit length $d(x) = \lfloor \log_{10} x \rfloor + 1$. In a permutation, the contribution of $x$ depends on its value $x$ and the sum of digit lengths of all numbers appearing after $x$. Partition the numbers $1 \dots N$ into at most 6 buckets based on their digit lengths $d \in \{1, 2, 3, 4, 5, 6\}$. For each bucket, the generating function of the exponent $\sum 10^{d(y)}$ factorizes as a product of polynomials $\prod (1 + 10^{d_i} t)$, solved via divide-and-conquer NTT polynomial multiplication.

## 3. Step-by-Step Algorithm
1. 1. Count the frequency of numbers with digit length $d$ for $d \in \{1, \dots, 6\}$.
2. 2. Compute the sum of values in each digit length bucket.
3. 3. Formulate the generating function of powers of 10 for elements placed after position $k$.
4. 4. Use divide-and-conquer NTT to compute the master polynomial $P(t) = \prod_{i=1}^N (1 + 10^{d_i} t)$.
5. 5. For each digit class, divide out one factor $(1 + 10^d t)$ in linear time, then compute the inner product with factorial permutations.
6. 6. Sum the contributions of all buckets modulo 998244353.

## 4. Complexity Analysis
- **Time Complexity**: `O(N \log^2 N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <map>

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

void ntt(vector<long long>& a, bool invert) {
    int n = a.size();
    for (int i = 1, j = 0; i < n; i++) {
        int bit = n >> 1;
        for (; j & bit; bit >>= 1) j ^= bit;
        j ^= bit;
        if (i < j) swap(a[i], a[j]);
    }
    for (int len = 2; len <= n; len <<= 1) {
        long long wlen = power(3, (MOD - 1) / len);
        if (invert) wlen = modInverse(wlen);
        for (int i = 0; i < n; i += len) {
            long long w = 1;
            for (int j = 0; j < len / 2; j++) {
                long long u = a[i + j];
                long long v = (a[i + j + len / 2] * w) % MOD;
                a[i + j] = (u + v) % MOD;
                a[i + j + len / 2] = (u - v + MOD) % MOD;
                w = (w * wlen) % MOD;
            }
        }
    }
    if (invert) {
        long long n_inv = modInverse(n);
        for (long long& x : a) x = (x * n_inv) % MOD;
    }
}

vector<long long> multiply(const vector<long long>& a, const vector<long long>& b) {
    vector<long long> fa(a.begin(), a.end()), fb(b.begin(), b.end());
    int n = 1;
    while (n < a.size() + b.size()) n <<= 1;
    fa.resize(n); fb.resize(n);
    ntt(fa, false); ntt(fb, false);
    for (int i = 0; i < n; i++) fa[i] = (fa[i] * fb[i]) % MOD;
    ntt(fa, true);
    while (fa.size() > 1 && fa.back() == 0) fa.pop_back();
    return fa;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    if (!(cin >> N)) return 0;

    map<int, int> counts;
    map<int, long long> sums;
    for (int x = 1; x <= N; ++x) {
        int d = to_string(x).length();
        counts[d]++;
        sums[d] = (sums[d] + x) % MOD;
    }

    vector<long long> fact(N + 1, 1), invFact(N + 1, 1);
    for (int i = 1; i <= N; ++i) fact[i] = (fact[i - 1] * i) % MOD;
    invFact[N] = modInverse(fact[N]);
    for (int i = N - 1; i >= 0; --i) invFact[i] = (invFact[i + 1] * (i + 1)) % MOD;

    auto nCr = [&](int n, int r) -> long long {
        if (r < 0 || r > n) return 0;
        return fact[n] * invFact[r] % MOD * invFact[n - r] % MOD;
    };

    vector<long long> poly = {1};
    for (auto& p : counts) {
        int d = p.first;
        int c = p.second;
        long long ten_d = power(10, d);

        vector<long long> bin_p(c + 1, 0);
        long long cur_pow = 1;
        for (int j = 0; j <= c; ++j) {
            bin_p[j] = (nCr(c, j) * cur_pow) % MOD;
            cur_pow = (cur_pow * ten_d) % MOD;
        }
        poly = multiply(poly, bin_p);
    }

    long long ans = 0;
    for (auto& p : counts) {
        int d = p.first;
        long long ten_d = power(10, d);

        vector<long long> Q(N, 0);
        Q[0] = poly[0];
        for (int i = 1; i < N; ++i) {
            long long prev = (ten_d * Q[i - 1]) % MOD;
            Q[i] = (poly[i] - prev + MOD) % MOD;
        }

        long long total_d = 0;
        for (int k = 0; k < N; ++k) {
            long long weight = (fact[k] * fact[N - 1 - k]) % MOD;
            total_d = (total_d + Q[k] * weight) % MOD;
        }
        ans = (ans + total_d * sums[d]) % MOD;
    }

    cout << ans << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
