# Problem Analysis: AtCoder-abc172_e — NEQ

**Problem ID**: `AtCoder-abc172_e`  
**Contest**: `abc172`  
**Rating / Difficulty**: 1880  
**URL**: https://atcoder.jp/contests/abc172/tasks/abc172_e  
**VJudge Tag**: `[problem:AtCoder-abc172_e]`  
**Category File**: [`../categories/combinatorics/pie_sequence_derangements_distinct_alphabet.md`](../categories/combinatorics/pie_sequence_derangements_distinct_alphabet.md)  

- **Tag (Domain)**: `Combinatorics`  
- **Subtopic**: `Inclusion-Exclusion`  
- **Topic (Skill)**: `Principle of Inclusion-Exclusion on Constrained Sequence Derangements`  

---

## 1. Problem Statement & Key Idea
Count pairs of sequences A and B of length N from {1..M} such that elements of A are pairwise distinct, elements of B are pairwise distinct, and A_i != B_i for all i, modulo 10^9 + 7.

**Key Insight**: The number of choices for A is P(M, N) = M! / (M - N)!. For any fixed sequence A, the number of valid sequences B is identical by symmetry. Using Principle of Inclusion-Exclusion, select k positions where B_i == A_i: C(N, k) ways. The remaining N - k elements of B are chosen from the M - k remaining values: P(M - k, N - k) ways.

## 2. Core Observation & Invariant
By PIE, ways for B = sum_{k=0}^N (-1)^k * C(N, k) * P(M - k, N - k). Total answer is P(M, N) * (ways for B).

## 3. Step-by-Step Algorithm
1. Precompute factorials and inverses up to M.
2. Compute ways_B = sum_{k=0}^N (-1)^k * C(N, k) * P(M - k, N - k) mod MOD.
3. ans = P(M, N) * ways_B mod MOD.
4. Print ans.

## 4. Complexity Analysis
- **Time Complexity**: `O(N + M)`
- **Space Complexity**: `O(M)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 1000000007;

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

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<long long> fact(m + 1), inv(m + 1);
    fact[0] = inv[0] = 1;
    for (int i = 1; i <= m; ++i) {
        fact[i] = (fact[i - 1] * i) % MOD;
    }
    inv[m] = power(fact[m], MOD - 2);
    for (int i = m - 1; i >= 1; --i) {
        inv[i] = (inv[i + 1] * (i + 1)) % MOD;
    }

    auto nCr = [&](int total, int r) -> long long {
        if (r < 0 || r > total) return 0;
        return fact[total] * inv[r] % MOD * inv[total - r] % MOD;
    };

    auto nPr = [&](int total, int r) -> long long {
        if (r < 0 || r > total) return 0;
        return fact[total] * inv[total - r] % MOD;
    };

    long long ways_b = 0;
    for (int k = 0; k <= n; ++k) {
        long long term = nCr(n, k) * nPr(m - k, n - k) % MOD;
        if (k % 2 == 1) {
            ways_b = (ways_b - term + MOD) % MOD;
        } else {
            ways_b = (ways_b + term) % MOD;
        }
    }

    long long ans = nPr(m, n) * ways_b % MOD;
    cout << ans << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Combining permutations with the Principle of Inclusion-Exclusion to enforce derangement constraints.
- **Reusable Pattern**: `Distinct Sequence Derangement: P(M, N) * sum (-1)^k C(N, k) P(M-k, N-k).`
