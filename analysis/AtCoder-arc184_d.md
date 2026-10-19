# Problem Analysis: AtCoder-arc184_d — D - Erase Balls 2D

**Problem ID**: `AtCoder-arc184_d`  
**Contest**: `arc184`  
**Rating / Difficulty**: 2804  
**URL**: https://atcoder.jp/contests/arc184/tasks/arc184_d  
**VJudge Tag**: `[problem:AtCoder-arc184_d]`  
**Category File**: [`../categories/dynamic_programming/quadrant_erasure_antichain_grid_dp.md`](../categories/dynamic_programming/quadrant_erasure_antichain_grid_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Dp on Different Structures`  
- **Topic (Skill)**: `DP on Trees and DAGs`  

---

## 1. Problem Statement & Key Idea
Given N balls on a 2D grid with permutation coordinates (X_i, Y_i), any chosen ball k erases all balls in its bottom-left and top-right quadrants. Find the number of distinct subsets of balls that can remain after any sequence of operations modulo 998244353.

## 2. Core Observation & Invariant
Any non-empty remaining set must form an antichain (strictly decreasing sequence of Y coordinates when ordered by X). Furthermore, a set is reachable if and only if it is maximal among antichains: no omitted ball between adjacent elements i and j could have survived without being erased by one of the selected balls. By adding sentinel boundary points at (0, N+1) and (N+1, 0), transition from i to j (with i < j, P_i > P_j) is valid if and only if no point k in between has empty rectangular regions (i, k, P_j, P_k) and (k+1, j, P_k+1, P_i). This yields an O(N^3) DP over the DAG of valid transitions.

## 3. Step-by-Step Algorithm
1. 1. Add boundary sentinel points (0, N+1) and (N+1, 0) and sort points by X.
2. 2. Precompute 2D prefix sums for rectangle point counts rect_sum(xl, xr, yl, yr).
3. 3. Define dp[j] as the number of reachable maximal prefixes ending at point j, with dp[0] = 1.
4. 4. For each pair (i, j) with i < j and P_i > P_j, test if transition is maximal: for every intermediate k in (i, j) with P_j < P_k < P_i, verify that either rect_sum(i, k, P_j, P_k) > 0 or rect_sum(k+1, j, P_k+1, P_i) > 0.
5. 5. If maximal, add dp[i] to dp[j] modulo 998244353.
6. 6. Output dp[N+1].

## 4. Complexity Analysis
- **Time Complexity**: `O(N^3)`
- **Space Complexity**: `O(N^2)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 998244353;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> P(n + 2);
    for (int i = 0; i < n; ++i) {
        int x, y;
        cin >> x >> y;
        P[x] = y;
    }
    P[0] = n + 1;
    P[n + 1] = 0;
    n += 2;

    vector<vector<int>> r_cnt(n + 1, vector<int>(n + 1, 0));
    for (int i = 0; i < n; ++i) {
        ++r_cnt[i + 1][P[i] + 1];
    }
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j <= n; ++j) {
            r_cnt[i + 1][j] += r_cnt[i][j];
        }
    }
    for (int i = 0; i <= n; ++i) {
        for (int j = 0; j < n; ++j) {
            r_cnt[i][j + 1] += r_cnt[i][j];
        }
    }

    auto rect_sum = [&](const int xl, const int xr, const int yl, const int yr) {
        return r_cnt[xr][yr] - r_cnt[xr][yl] - r_cnt[xl][yr] + r_cnt[xl][yl];
    };

    vector<long long> dp(n, 0);
    dp[0] = 1;
    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            if (P[i] < P[j]) {
                continue;
            }

            bool is_maximal = true;
            for (int k = i + 1; k < j; ++k) {
                if (P[k] > P[i] || P[k] < P[j]) {
                    continue;
                }
                const int a = rect_sum(i, k, P[j], P[k]);
                const int b = rect_sum(k + 1, j, P[k] + 1, P[i]);
                if (a == 0 && b == 0) {
                    is_maximal = false;
                    break;
                }
            }

            if (is_maximal) {
                dp[j] = (dp[j] + dp[i]) % MOD;
            }
        }
    }

    cout << dp[n - 1] << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
