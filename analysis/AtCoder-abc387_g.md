# Problem Analysis: AtCoder-abc387_g — G - Prime Circuit

**Problem ID**: `AtCoder-abc387_g`  
**Contest**: `abc387`  
**Rating / Difficulty**: 2986  
**URL**: https://atcoder.jp/contests/abc387/tasks/abc387_g  
**VJudge Tag**: `[problem:AtCoder-abc387_g]`  
**Category File**: [`../categories/graph_theory/block_cut_tree_prime_circuit_cactus_cdq_ntt.md`](../categories/graph_theory/block_cut_tree_prime_circuit_cactus_cdq_ntt.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Graph Connectivity`  
- **Topic (Skill)**: `Articulation Points and Block Cut Tree`  

---

## 1. Problem Statement & Key Idea
Find the number of simple connected graphs on N labeled vertices such that every circuit has a prime number of edges, modulo 998244353.

## 2. Core Observation & Invariant
Any two circuits cannot share an edge or vertex because their symmetric difference would form a composite circuit (even length > 2). Hence the block-cut tree must be a tree of isolated vertices and prime-length simple cycles. By Extended Cayley's Theorem, the exponential generating function is G(x) = (1/N^2) \exp(N x + (N/2) \sum_{p >= 3, p \in P} x^p). Computing [x^N] \exp(P(x)) via CDQ divide-and-conquer NTT online convolution yields an exact O(N \log^2 N) solution.

## 3. Step-by-Step Algorithm
1. 1. Sieve primes up to N.
2. 2. Construct polynomial P where P_1 = N and P_p = N / 2 for odd primes p <= N. Set A_k = k P_k.
3. 3. Solve the differential relation E' = P' E using CDQ divide-and-conquer NTT: cdq(l, r) recursively computes E[l..mid], convolves E[l..mid] with A[1..r-l] using NTT, adds contributions to E[mid+1..r], and recurses.
4. 4. Compute answer = (E[N] / N^2) * N! mod 998244353.
5. 5. Output answer.

## 4. Complexity Analysis
- **Time Complexity**: `O(N \log^2 N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
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
    int need = a.size() + b.size() - 1;
    int n = 1;
    while (n < need) n <<= 1;
    vector<long long> fa(n, 0), fb(n, 0);
    for (size_t i = 0; i < a.size(); ++i) fa[i] = a[i];
    for (size_t i = 0; i < b.size(); ++i) fb[i] = b[i];
    ntt(fa, false);
    ntt(fb, false);
    for (int i = 0; i < n; i++) fa[i] = (fa[i] * fb[i]) % MOD;
    ntt(fa, true);
    fa.resize(need);
    return fa;
}

vector<long long> A;
vector<long long> inv;
vector<long long> E;

void cdq(int l, int r) {
    if (l == r) {
        if (l > 0) {
            E[l] = (E[l] * inv[l]) % MOD;
        }
        return;
    }
    int mid = l + (r - l) / 2;
    cdq(l, mid);

    vector<long long> U(mid - l + 1);
    for (int i = l; i <= mid; ++i) {
        U[i - l] = E[i];
    }
    int v_len = r - l;
    vector<long long> V(v_len);
    for (int i = 1; i <= v_len; ++i) {
        V[i - 1] = A[i];
    }

    vector<long long> W = multiply(U, V);
    for (int k = mid + 1; k <= r; ++k) {
        int idx = k - l - 1;
        if (idx < (int)W.size()) {
            E[k] = (E[k] + W[idx]) % MOD;
        }
    }

    cdq(mid + 1, r);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    if (!(cin >> N)) return 0;

    if (N == 1) {
        cout << 1 << "\n";
        return 0;
    }

    vector<bool> is_prime(N + 1, true);
    is_prime[0] = is_prime[1] = false;
    for (int p = 2; p * p <= N; ++p) {
        if (is_prime[p]) {
            for (int i = p * p; i <= N; i += p) {
                is_prime[i] = false;
            }
        }
    }

    long long inv2 = (MOD + 1) / 2;
    A.assign(N + 1, 0);
    A[1] = (1LL * 1 * N) % MOD;
    for (int p = 3; p <= N; ++p) {
        if (is_prime[p]) {
            long long Pp = (1LL * N * inv2) % MOD;
            A[p] = (1LL * p * Pp) % MOD;
        }
    }

    inv.assign(N + 1, 1);
    for (int i = 2; i <= N; ++i) {
        inv[i] = (1LL * (MOD - MOD / i) * inv[MOD % i]) % MOD;
    }

    E.assign(N + 1, 0);
    E[0] = 1;

    cdq(0, N);

    long long ans = (E[N] * power(N, MOD - 3)) % MOD;
    long long fact = 1;
    for (int i = 1; i <= N; ++i) {
        fact = (fact * i) % MOD;
    }
    ans = (ans * fact) % MOD;

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
