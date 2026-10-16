# Problem Analysis: AtCoder-arc073_b — Simple Knapsack

**Problem ID**: `AtCoder-arc073_b`  
**Contest**: `abc060`  
**Rating / Difficulty**: 1477  
**URL**: https://atcoder.jp/contests/abc060/tasks/arc073_b  
**VJudge Tag**: `[problem:AtCoder-arc073_b]`  
**Category File**: [`../categories/dp/knapsack_small_weight_variance.md`](../categories/dp/knapsack_small_weight_variance.md)  

- **Tag (Domain)**: `Dynamic Programming`  
- **Subtopic**: `Classic DP`  
- **Topic (Skill)**: `Knapsack with Small Weight Variance [W, W+3]`  

---

## 1. Problem Statement & Key Idea
Knapsack problem with N items (N <= 100), capacity W <= 10^9, but with the guarantee that all item weights w_i satisfy w_1 <= w_i <= w_1 + 3.

**Key Insight**: Partition items into 4 groups by offset d = w_i - w_1 in {0, 1, 2, 3}. Sort each group by value descending, and iterate over how many items are selected from each group.

## 2. Core Observation & Invariant
Because values are positive, if we select c_d items from group d, it is always optimal to pick the c_d items with the highest values. Enumerating counts (c0, c1, c2, c3) yields at most (N/4)^4 ~ 4 * 10^5 states.

## 3. Step-by-Step Algorithm
1. Partition items into groups g[0], g[1], g[2], g[3] based on w_i - w_1.
2. Sort each group descending and compute prefix sums of values.
3. max_val = 0.
4. Iterate c0 from 0 to |g[0]|:
5.   Iterate c1 from 0 to |g[1]|:
6.     Iterate c2 from 0 to |g[2]|:
7.       Iterate c3 from 0 to |g[3]|:
8.         total_weight = (c0 + c1 + c2 + c3) * w1 + 0*c0 + 1*c1 + 2*c2 + 3*c3.
9.         If total_weight <= W:
10.           max_val = max(max_val, pref0[c0] + pref1[c1] + pref2[c2] + pref3[c3]).
11. Print max_val.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^4)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long W;
    if (!(cin >> n >> W)) return 0;

    long long w1;
    vector<long long> g[4];

    for (int i = 0; i < n; ++i) {
        long long w, v;
        cin >> w >> v;
        if (i == 0) w1 = w;
        g[w - w1].push_back(v);
    }

    for (int d = 0; d < 4; ++d) {
        sort(g[d].rbegin(), g[d].rend());
    }

    vector<long long> pref[4];
    for (int d = 0; d < 4; ++d) {
        pref[d].resize(g[d].size() + 1, 0);
        for (size_t i = 0; i < g[d].size(); ++i) {
            pref[d][i + 1] = pref[d][i] + g[d][i];
        }
    }

    long long ans = 0;

    for (size_t c0 = 0; c0 <= g[0].size(); ++c0) {
        for (size_t c1 = 0; c1 <= g[1].size(); ++c1) {
            for (size_t c2 = 0; c2 <= g[2].size(); ++c2) {
                for (size_t c3 = 0; c3 <= g[3].size(); ++c3) {
                    long long total_items = c0 + c1 + c2 + c3;
                    long long total_weight = total_items * w1 + 1 * c1 + 2 * c2 + 3 * c3;
                    if (total_weight <= W) {
                        ans = max(ans, pref[0][c0] + pref[1][c1] + pref[2][c2] + pref[3][c3]);
                    }
                }
            }
        }
    }

    cout << ans << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Exploiting narrow item parameter distributions to replace pseudopolynomial DP with brute-force count tuples.
- **Reusable Pattern**: `Small Variance Knapsack: group by w_i - w_1, sort descending, brute-force count tuples.`
