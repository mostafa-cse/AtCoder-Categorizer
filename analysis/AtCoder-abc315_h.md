# Problem Analysis: AtCoder-abc315_h — Ex - Typical Convolution Problem

**Problem ID**: `AtCoder-abc315_h`  
**Contest**: `abc315`  
**Rating / Difficulty**: 2807  
**URL**: https://atcoder.jp/contests/abc315/tasks/abc315_h  
**VJudge Tag**: `[problem:AtCoder-abc315_h]`  
**Category File**: [`../categories/math/quadratic_recurrence_online_convolution_ntt.md`](../categories/math/quadratic_recurrence_online_convolution_ntt.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Convolution`  
- **Topic (Skill)**: `Online FFT / NTT`  

---

## 1. Problem Statement & Key Idea
Given sequence A of length N, compute F_1..F_N where F_0 = 1 and F_n = A_n * sum_{i+j < n} F_i * F_j modulo 998244353.

## 2. Core Observation & Invariant
The sum sum_{i+j < n} F_i * F_j is the prefix sum of the self-convolution C = F * F. Since each F_n requires C_{n-1}, which depends on F_0..F_{n-1}, we can compute this recurrence using online relaxed convolution with NTT. Relaxed multiplication feeds each newly determined coefficient F_k into an ongoing convolution engine that maintains partial products using power-of-2 doubling, making C_{n-1} available just in time to determine F_n.

## 3. Step-by-Step Algorithm
1. 1. Initialize relaxed online convolution engine for C = F * F.
2. 2. Set F_0 = 1 and feed F_0 to the convolver.
3. 3. Maintain cumulative prefix sum S = C_0.
4. 4. For n = 1 to N:
5.    a. Read C_{n-1} from the convolver and update S = (S + C_{n-1}) mod MOD.
6.    b. Compute F_n = (A_n * S) mod MOD.
7.    c. Feed F_n into the online convolver.
8. 5. Output F_1..F_N.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log^2 N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <cassert>
#include <algorithm>

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

struct RelaxedConvolution {
    int N, q;
    vector<long long> a, b, c;
    vector<long long> f, g;
    vector<vector<long long>> as, bs;

    RelaxedConvolution(int _n) : N(_n), q(0) {
        a.resize(N + 1, 0);
        b.resize(N + 1, 0);
        c.resize(N + 1, 0);
    }

    long long get(long long x, long long y) {
        assert(q <= N);
        a[q] = x;
        b[q] = y;
        long long direct = (a[q] * b[0]) % MOD;
        if (q) direct = (direct + b[q] * a[0]) % MOD;
        c[q] = (c[q] + direct) % MOD;

        auto precalc = [&](int lg) {
            if ((int)as.size() <= lg) {
                as.resize(lg + 1);
                bs.resize(lg + 1);
            }
            if (!as[lg].empty()) return;
            int d = 1 << lg;
            vector<long long> s(a.begin(), a.begin() + d * 2);
            vector<long long> t(b.begin(), b.begin() + d * 2);
            ntt(s, false);
            ntt(t, false);
            as[lg] = s;
            bs[lg] = t;
        };

        q++;
        if (q > N) return c[q - 1];

        for (int d = 1, lg = 0; d <= q; d *= 2, lg++) {
            if (q % (2 * d) != d) continue;
            if (q == d) {
                f.assign(2 * d, 0);
                g.assign(2 * d, 0);
                for (int i = 0; i < d; i++) {
                    f[i] = a[i];
                    g[i] = b[i];
                }
                ntt(f, false);
                ntt(g, false);
                for (int i = 0; i < d * 2; i++) f[i] = (f[i] * g[i]) % MOD;
                ntt(f, true);
                for (int i = q; i < min(q + d, N + 1); i++) {
                    c[i] = (c[i] + f[d + i - q]) % MOD;
                }
            } else {
                precalc(lg);
                f.assign(2 * d, 0);
                g.assign(2 * d, 0);
                for (int i = 0; i < d; i++) {
                    f[i] = a[q - d + i];
                    g[i] = b[q - d + i];
                }
                ntt(f, false);
                ntt(g, false);
                const vector<long long>& s = as[lg];
                const vector<long long>& t = bs[lg];
                for (int i = 0; i < d * 2; i++) {
                    f[i] = (f[i] * t[i] + g[i] * s[i]) % MOD;
                }
                ntt(f, true);
                for (int i = q; i < min(q + d, N + 1); i++) {
                    c[i] = (c[i] + f[d + i - q]) % MOD;
                }
            }
        }
        return c[q - 1];
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;
    vector<long long> a(n + 1);
    for (int i = 1; i <= n; i++) cin >> a[i];

    RelaxedConvolution rc(n + 1);
    vector<long long> f_val(n + 1, 0);
    f_val[0] = 1;
    long long c0 = rc.get(1, 1);
    long long s = 0;

    for (int i = 1; i <= n; i++) {
        // C_{i-1} was returned at step i-1:
        // Wait, for i = 1, C_0 was returned by rc.get(1, 1) above!
        // S_i = sum_{k=0}^{i-1} C_k = S_{i-1} + C_{i-1}.
        if (i == 1) {
            s = (s + c0) % MOD;
        } else {
            // For i > 1, C_{i-1} was returned by the previous step's rc.get
            // Wait, previous step called rc.get(f_val[i-1], f_val[i-1]), which returned c[i-1]!
            // So s is already updated if we update it after rc.get!
        }
        f_val[i] = (a[i] * s) % MOD;
        long long ci = rc.get(f_val[i], f_val[i]);
        s = (s + ci) % MOD;
    }

    for (int i = 1; i <= n; i++) {
        cout << f_val[i] << (i == n ? "" : " ");
    }
    cout << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
