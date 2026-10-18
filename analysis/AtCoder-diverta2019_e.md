# Problem Analysis: AtCoder-diverta2019_e — XOR Partitioning

**Problem ID**: `AtCoder-diverta2019_e`  
**Contest**: `diverta2019`  
**Rating / Difficulty**: 2423  
**URL**: https://atcoder.jp/contests/diverta2019/tasks/diverta2019_e  
**VJudge Tag**: `[problem:AtCoder-diverta2019_e]`  
**Category File**: [`../categories/basics/equal_xor_partitioning_prefix_xor_transition.md`](../categories/basics/equal_xor_partitioning_prefix_xor_transition.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Range Queries Without Updates`  
- **Topic (Skill)**: `Prefix XOR`  

---

## 1. Problem Statement & Key Idea
Partition array into segments of equal XOR beauty by analyzing prefix XOR values: if total XOR S != 0, prefix XORs must alternate between S and 0; if total XOR S == 0, either all parts are 0 (2^c subsets) or prefix XORs alternate between X and 0, computable in O(N) using prefix zero counts.

## 2. Core Observation & Invariant
A partition has all segment XORs equal to X if and only if the prefix XOR at cut points strictly alternates between X and 0. For S == 0 and fixed X != 0, multiple zeros between consecutive occurrences of X can be skipped or chosen, multiplying the transition by the number of intervening zeros in O(1) time.

## 3. Step-by-Step Algorithm
1. 1. Compute prefix XOR array P.
2. 2. If P[N] != 0: let S = P[N]. Run a 2-state DP tracking ways ending at an S-cut (dp1) or 0-cut (dp0). The answer is dp0 before the final cut at N.
3. 3. If P[N] == 0: let c be the count of intermediate zeros in P[1..N-1]. Add 2^c for beauty 0.
4. 4. Precompute prefix counts of zeros in P.
5. 5. Group non-zero prefix XOR indices by value X. For each X, iterate through its occurrence list, jumping across intermediate zeros in O(1) to accumulate valid alternating cuts.
6. 6. Output the total modulo 10^9 + 7.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

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

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<ll> a(n);
    vector<ll> p(n + 1, 0);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
        p[i + 1] = p[i] ^ a[i];
    }

    if (p[n] != 0) {
        ll S = p[n];
        ll dp0 = 1, dp1 = 0;
        for (int i = 1; i < n; i++) {
            if (p[i] == S) {
                dp1 = (dp1 + dp0) % MOD;
            } else if (p[i] == 0) {
                dp0 = (dp0 + dp1) % MOD;
            }
        }
        cout << dp0 << "\n";
    } else {
        vector<int> pref_zeros(n + 1, 0);
        int total_zeros = 0;
        for (int i = 1; i < n; i++) {
            pref_zeros[i] = pref_zeros[i - 1] + (p[i] == 0 ? 1 : 0);
            if (p[i] == 0) total_zeros++;
        }

        ll ans = power(2, total_zeros);

        unordered_map<ll, vector<int>> pos;
        for (int i = 1; i < n; i++) {
            if (p[i] != 0) pos[p[i]].push_back(i);
        }

        for (auto& [X, x_list] : pos) {
            ll dpX = 0, dp0 = 0;
            for (size_t idx = 0; idx < x_list.size(); idx++) {
                int cur_x = x_list[idx];
                dpX = (dpX + 1 + dp0) % MOD;
                if (idx + 1 < x_list.size()) {
                    int next_x = x_list[idx + 1];
                    ll num_zeros = pref_zeros[next_x] - pref_zeros[cur_x];
                    dp0 = (dp0 + num_zeros * dpX) % MOD;
                }
            }
            ans = (ans + dpX) % MOD;
        }

        cout << ans << "\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
