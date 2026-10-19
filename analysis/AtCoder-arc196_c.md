# Problem Analysis: AtCoder-arc196_c — C. Strongly Connected

**Problem ID**: `AtCoder-arc196_c`  
**Contest**: `arc196`  
**Rating / Difficulty**: 2917  
**URL**: https://atcoder.jp/contests/arc196/tasks/arc196_c  
**VJudge Tag**: `[problem:AtCoder-arc196_c]`  
**Category File**: [`../categories/math/bipartite_pairing_cut_elimination_cdq_ntt.md`](../categories/math/bipartite_pairing_cut_elimination_cdq_ntt.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Convolution`  
- **Topic (Skill)**: `Number Theoretic Transform (NTT)`  

---

## 1. Problem Statement & Key Idea
In a bipartite graph with directed edges defined by pairing conditions, count configurations that result in a strongly connected graph modulo 998244353.

## 2. Core Observation & Invariant
A directed graph is not strongly connected iff there exists a directed cut with no outgoing edges. Enumerating strongly connected components translates to subtracting disconnected configurations via a recurrence: total configurations g_n = sum_{k=1}^n f_k * c_{n, k} * g_{n-k}, where f_k is the number of strongly connected configurations of size k. This recurrence has convolution form, solvable in O(N log^2 N) time via divide-and-conquer NTT (CDQ NTT).

## 3. Step-by-Step Algorithm
1. 1. Formulate the cut conditions and recurrence for strongly connected counts f_n.
2. 2. Express the recurrence as a polynomial convolution over prefix sizes.
3. 3. Implement divide-and-conquer NTT (cdq(l, r)):
4.    - Recursively solve cdq(l, mid).
5.    - Convolve f[l ... mid] with transition polynomial using NTT.
6.    - Add contribution to g[mid+1 ... r].
7.    - Recursively solve cdq(mid+1, r).
8. 4. Return f_N modulo 998244353.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log^2 N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

static const int MOD = 998244353;

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

const int MAXM = 400005;
long long fact[MAXM], invfact[MAXM];
int W[MAXM], B[MAXM];
long long dp[MAXM];
long long contrib[MAXM];

void cdq(int l, int r) {
    if (l == r) {
        if (l > 0) {
            if (W[l] >= B[l]) {
                long long cur = (contrib[l] % MOD + MOD) % MOD;
                dp[l] = (cur * invfact[W[l] - B[l]]) % MOD;
            } else {
                dp[l] = 0;
            }
        }
        return;
    }

    int mid = (l + r) / 2;
    cdq(l, mid);

    // Compute contributions from [l, mid] to [mid + 1, r]
    int min_b = B[l], max_b = B[mid];
    for (int j = l; j <= mid; ++j) {
        min_b = min(min_b, B[j]);
        max_b = max(max_b, B[j]);
    }

    int min_w = W[mid + 1], max_w = W[r];
    for (int i = mid + 1; i <= r; ++i) {
        min_w = min(min_w, W[i]);
        max_w = max(max_w, W[i]);
    }

    if (max_w >= min_b) {
        int max_s = max_w - min_b;
        int len_p = max_b - min_b + 1;
        int len_q = max_s + 1;

        int sz = 1;
        while (sz < len_p + len_q) sz <<= 1;

        vector<long long> P(sz, 0), Q(sz, 0);
        for (int j = l; j <= mid; ++j) {
            if (dp[j] != 0) {
                int idx = B[j] - min_b;
                long long val = (MOD - dp[j]) % MOD;
                P[idx] = (P[idx] + val) % MOD;
            }
        }

        for (int s = 0; s <= max_s; ++s) {
            Q[s] = fact[s];
        }

        ntt(P, false);
        ntt(Q, false);
        for (int i = 0; i < sz; ++i) {
            P[i] = (P[i] * Q[i]) % MOD;
        }
        ntt(P, true);

        for (int i = mid + 1; i <= r; ++i) {
            int req_s = W[i] - min_b;
            if (req_s >= 0 && req_s < sz) {
                contrib[i] = (contrib[i] + P[req_s]) % MOD;
            }
        }
    }

    cdq(mid + 1, r);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    if (!(cin >> N)) return 0;
    string S;
    cin >> S;

    int M = 2 * N;
    fact[0] = 1;
    invfact[0] = 1;
    for (int i = 1; i <= M; ++i) {
        fact[i] = (fact[i - 1] * i) % MOD;
    }
    invfact[M] = modInverse(fact[M]);
    for (int i = M - 1; i >= 1; --i) {
        invfact[i] = (invfact[i + 1] * (i + 1)) % MOD;
    }

    W[0] = B[0] = 0;
    for (int i = 1; i <= M; ++i) {
        W[i] = W[i - 1] + (S[i - 1] == 'W');
        B[i] = B[i - 1] + (S[i - 1] == 'B');
    }

    dp[0] = (MOD - 1); // -1 modulo MOD

    cdq(0, M);

    long long ans = (dp[M] % MOD + MOD) % MOD;
    cout << ans << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
