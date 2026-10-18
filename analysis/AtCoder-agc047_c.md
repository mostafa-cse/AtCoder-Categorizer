# Problem Analysis: AtCoder-agc047_c — C. Product Modulo

**Problem ID**: `AtCoder-agc047_c`  
**Contest**: `agc047`  
**Rating / Difficulty**: 2496  
**URL**: https://atcoder.jp/contests/agc047/tasks/agc047_c  
**VJudge Tag**: `[problem:AtCoder-agc047_c]`  
**Category File**: [`../categories/math/product_modulo_primitive_root_fft_convolution.md`](../categories/math/product_modulo_primitive_root_fft_convolution.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Convolution`  
- **Topic (Skill)**: `Number Theoretic Transform (NTT)`  

---

## 1. Problem Statement & Key Idea
Compute $\sum_{1 \le i < j \le N} (A_i A_j \pmod P)$ for prime $P = 200003$. $g = 2$ is a primitive root modulo $P$. Using discrete logarithm, map each non-zero $A_i$ to its exponent $e_i \in [0, P - 2]$ such that $g^{e_i} \equiv A_i \pmod P$. Then $A_i A_j \pmod P = g^{(e_i + e_j) \pmod{P - 1}} \pmod P$. The distribution of exponent sums is the polynomial multiplication $C(x) * C(x)$ where $C(x) = \sum cnt[e] x^e$. Fast Fourier Transform (FFT) convolves the frequency array in $O(P \log P)$ time.

## 2. Core Observation & Invariant
Zero elements contribute nothing to products and are ignored. Convolving $cnt$ with itself computes pairwise sums for all ordered pairs $(i, j)$. Subtracting self-products $A_i^2 \pmod P$ and dividing the total sum by 2 yields the exact unordered sum.

## 3. Step-by-Step Algorithm
1. 1. Precompute discrete logarithms with base $g = 2$ modulo $P = 200003$.
2. 2. Count occurrences of each discrete logarithm exponent in array $cnt$ of size $P - 1$.
3. 3. Perform complex FFT on $cnt$ padded to power of 2 ($2^{19}$).
4. 4. Square the transformed array and perform inverse FFT to obtain convolution counts $fa[S]$.
5. 5. For each exponent sum $S$, add $fa[S] \times (g^{S \pmod{P - 1}} \pmod P)$ to the total.
6. 6. Subtract self-products $A_i^2 \pmod P$ for all non-zero elements and divide by 2.

## 4. Complexity Analysis
- **Time Complexity**: `O(N + P \log P)`
- **Space Complexity**: `O(P)`

## 5. C++ Source Code
```cpp

#include <iostream>
#include <vector>
#include <cmath>
#include <complex>
#include <algorithm>

using namespace std;

typedef complex<double> cd;
const double PI = acos(-1);

void fft(vector<cd>& a, bool invert) {
    int n = a.size();
    for (int i = 1, j = 0; i < n; i++) {
        int bit = n >> 1;
        for (; j & bit; bit >>= 1) j ^= bit;
        j ^= bit;
        if (i < j) swap(a[i], a[j]);
    }

    for (int len = 2; len <= n; len <<= 1) {
        double ang = 2 * PI / len * (invert ? -1 : 1);
        cd wlen(cos(ang), sin(ang));
        for (int i = 0; i < n; i += len) {
            cd w(1);
            for (int j = 0; j < len / 2; j++) {
                cd u = a[i + j];
                cd v = a[i + j + len / 2] * w;
                a[i + j] = u + v;
                a[i + j + len / 2] = u - v;
                w *= wlen;
            }
        }
    }

    if (invert) {
        for (cd& x : a) x /= n;
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    const int P = 200003;
    const int G = 2;

    vector<int> exp_val(P - 1);
    vector<int> log_val(P, -1);
    long long cur = 1;
    for (int i = 0; i < P - 1; ++i) {
        exp_val[i] = cur;
        log_val[cur] = i;
        cur = (cur * G) % P;
    }

    vector<long long> cnt(P - 1, 0);
    vector<int> non_zero_a;
    for (int i = 0; i < n; ++i) {
        long long a;
        cin >> a;
        if (a % P != 0) {
            int a_mod = a % P;
            cnt[log_val[a_mod]]++;
            non_zero_a.push_back(a_mod);
        }
    }

    int sz = 1;
    while (sz < 2 * (P - 1)) sz <<= 1;

    vector<cd> fa(sz, 0);
    for (int i = 0; i < P - 1; ++i) {
        fa[i] = cnt[i];
    }

    fft(fa, false);
    for (int i = 0; i < sz; ++i) {
        fa[i] *= fa[i];
    }
    fft(fa, true);

    long long total_sum = 0;
    for (int i = 0; i < sz; ++i) {
        long long ways = (long long)round(fa[i].real());
        if (ways == 0) continue;
        int rem_exp = i % (P - 1);
        long long val = exp_val[rem_exp];
        total_sum += ways * val;
    }

    // Subtract self-products A_i * A_i
    for (int a_mod : non_zero_a) {
        long long self_prod = ((long long)a_mod * a_mod) % P;
        total_sum -= self_prod;
    }

    total_sum /= 2;
    cout << total_sum << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
