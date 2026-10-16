# Problem Analysis: AtCoder-typical90_br — Plant Planning

**Problem ID**: `AtCoder-typical90_br`  
**Contest**: `typical90` (Kyopro Typical 90, Problem 070)  
**Rating / Difficulty**: 1200 (★4)  
**URL**: https://atcoder.jp/contests/typical90/tasks/typical90_br  
**VJudge Tag**: `[problem:AtCoder-typical90_br]`  
**Category File**: [`../categories/math/manhattan_median.md`](../categories/math/manhattan_median.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Optimization & Medians`  
- **Topic (Skill)**: `Manhattan Median Principle / Dimension Separation L1 Minimization`  

---

## 1. Problem Statement & Key Idea
Given N factories at coordinates (X_i, Y_i), choose plant location (x, y) to minimize the sum of Manhattan distances: sum (|X_i - x| + |Y_i - y|).

**Core Idea**: The L1 norm separates dimensions: sum |X_i - x| + sum |Y_i - y| can be minimized independently for x and y.

## 2. Core Observation & Invariant
For any 1D set of numbers, sum |X_i - x| is minimized when x is the MEDIAN of {X_1, ..., X_N}!

## 3. Step-by-Step Algorithm
1. Sort X array, choose median x = X[N / 2].
2. Sort Y array, choose median y = Y[N / 2].
3. Sum |X_i - x| + |Y_i - y| over all points.

## 4. Complexity Analysis
Time: O(N log N), Space: O(N).

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> x(n), y(n);
    for (int i = 0; i < n; ++i) {
        cin >> x[i] >> y[i];
    }

    sort(x.begin(), x.end());
    sort(y.begin(), y.end());

    long long med_x = x[n / 2];
    long long med_y = y[n / 2];

    long long total_dist = 0;
    for (int i = 0; i < n; ++i) {
        total_dist += abs(x[i] - med_x) + abs(y[i] - med_y);
    }

    cout << total_dist << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Dimension separation and 1D median minimization.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: L1 metric dimensional independence and the Median Minimization theorem.
- **Reusable Pattern**: `Independent Median Minimization for L1 Metric.`

---
Back to [Manhattan Median Principle / Dimension Separation L1 Minimization](../categories/math/manhattan_median.md) | [Categories Directory](../categories/README.md)