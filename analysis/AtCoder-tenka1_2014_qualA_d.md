# Problem Analysis: AtCoder-tenka1_2014_qualA_d — D. 秘密結社

**Problem ID**: `AtCoder-tenka1_2014_qualA_d`  
**Contest**: `tenka1_2014_qualA`  
**Rating / Difficulty**: 2341  
**URL**: https://atcoder.jp/contests/tenka1_2014_qualA/tasks/tenka1_2014_qualA_d  
**VJudge Tag**: `[problem:AtCoder-tenka1_2014_qualA_d]`  
**Category File**: [`../categories/geometry/radial_sweep_circular_stabbing.md`](../categories/geometry/radial_sweep_circular_stabbing.md)  

- **Tag (Domain)**: `Geometry`  
- **Subtopic**: `Sweep Line`  
- **Topic (Skill)**: `Sweep Line Algorithm and Radial Sweep`  

---

## 1. Problem Statement & Key Idea
Line obstacles subtend angular intervals on the circle. Fixing the rightmost endpoint of an obstacle as the first ray reduces the circular stabbing problem to linear greedy interval stabbing in $O(N^2 \log N)$.

## 2. Core Observation & Invariant
Each obstacle line segment subtends an angular interval $[L_i, R_i]$ from the origin on the circle $S^1$. In an optimal stabbing ray set, at least one ray can be assumed to pass through the right endpoint $R_k$ of some obstacle without loss of generality. Cutting the circle at this ray reduces the remaining obstacles to a linear greedy interval stabbing problem on $[R_k, R_k + 2\pi)$.

## 3. Step-by-Step Algorithm
1. Transform each 2D segment into its subtended angle interval $[L_i, R_i]$ using $\text{atan2}$.
2. Iterate over all $N$ right endpoints as the fixed first ray.
3. Filter out intervals already stabbed by this ray, and solve the remaining 1D greedy interval scheduling/stabbing by sorting remaining intervals by right endpoint in $O(N \log N)$, taking $O(N^2 \log N)$ total time.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2 \log N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

const double PI = acos(-1.0);

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    struct Interval {
        double l, r;
    };

    vector<Interval> intervals(n);
    for (int i = 0; i < n; ++i) {
        double x1, y1, x2, y2;
        cin >> x1 >> y1 >> x2 >> y2;
        double a1 = atan2(y1, x1);
        double a2 = atan2(y2, x2);
        double diff = a2 - a1;
        while (diff <= -PI) diff += 2 * PI;
        while (diff > PI) diff -= 2 * PI;
        if (diff < 0) {
            swap(a1, a2);
            diff = -diff;
        }
        a1 = fmod(a1, 2 * PI);
        if (a1 < 0) a1 += 2 * PI;
        intervals[i] = {a1, a1 + diff};
    }

    int ans = n;
    for (int start_idx = 0; start_idx < n; ++start_idx) {
        double first_ray = intervals[start_idx].r;
        vector<pair<double, double>> lin;
        for (int i = 0; i < n; ++i) {
            double nl = fmod(intervals[i].l - first_ray, 2 * PI);
            if (nl < 0) nl += 2 * PI;
            double nr = nl + (intervals[i].r - intervals[i].l);
            if (nr >= 2 * PI || nl <= 1e-9) {
                // covered by first_ray
                continue;
            }
            lin.push_back({nl, nr});
        }

        sort(lin.begin(), lin.end(), [](const pair<double, double>& a, const pair<double, double>& b) {
            return a.second < b.second;
        });

        int cur_rays = 1;
        double last_ray = -1.0;
        for (auto& item : lin) {
            if (item.first > last_ray + 1e-9) {
                cur_rays++;
                last_ray = item.second;
            }
        }
        ans = min(ans, cur_rays);
    }

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
