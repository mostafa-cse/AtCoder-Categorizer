# Problem Analysis: AtCoder-abc256_g — G. Black and White Stones

**Problem ID**: `AtCoder-abc256_g`  
**Contest**: `abc256`  
**Rating / Difficulty**: 2250  
**URL**: https://atcoder.jp/contests/abc256/tasks/abc256_g  
**VJudge Tag**: `[problem:AtCoder-abc256_g]`  
**Category File**: [`../categories/math/matrix_exponentiation_circular_cycle_trace.md`](../categories/math/matrix_exponentiation_circular_cycle_trace.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Matrices`  
- **Topic (Skill)**: `Matrix Exponentiation`  

---

## 1. Problem Statement & Key Idea
We are given a cycle of $N$ edges and $N$ vertices. On each edge $i$, we choose white or black stones such that the total number of black stones on the edge is between $0$ and $D+1$, including the two stones placed at its incident vertices. Each edge has $D-1$ inner stones, and we want to count the number of valid stone assignments modulo 998244353.

## 2. Core Observation & Invariant
Notice that if we fix the total number of black stones on every edge to be some constant $k \in [0, D+1]$, then for an edge $(u, v)$ where vertex $u$ has stone color $x \in \{0, 1\}$ and vertex $v$ has stone color $y \in \{0, 1\}$, the remaining $k - x - y$ black stones must be placed among the $D-1$ inner stones on that edge. The number of ways to choose them is $\binom{D-1}{k - x - y}$.
This defines a $2 \times 2$ transition matrix $M_k$ between vertex stone colors. Because the vertices form an $N$-cycle, the number of valid assignments for a fixed $k$ is precisely the trace $\text{Tr}(M_k^N) = (M_k^N)_{0,0} + (M_k^N)_{1,1}$. Summing this over all $k \in [0, D+1]$ gives the total answer.

## 3. Step-by-Step Algorithm
1. Precompute factorials and modular inverse factorials up to $D$.
2. Iterate $k$ from $0$ to $D + 1$.
3. Construct the $2 \times 2$ transition matrix $M_k$ with entries $M_{0,0} = \binom{D-1}{k}, M_{0,1} = M_{1,0} = \binom{D-1}{k-1}, M_{1,1} = \binom{D-1}{k-2}$.
4. Compute $M_k^N$ via binary exponentiation in $O(\log N)$.
5. Add the trace $(M_k^N)_{0,0} + (M_k^N)_{1,1}$ modulo 998244353 to the total sum.
6. Output the total sum.

## 4. Complexity Analysis
- **Time Complexity**: `O(D \log N)`
- **Space Complexity**: `O(D)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 998244353;
const int MAX = 20005;

long long fact[MAX], inv[MAX];

long long mod_pow(long long a, long long b) {
    long long res = 1;
    a %= MOD;
    while (b > 0) {
        if (b & 1) res = (res * a) % MOD;
        a = (a * a) % MOD;
        b >>= 1;
    }
    return res;
}

void precompute() {
    fact[0] = 1;
    for (int i = 1; i < MAX; ++i) fact[i] = (fact[i - 1] * i) % MOD;
    inv[MAX - 1] = mod_pow(fact[MAX - 1], MOD - 2);
    for (int i = MAX - 2; i >= 0; --i) inv[i] = (inv[i + 1] * (i + 1)) % MOD;
}

long long nCr(int n, int r) {
    if (r < 0 || r > n) return 0;
    return fact[n] * inv[r] % MOD * inv[n - r] % MOD;
}

struct Mat2 {
    long long a[2][2];
    Mat2() {
        a[0][0] = a[0][1] = a[1][0] = a[1][1] = 0;
    }
    static Mat2 identity() {
        Mat2 res;
        res.a[0][0] = res.a[1][1] = 1;
        return res;
    }
};

Mat2 operator*(const Mat2& X, const Mat2& Y) {
    Mat2 Z;
    for (int i = 0; i < 2; ++i) {
        for (int k = 0; k < 2; ++k) {
            for (int j = 0; j < 2; ++j) {
                Z.a[i][j] = (Z.a[i][j] + X.a[i][k] * Y.a[k][j]) % MOD;
            }
        }
    }
    return Z;
}

Mat2 mat_pow(Mat2 base, long long exp) {
    Mat2 res = Mat2::identity();
    while (exp > 0) {
        if (exp & 1) res = res * base;
        base = base * base;
        exp >>= 1;
    }
    return res;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    precompute();

    long long N;
    int D;
    if (!(cin >> N >> D)) return 0;

    long long total_ways = 0;

    for (int k = 0; k <= D + 1; ++k) {
        Mat2 M;
        M.a[0][0] = nCr(D - 1, k);
        M.a[0][1] = nCr(D - 1, k - 1);
        M.a[1][0] = nCr(D - 1, k - 1);
        M.a[1][1] = nCr(D - 1, k - 2);

        Mat2 MN = mat_pow(M, N);
        long long tr = (MN.a[0][0] + MN.a[1][1]) % MOD;
        total_ways = (total_ways + tr) % MOD;
    }

    cout << total_ways << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
