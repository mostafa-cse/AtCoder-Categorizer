# Problem Analysis: AtCoder-abc318_h — Ex - Count Strong Test Cases

**Problem ID**: `AtCoder-abc318_h`  
**Contest**: `abc318`  
**Rating / Difficulty**: 2785  
**URL**: https://atcoder.jp/contests/abc318/tasks/abc318_h  
**VJudge Tag**: `[problem:AtCoder-abc318_h]`  
**Category File**: [`../categories/miscellaneous/strong_components_functional_graph_cycles.md`](../categories/miscellaneous/strong_components_functional_graph_cycles.md)  

- **Tag (Domain)**: `Miscellaneous`  
- **Subtopic**: `General`  
- **Topic (Skill)**: `Functional Graphs`  

---

## 1. Problem Statement & Key Idea
Count the number of functional graphs on N vertices with specific strong component structure modulo 998244353.

## 2. Core Observation & Invariant
In any functional graph on N vertices, every connected component contains exactly one directed cycle, and all strongly connected components are precisely these cycles. Using exponential generating functions (EGF), the cycle structure of functional graphs is governed by exp(sum_{n >= 1} x^n / n^2). The problem reduces to computing the N-th coefficient [x^N] exp(sum_{n=1}^N x^n / n^2) and combining with (N!)^2 factors, which can be computed via CDQ divide-and-conquer NTT or polynomial exp in O(N log^2 N) time.

## 3. Step-by-Step Algorithm
1. 1. Define F(x) = sum_{n=1}^N x^n / n^2.
2. 2. Compute G(x) = exp(F(x)) mod x^(N+1) using CDQ divide-and-conquer NTT.
3. 3. Extract coefficient c_N = [x^N] G(x).
4. 4. Compute the final answer: (N!)^2 * (1 - 2 * c_N) + N! mod 998244353.
5. 5. Output the result.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log^2 N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

static const int MOD = 998244353;
static const int G = 3;

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

void ntt(vector<int>& a, bool inv = false) {
    int n = a.size();
    for (int i = 1, j = 0; i < n; i++) {
        int bit = n >> 1;
        for (; j & bit; bit >>= 1) j ^= bit;
        j ^= bit;
        if (i < j) swap(a[i], a[j]);
    }
    for (int len = 2; len <= n; len <<= 1) {
        long long wlen = power(G, (MOD - 1) / len);
        if (inv) wlen = modInverse(wlen);
        for (int i = 0; i < n; i += len) {
            long long w = 1;
            for (int j = 0; j < len / 2; j++) {
                int u = a[i + j];
                int v = (1LL * a[i + j + len / 2] * w) % MOD;
                a[i + j] = (u + v < MOD ? u + v : u + v - MOD);
                a[i + j + len / 2] = (u - v >= 0 ? u - v : u - v + MOD);
                w = (w * wlen) % MOD;
            }
        }
    }
    if (inv) {
        long long inv_n = modInverse(n);
        for (int i = 0; i < n; i++) {
            a[i] = (1LL * a[i] * inv_n) % MOD;
        }
    }
}

vector<int> multiply(const vector<int>& a, const vector<int>& b) {
    int sz = 1;
    while (sz < (int)(a.size() + b.size())) sz <<= 1;
    vector<int> fa(sz, 0), fb(sz, 0);
    for (size_t i = 0; i < a.size(); i++) fa[i] = a[i];
    for (size_t i = 0; i < b.size(); i++) fb[i] = b[i];
    ntt(fa);
    ntt(fb);
    for (int i = 0; i < sz; i++) {
        fa[i] = (1LL * fa[i] * fb[i]) % MOD;
    }
    ntt(fa, true);
    return fa;
}

vector<int> inv_table;
vector<int> e_poly;
vector<int> A_acc;

void cdq(int L, int R) {
    if (L == R) {
        if (L > 0) {
            e_poly[L] = (1LL * A_acc[L] * inv_table[L]) % MOD;
        }
        return;
    }
    int M = (L + R) / 2;
    cdq(L, M);

    vector<int> P(M - L + 1);
    for (int i = 0; i <= M - L; ++i) P[i] = e_poly[L + i];

    vector<int> Q(R - L);
    for (int i = 0; i < R - L; ++i) Q[i] = inv_table[i + 1];

    vector<int> conv = multiply(P, Q);

    for (int k = M + 1; k <= R; ++k) {
        A_acc[k] = (A_acc[k] + conv[k - L - 1]) % MOD;
    }

    cdq(M + 1, R);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    if (!(cin >> N)) return 0;

    inv_table.resize(N + 1);
    inv_table[1] = 1;
    for (int i = 2; i <= N; ++i) {
        inv_table[i] = (1LL * (MOD - MOD / i) * inv_table[MOD % i]) % MOD;
    }

    e_poly.assign(N + 1, 0);
    e_poly[0] = 1;
    A_acc.assign(N + 1, 0);

    cdq(0, N);

    long long fact_N = 1;
    for (int i = 1; i <= N; ++i) {
        fact_N = (fact_N * i) % MOD;
    }

    long long term1 = (fact_N * fact_N) % MOD;
    long long inside = (1 - 2LL * e_poly[N]) % MOD;
    if (inside < 0) inside += MOD;

    long long ans = (term1 * inside) % MOD;
    ans = (ans + fact_N) % MOD;

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
