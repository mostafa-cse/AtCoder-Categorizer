# Problem Analysis: AtCoder-abc241_h — Ex. Card Deck Score

**Problem ID**: `AtCoder-abc241_h`  
**Contest**: `abc241`  
**Rating / Difficulty**: 2881  
**URL**: https://atcoder.jp/contests/abc241/tasks/abc241_h  
**VJudge Tag**: `[problem:AtCoder-abc241_h]`  
**Category File**: [`../categories/math/distinct_weights_partial_fractions_fps.md`](../categories/math/distinct_weights_partial_fractions_fps.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Polynomial`  
- **Topic (Skill)**: `Generating Functions`  

---

## 1. Problem Statement & Key Idea
Given N distinct card types with values A_i and limits B_i, count the sum of products of chosen card values over all multisets of size M modulo 998244353, where M can be up to 10^18 and N <= 16.

## 2. Core Observation & Invariant
The ordinary generating function for card i is sum_{j=0}^{B_i} (A_i x)^j = (1 - (A_i x)^{B_i + 1}) / (1 - A_i x). The total generating function is F(x) = prod_{i=1}^N (1 - (A_i x)^{B_i + 1}) / prod_{i=1}^N (1 - A_i x). Expanding the numerator yields at most 2^N terms (-1)^{|S|} prod_{i in S} A_i^{B_i+1} x^{sum_{i in S} (B_i+1)}. The denominator 1 / prod_{i=1}^N (1 - A_i x) decomposes by partial fractions into sum_{i=1}^N c_i / (1 - A_i x), where c_i = prod_{j != i} 1 / (1 - A_j / A_i). The coefficient of x^k in 1 / (1 - A_i x) is A_i^k. Thus, each monomial c * x^L in the numerator contributes c * sum_{i=1}^N c_i A_i^{M - L} to [x^M] F(x).

## 3. Step-by-Step Algorithm
1. 1. Compute partial fraction coefficients c_i = prod_{j != i} (1 - A_j * A_i^{-1})^{-1} modulo 998244353.
2. 2. Expand the numerator polynomial of degree up to sum (B_i + 1) using recursion / bitmask DP in O(2^N) time.
3. 3. For each monomial w * x^L in the numerator with L <= M, add w * sum_{i=1}^N c_i A_i^{M - L} to the answer.
4. 4. Output total modulo 998244353.

## 4. Complexity Analysis
- **Time Complexity**: `O(2^N * N + N^2)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>

using namespace std;

static const long long MOD = 998244353;

long long power(long long base, long long exp) {
    long long res = 1;
    base %= MOD;
    if (base < 0) base += MOD;
    while (exp > 0) {
        if (exp % 2 == 1) res = (__int128)res * base % MOD;
        base = (__int128)base * base % MOD;
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

    int n;
    long long m;
    if (!(cin >> n >> m)) return 0;

    vector<long long> a(n), b(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i] >> b[i];
    }

    vector<long long> C(n, 1);
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (i == j) continue;
            long long diff = (a[i] - a[j]) % MOD;
            if (diff < 0) diff += MOD;
            long long term = a[i] % MOD * modInverse(diff) % MOD;
            C[i] = C[i] * term % MOD;
        }
    }

    long long total_ans = 0;
    int num_masks = (1 << n);

    for (int mask = 0; mask < num_masks; ++mask) {
        int sgn = 1;
        long long deg = 0;
        long long coeff = 1;
        bool over = false;

        for (int i = 0; i < n; ++i) {
            if ((mask >> i) & 1) {
                sgn = -sgn;
                deg += b[i] + 1;
                if (deg > m) {
                    over = true;
                    break;
                }
                long long p_a = power(a[i], b[i] + 1);
                coeff = coeff * p_a % MOD;
            }
        }

        if (over || deg > m) continue;

        long long rem = m - deg;
        long long val = 0;
        for (int i = 0; i < n; ++i) {
            long long cur = C[i] * power(a[i], rem) % MOD;
            val = (val + cur) % MOD;
        }

        long long term = coeff * val % MOD;
        if (sgn == 1) {
            total_ans = (total_ans + term) % MOD;
        } else {
            total_ans = (total_ans - term + MOD) % MOD;
        }
    }

    cout << total_ans << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
