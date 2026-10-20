# Problem Analysis: AtCoder-agc068_a — A. Circular Distance

**Problem ID**: `AtCoder-agc068_a`  
**Contest**: `agc068`  
**Rating / Difficulty**: 2948  
**URL**: https://atcoder.jp/contests/agc068/tasks/agc068_a  
**VJudge Tag**: `[problem:AtCoder-agc068_a]`  
**Category File**: [`../categories/combinatorics/circular_distance_maximum_gap_complement_counting.md`](../categories/combinatorics/circular_distance_maximum_gap_complement_counting.md)  

- **Tag (Domain)**: `Combinatorics`  
- **Subtopic**: `Techniques`  
- **Topic (Skill)**: `Contribution Technique`  

---

## 1. Problem Statement & Key Idea
Choose N people out of L on a circle. The cost is the maximum pairwise circular distance. Find the sum of costs over all binom(L, N) subsets, modulo 998244353.

## 2. Core Observation & Invariant
Fix person 0 to be chosen, then multiply total cost by L/N. Compute c[d], the number of choices where maximum distance <= d. Points must lie in [-d, d]. Choosing points on the left [1, d-1] (red points) and right [L-d+1, L-1] (blue intervals of length W = L - 2d + 1) such that no red point falls in a blue interval. Classifying by the number of alternations i between red and blue components allows direct closed-form binomial coefficient evaluation: sum_i binom(d - i(W - 2), N - 1) binom(N, 2i + 1). Summing across d takes harmonic series time O(L log L).

## 3. Step-by-Step Algorithm
1. 1. Precompute factorials and inverses up to L + N.
2. 2. For each distance d in [1, L/2]: if t = L - 2d - 1 <= 0, c[d] = binom(L-1, N-1); else sum binom(d - i(t - 1), N - 1) binom(N, 2i + 1) for i * t <= d.
3. 3. Take differences (c[d] - c[d-1]) * d to accumulate expectation.
4. 4. Multiply final result by L * N^-1 mod 998244353.

## 4. Complexity Analysis
- **Time Complexity**: `O(L log L)`
- **Space Complexity**: `O(L)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>

using namespace std;

static const int MOD = 998244353;

long long power_mod(long long base, long long exp) {
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
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    long long m, n;
    if (!(cin >> m >> n)) return 0;

    int max_val = m + n + 10;
    vector<long long> fac(max_val, 1);
    for (int i = 1; i < max_val; ++i) {
        fac[i] = (fac[i - 1] * i) % MOD;
    }

    vector<long long> ifac(max_val, 1);
    ifac[max_val - 1] = power_mod(fac[max_val - 1], MOD - 2);
    for (int i = max_val - 1; i >= 1; --i) {
        ifac[i - 1] = (ifac[i] * i) % MOD;
    }

    auto C = [&](long long a, long long b) -> long long {
        if (b < 0 || b > a || a < 0) return 0;
        return fac[a] * ifac[b] % MOD * ifac[a - b] % MOD;
    };

    long long prev_c = 0;
    long long ans = 0;

    for (long long d = 1; 2 * d <= m; ++d) {
        long long t = m - 2 * d - 1;
        long long cur_c = 0;

        if (t <= 0) {
            cur_c = C(m - 1, n - 1);
        } else {
            for (long long i = 0; i * t <= d; ++i) {
                long long term = C(d - i * (t - 1), n - 1) * C(n, 2 * i + 1) % MOD;
                cur_c = (cur_c + term) % MOD;
            }
        }

        long long diff = (cur_c - prev_c + MOD) % MOD;
        ans = (ans + diff * d) % MOD;
        prev_c = cur_c;
    }

    long long total_ans = ans * m % MOD * power_mod(n, MOD - 2) % MOD;
    cout << total_ans << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
