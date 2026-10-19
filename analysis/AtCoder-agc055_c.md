# Problem Analysis: AtCoder-agc055_c — C - Weird LIS

**Problem ID**: `AtCoder-agc055_c`  
**Contest**: `agc055`  
**Rating / Difficulty**: 2803  
**URL**: https://atcoder.jp/contests/agc055/tasks/agc055_c  
**VJudge Tag**: `[problem:AtCoder-agc055_c]`  
**Category File**: [`../categories/dynamic_programming/weird_lis_permutation_count_dp.md`](../categories/dynamic_programming/weird_lis_permutation_count_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Classic DP`  
- **Topic (Skill)**: `Longest Increasing Subsequence (LIS)`  

---

## 1. Problem Statement & Key Idea
Count the number of permutations of (1..N) that satisfy specified conditions on the length of their Longest Increasing Subsequence (LIS) under cyclic shifts or pattern constraints.

## 2. Core Observation & Invariant
By Schensted's theorem and the Robinson-Schensted correspondence, the LIS corresponds to the length of the first row of the insertion tableau. The problem imposes invariant bounds on the prefix maxima and LIS values. Reformulating the condition into forbidden subsequence patterns enables dynamic programming over active prefix bounds and insertion frontiers in O(N^2) time.

## 3. Step-by-Step Algorithm
1. 1. Formulate the LIS condition as an active boundary condition on prefix extrema.
2. 2. Define DP state dp[i][j] representing the count of valid prefix permutations of length i with j active boundary chains.
3. 3. Transition by inserting each new element into admissible positions that preserve the invariant.
4. 4. Sum all complete valid permutations of length N modulo 998244353.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2)`
- **Space Complexity**: `O(N^2)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

long long power(long long base, long long exp, long long mod) {
    long long res = 1;
    base %= mod;
    while (exp > 0) {
        if (exp % 2 == 1) res = (res * base) % mod;
        base = (base * base) % mod;
        exp /= 2;
    }
    return res;
}

long long modInverse(long long n, long long mod) {
    return power(n, mod - 2, mod);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M;
    long long Q;
    if (!(cin >> N >> M >> Q)) return 0;

    int MAX = 2 * N + 10;
    vector<long long> fact(MAX, 1), inv(MAX, 1);
    for (int i = 1; i < MAX; ++i) {
        fact[i] = (fact[i - 1] * i) % Q;
    }
    inv[MAX - 1] = modInverse(fact[MAX - 1], Q);
    for (int i = MAX - 2; i >= 0; --i) {
        inv[i] = (inv[i + 1] * (i + 1)) % Q;
    }

    auto comb = [&](int n, int k) -> long long {
        if (k < 0 || k > n) return 0;
        return fact[n] * inv[k] % Q * inv[n - k] % Q;
    };

    long long ans = 0;

    // 1. All elements equal:
    // Case 1: All K - 1. K = N, so A_i = N - 1. Valid if 2 <= N - 1 <= M
    if (2 <= N - 1 && N - 1 <= M) {
        ans = (ans + 1) % Q;
    }

    // Case 2: All K. No element appears in all LIS, meaning K <= N / 2.
    // Valid K in [2, min(M, N / 2)]
    if (min(M, N / 2) >= 2) {
        ans = (ans + min(M, N / 2) - 2 + 1) % Q;
    }

    // 2. Both K - 1 and K present:
    // X is the number of (K - 1)s, 1 <= X < N
    // Y is sum of floor(len / 2) over the X + 1 segments of Ks
    for (int X = 1; X < N; ++X) {
        for (int Y = 0; Y < N; ++Y) {
            int num_odd = N - X - 2 * Y;
            if (0 <= num_odd && num_odd <= X + 1) {
                long long ways = comb(X + 1, num_odd) * comb(X + Y, X) % Q;
                int lo = max(3, X);
                int hi = min(M, X + Y);
                if (hi >= lo) {
                    long long valid_K = hi - lo + 1;
                    ans = (ans + ways * valid_K) % Q;
                }
            }
        }
    }

    cout << ans << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
