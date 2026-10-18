# Problem Analysis: AtCoder-abc267_h — Ex. Odd Sum

**Problem ID**: `AtCoder-abc267_h`  
**Contest**: `abc267`  
**Rating / Difficulty**: 2422  
**URL**: https://atcoder.jp/contests/abc267/tasks/abc267_h  
**VJudge Tag**: `[problem:AtCoder-abc267_h]`  
**Category File**: [`../categories/math/odd_cardinality_subset_sum_generating_functions_ntt.md`](../categories/math/odd_cardinality_subset_sum_generating_functions_ntt.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Polynomial`  
- **Topic (Skill)**: `Subset Sum Problem using Generating Functions`  

---

## 1. Problem Statement & Key Idea
Count subsets of odd cardinality with sum M by constructing the generating functions P(x) = prod(1 + x^v)^c_v and Q(x) = prod(1 - x^v)^c_v over the small value domain A_i in [1, 10], multiplying via divide-and-conquer NTT, and extracting (P_M - Q_M) / 2 mod 998244353.

## 2. Core Observation & Invariant
Because A_i <= 10, there are only 10 distinct value types. The polynomial for each value v is (1 +- x^v)^c_v, which is sparse and can be evaluated using binomial coefficients up to degree M / v. Multiplying these 10 polynomials via NTT takes O(M log M) time.

## 3. Step-by-Step Algorithm
1. 1. Count the frequencies of each value v in [1, 10].
2. 2. For sign in {+1, -1}, build the polynomial factors sum_{j=0}^{min(c_v, M/v)} C(c_v, j) * sign^j * x^{j * v}.
3. 3. Multiply the 10 polynomials using a priority queue with NTT, truncating polynomials to degree M + 1.
4. 4. Extract P_M = [x^M] P(x) and Q_M = [x^M] Q(x).
5. 5. Return (P_M - Q_M) / 2 modulo 998244353.

## 4. Complexity Analysis
- **Time Complexity**: `O(M log M)`
- **Space Complexity**: `O(M)`

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

vector<ll> multiply(const vector<ll>& a, const vector<ll>& b, int max_len) {
    int n = 1;
    while (n < (int)(a.size() + b.size())) n <<= 1;
    vector<ll> fa(n, 0), fb(n, 0);
    for (size_t i = 0; i < a.size(); i++) fa[i] = a[i];
    for (size_t i = 0; i < b.size(); i++) fb[i] = b[i];
    ntt(fa, false);
    ntt(fb, false);
    for (int i = 0; i < n; i++) fa[i] = (fa[i] * fb[i]) % MOD;
    ntt(fa, true);
    if ((int)fa.size() > max_len) fa.resize(max_len);
    return fa;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, M;
    if (!(cin >> n >> M)) return 0;

    vector<int> counts(11, 0);
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        if (x <= 10) counts[x]++;
    }

    auto get_poly = [&](int sign) -> vector<ll> {
        vector<vector<ll>> polys;
        for (int v = 1; v <= 10; v++) {
            if (counts[v] == 0) continue;
            int limit = min(counts[v], M / v);
            vector<ll> factor(limit * v + 1, 0);
            ll c = 1;
            factor[0] = 1;
            for (int j = 1; j <= limit; j++) {
                c = c * (counts[v] - j + 1) % MOD * modInverse(j) % MOD;
                ll val = c;
                if (sign == -1 && j % 2 == 1) {
                    val = (MOD - val) % MOD;
                }
                factor[j * v] = val;
            }
            polys.push_back(factor);
        }

        if (polys.empty()) return {1};

        auto cmp = [](const vector<ll>& a, const vector<ll>& b) {
            return a.size() > b.size();
        };
        priority_queue<vector<ll>, vector<vector<ll>>, decltype(cmp)> pq(cmp);
        for (auto& p : polys) pq.push(p);

        while (pq.size() > 1) {
            vector<ll> p1 = pq.top(); pq.pop();
            vector<ll> p2 = pq.top(); pq.pop();
            pq.push(multiply(p1, p2, M + 1));
        }

        return pq.top();
    };

    vector<ll> P_poly = get_poly(+1);
    vector<ll> Q_poly = get_poly(-1);

    ll P_M = (M < (int)P_poly.size() ? P_poly[M] : 0);
    ll Q_M = (M < (int)Q_poly.size() ? Q_poly[M] : 0);

    ll inv2 = modInverse(2);
    ll ans = (P_M - Q_M + MOD) % MOD * inv2 % MOD;

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
