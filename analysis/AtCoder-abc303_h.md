# Problem Analysis: AtCoder-abc303_h — Ex. Constrained Tree Degree

**Problem ID**: `AtCoder-abc303_h`  
**Contest**: `abc303`  
**Rating / Difficulty**: 2501  
**URL**: https://atcoder.jp/contests/abc303/tasks/abc303_h  
**VJudge Tag**: `[problem:AtCoder-abc303_h]`  
**Category File**: [`../categories/graph_theory/constrained_tree_degree_prufer_code_poly_exp.md`](../categories/graph_theory/constrained_tree_degree_prufer_code_poly_exp.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Graph Counting`  
- **Topic (Skill)**: `Prufer Code`  

---

## 1. Problem Statement & Key Idea
Count labeled trees on $N$ vertices where every vertex degree belongs to subset $S$. By Cayley's tree formula and Prüfer sequences, the degrees satisfy $\sum_{i=1}^N (d_i - 1) = N - 2$, and the number of trees with a fixed degree sequence is $(N - 2)! / \prod (d_i - 1)!$. Setting $k_i = d_i - 1$, this equals $(N - 2)! [x^{N-2}] F(x)^N$ where $F(x) = \sum_{d \in S} \frac{x^{d-1}}{(d-1)!}$. Since every tree with $N \ge 2$ has leaves ($1 \in S$), $F(0) = 1$. The power $F(x)^N$ is computed using polynomial $\ln$ and $\exp$ via NTT in $O(N \log N)$ time.

## 2. Core Observation & Invariant
If $1 \notin S$, no tree can exist and the answer is 0. If $1 \in S$, $F(0) = 1 \ne 0$, so $F(x)^N = \exp(N \ln F(x))$. Polynomial inversion, differentiation, integration, and Newton's method for $\exp$ compute the required coefficient in $O(N \log N)$.

## 3. Step-by-Step Algorithm
1. 1. If $1 \notin S$, output 0. If $N = 2$, output 1.
2. 2. Construct polynomial $F(x) = \sum_{d \in S, d - 1 \le N - 2} \frac{x^{d-1}}{(d-1)!}$.
3. 3. Compute $G(x) = \ln(F(x)) \pmod{x^{N-1}}$ via $G'(x) = F'(x) F(x)^{-1}$ with NTT polynomial inversion.
4. 4. Multiply $G(x)$ by $N \pmod{998244353}$.
5. 5. Compute $H(x) = \exp(N G(x)) \pmod{x^{N-1}}$ using Newton's method doubling.
6. 6. Output $(H[N - 2] \times (N - 2)!) \pmod{998244353}$.

## 4. Complexity Analysis
- **Time Complexity**: `O(N \log N)`
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
        for (long long& x : a) x = (x * n_inv) % MOD;
    }
}

vector<long long> multiply(const vector<long long>& a, const vector<long long>& b, int max_len) {
    int need = a.size() + b.size() - 1;
    int n = 1;
    while (n < need) n <<= 1;
    vector<long long> fa(n, 0), fb(n, 0);
    for (size_t i = 0; i < a.size(); ++i) fa[i] = a[i];
    for (size_t i = 0; i < b.size(); ++i) fb[i] = b[i];
    ntt(fa, false);
    ntt(fb, false);
    for (int i = 0; i < n; ++i) fa[i] = (fa[i] * fb[i]) % MOD;
    ntt(fa, true);
    if ((int)fa.size() > max_len) fa.resize(max_len);
    return fa;
}

vector<long long> poly_inv(const vector<long long>& a, int deg) {
    vector<long long> res = {modInverse(a[0])};
    int len = 1;
    while (len < deg) {
        len <<= 1;
        vector<long long> cur_a(min((int)a.size(), len));
        for (size_t i = 0; i < cur_a.size(); ++i) cur_a[i] = a[i];
        vector<long long> prod = multiply(cur_a, res, len);
        vector<long long> term(len, 0);
        for (int i = 0; i < len; ++i) {
            long long p = (i < (int)prod.size() ? prod[i] : 0);
            long long val = ((i == 0 ? 2 : 0) - p) % MOD;
            term[i] = (val + MOD) % MOD;
        }
        res = multiply(res, term, len);
    }
    res.resize(deg);
    return res;
}

vector<long long> poly_deriv(const vector<long long>& a) {
    if (a.size() <= 1) return {0};
    vector<long long> res(a.size() - 1);
    for (size_t i = 1; i < a.size(); ++i) {
        res[i - 1] = (i * a[i]) % MOD;
    }
    return res;
}

vector<long long> poly_integ(const vector<long long>& a) {
    vector<long long> res(a.size() + 1, 0);
    for (size_t i = 0; i < a.size(); ++i) {
        res[i + 1] = (a[i] * modInverse(i + 1)) % MOD;
    }
    return res;
}

vector<long long> poly_ln(const vector<long long>& a, int deg) {
    vector<long long> da = poly_deriv(a);
    vector<long long> ia = poly_inv(a, deg);
    vector<long long> prod = multiply(da, ia, deg - 1);
    vector<long long> res = poly_integ(prod);
    res.resize(deg);
    return res;
}

vector<long long> poly_exp(const vector<long long>& a, int deg) {
    vector<long long> res = {1};
    int len = 1;
    while (len < deg) {
        len <<= 1;
        vector<long long> ln_res = poly_ln(res, len);
        vector<long long> term(len, 0);
        for (int i = 0; i < len; ++i) {
            long long ai = (i < (int)a.size() ? a[i] : 0);
            long long li = (i < (int)ln_res.size() ? ln_res[i] : 0);
            long long val = (ai - li) % MOD;
            if (i == 0) val = (val + 1) % MOD;
            term[i] = (val + MOD) % MOD;
        }
        res = multiply(res, term, len);
    }
    res.resize(deg);
    return res;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    bool has_one = false;
    vector<int> s(k);
    for (int i = 0; i < k; ++i) {
        cin >> s[i];
        if (s[i] == 1) has_one = true;
    }

    if (!has_one) {
        cout << 0 << "\n";
        return 0;
    }

    int deg = n - 2;
    if (deg == 0) {
        cout << 1 << "\n";
        return 0;
    }

    vector<long long> fact(n + 1, 1), inv(n + 1, 1);
    for (int i = 1; i <= n; ++i) fact[i] = (fact[i - 1] * i) % MOD;
    inv[n] = modInverse(fact[n]);
    for (int i = n - 1; i >= 0; --i) inv[i] = (inv[i + 1] * (i + 1)) % MOD;

    vector<long long> F(deg + 1, 0);
    for (int d : s) {
        if (d - 1 <= deg) {
            F[d - 1] = inv[d - 1];
        }
    }

    vector<long long> ln_F = poly_ln(F, deg + 1);
    for (size_t i = 0; i < ln_F.size(); ++i) {
        ln_F[i] = (ln_F[i] * n) % MOD;
    }

    vector<long long> H = poly_exp(ln_F, deg + 1);
    long long ans = (H[deg] * fact[deg]) % MOD;
    cout << ans << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
