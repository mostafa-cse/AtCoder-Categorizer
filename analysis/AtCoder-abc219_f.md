# Problem Analysis: AtCoder-abc219_f — F. Cleaning Robot

**Problem ID**: `AtCoder-abc219_f`  
**Contest**: `abc219`  
**Rating / Difficulty**: 2542  
**URL**: https://atcoder.jp/contests/abc219/tasks/abc219_f  
**VJudge Tag**: `[problem:AtCoder-abc219_f]`  
**Category File**: [`../categories/miscellaneous/cleaning_robot_1d_interval_merge.md`](../categories/miscellaneous/cleaning_robot_1d_interval_merge.md)  

- **Tag (Domain)**: `Miscellaneous`  
- **Subtopic**: `Techniques`  
- **Topic (Skill)**: `Coordinate Compression`  

---

## 1. Problem Statement & Key Idea
Count distinct grid squares visited by a robot executing move sequence $S$ of length $N$ repeated $K$ times.

## 2. Core Observation & Invariant
Trace 1 cycle to find visited set $P$ and net vector $(\Delta x, \Delta y)$. If $(\Delta x, \Delta y) = (0, 0)$, answer is $|P|$. Otherwise, the trajectory decomposes into parallel 1D lines parameterized by canonical remainder $(r, base_y)$ with $x = q \Delta x + r$. Each point $(x, y) \in P$ generates an interval $[q, q + K - 1]$ along its line. Merging 1D intervals per line computes the exact union.

## 3. Step-by-Step Algorithm
1. 1. Trace a single execution of $S$ and collect unique points $P$.
2. 2. If $(\Delta x, \Delta y) == (0, 0)$, output $|P|$.
3. 3. Normalize vector so $\Delta x > 0$ (or $\Delta x = 0, \Delta y > 0$).
4. 4. Group points into lines $(r, base_y)$ with shift $q = \lfloor x / \Delta x \rfloor$.
5. 5. For each line, collect intervals $[q, q + K - 1]$, sort them, and merge overlapping intervals.
6. 6. Sum merged interval lengths across all lines.

## 4. Complexity Analysis
- **Time Complexity**: `O(|S| \log |S|)`
- **Space Complexity**: `O(|S|)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string s;
    if (!(cin >> s)) return 0;
    long long k;
    if (!(cin >> k)) return 0;

    long long cur_x = 0, cur_y = 0;
    vector<pair<long long, long long>> pts;
    pts.push_back({0, 0});
    for (char c : s) {
        if (c == 'L') cur_x--;
        else if (c == 'R') cur_x++;
        else if (c == 'U') cur_y--;
        else if (c == 'D') cur_y++;
        pts.push_back({cur_x, cur_y});
    }

    sort(pts.begin(), pts.end());
    pts.erase(unique(pts.begin(), pts.end()), pts.end());

    long long dx = cur_x;
    long long dy = cur_y;

    if (dx == 0 && dy == 0) {
        cout << pts.size() << "\n";
        return 0;
    }

    if (dx < 0) {
        dx = -dx;
        for (auto &p : pts) p.first = -p.first;
    }
    if (dx == 0 && dy < 0) {
        dy = -dy;
        for (auto &p : pts) p.second = -p.second;
    }

    auto floor_div = [&](long long a, long long b) -> long long {
        long long res = a / b;
        long long rem = a % b;
        if (rem != 0 && ((a < 0) ^ (b < 0))) res--;
        return res;
    };

    map<pair<long long, long long>, vector<pair<long long, long long>>> lines_map;

    if (dx != 0) {
        for (auto &p : pts) {
            long long q = floor_div(p.first, dx);
            long long r = p.first - q * dx;
            long long base_y = p.second - q * dy;
            lines_map[{r, base_y}].push_back({q, q + k - 1});
        }
    } else {
        for (auto &p : pts) {
            long long q = floor_div(p.second, dy);
            long long r = p.second - q * dy;
            lines_map[{p.first, r}].push_back({q, q + k - 1});
        }
    }

    long long total_cells = 0;
    for (auto &kv : lines_map) {
        auto &intervals = kv.second;
        sort(intervals.begin(), intervals.end());
        long long cur_l = intervals[0].first;
        long long cur_r = intervals[0].second;
        for (size_t i = 1; i < intervals.size(); ++i) {
            long long l = intervals[i].first;
            long long r = intervals[i].second;
            if (l <= cur_r) {
                cur_r = max(cur_r, r);
            } else {
                total_cells += cur_r - cur_l + 1;
                cur_l = l;
                cur_r = r;
            }
        }
        total_cells += cur_r - cur_l + 1;
    }

    cout << total_cells << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
