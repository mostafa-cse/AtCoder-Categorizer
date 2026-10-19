# Problem Analysis: AtCoder-abc213_h — H - Stroll

**Problem ID**: `AtCoder-abc213_h`  
**Contest**: `abc213`  
**Rating / Difficulty**: 2806  
**URL**: https://atcoder.jp/contests/abc213/tasks/abc213_h  
**VJudge Tag**: `[problem:AtCoder-abc213_h]`  
**Category File**: [`../categories/miscellaneous/stroll_online_convolution_cdq_divide_conquer.md`](../categories/miscellaneous/stroll_online_convolution_cdq_divide_conquer.md)  

- **Tag (Domain)**: `Miscellaneous`  
- **Subtopic**: `Techniques`  
- **Topic (Skill)**: `CDQ Divide and Conquer`  

---

## 1. Problem Statement & Key Idea
In a graph with time-dependent transition probabilities P(e, t), find the probability of a random stroll starting at vertex 1 returning to vertex 1 at time T, modulo 998244353.

## 2. Core Observation & Invariant
The DP state dp[v][t] = sum_{(u, v)} sum_{k=1}^t dp[u][t - k] * P(e, k) is a system of mutually recursive online convolutions. Using CDQ Divide and Conquer with NTT, the self-referential transitions can be computed offline in O(M * T log^2 T) time by splitting the time range [L, R] at mid, solving [L, mid], convolving [L, mid] with P(e) to push contributions into [mid + 1, R], and recursing on [mid + 1, R].

## 3. Step-by-Step Algorithm
1. 1. Set dp[1][0] = 1, all other dp[v][0] = 0.
2. 2. Implement cdq(L, R):
3.    a. If L == R, finalize dp[v][L] for all v.
4.    b. mid = (L + R) / 2; call cdq(L, mid).
5.    c. For each edge (u, v), perform polynomial multiplication (NTT) of dp[u][L..mid] and P(e, 1..R - L), accumulating into dp[v][mid + 1..R].
6.    d. Call cdq(mid + 1, R).
7. 3. Return dp[1][T] mod 998244353.

## 4. Complexity Analysis
- **Time Complexity**: `O(M * T log^2 T)`
- **Space Complexity**: `O((N + M) * T)`

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

void ntt(vector<long long>& a, bool invert) {
    int n = a.size();
    for (int i = 1, j = 0; i < n; i++) {
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
        for (int i = 0; i < n; i++) {
            a[i] = (a[i] * n_inv) % MOD;
        }
    }
}

struct Edge {
    int u, v;
    vector<long long> p;
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M, T;
    if (!(cin >> N >> M >> T)) return 0;

    vector<Edge> edges(M);
    for (int i = 0; i < M; ++i) {
        cin >> edges[i].u >> edges[i].v;
        edges[i].p.resize(T + 1, 0);
        for (int d = 1; d <= T; ++d) {
            cin >> edges[i].p[d];
        }
    }

    vector<vector<long long>> dp(N + 1, vector<long long>(T + 1, 0));
    dp[1][0] = 1;

    auto cdq = [&](auto& self, int L, int R) -> void {
        if (L == R) return;
        int mid = L + (R - L) / 2;

        self(self, L, mid);

        int len_A = mid - L + 1;
        int len_B = R - L; // max road length d that can contribute is R - L
        int sz = 1;
        while (sz < len_A + len_B) sz <<= 1;

        for (int e = 0; e < M; ++e) {
            int u = edges[e].u;
            int v = edges[e].v;

            // Contribution from v (L..mid) to u
            vector<long long> A(sz, 0), B(sz, 0);
            for (int i = 0; i < len_A; ++i) A[i] = dp[v][L + i];
            for (int i = 1; i <= len_B; ++i) B[i] = edges[e].p[i];

            ntt(A, false);
            ntt(B, false);

            vector<long long> C_u(sz);
            for (int i = 0; i < sz; ++i) C_u[i] = (A[i] * B[i]) % MOD;
            ntt(C_u, true);

            for (int t = mid + 1; t <= R; ++t) {
                int shift = t - L;
                if (shift < sz) {
                    dp[u][t] = (dp[u][t] + C_u[shift]) % MOD;
                }
            }

            // Contribution from u (L..mid) to v
            vector<long long> A_u(sz, 0);
            for (int i = 0; i < len_A; ++i) A_u[i] = dp[u][L + i];

            ntt(A_u, false);

            vector<long long> C_v(sz);
            for (int i = 0; i < sz; ++i) C_v[i] = (A_u[i] * B[i]) % MOD;
            ntt(C_v, true);

            for (int t = mid + 1; t <= R; ++t) {
                int shift = t - L;
                if (shift < sz) {
                    dp[v][t] = (dp[v][t] + C_v[shift]) % MOD;
                }
            }
        }

        self(self, mid + 1, R);
    };

    cdq(cdq, 0, T);

    cout << dp[1][T] << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
