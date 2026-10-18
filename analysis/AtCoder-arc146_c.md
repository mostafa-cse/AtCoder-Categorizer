# Problem Analysis: AtCoder-arc146_c — Even XOR

**Problem ID**: `AtCoder-arc146_c`  
**Contest**: `arc146`  
**Rating / Difficulty**: 2428  
**URL**: https://atcoder.jp/contests/arc146/tasks/arc146_c  
**VJudge Tag**: `[problem:AtCoder-arc146_c]`  
**Category File**: [`../categories/math/even_xor_free_subsets_affine_basis_gf2.md`](../categories/math/even_xor_free_subsets_affine_basis_gf2.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Linear Algebra`  
- **Topic (Skill)**: `Vector Space and XOR Basis`  

---

## 1. Problem Statement & Key Idea
Count subsets S of GF(2)^N where no non-empty even subset has XOR sum 0 by mapping each element x to the vector (x, 1) in GF(2)^(N+1) and recognizing that the condition is equivalent to linear independence in GF(2)^(N+1).

## 2. Core Observation & Invariant
For any subset T, sum_{x in T} (x, 1) = (XOR_{x in T} x, |T| mod 2). Thus an even-sized subset with XOR sum 0 corresponds exactly to a linear dependency among the augmented vectors! The size of S is bounded by N + 1, and the count of linearly independent sets of size k has a closed product form.

## 3. Step-by-Step Algorithm
1. 1. For k = 0, there is 1 set (empty set).
2. 2. For k from 1 to N + 1, the number of choices for the i-th vector with last coordinate 1 is 2^N for i = 1, and (2^N - 2^(i - 2)) for i >= 2.
3. 3. Maintain the running product of choices and divide by k! modulo 998244353.
4. 4. Accumulate the count across all k from 0 to N + 1 and output the sum.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(1)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

using ll = long long;
const ll MOD = 998244353;

ll power(ll base, ll exp) {
    ll res = 1;
    base %= MOD;
    while (exp > 0) {
        if (exp % 2 == 1) res = (res * base) % MOD;
        base = (base * base) % MOD;
        exp /= 2;
    }
    return res;
}

ll modInverse(ll n) {
    return power(n, MOD - 2);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    ll two_n = power(2, n);
    ll ans = 1; // k = 0
    ll cur_prod = 1;
    ll inv_fact = 1;

    for (int k = 1; k <= n + 1; k++) {
        ll term = 0;
        if (k == 1) {
            term = two_n;
        } else {
            ll p2 = power(2, k - 2);
            term = (two_n - p2 + MOD) % MOD;
        }
        cur_prod = (cur_prod * term) % MOD;
        inv_fact = (inv_fact * modInverse(k)) % MOD;
        ll ways = (cur_prod * inv_fact) % MOD;
        ans = (ans + ways) % MOD;
    }

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
