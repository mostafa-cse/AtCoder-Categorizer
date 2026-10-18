# Problem Analysis: AtCoder-arc182_c — C. Sum of Number of Divisors of Product

**Problem ID**: `AtCoder-arc182_c`  
**Contest**: `arc182`  
**Rating / Difficulty**: 2408  
**URL**: https://atcoder.jp/contests/arc182/tasks/arc182_c  
**VJudge Tag**: `[problem:AtCoder-arc182_c]`  
**Category File**: [`../categories/math/prime_factor_subset_divisor_counting_matrix_expo.md`](../categories/math/prime_factor_subset_divisor_counting_matrix_expo.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Matrices`  
- **Topic (Skill)**: `Matrix Exponentiation`  

---

## 1. Problem Statement & Key Idea
Sum the number of positive divisors of the product across all sequences of length 1 to N with elements in [1, M] (M <= 16). Because only 6 primes exist <= 16, expand the divisor count over prime subsets and evaluate via 65x65 Matrix Exponentiation.

## 2. Core Observation & Invariant
The number of divisors is prod_{j=1}^6 (e_j + 1) = sum_{S subset {1..6}} prod_{j in S} e_j. Each element A_t contributes v_{p_j}(A_t) to a subset of required primes. This defines a 64-state submask transition matrix, extended to 65x65 to compute prefix sums over all lengths 1 to N.

## 3. Step-by-Step Algorithm
1. 1. Factorize all numbers x in 1 to M into prime exponent vectors over {2, 3, 5, 7, 11, 13}.
2. 2. Build the 64x64 transition matrix where T[mask | sub][mask] += prod_{j in sub} v_{p_j}(x).
3. 3. Augment to 65x65 matrix to accumulate powers over lengths 1 to N.
4. 4. Compute A^N in O(65^3 log N) and return the accumulated sum at index 64.

## 4. Complexity Analysis
- **Time Complexity**: `O(65^3 log N)`
- **Space Complexity**: `O(65^2)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

using ll = long long;
const ll MOD = 998244353;

const int primes[6] = {2, 3, 5, 7, 11, 13};

using Matrix = vector<vector<ll>>;

Matrix mat_mul(const Matrix& A, const Matrix& B, int sz) {
    Matrix C(sz, vector<ll>(sz, 0));
    for (int i = 0; i < sz; i++) {
        for (int k = 0; k < sz; k++) {
            if (A[i][k] == 0) continue;
            for (int j = 0; j < sz; j++) {
                C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD;
            }
        }
    }
    return C;
}

Matrix mat_pow(Matrix A, ll p, int sz) {
    Matrix res(sz, vector<ll>(sz, 0));
    for (int i = 0; i < sz; i++) res[i][i] = 1;
    while (p > 0) {
        if (p & 1) res = mat_mul(res, A, sz);
        A = mat_mul(A, A, sz);
        p >>= 1;
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    ll n;
    int m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<int>> vp(m + 1, vector<int>(6, 0));
    for (int x = 1; x <= m; x++) {
        int temp = x;
        for (int j = 0; j < 6; j++) {
            while (temp % primes[j] == 0) {
                vp[x][j]++;
                temp /= primes[j];
            }
        }
    }

    Matrix trans(64, vector<ll>(64, 0));
    for (int x = 1; x <= m; x++) {
        vector<ll> sub_weights(64, 1);
        for (int T = 1; T < 64; T++) {
            ll w = 1;
            for (int j = 0; j < 6; j++) {
                if ((T >> j) & 1) w = (w * vp[x][j]) % MOD;
            }
            sub_weights[T] = w;
        }

        for (int mask = 0; mask < 64; mask++) {
            int rem = 63 ^ mask;
            int T = rem;
            while (true) {
                if (sub_weights[T] > 0) {
                    trans[mask | T][mask] = (trans[mask | T][mask] + sub_weights[T]) % MOD;
                }
                if (T == 0) break;
                T = (T - 1) & rem;
            }
        }
    }

    Matrix A(65, vector<ll>(65, 0));
    for (int i = 0; i < 64; i++) {
        for (int j = 0; j < 64; j++) {
            A[i][j] = trans[i][j];
            A[64][j] = (A[64][j] + trans[i][j]) % MOD;
        }
    }
    A[64][64] = 1;

    Matrix powA = mat_pow(A, n, 65);
    ll ans = powA[64][0];
    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
