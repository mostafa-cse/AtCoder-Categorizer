# Problem Analysis: AtCoder-yahoo_procon2019_qual_e — E. Odd Subrectangles

**Problem ID**: `AtCoder-yahoo_procon2019_qual_e`  
**Contest**: `yahoo_procon2019_qual`  
**Rating / Difficulty**: 2585  
**URL**: https://atcoder.jp/contests/yahoo_procon2019_qual/tasks/yahoo_procon2019_qual_e  
**VJudge Tag**: `[problem:AtCoder-yahoo_procon2019_qual_e]`  
**Category File**: [`../categories/math/odd_subrectangles_f2_nullspace_gaussian_elimination.md`](../categories/math/odd_subrectangles_f2_nullspace_gaussian_elimination.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Linear Algebra`  
- **Topic (Skill)**: `Gaussian Elimination Modulo 2`  

---

## 1. Problem Statement & Key Idea
Count pairs of row subset $A$ and column subset $B$ whose intersection has an odd sum in a binary matrix $a_{ij}$.

## 2. Core Observation & Invariant
Represent row and column choices as binary vectors $\mathbf{x} \in \mathbb{F}_2^N, \mathbf{y} \in \mathbb{F}_2^M$. The sum is $\mathbf{x}^T A \mathbf{y} \pmod 2$. For any row combination with $\mathbf{x}^T A \ne \mathbf{0}$, exactly $2^{M - 1}$ choices of $\mathbf{y}$ yield an odd sum. The number of $\mathbf{x}$ with $\mathbf{x}^T A = \mathbf{0}$ is $2^{N - r}$, where $r = \text{rank}(A)$ over $\mathbb{F}_2$.

## 3. Step-by-Step Algorithm
1. 1. Read matrix $A$ into `std::bitset<300>` rows.
2. 2. Compute the rank $r$ of $A$ over $\mathbb{F}_2$ using Gaussian elimination.
3. 3. The count of non-zero row vectors is $2^N - 2^{N - r} \pmod{998244353}$.
4. 4. Multiply by $2^{M - 1} \pmod{998244353}$.

## 4. Complexity Analysis
- **Time Complexity**: `O(N M \min(N, M) / 64)`
- **Space Complexity**: `O(N M / 64)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <bitset>

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

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    if (!(cin >> N >> M)) return 0;

    vector<bitset<300>> A(N);
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            int val;
            cin >> val;
            if (val) A[i].set(j);
        }
    }

    int rank = 0;
    for (int col = 0; col < M && rank < N; ++col) {
        int pivot = -1;
        for (int r = rank; r < N; ++r) {
            if (A[r].test(col)) {
                pivot = r;
                break;
            }
        }
        if (pivot == -1) continue;
        swap(A[rank], A[pivot]);
        for (int r = 0; r < N; ++r) {
            if (r != rank && A[r].test(col)) {
                A[r] ^= A[rank];
            }
        }
        rank++;
    }

    long long pow2_N = power(2, N);
    long long pow2_N_minus_r = power(2, N - rank);
    long long nonzero_x = (pow2_N - pow2_N_minus_r + MOD) % MOD;
    long long pow2_M_minus_1 = power(2, M - 1);

    long long ans = (nonzero_x * pow2_M_minus_1) % MOD;
    cout << ans << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
