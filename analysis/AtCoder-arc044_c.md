# Problem Analysis: AtCoder-arc044_c — C. ビーム

**Problem ID**: `AtCoder-arc044_c`  
**Contest**: `arc044`  
**Rating / Difficulty**: 2309  
**URL**: https://atcoder.jp/contests/arc044/tasks/arc044_c  
**VJudge Tag**: `[problem:AtCoder-arc044_c]`  
**Category File**: [`../categories/dynamic_programming/orthogonal_1d_beam_escape_interval_dp.md`](../categories/dynamic_programming/orthogonal_1d_beam_escape_interval_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Intro to DP`  
- **Topic (Skill)**: `Knapsack and Basic Dynamic Programming`  

---

## 1. Problem Statement & Key Idea
In a $W \times H$ grid with $Q$ horizontal and vertical beams appearing at integer times, find the minimum number of steps to avoid all beams or report -1.

## 2. Core Observation & Invariant
Vertical beams restrict only X coordinates and horizontal beams restrict only Y coordinates, rendering movement costs along X and Y completely decoupled and independent.

## 3. Step-by-Step Algorithm
1. Decompose the problem into two independent 1D problems for $W$ and $H$.
2. In 1D, at each beam event time $t$, contiguous segments of attacked coordinates $[l, r]$ force any occupant to escape to $l-1$ or $r+1$ with distance cost.
3. Maintain $dp[x]$ dynamically, updating boundary positions and invalidating blocked cells in $O((W + H + Q) \log Q)$ time.

## 4. Complexity Analysis
- **Time Complexity**: `O(W + H + Q \log Q)`
- **Space Complexity**: `O(W + H + Q)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

const long long INF = 1e16;

long long solve_1d(int L, const map<int, vector<int>>& events_by_t) {
    vector<long long> dp(L + 1, 0);

    for (const auto& kv : events_by_t) {
        vector<int> pts = kv.second;
        sort(pts.begin(), pts.end());

        vector<pair<int, int>> intervals;
        int cur_l = pts[0], cur_r = pts[0];
        for (size_t i = 1; i < pts.size(); ++i) {
            if (pts[i] == cur_r + 1) {
                cur_r = pts[i];
            } else {
                intervals.push_back({cur_l, cur_r});
                cur_l = cur_r = pts[i];
            }
        }
        intervals.push_back({cur_l, cur_r});

        vector<pair<int, long long>> updates;

        for (auto& iv : intervals) {
            int l = iv.first;
            int r = iv.second;

            long long m1 = INF;
            long long m2 = INF;
            for (int x = l; x <= r; ++x) {
                if (dp[x] < INF) {
                    m1 = min(m1, dp[x] + x);
                    m2 = min(m2, dp[x] - x);
                }
                dp[x] = INF;
            }

            if (l > 1 && m1 < INF) {
                updates.push_back({l - 1, m1 - l + 1});
            }
            if (r < L && m2 < INF) {
                updates.push_back({r + 1, m2 + r + 1});
            }
        }

        for (auto& up : updates) {
            dp[up.first] = min(dp[up.first], up.second);
        }
    }

    long long min_cost = INF;
    for (int x = 1; x <= L; ++x) {
        min_cost = min(min_cost, dp[x]);
    }
    return min_cost;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int W, H, Q;
    if (!(cin >> W >> H >> Q)) return 0;

    map<int, vector<int>> beams_x, beams_y;
    for (int i = 0; i < Q; ++i) {
        int t, d, x;
        cin >> t >> d >> x;
        if (d == 0) {
            beams_x[t].push_back(x);
        } else {
            beams_y[t].push_back(x);
        }
    }

    long long cost_x = solve_1d(W, beams_x);
    long long cost_y = solve_1d(H, beams_y);

    if (cost_x >= INF || cost_y >= INF) {
        cout << -1 << "\n";
    } else {
        cout << cost_x + cost_y << "\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
