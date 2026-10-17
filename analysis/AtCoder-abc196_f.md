# Problem Analysis: AtCoder-abc196_f — F. Substring 2

**Problem ID**: `AtCoder-abc196_f`  
**Contest**: `abc196`  
**Rating / Difficulty**: 2274  
**URL**: https://atcoder.jp/contests/abc196/tasks/abc196_f  
**VJudge Tag**: `[problem:AtCoder-abc196_f]`  
**Category File**: [`../categories/math/ntt_binary_string_hamming_distance.md`](../categories/math/ntt_binary_string_hamming_distance.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Convolution`  
- **Topic (Skill)**: `Number Theoretic Transform (NTT)`  

---

## 1. Problem Statement & Key Idea
Given binary strings $S$ and $T$ ($|T| \le |S| \le 10^6$). Choose a substring of $S$ of length $|T|$ to minimize the Hamming distance (number of differing characters) from $T$.

## 2. Core Observation & Invariant
The mismatch count at offset $i$ is $\sum_{j=0}^{|T|-1} [S[i+j] \neq T[j]] = \sum [S[i+j] == 0 \land T[j] == 1] + \sum [S[i+j] == 1 \land T[j] == 0]$.
Let $T^R$ be the reversal of $T$. Then $\sum_{j=0}^{|T|-1} S_1[i+j] T_0^R[|T|-1-j]$ is precisely the convolution of indicator array $S_1$ with $T_0^R$, evaluated at index $i + |T| - 1$. Similarly, the other term is the convolution of $S_0$ with $T_1^R$. Using NTT modulo 998244353, both convolutions are computed in $O(|S| \log |S|)$ time.

## 3. Step-by-Step Algorithm
1. Construct binary indicator vectors $S_0, S_1$ of size $|S|$ and reversed indicator vectors $T_0^R, T_1^R$ of size $|T|$.
2. Convolve $S_0$ with $T_1^R$ using NTT.
3. Convolve $S_1$ with $T_0^R$ using NTT.
4. For each starting index $i \in [0, |S| - |T|]$, the mismatch count is $conv_1[i + |T| - 1] + conv_2[i + |T| - 1]$.
5. Find and output the minimum mismatch count.

## 4. Complexity Analysis
- **Time Complexity**: `O(|S| \log |S|)`
- **Space Complexity**: `O(|S|)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <string>
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
    for (int i = 1, j = 0; i < n; ++i) {
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
            for (int j = 0; j < len / 2; ++j) {
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

vector<long long> multiply(const vector<long long>& a, const vector<long long>& b) {
    int need = a.size() + b.size() - 1;
    int n = 1;
    while (n < need) n <<= 1;
    vector<long long> fa(a.begin(), a.end()), fb(b.begin(), b.end());
    fa.resize(n, 0);
    fb.resize(n, 0);
    ntt(fa, false);
    ntt(fb, false);
    for (int i = 0; i < n; ++i) fa[i] = (fa[i] * fb[i]) % MOD;
    ntt(fa, true);
    fa.resize(need);
    return fa;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string s, t;
    if (!(cin >> s >> t)) return 0;

    int n = s.size();
    int m = t.size();

    // S_0: S[i] == '0'
    // S_1: S[i] == '1'
    // T_0_rev: T[m - 1 - j] == '0'
    // T_1_rev: T[m - 1 - j] == '1'
    vector<long long> s0(n), s1(n), t0_rev(m), t1_rev(m);
    for (int i = 0; i < n; ++i) {
        if (s[i] == '0') s0[i] = 1;
        else s1[i] = 1;
    }
    for (int j = 0; j < m; ++j) {
        if (t[m - 1 - j] == '0') t0_rev[j] = 1;
        else t1_rev[j] = 1;
    }

    // mismatch = (S[i+j] == 0 and T[j] == 1) + (S[i+j] == 1 and T[j] == 0)
    // conv1 = S_0 * T_1_rev
    // conv2 = S_1 * T_0_rev
    vector<long long> conv1 = multiply(s0, t1_rev);
    vector<long long> conv2 = multiply(s1, t0_rev);

    int ans = m;
    for (int i = 0; i <= n - m; ++i) {
        int idx = i + m - 1;
        int diff = conv1[idx] + conv2[idx];
        if (diff < ans) ans = diff;
    }

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
