# Problem Analysis: AtCoder-abc259_h — Ex. Yet Another Path Counting

**Problem ID**: `AtCoder-abc259_h`  
**Contest**: `abc259`  
**Rating / Difficulty**: 2406  
**URL**: https://atcoder.jp/contests/abc259/tasks/abc259_h  
**VJudge Tag**: `[problem:AtCoder-abc259_h]`  
**Category File**: [`../categories/data_structures/sqrt_decomposition_frequency_grid_path_counting.md`](../categories/data_structures/sqrt_decomposition_frequency_grid_path_counting.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Square Root Decomposition`  
- **Topic (Skill)**: `Basic SQRT Decomposition`  

---

## 1. Problem Statement & Key Idea
Count pairs of grid cells (r1, c1) and (r2, c2) with r1 <= r2, c1 <= c2 having the same color, weighted by the number of monotonic paths binom((r2-r1)+(c2-c1), r2-r1). Balance workload using Square Root Decomposition on color frequencies.

## 2. Core Observation & Invariant
If a color appears <= B times, pairwise binomial calculation takes O(B^2) time. If a color appears > B times, there are at most N^2 / B such heavy colors, and for each we can run a single O(N^2) grid DP.

## 3. Step-by-Step Algorithm
1. 1. Group all cell coordinates by their color.
2. 2. Set threshold B = N. For light colors with count <= B, iterate over all pairs and sum binom(dr + dc, dr).
3. 3. For heavy colors with count > B, initialize dp[r][c] = 1 on matching cells and propagate downward/rightward in O(N^2), then accumulate dp[r][c] at all matching cells.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^3)`
- **Space Complexity**: `O(N^2)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

using ll = long long;
const ll MOD = 998244353;

const int MAXF = 1005;
ll fact[MAXF], ifact[MAXF];

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

void init_fact() {
    fact[0] = 1;
    for (int i = 1; i < MAXF; i++) fact[i] = (fact[i - 1] * i) % MOD;
    ifact[MAXF - 1] = modInverse(fact[MAXF - 1]);
    for (int i = MAXF - 2; i >= 0; i--) ifact[i] = (ifact[i + 1] * (i + 1)) % MOD;
}

ll nCr(int n, int r) {
    if (r < 0 || r > n) return 0;
    return fact[n] * ifact[r] % MOD * ifact[n - r] % MOD;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    init_fact();

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<int>> a(n, vector<int>(n));
    unordered_map<int, vector<pair<int, int>>> cells_by_color;
    cells_by_color.reserve(n * n);

    for (int r = 0; r < n; r++) {
        for (int c = 0; c < n; c++) {
            cin >> a[r][c];
            cells_by_color[a[r][c]].push_back({r, c});
        }
    }

    int B = n;
    ll ans = 0;

    for (auto& [color, cells] : cells_by_color) {
        if ((int)cells.size() <= B) {
            int k = cells.size();
            for (int i = 0; i < k; i++) {
                int r1 = cells[i].first, c1 = cells[i].second;
                for (int j = 0; j < k; j++) {
                    int r2 = cells[j].first, c2 = cells[j].second;
                    if (r1 <= r2 && c1 <= c2) {
                        ans = (ans + nCr((r2 - r1) + (c2 - c1), r2 - r1)) % MOD;
                    }
                }
            }
        } else {
            vector<vector<ll>> dp(n, vector<ll>(n, 0));
            for (auto& p : cells) {
                dp[p.first][p.second] = 1;
            }
            for (int r = 0; r < n; r++) {
                for (int c = 0; c < n; c++) {
                    if (r > 0) dp[r][c] = (dp[r][c] + dp[r - 1][c]) % MOD;
                    if (c > 0) dp[r][c] = (dp[r][c] + dp[r][c - 1]) % MOD;
                }
            }
            for (auto& p : cells) {
                ans = (ans + dp[p.first][p.second]) % MOD;
            }
        }
    }

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
