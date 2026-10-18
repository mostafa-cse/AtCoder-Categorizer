# Problem Analysis: AtCoder-abc282_g — Similar Permutation

**Problem ID**: `AtCoder-abc282_g`  
**Contest**: `abc282`  
**Rating / Difficulty**: 2412  
**URL**: https://atcoder.jp/contests/abc282/tasks/abc282_g  
**VJudge Tag**: `[problem:AtCoder-abc282_g]`  
**Category File**: [`../categories/basics/permutation_similarity_insertion_2d_prefix_sum_dp.md`](../categories/basics/permutation_similarity_insertion_2d_prefix_sum_dp.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `2D Prefix Sum`  
- **Topic (Skill)**: `2D Prefix Sum`  

---

## 1. Problem Statement & Key Idea
Count pairs of permutations (A, B) of length N with similarity K (matching direction of adjacent steps) by inserting elements 1 to N, maintaining relative ranks of the latest elements, and optimizing rectangular quadrant transitions via 2D prefix sums in O(N^4).

## 2. Core Observation & Invariant
When inserting element i into permutation prefixes of length i-1 at relative ranks j and l, the relation between the previous element and the new element depends solely on whether the old element's rank was < or >= the new element's rank. This decomposes the transitions into 4 independent 2D rectangular subgrids that update similarity by +1 or +0.

## 3. Step-by-Step Algorithm
1. 1. Initialize dp[0][1][1] = 1 for the base prefix of length 1.
2. 2. For each length i from 2 to N, precompute 2D prefix sums of dp[s] for all valid similarities s.
3. 3. For each candidate rank pair (j, l) in [1, i] x [1, i], evaluate the 4 quadrant subrectangle sums in O(1) time.
4. 4. Quadrants where both permutations step in the same direction transition from similarity s - 1; discordant quadrants transition from similarity s.
5. 5. Sum the values of dp[K][j][l] over all final ranks j, l in [1, N] modulo P.

## 4. Complexity Analysis
- **Time Complexity**: `O(K * N^3) <= O(N^4)`
- **Space Complexity**: `O(K * N^2)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, K;
    ll P;
    if (!(cin >> N >> K >> P)) return 0;

    // dp[s][j][l]: current permutation length i
    // s in [0, min(K, i - 1)]
    // j in [1, i], l in [1, i]
    vector<vector<vector<ll>>> dp(1, vector<vector<ll>>(2, vector<ll>(2, 0)));
    dp[0][1][1] = 1;

    for (int i = 2; i <= N; i++) {
        int max_s = min(K, i - 1);
        vector<vector<vector<ll>>> new_dp(max_s + 1, vector<vector<ll>>(i + 1, vector<ll>(i + 1, 0)));

        int prev_s_max = min(K, i - 2);
        // Precompute 2D prefix sums for each s in [0, prev_s_max]
        vector<vector<vector<ll>>> pref(prev_s_max + 1, vector<vector<ll>>(i, vector<ll>(i, 0)));
        for (int s = 0; s <= prev_s_max; s++) {
            for (int r = 1; r <= i - 1; r++) {
                for (int c = 1; c <= i - 1; c++) {
                    ll val = dp[s][r][c];
                    pref[s][r][c] = (val + pref[s][r - 1][c] + pref[s][r][c - 1] - pref[s][r - 1][c - 1] + P) % P;
                }
            }
        }

        auto rect = [&](int s, int r1, int c1, int r2, int c2) -> ll {
            if (s < 0 || s > prev_s_max) return 0;
            if (r1 > r2 || c1 > c2) return 0;
            ll res = pref[s][r2][c2] - pref[s][r1 - 1][c2] - pref[s][r2][c1 - 1] + pref[s][r1 - 1][c1 - 1];
            res %= P;
            if (res < 0) res += P;
            return res;
        };

        for (int j = 1; j <= i; j++) {
            for (int l = 1; l <= i; l++) {
                for (int s = 0; s <= max_s; s++) {
                    ll ways = 0;
                    if (s > 0) {
                        ll q1 = rect(s - 1, 1, 1, j - 1, l - 1);
                        ll q2 = rect(s - 1, j, l, i - 1, i - 1);
                        ways = (ways + q1 + q2) % P;
                    }
                    if (s <= prev_s_max) {
                        ll q3 = rect(s, 1, l, j - 1, i - 1);
                        ll q4 = rect(s, j, 1, i - 1, l - 1);
                        ways = (ways + q3 + q4) % P;
                    }
                    new_dp[s][j][l] = ways;
                }
            }
        }

        dp = move(new_dp);
    }

    ll ans = 0;
    if (K < (int)dp.size()) {
        for (int r = 1; r <= N; r++) {
            for (int c = 1; c <= N; c++) {
                ans = (ans + dp[K][r][c]) % P;
            }
        }
    }

    cout << (ans % P + P) % P << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
