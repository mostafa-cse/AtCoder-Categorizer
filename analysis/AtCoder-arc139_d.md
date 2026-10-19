# Problem Analysis: AtCoder-arc139_d — D - Priority Queue

**Problem ID**: `AtCoder-arc139_d`  
**Contest**: `arc139`  
**Rating / Difficulty**: 2816  
**URL**: https://atcoder.jp/contests/arc139/tasks/arc139_d  
**VJudge Tag**: `[problem:AtCoder-arc139_d]`  
**Category File**: [`../categories/math/multiset_threshold_indicator_zero_one_principle.md`](../categories/math/multiset_threshold_indicator_zero_one_principle.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Probabilities and Expected Values`  
- **Topic (Skill)**: `Probabilities and Expected Values`  

---

## 1. Problem Statement & Key Idea
Given a multiset A of N integers in [1, M], repeat K times: insert a uniformly chosen integer in [1, M] and erase the X-th smallest element. Find the sum of multiset element sums across all M^K operation sequences modulo 998244353.

## 2. Core Observation & Invariant
By the 0-1 principle, sum_{a in A} a = sum_{v=1}^M sum_{a in A} [a >= v]. For any fixed threshold v, map elements >= v to 1 and < v to 0. An inserted 1 increases the count of ones c by 1 iff c <= N - X, while an inserted 0 decreases c by 1 iff c > N - X + 1. Thus c = N - X + 1 is an absorbing boundary! Crucially, the final count of 1s depends solely on the total number of inserted 1s j, independent of insertion order: final_c = min(N - X + 1, c_0 + j) if c_0 <= N - X + 1, and max(N - X + 1, c_0 - (K - j)) otherwise.

## 3. Step-by-Step Algorithm
1. 1. Compute prefix frequencies of initial elements >= v for all v in [1, M].
2. 2. Add the baseline contribution of v = 1: N * M^K mod 998244353.
3. 3. For each threshold v in [2, M], let c0 = count(A_i >= v), p1 = M - v + 1, p0 = v - 1.
4. 4. Iterate over the number of inserted 1s j from 0 to K. The probability weight is C(K, j) * p1^j * p0^(K - j).
5. 5. Determine the deterministic final count of 1s: min(N - X + 1, c0 + j) if c0 <= N - X + 1 else max(N - X + 1, c0 - (K - j)).
6. 6. Accumulate over all v and j modulo 998244353.

## 4. Complexity Analysis
- **Time Complexity**: `O(M * K)`
- **Space Complexity**: `O(K)`

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

long long modInverse(long long n) {
    return power(n, MOD - 2);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m, k, x;
    if (!(cin >> n >> m >> k >> x)) return 0;

    vector<int> a(n);
    vector<int> count_ge(m + 2, 0);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        count_ge[a[i]]++;
    }
    for (int v = m; v >= 1; --v) {
        count_ge[v] += count_ge[v + 1];
    }

    vector<long long> fact(k + 1, 1), inv(k + 1, 1);
    for (int i = 1; i <= k; ++i) {
        fact[i] = (fact[i - 1] * i) % MOD;
    }
    inv[k] = modInverse(fact[k]);
    for (int i = k - 1; i >= 0; --i) {
        inv[i] = (inv[i + 1] * (i + 1)) % MOD;
    }

    auto nCr = [&](int n_val, int r_val) -> long long {
        if (r_val < 0 || r_val > n_val) return 0;
        return fact[n_val] * inv[r_val] % MOD * inv[n_val - r_val] % MOD;
    };

    // Contribution of v = 1: each of the m^k scenarios ends with n elements, all >= 1.
    long long ans = (1LL * n * power(m, k)) % MOD;

    vector<long long> pow_p1(k + 1, 1), pow_p0(k + 1, 1);

    for (int v = 2; v <= m; ++v) {
        int c0 = count_ge[v];
        long long p1 = m - v + 1;
        long long p0 = v - 1;

        pow_p1[0] = 1;
        pow_p0[0] = 1;
        for (int i = 1; i <= k; ++i) {
            pow_p1[i] = (pow_p1[i - 1] * p1) % MOD;
            pow_p0[i] = (pow_p0[i - 1] * p0) % MOD;
        }

        long long sum_v = 0;
        for (int j = 0; j <= k; ++j) {
            long long ways = nCr(k, j) * pow_p1[j] % MOD * pow_p0[k - j] % MOD;
            int final_c = 0;
            if (c0 <= n - x + 1) {
                final_c = min(n - x + 1, c0 + j);
            } else {
                final_c = max(n - x + 1, c0 - (k - j));
            }
            sum_v = (sum_v + ways * final_c) % MOD;
        }
        ans = (ans + sum_v) % MOD;
    }

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
