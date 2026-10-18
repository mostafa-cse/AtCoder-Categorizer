# Problem Analysis: AtCoder-abc298_g — G. Strawberry War

**Problem ID**: `AtCoder-abc298_g`  
**Contest**: `abc298`  
**Rating / Difficulty**: 2405  
**URL**: https://atcoder.jp/contests/abc298/tasks/abc298_g  
**VJudge Tag**: `[problem:AtCoder-abc298_g]`  
**Category File**: [`../categories/dynamic_programming/grid_range_mcm_subrectangle_split_dp.md`](../categories/dynamic_programming/grid_range_mcm_subrectangle_split_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Classic DP`  
- **Topic (Skill)**: `Interval DP / Range DP / Matrix Chain Multiplication (MCM)`  

---

## 1. Problem Statement & Key Idea
Cut an H x W grid into T+1 rectangular pieces with straight cuts to minimize (max_piece - min_piece). Fix the minimum piece size X from the O(H^2 W^2) possible subrectangle sums and minimize the maximum piece size with range-based 2D MCM DP.

## 2. Core Observation & Invariant
Because H, W <= 6 and T <= 36, the number of distinct subrectangle sums is at most 441. Fixing the lower bound X converts the problem into finding the minimum possible maximum piece sum under the constraint that every cut piece has sum >= X.

## 3. Step-by-Step Algorithm
1. 1. Precompute 2D prefix sums for all subrectangles.
2. 2. Collect and sort all distinct subrectangle sums as candidates for the minimum piece size X.
3. 3. For each candidate X, compute dp(r1, c1, r2, c2, cuts) using memoized DFS: split horizontally or vertically into two subrectangles with k and cuts-1-k cuts respectively.
4. 4. Take the minimum over all valid X of (max_val - X).

## 4. Complexity Analysis
- **Time Complexity**: `O(H^3 W^3 T^2 + |candidates| * H^3 W^3 T)`
- **Space Complexity**: `O(H^2 W^2 T)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

using ll = long long;
const ll INF = 1e18;

ll dp[7][7][7][7][37];
ll pref[7][7];

ll get_sum(int r1, int c1, int r2, int c2) {
    return pref[r2][c2] - pref[r1 - 1][c2] - pref[r2][c1 - 1] + pref[r1 - 1][c1 - 1];
}

ll solve_dp(int r1, int c1, int r2, int c2, int cut, ll X) {
    if (dp[r1][c1][r2][c2][cut] != -1) return dp[r1][c1][r2][c2][cut];
    if (cut == 0) {
        ll s = get_sum(r1, c1, r2, c2);
        if (s < X) return dp[r1][c1][r2][c2][cut] = INF;
        return dp[r1][c1][r2][c2][cut] = s;
    }
    ll res = INF;
    for (int r = r1; r < r2; r++) {
        for (int k = 0; k < cut; k++) {
            ll v1 = solve_dp(r1, c1, r, c2, k, X);
            if (v1 == INF) continue;
            ll v2 = solve_dp(r + 1, c1, r2, c2, cut - 1 - k, X);
            if (v2 == INF) continue;
            res = min(res, max(v1, v2));
        }
    }
    for (int c = c1; c < c2; c++) {
        for (int k = 0; k < cut; k++) {
            ll v1 = solve_dp(r1, c1, r2, c, k, X);
            if (v1 == INF) continue;
            ll v2 = solve_dp(r1, c + 1, r2, c2, cut - 1 - k, X);
            if (v2 == INF) continue;
            res = min(res, max(v1, v2));
        }
    }
    return dp[r1][c1][r2][c2][cut] = res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int H, W, T;
    if (!(cin >> H >> W >> T)) return 0;

    vector<vector<ll>> s(H + 1, vector<ll>(W + 1, 0));
    for (int i = 1; i <= H; i++) {
        for (int j = 1; j <= W; j++) {
            cin >> s[i][j];
            pref[i][j] = s[i][j] + pref[i - 1][j] + pref[i][j - 1] - pref[i - 1][j - 1];
        }
    }

    vector<ll> candidates;
    for (int r1 = 1; r1 <= H; r1++) {
        for (int c1 = 1; c1 <= W; c1++) {
            for (int r2 = r1; r2 <= H; r2++) {
                for (int c2 = c1; c2 <= W; c2++) {
                    candidates.push_back(get_sum(r1, c1, r2, c2));
                }
            }
        }
    }
    sort(candidates.begin(), candidates.end());
    candidates.erase(unique(candidates.begin(), candidates.end()), candidates.end());

    ll ans = INF;
    for (ll X : candidates) {
        memset(dp, -1, sizeof(dp));
        ll max_val = solve_dp(1, 1, H, W, T, X);
        if (max_val < INF) {
            ans = min(ans, max_val - X);
        }
    }

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
