# Problem Analysis: AtCoder-arc230_d — D. Min Max Matrix

**Problem ID**: `AtCoder-arc230_d`  
**Contest**: `arc230`  
**Rating / Difficulty**: 2395  
**URL**: https://atcoder.jp/contests/arc230/tasks/arc230_d  
**VJudge Tag**: `[problem:AtCoder-arc230_d]`  
**Category File**: [`../categories/combinatorics/min_max_matrix_saddle_point_pie_lagrange.md`](../categories/combinatorics/min_max_matrix_saddle_point_pie_lagrange.md)  

- **Tag (Domain)**: `Combinatorics`  
- **Subtopic**: `Inclusion Exclusion`  
- **Topic (Skill)**: `Principle of Inclusion and Exclusion (PIE)`  

---

## 1. Problem Statement & Key Idea
Minimax equality is equivalent to the existence of a matrix saddle point. Inclusion-exclusion yields a polynomial expression in M summed over m, evaluated via binomial contraction and Lagrange interpolation in O(H^2 W log W) time.

## 2. Core Observation & Invariant
The condition min_i max_j A_{i,j} = max_j min_i A_{i,j} = m holds iff the matrix contains at least one saddle point. By inclusion-exclusion over non-empty subsets of h rows and w columns forming saddle points, the total valid matrices is sum_{h=1}^H sum_{w=1}^W sum_{m=1}^M C(H,h) C(W,w) (-1)^{h+w} m^{h(W-w)} (M+1-m)^{(H-h)w} M^{(H-h)(W-w)}. Viewing F(M) = sum_{m=1}^M f(m) as a polynomial of degree <= HW + 1, Lagrange interpolation computes the result in O(H^2 W log W) time.

## 3. Step-by-Step Algorithm
1. Factor the inner sum over w using binomial theorem into f(m) = sum_{h=1}^H C(H, h) (-1)^h [(-(M+1-m)^{H-h} + m^h M^{H-h})^W - (m^h M^{H-h})^W].
2. Each f(m) is computable in O(H log W) time.
3. If M <= HW + 1, sum f(m) directly.
4. Otherwise, evaluate prefix sums Y[k] = sum_{m=1}^k f(m) for k = 0 .. HW + 1 and apply Lagrange interpolation at point M in O(HW) time.

## 4. Complexity Analysis
- **Time Complexity**: `O(H^2 W \log W)`
- **Space Complexity**: `O(H W)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

using ll = long long;
const ll MOD = 998244353;

ll power(ll base, ll exp) {
    ll res = 1;
    base %= MOD;
    if (base < 0) base += MOD;
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
    ll H, W, M;
    if (!(cin >> H >> W >> M)) return 0;

    int deg = H * W + 1;
    int max_val = max((int)H, deg) + 5;
    vector<ll> fact(max_val), ifact(max_val);
    fact[0] = 1;
    for (int i = 1; i < max_val; i++) fact[i] = (fact[i - 1] * i) % MOD;
    ifact[max_val - 1] = modInverse(fact[max_val - 1]);
    for (int i = max_val - 2; i >= 0; i--) ifact[i] = (ifact[i + 1] * (i + 1)) % MOD;

    auto nCr = [&](int n, int r) -> ll {
        if (r < 0 || r > n) return 0;
        return fact[n] * ifact[r] % MOD * ifact[n - r] % MOD;
    };

    auto calc_f = [&](ll m) -> ll {
        ll fm = 0;
        for (int h = 1; h <= H; h++) {
            ll sign = (h % 2 == 1) ? (MOD - 1) : 1;
            ll coef = nCr(H, h) * sign % MOD;
            ll term1 = (MOD - power(M + 1 - m, H - h)) % MOD;
            ll term2 = power(m, h) * power(M, H - h) % MOD;
            ll val = (power((term1 + term2) % MOD, W) - power(term2, W) + MOD) % MOD;
            fm = (fm + coef * val) % MOD;
        }
        return fm;
    };

    if (M <= deg) {
        ll ans = 0;
        for (int m = 1; m <= M; m++) {
            ans = (ans + calc_f(m)) % MOD;
        }
        cout << ans << "\n";
        return 0;
    }

    vector<ll> Y(deg + 1, 0);
    for (int k = 1; k <= deg; k++) {
        Y[k] = (Y[k - 1] + calc_f(k)) % MOD;
    }

    vector<ll> pref(deg + 2, 1), suff(deg + 2, 1);
    for (int i = 0; i <= deg; i++) {
        pref[i + 1] = (pref[i] * ((M - i) % MOD + MOD)) % MOD;
    }
    for (int i = deg; i >= 0; i--) {
        suff[i] = (suff[i + 1] * ((M - i) % MOD + MOD)) % MOD;
    }

    ll ans = 0;
    for (int i = 0; i <= deg; i++) {
        ll num = (pref[i] * suff[i + 1]) % MOD;
        ll den = (ifact[i] * ifact[deg - i]) % MOD;
        if ((deg - i) % 2 == 1) den = (MOD - den) % MOD;
        ll term = Y[i] * num % MOD * den % MOD;
        ans = (ans + term) % MOD;
    }

    cout << (ans % MOD + MOD) % MOD << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
