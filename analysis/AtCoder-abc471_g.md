# Problem Analysis: AtCoder-abc471_g — G - Caeser Syllables

**Problem ID**: `AtCoder-abc471_g`  
**Contest**: `abc471`  
**Rating / Difficulty**: 2464  
**URL**: https://atcoder.jp/contests/abc471/tasks/abc471_g  
**VJudge Tag**: `[problem:AtCoder-abc471_g]`  
**Category File**: [`../categories/basics/caeser_syllables_cyclic_difference_ntt.md`](../categories/basics/caeser_syllables_cyclic_difference_ntt.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `More Techniques`  
- **Topic (Skill)**: `Difference Array`  

---

## 1. Problem Statement & Key Idea
Count the number of vowel syllables for each cyclic shift $k \in [0, K-1]$ of an array $A$ generated via a linear congruential PRNG.

## 2. Core Observation & Invariant
A syllable starts at index 0 if $(A_0 + k) \bmod K$ is a vowel, or at index $i \ge 1$ if $(A_{i-1} + k) \bmod K$ is a non-vowel and $(A_i + k) \bmod K$ is a vowel. The transition frequencies between $(K - A_i) \bmod K$ and $(K - A_{i-1}) \bmod K$ can be viewed as coefficients of a 2D bivariate polynomial $A(x, y)$, and the required counts correspond to the cyclic convolution of $A$ with non-vowel indicator $S(x)$ and vowel indicator $T(y)$. Decomposing into independent 1D circular convolutions via NTT solves all $K$ shifts efficiently.

## 3. Step-by-Step Algorithm
1. 1. Generate $A_0, \dots, A_{N-1}$ using the provided PRNG pseudocode.
2. 2. Count transition frequencies $rarr[j][i]$ where $j = (K - A_v) \bmod K$ and $i = (K - A_{v-1}) \bmod K$.
3. 3. Form indicator arrays $S$ (non-vowels) and $T$ (vowels).
4. 4. For each $j$, compute the cyclic convolution of $rarr[j]$ and $S$ using NTT to obtain $rsarr[j]$.
5. 5. Transpose $rsarr$ to $rsbrr$, and for each row compute the cyclic convolution with $T$ using NTT to obtain $rst$.
6. 6. For each shift $k$, the answer is $rst[k][k] + [V[(A_0 + k) \bmod K] == 1]$.

## 4. Complexity Analysis
- **Time Complexity**: `O(N + K^2 \log K)`
- **Space Complexity**: `O(K^2)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <cstdint>

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

void ntt(vector<long long> &a, bool invert) {
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
                a[i + j] = (u + v < MOD ? u + v : u + v - MOD);
                a[i + j + len / 2] = (u - v >= 0 ? u - v : u - v + MOD);
                w = (w * wlen) % MOD;
            }
        }
    }

    if (invert) {
        long long n_inv = modInverse(n);
        for (long long &x : a) x = (x * n_inv) % MOD;
    }
}

vector<long long> convolve(const vector<long long> &a, const vector<long long> &b) {
    int n = 1;
    while (n < (int)a.size() + (int)b.size()) n <<= 1;
    vector<long long> fa(n, 0), fb(n, 0);
    for (size_t i = 0; i < a.size(); i++) fa[i] = a[i] % MOD;
    for (size_t i = 0; i < b.size(); i++) fb[i] = b[i] % MOD;
    ntt(fa, false);
    ntt(fb, false);
    for (int i = 0; i < n; i++) fa[i] = (fa[i] * fb[i]) % MOD;
    ntt(fa, true);
    return fa;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    long long N;
    int K, M;
    uint64_t seed;
    if (!(cin >> N >> K >> seed >> M)) return 0;

    vector<int> b(M);
    for (int i = 0; i < M; ++i) cin >> b[i];

    vector<int> V(K);
    for (int i = 0; i < K; ++i) cin >> V[i];

    vector<vector<long long>> rarr(K, vector<long long>(K, 0));

    uint64_t state = seed;
    int prev_a = -1;
    int first_a = -1;

    for (long long i = 0; i < N; ++i) {
        int cur_a;
        if (i < M) {
            cur_a = b[i];
        } else {
            uint64_t x = (((state >> 18) ^ state) >> 27) & 0xFFFFFFFFULL;
            uint64_t r = state >> 59;
            uint64_t y = ((x >> r) + (x << (32 - r))) & 0xFFFFFFFFULL;
            cur_a = y % K;
            state = state * 6364136223846793005ULL + 2026081520260815ULL;
        }

        if (i == 0) first_a = cur_a;
        else {
            int idx_j = (K - cur_a) % K;
            int idx_i = (K - prev_a) % K;
            rarr[idx_j][idx_i]++;
        }
        prev_a = cur_a;
    }

    vector<long long> s(K, 0), t(K, 0);
    for (int i = 0; i < K; ++i) {
        if (V[i] == 1) t[i]++;
        else s[i]++;
    }

    vector<vector<long long>> rsarr(K, vector<long long>(K, 0));
    for (int i = 0; i < K; ++i) {
        vector<long long> p = convolve(rarr[i], s);
        for (size_t v = 0; v < p.size(); ++v) {
            rsarr[i][v % K] += p[v];
        }
    }

    vector<vector<long long>> rsbrr(K, vector<long long>(K, 0));
    for (int i = 0; i < K; ++i) {
        for (int j = 0; j < K; ++j) {
            rsbrr[i][j] = rsarr[j][i];
        }
    }

    vector<vector<long long>> rst(K, vector<long long>(K, 0));
    for (int i = 0; i < K; ++i) {
        vector<long long> q = convolve(rsbrr[i], t);
        for (size_t v = 0; v < q.size(); ++v) {
            rst[i][v % K] += q[v];
        }
    }

    for (int i = 0; i < K; ++i) {
        long long ans = rst[i][i];
        if (V[(first_a + i) % K] == 1) ans++;
        cout << ans << "\n";
    }

    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
