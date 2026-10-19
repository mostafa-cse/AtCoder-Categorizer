# Problem Analysis: AtCoder-arc186_d — D - Polish Mania

**Problem ID**: `AtCoder-arc186_d`  
**Contest**: `arc186`  
**Rating / Difficulty**: 2776  
**URL**: https://atcoder.jp/contests/arc186/tasks/arc186_d  
**VJudge Tag**: `[problem:AtCoder-arc186_d]`  
**Category File**: [`../categories/combinatorics/polish_sequences_catalan_lattice_path.md`](../categories/combinatorics/polish_sequences_catalan_lattice_path.md)  

- **Tag (Domain)**: `Combinatorics`  
- **Subtopic**: `Catalan`  
- **Topic (Skill)**: `Catalan Numbers`  

---

## 1. Problem Statement & Key Idea
A sequence of non-negative integers A is a Polish sequence if it corresponds to Polish prefix notation of a tree: every proper prefix sum sum_{j=1}^k (a_j - 1) >= 0 and the full sum is -1. Count Polish sequences of length N that are lexicographically <= A, modulo 998244353.

## 2. Core Observation & Invariant
Polish sequences correspond to lattice paths strictly above a boundary (Ballot theorem / Catalan lattice paths). If we deviate from A at index i with a choice x < A[i], the remaining suffix of length L = N - i must complete the path to total excess -1 without dropping below 0 before the end. The number of such completions from current excess h is given by F(L, h) = C(2L - 1 - h, L - 1) - C(2L - 1 - h, L). Summing F(L, h) over the valid choices of x < A[i] telescopes via the hockey-stick identity on Pascal's triangle into a closed form evaluable in O(1) time.

## 3. Step-by-Step Algorithm
1. 1. Precompute factorials and inverse factorials up to 2*N.
2. 2. Maintain prefix excess S_k = sum_{j=1}^k (A[j] - 1). If at any step S_k < 0 for k < N, the prefix is already invalid and no further prefix matches can continue.
3. 3. At each index i from 1 to N, consider branching with x < A[i]:
4.    - Suffix length L = N - i.
5.    - Branching range of x is 0 <= x < A[i] such that S_{i-1} + (x - 1) >= 0.
6.    - Sum F(L, S_{i-1} + x - 1) using precomputed binomial sums.
7. 4. Add 1 if the input sequence A itself is a valid Polish sequence.
8. 5. Output the total modulo 998244353.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

static const long long MOD = 998244353;

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

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    if (!(cin >> N)) return 0;

    vector<int> A(N);
    for (int i = 0; i < N; ++i) {
        cin >> A[i];
    }

    int max_fact = 2 * N + 5;
    vector<long long> fact(max_fact, 1), inv(max_fact, 1);
    for (int i = 1; i < max_fact; ++i) {
        fact[i] = (fact[i - 1] * i) % MOD;
    }
    inv[max_fact - 1] = modInverse(fact[max_fact - 1]);
    for (int i = max_fact - 2; i >= 0; --i) {
        inv[i] = (inv[i + 1] * (i + 1)) % MOD;
    }

    auto C = [&](int n, int k) -> long long {
        if (k < 0 || k > n) return 0;
        return fact[n] * inv[k] % MOD * inv[n - k] % MOD;
    };

    auto pref_sum = [&](int L, int H) -> long long {
        if (H <= 0) return 0;
        H = min(H, L);
        long long p1 = (C(2 * L - 1, L) - C(2 * L - 1 - H, L) + MOD) % MOD;
        long long p2 = (C(2 * L - 1, L + 1) - C(2 * L - 1 - H, L + 1) + MOD) % MOD;
        return (p1 - p2 + MOD) % MOD;
    };

    auto range_sum = [&](int L, int h1, int h2) -> long long {
        if (h1 > h2) return 0;
        return (pref_sum(L, h2) - pref_sum(L, h1 - 1) + MOD) % MOD;
    };

    long long ans = 0;
    int c = 1;
    bool possible_eq = true;

    for (int i = 1; i <= N; ++i) {
        int a_i = A[i - 1];
        int L = N - i;

        if (L == 0) {
            if (c == 1) {
                if (0 < a_i) {
                    ans = (ans + 1) % MOD;
                }
            }
            if (!(c == 1 && a_i == 0)) {
                possible_eq = false;
            }
            break;
        }

        int h_min = c - 1;
        int h_max = c + a_i - 2;
        ans = (ans + range_sum(L, h_min, h_max)) % MOD;

        c = c + a_i - 1;
        if (c <= 0) {
            possible_eq = false;
            break;
        }
    }

    if (possible_eq) {
        ans = (ans + 1) % MOD;
    }

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
