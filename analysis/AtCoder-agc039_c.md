# Problem Analysis: AtCoder-agc039_c — C. Division by Two with Something

**Problem ID**: `AtCoder-agc039_c`  
**Contest**: `agc039`  
**Rating / Difficulty**: 2379  
**URL**: https://atcoder.jp/contests/agc039/tasks/agc039_c  
**VJudge Tag**: `[problem:AtCoder-agc039_c]`  
**Category File**: [`../categories/combinatorics/negated_cyclic_shift_mobius_periods.md`](../categories/combinatorics/negated_cyclic_shift_mobius_periods.md)  

- **Tag (Domain)**: `Combinatorics`  
- **Subtopic**: `Inclusion Exclusion`  
- **Topic (Skill)**: `Principle of Inclusion and Exclusion (PIE)`  

---

## 1. Problem Statement & Key Idea
Compute the sum of return periods under negated cyclic bit shifts for all integers k <= X. Any state has period 2d dividing 2N with N/d odd, uniquely determined by its length-d prefix. Counting valid prefixes <= X in O(N) per divisor and applying inclusion-exclusion over odd-quotient divisors solves the problem in O(N d(N)) time.

## 2. Core Observation & Invariant
The operation shifts bits right with the new MSB equal to 1 - LSB, which is a negated cyclic shift of string S. A sequence has return period 2d dividing 2N iff N/d is odd and S satisfies S[i+d] = 1 - S[i] for all i. The sequence is completely determined by its prefix of length d.

## 3. Step-by-Step Algorithm
1. Find all divisors d of N such that N/d is odd.
2. For each divisor d, the number of valid sequences <= X is the binary value of X[0..d-1] plus 1 if the periodically generated string <= X.
3. Apply inclusion-exclusion over odd quotients: f[d] = C[d] - sum_{d' | d, d/d' odd, d' < d} f[d'].
4. Multiply each count by its return period 2d and sum modulo 998244353.

## 4. Complexity Analysis
- **Time Complexity**: `O(N d(N))`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

const long long MOD = 998244353;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    string X;
    if (!(cin >> n >> X)) return 0;

    vector<int> divs;
    for (int d = 1; d * d <= n; ++d) {
        if (n % d == 0) {
            if ((n / d) % 2 == 1) divs.push_back(d);
            int d2 = n / d;
            if (d2 != d && (n / d2) % 2 == 1) divs.push_back(d2);
        }
    }
    sort(divs.begin(), divs.end());

    int num_divs = divs.size();
    vector<long long> C(num_divs);

    for (int idx = 0; idx < num_divs; ++idx) {
        int d = divs[idx];
        long long val = 0;
        for (int i = 0; i < d; ++i) {
            val = (val * 2 + (X[i] - '0')) % MOD;
        }

        string S(n, '0');
        for (int i = 0; i < n; ++i) {
            int q = i / d;
            int r = i % d;
            char bit = X[r];
            if (q % 2 == 1) {
                bit = (bit == '0' ? '1' : '0');
            }
            S[i] = bit;
        }

        if (S <= X) {
            val = (val + 1) % MOD;
        }
        C[idx] = val;
    }

    vector<long long> f = C;
    for (int i = 0; i < num_divs; ++i) {
        int d = divs[i];
        for (int j = 0; j < i; ++j) {
            int d2 = divs[j];
            if (d % d2 == 0 && (d / d2) % 2 == 1) {
                f[i] = (f[i] - f[j] + MOD) % MOD;
            }
        }
    }

    long long ans = 0;
    for (int i = 0; i < num_divs; ++i) {
        ans = (ans + f[i] * (2LL * divs[i])) % MOD;
    }
    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
