# Problem Analysis: AtCoder-abc023_d — 射撃王

**Problem ID**: `AtCoder-abc023_d`  
**Contest**: `abc023`  
**Rating / Difficulty**: 1843  
**URL**: https://atcoder.jp/contests/abc023/tasks/abc023_d  
**VJudge Tag**: `[problem:AtCoder-abc023_d]`  
**Category File**: [`../categories/basics/binary_search_deadline_verification.md`](../categories/basics/binary_search_deadline_verification.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Binary Search`  
- **Topic (Skill)**: `Binary Search on Answer with Feasibility Deadline Verification`  

---

## 1. Problem Statement & Key Idea
N balloons. Balloon i starts at height H_i and ascends at S_i meters per second. You shoot one balloon per second at times t = 0, 1, ..., N - 1. Minimize the maximum height at which any balloon is shot.

**Key Insight**: Binary search on maximum height X. For height X, balloon i must be shot at time t <= floor((X - H_i) / S_i). This defines an exact deadline for each balloon. The schedule is feasible iff the number of balloons with deadline <= t does not exceed t + 1 for all t.

## 2. Core Observation & Invariant
If X < H_i for any balloon, it is immediately infeasible. Deadline counting can be done in O(N) using frequency buckets or sorting in O(N log N).

## 3. Step-by-Step Algorithm
1. low = min(H_i), high = max(H_i + (N - 1) * S_i), ans = high.
2. While low <= high:
3.   mid = low + (high - low) / 2.
4.   Build deadline counts deadline_cnt[0..N-1].
5.   For each balloon i:
6.     if mid < H_i: infeasible, break.
7.     limit_t = min((long long)N - 1, (mid - H_i) / S_i);
8.     deadline_cnt[limit_t]++;
9.   Verify cumulative count <= t + 1 for all t = 0..N-1.
10.   If feasible: ans = mid, high = mid - 1.
11.   Else: low = mid + 1.
12. Print ans.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log(max_ans))`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Balloon {
    long long h, s;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<Balloon> b(n);
    long long max_h = 0;
    for (int i = 0; i < n; ++i) {
        cin >> b[i].h >> b[i].s;
        max_h = max(max_h, b[i].h + (long long)n * b[i].s);
    }

    auto is_feasible = [&](long long x) -> bool {
        vector<int> count_limit(n, 0);

        for (int i = 0; i < n; ++i) {
            if (x < b[i].h) return false;
            long long t = (x - b[i].h) / b[i].s;
            if (t < n - 1) count_limit[t]++;
            else count_limit[n - 1]++;
        }

        int cum = 0;
        for (int t = 0; t < n; ++t) {
            cum += count_limit[t];
            if (cum > t + 1) return false;
        }
        return true;
    };

    long long low = 1, high = max_h, ans = max_h;
    while (low <= high) {
        long long mid = low + (high - low) / 2;
        if (is_feasible(mid)) {
            ans = mid;
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }

    cout << ans << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Converting maximum value minimization into deadline verification via binary search on answer.
- **Reusable Pattern**: `Binary Search on Max Height: Convert condition H_i + t * S_i <= X into deadline t <= (X - H_i)/S_i.`
