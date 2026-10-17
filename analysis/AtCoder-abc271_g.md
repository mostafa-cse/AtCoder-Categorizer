# Problem Analysis: AtCoder-abc271_g — G. Access Counter

**Problem ID**: `AtCoder-abc271_g`  
**Contest**: `abc271`  
**Rating / Difficulty**: 2323  
**URL**: https://atcoder.jp/contests/abc271/tasks/abc271_g  
**VJudge Tag**: `[problem:AtCoder-abc271_g]`  
**Category File**: [`../categories/math/markov_access_counter_matrix_exponentiation.md`](../categories/math/markov_access_counter_matrix_exponentiation.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Matrices`  
- **Topic (Skill)**: `Matrix Exponentiation`  

---

## 1. Problem Statement & Key Idea
A process transitions along a circular 24-hour clock. At hour $h$, with probability $p_h$ an access occurs. If so, with probability $A_i$ user $i$ accesses it. Find the probability that the $N$-th access is made by each user, modulo 998244353.

## 2. Core Observation & Invariant
The sequence of accesses forms a time-homogeneous Markov chain on the 24 hours of the day, where transition probability $M_{u, v}$ accounts for the geometric probability of failing all 24 hours $0, 1, 2, \dots$ times before hitting hour $v$.

## 3. Step-by-Step Algorithm
1. Calculate the 24-hour cycle failure probability $Q = \prod_{i=0}^{23} (1 - p_i)$.
2. For each pair of hours $(u, v)$, compute $M_{u, v} = \frac{P_{\text{skip}}(u \to v) \cdot p_v}{1 - Q}$.
3. The initial distribution $v_0$ is given by row 23 of $M$.
4. Compute $v_{N-1} = v_0 \times M^{N-1}$ via $24 \times 24$ binary matrix exponentiation, and sum the probabilities over all hours $v$ assigned to Aoki.

## 4. Complexity Analysis
- **Time Complexity**: `O(24^3 \log N)`
- **Space Complexity**: `O(24^2)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

const int MOD = 998244353;

long long modInverse(long long n) {
    long long res = 1, p = MOD - 2;
    n %= MOD;
    while (p > 0) {
        if (p & 1) res = (res * n) % MOD;
        n = (n * n) % MOD;
        p >>= 1;
    }
    return res;
}

using Matrix = array<array<long long, 24>, 24>;

Matrix mat_mul(const Matrix& A, const Matrix& B) {
    Matrix C{};
    for (int i = 0; i < 24; ++i) {
        for (int k = 0; k < 24; ++k) {
            if (A[i][k] == 0) continue;
            for (int j = 0; j < 24; ++j) {
                C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD;
            }
        }
    }
    return C;
}

Matrix mat_pow(Matrix A, long long p) {
    Matrix res{};
    for (int i = 0; i < 24; ++i) res[i][i] = 1;
    while (p > 0) {
        if (p & 1) res = mat_mul(res, A);
        A = mat_mul(A, A);
        p >>= 1;
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n, x, y;
    if (!(cin >> n >> x >> y)) return 0;

    string c;
    cin >> c;

    long long inv100 = modInverse(100);
    array<long long, 24> p{}, q{};

    for (int i = 0; i < 24; ++i) {
        long long prob = (c[i] == 'T' ? x : y);
        p[i] = (prob * inv100) % MOD;
        q[i] = (1 - p[i] + MOD) % MOD;
    }

    long long Q = 1;
    for (int i = 0; i < 24; ++i) {
        Q = (Q * q[i]) % MOD;
    }

    long long inv_1_minus_Q = modInverse((1 - Q + MOD) % MOD);

    Matrix M{};
    for (int u = 0; u < 24; ++u) {
        long long cur_q = 1;
        for (int dist = 1; dist <= 24; ++dist) {
            int v = (u + dist) % 24;
            M[u][v] = (((cur_q * p[v]) % MOD) * inv_1_minus_Q) % MOD;
            cur_q = (cur_q * q[v]) % MOD;
        }
    }

    array<long long, 24> v0 = M[23];

    if (n == 1) {
        long long ans = 0;
        for (int v = 0; v < 24; ++v) {
            if (c[v] == 'A') ans = (ans + v0[v]) % MOD;
        }
        cout << ans << "\n";
        return 0;
    }

    Matrix MN = mat_pow(M, n - 1);
    array<long long, 24> v_final{};
    for (int j = 0; j < 24; ++j) {
        long long s = 0;
        for (int i = 0; i < 24; ++i) {
            s = (s + v0[i] * MN[i][j]) % MOD;
        }
        v_final[j] = s;
    }

    long long ans = 0;
    for (int v = 0; v < 24; ++v) {
        if (c[v] == 'A') ans = (ans + v_final[v]) % MOD;
    }
    cout << ans << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
