# Problem Analysis: AtCoder-arc176_d — D. Swap Permutation

**Problem ID**: `AtCoder-arc176_d`  
**Contest**: `arc176`  
**Rating / Difficulty**: 2572  
**URL**: https://atcoder.jp/contests/arc176/tasks/arc176_d  
**VJudge Tag**: `[problem:AtCoder-arc176_d]`  
**Category File**: [`../categories/math/swap_permutation_markov_matrix_exponentiation.md`](../categories/math/swap_permutation_markov_matrix_exponentiation.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Probabilities and Expected Values`  
- **Topic (Skill)**: `Probabilities and Expected Values`  

---

## 1. Problem Statement & Key Idea
Compute the sum of $\sum_{i=1}^{N-1} |P'_i - P'_{i+1}|$ after $M$ uniform random transpositions on permutation $P$.

## 2. Core Observation & Invariant
By symmetry of random transpositions on the complete graph $K_N$, the joint distribution of original elements $(A, B)$ ending up at any adjacent positions $(i, i+1)$ partitions into 3 symmetric states: Type 1 (both original $P_i, P_{i+1}$), Type 2 (one original, one outside), and Type 3 (both outside). The probabilities satisfy a 3-state Markov chain solved via matrix exponentiation.

## 3. Step-by-Step Algorithm
1. 1. If $N=2$, answer is 1.
2. 2. For $N \ge 3$, set up the $3 \times 3$ transition matrix for the pair position Markov chain under random transpositions.
3. 3. Compute $(M_{\text{trans}})^M$ via binary matrix exponentiation to obtain per-pair probabilities $c_1, c_2, c_3$.
4. 4. Compute $S_{\text{all}} = \sum_{a < b} (b - a)$, $\sum D(i, i+1)$, and endpoint potentials $R(P_1), R(P_N)$.
5. 5. Combine components into the final answer modulo 998244353.

## 4. Complexity Analysis
- **Time Complexity**: `O(N + \log M)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <cmath>

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

vector<vector<long long>> mat_mul(const vector<vector<long long>>& A, const vector<vector<long long>>& B) {
    int n = A.size();
    vector<vector<long long>> C(n, vector<long long>(n, 0));
    for (int i = 0; i < n; ++i) {
        for (int k = 0; k < n; ++k) {
            if (A[i][k] == 0) continue;
            for (int j = 0; j < n; ++j) {
                C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD;
            }
        }
    }
    return C;
}

vector<vector<long long>> mat_pow(vector<vector<long long>> A, long long p) {
    int n = A.size();
    vector<vector<long long>> res(n, vector<long long>(n, 0));
    for (int i = 0; i < n; ++i) res[i][i] = 1;
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

    long long N, M;
    if (!(cin >> N >> M)) return 0;
    vector<long long> P(N);
    for (int i = 0; i < N; ++i) cin >> P[i];

    if (N == 2) {
        cout << 1 << "\n";
        return 0;
    }

    long long T = (N * (N - 1) / 2) % MOD;
    long long c1 = 0, c2 = 0, c3 = 0;

    if (N == 3) {
        vector<vector<long long>> mat = {
            {1, 2},
            {1, 2}
        };
        auto res_mat = mat_pow(mat, M);
        long long w1 = res_mat[0][0];
        long long w2 = res_mat[0][1];
        c1 = w1;
        c2 = (w2 * modInverse(2 * (N - 2))) % MOD;
        c3 = 0;
    } else {
        long long s11 = (1 + (N - 2) * (N - 3) / 2) % MOD;
        long long s12 = (2 * (N - 2)) % MOD;
        long long s13 = 0;

        long long s21 = 1;
        long long s22 = (T - 1 - (N - 3) + MOD) % MOD;
        long long s23 = (N - 3) % MOD;

        long long s31 = 0;
        long long s32 = 4;
        long long s33 = (T - 4 + MOD) % MOD;

        vector<vector<long long>> mat = {
            {s11, s12, s13},
            {s21, s22, s23},
            {s31, s32, s33}
        };
        auto res_mat = mat_pow(mat, M);
        long long w1 = res_mat[0][0];
        long long w2 = res_mat[0][1];
        long long w3 = res_mat[0][2];
        c1 = w1;
        c2 = (w2 * modInverse(2 * (N - 2))) % MOD;
        long long pairs3 = ((N - 2) * (N - 3) / 2) % MOD;
        c3 = (w3 * modInverse(pairs3)) % MOD;
    }

    long long S_all = (N * (N + 1) % MOD * (N - 1) % MOD * modInverse(6)) % MOD;

    long long sum_D = 0;
    for (int i = 0; i < N - 1; ++i) {
        sum_D = (sum_D + abs(P[i] - P[i + 1])) % MOD;
    }

    auto get_R = [&](long long val) -> long long {
        long long left = (val - 1) * val / 2;
        long long right = (N - val) * (N - val + 1) / 2;
        return (left + right) % MOD;
    };

    long long R1 = get_R(P[0]);
    long long RN = get_R(P[N - 1]);
    long long sum_R = (4 * S_all - R1 - RN + 2 * MOD) % MOD;

    long long term1 = sum_D;
    long long term2 = (sum_R - 2 * sum_D + 2 * MOD) % MOD;
    long long term3 = ((N - 1) * S_all % MOD - sum_R + sum_D + 2 * MOD) % MOD;

    long long ans = (c1 * term1 % MOD + c2 * term2 % MOD + c3 * term3 % MOD) % MOD;
    cout << ans << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
