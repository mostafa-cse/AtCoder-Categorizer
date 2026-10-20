# Problem Analysis: AtCoder-arc064_d — F. Rotated Palindromes

**Problem ID**: `AtCoder-arc064_d`  
**Contest**: `arc064`  
**Rating / Difficulty**: 2949  
**URL**: https://atcoder.jp/contests/arc064/tasks/arc064_d  
**VJudge Tag**: `[problem:AtCoder-arc064_d]`  
**Category File**: [`../categories/miscellaneous/rotated_palindrome_burnside_period_mobius_inversion.md`](../categories/miscellaneous/rotated_palindrome_burnside_period_mobius_inversion.md)  

- **Tag (Domain)**: `Miscellaneous`  
- **Subtopic**: `General`  
- **Topic (Skill)**: `Burnside's Lemma / Polya Enumeration Theorem`  

---

## 1. Problem Statement & Key Idea
Takahashi creates a palindrome of length N with elements in {1, ..., K}. Aoki cyclically shifts it any number of times. Count the number of distinct possible final sequences modulo 10^9 + 7.

## 2. Core Observation & Invariant
The set of obtainable sequences is the union of cyclic shift orbits containing at least one palindrome. For an orbit with minimal period d (where d | N), the block of length d must itself be a palindrome of length d, so there are K^{ceil(d / 2)} palindromes of period dividing d. By Mobius inversion / divisor DP, we compute the number of palindromes f(d) with minimal period exactly d. If d is odd, the orbit has size d and contains exactly 1 palindrome, contributing f(d) * d. If d is even, the orbit contains 2 palindromes, contributing f(d) * (d / 2).

## 3. Step-by-Step Algorithm
1. 1. Find all divisors d of N and sort them.
2. 2. Compute g(d) = K^{ceil(d / 2)} mod (10^9 + 7).
3. 3. Compute f(d) = g(d) - sum_{c | d, c < d} f(c).
4. 4. For each divisor d, add f(d) * (d if odd else d/2) to total sum.
5. 5. Output answer modulo 10^9 + 7.

## 4. Complexity Analysis
- **Time Complexity**: `O(d(N)^2 + sqrt(N))`
- **Space Complexity**: `O(d(N))`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

static const long long MOD = 1000000007;

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

    long long n, k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> divs;
    for (long long i = 1; i * i <= n; ++i) {
        if (n % i == 0) {
            divs.push_back(i);
            if (i * i != n) {
                divs.push_back(n / i);
            }
        }
    }
    sort(divs.begin(), divs.end());

    int num_divs = divs.size();
    vector<long long> f(num_divs, 0);

    for (int i = 0; i < num_divs; ++i) {
        long long d = divs[i];
        long long exp = (d + 1) / 2;
        long long g = power_mod(k, exp);
        long long cur = g;

        for (int j = 0; j < i; ++j) {
            long long c = divs[j];
            if (d % c == 0) {
                cur = (cur - f[j] + MOD) % MOD;
            }
        }
        f[i] = cur;
    }

    long long ans = 0;
    for (int i = 0; i < num_divs; ++i) {
        long long d = divs[i];
        long long mult = (d % 2 == 1) ? d : (d / 2);
        mult %= MOD;
        ans = (ans + f[i] * mult) % MOD;
    }

    cout << ans << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
