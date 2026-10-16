# Problem Analysis: AtCoder-abc034_d — Salt Water

**Problem ID**: `AtCoder-abc034_d`  
**Contest**: `abc034`  
**Rating / Difficulty**: 1549  
**URL**: https://atcoder.jp/contests/abc034/tasks/abc034_d  
**VJudge Tag**: `[problem:AtCoder-abc034_d]`  
**Category File**: [`../categories/basics/binary_search_average_fractional_programming.md`](../categories/basics/binary_search_average_fractional_programming.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Binary Search on Answer`  
- **Topic (Skill)**: `Binary Search on Average / Dinkelbach Fractional Programming`  

---

## 1. Problem Statement & Key Idea
Given N beakers of salt water with weight w_i and concentration p_i%. Select exactly K beakers to mix such that the resulting concentration is maximized. Output the maximum concentration.

**Key Insight**: Binary search on target concentration X. A mixture has concentration >= X iff sum_{chosen} w_i * (p_i - X) >= 0.

## 2. Core Observation & Invariant
For a fixed candidate percentage X, calculate the relative gain value v_i = w_i * (p_i - X) for each beaker. Sort values descending and take the sum of the K largest values. If this sum >= 0, target concentration X is achievable.

## 3. Step-by-Step Algorithm
1. Binary search on X in [0.0, 100.0] for 100 iterations.
2. For each iteration with mid X:
3.   Compute v[i] = w[i] * (p[i] - X).
4.   Sort v in descending order.
5.   Sum the top K elements.
6.   If sum >= 0, low = mid; else high = mid.
7. Print low with high precision.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N * 100)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <iomanip>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> w(n);
    vector<double> p(n);

    for (int i = 0; i < n; ++i) {
        cin >> w[i] >> p[i];
    }

    double low = 0.0, high = 100.0;
    for (int iter = 0; iter < 100; ++iter) {
        double mid = (low + high) / 2.0;

        vector<double> gain(n);
        for (int i = 0; i < n; ++i) {
            gain[i] = w[i] * (p[i] - mid);
        }

        sort(gain.rbegin(), gain.rend());

        double top_k_sum = 0;
        for (int i = 0; i < k; ++i) {
            top_k_sum += gain[i];
        }

        if (top_k_sum >= 0) {
            low = mid;
        } else {
            high = mid;
        }
    }

    cout << fixed << setprecision(12) << low << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Fractional programming reduction via binary search on target ratio (Dinkelbach method).
- **Reusable Pattern**: `Maximize Weighted Average: binary search X with check sum of top K w_i*(p_i - X) >= 0.`
