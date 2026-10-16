# Problem Analysis: AtCoder-arc095_b — Binomial Coefficients

**Problem ID**: `AtCoder-arc095_b`  
**Contest**: `abc094`  
**Rating / Difficulty**: 867  
**URL**: https://atcoder.jp/contests/abc094/tasks/arc095_b  
**VJudge Tag**: `[problem:AtCoder-arc095_b]`  
**Category File**: [`../categories/combinatorics/binomial_coefficient_unimodality.md`](../categories/combinatorics/binomial_coefficient_unimodality.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Combinatorics`  
- **Topic (Skill)**: `Binomial Coefficient Unimodality Maximization`  

---

## 1. Problem Statement & Key Idea
Given n distinct positive integers a_1, ..., a_n. Choose a pair (a_i, a_j) with a_i > a_j that maximizes the binomial coefficient C(a_i, a_j).

**Key Idea**: The sequence C(n, r) for fixed n is unimodal: it increases for r <= n/2, peaks at floor(n/2) and ceil(n/2), and decreases symmetrically for r >= n/2.

## 2. Core Observation & Invariant
C(n, r) is strictly increasing with n. Therefore, a_i must be the maximum element in the entire array: a_i = max(A). To maximize C(a_i, a_j), a_j should be chosen from the remaining elements to minimize |a_j - a_i / 2.0|.

## 3. Step-by-Step Algorithm
1. Find the maximum element in A, let it be max_val.
2. Iterate through all other elements x in A, finding the one that minimizes |x - max_val / 2.0|.
3. Print max_val and the chosen x.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
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

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    sort(a.begin(), a.end());
    long long max_val = a[n - 1];

    long long best_r = a[0];
    double target = max_val / 2.0;

    for (int i = 0; i < n - 1; ++i) {
        if (abs(a[i] - target) < abs(best_r - target)) {
            best_r = a[i];
        }
    }

    cout << max_val << " " << best_r << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Unimodality properties of Pascal's triangle and binomial coefficients.
- **Reusable Pattern**: `Maximize C(n, r): set n = max(A) and pick r closest to n / 2.`
