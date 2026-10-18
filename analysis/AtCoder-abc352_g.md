# Problem Analysis: AtCoder-abc352_g — Socks 3

**Problem ID**: `AtCoder-abc352_g`  
**Contest**: `abc352`  
**Rating / Difficulty**: 2413  
**URL**: https://atcoder.jp/contests/abc352/tasks/abc352_g  
**VJudge Tag**: `[problem:AtCoder-abc352_g]`  
**Category File**: [`../categories/math/socks_distinct_draws_generating_functions_ntt.md`](../categories/math/socks_distinct_draws_generating_functions_ntt.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Polynomial`  
- **Topic (Skill)**: `Generating Functions`  

---

## 1. Problem Statement & Key Idea
Compute the expected number of draws to obtain a matching pair by linearity of expectation E[X] = sum P(X > k), where P(X > k) is the probability that the first k drawn socks are all of distinct colors, expressed as [x^k] prod(1 + A_i x) / C(S, k) via Divide and Conquer NTT.

## 2. Core Observation & Invariant
By the tail sum formula for expectation, E[X] equals sum_{k=0}^N P(X > k). Drawing k socks of distinct colors is equivalent to selecting k distinct colors and 1 sock from each, whose combinatorial count is precisely the coefficient of x^k in the generating function prod_{i=1}^N (1 + A_i x).

## 3. Step-by-Step Algorithm
1. 1. Set up the linear factors (1 + A_i x) for each color i.
2. 2. Compute the polynomial product prod_{i=1}^N (1 + A_i x) using Divide and Conquer with NTT in O(N log^2 N) time.
3. 3. Precompute combinations C(S, k) modulo 998244353 using running falling factorials.
4. 4. For each k from 0 to N, compute P(X > k) = c_k * C(S, k)^(-1) mod 998244353.
5. 5. Sum P(X > k) over all k = 0 to N and print the answer.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log^2 N)`
- **Space Complexity**: `O(N)`

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

void ntt(vector<ll>& a, bool invert) {
    int n = a.size();
    for (int i = 1, j = 0; i < n; i++) {
        int bit = n >> 1;
        for (; j & bit; bit >>= 1) j ^= bit;
        j ^= bit;
        if (i < j) swap(a[i], a[j]);
    }
    for (int len = 2; len <= n; len <<= 1) {
        ll wlen = power(3, (MOD - 1) / len);
        if (invert) wlen = modInverse(wlen);
        for (int i = 0; i < n; i += len) {
            ll w = 1;
            for (int j = 0; j < len / 2; j++) {
                ll u = a[i + j];
                ll v = (a[i + j + len / 2] * w) % MOD;
                a[i + j] = (u + v < MOD ? u + v : u + v - MOD);
                a[i + j + len / 2] = (u - v >= 0 ? u - v : u - v + MOD);
                w = (w * wlen) % MOD;
            }
        }
    }
    if (invert) {
        ll n_inv = modInverse(n);
        for (ll& x : a) x = (x * n_inv) % MOD;
    }
}

vector<ll> multiply(const vector<ll>& a, const vector<ll>& b) {
    int n = 1;
    while (n < (int)(a.size() + b.size())) n <<= 1;
    vector<ll> fa(n, 0), fb(n, 0);
    for (size_t i = 0; i < a.size(); i++) fa[i] = a[i];
    for (size_t i = 0; i < b.size(); i++) fb[i] = b[i];
    ntt(fa, false);
    ntt(fb, false);
    for (int i = 0; i < n; i++) fa[i] = (fa[i] * fb[i]) % MOD;
    ntt(fa, true);
    while (fa.size() > 1 && fa.back() == 0) fa.pop_back();
    return fa;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<ll> a(n);
    ll S = 0;
    for (int i = 0; i < n; i++) {
        cin >> a[i];
        S += a[i];
    }

    auto dnc = [&](auto& self, int l, int r) -> vector<ll> {
        if (l == r) {
            return {1, a[l] % MOD};
        }
        int mid = (l + r) / 2;
        vector<ll> left_p = self(self, l, mid);
        vector<ll> right_p = self(self, mid + 1, r);
        return multiply(left_p, right_p);
    };

    vector<ll> poly = dnc(dnc, 0, n - 1);

    // Precompute factorials for combinations C(S, k)
    // S can be large, but k <= n <= 3e5.
    // C(S, k) = S * (S - 1) * ... * (S - k + 1) / k!
    vector<ll> inv(n + 1, 1), fact_inv(n + 1, 1);
    for (int i = 2; i <= n; i++) {
        inv[i] = (MOD - MOD / i) * inv[MOD % i] % MOD;
        fact_inv[i] = (fact_inv[i - 1] * inv[i]) % MOD;
    }

    ll ans = 0;
    ll num = 1; // S * (S - 1) * ...
    for (int k = 0; k <= n; k++) {
        if (k > 0) {
            ll term = (S - k + 1) % MOD;
            num = (num * term) % MOD;
        }
        ll c_k = (k < (int)poly.size() ? poly[k] : 0);
        if (c_k > 0) {
            ll comb = (num * fact_inv[k]) % MOD;
            ll term = (c_k * modInverse(comb)) % MOD;
            ans = (ans + term) % MOD;
        }
    }

    cout << (ans % MOD + MOD) % MOD << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
