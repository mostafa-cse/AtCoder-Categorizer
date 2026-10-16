# Problem Analysis: AtCoder-abc169_e — Count Median

**Problem ID**: `AtCoder-abc169_e`  
**Contest**: `abc169`  
**Rating / Difficulty**: 1353  
**URL**: https://atcoder.jp/contests/abc169/tasks/abc169_e  
**VJudge Tag**: `[problem:AtCoder-abc169_e]`  
**Category File**: [`../categories/math/interval_medians_feasible_range.md`](../categories/math/interval_medians_feasible_range.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Median Optimization`  
- **Topic (Skill)**: `Interval Medians Feasible Range [Min Median, Max Median]`  

---

## 1. Problem Statement & Key Idea
N integers X_1..X_N where each X_i is chosen from integer interval [A_i, B_i]. Find the number of possible distinct values of the median of X_1..X_N.

**Key Idea**: The median achieves its absolute minimum when all X_i = A_i, and its absolute maximum when all X_i = B_i.

## 2. Core Observation & Invariant
Sort A and B independently. (1) If N is odd: the median is an integer. Min median is A[N/2], max median is B[N/2]. Every integer in [min, max] is achievable, giving B[N/2] - A[N/2] + 1 values. (2) If N is even: the median is (X_{N/2 - 1} + X_{N/2}) / 2. Min sum is A[N/2 - 1] + A[N/2], max sum is B[N/2 - 1] + B[N/2]. Every integer sum in between is achievable (each step of 0.5 in median), giving max_sum - min_sum + 1 values.

## 3. Step-by-Step Algorithm
1. Sort array A and array B independently in ascending order.
2. If N is odd: print B[N / 2] - A[N / 2] + 1.
3. If N is even: min_sum = A[N / 2 - 1] + A[N / 2]; max_sum = B[N / 2 - 1] + B[N / 2]; print max_sum - min_sum + 1.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N)`
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
    if (!(cin >> n)) return 0;

    vector<long long> a(n), b(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i] >> b[i];
    }

    sort(a.begin(), a.end());
    sort(b.begin(), b.end());

    if (n % 2 == 1) {
        long long min_med = a[n / 2];
        long long max_med = b[n / 2];
        cout << max_med - min_med + 1 << "\n";
    } else {
        long long min_sum = a[n / 2 - 1] + a[n / 2];
        long long max_sum = b[n / 2 - 1] + b[n / 2];
        cout << max_sum - min_sum + 1 << "\n";
    }

    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Determining the continuous interval of reachable medians across independent component bounds.
- **Reusable Pattern**: `Reachable medians: [median(A), median(B)] is contiguous.`
