# Problem Analysis: AtCoder-abc020_d — LCM Rush

**Problem ID**: `AtCoder-abc020_d`  
**Contest**: `abc020`  
**Rating / Difficulty**: 2695  
**URL**: https://atcoder.jp/contests/abc020/tasks/abc020_d  
**VJudge Tag**: `[problem:AtCoder-abc020_d]`  
**Category File**: [`../categories/number_theory/lcm_rush_mobius_inversion.md`](../categories/number_theory/lcm_rush_mobius_inversion.md)  

- **Tag (Domain)**: `Number Theory`  
- **Subtopic**: `Multiplicative Functions`  
- **Topic (Skill)**: `Mobius Function and Mobius Inversion`  

---

## 1. Problem Statement & Key Idea
sum_{i=1}^N lcm(i, K) = K * sum_{g | K} sum_{j=1, gcd(j, K/g)=1}^{floor(N/g)} j. For each divisor g of K, the inner coprime sum S(L, M) with M = K/g and L = floor(N/g) is computed in O(2^{omega(M)}) via Mobius inversion / Inclusion-Exclusion over distinct prime factors of M.

## 2. Core Observation & Invariant
Since K <= 10^9, K has at most 10 distinct prime factors and at most 1344 divisors. For each divisor g | K, M = K/g has a subset of K's prime factors. Summing over square-free divisors d | M gives S(L, M) = sum_{d | M} mu(d) * d * (floor(L/d) * (floor(L/d) + 1) / 2). Total operations across all divisors <= 3^{omega(K)} <= 59049.

## 3. Step-by-Step Algorithm
1. 1. Factorize K into distinct prime factors in O(sqrt(K)).
2. 2. Find all divisors g of K.
3. 3. For each divisor g with L = floor(N / g) > 0 and M = K / g:
4.    - Identify prime factors of M.
5.    - Run DFS inclusion-exclusion over subsets of prime factors of M to compute sum_{d | M} mu(d) * d * (L/d * (L/d + 1) / 2) mod MOD.
6.    - Add to total sum.
7. 4. Multiply total sum by K mod MOD and print.

## 4. Complexity Analysis
- **Time Complexity**: `O(sqrt(K) + 3^{omega(K)})`
- **Space Complexity**: `O(d(K) + omega(K))`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

static const long long MOD = 1000000007;

void dfs(int idx, long long cur_d, int sign, int P, long long L, const vector<long long>& m_primes, long long& s_val) {
    if (idx == P) {
        long long cnt = (L / cur_d) % MOD;
        long long term = (cnt * (cnt + 1) / 2) % MOD;
        term = (term * (cur_d % MOD)) % MOD;
        if (sign == 1) {
            s_val = (s_val + term) % MOD;
        } else {
            s_val = (s_val - term + MOD) % MOD;
        }
        return;
    }
    // without
    dfs(idx + 1, cur_d, sign, P, L, m_primes, s_val);
    // with
    dfs(idx + 1, cur_d * m_primes[idx], -sign, P, L, m_primes, s_val);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n, k;
    if (!(cin >> n >> k)) return 0;

    // Prime factors of K
    long long temp = k;
    vector<long long> primes;
    for (long long d = 2; d * d <= temp; ++d) {
        if (temp % d == 0) {
            primes.push_back(d);
            while (temp % d == 0) {
                temp /= d;
            }
        }
    }
    if (temp > 1) {
        primes.push_back(temp);
    }

    // Divisors of K
    vector<long long> divs;
    for (long long d = 1; d * d <= k; ++d) {
        if (k % d == 0) {
            divs.push_back(d);
            if (d * d != k) {
                divs.push_back(k / d);
            }
        }
    }
    sort(divs.begin(), divs.end());

    long long total_sum = 0;
    for (long long g : divs) {
        long long M = k / g;
        long long L = n / g;
        if (L == 0) continue;

        vector<long long> m_primes;
        for (long long p : primes) {
            if (M % p == 0) {
                m_primes.push_back(p);
            }
        }

        long long s_val = 0;
        dfs(0, 1, 1, m_primes.size(), L, m_primes, s_val);
        total_sum = (total_sum + s_val) % MOD;
    }

    long long ans = (total_sum * (k % MOD)) % MOD;
    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
