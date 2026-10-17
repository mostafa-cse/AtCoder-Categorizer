# Problem Analysis: AtCoder-abc349_f — I. Subsequence LCM

**Problem ID**: `AtCoder-abc349_f`  
**Contest**: `abc349`  
**Rating / Difficulty**: 2169  
**URL**: https://atcoder.jp/contests/abc349/tasks/abc349_f  
**VJudge Tag**: `[problem:AtCoder-abc349_f]`  
**Category File**: [`../categories/dp/subsequence_lcm_sos_dp_inclusion_exclusion.md`](../categories/dp/subsequence_lcm_sos_dp_inclusion_exclusion.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Bit Related DP`  
- **Topic (Skill)**: `Sum Over Subsets DP (SOS DP)`  

---

## 1. Problem Statement & Key Idea
Find the number of non-empty subsequences with LCM equal to M. Factor M into distinct prime powers p_j^{e_j} (at most k <= 15 prime powers). Filter elements to those dividing M, mapping each to a k-bit mask indicating which prime power exponents match e_j. Count subsequences whose bitwise OR is full mask (1<<k)-1 using SOS DP and Principle of Inclusion-Exclusion.

## 2. Core Observation & Invariant
An element A_i can only be used if A_i | M. For each prime factor p_j, the LCM reaches the exact power p_j^{e_j} iff at least one chosen element has exponent e_j. With k <= 15 distinct prime powers, submask counts F(S) = sum_{T subseteq S} cnt[T] are computed in O(k * 2^k) via SOS DP. By inclusion-exclusion, the number of full-OR subsets is sum_{S} (-1)^{k - |S|} 2^{F(S)}.

## 3. Step-by-Step Algorithm
1. If M = 1, count elements equal to 1 (say c) and output 2^c - 1.
2. Factorize M into prime powers (p_0, pw_0), ..., (p_{k-1}, pw_{k-1}).
3. For each A_i dividing M, compute its bitmask sum_{j} [A_i % pw_j == 0] * 2^j, and record counts in array cnt[mask].
4. Compute SOS DP f[mask] = sum_{sub subseteq mask} cnt[sub] in O(k * 2^k).
5. Calculate answer via inclusion-exclusion: ans = sum_{mask} (-1)^{k - popcount(mask)} * 2^{f[mask]} mod 998244353.

## 4. Complexity Analysis
- **Time Complexity**: `O(N + sqrt(M) + k * 2^k)`
- **Space Complexity**: `O(2^k)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 998244353;

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

    int N;
    long long M;
    if (!(cin >> N >> M)) return 0;

    vector<long long> A(N);
    for (int i = 0; i < N; ++i) cin >> A[i];

    if (M == 1) {
        int c = 0;
        for (long long x : A) {
            if (x == 1) c++;
        }
        cout << (power(2, c) - 1 + MOD) % MOD << "\n";
        return 0;
    }

    long long temp = M;
    vector<pair<long long, long long>> primes;
    for (long long p = 2; p * p <= temp; ++p) {
        if (temp % p == 0) {
            long long pw = 1;
            while (temp % p == 0) {
                pw *= p;
                temp /= p;
            }
            primes.push_back({p, pw});
        }
    }
    if (temp > 1) {
        primes.push_back({temp, temp});
    }

    int k = (int)primes.size();
    vector<int> cnt(1 << k, 0);

    for (long long x : A) {
        if (M % x != 0) continue;
        int mask = 0;
        for (int i = 0; i < k; ++i) {
            if (x % primes[i].second == 0) {
                mask |= (1 << i);
            }
        }
        cnt[mask]++;
    }

    vector<int> f = cnt;
    for (int i = 0; i < k; ++i) {
        for (int mask = 0; mask < (1 << k); ++mask) {
            if (mask & (1 << i)) {
                f[mask] += f[mask ^ (1 << i)];
            }
        }
    }

    long long ans = 0;
    for (int mask = 0; mask < (1 << k); ++mask) {
        int set_bits = __builtin_popcount(mask);
        int sign = ((k - set_bits) % 2 == 1 ? -1 : 1);
        long long term = power(2, f[mask]);
        ans = (ans + sign * term) % MOD;
        if (ans < 0) ans += MOD;
    }

    cout << ans << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
