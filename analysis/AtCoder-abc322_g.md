# Problem Analysis: AtCoder-abc322_g — G. Two Kinds of Base

**Problem ID**: `AtCoder-abc322_g`  
**Contest**: `abc322`  
**Rating / Difficulty**: 2876  
**URL**: https://atcoder.jp/contests/abc322/tasks/abc322_g  
**VJudge Tag**: `[problem:AtCoder-abc322_g]`  
**Category File**: [`../categories/number_theory/polynomial_base_difference_divisor_casework.md`](../categories/number_theory/polynomial_base_difference_divisor_casework.md)  

- **Tag (Domain)**: `Number Theory`  
- **Subtopic**: `Primes and Divisors`  
- **Topic (Skill)**: `Sieve, Prime Factorization and Divisors`  

---

## 1. Problem Statement & Key Idea
Given N and X, count pairs of bases (a, b) with 2 <= a < b <= N such that some integer has identical digits in base a and base b, and the difference in values is X, modulo 998244353.

## 2. Core Observation & Invariant
Let shared digits be d_k ... d_0. The value difference is sum_{i=0}^k d_i (b^i - a^i) = X.
- For k = 2 (2 digits): d_1 (b - a) = X. For each divisor d of X with d_1 = d, count a such that d < a <= N - X/d.
- For k = 3 (3 digits): (b - a)(d_2(a+b) + d_1) = X. Divisors of X yield pairs (a, b).
- For k >= 4: since b >= 3, b^3 <= X implies b <= X^{1/3} <= 10^6. We can directly iterate over (a, b) and greedily verify digits.

## 3. Step-by-Step Algorithm
1. 1. Factorize X and collect all divisors.
2. 2. For k = 2: sum (N - X/d - d) over divisors d of X.
3. 3. For k = 3: iterate over divisors Delta of X and solve for valid digit pairs (d_2, d_1).
4. 4. For k >= 4: iterate over b <= min(N, X^{1/3} + 2) and a < b, greedily extracting base difference digits.
5. 5. Sum results modulo 998244353.

## 4. Complexity Analysis
- **Time Complexity**: `O(d(X) + X^{2/3})`
- **Space Complexity**: `O(1)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

static const long long MOD = 998244353;

long long sum_min10(long long L, long long R) {
    if (L > R) return 0;
    long long ans = 0;
    long long p1_L = L;
    long long p1_R = min(R, 9LL);
    if (p1_L <= p1_R) {
        long long count = p1_R - p1_L + 1;
        long long sum_val = (p1_L + p1_R) * count / 2;
        ans = (ans + sum_val) % MOD;
    }
    long long p2_L = max(L, 10LL);
    long long p2_R = R;
    if (p2_L <= p2_R) {
        long long count = (p2_R - p2_L + 1) % MOD;
        ans = (ans + 10 * count) % MOD;
    }
    return ans % MOD;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    long long n, x;
    if (!(cin >> n >> x)) return 0;

    long long ans = 0;

    // k = 2
    for (int S1 = 1; S1 <= 9; ++S1) {
        if (x % S1 == 0) {
            long long d = x / S1;
            long long L = S1 + 1;
            long long R = n - d;
            ans = (ans + sum_min10(L, R)) % MOD;
        }
    }

    // k >= 3
    vector<long long> divs;
    for (long long d = 1; d * d <= x; ++d) {
        if (x % d == 0) {
            divs.push_back(d);
            if (d * d != x) {
                divs.push_back(x / d);
            }
        }
    }

    for (long long s : divs) {
        if (s * s >= x) continue;
        long long max_b = (x - s * s) / (2 * s);
        max_b = min(max_b, n - s);

        for (long long b = 1; b <= max_b; ++b) {
            long long a = b + s;
            vector<long long> w;
            long long cur_a = a;
            long long cur_b = b;

            while (cur_a - cur_b <= x) {
                w.push_back(cur_a - cur_b);
                if (cur_a > x) break;
                cur_a *= a;
                cur_b *= b;
            }

            if ((int)w.size() < 2) continue;

            long long rem = x;
            vector<long long> digits;
            bool valid = true;
            for (int i = (int)w.size() - 1; i >= 0; --i) {
                long long d_val = rem / w[i];
                rem %= w[i];
                digits.push_back(d_val);
                if (d_val > min(9LL, b - 1)) {
                    valid = false;
                    break;
                }
            }

            if (valid && rem == 0) {
                size_t idx = 0;
                while (idx < digits.size() && digits[idx] == 0) {
                    idx++;
                }
                if (idx < digits.size()) {
                    if (digits.size() - idx + 1 >= 3) {
                        ans = (ans + min(10LL, b)) % MOD;
                    }
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
