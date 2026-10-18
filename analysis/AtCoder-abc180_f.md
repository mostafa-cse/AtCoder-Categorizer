# Problem Analysis: AtCoder-abc180_f — Unbranched

**Problem ID**: `AtCoder-abc180_f`  
**Contest**: `abc180`  
**Rating / Difficulty**: 2419  
**URL**: https://atcoder.jp/contests/abc180/tasks/abc180_f  
**VJudge Tag**: `[problem:AtCoder-abc180_f]`  
**Category File**: [`../categories/combinatorics/max_component_size_paths_cycles_pie.md`](../categories/combinatorics/max_component_size_paths_cycles_pie.md)  

- **Tag (Domain)**: `Combinatorics`  
- **Subtopic**: `Inclusion Exclusion`  
- **Topic (Skill)**: `Principle of Inclusion and Exclusion (PIE)`  

---

## 1. Problem Statement & Key Idea
Count graphs on N labeled vertices and M unlabeled edges where every vertex has degree <= 2 and maximum connected component size is exactly L by subtracting the count for max component size <= L - 1 from the count for max component size <= L.

## 2. Core Observation & Invariant
Degree <= 2 implies every connected component is either an isolated vertex, a simple path, or a cycle (including double edges). By pinning the lowest-indexed remaining vertex to form a component of size s, we avoid overcounting and compute graphs with component size <= K in O(N^2 M) DP.

## 3. Step-by-Step Algorithm
1. 1. Define a helper solve_count(N, M, K) that computes the number of valid graphs with maximum component size <= K.
2. 2. In DP state dp[i][j] (i vertices, j edges remaining), fix the component containing the smallest unchosen vertex.
3. 3. Iterate over the component size s from 1 to min(i, K), choosing the remaining s - 1 vertices in C(i - 1, s - 1) ways.
4. 4. If formed as a path (s - 1 edges), multiply by s! / 2 (or 1 if s == 1); if formed as a cycle (s edges), multiply by (s - 1)! / 2 (or 1 if s == 2).
5. 5. Return (solve_count(N, M, L) - solve_count(N, M, L - 1) + MOD) % MOD.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2 * M)`
- **Space Complexity**: `O(N * M)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

using ll = long long;
const ll MOD = 1e9 + 7;

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

ll solve_count(int N, int M, int K) {
    if (K <= 0) return 0;
    vector<vector<ll>> dp(N + 1, vector<ll>(M + 1, 0));
    dp[0][0] = 1;

    vector<ll> fact(N + 1, 1), ifact(N + 1, 1);
    for (int i = 1; i <= N; i++) fact[i] = (fact[i - 1] * i) % MOD;
    ifact[N] = modInverse(fact[N]);
    for (int i = N - 1; i >= 0; i--) ifact[i] = (ifact[i + 1] * (i + 1)) % MOD;

    auto nCr = [&](int n, int r) -> ll {
        if (r < 0 || r > n) return 0;
        return fact[n] * ifact[r] % MOD * ifact[n - r] % MOD;
    };

    ll inv2 = modInverse(2);

    for (int i = 1; i <= N; i++) {
        for (int j = 0; j <= M; j++) {
            int s_max = min(i, K);
            ll val = 0;
            for (int s = 1; s <= s_max; s++) {
                ll comb = nCr(i - 1, s - 1);
                // Path of size s: s - 1 edges
                if (j >= s - 1) {
                    ll ways_path = (s == 1 ? 1 : fact[s] * inv2 % MOD);
                    val = (val + comb * ways_path % MOD * dp[i - s][j - (s - 1)]) % MOD;
                }
                // Cycle of size s: s edges
                if (s >= 2 && j >= s) {
                    ll ways_cycle = (s == 2 ? 1 : fact[s - 1] * inv2 % MOD);
                    val = (val + comb * ways_cycle % MOD * dp[i - s][j - s]) % MOD;
                }
            }
            dp[i][j] = val;
        }
    }
    return dp[N][M];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M, L;
    if (!(cin >> N >> M >> L)) return 0;

    ll ans = (solve_count(N, M, L) - solve_count(N, M, L - 1) + MOD) % MOD;
    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
