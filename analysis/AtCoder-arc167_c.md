# Problem Analysis: AtCoder-arc167_c — C. MST on Line++

**Problem ID**: `AtCoder-arc167_c`  
**Contest**: `arc167`  
**Rating / Difficulty**: 2388  
**URL**: https://atcoder.jp/contests/arc167/tasks/arc167_c  
**VJudge Tag**: `[problem:AtCoder-arc167_c]`  
**Category File**: [`../categories/combinatorics/kruskal_mst_line_gap_stars_and_bars.md`](../categories/combinatorics/kruskal_mst_line_gap_stars_and_bars.md)  

- **Tag (Domain)**: `Combinatorics`  
- **Subtopic**: `Techniques`  
- **Topic (Skill)**: `Contribution Technique`  

---

## 1. Problem Statement & Key Idea
Represent MST weight as sum of (A_{v+1} - A_v) (c(v) - 1). For vertices placed on a line, components using edges of span <= K correspond to clusters separated by index gaps > K. Linearity of expectation and stars-and-bars evaluate the total weight in O(N log N) time.

## 2. Core Observation & Invariant
In Kruskal's algorithm on the line with edges between |i - j| <= K, sorting A allows computing the MST weight as sum_{v=1}^{N-1} (A_{v+1} - A_v) (c(v) - 1) + A_1 (N - 1), where c(v) is the number of connected components formed by vertices with values <= A_v. The number of gaps between consecutive placed vertices exceeding K follows hypergeometric/stars-and-bars counting, with probability C(N-K, v)/C(N, v) per gap.

## 3. Step-by-Step Algorithm
1. Sort A in ascending order. Base contribution is A[0] * (N - 1) * N!.
2. For each cut v from 1 to N-1, the number of connected components minus 1 is (N - v) + sum of indicator variables for whether adjacent elements in the sorted prefix have index difference > K.
3. Over all N! permutations, the expected number of gaps exceeding K is (v - 1) * C(N-K, v) / C(N, v).
4. Multiply by (A[v] - A[v-1]) * N! and accumulate in O(N log N) total time.

## 4. Complexity Analysis
- **Time Complexity**: `O(N \log N)`
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

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N;
    ll K;
    if (!(cin >> N >> K)) return 0;
    vector<ll> A(N);
    for (int i = 0; i < N; i++) cin >> A[i];
    sort(A.begin(), A.end());

    vector<ll> fact(N + 1, 1), ifact(N + 1, 1);
    for (int i = 1; i <= N; i++) fact[i] = (fact[i - 1] * i) % MOD;
    ifact[N] = modInverse(fact[N]);
    for (int i = N - 1; i >= 0; i--) ifact[i] = (ifact[i + 1] * (i + 1)) % MOD;

    auto nCr = [&](int n, int r) -> ll {
        if (r < 0 || r > n) return 0;
        return fact[n] * ifact[r] % MOD * ifact[n - r] % MOD;
    };

    ll ans = 0;
    // Base weight A[0] * (N - 1) * N!
    ans = (ans + A[0] % MOD * (N - 1) % MOD * fact[N]) % MOD;

    for (int v = 1; v < N; v++) {
        ll term = ((ll)(N - v) * fact[N]) % MOD;
        if (v - 1 > 0 && N - K >= v) {
            ll add_val = (ll)(v - 1) * nCr(N - K, v) % MOD * fact[v] % MOD * fact[N - v] % MOD;
            term = (term + add_val) % MOD;
        }
        ll diff = (A[v] - A[v - 1]) % MOD;
        ans = (ans + diff * term) % MOD;
    }

    cout << (ans % MOD + MOD) % MOD << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
