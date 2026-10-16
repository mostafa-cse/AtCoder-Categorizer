# Problem Analysis: AtCoder-arc100_a — Linear Approximation

**Problem ID**: `AtCoder-arc100_a`  
**Contest**: `abc102`  
**Rating / Difficulty**: 1089  
**URL**: https://atcoder.jp/contests/abc102/tasks/arc100_a  
**VJudge Tag**: `[problem:AtCoder-arc100_a]`  
**Category File**: [`../categories/math/absolute_deviation_median.md`](../categories/math/absolute_deviation_median.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Median Optimization`  
- **Topic (Skill)**: `1D L1-Norm / Absolute Deviation Median Minimization`  

---

## 1. Problem Statement & Key Idea
Given an array A of N integers. Find an integer b that minimizes sum_{i=1}^N |A_i - (b + i)|.

**Key Idea**: Rewrite the expression by defining C_i = A_i - i. Then the objective is to minimize sum_{i=1}^N |C_i - b|.

## 2. Core Observation & Invariant
The value b that minimizes the sum of absolute deviations sum |C_i - b| is the median of array C! Sort C in ascending order and set b = C[N / 2].

## 3. Step-by-Step Algorithm
1. Compute C[i] = A[i] - (i + 1) for each 0 <= i < N.
2. Sort C in ascending order.
3. Set b = C[N / 2].
4. Compute total = sum_{i=0}^{N-1} |C[i] - b|.
5. Output total.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`

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

    vector<long long> c(n);
    for (int i = 0; i < n; ++i) {
        long long a;
        cin >> a;
        c[i] = a - (i + 1);
    }

    sort(c.begin(), c.end());
    long long b = c[n / 2];

    long long ans = 0;
    for (int i = 0; i < n; ++i) {
        ans += abs(c[i] - b);
    }

    cout << ans << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Minimizing L1 absolute distance by setting the center to the median.
- **Reusable Pattern**: `Min sum |(A[i] - i) - b|: median of (A[i] - i).`
