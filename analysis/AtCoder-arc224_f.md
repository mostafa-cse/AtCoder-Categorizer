# Problem Analysis: AtCoder-arc224_f — F. AND/OR

**Problem ID**: `AtCoder-arc224_f`  
**Contest**: `arc224`  
**Rating / Difficulty**: 2407  
**URL**: https://atcoder.jp/contests/arc224/tasks/arc224_f  
**VJudge Tag**: `[problem:AtCoder-arc224_f]`  
**Category File**: [`../categories/basics/bitwise_and_or_suffix_fixed_flag_pascal_dp.md`](../categories/basics/bitwise_and_or_suffix_fixed_flag_pascal_dp.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Bitwise Thinking`  
- **Topic (Skill)**: `Bitwise Operations and Bitmasks`  

---

## 1. Problem Statement & Key Idea
Choose AND or OR for each element of A with at most K OR operations to achieve the maximum possible final value M. Count the number of valid operation sequences by working backwards with a fixed-bit state and Pascal triangle prefix sums.

## 2. Core Observation & Invariant
The maximum value M is achieved by placing all K OR operations at the end: M = OR_{i=N-K}^{N-1} A_i. Working backwards from the last operation, bits that must match M become permanently fixed, bounding the number of active branch states to at most 2.

## 3. Step-by-Step Algorithm
1. 1. Compute maximum value M using the suffix of K elements.
2. 2. Work backwards from step N-1 to 0 maintaining (fixed_flag, remaining_k, ways_sum).
3. 3. Use Pascal's triangle identity S_d = 2 S_u - binom(N-1, K) to update binomial prefix sums in O(1) time.
4. 4. Aggregate solutions where all bits of M are certified.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

using ll = long long;
const int MOD = 998244353;

struct Mint {
    ll v;
    Mint(ll _v = 0) { v = (-MOD < _v && _v < MOD) ? _v : _v % MOD; if (v < 0) v += MOD; }
    Mint& operator+=(const Mint& o) { if ((v += o.v) >= MOD) v -= MOD; return *this; }
    Mint& operator-=(const Mint& o) { if ((v -= o.v) < 0) v += MOD; return *this; }
    Mint& operator*=(const Mint& o) { v = (v * o.v) % MOD; return *this; }
    Mint& operator/=(const Mint& o) { return (*this) *= o.inv(); }
    Mint operator+(const Mint& o) const { return Mint(*this) += o; }
    Mint operator-(const Mint& o) const { return Mint(*this) -= o; }
    Mint operator*(const Mint& o) const { return Mint(*this) *= o; }
    Mint operator/(const Mint& o) const { return Mint(*this) /= o; }
    Mint inv() const {
        ll a = v, b = MOD, u = 1, w = 0;
        while (b) { ll t = a / b; a -= t * b; swap(a, b); u -= t * w; swap(u, w); }
        if (u < 0) u += MOD;
        return Mint(u);
    }
};

const int MXM = 200005;
Mint fac[MXM], invfac[MXM];

void calc_fac() {
    fac[0] = Mint(1);
    for (int i = 1; i < MXM; i++) fac[i] = fac[i - 1] * Mint(i);
    invfac[MXM - 1] = fac[MXM - 1].inv();
    for (int i = MXM - 2; i >= 0; i--) invfac[i] = invfac[i + 1] * Mint(i + 1);
}

Mint nCr(ll n, ll r) {
    if (n < 0 || r < 0 || n < r) return Mint(0);
    return fac[n] * invfac[r] * invfac[n - r];
}

using tup = tuple<ll, ll, Mint>;

void solve() {
    ll n, k;
    if (!(cin >> n >> k)) return;
    ll al = (1ULL << 60) - 1;
    ll o = 0;
    vector<ll> a(n);
    for (auto &nx : a) {
        cin >> nx;
        o |= nx;
    }
    ll d1 = 0;
    for (ll i = n - k; i < n; i++) d1 |= a[i];
    ll d0 = (al ^ d1);
    Mint ini(0);
    for (ll i = 0; i <= k; i++) ini += nCr(n, i);
    vector<tup> sta = {{0, k, ini}};
    Mint res = 0;
    Mint inv2 = Mint(2).inv();

    for (ll i = n - 1; i >= 0; i--) {
        vector<tup> nsta;
        for (auto [f, rk, pat] : sta) {
            ll e0 = ((al ^ f) & d0);
            ll e1 = ((al ^ f) & d1);
            int ban = 0;
            if ((e0 & a[i]) > 0) ban |= 2;
            if ((e1 & (al ^ a[i])) > 0) ban |= 1;
            if ((ban & 1) == 0) {
                Mint npat = (pat + nCr(i, rk)) * inv2;
                nsta.push_back({(f | (e0 & (al ^ a[i]))), rk, npat});
            }
            if ((ban & 2) == 0 && rk > 0) {
                Mint npat = (pat - nCr(i, rk)) * inv2;
                nsta.push_back({(f | (e1 & a[i])), rk - 1, npat});
            }
        }
        sta.clear();
        for (auto [f, rk, pat] : nsta) {
            if ((f & o) == o) {
                res += pat;
            } else {
                sta.push_back({f, rk, pat});
            }
        }
    }
    for (auto [f, rk, pat] : sta) {
        if ((f & d1) == d1) res += pat;
    }
    cout << res.v << "\n";
}

int main() {
    calc_fac();
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t;
    if (cin >> t) {
        while (t--) solve();
    }
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
