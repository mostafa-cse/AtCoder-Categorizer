# Problem Analysis: AtCoder-abc003_3 — AtCoder Programming Course

**Problem ID**: `AtCoder-abc003_3`  
**Contest**: `abc003`  
**Rating / Difficulty**: 824  
**URL**: https://atcoder.jp/contests/abc003/tasks/abc003_3  
**VJudge Tag**: `[problem:AtCoder-abc003_3]`  
**Category File**: [`../categories/basics/greedy_sorting_recurrence.md`](../categories/basics/greedy_sorting_recurrence.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Greedy`  
- **Topic (Skill)**: `Greedy Sorting on Floating Point Recurrence`  

---

## 1. Problem Statement & Key Idea
Choose K videos out of N with ratings R_1, ..., R_N. Starting from rating 0, watching a video with rating R updates your rating to (current + R) / 2. Maximize the final rating.

**Key Idea**: If we select K videos and watch them in order R_(1), ..., R_(K), the final rating is sum_{i=1}^K R_(i) / 2^(K - i + 1). Videos watched later are divided by smaller powers of 2.

## 2. Core Observation & Invariant
To maximize the weighted sum, we must choose the K largest ratings and watch them in strictly ascending order so that the largest values receive the largest coefficients (1/2, 1/4, etc.).

## 3. Step-by-Step Algorithm
1. Sort all N ratings in ascending order.
2. Take the suffix of length K: R[N - K .. N - 1].
3. Initialize rate = 0.0.
4. For each rating r in the suffix, update rate = (rate + r) / 2.0.
5. Print rate with high precision.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<double> r(n);
    for (int i = 0; i < n; ++i) {
        cin >> r[i];
    }

    sort(r.begin(), r.end());

    double rate = 0.0;
    for (int i = n - k; i < n; ++i) {
        rate = (rate + r[i]) / 2.0;
    }

    cout << fixed << setprecision(9) << rate << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Standard editorial method.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Determining optimal greedy order from recurrence expansion weights.
- **Reusable Pattern**: `Ascending order over top-K elements for compounding average updates.`
