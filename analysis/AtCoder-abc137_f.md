# Problem Analysis: AtCoder-abc137_f — F. Polynomial Construction

**Problem ID**: `AtCoder-abc137_f`  
**Contest**: `abc137`  
**Rating / Difficulty**: 2402  
**URL**: https://atcoder.jp/contests/abc137/tasks/abc137_f  
**VJudge Tag**: `[problem:AtCoder-abc137_f]`  
**Category File**: [`../categories/math/lagrange_interpolation_indicator_polynomial.md`](../categories/math/lagrange_interpolation_indicator_polynomial.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Polynomial`  
- **Topic (Skill)**: `Lagrange Interpolation`  

---

## 1. Problem Statement & Key Idea
Given a function f: F_p -> {0, 1}, construct a polynomial P(x) of degree at most p-1 such that P(x) = f(x) for all x in F_p. By Fermat's Little Theorem, the indicator function for x=a is 1 - (x - a)^{p-1}.

## 2. Core Observation & Invariant
For any element a in F_p, (x - a)^{p-1} is 0 if x=a and 1 if x != a (mod p). Thus, the indicator polynomial for x = a is I_a(x) = 1 - (x - a)^{p-1}. Summing over all a with f(a) = 1 gives P(x) = sum_{a: f(a)=1} (1 - (x - a)^{p-1}) mod p.

## 3. Step-by-Step Algorithm
1. 1. Express P(x) = sum_{a: f(a)=1} (1 - (x - a)^{p-1}).
2. 2. Expand (x - a)^{p-1} using the Binomial Theorem: sum_{k=0}^{p-1} binom(p-1, k) x^k (-a)^{p-1-k}.
3. 3. Aggregate the coefficients across all active a in O(p^2) time.

## 4. Complexity Analysis
- **Time Complexity**: `O(p^2)`
- **Space Complexity**: `O(p)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int p;
    if (!(cin >> p)) return 0;

    vector<int> a(p);
    for (int i = 0; i < p; i++) cin >> a[i];

    auto power = [&](ll base, ll exp) -> ll {
        ll res = 1;
        base %= p;
        while (exp > 0) {
            if (exp % 2 == 1) res = (res * base) % p;
            base = (base * base) % p;
            exp /= 2;
        }
        return res;
    };

    vector<ll> b(p, 0);
    b[0] = a[0];
    for (int k = 1; k < p; k++) {
        ll s = 0;
        if (k == p - 1) {
            s = (s - a[0] + p) % p;
        }
        for (int i = 1; i < p; i++) {
            if (a[i]) {
                ll val = power(i, p - 1 - k);
                s = (s - val + p) % p;
            }
        }
        b[k] = s;
    }

    for (int i = 0; i < p; i++) {
        cout << b[i] << (i + 1 == p ? "" : " ");
    }
    cout << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
