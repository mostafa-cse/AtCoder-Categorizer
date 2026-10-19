# Problem Analysis: AtCoder-abc307_h — H - Marquee

**Problem ID**: `AtCoder-abc307_h`  
**Contest**: `abc307`  
**Rating / Difficulty**: 2750  
**URL**: https://atcoder.jp/contests/abc307/tasks/abc307_h  
**VJudge Tag**: `[problem:AtCoder-abc307_h]`  
**Category File**: [`../categories/strings/marquee_wildcard_string_matching_fft.md`](../categories/strings/marquee_wildcard_string_matching_fft.md)  

- **Tag (Domain)**: `Strings`  
- **Subtopic**: `String Matching`  
- **Topic (Skill)**: `String Matching with FFT ft Wildcard Matching`  

---

## 1. Problem Statement & Key Idea
Given a pattern P of length W (consisting of uppercase letters and wildcard '_') and a string S of length L, consider repeating S infinitely. We want to find the number of starting positions in a single period where P matches S (wildcard '_' matches any letter).

## 2. Core Observation & Invariant
String matching with wildcards can be evaluated algebraically. Assign each letter A-Z a non-zero integer v(c) in 1..26, and map wildcard '_' to 0. A match occurs at offset k if and only if sum_{i=0}^{W-1} v(P[i]) * (v(P[i]) - v(T[k+i]))^2 = 0. Expanding the square yields three terms: sum v(P[i])^3 - 2 sum v(P[i])^2 v(T[k+i]) + sum v(P[i]) v(T[k+i])^2. Each term is a cross-correlation, which can be computed via NTT polynomial multiplication modulo 998244353 and a second NTT modulo 1004535809 to avoid false positives.

## 3. Step-by-Step Algorithm
1. 1. Extend S cyclically to length L + W - 1 to form text T.
2. 2. Assign non-zero integer values to characters in S and P, with '_' mapped to 0.
3. 3. Reverse pattern P.
4. 4. Compute polynomial convolutions P^2 * T and P * T^2 using NTT.
5. 5. For each shift k in 0..L-1, evaluate the mismatch function.
6. 6. Count the number of shifts where the mismatch sum evaluates to 0.

## 4. Complexity Analysis
- **Time Complexity**: `O((L + W) log(L + W))`
- **Space Complexity**: `O(L + W)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

long long power(long long base, long long exp, long long mod) {
    long long res = 1;
    base %= mod;
    while (exp > 0) {
        if (exp % 2 == 1) res = (res * base) % mod;
        base = (base * base) % mod;
        exp /= 2;
    }
    return res;
}

long long modInverse(long long n, long long mod) {
    return power(n, mod - 2, mod);
}

template<int MOD, int G>
struct NTT {
    static void ntt(vector<long long>& a, bool inv = false) {
        int n = a.size();
        for (int i = 1, j = 0; i < n; i++) {
            int bit = n >> 1;
            for (; j & bit; bit >>= 1) j ^= bit;
            j ^= bit;
            if (i < j) swap(a[i], a[j]);
        }
        for (int len = 2; len <= n; len <<= 1) {
            long long wlen = power(G, (MOD - 1) / len, MOD);
            if (inv) wlen = modInverse(wlen, MOD);
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
        if (inv) {
            long long inv_n = modInverse(n, MOD);
            for (int i = 0; i < n; i++) {
                a[i] = (a[i] * inv_n) % MOD;
            }
        }
    }

    static vector<long long> multiply(const vector<long long>& a, const vector<long long>& b) {
        int sz = 1;
        while (sz < (int)(a.size() + b.size())) sz <<= 1;
        vector<long long> fa(sz, 0), fb(sz, 0);
        for (size_t i = 0; i < a.size(); i++) fa[i] = (a[i] % MOD + MOD) % MOD;
        for (size_t i = 0; i < b.size(); i++) fb[i] = (b[i] % MOD + MOD) % MOD;
        ntt(fa, false);
        ntt(fb, false);
        for (int i = 0; i < sz; i++) fa[i] = (fa[i] * fb[i]) % MOD;
        ntt(fa, true);
        return fa;
    }
};

using NTT1 = NTT<998244353, 3>;
using NTT2 = NTT<1004535809, 3>;

int charVal(char c) {
    if (c == '_') return 0;
    if (c == '.') return 1;
    if (c >= 'a' && c <= 'z') return (c - 'a' + 2);
    if (c >= 'A' && c <= 'Z') return (c - 'A' + 28);
    return 0;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int L, W;
    if (!(cin >> L >> W)) return 0;

    string S, P;
    cin >> S >> P;

    int M = L + W - 1;
    string T = S + string(W - 1, '.');
    string T2 = T + T;

    int T_len = (int)T2.size();

    // Constant C: sum_{i=0}^{W-1} v(P[i])^3
    long long C1 = 0, C2 = 0;
    for (int i = 0; i < W; i++) {
        long long v = charVal(P[i]);
        long long v3 = v * v * v;
        C1 = (C1 + v3) % 998244353;
        C2 = (C2 + v3) % 1004535809;
    }

    // Poly A: v(P[W - 1 - i])^2
    // Poly B: v(T2[j])
    vector<long long> A(W), B(T_len);
    for (int i = 0; i < W; i++) {
        long long v = charVal(P[W - 1 - i]);
        A[i] = v * v;
    }
    for (int j = 0; j < T_len; j++) {
        B[j] = charVal(T2[j]);
    }

    vector<long long> conv_AB_1 = NTT1::multiply(A, B);
    vector<long long> conv_AB_2 = NTT2::multiply(A, B);

    // Poly D: v(P[W - 1 - i])
    // Poly E: (v(T2[j]))^2
    vector<long long> D(W), E(T_len);
    for (int i = 0; i < W; i++) {
        D[i] = charVal(P[W - 1 - i]);
    }
    for (int j = 0; j < T_len; j++) {
        long long v = charVal(T2[j]);
        E[j] = v * v;
    }

    vector<long long> conv_DE_1 = NTT1::multiply(D, E);
    vector<long long> conv_DE_2 = NTT2::multiply(D, E);

    int ans = 0;
    for (int k = 0; k < M; k++) {
        int idx = k + W - 1;
        long long term1 = (C1 - 2 * conv_AB_1[idx] + conv_DE_1[idx]) % 998244353;
        if (term1 < 0) term1 += 998244353;

        long long term2 = (C2 - 2 * conv_AB_2[idx] + conv_DE_2[idx]) % 1004535809;
        if (term2 < 0) term2 += 1004535809;

        if (term1 == 0 && term2 == 0) {
            ans++;
        }
    }

    cout << ans << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
