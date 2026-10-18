# Problem Analysis: AtCoder-arc073_c — E. Ball Coloring

**Problem ID**: `AtCoder-arc073_c`  
**Contest**: `arc073`  
**Rating / Difficulty**: 2434  
**URL**: https://atcoder.jp/contests/arc073/tasks/arc073_c  
**VJudge Tag**: `[problem:AtCoder-arc073_c]`  
**Category File**: [`../categories/basics/ball_coloring_extremal_two_pointers.md`](../categories/basics/ball_coloring_extremal_two_pointers.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Leveraging Monotonicity`  
- **Topic (Skill)**: `Two Pointers`  

---

## 1. Problem Statement & Key Idea
Each bag has two balls $(x_i, y_i)$. We paint one red and the other blue to minimize $(R_{max} - R_{min}) \times (B_{max} - B_{min})$. In Case 1, global minimum and global maximum are different colors: assigning the smaller of each bag to Red and larger to Blue is optimal. In Case 2, global minimum and maximum are the same color (say Red), so $R_{max} - R_{min} = ALL_{max} - ALL_{min}$ is fixed, and the remaining balls in Blue must contain exactly one ball from each bag, which is solved by sliding a two-pointer window over the sorted $2N$ values.

## 2. Core Observation & Invariant
Because every bag contributes one ball to Blue, finding the minimum range $[L, R]$ covering at least one ball from each bag is an exact equivalent to the shortest subarray containing all $N$ colors. Two pointers in $O(N \log N)$ over the $2N$ sorted values determines the optimal interval.

## 3. Step-by-Step Algorithm
1. 1. Identify the global minimum $ALL_{min}$ and maximum $ALL_{max}$ across all $2N$ balls.
2. 2. Evaluate Case 1 where $ALL_{min}$ is Red and $ALL_{max}$ is Blue: $R_{max} = \max_i \min(x_i, y_i)$ and $B_{min} = \min_i \max(x_i, y_i)$.
3. 3. Evaluate Case 2 where $ALL_{min}$ and $ALL_{max}$ are both Red: create $2N$ events $(v, \text{bag\_id})$ and sort by value.
4. 4. Maintain a sliding window $[l, r]$ containing at least one ball from every bag using two pointers and frequency counts.
5. 5. Output the minimum of Case 1 and Case 2 products.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<pair<long long, long long>> bags(n);
    long long all_min = 2e18, all_max = -2e18;
    long long r_max1 = -2e18, b_min1 = 2e18;

    for (int i = 0; i < n; ++i) {
        long long x, y;
        cin >> x >> y;
        if (x > y) swap(x, y);
        bags[i] = {x, y};
        all_min = min(all_min, x);
        all_max = max(all_max, y);
        r_max1 = max(r_max1, x);
        b_min1 = min(b_min1, y);
    }

    long long ans1 = (r_max1 - all_min) * (all_max - b_min1);

    vector<pair<long long, int>> events;
    events.reserve(2 * n);
    for (int i = 0; i < n; ++i) {
        events.push_back({bags[i].first, i});
        events.push_back({bags[i].second, i});
    }
    sort(events.begin(), events.end());

    vector<int> cnt(n, 0);
    int distinct = 0;
    int r = 0;
    long long min_diff = 2e18;

    for (int l = 0; l < 2 * n; ++l) {
        while (r < 2 * n && distinct < n) {
            int bag = events[r].second;
            if (cnt[bag] == 0) distinct++;
            cnt[bag]++;
            r++;
        }
        if (distinct == n) {
            min_diff = min(min_diff, events[r - 1].first - events[l].first);
        }
        int l_bag = events[l].second;
        cnt[l_bag]--;
        if (cnt[l_bag] == 0) distinct--;
    }

    long long ans2 = min_diff * (all_max - all_min);
    cout << min(ans1, ans2) << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
