# Problem Analysis: AtCoder-abc159_e — Dividing Chocolate

**Problem ID**: `AtCoder-abc159_e`  
**Contest**: `abc159`  
**Rating / Difficulty**: 1450  
**URL**: https://atcoder.jp/contests/abc159/tasks/abc159_e  
**VJudge Tag**: `[problem:AtCoder-abc159_e]`  
**Category File**: [`../categories/basics/bitmask_cuts_greedy_sweep.md`](../categories/basics/bitmask_cuts_greedy_sweep.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Bitmask Search`  
- **Topic (Skill)**: `Bitmask Horizontal Cuts with Greedy Vertical Sweeping`  

---

## 1. Problem Statement & Key Idea
An H x W grid of chocolate bar contains white chocolate chips ('0' or '1'). Divide the bar into pieces using horizontal and vertical straight cuts across the entire bar so that each piece contains at most K chips. Minimize the total number of cuts. H <= 10, W <= 1000.

**Key Insight**: Because H <= 10, enumerate all 2^(H-1) subsets of horizontal cuts. For each fixed horizontal cut mask, greedily sweep columns from left to right, making a vertical cut whenever any horizontal slice would exceed K chips.

## 2. Core Observation & Invariant
2^(10 - 1) = 512 horizontal configurations. For each configuration, greedy column sweeping is optimal because deferring vertical cuts is always strictly better.

## 3. Step-by-Step Algorithm
1. Initialize min_cuts = INF.
2. Iterate mask from 0 to (1 << (H - 1)) - 1:
3.   Assign group IDs to rows based on horizontal cuts in mask.
4.   num_groups = count of horizontal slices.
5.   cuts = popcount(mask).
6.   current_sum[num_groups] = 0.
7.   valid = true.
8.   For each column c from 0 to W - 1:
9.     Compute col_sum[g] for each slice g in this column.
10.     If any col_sum[g] > K: valid = false, break.
11.     If any current_sum[g] + col_sum[g] > K:
12.       cuts++; current_sum = col_sum.
13.     Else:
14.       current_sum[g] += col_sum[g] for all g.
15.   If valid, min_cuts = min(min_cuts, cuts).
16. Print min_cuts.

## 4. Complexity Analysis
- **Time Complexity**: `O(2^(H-1) * H * W)`
- **Space Complexity**: `O(H * W)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int h, w, k;
    if (!(cin >> h >> w >> k)) return 0;

    vector<string> s(h);
    for (int i = 0; i < h; ++i) {
        cin >> s[i];
    }

    int ans = 1e9;
    int total_masks = 1 << (h - 1);

    for (int mask = 0; mask < total_masks; ++mask) {
        // Map rows to group indices
        vector<int> group_id(h, 0);
        int g = 0;
        for (int r = 0; r < h - 1; ++r) {
            if (mask & (1 << r)) g++;
            group_id[r + 1] = g;
        }
        int num_groups = g + 1;

        int cuts = __builtin_popcount(mask);
        vector<int> current_chips(num_groups, 0);
        bool valid = true;

        for (int c = 0; c < w; ++c) {
            vector<int> col_chips(num_groups, 0);
            for (int r = 0; r < h; ++r) {
                if (s[r][c] == '1') {
                    col_chips[group_id[r]]++;
                }
            }

            // If a single column exceeds K in any group, this mask is impossible
            for (int i = 0; i < num_groups; ++i) {
                if (col_chips[i] > k) {
                    valid = false;
                    break;
                }
            }
            if (!valid) break;

            // Check if adding this column forces a cut
            bool need_cut = false;
            for (int i = 0; i < num_groups; ++i) {
                if (current_chips[i] + col_chips[i] > k) {
                    need_cut = true;
                    break;
                }
            }

            if (need_cut) {
                cuts++;
                current_chips = col_chips;
            } else {
                for (int i = 0; i < num_groups; ++i) {
                    current_chips[i] += col_chips[i];
                }
            }
        }

        if (valid) {
            ans = min(ans, cuts);
        }
    }

    cout << ans << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Small-dimension bitmask exhaustive search coupled with greedy sweeping along the large dimension.
- **Reusable Pattern**: `2D Grid Cutting: 2^(H-1) horizontal bitmask + greedy vertical column accumulator.`
